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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b445be49-60b7-3a60-8f8c-1b980e0d6ca2 | -3.25386 | -50.3424 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 77d840cd-af1f-3a76-821b-69cf5a41945f | -3.25208 | -50.35389 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f27eff38-aa81-368c-89f4-831b7da539c5 | -3.22803 | -50.18081 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| aaec7863-a3a8-32a7-ba2c-af13328eb769 | -3.22631 | -50.19208 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3c792e8c-1ee6-3ce8-89a1-fac4eb46d0a9 | -3.20264 | -45.00268 | 2024-10-30 05:27:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1b7ff5af-8432-3b00-80f2-e18b0465e2b3 | -3.20117 | -45.01256 | 2024-10-30 05:27:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2843626e-9623-3b0e-91bb-f5562ff8de3c | -3.18667 | -50.38455 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9fccadf4-2f5b-34f6-97c2-24240ae0158f | -3.17641 | -50.58766 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d52ef889-7f0a-3ee5-b151-c055459eedfa | -3.17459 | -50.59964 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3ee38c41-f47f-3332-9bc3-266eec521d1d | -3.1662 | -50.58613 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 756b0598-1ac4-3fed-aebb-c31c7df0b164 | -3.1607 | -50.62212 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 49a88641-bc28-3d1b-921f-0cab4993166e | -3.12431 | -49.2908 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2075b096-5a84-39b4-a8a7-682254cbe1ea | -3.12071 | -54.27506 | 2024-10-30 05:27:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8bd1bdfa-4761-30fb-9cf8-3eeef003fc01 | -3.10702 | -54.27291 | 2024-10-30 05:27:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 85ffaf56-d4ff-3e9c-9083-551f861aa76e | -3.09924 | -54.26695 | 2024-10-30 05:27:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 2e134c6b-66aa-397e-af8c-de3b5ce66950 | -3.09574 | -54.28986 | 2024-10-30 05:27:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a9f49098-f667-39bd-b28c-3a7057c15681 | -3.04979 | -50.41116 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 994240b3-0275-3bf2-86a6-39d323d42271 | -3.0472 | -50.41785 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a4325243-68b8-3a6d-b89c-f97513749b63 | -2.9135 | -52.58757 | 2024-10-30 05:27:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 660bda64-c127-3bd1-b121-6a409268bcee | -2.91336 | -48.60476 | 2024-10-30 05:27:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 755a27a1-9236-365c-898d-5d56dd09429d | -2.91194 | -48.61419 | 2024-10-30 05:27:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 684ade88-6722-3fc8-9998-be24eeeaf977 | -2.85807 | -49.44694 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4ec1807e-fa58-32b6-841f-35ea6bc96040 | -2.84609 | -49.24084 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a5179d1b-dff7-3cbb-85cd-a6bd81bee035 | -2.83818 | -49.22938 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| d5585401-433e-3428-9fcd-f632ee47e8a9 | -2.83667 | -49.23944 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 22e207e1-7a8e-3f38-9b4c-720d44312794 | -2.82876 | -49.22799 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e5d4bd29-6274-3788-94b5-68c975f6ec5b | -2.82725 | -49.23804 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 34ff3b1d-1103-39c0-b315-3f3e6f0bdcec | -2.81145 | -49.21519 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7bc1ee4c-a304-33b7-9125-bf7453c1111c | -2.80052 | -49.22381 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 33724a69-a17f-36c5-85ae-542a7fc82a0b | -2.79026 | -49.48312 | 2024-10-30 05:27:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b80956d-8d24-3968-acaa-4b9db1751cc2 | -2.72711 | -48.73967 | 2024-10-30 05:27:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce0f52dc-3bc7-3f3c-a5d5-350cbdd92639 | -2.7225 | -46.67783 | 2024-10-30 05:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c910cb0-87f0-3d2d-895f-a312612b580f | -2.72118 | -46.68664 | 2024-10-30 05:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0ea4e8a6-060d-3365-b448-9d6040279105 | -2.71987 | -46.69544 | 2024-10-30 05:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 29f2df62-6a0a-3606-85d9-55e928bc56b5 | -2.71855 | -46.70424 | 2024-10-30 05:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5a867026-7e5a-3b18-bc8a-d65b4f488748 | -2.6956 | -48.63761 | 2024-10-30 05:27:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ca0d998-2e1a-37f9-a3f4-5586d74deea2 | -2.64415 | -51.74039 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a6cd8852-7f12-3b1e-b97e-5ba713e60365 | -2.60687 | -48.24917 | 2024-10-30 05:27:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0211784d-9ce5-35c1-b11d-f8a58e2e5862 | -2.60549 | -48.25842 | 2024-10-30 05:27:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33ee6a73-51a6-3700-8371-f985cabcb5ba | -2.54252 | -47.50856 | 2024-10-30 05:27:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1085e691-28da-365f-a720-d986bc6c5951 | -2.52509 | -49.08311 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 97291223-bc74-355b-a9b8-a3daa9a73724 | -2.52357 | -49.09304 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 31437a9f-d1ba-3336-8f1b-618ad8ac538e | -2.51283 | -49.16307 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 654717d7-9af9-3183-92af-5cd9144f83a4 | -2.4239 | -46.70524 | 2024-10-30 05:27:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 04a6017c-a66d-3a21-b944-723288237b1c | -2.39164 | -48.57763 | 2024-10-30 05:27:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0bf02f60-98be-3f28-9b4e-b586764acc7e | -2.391 | -48.93967 | 2024-10-30 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f5c5748-e81c-3d90-8884-5625c0bd50e1 | -2.36469 | -50.32605 | 2024-10-30 05:27:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9d292427-bb58-3070-8a10-5dbc23c72e62 | -2.34038 | -46.64246 | 2024-10-30 05:27:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82ad3515-207b-340a-bcff-5bc55bbf86f9 | -2.20291 | -50.57877 | 2024-10-30 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 504bb42b-5f72-3d17-8ee3-d6bb48e12a61 | -1.6008 | -47.13174 | 2024-10-30 05:27:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 37ef75e9-edea-362e-a428-1ce5d90afeec | -1.59948 | -47.14056 | 2024-10-30 05:27:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e3577418-1cf5-3263-b5c5-9ce84c22195b | -12.9 | -45.04395 | 2024-10-30 05:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| efa08dd3-c79a-3f71-9909-f2951d1e94ad | -12.89824 | -45.0573 | 2024-10-30 05:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 00a886f1-7161-35d0-a5be-fe23f557fb7f | -12.88769 | -44.61263 | 2024-10-30 05:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 860dfdb4-4888-3755-a9be-b7d29f30318b | -10.71473 | -44.91323 | 2024-10-30 05:29:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| f70ec5bc-14fc-3c27-a5a5-79b283a897a7 | -10.71302 | -44.92583 | 2024-10-30 05:29:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 691510b4-c207-3b14-8420-e94ee02babca | -9.05096 | -50.00586 | 2024-10-30 05:29:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6b89dfa6-69b8-3938-af72-5e24625a2f8f | -8.95783 | -47.63367 | 2024-10-30 05:29:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9f2b819f-03d8-3333-aebc-6d8a85058ae3 | -8.85335 | -49.85873 | 2024-10-30 05:29:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4ecb66e-f7ed-3698-9193-5ad85f1ad64f | -8.84568 | -49.84784 | 2024-10-30 05:29:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1aefe120-42cf-3e0b-9e98-262bec8743b9 | -8.84423 | -49.85735 | 2024-10-30 05:29:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| e42cda92-88b0-3011-a882-0728e4682770 | -7.88523 | -46.89465 | 2024-10-30 05:29:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ac291e2-6791-3817-8235-7b224ec02d15 | -7.88387 | -46.90387 | 2024-10-30 05:29:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afe2bbd6-3c5d-3a7f-942d-d8e1101a95c7 | -7.48814 | -47.14761 | 2024-10-30 05:29:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4584d882-a002-31bc-b47e-e9174759f825 | -7.4868 | -47.15665 | 2024-10-30 05:29:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d870a8c1-7ac5-3ae0-a272-368484afaa65 | -6.8897 | -46.83161 | 2024-10-30 05:29:00 | AQUA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c76857ca-36ca-3f2a-bf14-12c4e42b5867 | -6.88834 | -46.84075 | 2024-10-30 05:29:00 | AQUA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e25a02b3-97c8-380d-8df7-5022e8b29da6 | -12.63235 | -46.87272 | 2024-10-30 05:29:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d97ef03b-3ca5-3a29-9094-5d24059e1751 | -11.78562 | -47.07435 | 2024-10-30 05:29:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ec1bc378-dd51-315e-98d3-3cf206545bfa | -11.66279 | -48.79805 | 2024-10-30 05:29:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15e19915-3030-38d5-b350-3a837d26faba | -11.65527 | -48.78773 | 2024-10-30 05:29:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41958ad2-392f-3091-b85b-e36bff2e5096 | -11.65393 | -48.79672 | 2024-10-30 05:29:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 704083ed-10d2-3c27-ba81-73774d1216b7 | -10.34494 | -49.64312 | 2024-10-30 05:29:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| c87028b6-e833-39de-b13f-9885c6e70a8b | -10.34354 | -49.65231 | 2024-10-30 05:29:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| f00fc07d-bb99-3065-9442-451051ac0d58 | -10.34214 | -49.6615 | 2024-10-30 05:29:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e28dddcb-eb45-3ac2-b903-4919858ec1fe | -19.62694 | -56.69353 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 94414550-fc9b-38b4-a47c-6098978bac42 | -19.62368 | -56.71152 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| ec9432c3-6502-3db2-adf3-fe44c6ddcea5 | -19.61498 | -56.69107 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 8785bbfe-465e-3c99-b945-75e65abdec3d | -19.61171 | -56.70905 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| e084763f-bde9-31fc-a8e2-c53d9177b33f | -19.60302 | -56.68861 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 256658f4-daee-3dba-9c1d-cdececf04214 | -19.59973 | -56.70659 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 7af36a4b-1316-3283-80b3-2c2c1ad34d54 | -19.58774 | -56.70414 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 05dbf481-2288-34da-b5ed-37aa6374107f | -19.58442 | -56.72218 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 36.5 |
| 176ba632-4247-3a01-9d54-4e4e2934002b | -19.57576 | -56.70168 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| fa412a99-7b25-35e6-937e-ed6bb0b93e10 | -19.57243 | -56.71972 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.5 |
| 55857722-9d96-3da5-8a78-18ed93065cf6 | -19.5454 | -56.70681 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.4 |
| 5bf47d87-ac44-3615-951c-0fc4251109e2 | -19.53981 | -56.69434 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 4215325c-c6ca-3a37-abdd-3ddf30ff17bf | -19.53642 | -56.71237 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.6 |
| bdba1e2d-35e9-3e8c-9b67-d993fca8a6b3 | -19.5334 | -56.70436 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 8789827c-68ca-314d-8032-cb0020a83fd6 | -19.51711 | -56.58963 | 2024-10-30 05:31:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 7bcc5718-7a75-3df5-871f-e85d142f127d | -19.5127 | -56.68139 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| c3ab5abe-4480-3273-94e4-c651e361f4ce | -19.50521 | -56.58721 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 4a784cbb-3774-3739-bbf3-3af3857bf91c | -19.4748 | -56.6179 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| ad5db5a8-bc92-3a7a-811f-c34b7c22ccb3 | -19.46585 | -56.6293 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| a56f7f76-b212-3ca9-83f1-5bcce1a9877e | -18.26605 | -55.9601 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| f8f3729b-4991-3058-aad7-c105bbf6ab8d | -18.26307 | -55.97689 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 890a4ae9-70f8-3fae-80bb-05ebe26d91c0 | -18.25441 | -55.95781 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 680e9ccb-6a1b-3aac-854a-091fb0bf13fb | -18.25141 | -55.97461 | 2024-10-30 05:31:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 3a0a5386-424c-33d6-965e-b9677209fb67 | -24.01126 | -54.13681 | 2024-10-30 05:33:00 | AQUA_M-M | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 96e5698e-5112-3a1c-9d63-088a13562a0c | -23.98674 | -54.10957 | 2024-10-30 05:33:00 | AQUA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |


[Clique aqui para ver as próximas entradas](README98.md)
