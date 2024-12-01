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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3e25918-9843-3338-94f0-c8ca0e4d67d8 | -2.59717 | -54.2229 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bc79451-e7f7-31bf-9c03-e5831c0817a7 | -1.92923 | -53.96391 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4bc29dd-3035-3bc6-9362-f4f6a50a468e | -3.07351 | -50.3271 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24eaf39a-1261-3658-9a54-bbc64722b0b7 | -3.05665 | -57.38893 | 2024-12-01 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1bf648a-44d8-394b-bb87-46612f540fd0 | -2.87388 | -53.9887 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f551d5c9-ddca-3393-a268-b94721566b31 | -3.10699 | -50.31828 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15a5569f-1c8f-3749-9aaf-f8a61fdd8e5b | -3.21686 | -54.17783 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdd98688-ee13-3097-90f5-e793ad9fa76c | -8.93097 | -44.25013 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eec7a6c8-5ec2-3a15-a56d-aff626f0ef41 | -3.18753 | -53.25508 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 478dca27-040e-351a-bf62-1e8f20427677 | -3.32356 | -50.22155 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 886a960e-9482-3127-98cc-4ad601b6418b | -4.534 | -45.70528 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c31966f1-6afc-3167-b17d-77b1508cb90c | -2.58453 | -54.21323 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e09d24-0594-33c1-92a7-a02caee1a3e5 | -3.46903 | -50.27134 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| be4416c7-2ebf-3963-a60c-056469b85bf1 | -2.73023 | -54.10212 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e312baf9-72e1-3e7c-95ae-281ad806da24 | -1.49357 | -52.3292 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f79b2d24-9e31-30b2-aced-3d67ce31379b | -2.6004 | -54.04409 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26b48902-43c5-3c4c-a73f-4f1db2c68360 | -5.31156 | -50.57064 | 2024-12-01 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73f5481d-1061-3376-a813-a1ca89d46ecd | -3.67101 | -54.04959 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 959d84f3-2f3d-3eac-8f0e-612ca7c230a7 | -3.32142 | -50.03037 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a8afa72-e81f-3e9f-a644-c61352f30d37 | -3.51995 | -62.76218 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 360168fd-43e7-3811-b978-0d616e365b50 | -3.02496 | -54.01537 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 090d19e0-e684-3ae6-beb1-df5ba4091576 | -4.00341 | -54.61592 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 617e1332-77f6-3b07-89eb-e21e94e13e4c | -3.66456 | -52.29727 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fefc50d-7ed2-3357-b6f0-f974e1bd360d | -3.47228 | -47.68333 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc050d76-6384-3373-b11a-cbdcc13269c0 | -2.2395 | -54.91598 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46bb3d34-c5c9-3251-a0b6-5a10a1c82c93 | -1.64133 | -55.06745 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47911079-dd4b-39f9-b51a-f0004ce7555e | -3.26861 | -50.56493 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79769521-3d47-3e77-9f9d-74124f77361f | -2.29973 | -51.98738 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 074500bc-e81a-340c-aad4-567283ffb136 | -2.03626 | -54.6711 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a4bf9e3-77e4-34cc-941e-03225daa96b0 | -1.35999 | -55.15326 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7adef902-66b9-3de7-a40a-0ef91a2ee020 | -2.89361 | -54.1611 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ab55642-256c-3772-9277-442adb30d6ef | -2.032 | -52.07698 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85e02203-fa5d-320a-80cd-966b521dd641 | -3.09687 | -53.28858 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 476e05bf-1123-32be-afc3-d6ae0751f9d5 | -3.14864 | -45.3681 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 22c087a7-b39e-32ad-8cde-2b151b30fc12 | -1.40093 | -54.09425 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d67b1f84-b7d1-31b7-88ac-614f175b2a65 | -1.69926 | -52.77016 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff080563-4970-3ad7-a069-c0f1c0188180 | -3.18223 | -54.33227 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d821616-40f3-36db-a1fa-d142b7a462d2 | -1.71691 | -52.77726 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77883570-c57f-3b13-b3bc-de33e443d94d | -3.86741 | -51.01452 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70562adb-cda0-3e47-9760-0d9b246b473a | -2.52498 | -54.07135 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 625c7acb-543e-3b78-80ee-230e76bfd412 | -3.17407 | -53.63589 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f18c3d4f-f913-38a6-a47f-2d33a4a40ca2 | -4.00282 | -54.61971 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fbb18c4-4268-3126-88c8-1387b5116d1c | -2.80596 | -54.02724 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51747cb8-7361-3f08-8921-a1fa36cab072 | -5.53467 | -45.43425 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0075d8be-c477-3902-8a59-bf8a1b22c483 | -1.57603 | -53.86524 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67f5b7e3-ea1b-3148-88aa-d9dff53b5ba5 | -3.2649 | -53.63263 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a0be82ab-f61e-3704-b5f2-1a6a47a0fa37 | -3.08815 | -54.12312 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3207218d-7789-3d07-a15d-edb28ecf7d66 | -3.09946 | -54.04976 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de94b44a-a180-30c5-9806-b37238a6e3dd | -2.59613 | -54.26836 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a7c438-460b-3e43-a51d-198c994a63e6 | -4.25588 | -50.84274 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 940e3053-20e9-315f-8e67-86f5cea8efe6 | -2.90349 | -53.88945 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e796f19f-8c7c-395f-ad4b-32618fc2353d | -3.67301 | -52.29364 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f52badd-4c4d-3a58-a46d-59fef117b16b | -3.09334 | -54.29599 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 337339dc-6381-327b-bf1d-f5060f465622 | -3.69281 | -51.81817 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4161965-f1a0-3eb6-9c8b-7f263ce027a7 | -3.07593 | -53.42574 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c48cb8f-d55f-384c-bf38-531c684770db | -3.25187 | -53.62226 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a6ad146-004e-3069-ae95-a2cab22bbede | -6.28308 | -43.85558 | 2024-12-01 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e77a8736-be1a-32d9-86bb-3790419ca69d | -1.46096 | -54.49181 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a9f6dc6-0a35-3d6c-8f4a-4f12f350feb8 | -1.44539 | -55.12707 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 209da3ba-5966-339e-9d6c-86bf116d79c9 | -1.67241 | -52.50294 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8c2acaf-ad4f-33dc-85c7-85db833291c3 | -2.74129 | -54.07639 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f31c78f-e4be-3727-a76f-b29c7816d805 | -2.14455 | -54.87185 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b77e18b-690f-3488-a6a1-4f25db2a647e | -3.67452 | -54.05015 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 398b71e5-9fca-3b94-b1a9-46030acaf390 | -3.84016 | -59.57843 | 2024-12-01 05:08:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5dca4e0-6cfd-3ea9-847a-0f85c77d74cd | -3.48392 | -50.32185 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 07e45a61-b0d4-39a3-b093-22af4cde92d3 | -2.87084 | -54.03183 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ac5e0c-1344-3e87-b998-837437845827 | -2.48994 | -55.2666 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371ca5fb-5cbf-3af5-b8de-dd9fb394558b | -3.5184 | -62.76279 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b128a54-8135-3d09-8598-7422b2651eaa | -2.85451 | -54.0451 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fd058b9-3675-3eb5-8c11-8089d64c92b2 | -2.84872 | -54.03631 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ac733d-7861-324f-a8cb-855358cfccf0 | -2.53613 | -53.99871 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae60e1ca-cbda-343f-984e-282edf75b1d2 | -2.69223 | -51.72567 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ea3b8d0-5d6c-39cb-9969-a4cc92251ce3 | -2.73072 | -54.16843 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9a97106-cd53-368a-95c3-292b02e77794 | -3.80358 | -51.00645 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6ff6b85-4de7-361b-b622-b68a27ec03f6 | -3.27081 | -53.64176 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2377911a-ab40-35bf-aa74-10b9d8946eee | -1.33915 | -54.98127 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 349608bc-c681-3c55-93ae-598793d9bc99 | -1.85072 | -55.61797 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7adf23d-18e5-3920-848a-c0f2a80e43d5 | -2.88429 | -54.01411 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a577ce5-b5a3-31cb-b3b2-bf09a3768ce0 | -3.03846 | -50.97879 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 166829b2-6ccc-37e0-8ae6-cdf3b26ece65 | -3.03187 | -51.54435 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a88ee59f-1c28-38a9-b336-0ae60bab975c | -4.55156 | -43.29669 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 5987bd3f-a45a-374c-bffd-8debca9c6fa2 | -3.105 | -54.12947 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f80d77c5-8598-3dc8-81f3-e70701d77f5f | -1.43819 | -55.15113 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fc372a-1f1f-3518-8ec1-8bfcacaf3d4c | -3.68984 | -51.81089 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ea08566-7cdd-3d68-85c9-1c53c3a60e66 | -2.9615 | -53.72447 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bc6774f-16b5-3f2c-8287-c5d630db10d9 | -3.30116 | -50.49417 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6cd151a-ad83-35d0-afcc-bc43bebf9e3f | -2.98158 | -53.90086 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4787a18d-73c4-3bc8-92f2-b7b363987fbf | -1.23387 | -53.3616 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7d25b2-6472-3fbe-a73e-5ee45dde643d | -2.75232 | -51.75558 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2bc4347c-138b-3000-8c67-f09912b0db20 | -3.21306 | -50.26914 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ee0f132-e8fb-3336-82f2-7de451db1966 | -2.96385 | -53.89464 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f756ea10-84d1-35e0-bdc3-bed99621e4db | -2.96676 | -53.89904 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5d95d04-fa47-37a9-93f1-579bad08739e | -3.6384 | -54.44247 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d833dafb-25be-3e7c-83c2-a31142da5756 | -6.19229 | -44.42751 | 2024-12-01 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec759854-4478-33a7-bb98-ab9e9b205968 | -3.09743 | -54.1323 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8007c467-3210-378e-bc7c-88265cbf72a6 | -3.09117 | -51.26064 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d80592d-4d2e-3345-90be-3e87c4a47b46 | -1.69667 | -52.6415 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fe323e1-01e6-35b1-bc94-ab84dce5d090 | -3.71002 | -54.61086 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9e865ac-0baf-3cbc-8358-52037bb4917d | -2.59486 | -53.9882 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7a3999e-6ede-36a4-8809-a0071abae54e | -1.81765 | -50.90617 | 2024-12-01 05:08:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README86.md)
