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

## Dados Diários - Página 328

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1862c41-ab5f-3914-a863-3154adde768b | -10.90751 | -45.53143 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 93f754e3-4139-3fc6-918c-003c1e82cde4 | -7.64129 | -44.3747 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f78b1442-ad5e-38b5-a9a7-40e6832647e1 | -10.46423 | -47.23957 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 75d58833-d86e-3b9e-8572-540087bec3de | -7.30581 | -43.98222 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1922d2f-27cd-34d5-91fc-05d3a345f0a6 | -7.88356 | -44.96999 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4d770d21-942e-30f3-8e22-f03eb2286de4 | -9.27137 | -45.63451 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d313c13-ce54-3d30-ac79-106b0d538578 | -10.90804 | -45.53497 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8bb7317a-f180-3611-bc23-353e09c1be61 | -7.58325 | -46.20326 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d6594586-cdd2-30be-8341-92efc5766fe0 | -7.78074 | -43.81484 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 05288984-ad06-3183-b826-d4f28910fd0c | -12.40988 | -39.08328 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| b9080140-e932-38bb-ad1e-b5406127a325 | -6.49372 | -43.9442 | 2026-10-08 16:37:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3cf87307-af0a-3f1d-b7cc-2a996f466a1d | -6.43058 | -44.81708 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fe17405d-eae0-3994-8bc4-ea4b1e2e5b92 | -5.99013 | -40.92556 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 01b84df1-b96c-3c36-ac11-37e29fea077e | -11.13717 | -46.13396 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 55a7fa40-ebf2-39a8-acd8-7891aae612d1 | -11.07362 | -44.02427 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 510ee613-4b9a-3253-9763-7a1927f4f55e | -6.6794 | -44.32225 | 2026-10-08 16:37:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 39b0e61d-7dd8-3e1a-b5fa-1d1eae0360b6 | -9.03087 | -44.37642 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 236f8898-fb38-3d28-bb33-15cf23d2bd45 | -11.76545 | -45.55463 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7c84d1d9-d918-3db2-9a33-f169746bc751 | -11.53601 | -47.71933 | 2026-10-08 16:37:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94b1cb33-a162-3ecc-920b-6f0632a2a5a4 | -11.11385 | -45.68682 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 1a93d111-1edf-38e9-a940-d5baeb372b81 | -12.15359 | -44.75433 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ce309c4a-5320-391c-956a-3412c629911e | -7.59692 | -42.39282 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 03cfe7f7-a887-3a99-b427-1710ca9c93be | -10.87801 | -47.60862 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 920e5359-b351-33ea-8d0c-bd9851c4ebfd | -7.60118 | -38.28609 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8974b29f-23ef-3367-af27-18030e8eb3ae | -6.07077 | -44.10678 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 68efddd7-3af3-3cbb-bce8-46ac6cc333f7 | -17.43031 | -40.41926 | 2026-10-08 16:37:00 | NOAA-20 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 0891f551-c4dc-3441-9502-02fc679ed689 | -9.77442 | -45.88829 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 98cf4949-4960-37a2-9d8e-2dd7a417d89c | -6.9582 | -45.24323 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f9993add-332d-37a9-ac39-cdb02513327f | -10.33526 | -46.23977 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 65519809-fd8c-3b02-a380-4dd127004c1b | -6.68336 | -44.32538 | 2026-10-08 16:37:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 5ddfa1e9-3dbb-3d23-a8b2-af8d3e99bedd | -11.87399 | -47.40885 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 97650b0d-0f30-370d-b693-4aec14f132e7 | -7.73987 | -49.59865 | 2026-10-08 16:37:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 540793a1-30cb-3ead-ae2e-c143e28eb67b | -8.03458 | -47.02376 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c34e737f-4aa8-3da7-8cde-49899d6a420b | -9.08128 | -45.12257 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 41df1729-50e4-393a-bf21-251ec3c9a37d | -10.51121 | -47.31947 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ff4e9ec4-fa70-3dc3-a303-f06e014e7bbf | -10.63422 | -41.39388 | 2026-10-08 16:37:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 79f86698-54e6-359e-830f-d4a0c120c105 | -12.72079 | -45.8204 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9c93f3d1-fcd7-38b0-9331-aedcb7607a11 | -9.36704 | -45.95293 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cc77444a-2248-3dee-a68c-f542e92423b4 | -9.1356 | -45.83563 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 49f38799-b9b8-37e0-8268-cf682eeadb04 | -11.76506 | -45.52924 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 979ad498-8166-3224-b0f4-941d3ef9339e | -18.12756 | -42.38786 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 019489f5-a1c6-3395-a810-5af322003d96 | -12.28252 | -45.3161 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 26dd6aa4-91aa-3359-bc1a-659e3ac75101 | -12.83938 | -44.62432 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 61bfea88-0437-366f-8f5b-49fb017b17de | -6.39844 | -44.9349 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5165426c-1862-30e8-8c2d-98203dbaf778 | -12.7709 | -44.86663 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c3c226e5-0445-3f0a-8f9b-e5a62189a403 | -10.92986 | -45.38737 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| b73f803e-8331-38dc-925a-77e49e19e5d4 | -12.23629 | -44.74132 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5e298e1c-9ac3-3c8e-b680-cf62e4eb5ad2 | -7.05704 | -46.53616 | 2026-10-08 16:37:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 519bf43e-6d6f-3c60-8d6b-02aefc6d1cd3 | -9.97556 | -43.57742 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 30cb9958-b801-3fa0-9a6b-f6f6e9cfc005 | -12.01416 | -39.04941 | 2026-10-08 16:37:00 | NOAA-20 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 9fc0cefe-3cb2-36c8-baa5-429d36c2520d | -8.28957 | -45.73756 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| e824eacb-c015-36f9-a3d1-c40b21fd5939 | -6.42555 | -44.82874 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 58c55943-b515-3855-9350-d2ece315c2fc | -9.76677 | -44.79023 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 0f7c3d60-2578-3539-8d86-bcb2b429e5aa | -12.18543 | -44.65215 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 95ae6846-dd88-38e4-b1cb-66de8afcd6be | -11.76639 | -45.49273 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c57d58d3-05c2-3f68-a28e-dbad64d7b1d7 | -6.53435 | -45.40039 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 509a6244-ada8-3aea-b177-acfe1b1c08ac | -6.96431 | -44.99536 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f455f714-f6b4-3cb6-b5ae-8317b6f15be6 | -8.54888 | -46.91534 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2098d64e-18b7-3627-a89e-aa359bdea60c | -7.25521 | -45.3419 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 721e8fbd-370d-3df2-91e7-34c74d5a46ac | -6.26523 | -44.73117 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9adf4273-dc8a-3757-ba0e-533bf1d6617b | -6.63571 | -44.89295 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 98cb4901-8c7a-3014-899c-5c75302fad95 | -8.61905 | -44.87574 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34a17c59-1606-3f5a-85b5-aa6f0f4e8a84 | -8.08271 | -55.28942 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c6a4f40-cf3b-38cd-84be-4e6a7edafa21 | -6.59896 | -44.84872 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 12e942cf-c97e-311c-8a1a-77926f261a0c | -6.53767 | -45.39989 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c558993-0d44-300b-956a-cf879ee6046a | -5.98996 | -37.38235 | 2026-10-08 16:37:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2894f70e-bd3f-3713-92c7-dea2ef60effe | -12.03224 | -43.4408 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d5e136e2-88a7-31dd-9909-8e29a0661681 | -7.34309 | -46.14116 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6517e5f8-9532-33b8-8b7d-ee0a2b270bd3 | -6.97635 | -47.67496 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| adadc500-b6b6-3ce3-87ee-6bb7c2732f6d | -8.18866 | -46.37201 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d83c06ef-9c84-3f78-9534-c505b08871be | -12.77699 | -44.86206 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| f28b749a-ba21-3ffc-a7d3-91a59f465b59 | -11.69231 | -43.65891 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d308c65-8dc6-3bb5-a725-d8e26b8f8be4 | -8.50694 | -54.6307 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d092df90-3403-3de1-9825-cd2b1f076b88 | -8.40539 | -46.91126 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9a64e179-b92b-3b6c-b9f8-221e36c7985e | -11.77705 | -45.5638 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0d2d32c5-6d3d-326e-80f0-15b1e6e18f57 | -7.76058 | -54.94952 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 297f292e-0c5e-38d7-a610-b920b7cd7b54 | -5.5164 | -37.48899 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b0ae469e-56d5-3dbb-a7da-a8d9d44f193b | -9.21236 | -57.72764 | 2026-10-08 16:37:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 9a925441-610f-3a30-a90d-945f9dfd7e75 | -7.87119 | -54.96098 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9a14c709-ca33-3f84-b81f-f589d462472a | -6.68873 | -45.30076 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 1065a8c4-bace-3c12-94b7-e97a3b492dca | -14.33138 | -52.07575 | 2026-10-08 16:37:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2ba3bcd-d60f-369a-add7-c978ed4dc620 | -9.70493 | -45.69769 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| dfefd585-f916-319e-89aa-19cc75e3dcf8 | -9.85579 | -47.85304 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| e99213cd-381c-39d2-bcca-235754c3bbf0 | -9.91615 | -44.79128 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| cdfb01cf-d9fe-3642-bd4a-12eccf591842 | -9.80707 | -47.81506 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 02744ab5-f675-3d0c-b720-4fd89139b47f | -5.9905 | -37.38544 | 2026-10-08 16:37:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f07b7151-5f33-3586-87b6-75ce75b60d35 | -11.38674 | -47.73069 | 2026-10-08 16:37:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 78a6105e-5e80-36aa-a0ae-792075d10173 | -6.35272 | -44.36234 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d49461dd-7024-3e34-8365-acae922b4b05 | -12.24675 | -44.74327 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 4a693053-c9d8-3bfc-b069-06ed73da6f6f | -7.82045 | -38.86254 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 131.3 |
| e8acbc99-982f-3b5c-a6bc-cc6a644a4758 | -11.00694 | -45.42551 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4c017bfd-b2cd-313e-b379-d55d080da9c1 | -19.57947 | -47.76414 | 2026-10-08 16:37:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2530accb-5d5d-3b53-9178-424d5fc1d3e9 | -12.22324 | -44.70016 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 23e8a490-1d4f-34c8-8499-8f4233ca0052 | -11.08084 | -44.02676 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 37fc4116-244d-329d-a76e-13d8a409e7c9 | -5.73892 | -41.76282 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dd8d8b0d-47dd-3ea6-a907-cf2d9f8e36c9 | -5.76713 | -42.05711 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| db6511a1-da0b-3af8-bd89-ac76ae6480a3 | -11.62218 | -43.68568 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 24d02ed9-cc74-32c8-8ccb-ae29c15f8f1f | -5.74969 | -41.70698 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 5bd125f2-92ae-3964-8745-ce09d9c279b3 | -6.62904 | -44.894 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f54019c3-5c41-3ce6-b507-4ce72a630fa5 | -12.47935 | -42.23565 | 2026-10-08 16:37:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |


[Clique aqui para ver as próximas entradas](README329.md)
