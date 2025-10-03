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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 488dab53-ef24-34ba-aa5e-6c6ccf68f7b7 | -9.99457 | -50.24694 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68c4d839-6d3d-319c-a150-f2c284511730 | -9.95589 | -48.77469 | 2025-10-03 05:23:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52ab9914-de70-375b-9a51-2ab7236dccb4 | -9.96259 | -48.77501 | 2025-10-03 05:23:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7537f0b6-f64f-34e9-91a2-59cd37ce1188 | -9.4595 | -63.39018 | 2025-10-03 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68e9f1a4-4771-3993-87ba-519c955b4f8c | -1.08494 | -53.68013 | 2025-10-03 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 60ae0277-a46a-3f07-b261-aa009e6a6d40 | -9.79944 | -59.95775 | 2025-10-03 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a555d2fe-4999-3bde-a72d-e31ff20d418a | -3.35098 | -54.72674 | 2025-10-03 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7c7553d-a8f2-3276-8345-4d5e07fae742 | -11.08267 | -47.87535 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14ec1dc0-41b7-36e6-bae9-923027e03a28 | -10.01499 | -50.23092 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5d42e4e1-aadc-3baa-9e01-0a5c14385fcc | -10.00948 | -50.22545 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 846cb57e-7fe3-34dc-8e07-5fcb5bc017c6 | -12.71537 | -48.57076 | 2025-10-03 05:23:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 14619b3b-608d-3a86-a7f7-ecc4f7875bb6 | -10.89408 | -56.20189 | 2025-10-03 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf5231b0-22e3-3847-8b49-31113f5649ab | -9.99646 | -50.21881 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fc63c5a-55e0-3818-bc93-36a9d9bfae47 | -10.00448 | -50.25279 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3335d1bd-07ea-336f-acd1-55de00ec2783 | -6.41149 | -52.86261 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a7ef702-2469-33c7-b0f0-ca7f4a2e7b9f | -10.0078 | -50.23936 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5a64325b-f239-38b5-9bfc-fb466cd47153 | -10.00742 | -50.22971 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 0869c0cc-8425-369e-ac68-78ae48c9b15c | -9.44804 | -56.65403 | 2025-10-03 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bec4cb2-28b0-335b-be93-ba9c5b64eb2b | -10.01331 | -50.24481 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b4d86e3c-ab6b-3efc-b3ba-13064381eaed | -3.0945 | -47.00613 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2e38143d-c6aa-3307-a4af-874e919c3c70 | -2.09992 | -56.83034 | 2025-10-03 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 125b28b4-e810-3c10-98d9-55fa805cf91f | -3.08987 | -47.00721 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bfd63305-5327-3f3e-9ffb-8c932ebb998c | -11.54031 | -49.82073 | 2025-10-03 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8fa2569-9289-3d57-9d34-c29c11b5d961 | -11.09765 | -47.86989 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 59ec16b4-a608-3240-9f20-72d948d6f272 | -3.16891 | -48.60914 | 2025-10-03 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce8d6209-ddc0-31d8-b09c-3f132660b14f | -9.91843 | -50.4992 | 2025-10-03 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43f596ea-9453-3a29-bfe0-de6f04288520 | -10.33842 | -54.18941 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac6f048d-ec07-348b-9651-16e2d58a2d74 | -9.99678 | -50.22842 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 22ce57e1-97cf-39b7-b470-93bd78b76d52 | -11.00143 | -56.92038 | 2025-10-03 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f2e1670-debb-3f9a-8628-ff71146119ae | -5.62098 | -51.93752 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7e5bfb-31fc-3013-9c58-373cfdefe80c | -11.08046 | -47.87165 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 430592dd-9c88-3fcc-82ea-65c1bf6a912b | -1.08071 | -53.67957 | 2025-10-03 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa18f418-42c9-31b2-a4e1-30aa142d1050 | -11.0905 | -47.86963 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6eb75e24-ab8e-3aaa-8cf8-772545ac8726 | -1.41876 | -55.2752 | 2025-10-03 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c0fb1c-a13c-3a49-b8f4-e30f14de69ad | -12.21508 | -54.31887 | 2025-10-03 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9279735f-a6a8-3e25-9a2f-766467edec8d | -10.00018 | -50.23814 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| c4949da2-9754-3704-a6bd-93b2568a1f2a | -10.12684 | -52.3478 | 2025-10-03 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5f29c71-478c-3bf7-af58-c007af309bba | -10.41319 | -54.41014 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dbcb2a28-5728-3a03-a08e-6e6019263a13 | -10.00644 | -48.27371 | 2025-10-03 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 67d9cd3c-cf86-3096-adca-48fdcc64a488 | -12.9331 | -48.43594 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdd42a72-adf8-3a64-985b-4bd30961a601 | -1.08433 | -53.68407 | 2025-10-03 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0024a479-c963-3125-8ab3-1b17e0775a49 | -11.11723 | -47.8637 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e07c5e58-cae8-351d-b2a2-0942b75669bc | -9.45123 | -56.65955 | 2025-10-03 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04fcc320-56b4-36db-b197-e5fffc62e94d | -10.01443 | -50.23556 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4cf4ccb8-dbcf-37a0-b030-fb8a12dab56e | -10.2881 | -50.30037 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c61a463-7411-33a2-bac8-6a4ef4139487 | -9.99705 | -50.21418 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9eeff9d0-8f1d-3332-bafa-2a3d940e9a41 | -10.85713 | -59.12148 | 2025-10-03 05:23:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b275d139-576d-3e81-acbb-45cf16d686e9 | -9.99901 | -50.24737 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 452a07fa-ba6e-3f6b-920f-324e9f5320e3 | -2.97333 | -53.09026 | 2025-10-03 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc3d3b32-6bfe-3a23-8a53-d422bdacd1f4 | -9.99512 | -50.24231 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ef12589d-5420-35ae-8ae7-ed8068ec0293 | -12.9317 | -48.43858 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2ff8839-b317-371a-97bc-b0800a7eba7f | -11.09466 | -47.87313 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d87b66a7-ef3d-3f7f-8fad-003ac33c2f68 | -10.00136 | -50.2289 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 786c1cf0-b74a-32e2-95e0-dc9af55afe67 | -9.9905 | -57.82259 | 2025-10-03 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94dd55ee-a996-3f8b-b496-9054d5f4dd56 | -1.08132 | -53.67562 | 2025-10-03 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b24b2a71-301b-3158-a974-a77f6c0573be | -10.00613 | -50.25322 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff29a350-4316-3274-81af-f7670f59e9e8 | -2.92375 | -48.30972 | 2025-10-03 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 24dafd49-13fb-3738-bf09-51e5e2193744 | -9.88483 | -47.81508 | 2025-10-03 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 17f78665-16ed-3ae2-beb4-9c16dd073bed | -11.28962 | -47.83861 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc33a2cd-6185-3aee-84e4-69af1369c9a0 | -2.94266 | -51.27324 | 2025-10-03 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3289140-c7d4-3839-904c-776891c0fa86 | -11.1069 | -47.826 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61a7ed90-1bdf-3a3c-be06-773fad034519 | -3.56082 | -51.12544 | 2025-10-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b7117cc-6f4d-30cd-b3a0-c4cd83d4bda9 | -3.1937 | -51.02898 | 2025-10-03 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10712aad-6e21-34b5-9a60-e2bd93459dc4 | -12.75976 | -50.55326 | 2025-10-03 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54b6213a-84c2-31a2-ae9f-3067a6f6e0e3 | -10.96946 | -51.08434 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d63629a4-be9e-37f3-b4fb-10e349f02fbf | -10.00371 | -50.21036 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65dd4b84-9ac9-317c-a6a6-745518b2a928 | -9.99072 | -50.22758 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22aa850f-3c8c-33ba-8280-2a899b37bd67 | -9.28174 | -60.53915 | 2025-10-03 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e1f31f2-7e4b-383c-a461-01ab9cd9edd0 | -10.34054 | -54.18877 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67d1b04c-5747-31d6-a0e6-6ec29ccadc60 | -9.99412 | -50.23732 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5a460d0c-9bb6-36c6-be38-ab129addd96d | -9.99623 | -50.23305 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d16aa4d7-a085-30d7-8b40-a462c0b4ce51 | -2.25359 | -47.87971 | 2025-10-03 05:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 01d1fba0-ac35-37e5-9150-0b5f0db8644f | -9.87774 | -47.81485 | 2025-10-03 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 968a125f-c209-3318-a66c-587374ea7c5e | -11.90586 | -54.82757 | 2025-10-03 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1d0d5bc-6a3e-3a2b-b6d5-b6a42d8e3d12 | -3.30605 | -53.8544 | 2025-10-03 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9af6a358-8d6f-3d81-8696-05d3524178c4 | -3.09177 | -47.02451 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 370081c4-61f8-366e-8f75-1edb2c2ea167 | -3.09654 | -47.00883 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 26e1bbba-4b17-31f1-8745-00254cea5cb5 | -10.60581 | -48.71431 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 882eabfa-2fc6-34b5-8503-aa12ed42b436 | -11.3116 | -47.83556 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e2efe57b-2ad1-3987-b5a3-348a2293166c | -11.62831 | -47.99025 | 2025-10-03 05:23:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67c06735-31a6-381a-aba2-41b6e93da191 | -10.59845 | -48.71894 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dde1838e-00c1-30f9-b185-e17902af890f | -10.21733 | -53.87654 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4e1320d-db70-3ed1-84fa-c0b8a54477bd | -2.92509 | -48.31177 | 2025-10-03 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c9d1aab0-b6ff-371c-8aed-a0e25e9b74d9 | -11.62906 | -47.98317 | 2025-10-03 05:23:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 818229f9-4cf9-3752-b34b-725795064ebb | -10.00892 | -50.23009 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 45f493b7-b874-3d91-8cab-694dec2b9135 | -11.11656 | -47.8698 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 01bdaef8-fbe6-3f9d-a6eb-403085f79f11 | -1.08976 | -53.67681 | 2025-10-03 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39931a2d-383d-3a81-9bd2-21f7b3fff495 | -9.56128 | -57.99514 | 2025-10-03 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d31d2768-23ee-3099-b0d0-4abe30ea16c3 | -9.45123 | -56.66118 | 2025-10-03 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af96653e-d733-31e5-8578-38bf99c2a034 | -2.04877 | -56.43242 | 2025-10-03 05:23:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3089565b-3e85-3146-b7da-41a92109c459 | -12.21576 | -54.31362 | 2025-10-03 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e242c25e-2de3-326d-ba80-9aa68d258298 | -6.00878 | -52.38471 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 830061df-c379-3d11-8aba-33eacd1b2c03 | -7.26283 | -48.48194 | 2025-10-03 05:23:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7701cb63-9051-31b8-a4fa-3e8b8a0772f2 | -3.09568 | -47.01494 | 2025-10-03 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 80801841-ce3a-3939-8d0c-94afc990abb4 | -11.0762 | -48.36272 | 2025-10-03 05:23:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eaf06e1-577a-3323-b0b5-139b62d9cb99 | -9.46012 | -63.38639 | 2025-10-03 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6779562f-fa5a-34c4-96de-6529bd2b561b | -3.93444 | -47.5632 | 2025-10-03 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 838e6005-5125-342d-98db-dff1c7980ff8 | -10.96996 | -51.08016 | 2025-10-03 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| fab9595f-1c74-3b6c-934b-992f422e0e1a | -12.93855 | -48.44098 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aea0d914-acd2-3fe9-84e9-ea3f84025324 | -9.83433 | -58.07495 | 2025-10-03 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README135.md)
