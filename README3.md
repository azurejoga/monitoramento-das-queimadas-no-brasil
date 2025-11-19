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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d95343c2-0900-3668-b3bd-1a808cd25d11 | -4.58886 | -48.54023 | 2025-11-19 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d50abb23-c13d-3e79-b278-f94417750320 | -2.87757 | -52.60992 | 2025-11-19 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f4230e6-f15b-31c0-b0cf-f1422b3e46bd | -2.53298 | -51.17447 | 2025-11-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c4f54fd-4889-3c76-b5a5-9a51935e63f0 | -6.1245 | -42.95836 | 2025-11-19 00:34:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 0cc4161f-932d-39eb-b6e7-7cb312d3a8ac | -3.55727 | -43.46167 | 2025-11-19 00:34:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f6cce6f7-c8a6-3b0e-932c-b030f43c3528 | -6.30759 | -43.8021 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2045facb-83be-37eb-8dd7-52c0db19b864 | -6.71094 | -42.12797 | 2025-11-19 00:34:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 89695f59-cc25-3d06-bc67-cca285f267db | -2.54145 | -45.37978 | 2025-11-19 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f1842a33-0b41-3b90-8a43-f6a67a77ff15 | -6.30469 | -43.78263 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e4538e63-aa00-3468-b4ab-50016ca98032 | -3.75425 | -51.81705 | 2025-11-19 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f7e683f3-6dc8-3863-b0a4-88baccbe4270 | -3.56079 | -43.48544 | 2025-11-19 00:34:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c0eba6a1-9e58-33fb-b68c-4a275195cf91 | -3.60939 | -51.37005 | 2025-11-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 62f24674-6d4c-3f3e-89cc-b0741effb1c3 | -1.34814 | -47.00217 | 2025-11-19 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ce6d5789-a5f1-3897-b619-b2f21ad3f757 | -1.48521 | -54.19421 | 2025-11-19 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b90acf03-d360-3419-b2fe-2139cbcb2415 | -1.9118 | -50.61567 | 2025-11-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96ecb722-be11-3da8-83f9-a7b7bd7ab0aa | -1.34854 | -54.611 | 2025-11-19 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 87583430-1393-3d0c-a1de-3a8df5c99a79 | -1.14745 | -54.10509 | 2025-11-19 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a74ea8cc-c83e-3b58-ad9b-cf5bc1420765 | -1.68541 | -53.18224 | 2025-11-19 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3f4488ed-9973-393b-81a2-f0f512983fd9 | -0.98444 | -52.43828 | 2025-11-19 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5c62f5f2-5744-306d-a7cf-bf729e50d6ef | -0.91062 | -52.90297 | 2025-11-19 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ff0c022-b77d-3873-9127-dc4204b4af9e | -1.70877 | -55.46584 | 2025-11-19 00:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3d54b6d2-ac49-36e5-9358-c9a173835438 | -1.12284 | -47.52233 | 2025-11-19 00:34:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b12ed753-70d4-3462-8ac1-990fd3d29257 | -1.35003 | -47.0159 | 2025-11-19 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| d11226e5-0dd6-3d6d-9028-55143fdd76a9 | -0.77075 | -52.48944 | 2025-11-19 00:34:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c85dbe24-4b3b-3c89-a3f1-6253a949dc6a | -1.3525 | -47.00906 | 2025-11-19 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 427e3435-49dc-39e9-8b83-a352632ad19b | -2.21747 | -53.63905 | 2025-11-19 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| da48711c-183d-3643-b68d-61fe53f164ec | -1.44166 | -52.67904 | 2025-11-19 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e51e6344-181e-3174-840d-3cfb444df505 | -1.35449 | -47.02275 | 2025-11-19 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 22c3d92b-af4c-3e2d-aaf0-99fa6c6cce51 | -1.48671 | -54.2051 | 2025-11-19 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1d13d759-4f5c-3051-8a07-04533202c71b | -1.8305 | -52.15829 | 2025-11-19 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd0c8719-b138-3be8-8a81-4d4ea90d7a38 | -0.9224 | -48.06556 | 2025-11-19 00:34:00 | TERRA_M-M | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a1a4168c-99b8-3876-9522-cc229af5e5ff | -2.4774 | -54.79725 | 2025-11-19 00:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2c1923d0-2112-30e1-bc07-69d414f90b28 | -1.68674 | -53.19199 | 2025-11-19 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c48670e-6f07-33a9-88fc-a76fea542711 | -4.9143 | -48.176201 | 2025-11-19 00:35:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01aa3491-0ac9-334b-8df8-cf7b9904aec0 | -5.7174 | -42.7351 | 2025-11-19 00:35:00 | METOP-C | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 081dc66d-25cd-3eed-8017-3ac51905347d | -11.0163 | -49.0298 | 2025-11-19 00:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9397f77b-12ea-3268-abe8-e15142b32379 | 3.6503 | -51.293301 | 2025-11-19 00:35:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0bd18d7d-0b76-30bf-90b2-ddb76abce482 | -11.6181 | -43.897598 | 2025-11-19 00:35:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30bb87d9-2683-3b9f-8d9a-9d0921c6906f | -12.1236 | -40.855 | 2025-11-19 00:35:00 | METOP-C | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6438a526-cb1f-3cfb-ad02-b4f872a5dcd3 | -5.2368 | -43.980499 | 2025-11-19 00:35:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e857641-9b9b-3f82-b2d7-02ad9c012f3c | -10.8813 | -49.5453 | 2025-11-19 00:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc7d05f0-d3f5-3840-a382-5d310c540f4a | -12.1356 | -45.161598 | 2025-11-19 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1fa28a00-8bd6-34c5-958b-930bde213fc2 | -4.6624 | -43.202801 | 2025-11-19 00:35:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5726ea5b-da53-32f4-a1db-33a6522a7dc5 | -10.7765 | -48.115002 | 2025-11-19 00:35:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f365b5ee-cb05-3ec3-92b1-578b9311d6c9 | -6.1092 | -42.952 | 2025-11-19 00:35:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a524c09-9b30-39d5-a204-1422ea65f84f | -21.4184 | -47.6847 | 2025-11-19 00:35:00 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7ffe109c-d71d-3502-a80b-4a4a272e5ca2 | -2.8443 | -45.625801 | 2025-11-19 00:35:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ddba99aa-6db3-3b50-92f9-501797411809 | -9.9957 | -44.069801 | 2025-11-19 00:35:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0eac2eae-f6c9-33cd-872a-3bcff1c772df | -9.3732 | -48.4156 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc017a1-fa4a-33f4-9928-f3144ed728bd | -5.1667 | -42.674702 | 2025-11-19 00:35:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 710a6258-9082-3d2e-b32d-7a673d4150b6 | -3.3592 | -43.493099 | 2025-11-19 00:35:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5355c59b-e3b6-38c5-a587-40f7172e3793 | -4.5754 | -44.063801 | 2025-11-19 00:35:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c84b55e9-761e-390e-b60d-1ced73655c49 | -4.5872 | -44.069801 | 2025-11-19 00:35:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 984c55bd-0087-307f-82ac-bfbea6138582 | -2.8541 | -45.6236 | 2025-11-19 00:35:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1d5bcc2-d0ca-3e3e-acd5-1bad14de80b6 | -10.5024 | -44.028702 | 2025-11-19 00:35:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d484ef7-0ca7-31fc-890e-e3488b0fbf74 | -6.3133 | -43.774601 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbb43e6-2883-31d5-8aa7-69e04dba79c1 | -11.7954 | -44.620499 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 137e414a-6562-3a6d-a3a8-dd9aa7c33653 | -9.4013 | -48.449799 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02937aef-6e28-3ec9-9fbc-db1c552dc98c | -10.5459 | -44.126801 | 2025-11-19 00:35:00 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35dd4d55-3caf-357b-9613-09b314471df5 | -12.1371 | -45.168598 | 2025-11-19 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6911fdb9-ec55-3bce-b8e6-3f1cc1eaea60 | -11.802 | -44.604099 | 2025-11-19 00:35:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1d5d3d2-d08d-33b8-8586-667e766fae8a | -3.3516 | -43.504398 | 2025-11-19 00:35:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d7aaca1-5c3a-3a2e-8006-03584f772176 | -4.7819 | -40.2435 | 2025-11-19 00:35:00 | METOP-C | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4001d4db-1230-3ddb-8897-d0ddbbdadc1c | -13.3896 | -44.3736 | 2025-11-19 00:35:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a417ded-57a6-3c1e-bdc7-6c9f21ac3dc1 | -10.7793 | -48.834801 | 2025-11-19 00:35:00 | METOP-C | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1cf4546-17ef-334b-b608-6f29debe5ac5 | -5.6821 | -45.986801 | 2025-11-19 00:35:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1696b5f-16b4-32f9-836a-257275a1d664 | -4.3654 | -43.606899 | 2025-11-19 00:35:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5adff6a-214f-3a9a-ab3c-1490350e6532 | -5.1645 | -42.665199 | 2025-11-19 00:35:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a230a2f2-93f9-378b-b558-1bfd1ef551fe | -11.784 | -44.6157 | 2025-11-19 00:35:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9284592c-c9fa-3985-9ba8-5720a7b00d4c | -5.1545 | -44.4673 | 2025-11-19 00:35:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88e10d2f-73c4-3abf-b8b1-4bb663ba4ecc | -13.367 | -44.772301 | 2025-11-19 00:35:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31fc1291-4c8c-3513-8836-4a649e226c1a | -2.8524 | -45.616299 | 2025-11-19 00:35:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffd2cf1d-2c86-3547-ab93-1ac390315fc1 | -11.8166 | -44.622898 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d43f5793-ea0f-3730-96bd-25a248906be2 | -5.0317 | -43.589298 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b0052ab-b165-33a9-bada-61f34c239f25 | -6.3073 | -43.792999 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20968963-79ca-3d9b-9d3c-26d2e075d410 | -2.8426 | -45.6185 | 2025-11-19 00:35:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57129066-30f8-3219-9421-580d2d825c11 | -6.2474 | -43.669498 | 2025-11-19 00:35:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74de3cbf-a5e5-3f06-a0d1-c18aadafa251 | -8.0348 | -40.952099 | 2025-11-19 00:35:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0993bd52-07ba-396b-855d-a2650d0a8cb7 | -3.7477 | -51.809799 | 2025-11-19 00:35:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27b1831d-c5e4-30bf-9e9a-42f5dcbdac73 | -6.3468 | -44.2258 | 2025-11-19 00:35:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d61f874-95c3-3fed-ad51-28b128e7a92a | -4.9944 | -44.754101 | 2025-11-19 00:35:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae0456d5-0067-3363-ba08-d9bd5f72115e | -10.2475 | -36.373199 | 2025-11-19 00:35:00 | METOP-C | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 924d1147-2776-3f58-b002-5fcdd70fa8c0 | -5.3375 | -43.7495 | 2025-11-19 00:35:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1860423a-3a5d-3006-9e08-26e4f00f37e3 | -12.126 | -40.864899 | 2025-11-19 00:35:00 | METOP-C | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 11b615f4-4596-31f8-bfe9-004df3fbb4c1 | -6.3035 | -43.776798 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 678633ed-fe50-306f-8205-6d18948e7894 | -11.8134 | -44.608799 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bab2cc0d-4f17-3c0c-82bb-33bcaa28d67d | -6.119 | -42.949699 | 2025-11-19 00:35:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74baf3d7-593c-3b58-aad0-fc2f2c3cf37e | -4.6764 | -43.218601 | 2025-11-19 00:35:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80ba72f0-7f86-3534-b4b2-33919f609d68 | -2.2229 | -44.811901 | 2025-11-19 00:35:00 | METOP-C | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d36bcbfd-6557-3fd4-abbf-5ba43f91c3ee | -2.8559 | -45.452599 | 2025-11-19 00:35:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38a1041a-ff5b-399d-a5cc-c43efa5b58dd | -2.2211 | -44.803902 | 2025-11-19 00:35:00 | METOP-C | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb3fc294-3f98-3681-b48c-9241fdc7d4e3 | -11.7905 | -44.5993 | 2025-11-19 00:35:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2a92642-ea51-3580-abdb-1a56545dc452 | -9.3749 | -48.423302 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5c5e20b-70b2-339f-82cd-b86d5d0c3b14 | -11.0259 | -43.882099 | 2025-11-19 00:35:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b48f7b44-f8fe-3054-b7cb-68099f874483 | -13.0744 | -42.138401 | 2025-11-19 00:35:00 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d6a3b844-e55e-3bf3-8ef3-ecad399681dc | -5.0435 | -43.595501 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0064ed1c-ba29-3a73-aec0-b210851fdca0 | -11.8583 | -46.958 | 2025-11-19 00:35:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c76ae8bd-8116-388b-b1a0-2eed151c6b86 | -13.4858 | -44.388199 | 2025-11-19 00:35:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd69730b-ad86-3a69-be28-b79ff814e8c5 | -12.601 | -48.868 | 2025-11-19 00:35:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0dd94f1f-6080-3380-a223-7e25d2fb94ce | -10.3527 | -48.9016 | 2025-11-19 00:35:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
