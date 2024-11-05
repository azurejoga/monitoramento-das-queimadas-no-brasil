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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 984e1544-99b8-3078-a273-b9c1aa4eae8f | -2.87794 | -51.31005 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd529b48-8d57-3ae0-95cd-51e210c5099a | -4.59633 | -49.51931 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e06befee-8afc-336f-8bad-6cd77dbaffea | -3.55446 | -47.38998 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f3349de0-94f1-39ad-abd4-8282a8f447b8 | -4.08067 | -48.31319 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 328b9029-ba1d-3197-9126-ef3ae3642cbe | -2.77536 | -51.60897 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a006142-8c54-3222-82ea-538fea9c716b | -4.5434 | -48.83005 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d417c631-aa25-3a54-97fa-721644572dc8 | -3.21769 | -53.06455 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7616106-41c3-37d1-8630-edbbe1f04539 | -3.00065 | -51.21964 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56fe7dac-4c5e-3b32-b264-20c21dcfa9d0 | -1.38369 | -55.42425 | 2024-11-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f903a1f1-4d5a-3e5a-bc37-d7475c9ff3c5 | -5.83826 | -46.27488 | 2024-11-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bdee361-5406-354c-ad2a-eaab17badb13 | -2.78159 | -51.61369 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 389d28df-c93f-3366-9544-d417cd679a74 | -3.03953 | -53.26956 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a6b11c8-527b-3ada-a524-bd135bafdedd | -4.88481 | -46.7098 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fe7f892-5c13-369e-900e-dba306484ed7 | -3.45666 | -47.67036 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a1d4c79-2f0b-3e9d-9be3-a77a16998c48 | -5.6611 | -45.2071 | 2024-11-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df53ea3e-004a-3a74-a535-25db856dd4b0 | -2.90192 | -49.39391 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f64ab12-6808-372f-9895-f5d4f6b16914 | -3.26594 | -50.34355 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 310dbc05-69ee-3da8-ae3d-b1cfd9074ecb | -2.27626 | -50.78442 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c978dd84-6380-3752-b98b-ab21debbb772 | -2.8167 | -52.93496 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19fa5e21-cdd0-3858-85a1-ff74fe0635d4 | -3.96214 | -48.15803 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92fa8345-1cfd-38bc-9874-146e0b380511 | -1.49938 | -54.86517 | 2024-11-05 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94b24ed0-46b1-306f-91f7-b85d78fdecea | -2.89047 | -49.26368 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a95a5498-72b6-3104-b656-b821ebc07346 | -4.56336 | -50.24574 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99f7987c-d0a0-3d85-b189-9db031afff4d | -5.37319 | -46.45466 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31be0083-292b-3300-b571-3bd38e03f5c1 | -3.45241 | -47.66959 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9ab63d-63df-35a4-af11-f500f49953db | -5.4209 | -48.14093 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d46587a-5072-3eb8-9488-1fde63ae71da | -2.18988 | -53.24849 | 2024-11-05 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a79d417b-3bf6-3049-be4d-c519eadbc67f | -2.7867 | -51.60323 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31674c70-1a40-382c-a8f3-6f98407edad4 | -2.84498 | -48.44952 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bf0271c-2849-3ddc-97c4-a5ddc49ac5df | -2.45145 | -48.87237 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 143abfab-9f51-3d0b-b1ea-5c4c26d32656 | -3.45727 | -47.66638 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4098ed6-1737-3137-be9f-15c706fa1176 | -5.51623 | -48.08037 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20ee866f-4386-337c-8ef1-0e01aff55ba6 | -3.12713 | -51.10615 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89f414dc-c99c-3e41-85ba-0be724b95f54 | -2.49922 | -48.74361 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce224ed0-2069-3174-818a-03411dcc3dd9 | -3.64112 | -50.13666 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73e5b08f-9255-353a-ba6c-517802c1863f | -3.35505 | -50.12439 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3adcb9c-b535-33fe-aee7-84d6b677739e | -7.1364 | -46.01197 | 2024-11-05 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb50e61-08e6-3770-9570-03b6140e0fb5 | -3.85697 | -52.13969 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2ee7294-5c3c-370e-9dc3-1790f45cfd96 | -6.11036 | -43.96302 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 239e96f1-87c5-33f0-b727-6d299002d520 | -3.80654 | -51.14207 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f560654d-2343-3fa2-98f8-47bbf4d100c0 | -4.42518 | -45.84834 | 2024-11-05 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaf19d2d-d603-357f-87a1-12f38d508c02 | -2.24155 | -50.70742 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad017779-5de5-3cee-b5b9-a6e8b7ab80a4 | -3.96488 | -48.94169 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d52fbfe-f227-3685-ae4e-2dad390a288b | -4.58437 | -48.07022 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7cf84dde-320d-36cd-b523-bfb5ce7bf7bf | -3.1043 | -50.2958 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3ddf574-65e0-3ba9-b99a-d6910b620e40 | -3.944 | -45.57041 | 2024-11-05 04:55:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1c154631-d7cc-3de7-8396-3444c091aeb6 | -4.24339 | -48.03863 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 457d782e-985b-3e42-8883-ca12436117bc | -3.12017 | -51.10511 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e1f1e57-0041-35f3-817e-ccfc617267c4 | -3.08369 | -54.51812 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fa6e3b3-7af0-3d0e-96d3-8521dd79e90b | -3.5181 | -51.3621 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195e38cb-8c6a-3ae2-914c-bb5ec63f7d20 | -2.75593 | -53.21434 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aceacd56-87b4-3675-be5c-e3a651419def | -2.90624 | -48.59685 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2262d8d-b535-3099-b821-a96f8bccb9d1 | -3.54766 | -47.37584 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| b79b334a-7d68-3dfd-809c-7ca093dedd88 | -6.51899 | -45.93736 | 2024-11-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cc28aa0-f66b-3b9c-8d58-40b1c225756d | -1.88128 | -51.11457 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96bb92a1-9604-373f-8ba8-46f790c6fd3c | -5.98117 | -45.36781 | 2024-11-05 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d873acda-a114-307b-b74f-bb641ca3b24c | -3.24566 | -52.2114 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 106f1269-113d-3b71-86e9-37b3c20b963a | -4.5337 | -46.73613 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e368ab51-8ec4-3e49-8b1c-7812a16c56e7 | -2.45534 | -48.87295 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd269849-bef8-3ea8-b1b2-d8af796dc257 | -3.55325 | -47.39797 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09d46f3e-b3da-3cc5-8c37-ba351706acb4 | -3.08147 | -54.51057 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe7c18f5-ff5e-3b05-94ee-9f18c9ec7831 | -2.45604 | -48.05158 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c669d0a4-257a-3d18-9592-af1cd4a9f7cf | -2.20908 | -51.75676 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65b6b181-a6a7-39a8-b6b5-64a3e44e105a | -3.4792 | -50.38348 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab742cf4-2f4c-333f-bd71-93c49a1fb49a | -1.49715 | -54.85735 | 2024-11-05 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec3c991f-57a1-3129-b939-585ce79c2319 | -4.01629 | -51.02174 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb922d02-85a1-3b90-b671-7c85e4042f6e | -5.12128 | -45.15991 | 2024-11-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a05d132-350c-35d5-a764-3451553631d6 | -4.2621 | -50.71973 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd0e9f68-ec79-3c07-a19a-3add9fd2b76c | -2.91973 | -48.31273 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d28c6ff-f240-324a-a7ee-0a49c0619ac2 | -2.5536 | -47.49268 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd14cbbc-988e-3371-b7ae-940aa79f70f7 | -2.63476 | -48.02956 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bf8d685-51b3-3bbf-a5a8-e352f0655445 | -3.11261 | -51.10791 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b85a4355-9b88-3392-a51c-00f04676b367 | -3.04779 | -51.06652 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b01842d-4968-3320-b80f-ae9ea98378bb | -3.24511 | -52.21496 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33d2ff30-b96f-3338-81af-bc555992c0ad | -3.40646 | -54.51897 | 2024-11-05 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3495c88e-d605-3f18-8097-8fe30734aacf | -3.01484 | -53.23044 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dc2ebf5-8bcc-35f4-8d45-26df0b50b0cf | -5.51194 | -48.07977 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66578537-98ad-3397-b127-2a605aa3eef3 | -3.29279 | -50.02004 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39f09fed-f2b0-33f0-a8e5-7ae3f25a3ab9 | -4.60216 | -46.87505 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f51585a-b5e8-392d-a46c-731dad0c30f2 | -2.61723 | -51.72631 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cae18042-85d2-37f2-a984-556c0f89d063 | -2.08 | -53.23482 | 2024-11-05 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f4b54943-6fc9-39fd-b212-21b966b38a33 | -2.90668 | -49.41349 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa087377-537f-3f95-81e0-338309f88040 | -2.93306 | -52.5378 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e6f1a0da-ff51-3bac-bcf3-ce4d661577ab | -2.2152 | -51.67285 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63cd39ce-c1c2-34fb-8a12-75d5682e5813 | -3.03791 | -53.27986 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de41728e-a5d0-3df5-863c-0e4404f3f6c3 | -2.86682 | -49.39513 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf87431-d921-33de-a4a9-a9aa81ab2909 | -2.82765 | -48.34608 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81586157-80cd-3e31-b520-8acb5efc58a2 | -2.81892 | -52.94238 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 802c95de-ecc2-353b-812e-fc02d4411bc8 | -2.90226 | -48.59624 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b798eee5-94d4-3a5f-8c76-a6f97979f971 | -3.29078 | -50.03295 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02476f0d-85f2-3e58-98fe-6223927c10b3 | -4.26378 | -50.73257 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d9a39e6-ac88-30a7-9514-39778695a6bf | -5.8343 | -43.6487 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a5166b47-4059-37c3-a9e1-9e67e8cacb12 | -4.10535 | -50.23181 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dc679f2-9dff-3d81-91d8-e6e2f9518f7b | -3.80936 | -48.88008 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57d104be-d4d8-3460-8821-aa6c94ea87d0 | -4.7788 | -43.64734 | 2024-11-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c9516a4-3bfc-3ec5-a1eb-912101a1cfc7 | -3.16994 | -46.60973 | 2024-11-05 04:55:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d6aa8b7-10f2-3b78-a9d2-bf4490d5648b | -3.47985 | -50.37936 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d20bb6a0-a1ff-3a42-8af5-e49e781d5a96 | -5.69587 | -45.834 | 2024-11-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8217e54-80f0-31ca-8db8-8a522441eba9 | -2.17537 | -48.86401 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 205abb4d-475e-3bbb-91b0-716c439bf0d2 | -2.78953 | -51.60742 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README24.md)
