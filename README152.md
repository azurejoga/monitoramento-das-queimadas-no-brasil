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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03b47262-ec0a-35d9-8139-42412c0294f3 | -2.84552 | -49.77585 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d639404e-c113-3443-b37c-8d87d9108b7e | -2.81888 | -50.49 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4460241a-1ca6-3bfd-9d48-d8745138aa58 | -2.8071 | -50.41328 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e3ff5289-0030-3411-b601-922368521687 | -2.77519 | -49.79036 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 154aec19-f70b-314a-8181-9fae4225b6dd | -2.77181 | -49.79088 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e472c11-2664-3a25-8fa5-7bab1fe8aa0c | -2.74762 | -49.76878 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3e40d774-f828-3f5c-b39d-08219ba8e001 | -2.74706 | -49.76517 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a4ef69d-9643-368e-add0-5814b0702e8a | -2.74609 | -49.76954 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3539401a-8a2e-3ec2-a8d8-57d64d105056 | -2.74327 | -49.77366 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e138dad4-66be-31a7-8dfa-eaab2abda21d | -2.74272 | -49.77005 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ccabd629-1336-3eef-8703-27a437d28a46 | -2.71004 | -49.78247 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 502855a0-584b-322b-93f6-f066e6963a15 | -2.70615 | -49.75721 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 42472a60-c487-32af-9ef5-4a62503913fe | -2.70555 | -49.77578 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e2fe4d1-0cc4-3199-ad40-297e9fa70bf1 | -2.70277 | -49.75774 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5107a79-1174-3415-a11b-60f091a4583b | -2.69939 | -49.75826 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c68856a3-6428-35e3-946e-8f055d670fa4 | -2.68971 | -49.82985 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c2ef1d7a-7afc-3078-9309-5651f99c4451 | -2.68866 | -49.77838 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 96c44242-6984-3b39-a33e-a5d9731b1feb | -2.67406 | -49.72882 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1de9f33c-cc99-3603-b2bc-c7391c578b3e | -2.66161 | -49.80468 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 51505a4b-e390-3797-b5b0-51146828d986 | -2.66105 | -49.80108 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d36acb91-4619-34ca-92d8-a34752a18a55 | -2.65207 | -49.72109 | 2024-10-25 16:52:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 069257f5-b1e7-333b-ad18-706f0891f0a0 | -2.62195 | -49.78166 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 98e28880-5da3-3478-bdd2-b7ce418eebf9 | -2.58197 | -49.76931 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2fd3bd44-ded3-33bd-8303-66e0f3dccfb5 | -2.58139 | -49.7879 | 2024-10-25 16:52:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 14cc75b2-4e69-387e-b4a2-81d6af5817a1 | -3.02225 | -49.57809 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f4972bbc-4533-3d55-be34-ca55e0950816 | -3.0098 | -49.58746 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 9eb2c00a-8e9b-3a9b-9dc4-515e32bdb222 | -3.00641 | -49.58799 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 51100764-35c4-31a0-9370-238ec8f3f59f | -2.94365 | -49.56413 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43159a32-7d53-3eab-a783-df32b146a88e | -2.9138 | -49.37333 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a922f3d2-f795-33b4-b02e-c5d3650ddf64 | -2.91323 | -49.36964 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31730432-8b33-3a67-962b-a6e236bfa11e | -2.91265 | -49.36595 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f897f37-d4b2-38cb-b233-5933e449e9de | -2.90181 | -49.36382 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 64ebdb32-b7c6-3437-b2c3-2ce83c134aef | -2.90156 | -49.36419 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1b8f48ad-559a-3d48-889f-cf63c6681d49 | -2.87364 | -49.45537 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ed90e0bd-aeac-3999-94ee-fedd2b5068d7 | -2.87137 | -49.46324 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9f153e31-e614-38f5-99e1-00798c37cf97 | -2.8708 | -49.45957 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 10872777-e44b-348c-ae69-c841e31464a5 | -2.87023 | -49.4559 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| acea4e0b-e7c7-3390-b8a5-422bce6740e7 | -2.86966 | -49.45222 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f29edac9-6fa9-39f0-ab9c-ca43f9c805c0 | -2.8691 | -49.44855 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7855f227-9611-39d8-a8d3-dbeb90c0f26f | -2.86739 | -49.4601 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db0b5848-7057-3e8e-ad7a-ed51cd2110c5 | -2.86626 | -49.45275 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 17dc37a0-66be-388a-a7eb-4a1640d5c941 | -2.86342 | -49.45695 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d3625866-90fd-390c-88da-eb0e830662ce | -2.86285 | -49.47583 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| df48f9a2-0202-3ab5-b0a6-1f8dd6d9117b | -2.86285 | -49.45329 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ce53cdfd-1374-30f6-a043-9350ea03de4b | -2.84757 | -49.53448 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 28349572-fba8-3f5e-808f-59837951e367 | -2.8447 | -49.49366 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8d86456a-879a-340e-a229-d378a6855257 | -2.84282 | -49.34666 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be6b881f-2720-3498-9ef0-03e7cf13dd78 | -2.82554 | -49.25793 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 66dc5cc5-a4b7-3b43-bb57-05b498af1d11 | -2.82496 | -49.25419 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9f428a9c-ebf3-3e63-bf51-011fe0aa20af | -2.82211 | -49.25846 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| fd96c03c-aa58-337b-bf97-8a2a9543f95c | -2.82153 | -49.25472 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 09f9148d-fcee-3e1c-9ef5-3d8541344813 | -2.81926 | -49.26272 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e3d8ee9-0c80-3064-bc44-b7b16dac4e37 | -2.81868 | -49.25899 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9cea0cbe-5737-350b-bf47-b1f56e70f730 | -2.81809 | -49.25525 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bdd319cb-5b84-318c-91db-053f55b46ec3 | -2.81751 | -49.25151 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c0bf4f07-1819-3d2c-8704-f06f09d90f45 | -2.81524 | -49.25951 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b9b411d-6ce2-3b62-96ed-fc60f4a436f7 | -2.81466 | -49.25578 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e9d3108-e59c-3c81-9f16-37a41368da13 | -2.81408 | -49.25204 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2a854304-e673-3425-87a4-268e170733b1 | -2.81268 | -49.58427 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 21de19ac-4a2f-3348-a75a-2a3db1dde1b8 | -2.80948 | -49.2451 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 395f3458-1046-3398-b35a-6ed5270406d3 | -2.8089 | -49.24136 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b01e7645-1351-3630-a3e8-344b6baecde5 | -2.80831 | -49.23762 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ba3ce10-1350-3bfa-9196-7372895625e5 | -2.80809 | -49.62229 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 2c776944-1bf3-3e52-90b5-09df3aabda99 | -2.80753 | -49.61865 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c29260db-24ea-3f7a-b45e-1a4d023449fd | -2.80611 | -49.26857 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| fc83b26f-0d9b-3231-9cfc-c41cdd0e4ebe | -2.80604 | -49.24563 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 273991dd-1c0e-341d-8cf0-b2ef78bbed2a | -2.80552 | -49.26483 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 97ee3016-a78c-3332-b7eb-7f706c71aa40 | -2.80488 | -49.23815 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6817dee7-9570-3368-b76c-179efef9f668 | -2.80209 | -49.26536 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f63190a2-b1cc-3851-9772-0df6bb3226ab | -2.80034 | -49.25415 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 17078055-f24c-3329-9e4a-dffae447ecbb | -2.79252 | -49.31643 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74b6890a-6f7f-337f-9dff-f1de697da4a5 | -2.78191 | -49.22636 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7635bb45-79d2-357c-8d99-0a38dc77cb50 | -2.77882 | -49.31793 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c2099a20-3c82-3997-b92b-98973b491f33 | -2.77653 | -49.3487 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a95ca6b9-2003-334c-8112-8de6cdfc0e86 | -2.77539 | -49.31844 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cf52b0b4-84d4-3dc9-bd6e-ea9985e62581 | -2.77081 | -49.51582 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1dc349ee-0e5a-3c46-96a4-1350dba8438c | -2.74132 | -49.55035 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddd3904e-d079-31d5-829e-44c4d667c310 | -2.73856 | -49.64414 | 2024-10-25 16:52:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c903b186-5f1b-3a24-ae51-a381b68500d7 | -2.70036 | -49.06044 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a745bda8-79cf-3030-b474-29e5f4430468 | -2.69748 | -49.06477 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 221e86fb-db95-366f-84d6-dd41ce15fe1f | -2.68795 | -49.32051 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f850e54-4ceb-3f07-8db9-d62bf62a7254 | -2.68682 | -49.15556 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6b19fb4-1aa2-3479-92ea-5df221a15a01 | -2.68043 | -49.13723 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 415f5a7f-aead-3820-a92a-542e876836ad | -2.63761 | -49.24437 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a9648d16-b020-3d36-aa16-63167c5fca73 | -2.63246 | -49.25668 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| a5db3b50-c59d-38ac-a051-b2923f0e2b1d | -2.60454 | -49.09872 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 052bf06a-0145-35c9-a145-baf8b8f42d19 | -2.60201 | -49.48952 | 2024-10-25 16:52:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b3572315-9df7-32d9-8b46-b5f0e25a9e23 | -2.60108 | -49.09925 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 22ba79fa-81a8-3c34-ba43-21bf009f07b7 | -2.57213 | -48.93524 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e320c1f-6d6d-3f6f-8994-2c7ae094e022 | -2.5687 | -49.23193 | 2024-10-25 16:52:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7a669aeb-6f5e-3e52-aa77-a8dc9b5b7fac | -2.56007 | -49.62766 | 2024-10-25 16:52:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52f59413-ede0-3d69-83d1-80dd25e31f2c | -3.46713 | -50.08632 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a322be4b-96e2-3cc3-8265-59b9584ddd6a | -3.46379 | -50.08681 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e17326bc-9316-3670-b425-3c121800cc63 | -3.44343 | -50.17339 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa53ea72-9cfb-3c72-99d3-20cabe934169 | -3.35756 | -50.10387 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c2390052-48bf-34e6-a0c6-924caefae9cc | -3.33453 | -49.95556 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0da54d71-f100-3ed1-9504-692ac939417b | -3.2952 | -50.16077 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| dbb0391d-e89c-3f95-bb46-02af13d6e8f2 | -3.28551 | -50.07578 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bda0096-df44-33f1-8146-36a5b67d62b2 | -3.28496 | -50.07225 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6beb3c43-4806-3dad-a2f2-99fec156b3f9 | -3.28216 | -50.07628 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README153.md)
