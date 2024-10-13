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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17ea3e69-dfa7-3347-9a47-e057f54d153a | -4.11172 | -48.25185 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 82868d83-caf6-376a-890f-53c34fe9e253 | -4.10574 | -48.24917 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7ebb0b48-ebed-3962-8c3e-aa3b968ed83d | -4.10479 | -48.25558 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5793c04b-955e-3e2a-a9fc-c91848ee9368 | -3.92017 | -48.36152 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5d6912d-9c8f-39d7-ad4c-896f829c2584 | -3.91328 | -48.36047 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60d7e2d0-7e55-3473-bb1d-20eed4f52ee4 | -3.90636 | -48.3596 | 2024-10-13 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b68c289f-827d-3bdc-ba17-13f6c42d7ea6 | -2.1734 | -48.84398 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e04e577-1450-3cb7-b9e5-7f52f9b2a22b | -2.17255 | -48.84955 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edfb2bdc-8067-3894-a771-a3d66ffd29b9 | -2.17208 | -48.84486 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1291dc42-258f-3781-ab2e-90fe8be2527c | -2.166 | -48.84856 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3eb243c-d4ac-30a4-a08f-00fbcf45b75d | -1.46775 | -49.32122 | 2024-10-13 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5271b8af-8328-32ff-a97c-53396bc5c759 | -1.46505 | -49.31744 | 2024-10-13 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9597daa2-d4e0-3451-b978-4d1b40ba741d | -1.4643 | -49.3225 | 2024-10-13 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a3ebd25-d657-3bce-bc41-a30b5a06ed2d | -1.46224 | -49.31523 | 2024-10-13 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c58e7afd-3265-3308-87b5-40630097dc4e | -1.46145 | -49.32029 | 2024-10-13 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb473bd9-2f56-36f3-bfe4-06c10936b52c | -2.79568 | -49.29935 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf4e2888-8cb4-3db4-afc9-9aba33efa0bd | -2.79003 | -49.29305 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4c3b312-1c51-311a-bfe2-0c7152cc3a56 | -2.78925 | -49.29838 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6dcacb3b-83b1-3ae4-b369-a81c42fdf04d | -2.78886 | -49.29424 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 060d4b01-df04-34df-95b9-58cf522cffe1 | -2.78805 | -49.29953 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f76d9b92-6416-3ca7-b1fd-1933f049a563 | -2.77765 | -49.36727 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b0156ab-b640-3a57-8a4c-4660eb913455 | -2.77125 | -49.3663 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89400c24-ad84-3849-a6b1-e9847b527602 | -2.52058 | -49.67913 | 2024-10-13 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea1e6780-6033-34f9-8e33-1ae5998312ee | -2.51694 | -49.67671 | 2024-10-13 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f3f7a5f-4ca0-3474-99f5-cc8ddffcad4c | -3.3339 | -49.16113 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 680afd2b-2a28-3511-8f4c-d692be6da32c | -3.33353 | -49.16092 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac3ee675-9338-32fa-a68a-ffcc303ef8ce | -3.33307 | -49.16665 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b52a5fe-499c-34b8-ab45-e8784a4b4b22 | -3.33274 | -49.16645 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1851348-0f7d-3b6c-89fb-acdaa6d8e136 | -3.32094 | -50.46655 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6490957-4a73-30fc-b229-994a0945cbf7 | -3.31923 | -50.46293 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03b47b16-79b9-38e1-b8fc-e1f2885503f8 | -3.31855 | -50.46751 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94e761a7-a67c-3b9f-873d-2c7f11940aed | -3.1887 | -50.45934 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 712baada-a817-3eeb-8198-833c1b7da197 | -3.18801 | -50.46404 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bb7605af-dd53-393a-8fa9-352edca9eef9 | -3.18337 | -50.45389 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf84328f-b4c8-3e34-bd11-b2f7768a5a4c | -3.18268 | -50.45852 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bfdd0d78-274f-35fc-98fe-0d362ff3515e | -3.182 | -50.46313 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 20d4e271-561f-333e-9b3f-08a7b7192070 | -3.18133 | -50.46763 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6d129e6d-56a7-3888-989e-6ed9e79670ff | -3.17732 | -50.45321 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 63025f8a-e60a-3720-ab04-3bcb1fcfe0e6 | -3.17665 | -50.45775 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5372d2d6-340b-3e2e-8b44-540a3a2bbf7d | -3.17599 | -50.46223 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 66198068-7545-3d3e-a4e2-af76dfef86c5 | -3.17533 | -50.46674 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c62c3a5b-a4a1-3c39-a5f0-76b1e72fad78 | -3.16998 | -50.46139 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a2ca5720-becb-37dd-80db-fea7e737fbfe | -3.16932 | -50.46587 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| df642a7b-ee7c-35b3-b244-b449cacacdd9 | -3.16866 | -50.47036 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dc608dc3-fc73-3349-9ef3-72a6dee83882 | -3.16165 | -50.34979 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 462a3aa4-2881-3b7c-a952-cea19ac4c22d | -3.161 | -50.35423 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ce5a3e-a074-3605-af16-0afa785fb592 | -3.15948 | -50.35291 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9da03c5f-ab78-357b-9201-85b27a8fab19 | -3.1588 | -50.35738 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e1018f-212e-3831-84fe-49cedbf25f63 | -3.15558 | -50.34905 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b814918f-c351-367a-9dab-5fbfa3286f2d | -3.15492 | -50.35357 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 184fc672-73e8-3d0b-a68f-a0090f779fd5 | -3.15428 | -50.35796 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 525ddcb9-f670-38cd-933d-cd83432f6525 | -3.15365 | -50.36237 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 511a8dc8-cae7-3ff4-b12e-8a42d3d20f0c | -3.1534 | -50.35223 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59868de1-ce51-3e1b-bc74-f6aec74b4681 | -3.15297 | -50.36701 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1677b2c0-4a96-3576-85a0-bcbab9957fb7 | -3.15273 | -50.35666 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f9fed77-1454-36fe-ae6d-59dc653c54ad | -3.15231 | -50.3716 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b67b96e-7f98-3430-962f-db22f5f25e36 | -3.15206 | -50.36105 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9e6c9cd-ec6c-3830-b214-47792d60fac2 | -3.15165 | -50.37613 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ab38241-24dd-34f4-879f-fe857a5a6d2a | -3.15138 | -50.36556 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d02f1e52-b0b0-3ea7-a7be-9c4a2d09f938 | -3.151 | -50.38064 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b684ea55-9c0d-349b-b383-78ca562aef95 | -3.15068 | -50.37014 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fff1ed6-a53b-363a-aa0c-6623e583f269 | -3.14999 | -50.37465 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80db1750-9779-3ce2-aa27-9bc733f3b746 | -3.1493 | -50.37918 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4bed9a-ae12-3be1-8f2b-f9505ecb2b80 | -3.14693 | -50.3661 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 792f4709-0f75-30be-8c18-4a98ef978cba | -3.04476 | -49.41882 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9076557b-1a32-31f9-82a1-763193b013fd | -2.98749 | -49.52935 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0aa58d79-791a-3466-8615-8dcb7774df8d | -2.98672 | -49.53454 | 2024-10-13 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4442228e-8741-3556-8bb2-2f9f007cfbb8 | -4.12307 | -50.75541 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be832a6d-d5b1-37a2-93b1-7ea588302909 | -4.11706 | -50.75478 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed586015-08c1-3dbc-8983-efdb41145f89 | -4.40735 | -50.5746 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f38fcc6-007e-34e2-a13e-558f6be14d60 | -4.4067 | -50.5792 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79a273bb-217c-3fdb-ba38-b51dfd56d1af | -4.40585 | -50.57552 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a1ce253-ba98-3634-b065-e4f331ef2905 | -4.40517 | -50.5801 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab064af4-2a00-31cc-b08c-d03817c67600 | -4.36593 | -50.80349 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3e37853-ba07-3a8d-b7d2-5f26e4a118d0 | -4.36302 | -50.80227 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 797cc76c-3e79-3252-9fa3-0671958b1022 | -4.3624 | -50.80669 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29cfb66e-ef9c-3f82-8ad2-ca082452c432 | -4.36178 | -50.81107 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dcb6a2e4-45f2-3677-a11f-4a74b59a00d6 | -4.35994 | -50.8027 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e46349e-cb6e-3076-babc-c052c9c35896 | -4.35929 | -50.80708 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c6b0bc3-ccb2-313f-a4ac-5a01716b584f | -4.35865 | -50.81142 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0eafd275-91b8-324d-9550-d8fbc45fac43 | -4.35581 | -50.81016 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47f3c22a-39ad-32cc-bab9-23a94ad18590 | 0.94907 | -50.20866 | 2024-10-13 05:25:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4edf6b60-71f0-3a72-8d45-ba9cbfedec15 | -3.584 | -51.51308 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d62fc742-3275-3e0c-ba20-dca3c4e3fe99 | -3.58343 | -51.51687 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40ce0d20-9b20-3240-95eb-e00e865335ff | -3.57836 | -51.51219 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2ec6b28-ee3d-330f-ad46-55cfd0fb3c92 | -3.5778 | -51.51597 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 299bc2ae-d474-358c-90e9-44933b7ee762 | -3.46554 | -51.55258 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3db4a28-d87c-3ed8-8475-bec457eba4aa | -3.46497 | -51.55637 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cb5e5f2-4e4e-3b78-9fca-f92e7e4d6fe0 | -3.45936 | -51.55553 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7838b1e-1e7e-3729-a7f6-1ab550077114 | -3.3034 | -51.49698 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a635f6b9-630b-3f45-b7a7-eb75a92f1c67 | -3.30006 | -51.49727 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a15b6ab-2461-3dbd-bd3b-64a988f1a741 | -3.29776 | -51.49619 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48604382-5d57-3375-aca9-0ccd874047e0 | -3.28157 | -50.95329 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a16f8cc1-20cd-3611-92fd-fdf1effdb6f8 | -3.28141 | -50.95271 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 774cee64-2fcf-3ec1-bd96-b065ce1831cb | -3.04136 | -51.13504 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| de64a005-73fc-3023-ad98-1f7237a10a20 | -3.04023 | -51.13298 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0cbab1d7-71eb-3945-9128-989674de0f45 | -2.82124 | -51.33654 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d577e68-2bea-36ee-95bb-03d7273cd492 | -2.82067 | -51.34038 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51c7bb99-bec5-3528-9eb2-4c0b567ae469 | -2.81503 | -51.33953 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 791841f9-eb20-3009-b3b8-8f910fea1998 | -2.788 | -51.36655 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README96.md)
