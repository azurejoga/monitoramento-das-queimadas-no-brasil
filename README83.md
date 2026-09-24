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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f533720-d6c6-38e6-a30e-960b46c1c94c | -9.34644 | -65.73313 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4ec67c9-a791-36cf-8db3-8b3ab01424f6 | -5.86128 | -60.1624 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c237d1c-e24a-39f8-bd18-ba865c6a6152 | -9.64588 | -67.06695 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e4a0551-6c34-3465-b470-b0fda2c5791c | -7.89735 | -61.16748 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bcc408a-dcad-3fd7-972c-966254a74625 | -8.01021 | -71.31287 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87e0e7e1-801b-3194-be59-3caca49a4184 | -8.57261 | -70.88256 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a87b3892-12e0-37e9-a7a5-eba02618cb5e | -6.06917 | -57.79994 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf0674d5-b30f-3619-b61e-69d80c178907 | -6.89686 | -55.57813 | 2026-09-24 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 834d040f-4ec5-3909-bac3-0f5bc409efae | -6.45668 | -55.00738 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 307a30f2-e452-302f-8401-94fe5cb352f4 | -9.49819 | -64.03101 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a163807c-4ab9-36fa-a310-af0f66f5bf85 | -9.75315 | -64.30612 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17c6f3c2-e09a-3fed-bd57-3655b110ada3 | -8.64561 | -67.02868 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9869a75e-efc6-387c-ad6b-401ca2cf88e6 | -7.88748 | -61.17451 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6041cfb7-63f3-3861-b6d2-7b32bdea93e8 | -6.08856 | -57.6232 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00904c56-399c-3069-a304-16f091c69cf2 | -7.87759 | -61.18171 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e0c9f1-96a5-3ba0-9853-cb97dfcab454 | -9.19119 | -65.78674 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e1a3b07-d77b-3668-876f-da2e08837391 | -6.67437 | -58.57616 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92071ed2-4216-3c64-86dd-36dd537cb9e7 | -8.77384 | -72.77275 | 2026-09-24 05:50:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad572a0d-542e-350e-86e0-3262f029b4a9 | -10.24387 | -68.29623 | 2026-09-24 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 586e790b-09dc-36cc-ba51-4159b1587cde | -6.66967 | -58.57236 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85c73f87-5c04-31fd-a3d2-7a00da7dbca1 | -8.54004 | -70.78603 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f50675-d4b1-38b0-8210-ed2388b89e25 | -7.0469 | -62.93004 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c7357ca-5213-38ae-b656-a2c0b4efe166 | -6.65984 | -58.5678 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82621f4f-d027-35af-a6a7-68cdabafa2f9 | -6.12718 | -57.7607 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8dc5414-068d-39ed-aa14-d5b2e4d7e699 | -7.05387 | -62.93596 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fddd1b2d-1b3a-3f96-bcb6-1709a152458b | -7.69619 | -69.92767 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40cf6b41-3b2b-3f68-ace5-eafc51aee1d9 | -7.04932 | -62.94017 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8337473c-8ede-38b1-8fc5-688e44629f4f | -6.43922 | -59.95559 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e37bf8f2-7f97-3de3-ad23-48f3465d7361 | -6.43534 | -59.95761 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bd1f5c0-2c99-3dbc-8948-219de2a46502 | -9.94217 | -60.72702 | 2026-09-24 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b1001d6-23b8-301d-bdd7-3fc6e44459e4 | -6.07451 | -57.80081 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1a0f0d9-85cc-345a-b288-9af64be242cc | -6.30407 | -57.75161 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f4fa4af-bf56-322a-b94c-f53c3970e619 | -7.52091 | -61.48555 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 222806a1-fe62-3699-b2a9-1fb34c55a29f | -6.10377 | -59.88326 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b52b70df-6a51-3a0c-9ef9-29e8a3ae4d73 | -8.86224 | -71.38052 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c59f823-9b3e-3b98-b935-d99cfeab5453 | -6.6164 | -59.93372 | 2026-09-24 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eea2020b-e5b3-3925-8c31-26884cdb511d | -8.65277 | -67.02621 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11f6fa33-9dc6-3307-aff0-96af3bf1d312 | -6.75706 | -59.73651 | 2026-09-24 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 303ab7bb-777f-3950-93ea-b4fed7b81b81 | -8.91108 | -71.33838 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff40f939-8aa7-33b3-9354-fa15c6d472b6 | -7.51666 | -61.48489 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70ae9b77-a2df-3548-a1f7-114b624ba865 | -8.986 | -65.40525 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e598fce7-0dd0-3645-ad72-c9e52d536b32 | -6.10654 | -57.66982 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 711f1329-dc4f-35d6-85a8-d443be56154f | -6.07402 | -57.80426 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ba08a7c-a7c0-384c-816b-f154b3f819e6 | -9.56102 | -65.98633 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 071de453-70de-3bbf-912d-5a48fa2dfce3 | -9.03924 | -65.42028 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f0d9eab-b318-35fc-91f5-5d633c891f7b | -7.04235 | -62.93424 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72e8f362-4c3c-3b71-91aa-ed5f84dd9d47 | -9.50891 | -66.76373 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecdd6684-33eb-3b7f-aba5-deb1598b1cd6 | -9.04787 | -65.40984 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18b39c8a-c008-382a-a7ec-375774df761f | -6.61174 | -59.93303 | 2026-09-24 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56e14e4f-09af-3a35-bdb1-5825d82bc6cd | -8.58723 | -67.31471 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84e5735d-9f81-3e07-b10b-b878543843c4 | -8.56829 | -70.88624 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 505a6cb5-b72a-30a4-b47a-56bab068a9a9 | -7.89183 | -61.17523 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76e78554-787d-3b8d-be76-aa29be35e201 | -6.46369 | -54.99537 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5afc5dca-dc74-330d-a65c-b4b97e663981 | -7.89124 | -61.17949 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7393e47f-2734-3b4a-b770-27559d2a8679 | -9.70127 | -64.91012 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72052ecc-10aa-3def-8cec-179338fa878f | -9.22502 | -67.39092 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d510ad11-0e15-3cda-8642-59f812422834 | -9.64534 | -67.07047 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a653bc3-5fde-3e1c-801a-c9442250e0fe | -7.40562 | -61.62979 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27a4c91b-9fcb-3180-b35b-b1f01a55c165 | -10.03645 | -62.4589 | 2026-09-24 05:50:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04d98656-d9ff-3bb6-a391-423884e80112 | -8.94046 | -68.55674 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cc139c5-ad7e-3b61-9566-275d46ec003c | -9.10412 | -61.43834 | 2026-09-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04075cb0-59b0-3cca-9e01-0d4af3301592 | -9.72448 | -65.02069 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 444e70ec-32f4-348c-a1c7-276c36260874 | -6.4407 | -59.95341 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf041128-64e8-360f-92fb-7ac4a7b3794a | -6.67729 | -58.55499 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 850dd846-34eb-3232-a1c6-e4b6c34eda99 | -7.58738 | -57.66219 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57ef762f-5f8e-3f1a-8ec2-71c4ffe80a4c | -7.90606 | -61.16887 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f883d69-0c07-356e-9076-0e0b6bab5edc | -6.00064 | -57.72151 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b306ffdf-03af-37c2-9939-c61877aeb98b | -8.91374 | -68.63945 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53bced07-5f29-3981-9613-cd598f858159 | -9.93885 | -60.71656 | 2026-09-24 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e79fdaff-1fca-3292-9d43-287c892014a9 | -8.90593 | -71.3466 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8124c8c8-fec8-3c61-83f2-8eafd8338b9a | -7.88253 | -61.17811 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83087638-b7e7-3124-b93d-c07d8f049506 | -8.88543 | -62.54662 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cfa2419-248a-3fd5-a220-0f7e7bff5859 | -7.51532 | -70.39397 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9de44c8a-db25-3fc7-b2f2-3265002c94cc | -6.09397 | -57.62401 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25eea169-2d9d-388c-ba39-d6d6cd2a1db8 | -9.75378 | -64.30179 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a15b2e5-b528-3b75-8ac1-bd76771fcd3c | -6.04573 | -57.77211 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f095c7c3-63f5-3655-900f-f14c3783a8d6 | -5.86649 | -60.15852 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b5847c1-afd1-3564-a7e2-8a4acf8e0dac | -8.91041 | -68.63892 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7a21cb5-4620-30ef-80b8-e38c2de50511 | -6.46297 | -55.00071 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b205eb5-9100-3ddf-8a6c-159d2754f28d | -8.88642 | -62.53948 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e75f1b15-fe54-3761-8d88-8248756e82e7 | -9.03399 | -61.65731 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c02de18-2440-3804-b947-8c77ef2fa293 | -6.67908 | -58.57994 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fb20290-3d7f-3cbb-9938-752705bdf195 | -6.68211 | -55.04687 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cc76e86-fa84-3fb8-8546-916078fe7e14 | -7.89741 | -71.69197 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a63635ea-be5f-32d8-b45e-fdd7508d16b5 | -8.30776 | -56.36277 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 536fc95d-6c0b-35f0-9e71-cd57d369411f | -7.89241 | -61.17098 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61169ff8-09a5-3668-987c-b94e12b1cfaf | -6.04038 | -57.77128 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 10d36b84-1e7a-3dc6-87ab-eb29dc14c556 | -6.34573 | -57.76862 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25f868c0-35d3-3e58-b20a-98f7979aa562 | -6.35064 | -57.77288 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bf8fbf1-cae9-37bc-8794-3ac7b7e51922 | -9.04845 | -65.406 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2087102a-4d35-3349-9a0b-b0e2230c9d48 | -6.35109 | -57.76958 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae236afa-25a2-3522-8eaf-ac14c2b2f1eb | -8.92671 | -61.49189 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a15d31d9-c5f4-35e9-9372-8d9318953a3c | -8.88593 | -62.54305 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccdc818d-5e55-3327-8faf-b267e0dd6760 | -8.30603 | -56.36643 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38c8d5bb-0955-3a80-9160-747af8f987a4 | -9.32655 | -56.81646 | 2026-09-24 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbab0520-e84d-37bd-ac5c-580df8bc89b1 | -7.66692 | -69.93097 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8d4ba4d-c93e-34ee-b959-13fde174671b | -9.56157 | -65.9826 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64903520-3a17-3ba2-930e-30ae64724644 | -9.50611 | -66.75967 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0863df5f-a08b-34c2-83bc-816f394a9c51 | -6.77151 | -63.14339 | 2026-09-24 05:50:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f38d4be7-a36a-3ae9-8996-44668990befb | -7.04549 | -62.9396 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README84.md)
