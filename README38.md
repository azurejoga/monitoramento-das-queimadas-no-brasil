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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 181ceabd-3c8d-3248-99e6-deab3db2017f | -6.17789 | -45.43928 | 2024-10-19 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b4ad6b5f-22ee-3a89-8819-5505fc44cd89 | -6.17715 | -45.43399 | 2024-10-19 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6f218e7-4182-3fa5-a2d5-91b3adafe2a2 | -6.17699 | -45.44574 | 2024-10-19 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92e5c1bf-6dd3-334a-a07b-804e0bad9f99 | -6.17625 | -45.44075 | 2024-10-19 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f96bcce-64ed-3f05-ae37-f20aefa94f81 | -6.1754 | -45.44719 | 2024-10-19 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 351f8dc4-e141-3ba4-8c9b-e00b29637d25 | -6.17005 | -45.44439 | 2024-10-19 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1565d8be-627e-360e-8e51-fa766c1782b3 | -2.57282 | -47.07281 | 2024-10-19 05:14:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfd20dfe-bc51-3ae5-8374-6a00c1d0e107 | -2.56744 | -47.06742 | 2024-10-19 05:14:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f477ba0c-3484-30c1-bbc5-5835e546a857 | -2.56676 | -47.07197 | 2024-10-19 05:14:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c519dc0-d288-38ed-9f88-92d4358aa61b | -2.56609 | -47.07648 | 2024-10-19 05:14:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 188b8b53-ccc8-31b1-bad5-a11ff0c8a5f3 | -2.53146 | -47.2266 | 2024-10-19 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f80659f-d011-3476-afee-81150f4e65c0 | -2.14739 | -47.06405 | 2024-10-19 05:14:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d77dfd5-2728-326e-83b2-458969d50b7c | -6.63023 | -47.3545 | 2024-10-19 05:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c5a36ff-049b-3a48-8bd4-ceff8280e666 | -6.62395 | -47.35357 | 2024-10-19 05:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc44280d-2b19-3b76-a63c-0ec5accc4fcf | -6.61663 | -47.38106 | 2024-10-19 05:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c26eec-63f1-3043-bee8-37fe38106ccc | -6.61444 | -47.37743 | 2024-10-19 05:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d27d6373-4804-39f8-849e-a4932c3fce30 | -6.61379 | -47.3824 | 2024-10-19 05:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d87940fc-aadf-339b-914e-3ff1042326c9 | -6.61038 | -47.38005 | 2024-10-19 05:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 374e3bc9-fd1f-32d1-a4ab-16330519e8cb | -1.97529 | -48.68784 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 065344f6-b330-3c55-b175-8bb63bd3ffc7 | -1.97478 | -48.69123 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 73a2b008-265c-3679-a5b1-241bd47a6770 | -1.43632 | -48.14649 | 2024-10-19 05:14:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b6ce3ed-a171-3e39-bed1-2da2d44b2fea | -1.43078 | -48.1456 | 2024-10-19 05:14:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32424a50-ceae-37a1-862e-cef2a3cf7da4 | -1.14159 | -47.31355 | 2024-10-19 05:14:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72302962-ff2d-3893-95d0-575d19252459 | -1.14096 | -47.3176 | 2024-10-19 05:14:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df5da6ad-8019-3d0b-a4c8-afd570d836c6 | -1.14034 | -47.32163 | 2024-10-19 05:14:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5deb457-36c5-3a68-8340-63672ad6ea06 | -2.72053 | -48.83441 | 2024-10-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f2935f6-8474-3779-bf32-b4f2623d98d8 | -2.72001 | -48.83788 | 2024-10-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c280cad4-3b21-3410-bcc8-8461ef1542a7 | -2.33004 | -48.83485 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95188087-7957-304a-8a49-bb4163c14af1 | -2.26217 | -48.82711 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65fba434-1a05-3627-bf5e-9da2ff08deb1 | -2.25977 | -48.82761 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f0457a1-0c30-366e-b8e4-a823d108536d | -2.2568 | -48.82631 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28da2cf4-d965-39b5-b7fc-9c5b3111cff9 | -2.25489 | -48.82347 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2106159-f5b8-3911-a5a7-f18943ef0da0 | -2.2544 | -48.82679 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a468763d-ce3e-3089-bcf1-7c8570cb5cb6 | -2.25143 | -48.82552 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28cb20dd-87d7-37d5-af96-8992bbbee0c8 | -2.87691 | -48.24535 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db564135-398e-3170-ae95-7ea348e784a3 | -2.87633 | -48.24915 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49498605-b6e9-372f-ade3-0872bc061fad | -2.87455 | -48.2443 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac6f2a68-e170-3765-923a-addb7df5cf22 | -2.87401 | -48.24809 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 688c6957-7240-37b9-8bd1-7000dbe9a04f | -2.87344 | -48.25196 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d75e4e5-f835-3dd8-9514-6c5f89b44a6b | -2.87128 | -48.24447 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe17bc89-e105-3430-80fd-e36c4b48b809 | -2.8707 | -48.24831 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5a58b26-1886-37ba-9844-6712b14214c5 | -2.87011 | -48.25214 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0784a14-cdf3-397c-80bc-4bd847dc697f | -2.86782 | -48.25106 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ab34b1e-df5d-3438-a026-3e0c0e80d7a4 | -2.65196 | -48.49773 | 2024-10-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fad374f6-1c13-3e89-a2b7-26d6d9dbbf06 | -2.65143 | -48.50136 | 2024-10-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85846936-5fbd-33e9-873d-190fe46395ee | -2.64644 | -48.49692 | 2024-10-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e205d1a-afba-304a-98b6-e59953ca515b | -2.64591 | -48.50053 | 2024-10-19 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b03e4024-d958-35ff-8aa8-7162a4610542 | -2.44626 | -48.44073 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f267f33f-617b-3a91-b8a7-d5257b8083d2 | -2.44533 | -48.48498 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67023566-dbbb-34b4-84e8-88ca0bafa750 | -2.44479 | -48.48859 | 2024-10-19 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3a10a7d-eb13-3b43-aad4-ba7832786394 | -2.35552 | -47.61035 | 2024-10-19 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b452e023-8fda-3352-82f9-9a58120358fb | -2.35492 | -47.61441 | 2024-10-19 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5697b8c8-dcf0-3430-8ed7-3904c07717fe | -2.28848 | -47.85548 | 2024-10-19 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14697d5a-f995-3dcf-b972-9d34d475c829 | -2.28458 | -47.85156 | 2024-10-19 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cbdf2b4-7ea0-3abd-b54a-91fa3553a273 | -2.28401 | -47.85546 | 2024-10-19 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed633db3-dd6d-3950-9fff-ec16a9d8fe04 | -2.28277 | -47.85449 | 2024-10-19 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b4b3762-ecf2-3ad8-be48-1acc2a94a80c | -3.58401 | -48.9424 | 2024-10-19 05:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a45d944-488c-3e0b-af70-7cc24ac88385 | -3.58349 | -48.94588 | 2024-10-19 05:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a295a4d0-5296-39bd-bb83-b1857d69dc1b | -2.19302 | -49.13334 | 2024-10-19 05:14:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d076995d-89ae-312f-9428-af1104572f9f | -1.13677 | -49.04784 | 2024-10-19 05:14:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71b157c7-8647-3986-8119-b45633a68aa2 | -1.13206 | -49.04393 | 2024-10-19 05:14:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c16c9106-312a-36bb-b19c-64135c46f726 | -1.13157 | -49.04707 | 2024-10-19 05:14:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6f52ded-dc19-3fa7-8a4f-2e9ccca861e7 | -3.46296 | -50.61307 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00e7838e-50a9-3860-8569-161712debbbf | -3.45812 | -50.61237 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ada5f2f5-728d-39b8-8848-38d6a8efbd78 | -3.44182 | -50.1753 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3143964-a002-35c6-aeb3-3314bac4ade2 | -3.44136 | -50.17829 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a44a304-3516-3642-ad26-d6a9c2ab2360 | -3.43555 | -50.21654 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65f7e3ba-b9a6-3f8a-848c-7ff842638e8a | -3.4319 | -50.2117 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 50e89dbd-6faa-325a-9177-59eda46d6372 | -3.43141 | -50.21031 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 3fc62c24-2b72-3f9f-901c-520d6c6740ab | -3.43111 | -50.21725 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| baa78cf7-5701-388a-a626-1e7fe858c031 | -3.43057 | -50.2159 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 54a40283-af9d-3088-b91b-0d3ea838d74f | -3.42973 | -50.22141 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 566be2b3-d7ab-3ed0-a34b-d5aad6f69107 | -3.42644 | -50.20958 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| fd566a65-a259-345a-b995-5d70617de868 | -3.4256 | -50.21518 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| dbcbc156-bd91-35d2-92b8-a1f53839982e | -3.42001 | -50.38462 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d04d467-27f6-3fda-ba97-2a629dd23123 | -3.38568 | -50.34591 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 919c206d-3824-3179-a450-91b226c3bdbd | -3.38486 | -50.35138 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b092a05b-f94f-3c5d-94a0-4b0feea938f3 | -3.37997 | -50.3505 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5801e46f-0605-30a4-84a9-43b84eb46af4 | -3.3619 | -50.30272 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af55d798-b517-3cda-ace1-2817b1f4d9e9 | -3.35698 | -50.30194 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38b1e306-6ce5-3899-837f-88d50a562e65 | -3.27757 | -50.17942 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6382cf26-0df2-3bb2-8a07-42019b880ed1 | -3.22303 | -50.36296 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9a7fb63-ec0a-32ea-a889-7da8f14aef1f | -3.22091 | -50.35854 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b2311cf-0ef9-3c82-acb3-207497db508f | -3.22012 | -50.36391 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de99d78b-ec4f-35f7-9aac-d7aa3f39a530 | -3.21896 | -50.35684 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3924dbda-bfb1-3d81-9f84-692ee0143246 | -3.21813 | -50.3622 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78927691-12e4-3a32-a169-b77c90cc08a4 | -3.21601 | -50.35778 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d41631a-57cc-37e7-8d62-7914fef7a9a4 | -3.10056 | -50.19561 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c5e22a5-51a4-3ab1-98be-8ede8abcc963 | -3.06972 | -50.36576 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93687ce5-186d-3004-865f-b6cc36877385 | -3.06484 | -50.36499 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef7c444e-f413-3453-9723-d7b9856bd8c4 | -2.46135 | -50.24978 | 2024-10-19 05:14:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4554af88-3473-3d95-ae57-b55b88f935d8 | -2.46051 | -50.2552 | 2024-10-19 05:14:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd9de89a-9298-3a21-84ca-af30433862c3 | -2.45919 | -50.25033 | 2024-10-19 05:14:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc53494e-b9ef-39a4-99bf-86f1210fd373 | -2.45839 | -50.25576 | 2024-10-19 05:14:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 889b5ea5-548a-3a59-8ddc-a8ebfd1ac883 | -2.41574 | -50.28711 | 2024-10-19 05:14:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b97b5eef-33a7-35b5-9238-da936b20dc44 | -3.26835 | -49.08614 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96f9f023-7d17-3b13-adf9-0b2fe1f0cca9 | -3.26784 | -49.08952 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4bf4e45-5df3-35ed-8ac3-56b330e72491 | -3.26299 | -49.08537 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1255a11-bd15-3da4-b319-7a3673a0d0d9 | -3.26249 | -49.08871 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccc2d4c0-56f8-32f2-a534-c836659f5c22 | -3.0532 | -49.41241 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README39.md)
