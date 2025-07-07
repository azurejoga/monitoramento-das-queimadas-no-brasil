# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b67de7f5-8e4f-34eb-ab6b-5ae82d97b4a4 | -12.01762 | -47.77945 | 2025-07-07 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dadc90c-75e1-3c42-81e0-248d3cf577fc | -7.38928 | -46.82725 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d7485f6-d1ac-3994-8727-967233815729 | -8.33103 | -49.18795 | 2025-07-07 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6b41432-375a-3be0-9e12-9037d3baebd0 | -11.49987 | -48.07752 | 2025-07-07 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baf71a96-aa93-34f7-aea5-774f41aa30f4 | -7.69405 | -44.58593 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7ea4007d-1bb8-3b8b-a7f5-6d5ff51008e0 | -7.82559 | -44.18826 | 2025-07-07 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffb46174-f16d-3d9b-84f9-0346173ef7db | -7.69034 | -44.58538 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 97338ba1-1043-3659-ab93-c857f7eec78a | -13.02149 | -46.77259 | 2025-07-07 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b022c5e-aa92-3110-8596-393511d94560 | -7.6897 | -44.58974 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| de54fca6-962c-3cd2-8f58-86dee112a4ed | -10.57506 | -49.13392 | 2025-07-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2137b7c9-05ee-3f82-a61e-348d61fcd6ff | -12.03003 | -57.08017 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fd16ec3-06fe-3542-95aa-4c270f6b3941 | -12.02525 | -57.07925 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d712140f-35b4-3bdf-beff-4a8d60f8f578 | -8.14174 | -47.16934 | 2025-07-07 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb5ba7d-dc8b-36f1-986c-7da2ad91e0ab | -8.71485 | -50.00422 | 2025-07-07 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b01fc95e-98a4-3760-89e0-eae2293cecae | -7.27482 | -44.61531 | 2025-07-07 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65f07085-6970-3126-ace5-f65bc336e622 | -7.62633 | -45.36449 | 2025-07-07 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65589742-a7af-34dc-8d4b-8cc723083df6 | -14.03445 | -46.24971 | 2025-07-07 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad4d7918-cc35-3665-b709-dd44bd3daf7d | -7.69164 | -44.57653 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 94d79a95-fb06-37be-88aa-4a2711d41ec9 | -8.13839 | -47.16879 | 2025-07-07 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1591637-02f1-352a-bea0-970a0d4ce6c3 | -7.69971 | -44.57322 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2714114-5f36-3b56-be25-df3206b584dd | -7.696 | -44.57266 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b3938d0-4a3c-3f2b-8fb0-2dd500056dd7 | -9.19611 | -45.3352 | 2025-07-07 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 610050ab-f764-399d-b05e-c523cf17effd | -10.63836 | -46.37932 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1de77fb9-9a5a-3a26-bb5e-67dfebe9e4ff | -10.50794 | -51.87872 | 2025-07-07 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1452c5b-7629-3852-80c1-7c0a13b0d351 | -7.26894 | -44.65487 | 2025-07-07 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22d4c440-ce3a-3313-b09b-03c0a05b6459 | -7.71086 | -44.57484 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a734b08c-5f8d-37a7-a29b-bc1acf97970d | -12.75301 | -44.416 | 2025-07-07 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac6c72cb-2624-3544-a4dc-c4d6b9506960 | -10.65295 | -46.37759 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90be94e9-459d-3d0c-91b1-1870758c2649 | -7.68663 | -44.58482 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f520f271-2efd-3ab3-9600-3b34627245a3 | -10.63729 | -46.3802 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e86f8639-18cc-3a5a-b655-63431e154b54 | -12.02908 | -57.08543 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20d52c5d-de57-3dde-aa69-5465fc9ced8a | -7.69842 | -44.58204 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daf860a1-78bd-3f25-adc4-ac476086a2da | -10.9541 | -49.25253 | 2025-07-07 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf302e5a-e343-36cc-8b81-b76f3bec8483 | -11.32405 | -51.44376 | 2025-07-07 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ef0214d-e2b7-3d01-abc5-22e8bd265f10 | -7.71151 | -44.57047 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b36dd3b-2192-393b-9ca9-5bd0bcf7ba4b | -7.69535 | -44.57709 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 51400fd2-24e0-33b4-be0d-11a2b800d928 | -12.0262 | -57.07402 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6085427a-0275-369f-ac3c-423ef3045e49 | -12.02567 | -57.07584 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3bedf295-5d4a-351d-ae72-2fc55fc49287 | -7.66834 | -44.36266 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ce6b78b4-67eb-357a-a9af-51874eddc4cd | -13.65155 | -46.81442 | 2025-07-07 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4df515a7-d80b-3207-b7d7-343cd9c0cd0b | -10.58332 | -49.1245 | 2025-07-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7d4110c-9b0f-3ae5-adb5-4bd72c33d284 | -9.19973 | -45.33574 | 2025-07-07 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8fcc7c7-8bac-3c29-834d-b981cd72464c | -8.06028 | -43.11813 | 2025-07-07 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| fb110f31-9dc9-3343-a097-9cef4e74ff9c | -7.71458 | -44.57537 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbe3b009-daa0-3a8a-acde-653f1b25457a | -13.01912 | -46.76414 | 2025-07-07 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 376e6eb8-8a02-3ab7-b439-279ca8c18b04 | -10.67117 | -56.54507 | 2025-07-07 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32f18275-a55f-36e1-b0ea-8818503c78aa | -9.5805 | -57.39832 | 2025-07-07 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1cd72ee-4f62-341c-850d-b1baaf6c54b9 | -10.24375 | -46.80451 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 771735d8-1963-38ff-a1b5-d68608fac393 | -7.44672 | -46.78024 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46b56e90-8088-3ac6-82b4-a401bdfc6e05 | -14.12898 | -51.29675 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57aff048-a2a7-3dd6-bb58-db7e93a7b8f2 | -17.0236 | -48.02474 | 2025-07-07 04:36:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 024610d9-93c3-3416-bec3-8371fb5ee05c | -16.32616 | -43.62025 | 2025-07-07 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 949c0d4b-f7f3-3f9d-a1d2-9f0e3a1952d2 | -13.78729 | -53.40332 | 2025-07-07 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ee6f172-7dd0-3868-8744-36bc554e6a6d | -16.2777 | -47.55095 | 2025-07-07 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7b5108a-69ae-391f-afb6-747c2c4c4964 | -14.13391 | -51.30898 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c77ed51-c447-36d4-b5ba-cf92d1544dfa | -15.80445 | -47.65231 | 2025-07-07 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5151867-9428-3bbf-876a-d6c427df6e2e | -16.68302 | -43.88485 | 2025-07-07 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29b5f220-7135-39fa-8577-d1edef0153a8 | -14.07903 | -54.52089 | 2025-07-07 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10e8e91e-1112-3afe-bf35-f111d8180e6a | -14.12717 | -51.30784 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50a22682-fa64-3d81-9c05-7cdf3181548f | -14.63367 | -48.14508 | 2025-07-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 894dcc65-efe8-30ee-a56d-606bd8940a4e | -14.13512 | -51.30159 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ea5e6a1-043d-34eb-b168-93a3ae360d1c | -14.63028 | -48.14455 | 2025-07-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45f2b72e-2aa9-3460-a89a-9ae39efdf191 | -20.76556 | -46.76805 | 2025-07-07 04:36:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 686732a9-346b-35ab-b980-6d73aed7994a | -17.7044 | -46.28912 | 2025-07-07 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8fcd4ff-3141-3849-a444-b278bc3a0e49 | -15.85371 | -48.10968 | 2025-07-07 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e83df5c0-8c16-3d9c-93cd-dda8a7f59333 | -14.13175 | -51.30102 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9527024-c42d-31cd-a351-4b8f4ff6f330 | -14.12501 | -51.29987 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f15ce22-ca17-35be-a99e-549c10d9665e | -19.71968 | -40.35341 | 2025-07-07 04:36:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 464575da-f91e-3d49-a1f1-8244ac29105a | -14.63422 | -48.14135 | 2025-07-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18dd1a9d-f619-318e-994c-cc509cf7d120 | -14.12379 | -51.30726 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e694d9ad-532d-3053-bfa9-f0de9d0417a6 | -16.28006 | -47.55963 | 2025-07-07 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14548963-9023-3644-a8ee-4409e450eac2 | -17.17357 | -42.83736 | 2025-07-07 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e0cd589-f7b0-3804-813f-dc596acc6685 | -16.27128 | -47.57064 | 2025-07-07 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| badca5ed-0919-355f-8015-655bcd659069 | -16.67171 | -49.29872 | 2025-07-07 04:36:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ea0f292-6f0a-3c5a-8c48-4c10a4b5dfbf | -15.6842 | -53.67757 | 2025-07-07 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca1e451-5776-32ff-98d0-4cf05cb0ac5c | -17.0958 | -43.80552 | 2025-07-07 04:36:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd764901-8abb-3035-bd32-14058e5a39fa | -16.2748 | -47.57122 | 2025-07-07 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 620b3b93-7dae-34f6-90ea-512417d070af | -14.12103 | -51.30299 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 561f1671-5593-3fcd-abb6-d50eb06c966c | -16.57868 | -45.14538 | 2025-07-07 04:36:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4745c46f-6481-3913-a831-9b88fad9ff02 | -15.80502 | -47.64834 | 2025-07-07 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b472b2f-89dd-3779-a1d6-5e13bd1b3541 | -20.76295 | -46.76906 | 2025-07-07 04:36:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5dcf93bf-e539-33f5-ae45-041a6c483b88 | -14.12777 | -51.30414 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b957fba-0f81-308c-930e-9b3f42ab53f9 | -14.12561 | -51.29618 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 676c64af-963c-36dd-ac4c-ca368b5318f8 | -14.13054 | -51.30841 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ed6d49b-1a45-3000-adda-98379f88e4ac | -15.74803 | -47.78311 | 2025-07-07 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8008430f-181a-38d5-8410-de7eeb1cd15d | -15.07807 | -48.94364 | 2025-07-07 04:36:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad5090de-0566-30bb-b50a-6468a8661a0e | -16.28299 | -47.56428 | 2025-07-07 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 624316e3-0e0a-365b-8ec1-9ef76c110b97 | -14.92961 | -55.83604 | 2025-07-07 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9edba95-420f-318d-9543-c128f88eac12 | -15.56874 | -47.85593 | 2025-07-07 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c90728a5-d361-378f-bbc0-2d78103b22df | -14.12002 | -51.29947 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8698745-8d21-378b-8576-973a5fd75fa5 | -15.03901 | -48.64194 | 2025-07-07 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 12ce1105-104d-3163-bec3-87b4f16b6f79 | -20.25528 | -44.421 | 2025-07-07 04:36:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5ea57225-494f-3368-98c6-880dc1564f2c | -14.12656 | -51.31154 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8a13389-04f2-30eb-9652-cfb7dfb4fbaa | -20.37627 | -45.60285 | 2025-07-07 04:36:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5f9bab4-a085-3ee1-980a-6f524b97810c | -14.1244 | -51.30357 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ceef120-79e6-3baf-8c96-16850084e8a9 | -14.12838 | -51.30045 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80e0687b-a9b6-3251-83a3-e837789c77fd | -16.28357 | -47.56021 | 2025-07-07 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b264dba7-1c6c-3faa-b269-bf35f3f70d5e | -14.13452 | -51.30528 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41b0fdda-24b7-35b5-8e22-216fc5de0e48 | -15.68455 | -53.67583 | 2025-07-07 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a49a9d3f-fc30-3b36-bb8f-a0ee88b6603d | -14.13114 | -51.30471 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README9.md)
