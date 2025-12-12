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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b7c1ebd-c144-3817-8065-87273e29c6e8 | -2.94178 | -53.02834 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 090f6f44-656a-36ac-aa41-34cf85982618 | -3.49619 | -44.89148 | 2025-12-12 04:21:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acb9a8b9-0f82-32d4-9000-b825996b1c18 | -5.14526 | -43.80632 | 2025-12-12 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb830710-f139-343f-9814-65eb93114a3b | -2.6535 | -51.64847 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0da438af-aa0e-388a-aa00-62cce11ef4bd | -2.29807 | -45.59118 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab368c2c-ece7-361e-bde7-a091af8a0a82 | -1.14373 | -47.24971 | 2025-12-12 04:21:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40338245-083f-3cf7-be82-3b897cbf6dcb | -2.88595 | -47.79863 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b8a3cd-fade-3150-8d71-4b834b612c19 | -1.33979 | -54.61473 | 2025-12-12 04:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14fd6486-9475-3fee-8545-779bad3a6586 | -5.15735 | -37.69808 | 2025-12-12 04:21:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8ad94841-e5f8-3446-8bb2-eff611df1b50 | -4.38227 | -43.62673 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68630907-afef-3f77-9265-072b881a953d | -2.82517 | -45.26058 | 2025-12-12 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c25231b6-9667-3d22-9c19-cc5016e9312b | -2.02943 | -47.14278 | 2025-12-12 04:21:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64938f78-a394-3e8f-8933-68934f061141 | -2.69453 | -45.70102 | 2025-12-12 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1ac0a25e-c302-3dde-a919-58c3f3e03c26 | -3.41994 | -42.28222 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b50c5d63-b893-3e69-b970-1c4a299f0a4c | -1.66035 | -46.23158 | 2025-12-12 04:21:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0462182-dfa1-39e3-be7f-f4d74c14aa27 | -4.93406 | -43.96213 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8173147-f8c8-33ef-8446-a03827cb0a0a | -6.11544 | -41.28214 | 2025-12-12 04:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5b5df412-6d90-3229-bdf7-6fcc2e1ba26f | -6.22574 | -44.17169 | 2025-12-12 04:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 037d0eb8-4cdb-3ac9-8ada-cc1190f6946f | -3.42734 | -42.27957 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57f6431b-e327-3e8d-967d-8fdaf930af46 | -6.51438 | -55.03902 | 2025-12-12 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ecbaefa-d7ea-3c55-b568-f8f35ac2696b | -2.66935 | -46.897 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83195841-8a72-3293-a8e4-be9c59fb68d8 | -2.69793 | -45.70156 | 2025-12-12 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b55a4180-2433-3ae0-b06b-7f62bb354582 | -4.7455 | -44.55411 | 2025-12-12 04:21:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36a9c2a0-b51f-3388-9e21-ad9001f6cdae | -2.82853 | -45.2611 | 2025-12-12 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dea996-2edf-3050-a688-c8f0058ad3bf | -6.57009 | -47.24541 | 2025-12-12 04:21:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93a95bf8-85ce-3456-809d-124883453f3e | -2.49655 | -51.79715 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4d18e40d-2cc4-3786-9c85-ab5a68b3d8b5 | -3.06488 | -45.79942 | 2025-12-12 04:21:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82632a20-e3c2-318e-a2ff-0e1b7c7b1903 | -6.02317 | -43.70673 | 2025-12-12 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ea77e33-87aa-3410-afc1-a152f168a834 | -3.01406 | -41.13846 | 2025-12-12 04:21:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8633e4f5-226b-3c89-a115-8a9a3c57e903 | 0.10206 | -51.13027 | 2025-12-12 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e33d3446-1d25-3a39-aac3-3ae5906944f8 | -3.88251 | -46.12266 | 2025-12-12 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f45ffa4-412c-3926-a259-24b94d33b9e8 | -8.03823 | -43.10655 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e095984-52ea-3bb9-9a62-d30511af81aa | -1.02931 | -53.74498 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dc364d9-7083-3094-adb2-6a4283b216bc | -4.74935 | -44.55118 | 2025-12-12 04:21:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62d93cd6-d413-3aa0-b116-8b0835b6d8ad | -3.95285 | -41.52205 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 10ccb02e-b8f6-320c-8c65-a08e94d1fc5b | -3.85916 | -40.66291 | 2025-12-12 04:21:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cce2ca8e-17f3-3f46-8366-fc42b1de6994 | -2.91019 | -45.22312 | 2025-12-12 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06b59a81-defa-3149-b628-cf8442036ae0 | -2.42873 | -51.93341 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 61ae8a7b-1f6a-3182-9eaf-301e456619e5 | -3.23865 | -42.07282 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51bf3946-db13-3f63-9265-05f32ec5e408 | -2.36544 | -47.68407 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 520a482f-16ca-302a-bf02-87710673bd4b | -2.89997 | -51.93832 | 2025-12-12 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 324e9f4a-c8a2-3f33-bad9-df0b57908cdf | -2.42378 | -51.9326 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 56d27800-ee00-3e26-86dc-67cdcb726a12 | -8.03421 | -43.10978 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b50d80a5-9fc3-3208-9a34-3ad389f41ba8 | -3.12183 | -54.1838 | 2025-12-12 04:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a27ab52-10ae-33cb-a33b-142ce2dfb2d5 | -3.64106 | -39.37537 | 2025-12-12 04:21:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eea05366-f113-3a1f-8e2e-a8a2d1b8b634 | -8.03194 | -43.10172 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9ce84b89-ec8f-3260-8e43-f5402e4ad0fc | -3.85208 | -46.9566 | 2025-12-12 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9eea54b-660b-35c3-ab34-fbd8ae86a372 | -4.30446 | -43.2127 | 2025-12-12 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef3c46a5-d739-3382-8a5e-012b2795cee9 | -1.10938 | -53.69391 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffa3e5ed-2fee-3eb6-80b8-8df72fa1f032 | -2.94123 | -53.03168 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76c9d6d4-ae6d-3797-9baf-8c203c3c6130 | -3.38293 | -47.18673 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8513ce41-501a-33af-83b9-e187a8a90fe0 | -3.96345 | -41.52371 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c2fbf4f5-55ff-39d8-81e7-c63fb1903490 | -2.66734 | -46.89335 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 880eee76-bd7a-3a24-a8ee-b3e14bb69145 | -6.4696 | -35.17191 | 2025-12-12 04:21:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2778573b-4a32-368d-86a6-78b56b0c7152 | -8.03882 | -43.10278 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5e45c07-0880-3dd0-ae80-cc7c4a9e3185 | -3.38585 | -47.1914 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 590ecbf5-36bf-330f-9121-8828808cd329 | -3.23522 | -42.0723 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eef5702-81f8-3f2a-8009-a6554bc82fd5 | -2.4278 | -51.93901 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 985abc16-fde9-3472-b130-a590dca05104 | -2.82318 | -45.26043 | 2025-12-12 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b0579d-29ba-3a40-8933-7d19f0063b03 | -3.5004 | -52.52893 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b4e71a1-6004-3d06-b2b5-75706bb7af7e | -0.97031 | -53.18757 | 2025-12-12 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2edee882-4f7f-3542-b701-f198b3ae3fdc | -4.38559 | -43.62724 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ae1ba89-e227-396f-b54b-95f0f7834242 | -1.31059 | -52.54025 | 2025-12-12 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d765c4b-a351-3de7-a4bf-239d4010f181 | -4.81177 | -44.48022 | 2025-12-12 04:21:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eee565f6-ddac-302e-a494-9d60af319f8d | -1.01352 | -53.73363 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 661040b9-247a-3190-b8ee-9f3bc71fa6c8 | -2.25613 | -48.23757 | 2025-12-12 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a229693-8aef-3b5e-a913-77cfa8607ceb | -6.12277 | -41.28323 | 2025-12-12 04:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de2faccf-1a43-316e-9271-0f61c21ee68b | -8.03654 | -43.09471 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 783fe34d-d573-325d-9c26-e17ce8621dfa | -2.53996 | -47.80502 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc0f463f-10cb-3dbd-8fd2-b5d094272cc9 | -3.06466 | -45.79629 | 2025-12-12 04:21:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4f7b650-015a-31d4-8116-dd8dfc7fdb30 | -3.23808 | -42.07655 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 031fe85a-27c5-33f7-a1fc-db10e48ffaa6 | -6.79518 | -47.59739 | 2025-12-12 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d31374bd-c041-3d46-b464-d44d7416540c | -2.21894 | -45.40408 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3871d589-3fbd-3b27-b607-9e81676e6765 | -2.43458 | -51.92875 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 64dd33dd-bef4-3ab1-b6d3-2a5ba323b0aa | -6.75924 | -39.05593 | 2025-12-12 04:21:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 40a321ba-3d17-320f-8cff-15207689202a | -1.28987 | -53.1688 | 2025-12-12 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80701c67-9a24-34c4-a395-dccfaf5a1f5c | -3.34826 | -53.07541 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2733a1e4-81fd-3791-b979-a1d7e59162dc | -2.30836 | -47.91715 | 2025-12-12 04:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d22bb8eb-ae41-3035-83ed-52c24735a37b | -8.03368 | -43.09042 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3be69dcd-81b0-3233-8ecc-2fa8687ac008 | -8.03078 | -43.10925 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 25256686-9c48-39a9-aaec-93a9b5741313 | -4.30501 | -43.20918 | 2025-12-12 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b67a6bb-70c0-32da-a1b0-03a14e0ff097 | -5.21437 | -38.58215 | 2025-12-12 04:21:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57eb0486-2445-3811-8fbe-d7f90ae67fb6 | -4.10855 | -47.3002 | 2025-12-12 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a61ed51-0557-31a0-b9af-9af24ad9b853 | -3.01852 | -52.82672 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45876f11-9ddc-31d5-963d-9dfbfcb0dac5 | -3.43765 | -41.6481 | 2025-12-12 04:21:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a8bc1eb2-28e8-347c-81b5-d545affc6d7b | -2.51118 | -47.8113 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99c0a853-051b-3f9e-8f2e-4e75b424c4ee | -2.35568 | -54.37781 | 2025-12-12 04:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d2f4aee3-adb7-3df5-a8df-b8a491648068 | -3.22864 | -41.80177 | 2025-12-12 04:21:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f4c91b94-e43f-3f97-b966-ee03252c96df | -0.97669 | -47.94021 | 2025-12-12 04:21:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3e40c92-faf8-365e-b4e5-b8d1621fb05d | -3.65724 | -47.15307 | 2025-12-12 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3de34fb5-e870-31f9-9da1-32b6373ecdfc | -6.11479 | -41.2864 | 2025-12-12 04:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce1f509e-ab71-3c58-9585-7d2e1430f328 | -3.42676 | -42.28325 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6df11fd-9182-3e87-9e7f-60c9f09fbf50 | -2.34143 | -45.7818 | 2025-12-12 04:21:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3bf0c76-fd1a-3d3b-9b75-5033a457a88e | -3.82468 | -51.14062 | 2025-12-12 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d015f872-edfe-3393-9612-79ee310f4594 | -3.90932 | -46.06633 | 2025-12-12 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb5b385b-95f0-3b6a-bc20-33299da6ecd1 | -2.57442 | -46.92453 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca68c673-448e-3c78-af95-94f33bfa5a40 | -8.03712 | -43.09094 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c03dad3b-00e6-3792-8de6-b00953589cf7 | -3.61216 | -41.8313 | 2025-12-12 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1bf66fb-624b-3566-b57e-eada7110700a | -6.12059 | -38.34974 | 2025-12-12 04:21:00 | NOAA-20 | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2f811dd-9991-3e02-9bab-2c40ae5d58b6 | -3.02317 | -52.83089 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README16.md)
