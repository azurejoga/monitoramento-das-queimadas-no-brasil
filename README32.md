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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 019799ea-aa0c-369a-87bc-d409d9da9fb5 | -2.76775 | -52.60397 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9223c70f-c258-369b-b6b3-e39091333bd1 | -0.93213 | -51.64369 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c1ceca4-76d2-38b1-97c6-dc51c298f5c5 | -2.85716 | -51.58462 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 284cf90c-1eef-3a58-8869-a8ed09b34da1 | -6.62706 | -46.56769 | 2024-11-19 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 200d4ad8-07a3-3b30-97c3-ebe1ebf2fa58 | -2.58736 | -51.71999 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae76bb0b-bd00-3b8b-9fdf-4426131e3944 | -1.92471 | -53.35133 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9c7cd5d-6a90-3b72-9335-611350d47909 | -3.41247 | -50.86051 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2fd51b1-7ae4-3df4-995d-26a07209f2a3 | -3.41583 | -42.38789 | 2024-11-19 04:46:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5f9df429-f5ca-325c-902a-9f9129204166 | -3.8177 | -51.38086 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c5dc240-72ef-317e-aaa8-d647b9e90597 | -2.32596 | -45.65079 | 2024-11-19 04:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09966af2-5927-374b-b7e1-b63160b406bd | -3.99488 | -49.91717 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6161cce-d128-37bc-bd49-26a83115c839 | -3.36774 | -50.82191 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d5cf4cf-0cf5-316c-86f7-2cf65a4053b4 | -3.3067 | -53.36775 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22db76ec-05e7-3518-a34c-65b85ae6a6fa | -1.10502 | -51.92786 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ac0a448-db5c-32e3-87ff-4837c15e876b | -2.32892 | -51.28633 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e53c72e-c3cc-30eb-a160-1a206839fdb3 | -3.0414 | -49.46547 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 07f0bee5-983f-326e-a685-d2a1370f19c4 | -3.75126 | -52.66684 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf141d42-fbdb-3e7e-aee0-639b82ff5612 | -3.49847 | -51.68135 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0a79c8b-0731-30c7-90b5-09f0fcfc52ff | -2.66239 | -51.71693 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 89102512-ab68-30c7-85a1-8cb106c128d1 | -3.76284 | -52.14471 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4374f4f-9e3b-3059-bb17-a835ef1ad244 | -7.42727 | -47.86705 | 2024-11-19 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f7093d9-31b0-3900-b841-23a8bc850309 | -2.95937 | -51.45292 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 364b8da6-e4a5-3f7f-acf9-cc2622c7b390 | -3.62883 | -51.2621 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f106b22-8c66-3aeb-81ee-49064b5f5af9 | -1.75476 | -50.73805 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acfe36c0-e7bb-3ae7-bba5-9f39dfc66699 | -4.99582 | -44.33615 | 2024-11-19 04:46:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cd63f63-94b9-3a23-b9fd-46ac8c65b4cd | -2.38216 | -48.91511 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8b86028-7caa-3ee4-b967-3801f2daea17 | -2.58982 | -47.47766 | 2024-11-19 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94b6d5a3-aee9-31ae-b5d1-d9201c6e2338 | -4.06216 | -50.00988 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f6d84f2-0d6d-3b10-9cf9-e853f594b7a9 | -0.84344 | -48.74823 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cd168db-0e79-3a1f-a803-f0477ae6a17c | -3.07646 | -51.66183 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e985629d-aa28-38f4-a181-39aa3a797cf2 | -3.51057 | -50.23166 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22482d4a-d3e1-3d9d-b4a2-ce7ed4b1d644 | 0.13247 | -50.49249 | 2024-11-19 04:46:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8ba7190-43a8-3c8c-a680-7215af47bca4 | -2.89796 | -54.00488 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6999616d-ebf2-3ccb-8507-55a28d57e205 | -3.31024 | -53.36833 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ebc68e-0854-3cbb-a4b9-1a405bba57b1 | -3.57688 | -54.54613 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dafa39e-821d-3066-b018-e8d216fc52d4 | -4.06061 | -54.05072 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e1a83fe-7bc2-3f2a-95bf-6ba1d0a7d650 | -2.58624 | -51.7271 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03aee403-e523-34fe-be44-9eab3fea4538 | -5.70097 | -46.37585 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 109eeb52-ff0b-3987-9147-cc8d9b52d3ac | -1.05859 | -51.75204 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a40e6e66-1d0c-3881-8525-0415a531bc59 | -3.11877 | -53.70248 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc3dbaf9-d931-333e-a29f-d268b8389d85 | -2.59016 | -51.72406 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 102bcfd6-4510-38b0-8953-d3d6a4db8253 | -3.7176 | -51.84224 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cadbde4-aa78-368c-9491-cf7d743d40b3 | -2.77771 | -48.58175 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 029ea544-c100-3b88-8017-ec1132987cf0 | -0.96876 | -51.71977 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75d1c250-ef63-3e6f-afa2-2f1db42fd35b | -4.25102 | -48.53377 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed03cd21-dcee-3caa-94a4-f0af7511e60c | -0.88819 | -51.8119 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f5bef53-5cbb-34ad-961f-05b11987db22 | -4.10262 | -51.06057 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2d8842e-37e9-3820-aec9-9d6ec61a2645 | -3.57004 | -51.44147 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8177e441-0378-32c1-96c6-f31d8acef90b | -3.38767 | -53.26954 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6098f788-36ee-38bf-a3b6-19eb03a0b955 | -1.21513 | -51.78748 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d14d50e-9b3d-3397-be48-ce23e16dce8e | -3.28803 | -54.16768 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfda1547-21c3-369f-b0a8-25ebf61474d6 | -3.1025 | -53.10209 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 288afd98-f375-33eb-ac75-19f62942bd2f | -2.92492 | -48.05742 | 2024-11-19 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 344ba8bb-0c4f-39f8-a82f-ae5b8e2728e8 | -6.97992 | -46.81672 | 2024-11-19 04:46:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4217d5f4-a7b4-3bef-906b-b747b19c9727 | -0.92932 | -51.63956 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c9b0b67-6486-3a16-aa29-575078c399d3 | -3.82226 | -52.26094 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2ef3141-dcf5-3622-b168-b1102f43fdb6 | -3.10847 | -53.74359 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dff648e6-c733-37b1-8df2-303135d4a018 | -2.69224 | -46.22374 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d36be80d-9ef5-37b0-95e2-7f7887563a64 | -4.55498 | -48.00808 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5542c4b-491e-3b4c-9690-f017ab1f685a | -1.47322 | -51.97297 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 751be296-3e64-3ca2-954c-ef47597c983a | -2.86595 | -51.78523 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d3521c6-7c06-3fdb-9127-a7a7267f03b4 | -2.8994 | -53.05601 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90bea4a3-ae57-3236-b00c-d532dd89ad29 | -2.86874 | -51.78931 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 304188bb-1225-3318-8b90-234b9932b3db | -1.48501 | -52.09928 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9370f102-2357-33b8-aadc-01eef2e0e895 | -1.39668 | -52.94928 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f8234ef-448c-381f-9e81-75a461805194 | -6.93359 | -45.09169 | 2024-11-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eaabdcdd-67e1-345f-a910-f3a325dec19e | -3.72772 | -51.23861 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 277b3666-2c84-3cfe-b9da-963f2dfa6744 | -4.3913 | -47.77454 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a3cfe879-0297-3369-b399-c4142298c0cd | -1.14764 | -51.94567 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d984baac-04bb-3fc4-adf3-64917fb0c1fa | -4.11469 | -51.04831 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80ee978b-2755-3a96-842a-c908bf5de61a | -5.51066 | -46.44111 | 2024-11-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e536c0d2-7363-3154-bb50-243caa6d9bab | -0.92875 | -51.64317 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 792b57cd-59c4-33ad-8fdd-afe4643baba1 | -3.38569 | -52.80262 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a869274-840a-3406-b617-faa553dbd168 | -4.11222 | -45.63073 | 2024-11-19 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cce3b124-6838-3d9e-bb7d-2599caf52365 | -6.98492 | -47.82314 | 2024-11-19 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 677d8139-fc0a-3d86-88b8-61b022b4c315 | -2.1153 | -50.62884 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dc0105f-017f-32ff-bb78-a9b53086ea0d | -1.83801 | -46.28225 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3290ff6-dbf1-3a9e-8352-e052ddddbeab | -1.09195 | -51.73857 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0681676b-0370-304d-b54f-d84a48afb93f | -2.68644 | -51.80449 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dfae32f9-386d-3498-ae04-b1d876d10b89 | -1.21379 | -52.48137 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a02ea768-9af5-3497-bc5b-552ef2994232 | -3.06352 | -53.27784 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9cd4b33-71d5-3338-ab4b-9a8e190b361d | -3.98383 | -49.9226 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 547ca8c2-03e9-34b1-9132-3f4f038e70fb | -3.99156 | -49.91666 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 074667ec-2ed2-3854-ae6f-d256bee1ae9c | -1.39223 | -52.4229 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e48a557-52f8-308b-8d88-5ea3e8993d77 | -0.9405 | -51.72287 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af885912-ea37-3079-9221-2d6fa79bd896 | -5.84785 | -46.43847 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e854c3c-dfe1-3e8d-a057-482264459b2f | -2.02166 | -52.07915 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1f20549-7644-3781-b65f-baa846ea6692 | -3.3451 | -53.30836 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7573f0d6-c923-3e5c-9b61-7ca2a59e1655 | -3.91858 | -42.41798 | 2024-11-19 04:46:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 32e3f312-c172-33c1-a64e-9a405a19cb4c | -1.57933 | -50.44606 | 2024-11-19 04:46:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00dd6ca5-e10e-3520-a9f4-d7e23553da72 | -3.9921 | -49.91317 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfcba460-46e7-33be-8beb-517e1a7e652e | -2.16652 | -51.96732 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 234b427b-87a9-32a8-850e-729ec64a094a | -4.93497 | -47.74453 | 2024-11-19 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc66f954-e837-3c72-83fa-9d93ee6e7879 | -3.50392 | -51.0157 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2157db56-2b2d-3c21-ad59-fda724b8096e | -7.00642 | -45.61504 | 2024-11-19 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 720b2cdf-95c8-333b-be01-980795870c45 | -0.28648 | -51.55206 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 940c8699-8ffe-3f6f-b3df-6b9c75496344 | -2.99603 | -51.45854 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47038425-c6e4-3601-aefb-4192dec7ceae | -2.15854 | -50.70244 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4102db8-9bce-35c0-87dd-27d5890a8c3f | -5.58341 | -44.87663 | 2024-11-19 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5f079ef4-dc3c-3e1e-8450-24f93d03114b | -4.2291 | -47.18657 | 2024-11-19 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README33.md)
