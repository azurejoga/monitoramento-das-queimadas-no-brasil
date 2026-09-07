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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d831ab64-4a5e-3a44-8819-7d820f4fb1b0 | -5.15631 | -55.96501 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13dbc263-c0fc-3788-8707-f4c6e89a5a8f | -3.39246 | -61.31284 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 674e8460-b6c4-3b76-8b6a-c5c724775a5c | -2.97854 | -60.93784 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e05cb125-2c4d-3faf-9902-65bf92282b94 | -5.14772 | -55.95733 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aa1bf0e-17ab-3690-bf6f-81e97487a6bf | -3.97592 | -60.03139 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31d9c647-c0cc-33da-8ba0-ad2bccb0a3fa | -4.2893 | -59.95987 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eebe9d09-4877-3d9b-b067-24fe03789f93 | -5.15295 | -55.97058 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e472bb2-7c05-309e-91af-fe0964d0cad9 | -5.25867 | -60.12398 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b73948-f113-3858-86d6-e9c55bbdb8f9 | -3.49737 | -50.60934 | 2026-09-07 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b4ff5d4-bbed-3ea2-8f6c-c51cae1f4641 | -5.3625 | -56.03535 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88b278a1-45f3-38c5-8831-95c30455156f | -3.70455 | -58.93511 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 392c454c-b1ce-3c99-bcc2-e197f98e5afa | -5.2915 | -60.12577 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 372a6168-10ea-3850-b3e5-d09588006e07 | -12.75895 | -52.85115 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4af5def0-6e93-3e87-9693-9aff5cb322ba | -6.18094 | -57.72899 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| decc472f-61fa-350d-ad14-2796332a94de | -3.70069 | -58.93804 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f668ea8-0b4f-3e4e-88b7-e09a3311c1c8 | -5.9923 | -57.68861 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f7d5e33-9d04-3c1c-b1c0-ca3714770397 | -3.38793 | -61.34097 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 063b6405-80ca-38ca-befa-30d888fdd6e6 | -11.53479 | -49.62773 | 2026-09-07 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4eabd440-6007-3c58-9705-66fa4baf492c | -8.76196 | -62.42441 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb8fbf27-2364-3be2-aa84-32dbdcf1c84e | -5.59477 | -60.24646 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1447c5a-08d3-3fe1-869f-58a57e9c0f15 | -4.11348 | -49.06554 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87b07a20-56e3-31d9-8c54-6ae55bbca5e3 | -5.14415 | -55.95678 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb42298f-b344-3d03-870f-61b29334b847 | -1.19866 | -55.73632 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3227b2cb-506c-306f-95c9-7bac58692c1d | -6.4421 | -58.1628 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b954ec7-23d5-30ac-a0fc-42d5ab2b2dab | -4.67906 | -55.63426 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3220a4a6-6035-3270-9da3-45630414c014 | -5.31863 | -55.87569 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af553971-f734-34a1-b5cc-352633aca41e | -8.73038 | -62.43967 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41386dde-84d5-37c0-8727-861523167067 | -3.54382 | -48.18576 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14e9d45c-0a6e-351a-9511-f7d93ad58a9d | -8.52965 | -63.88869 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c14b4560-5555-3e38-a98b-a668684a2f12 | -3.78925 | -55.87596 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5399c5e-9f31-3cef-a323-0b33b2182a6f | -4.07924 | -48.95269 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5793c7de-d336-33ea-b471-65178493abd7 | -5.99511 | -57.69273 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d4a5b15-3f2c-396e-b316-6ff09edb77b7 | -3.81151 | -55.89557 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb39a48c-8ecb-3330-a92d-3567b90e1ac2 | -8.75843 | -62.4238 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada8193b-d1ec-3d38-b3ce-9c9b537e4ac7 | -3.2294 | -58.22522 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 242edeac-7c72-3259-b3c2-5e9e2902017d | -3.41314 | -61.32029 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1202a52-83d3-3980-9974-239cae72e9d1 | -4.10744 | -49.06829 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28845fc4-52b7-3b28-a7e0-d995ca25e313 | -8.72532 | -62.42648 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 995e5ea0-b1f0-3f31-8729-dc50f11895c4 | -4.95552 | -56.26261 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64a11177-5b15-3626-b1f6-83379f874c06 | -6.48671 | -57.87886 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6af7a86-8f00-3f9d-8735-2c827f4386ab | -6.56498 | -58.97882 | 2026-09-07 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de198d60-f41a-3a3e-bc61-2ef92588ad74 | -8.71423 | -62.44936 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5d9293d-6fb3-30db-83e9-7e11dd0ce4ce | -2.1934 | -60.19806 | 2026-09-07 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adb522f7-d61c-3952-8856-0a7908c35e8d | -6.13324 | -57.74734 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e93dac9-2103-3c24-9570-0b9c36d2ccb3 | -5.30092 | -60.15283 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c780fbd6-3fa5-3323-b5ef-1c380bcb2ae0 | -5.36189 | -56.0394 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9d89a5c-9068-3e83-a221-dd0f72f6dc24 | -1.18485 | -55.71102 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70db0578-6194-3dcf-a40c-aff1bba4159e | -5.16344 | -55.96616 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73cf9dc1-e241-327e-a32b-f25532f57398 | -4.67014 | -55.63452 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 597a19b4-8da6-33b5-aaa3-5f661abcfbca | -4.65943 | -56.02581 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a56c08e-fe1d-39f2-83cd-bfc1fdeaf68e | -3.9776 | -60.03123 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6562e5a-3187-383b-a656-81f3e8241d6b | -6.13623 | -59.92395 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e28fc5f4-f370-3b50-9d06-9cd7c8fc2a23 | -5.5531 | -60.23693 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fc46642-0876-38c0-9ee4-c95d7aae3d6d | -8.71843 | -62.44595 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b2983e6-8fdf-3b1e-9211-56da8c780f74 | -5.14646 | -55.96542 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee7b0573-1998-3d59-a6f2-ec8e9d14715a | -3.22995 | -58.22178 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57ebc2c9-0e9d-3d7e-b755-34c67952af38 | -5.29985 | -60.13805 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb50f3bf-6a56-371a-9409-2a0dc40a9147 | -5.26285 | -60.15404 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b12ab4ac-5710-3ca8-ad63-1275fcaedf1f | -5.36729 | -56.02779 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c166b1e-0985-397e-82f9-7702864ffac1 | -8.89582 | -62.3603 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21ef9d0f-1083-3553-89bb-fd342b2f903b | -3.47563 | -54.4825 | 2026-09-07 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c6144d2-0697-3d69-b39b-6583fc62b901 | -8.72197 | -62.44653 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a4d6b83-c9ca-3d44-be99-d88e2b57a493 | -5.2825 | -60.13893 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eff95ff6-657c-32d4-9151-c1fa87ff3907 | -3.89968 | -60.92847 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4810c18-5066-341a-8e98-f096b73103b2 | -8.52662 | -63.88327 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 001d6c40-2515-35b9-a651-49bc2c8afc82 | -5.64799 | -60.23672 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a25014f-bf68-3853-8653-d74dd06057c1 | -5.29036 | -60.13289 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db5d0676-ceaf-3bb6-a4a8-3d16832ec280 | -5.99288 | -57.7071 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a559d2d7-e8ed-31ba-bd68-f34285ff8318 | -5.16071 | -55.96768 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c23b40f0-ab89-3f67-b460-4ae2e759b6a5 | -3.64132 | -59.54561 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1039f242-e4e2-3b9a-9867-2ee31f2c368a | -9.86711 | -60.28389 | 2026-09-07 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d785ec1b-7b84-3569-bb3d-69b99492a7f2 | -5.37085 | -56.02832 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19465e54-3831-3274-a0b7-59406008a15d | -3.28942 | -57.88816 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e65b9779-0e3e-3f8d-8e69-3fbbff9d8c96 | -5.94178 | -57.73674 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a15f50e4-2a78-3a08-9409-9b06c51bf577 | -3.1429 | -60.65954 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e606340-daaa-316c-bf3f-b2670727d0ea | -3.37932 | -59.42157 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d667b6e0-75d7-33ab-837e-daaef95546e4 | -2.56084 | -54.74344 | 2026-09-07 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fd6058e-9af1-393a-93ac-021aa5941e1e | -4.97646 | -56.28973 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4c5ed750-7051-3818-b4c5-ac41b321349c | -8.72044 | -62.43391 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89aa0767-a7a8-310e-92b7-14325636302a | -8.70564 | -62.43554 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c74a1edb-5e0d-3b4f-b3f7-9c9f2c8b79d5 | -5.16282 | -55.97023 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e4f116-466d-301b-806d-e0d7444c72a7 | -3.38632 | -61.32833 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6252c879-5863-3e25-9019-a78cdc567b0a | -3.14637 | -60.66008 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b95a341-512f-3dcb-9a57-d1b1ea56d1cd | -3.61332 | -60.5702 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c84b084-e6fa-3757-8968-0b7347842538 | -3.81463 | -59.16191 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fb6f13f-f281-37f3-9cd5-dc05142f3dd8 | -6.01868 | -57.69638 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf2cd77c-ab0d-3f69-a104-f055169d689e | -3.14127 | -60.64764 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6455e2bc-525d-3e56-b852-5c8bd3405262 | -6.06189 | -57.79474 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd4e1e42-0e15-3b5d-878b-5f83fc76de3f | -8.72398 | -62.43448 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bfa9ec5-151b-3b7e-9836-4ae89964db85 | -5.26228 | -60.1576 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d415eac-7c9f-30ed-84e3-daead8a0e5e1 | -8.71338 | -62.4327 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70d3687f-cd20-31f1-9ba5-3ffb2b86957b | -3.06541 | -61.2061 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa589e96-7b0e-30df-a45e-7876926b7cbd | -2.9804 | -54.02521 | 2026-09-07 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aedf8b52-ebff-317d-ad7c-564ae3ef239f | -3.61556 | -60.57822 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6516f19-1822-3551-a5da-2bffc6def78c | -5.35749 | -56.0275 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 459378c9-bbc3-3e80-a3a1-21be8bd457fa | -3.13944 | -60.65899 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 436a9b7f-b869-35b9-9211-8e3fb9e1ac1b | -8.52058 | -63.87244 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbbd721d-a442-3939-9a49-23f159b8bff9 | -1.18832 | -55.71157 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8618573-4b4e-35d2-959f-2a840524855f | -3.14311 | -60.63627 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02b93706-de6f-333e-9d1c-fb65a8dcac5d | -5.30042 | -60.13449 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README31.md)
