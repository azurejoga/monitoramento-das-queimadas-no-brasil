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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd28574f-1f8d-3890-a28c-e4c5ac4c4114 | -4.38339 | -48.69723 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3186b3bd-64e0-3748-b5d9-57a7708177ee | -4.38285 | -48.70067 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebd9d346-23d0-3e19-a065-38f3e8b0da5d | -4.38008 | -48.69672 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db340095-4935-326f-a4c6-a599e66b479f | -4.37677 | -48.6962 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9089a56-96bc-3694-a736-9fb95dc4315b | -4.27858 | -48.0639 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 947eeab8-1739-33a4-94a6-4ff99158662d | -4.20048 | -48.86564 | 2024-10-05 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9354f47d-1620-3809-842e-7facfd371981 | -4.19994 | -48.86908 | 2024-10-05 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25de25d7-379e-3781-b65b-cbd656b0632b | -4.19717 | -48.86512 | 2024-10-05 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 084fdb5d-eb1f-3369-a57a-c286846f51d9 | -4.19663 | -48.86856 | 2024-10-05 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b69b9549-7075-36fc-b0a9-2a82b319ad74 | -4.09389 | -48.48584 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2178192-1bb3-38c9-9f41-b9406408607b | -4.09262 | -48.27692 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0e6b96f3-6e1d-3e96-a3b8-671029ee5e9e | -4.092 | -48.25911 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a6d5c13-99fe-32b3-8bca-304a86a5f86e | -4.09004 | -48.48876 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79932252-5795-3761-b528-f9f4ef369f90 | -4.0895 | -48.49221 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201bec30-8647-33ab-9762-f8f1d8461fb9 | -4.08914 | -48.25478 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb5dec47-d9cf-3384-b239-9542dc492044 | -4.08806 | -48.2617 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61c31c9e-c360-3e1c-94bb-980905bff0cc | -4.08673 | -48.48825 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 124aa141-d36e-34a8-b708-922db22cdd27 | -4.0862 | -48.49169 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea3d8887-64d1-39ee-8cdb-e78e917a6562 | -4.08397 | -48.48429 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fecd522-c544-37eb-bfab-fafe84a476f7 | -4.08173 | -47.95443 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d5fdc0d3-ef28-3424-9fc2-5b70eaa20b8a | -4.08119 | -47.95794 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a2219cf-d80a-3a3d-bb11-d678515b0801 | -4.07895 | -47.95042 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ded2aaf9-a06c-3838-90bb-f074b2bc5fe2 | -4.07841 | -47.95391 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a6dfd52-9446-31d2-aba4-d9f4c174afbe | -4.07735 | -48.48326 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfe993b6-ea02-3ba0-b880-35720aee9c2c | -4.07562 | -47.94991 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a3e5ed28-b71a-3478-a9b8-5ceda8e67469 | -4.07393 | -47.93889 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbe0b7fc-f55c-344a-a8fb-47c81b91d830 | -4.06951 | -47.94538 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 62dc1276-4f10-3055-a988-dd5f9a87cafc | -3.95645 | -49.03503 | 2024-10-05 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4a2c1e2-0f3c-3946-8c13-efc3b19b9e96 | -3.90168 | -48.34662 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04ada2d2-bcbf-3c6e-ab4b-cfb9135d1cc2 | -3.90114 | -48.35007 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4f0ae52-5afe-3148-8d37-e784fdeddde0 | -3.90006 | -48.35696 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cade6f0-87c1-3f16-913b-736241d9fcd1 | -3.89837 | -48.34611 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 790e1f0d-a3a8-3c86-9b1e-3bdee24d815f | -3.89783 | -48.34956 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4515462e-9375-3d54-ba8c-a4dec52e319a | -3.89729 | -48.353 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d47bcf1-6193-39fb-8f11-8121e5874886 | -3.89614 | -48.33869 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54411766-ed13-3899-ab3c-adf3839b093a | -3.88898 | -48.34111 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 889477a4-2c6a-3ec3-947b-974fbb5d6862 | -0.25372 | -48.77355 | 2024-10-05 04:36:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5e8d458-c643-39d2-b3d2-968b653f383a | -0.2504 | -48.77304 | 2024-10-05 04:36:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de53db51-5e76-3aa7-8c0a-b9b0d4a285a9 | -2.20234 | -48.84832 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bda191e1-9e12-300f-8830-e38c63851542 | -1.16549 | -48.85221 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a59a5ea4-33a9-3685-b02c-a33f9309c218 | -1.03699 | -48.69769 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce29fcbc-274a-38e1-b2bd-99670dddd584 | -1.03422 | -48.69373 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4efde5dc-d814-350f-98bf-4e0986c45a47 | -0.86515 | -48.68824 | 2024-10-05 04:36:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 879a4976-8cdf-3be3-967e-7acd0a7357ec | -2.20179 | -48.85176 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00c2b11e-c80f-395e-86fc-9507fa41982e | -1.16603 | -48.84875 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78b3d40a-4b0e-346f-a502-5f350ba5a950 | -1.16272 | -48.84824 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 486ceb40-0462-3abb-a42e-48f3f7fd48a9 | -1.03644 | -48.70114 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 571768b6-1f25-3b19-9c72-0cd658d8790b | -1.0359 | -48.70459 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70c25be0-e70a-3719-be07-9d46130598d7 | -1.03367 | -48.69718 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def1ab5d-961c-3bf9-bc01-ee86cb5e58c2 | -3.32377 | -50.07376 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b44e01f9-1784-3d51-8a21-d83943b0fcd6 | -3.3232 | -50.07734 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d319414e-a77a-389d-a5fb-d9ee47ab6723 | -3.32041 | -50.07323 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77cb9f38-b446-3679-be73-a860067f85e4 | -3.31984 | -50.07681 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bbda7a5-d6df-3075-8f08-0dda6f28b678 | -3.30755 | -50.04556 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed560e64-d34c-3ef6-8fca-590949805dfc | -3.30419 | -50.04503 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b965455-7c94-3cbb-bb12-aa049853731c | -3.30272 | -50.47119 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 382fe8f0-de2f-3cd1-8991-c3110a15968e | -3.30047 | -50.46334 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22413ea5-98db-3e34-a845-5a736b58a9a8 | -3.29932 | -50.47065 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a6f78f9-00b2-3af1-92d5-a5338b428ad6 | -3.28005 | -49.10215 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb0535b9-e83e-3f94-bd35-06be00afd24a | -3.27951 | -49.1056 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da2762a2-7f76-3983-bab1-cbd8d5f0256b | -3.27674 | -49.10163 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96409754-8a9c-32df-afe5-8dfd6064302e | -3.27463 | -49.13664 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 722df6e4-4fc6-3f6a-824f-e3ca08a12990 | -3.27289 | -49.10456 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b709e70-51e0-3743-8c51-c3105b7615fe | -3.27132 | -49.13612 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b04d318-cb6a-357d-b179-6a9a578ed5b2 | -3.26849 | -49.11095 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b1925d1-896e-39f8-bf95-83807a39d0bc | -3.26795 | -49.1144 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e52afb4-0805-39ef-9f36-2a2fbabceea9 | -3.26573 | -49.10698 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c199cf20-1ed8-3dc1-b5a3-1b22e6c45b76 | -3.2579 | -50.14054 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e34996e9-78ce-3201-bd06-a5aa47d25ea2 | -3.25452 | -50.14002 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a84f7782-d28c-36da-9ef8-0efef8d996fb | -3.2542 | -50.1108 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a136a3c-2843-3e0f-8ba7-0fe66ab0616d | -3.25195 | -50.10311 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7176b7bd-5062-31d6-b559-f91add0624a4 | -3.25139 | -50.1067 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72698ae6-089d-3b6d-b85a-19b198862429 | -3.25115 | -50.13949 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8e1ca86-c906-351b-bb91-5846e975cead | -3.24969 | -50.13954 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a520ae48-15d7-3035-a8cd-c1d043d600bd | -3.24651 | -49.40188 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aebfecb8-71cc-3807-9fd7-b45122c817d8 | -3.24542 | -49.40883 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76b0147c-333b-3e76-b4b8-b88af47f3409 | -3.235 | -50.37057 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37fad14b-dae3-36ed-826a-140310f569a0 | -3.14587 | -50.22668 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec8f0139-8cf6-35a1-8a4b-98895332be85 | -3.14364 | -50.21894 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9fdbfb7f-baba-3478-a065-8ee860a921d7 | -3.14306 | -50.22254 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5aa6229-e744-3383-aaac-a441ec219082 | -3.14073 | -49.23252 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bf046e1-8855-3cdb-8a3d-5ead799e6312 | -3.13968 | -50.22202 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7b87d9c5-62e4-3463-8242-45246ef9ab75 | -3.10965 | -50.47511 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0108b5ae-5438-3d6a-9322-53be51954814 | -3.10683 | -50.47088 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d24c3b4-933a-3fa0-9aa9-f1a68b1fb3a1 | -3.10624 | -50.47457 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d298cf68-058b-3d2a-b78e-3231a061bc08 | -3.10342 | -50.47034 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d06f2f4f-408b-3506-bc52-26d48e7ad047 | -3.08819 | -49.63112 | 2024-10-05 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 120708c8-e0e6-39c4-9133-f3ea31b0ea5c | -2.80482 | -50.31921 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a9f6eef-0366-3548-8791-9230847a6fd2 | -2.80142 | -50.31866 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f670b2d3-cdaf-3177-9194-23579c12669e | -2.79931 | -49.58569 | 2024-10-05 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 370e0378-e4bc-3050-a7ca-7bd2995644cb | -2.79462 | -50.31759 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b713061-4b7d-3ffc-99c2-16b3a7e447da | -2.72533 | -49.53849 | 2024-10-05 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 960d9d4b-dab2-3810-93ef-78edd43deaac | -2.64712 | -49.10882 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb938bc4-a2fa-3cf0-bcf7-d82e478e72ab | -3.38605 | -49.24947 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1e14892-db73-3896-a54d-ab7454378598 | -3.31517 | -49.13928 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b975faea-0ae4-356e-83bd-ef5f9eedd97e | -3.30742 | -49.46816 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 326b63f3-3301-3954-b89f-baa810531385 | -3.28559 | -49.11008 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 812cc774-a8bc-35d7-9a20-fe8080e8f73b | -3.28282 | -49.10611 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcb0218a-14fb-3d26-9ddc-effe0876c532 | -3.27235 | -49.10801 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c35d38-d70b-3e5b-8f43-bb7b4a4633a1 | -3.27126 | -49.11491 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README92.md)
