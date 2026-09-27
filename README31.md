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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76e3f45d-1b15-3a00-a1c0-b39ac0bdc6fb | -2.96304 | -49.56293 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6cd8304-17ac-3388-8538-458b5adcc717 | -3.26833 | -50.08871 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b1076b6-4e91-341e-ab2c-eee8cfc51af4 | -8.46848 | -54.92126 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8c00741-a594-314a-bcc5-7bd173c1c4d6 | -2.96294 | -48.70499 | 2026-09-27 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 000a7659-40ad-3014-b8d1-449285493037 | -2.44618 | -49.22378 | 2026-09-27 04:51:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7047eff-5a42-3711-8eaa-c267e33bdb52 | -5.73402 | -45.02148 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd9ae5bd-e6c1-3325-b717-7ff62cc844e3 | -4.26173 | -51.04425 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ea4c4f-42df-3eda-a7bb-7a7a0bb0c34a | -2.99414 | -50.47375 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c128a872-acf6-34bc-a2f7-195e4787bf87 | -3.72039 | -54.65435 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ca164dd-b9e5-3244-8e8d-3b214954481b | -5.74207 | -45.06638 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 754a40bc-5b40-37c6-9580-5f85590f8578 | -8.49788 | -54.78046 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a89f2a01-dafc-3d90-8550-3e95f0cb6a57 | -2.89433 | -54.19297 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ebbf047-c261-37cd-b371-8fd47fa26d4b | -3.4187 | -54.00671 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f89a64d-4e03-3965-8c02-abdbaeb6b5f4 | -3.07515 | -54.40294 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15f16ca9-2f7f-3973-9470-63dc0c5b9c13 | -8.33977 | -44.16087 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24eae4e2-cf36-3fc0-abb4-96115210773e | -4.28503 | -55.25719 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e253516c-7717-3e43-a1f5-eb97c4dff936 | -2.73601 | -49.462 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48c1de66-c324-36f3-9989-88dfc174cf3c | -5.66514 | -46.36058 | 2026-09-27 04:51:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a44c3a3f-42dd-3aa1-ab2e-a2b22264804d | -4.54528 | -55.53444 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6780695b-681f-34df-8fc3-f1ada23d1c3b | -8.30274 | -45.64193 | 2026-09-27 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 242b77ba-3b2b-309c-80d9-016db5fef8ad | -3.26679 | -50.14491 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfaa4ff2-35d1-3cd6-916d-3e3a14d18d95 | -4.87804 | -55.84637 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5df211fe-cfa8-32bc-9c71-574cb85fcf50 | -6.07377 | -57.81429 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81b2e369-f717-3cd9-9267-fea729719ca9 | -5.16697 | -56.00808 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8efffce7-0817-36d6-ad11-88b2297d7c84 | -8.35702 | -44.15951 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 854bf994-9830-3d6d-8b31-531d29377416 | -2.05709 | -56.86879 | 2026-09-27 04:51:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88440751-a9fc-323c-ac01-b18951af5be8 | -6.08801 | -53.51533 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aed0d3ba-7799-316e-905c-ef0f194fe951 | -8.47524 | -54.92237 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5af95b24-a6a4-37df-b2d2-b9abd832d8b1 | -2.92497 | -54.15535 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b66dc53-9f84-34f0-a274-9d9ddc084057 | -2.89148 | -54.18869 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dbae24d-7047-3938-b881-c26a2b467876 | -5.82635 | -52.03368 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b7812c-070d-39cf-b382-dce479c9b3a0 | -6.78074 | -48.66209 | 2026-09-27 04:51:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9c46055-120b-32be-a444-4942691a2692 | -1.11167 | -57.0633 | 2026-09-27 04:51:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c40f8e8f-6859-382d-96c2-cab537fdac06 | -6.07668 | -57.8147 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ed0413b-aefd-3c46-93b9-d5921a0b1bea | -7.38367 | -47.02061 | 2026-09-27 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16ecd4cb-8506-3322-8e4b-2c185c4a027d | -6.13374 | -44.59025 | 2026-09-27 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7061eadb-dd84-31a9-b209-1d7c823a36be | -3.42562 | -50.43165 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c27f973-f306-34ef-820b-e7a73c086215 | -4.54273 | -54.98211 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ae7b4846-fcc7-3246-8176-41e6627a7085 | -1.61905 | -54.9194 | 2026-09-27 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5d79cc2-678a-3866-80d3-03f6c4db8260 | -8.07753 | -54.74998 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fc3631f-6215-3fdc-a090-ee2ac037c1a8 | -2.862 | -54.13023 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afd25a33-9dfd-3358-911b-663aed2f135a | -3.22827 | -54.32534 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb905f84-3541-3a19-8abc-0293a4dd52c9 | -3.94939 | -53.8501 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c7fd66a-d1b9-358c-9249-ad01ee88f7e0 | -5.2767 | -48.38611 | 2026-09-27 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9235551-76d1-31f7-b6a2-d0cd6b4cdcec | -3.08209 | -54.404 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e8bbae1-c586-3b4f-98a2-d6e84254029c | -5.73961 | -45.01675 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 69dc87cd-126a-34af-94f0-0755885a77a7 | -6.06918 | -57.80993 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d767a72f-7950-3976-abdc-4946eb9d686e | -4.71471 | -55.71864 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 636af663-3e7f-3cf6-ad02-e679debf025e | -2.458 | -50.54602 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb35faae-f432-3719-995b-d0cec5db2c18 | -2.96303 | -54.09224 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15770b26-076f-312c-b3c3-e67c1d2d9e8b | -5.82411 | -52.02622 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2698f27-9b30-3d00-9384-4ea46c761274 | -8.28363 | -45.41713 | 2026-09-27 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ced03aab-b673-3096-80e3-48800f2313b8 | -3.87377 | -51.79158 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d20e9da-39e7-3375-ba7d-e0f6695d9305 | -4.05216 | -45.33345 | 2026-09-27 04:51:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 6e22db81-0ff2-38fd-8cd1-6872b3fe86f1 | -6.13006 | -53.0532 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d62060f-f7a2-3de0-8740-8d7bd69251d1 | -8.34779 | -44.1824 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| bfa85200-545d-3f27-a080-aa37621c619d | -6.07726 | -57.81113 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c2f6370-fcdd-30fc-af29-bfc1d430ba79 | -8.32034 | -49.97337 | 2026-09-27 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9827595-461e-3e66-bcc2-f4fc85acd3b6 | -5.73883 | -45.02214 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c67aba96-92f0-3d37-b855-604fb5a5e604 | -6.07781 | -57.81487 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de5c718c-a57a-3c75-a1ca-6c358972db6a | -7.29116 | -43.30474 | 2026-09-27 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acd27ce1-71d3-3b84-a48e-cb1cd572ab27 | -3.8504 | -52.01057 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f842a16d-182a-3b32-b7c7-cf92e0edfbd6 | -6.9316 | -62.94154 | 2026-09-27 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce7110c3-5e2b-3d1b-842e-930d4732ce87 | -2.89665 | -54.08959 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2735fcb4-03ff-35ec-8bcd-1d89450a8620 | -3.92132 | -43.02272 | 2026-09-27 04:51:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64642c49-792e-3ee1-8ba6-5676e710ee1f | -6.07611 | -57.81823 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50e554a7-a7e1-31e6-9fd9-e2a9a36a877e | -4.51695 | -54.98602 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 868c4a65-f024-348f-bab8-cd37afde0ce6 | -2.37709 | -50.409 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d0d71e4-3319-36de-8a28-3575adeb1a5c | -4.50982 | -54.9409 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f439e7d-c7da-3af1-a59f-da728b9fc0cb | -3.01861 | -51.53834 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d05fe16a-cc4f-3bf4-9c7d-ac010b2fe125 | -3.12015 | -45.43632 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b0fd25c-9fa1-3cec-ace8-1432ee9674b0 | -3.22279 | -53.96138 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fd91c3a-b965-3f60-bda9-6ccfd91d8401 | -4.27335 | -55.42339 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b184ebe-380b-3bce-9bbb-c51f73c68654 | -2.56605 | -57.37352 | 2026-09-27 04:51:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6d1abcc-1c39-3903-b709-68d3d02096ec | -2.83038 | -50.47116 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8a3e362-bc03-349c-bbc8-4e79387caece | -3.96904 | -50.7139 | 2026-09-27 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d08b245d-6e22-30e0-961a-6e64c7eda33f | -3.09297 | -49.35358 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1f5eba2-3437-356b-bccd-50068d35d931 | -3.10002 | -49.35467 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30968ef4-489c-30d3-a7fc-97428c3ad5e1 | -2.83859 | -51.36153 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6989bb52-1186-344f-9e63-7d0eb472b633 | -2.88852 | -49.4803 | 2026-09-27 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c03724f2-1096-3453-9e96-20ef61c9de41 | -3.21996 | -53.95721 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb861f9-817b-384e-af6a-6d8688de36fe | -8.35251 | -44.14584 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b09b088-b1e6-3080-95e3-aba60e78dc61 | -9.31396 | -47.63313 | 2026-09-27 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f72928b-33ae-39c9-a814-c0ba909b0baa | -6.87926 | -55.5544 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d746ff4-0ea3-3a24-9b32-55824311844f | -8.34275 | -44.13764 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15869e92-88c5-3680-a232-3d15ef73309f | -4.87743 | -55.84695 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09b923d6-10bb-3a76-8423-aff533a48f6e | -5.17904 | -46.08234 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7add0224-9693-34af-94a7-e4827219c9b3 | -8.35652 | -44.15664 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a8785fe2-2b64-314e-b27c-2605e3cd3524 | -8.35218 | -44.15544 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 10d19f3e-7e67-34d6-bfba-2f4170d8ca0c | -5.27777 | -48.38425 | 2026-09-27 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d5641a7-f363-30df-84af-5b2a4adec507 | -8.34766 | -44.18849 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0320b852-ee4f-3afd-a0e1-51247c102db9 | -1.11109 | -57.06691 | 2026-09-27 04:51:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df6d11d6-9c06-3832-9a39-478e09f717a8 | -2.97191 | -51.05112 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32976b3e-6df1-37d1-b593-c1c0641fafb2 | -2.88377 | -50.46097 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c75d2e0e-1d9f-3bd2-b5e8-167a7f9ff76b | -4.78087 | -43.65862 | 2026-09-27 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbae809a-df68-390f-b83a-efdec60582e0 | -3.07108 | -54.4062 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 999cb5d9-f107-3d9f-b850-5ea26cc24ba5 | -4.49806 | -54.94706 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e46d0cde-4dc3-3ee3-8c4b-c0063e217221 | -4.97446 | -56.15285 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c58b4e7-f631-30db-aacb-7a4759b919e9 | -7.27507 | -55.57192 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 603c26cc-1604-38cf-aee9-eeb2696b05d6 | -2.95792 | -54.07997 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
