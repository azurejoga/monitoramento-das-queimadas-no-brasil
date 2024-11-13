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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afd9edbb-4122-3904-a94a-f8ac2a1cb2dc | -1.41554 | -51.11641 | 2024-11-13 04:04:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6e2c687-a23a-3c45-bb47-3695f0518914 | -2.60828 | -46.17361 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5019373-fe4e-3df6-8d16-388c5908779d | -3.35445 | -48.96975 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d9cff39-c078-3b1c-9667-efd16b91a84b | -3.25265 | -50.39974 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ab4d62d-4f14-3e4f-912e-42f4b43d5edf | -3.09491 | -54.31546 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf595f84-a867-3a8f-98ba-92a27fb036d2 | -4.05833 | -48.32302 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adf7eeed-2f85-3736-932b-32ae14779f8b | -2.39897 | -53.73749 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10157bbf-bdb0-3442-af1e-3b0b15a53de3 | -3.1647 | -50.45109 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca34508-df11-32c8-9376-4e1cf4de1898 | -2.68567 | -48.66603 | 2024-11-13 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7247712-c395-3a2c-a93b-0b1c0e269e8b | -3.25814 | -50.4007 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034ebf1d-e846-39d0-95a2-e9ec4f3f1607 | -2.78651 | -48.08404 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41d6701c-23d7-3afe-b633-d1717e6e19fc | -1.65088 | -47.47459 | 2024-11-13 04:04:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0494b861-a4b8-3c77-8932-5fe543166f7b | -3.51568 | -49.95601 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7628f179-db4c-3feb-8247-aac89a8f1ef6 | -1.65226 | -52.63042 | 2024-11-13 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f31693f0-1b7e-3435-bad4-4a15e7085f9f | -3.34355 | -48.97377 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3ddc46ef-0837-399c-a358-ae148581f610 | -3.02224 | -50.97916 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a716a31-eb49-31fa-a313-03f45fca867f | -3.99028 | -48.3147 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d2c59e6-6d38-357d-819a-53f3d512810f | -2.24036 | -53.75299 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98c021fe-cc94-3228-a33d-a6afc79b2cba | -3.29404 | -51.59925 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1997d8c5-5be2-30e3-b9bc-883a02b071c0 | -2.65537 | -46.7925 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd1f2ce6-2049-351e-9c10-4c9f362df27d | -3.52096 | -49.96618 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11d11dfd-39fa-3994-a99c-e32694eb0cde | -2.97708 | -45.1641 | 2024-11-13 04:04:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71c08186-a52e-39e1-b572-e113f2e37c98 | -1.98375 | -51.10158 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99c918dd-43a1-31a4-8e36-0f0645d5d94e | -4.00312 | -46.53194 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d96b92c-7a5e-3764-b14e-405259805820 | -3.33671 | -48.9853 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfcc6367-7939-34f0-b0b1-79c732598b59 | -1.82262 | -45.91996 | 2024-11-13 04:04:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 027c3a1d-1eb3-34da-9f30-bf89b93d7d77 | -2.24622 | -53.76032 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 96899a27-ed68-3827-b469-f2c8a8f371b5 | -3.95232 | -46.41538 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| eaa78bb0-3a04-352a-aca9-2e7b6f878a10 | -2.98798 | -53.98298 | 2024-11-13 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8165bae-053b-3cea-8edd-018e23c6cca3 | -3.16169 | -48.36966 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 645310c7-71d1-316f-a791-08ece361f7e1 | -1.65013 | -47.47939 | 2024-11-13 04:04:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6733da6c-3e05-37db-8c2e-53975b9b3fc7 | -3.95066 | -48.17526 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| df40b7d4-8f74-3639-adb9-33b301949cf7 | -2.31503 | -50.68925 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5db2fa5b-f241-33ea-b3fc-c6f823e77265 | -3.34654 | -48.95773 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 7cadc60e-c57e-39b0-bcbc-e7723599fa03 | -2.11593 | -50.68903 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55966430-38bc-3914-aeae-7f4c4a37c0a6 | -3.07642 | -50.33647 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c66e085f-960c-38f3-8b52-80b14002cece | -2.46609 | -50.12701 | 2024-11-13 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 97d9c643-273a-3c67-b85d-036ca1d41af6 | -1.97307 | -46.57369 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11487fbc-0be0-3c48-893f-c5e26b96cff4 | -3.51454 | -49.96264 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 196b12ea-567e-368b-bc05-7f84850c1901 | -4.06593 | -47.96633 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 356b71e6-91ea-342d-9d43-ce6561a66e05 | -2.65358 | -46.83062 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| facc28b7-6b92-3d37-9110-2ca4d9289edf | -3.33452 | -48.96637 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 992ad085-18e9-33d7-a145-e79361484629 | -3.02429 | -50.97413 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ff6d529-9e3b-3518-b21a-2bece555476c | -3.49414 | -50.84226 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ba09442f-b1c2-3c29-a1bb-2f47ae22dbc5 | -2.65903 | -46.79736 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c561840d-e83d-32c4-86c9-b9aad104256c | -1.82202 | -45.92368 | 2024-11-13 04:04:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93e67ff8-1a7f-3907-b6f7-ac219ea12fe3 | -3.35165 | -48.98794 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00f5aaeb-6466-3384-a0e5-a1bbe5912d97 | -2.63694 | -46.1656 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 547a5efb-b5c7-3583-90dd-3999c7a67483 | -3.39832 | -52.47444 | 2024-11-13 04:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e49620d1-c4d4-31f7-8701-133cc0c13ed4 | -2.52992 | -47.09195 | 2024-11-13 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e99e595-2ad0-353f-b95e-61855eeaefc4 | -2.66203 | -46.80623 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8160f05-0df1-3944-817a-b7a7aa139855 | -3.07582 | -50.34002 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f4e6bcc-cdf8-3f1b-90b3-681e11f73c72 | -2.81723 | -46.65448 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5beb758-bd2d-3d6f-88c5-038b31cc5e3f | -5.79764 | -35.58318 | 2024-11-13 04:04:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4340121f-6575-306f-b652-77e6be831d7c | -1.59821 | -47.00401 | 2024-11-13 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3ba64e5-5bbe-3be9-8b4e-3d2747cb4d12 | -3.20989 | -46.53069 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78bba624-61b1-399f-a2a3-2b083e0798e7 | -2.34263 | -48.59819 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ec4dc16-bda3-3a70-a954-d314d75baef3 | -4.13527 | -40.63338 | 2024-11-13 04:04:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 90d57e46-131e-3c28-9bfb-7dfb87f5faad | -3.05446 | -50.33283 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ad53e65a-2305-3dea-a24e-0c0f7ece3ab5 | -2.9836 | -51.24697 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dce60fc-76e2-3b49-80bf-8b45f7708f45 | -1.38334 | -52.39838 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4c96ad1-e416-3152-85eb-c874a0940040 | -3.05756 | -50.34797 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98fe0d05-0f65-3561-8816-4565ec75ee9d | -3.3446 | -48.9691 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 28f3d015-412f-38ca-b4ee-f64a9b82a1be | -3.84167 | -46.0167 | 2024-11-13 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 092e94f6-dad9-36f7-9f5c-f4fb21a7c3b0 | -2.47213 | -50.12439 | 2024-11-13 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc49eedb-2ed0-3783-8211-e734db696143 | -3.02351 | -50.97137 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 997d59eb-a250-35ca-88f0-cbf95aea1baa | -2.2393 | -53.7594 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e2546693-aa5b-365e-863c-63cf0580b52c | -3.50043 | -50.8394 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| da7afe38-5b09-35a3-946d-79703fcc2287 | -3.5433 | -51.59479 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe6580a0-3ae6-34f7-9739-85340649a5be | -3.06603 | -50.33112 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4e36b8dc-e4c7-3eec-849d-b25390c11bf6 | -3.19163 | -50.28973 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 032f2771-d60b-37ea-b3a6-d31e2dbdbea3 | -3.94902 | -48.1851 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ad174367-88ab-393b-80e8-8c6e026673d5 | -3.34262 | -48.97953 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8f9addac-be80-3703-a6ac-1cf70ca5de1c | -3.9927 | -48.33863 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 264337e0-01fc-3e4e-bdae-f18daa6df5c3 | -4.13581 | -40.62993 | 2024-11-13 04:04:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee54248a-3b7f-3c0e-862d-7fdfc0a59a00 | -2.72535 | -51.8331 | 2024-11-13 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce0aaa8-1af1-39b8-81c7-feeae4f81fa1 | -2.77594 | -50.30539 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17cc4500-58b9-3742-926a-9858df6cb24b | -3.06975 | -50.34262 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd1eab64-a9f5-30d7-b56e-e79211e1ba26 | -3.3395 | -48.96725 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2638bb7e-ab61-31d4-8396-9e86c0821ef8 | -3.04229 | -50.33801 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 763d5fb2-d263-3bb4-b548-048e2e4c4480 | -2.56083 | -49.11707 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 631fc011-04a5-3fef-9786-0bf61725eeb9 | -5.45834 | -43.24815 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51c8bc64-ffe5-3501-81e6-b27d8b5b4193 | -5.97453 | -46.3002 | 2024-11-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1283aec7-251a-370f-9d71-ce18282eface | -3.97173 | -50.9366 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9864fde9-bd5b-35e8-b73f-82a086b50f4c | -4.33525 | -50.4282 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b5066a79-21ca-34cf-a657-3bc4c7426824 | -4.41665 | -48.85595 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2fac859-0da6-349f-868b-e0ea60dd3133 | -4.51635 | -48.9351 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c050babf-144a-3634-a349-4efc9918e4f8 | -4.3306 | -48.7233 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08dd14f0-203d-3681-9367-65158f155e19 | -4.3241 | -48.61439 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4da89ea5-d7b7-3f4b-bca4-59db6bf82d2d | -4.60229 | -46.94617 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3b82d74-80ad-3aa6-8d53-cbb1c72cfb7b | -5.25095 | -49.7961 | 2024-11-13 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1f8c772-ee63-3b79-bcfd-56b9c5ac9554 | -5.35789 | -46.06741 | 2024-11-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70f91c11-00ec-3936-bebc-f5bd395e2ea3 | -6.96708 | -40.3752 | 2024-11-13 04:06:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 78f321e0-15d4-3b6a-ae8c-c23ce1ab4cec | -4.41849 | -49.72326 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d8f4c93-2648-3b74-853c-86efbe4aea06 | -3.98644 | -49.94638 | 2024-11-13 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f9eb9a-a642-3974-91ce-8ae8a9365f98 | -4.16047 | -50.75307 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fea9475e-759f-3393-9e91-ede5f1a24458 | -3.25107 | -54.53981 | 2024-11-13 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edf62fdc-84c6-3c07-9617-29f0b1fc63ba | -4.33043 | -50.42381 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7dda3fea-f49a-3785-8790-e459a33f9ba1 | -4.40908 | -49.64109 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4887f7a7-7423-3851-923a-e92db1ba7776 | -5.70093 | -45.67121 | 2024-11-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
