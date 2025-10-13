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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 396bbd0a-c090-3683-a68e-f46d381a3e14 | -7.61979 | -43.04995 | 2025-10-13 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4c81f45e-74ac-387b-97b3-ad158fcb0dcd | -7.9205 | -43.30704 | 2025-10-13 03:55:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5217c551-855c-3655-b941-300069fe7419 | -10.80521 | -43.96345 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbcc9bfc-1e37-30f3-82c9-0c951925f642 | -13.56538 | -43.42049 | 2025-10-13 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 295db437-3ace-3114-a9ea-bd2851fd88b0 | -8.21922 | -43.32577 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 24a54eba-5d8c-36a9-8569-6c5f4aef5fbc | -7.83743 | -44.52822 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd7ff18c-cb9c-3f08-bfb4-a8a83372203c | -8.46102 | -46.12848 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5209b3fc-0d03-3939-bd86-f14e8157deae | -10.81124 | -43.97512 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51130e8f-38a5-33e9-91d8-d02ff95d8eb1 | -8.45166 | -46.12697 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e5597a1-5ece-3817-a6ce-9d9f02b6c66b | -15.19009 | -43.57601 | 2025-10-13 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0b11a9e4-eeb3-3689-a778-e3f114934b20 | -15.54823 | -41.80958 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 61ba2e0f-d8e7-3d29-9aa3-8346fa4eafe7 | -7.49945 | -44.59626 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fe48fe16-e72f-3dfc-b363-ab75458d3c20 | -7.68652 | -42.57514 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 471d3a52-5764-3a74-b6f7-f26477214360 | -8.47594 | -46.12564 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19e3267a-0123-3662-8e06-60e8297fa3ae | -10.03724 | -43.80779 | 2025-10-13 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 06ab5946-8b45-3a1c-bc09-45e7030eba22 | -7.49464 | -44.6243 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 8c279011-558d-397e-8c99-5e12347aca90 | -10.80648 | -43.97954 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ce60912-979b-33a5-b27e-20232382c547 | -8.47345 | -46.16772 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 536ddab5-1e81-3a46-aedb-fea9ff379242 | -13.67581 | -43.05462 | 2025-10-13 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c15df854-a110-3161-8015-1a13a0d89a94 | -8.22951 | -43.34092 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8bb339b6-c369-316d-8430-6ea6b5c2b254 | -8.4742 | -46.13567 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7d89619-2cc3-39f7-8c45-19949c93813c | -7.74819 | -42.41369 | 2025-10-13 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e6a108a-b871-3328-b299-ec3a80d8f635 | -8.23255 | -43.34659 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f7890094-ead9-3cae-a737-7fb3d00136c8 | -7.70405 | -42.36731 | 2025-10-13 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 90c79b16-db0c-3da3-ba10-f31f059407e2 | -7.54084 | -46.09402 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d01e7790-7c6c-3496-9a40-13cfda02feb5 | -15.53996 | -41.79684 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6a553a75-bea8-3400-b940-7bdd3c4fa50c | -10.79221 | -43.94572 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6caf6da3-c20e-3056-85bc-98868f99ea6d | -10.80951 | -43.98532 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1bc4c170-a6ea-3b3c-a0d9-578207e0e1a8 | -7.80467 | -42.44134 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a534acd-b124-308f-8fdd-4c039568f31e | -7.50679 | -44.63057 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9a62cb17-b068-3e7a-9440-c07b02b64f86 | -7.7741 | -44.04661 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb909210-3578-3857-af7d-0f0c5c5cc4fd | -13.75206 | -45.66037 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa76ba5-2eae-3fba-aa4f-158d8fdcae60 | -8.46191 | -46.12338 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6faebdb1-d003-313a-8c7e-05f1478daf3e | -8.52337 | -45.40211 | 2025-10-13 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21d820cc-4d1a-3ab5-adf1-ea1bcf5d786a | -9.26484 | -40.43628 | 2025-10-13 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab348b6c-4a18-36f4-af5c-ef4fcd05d030 | -8.21564 | -43.32837 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ec53d8bf-6800-39fd-95c2-dc3ff2e3f50c | -8.45723 | -46.12267 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 845c0057-501e-3311-ad7c-60e5713d04f3 | -7.79343 | -42.39369 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf789fb1-ef54-363d-9c3f-5cfea4032878 | -7.4981 | -44.60414 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f41a72f7-3f18-3527-9852-635d68941b27 | -10.79158 | -47.28316 | 2025-10-13 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b96bcb1-97c9-3c0c-9ce7-5eec0a3aa589 | -8.23697 | -43.36766 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8eac1873-2966-37bd-beef-6a5a74fb05f0 | -13.31863 | -47.09867 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8dc29fa6-f70b-3f28-9676-0285f70c55b4 | -9.7845 | -42.0303 | 2025-10-13 03:55:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ecbcc8cd-c831-308d-99d7-302203f9db0a | -8.22561 | -43.34028 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2fea5447-d1d4-37b4-bfa9-13f32368d1d4 | -11.59997 | -47.52148 | 2025-10-13 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bba72666-2a63-3d35-8b02-6fa0b1eb2baf | -8.46659 | -46.12411 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b9b0af0-0f9c-3109-b5af-c132054e59db | -8.40241 | -45.05859 | 2025-10-13 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02e64990-11b4-34e7-86b4-76c56ab4100a | -8.21885 | -43.37981 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d2e0f60-2274-38ac-aa21-2fc0e99ee810 | -11.43429 | -42.31201 | 2025-10-13 03:55:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad516bed-d36c-3c14-85ff-d6a215aeb758 | -15.54249 | -41.82378 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4139da7f-626a-3f8a-83ef-d572d60b5046 | -13.85737 | -45.49287 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71e1a28-5120-3edd-b50d-e8ec7dc64f11 | -7.69027 | -42.57574 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 488f1f6e-95b5-3462-a0c6-d7d538c1d25a | -8.5213 | -45.39329 | 2025-10-13 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7639062c-d78c-364f-885f-e2a1e99f6de7 | -13.75137 | -45.66419 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7f15026-e9ce-387c-b738-a15a5d6cc54b | -10.80218 | -43.9577 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f7e07957-b9eb-36f4-bfc8-b74bfac6f068 | -7.36019 | -45.20111 | 2025-10-13 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a86cf030-3b21-3b0c-b5b5-27d1b1b78517 | -7.54979 | -43.83627 | 2025-10-13 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59543a01-ad18-3dac-9a52-7670e35e7b26 | -15.53363 | -41.81464 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 42b1d734-431f-3ca5-9f70-8ecb064913c3 | -13.84786 | -45.54525 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c653567-ae3b-3116-af62-7114564237c9 | -8.45256 | -46.12187 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0f502b83-e660-34fd-a232-ddde87fe2a21 | -8.46012 | -46.13364 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d56234e9-9312-39c8-8a21-e887ed18b6d7 | -8.46391 | -46.13948 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33468715-bc42-3f97-ade5-b203ac3ed2f9 | -8.67364 | -36.69514 | 2025-10-13 03:55:00 | NOAA-21 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e633db9a-67fc-3732-9bc4-1bb05a6242b1 | -7.88125 | -44.44959 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78942e32-8816-3b65-8164-30bf075c3423 | -7.784 | -44.05663 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e200e9c6-37fd-3fad-9355-d22626411a85 | -7.54752 | -47.32581 | 2025-10-13 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c205bcd1-fe8b-3149-90ec-bb6858df8818 | -8.21144 | -43.32442 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7cb54b97-641a-35f4-a3cd-09e01fa67ee7 | -7.80837 | -42.44203 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8529b820-3399-3f8d-a6a6-b9ddfa57ea71 | -12.74761 | -50.65907 | 2025-10-13 03:55:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d4cfeef-6297-3e9a-b147-0c9b58696a6b | -10.79957 | -43.97301 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 918ef103-4fb6-3c55-bde0-0304aadf7d84 | -7.78054 | -44.05223 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0757771-7368-3788-84be-fd41d3d52371 | -7.95133 | -41.69171 | 2025-10-13 03:55:00 | NOAA-21 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3249a1ed-0f46-338b-838e-786c269b778e | -7.51298 | -44.59433 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 312d8d59-d62f-3552-8c8b-335a9edf7aae | -13.8805 | -45.48143 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aff966df-2c5d-33ab-b340-11a49008b6b8 | -9.25657 | -44.37765 | 2025-10-13 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c5736280-fc88-38db-8883-c8b3658eabd4 | -7.53896 | -46.09699 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a8f6393-db24-341e-94a6-ebbd59bdadbd | -7.67435 | -43.98838 | 2025-10-13 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f964b272-f7cd-329d-ad89-82ef1da39b84 | -15.02006 | -41.82477 | 2025-10-13 03:55:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69e2524e-5d4a-3f8a-b375-f3c33561636c | -10.81427 | -43.98094 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ef82e855-7d89-3e10-a90a-d07839a53e26 | -7.80022 | -42.44521 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3c636724-b005-3aad-ad3d-22e8aef64a20 | -13.8567 | -45.4966 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6db3828a-78e5-3594-84f5-3288471a9f97 | -7.49035 | -44.6236 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 34ea20ad-2d01-38ca-875d-f4b3c4f2aa5a | -10.78955 | -47.28602 | 2025-10-13 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dea52fe6-4138-34de-a2dc-37fc78d35cd7 | -7.77361 | -44.04348 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd82d136-ae06-3232-9431-4027ae1b2a9e | -13.31841 | -47.10059 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3668c9a9-bc2f-30f6-95c3-418e3af45f4f | -8.49848 | -44.73121 | 2025-10-13 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dd2abae-f377-3f30-be4e-cd8ec3134375 | -8.4768 | -46.12067 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 195d648a-cfc8-3035-a678-212abf8f62dd | -8.23865 | -43.35779 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 299363ef-414c-3b59-b522-a5aad9885dbb | -13.27286 | -47.11641 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4322a003-38d8-3341-8229-cfe9c3d33078 | -8.21953 | -43.32903 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f4e50e82-dbaa-3454-bcda-3b190fce25a5 | -15.54308 | -41.82008 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 435cabef-07a4-3ebf-b1c8-50086b2553ba | -12.76802 | -50.67493 | 2025-10-13 03:55:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d75d2b43-34fe-36a0-97b2-af1031dcf691 | -8.1811 | -43.3144 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7f08b5dc-9bd5-36ca-88ac-4271fdfe6a8f | -7.83812 | -44.52421 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a34a622-0a8e-343f-8c78-7847063bff0e | -15.53326 | -41.79569 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2959d626-d550-300b-9558-9ada772aaa64 | -7.7415 | -42.43087 | 2025-10-13 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7a893885-c1df-3ecd-8bc5-f14c72c9e413 | -13.85874 | -45.48536 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4b3dcb2-e482-3041-88a7-6969ed0b83ba | -13.8669 | -45.44033 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 089fb297-d305-3486-a0a2-596d57fb5927 | -7.80095 | -42.44073 | 2025-10-13 03:55:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c37b8ce4-066f-30dc-a464-c60fbe72a45e | -7.50942 | -44.58942 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README13.md)
