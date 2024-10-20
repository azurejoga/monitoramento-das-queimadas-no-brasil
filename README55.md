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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdd9409d-5822-31db-9ddc-7b84a9eba066 | -4.37963 | -45.83718 | 2024-10-20 05:18:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 01c24796-d7f2-379d-8cd6-c045bb49db31 | -4.3425 | -48.56149 | 2024-10-20 05:18:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 86cac998-3e99-3ef9-a653-bdf0e86622a5 | -4.34081 | -48.57238 | 2024-10-20 05:18:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 45f5dbf1-8796-3e12-82c5-41af52efd5c5 | -4.33412 | -48.61552 | 2024-10-20 05:18:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 8f54382b-4c5c-348c-8afa-6fa850c48113 | -4.20347 | -46.63118 | 2024-10-20 05:18:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 892f315f-bfa1-378c-9481-9926b2c7aed3 | -4.20211 | -46.64019 | 2024-10-20 05:18:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9843e7aa-ada5-3771-aa0c-7f765a9efcb6 | -4.19454 | -46.6298 | 2024-10-20 05:18:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| e7dabb1c-e322-322e-8e56-2fc39e01a2cb | -4.19318 | -46.63885 | 2024-10-20 05:18:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 0d0a3402-e53b-3775-a1d1-5767bc090036 | -4.10533 | -48.23618 | 2024-10-20 05:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7fa224cf-bb8d-3a90-af22-e14e9cdcfe06 | -4.10373 | -48.24651 | 2024-10-20 05:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d7c57361-a0de-30df-89b9-91ad3860f35b | -4.09655 | -46.91501 | 2024-10-20 05:18:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa641aa6-914c-31ab-a9e8-b69630b97ec7 | -4.03829 | -46.93454 | 2024-10-20 05:18:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b01ce9fb-98b2-3e00-bb5e-aa979bc3d581 | -4.0369 | -46.9437 | 2024-10-20 05:18:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2d6f4a4f-52bf-3d6b-88e3-3581f21caf61 | -3.91514 | -48.33538 | 2024-10-20 05:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bc9694ff-decd-3eac-a8d7-3730c11d513f | -3.90965 | -49.98214 | 2024-10-20 05:18:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0c285dd5-57e3-3594-afb1-489656bf1132 | -3.90549 | -48.33395 | 2024-10-20 05:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7326269a-ef56-3f69-879e-513f9f010941 | -3.8988 | -49.98052 | 2024-10-20 05:18:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 103f8115-c6c5-3c42-b965-1f707b4a0587 | -3.89672 | -49.99416 | 2024-10-20 05:18:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 81449add-cbdd-3e0e-ad14-e6d82c2cd140 | -3.8391 | -48.95872 | 2024-10-20 05:18:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 78d501f9-58f7-3241-9c32-7e23c517fdac | -3.83151 | -48.87509 | 2024-10-20 05:18:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 56c43d1d-3705-3210-823b-f88e48deee4e | -3.82972 | -48.88657 | 2024-10-20 05:18:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f112996-c604-312c-864e-14b2ae51f4ab | -3.82904 | -48.95721 | 2024-10-20 05:18:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f1b3be55-de8d-3df8-bf7e-e0ec968258d1 | -3.81315 | -48.86539 | 2024-10-20 05:18:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7d087d9b-7ffe-3409-98fa-bc7a6ca2d089 | -3.72788 | -50.71302 | 2024-10-20 05:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2001701a-eddb-37cd-a2ae-0805b28b8f9d | -3.59875 | -50.58601 | 2024-10-20 05:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 91599626-28d1-31b2-ba6a-6ec967734e92 | -3.54991 | -50.31179 | 2024-10-20 05:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 519610ce-086f-38da-8368-d5a0dbbe3646 | -3.47696 | -50.48314 | 2024-10-20 05:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b35d98fd-da92-3f8a-986d-e7338d467728 | -3.39246 | -50.65282 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a16d8a69-c92f-31a8-a1b2-b5e4cdd8e4ac | -3.39003 | -50.66844 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 91e167e2-adb7-35e7-b779-74e757cd4506 | -3.37846 | -50.66681 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 36ec77cc-5c1e-336a-9eb5-17fdd9a8c8bf | -3.21694 | -48.61106 | 2024-10-20 05:18:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fd9d3356-b86b-3701-94ce-791fbcda42fa | -3.20702 | -48.60959 | 2024-10-20 05:18:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 72f50db8-6d29-3e10-bdad-4e92ad372e68 | -3.20453 | -48.61498 | 2024-10-20 05:18:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5f02c0ab-41a0-35fc-b360-3de3751a5711 | -3.17772 | -51.24932 | 2024-10-20 05:18:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 61a69fcf-966d-3115-a7c1-84b55ce05e8e | -3.13408 | -54.35462 | 2024-10-20 05:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 775e6119-7735-39ad-8775-e5b10c675436 | -3.08822 | -45.94889 | 2024-10-20 05:18:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 514355b3-4472-3165-84d6-4d1f633b906e | -3.03719 | -51.01005 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 37c418fd-b782-3052-bb38-c1bb289ef40f | -3.03454 | -51.02692 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| bf311a09-ef7c-3651-94ec-0257d8249f0d | -2.99105 | -45.60702 | 2024-10-20 05:18:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e39aa458-7a5e-35b7-a90b-93b0b7ac40fd | -2.97514 | -47.91251 | 2024-10-20 05:18:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 222cd51f-ae17-3c72-9e30-39ba4b72b2c9 | -2.97369 | -52.83971 | 2024-10-20 05:18:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 177f69d2-5a88-3571-a8f7-570296f749fe | -2.94862 | -52.9087 | 2024-10-20 05:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 39295499-66b2-3e2e-9a0c-c50c52545486 | -2.85306 | -53.32738 | 2024-10-20 05:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 609ae140-bcb5-3acc-8e25-bc51813e163e | -2.84999 | -53.32195 | 2024-10-20 05:18:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8c340344-2aaf-3b03-ae2d-266c9f67b198 | -2.79888 | -51.3542 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 53e72d31-8bab-310f-a7dd-35c122a17515 | -2.79531 | -51.34809 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1b594d60-b826-37d9-bae5-6304ef795b21 | -2.79521 | -48.68036 | 2024-10-20 05:18:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 83031a40-27b2-3913-b729-c0dd8e78c378 | -2.79259 | -51.36628 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 78ede03c-cb4f-3349-adc8-d9b7bc99a177 | -2.78653 | -51.35235 | 2024-10-20 05:18:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 762e9e01-8e0e-395b-80db-4aa8408e3e2d | -2.78534 | -49.28839 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3931e422-bd4b-3334-8643-a84e58260a67 | -2.78341 | -49.30101 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d423e548-92c3-3be7-807b-b4229d6adb16 | -2.78147 | -49.31372 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b4d83037-a719-301c-9d51-dd9091e3aa18 | -2.77292 | -49.29946 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7807bfcb-affe-3a56-b3c4-e3c1a8c6ee8f | -2.76781 | -49.40324 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4cf47762-ae6e-3330-8ca3-eb524699df03 | -2.76584 | -49.41618 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7097e436-0b1d-3921-bdfe-a049244cf03f | -2.66242 | -49.13642 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 996c5b90-f7c4-3e7f-a1af-3acbf7ea8106 | -2.65712 | -49.12875 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8ae7a579-c1b1-37ca-a938-3d3efdbae15d | -2.65526 | -49.1412 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 29567dfe-7c8e-330d-bb38-cd49717985f8 | -2.64198 | -49.08858 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b07f35e5-a3f2-3bda-bc25-44356022e8ee | -2.51652 | -47.47643 | 2024-10-20 05:18:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eeb0ba45-9d8b-369e-8e7a-e3689f2c3db1 | -2.51503 | -47.48634 | 2024-10-20 05:18:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 2f57f96e-0e85-3c9b-971e-a3ffd240a8a9 | -2.47872 | -49.08963 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 892bf50a-7d55-3b74-bb60-1654257f35d0 | -2.47686 | -49.10201 | 2024-10-20 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b8f0518e-690e-38d0-b6c6-6c1db8c93da1 | -2.29965 | -48.57485 | 2024-10-20 05:18:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 934bd018-6cb0-35fc-9aef-02bbada75e93 | -2.29786 | -48.5864 | 2024-10-20 05:18:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 79becbfc-582c-3cd9-9d08-e0983c369d0e | -2.20324 | -50.45509 | 2024-10-20 05:18:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f6aeb890-aa33-3477-8cb4-335bd7e24b0e | -1.78522 | -52.04209 | 2024-10-20 05:18:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2c84201b-2034-311c-b288-ec87459ba06e | -1.1691 | -53.65703 | 2024-10-20 05:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| b6f4d805-98c6-321f-928f-f987f1c762ef | -1.16716 | -53.66147 | 2024-10-20 05:18:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| f5d5b5ae-2062-3431-b948-0ad5befae9b0 | -7.68194 | -47.32554 | 2024-10-20 05:21:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1b4d152a-1859-324c-a228-72f6a6c316f2 | -7.67439 | -47.31515 | 2024-10-20 05:21:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8cb2eb9c-6a90-3919-a013-8bee0ea133bb | -7.67301 | -47.32419 | 2024-10-20 05:21:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3999dd8d-a1d6-3b4b-91e4-4129f60fcea7 | -5.50047 | -50.58705 | 2024-10-20 05:21:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 63be0911-8140-3c30-bc51-3a2b1f912518 | -2.2994 | -48.5722 | 2024-10-20 05:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f889eef2-1789-3302-9ad8-1f26100238bc | -2.7773 | -49.3067 | 2024-10-20 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c8f96868-9b35-3253-8a1d-03cf520906e8 | -3.0478 | -51.0226 | 2024-10-20 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6507525e-42b4-3c96-aa39-346f0b938e5a | -2.2993 | -48.5936 | 2024-10-20 05:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 1118c0a1-7af5-3341-8dc4-ecb124c3ca93 | -2.2994 | -48.5722 | 2024-10-20 05:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 0f5cd706-42a1-30d7-a829-2754006c105e | -2.7773 | -49.3067 | 2024-10-20 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 94b90398-d871-3c38-8619-58ac15aef76f | -2.7958 | -49.3062 | 2024-10-20 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e2727f8c-2973-32bb-a796-46929c3b19f2 | -2.3198 | -54.3838 | 2024-10-20 05:45:19 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 6c6c49f0-7742-3824-9a45-5f7fc1e27988 | 2.84044 | -61.35784 | 2024-10-20 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 084d28cb-e4f9-3010-91a3-39c0616adff0 | 0.99436 | -59.44693 | 2024-10-20 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7201673-cf74-31d7-a376-45b61724fd18 | 0.99375 | -59.44298 | 2024-10-20 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b979d44c-591f-3d1d-bc8a-5c487125697a | 0.87498 | -59.70446 | 2024-10-20 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c3db89c-c142-3c73-861e-3c4018e94fb5 | -4.71526 | -56.14191 | 2024-10-20 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 632eaaa8-b69b-3e49-ae82-a7c0df69c4c4 | -4.06761 | -53.77357 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11f83bc2-78f1-3d9a-93f5-0888ff5a2355 | -4.06509 | -53.77279 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a81c9815-7f70-3719-8fc2-82a30712fb5d | -4.06096 | -53.77266 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80b73491-b9f7-389d-b5cc-ac37e545b71b | -3.76859 | -53.40621 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bc1d288-d6c7-3035-9117-8663910d4f70 | -3.7677 | -53.41234 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 623ed7f8-f71c-30c6-9c40-ca941d1bec08 | -3.58812 | -54.67992 | 2024-10-20 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| eee9d12a-5a3f-31e9-b62b-5bff1cd2b6ac | -3.58641 | -54.6793 | 2024-10-20 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b9ebed09-7a36-3523-a142-84b9ec0bd159 | -3.58571 | -54.68433 | 2024-10-20 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8e5499d2-3fc6-339f-997e-c50b081ea170 | -3.57121 | -53.75337 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83eab945-146e-3839-ba86-4c46802594da | -3.56547 | -53.74637 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 461c5915-a0b0-3960-80fe-8854a620ac9e | -3.5646 | -53.75247 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2636ef1a-6004-34ad-b141-cdbddaec6188 | -3.50597 | -54.68726 | 2024-10-20 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d598b702-a85a-3b2a-8a66-9bbf90f1bbb7 | -3.50412 | -54.6877 | 2024-10-20 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b323339-b664-38ad-bc83-e47c833f6637 | -3.49977 | -54.68608 | 2024-10-20 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README56.md)
