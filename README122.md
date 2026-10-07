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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ce1d6af-4108-359b-9534-b4a5e9fe8835 | -8.33607 | -72.6086 | 2026-10-07 06:01:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54d4590f-da59-3fe6-9337-d8e6b3ac9c57 | -7.88757 | -72.35345 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f5cdc02b-6540-3ea0-8a7f-21d06faf6f7b | -9.44812 | -68.40002 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2184d4b3-d49b-3d50-9c1c-bdd432799965 | -8.76595 | -71.11219 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e7bbbf-62fd-3270-a148-d50ad081981a | -10.04167 | -67.75168 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0fe16f42-de15-3e90-afc8-bca0d23cade0 | -9.23627 | -67.88638 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32a65604-ee42-3b30-b5bb-b1e6722e9b0e | -9.69741 | -67.50876 | 2026-10-07 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05f86b06-67a5-3084-84d4-adc9e6f06c2f | -9.10322 | -67.75449 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 758b2aff-b068-39af-b208-17c06d7e8610 | -7.9525 | -71.33917 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fb43ac2-b862-3f41-a4d7-80291d490ff8 | -9.59097 | -65.24067 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1db822e8-1731-327a-8c41-59a32ae31f8b | -8.97632 | -67.507 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 677f0dbb-f30e-3f6c-ac4c-2f7d0051b644 | -8.9731 | -65.44463 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 274a6f44-63d7-302c-a0c8-691d34964c66 | -9.05665 | -65.48308 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15c5aba3-dc74-34d0-9b79-8df1c779fa8d | -8.28908 | -64.06744 | 2026-10-07 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80251878-30f3-35ab-8bfe-2fd0c33ac3f2 | -10.03884 | -67.74746 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ebf60f3-6f58-34ca-92d9-4d1836384f3a | -10.08884 | -68.47079 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 213c706d-e958-331c-81ea-8728ef2cf9d3 | -8.58293 | -67.22003 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 465de24e-0a59-3ffa-984d-6e09128a88d9 | -8.69293 | -68.71246 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227588b3-6755-3b12-b3b0-3ff83ca9541f | -8.77788 | -71.16793 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b5e660-9750-33ec-95d8-36bfe299e8ac | -9.14533 | -65.30338 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14374b71-bea9-3a6e-9196-90b824632ba7 | -8.88789 | -68.81161 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dfd336d-5b45-3841-bb0a-5f56b881a5cf | -8.97751 | -65.4407 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cc43785-d79f-344c-b54d-fd0f4b8471d4 | -8.96618 | -68.59436 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c924e71e-eef2-3b85-a7f2-804d7d29ec44 | -8.62682 | -67.04979 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9429dc4-a991-3d6d-a4c9-5ecfdc485518 | -10.58597 | -69.24395 | 2026-10-07 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bc32b93-c45f-36cb-9f4d-5ffea51b7143 | -8.7813 | -71.16851 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ceda13b-6c82-30f3-a8a4-b6e9105a1ec9 | -8.68961 | -68.71194 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0fe5c52-9ae2-30e0-9fd9-5a65557bb564 | -9.05827 | -69.6883 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17fd8179-7313-3bba-bf78-3d8099f79ca2 | -7.0288 | -71.74694 | 2026-10-07 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a786bbc6-5f2e-3460-8201-8dec2d6ed16b | -8.84806 | -66.79156 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1178a175-2138-3eb3-8a17-8765f2184b85 | -6.84735 | -58.59511 | 2026-10-07 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fce096e-c38f-308d-8736-050992ce1304 | -8.46278 | -70.83944 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c36e7be1-da40-35fe-8464-4dc8dacef93f | -9.46402 | -66.78444 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9924d7cc-c073-3266-a923-2c4afe866de7 | -8.63187 | -67.05704 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bb4ed4ee-f319-31ac-80b9-d95038491aba | -9.2357 | -67.89 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 141f7d93-6915-3a4c-976c-2e2b0daa0c9f | -8.65367 | -66.93577 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0e99386-7d64-34c4-88fc-1e4ec3767f82 | -9.5482 | -64.81752 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0c8d15f-0d0d-311a-af0c-bd0cd75a4580 | -9.52571 | -67.41849 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57bbf701-fee9-3f49-b704-eecb516dfc2b | -8.33167 | -72.61233 | 2026-10-07 06:01:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36f499b8-4cff-3c41-b739-3181a04c014b | -7.56759 | -69.97726 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5615d02a-f27c-3f16-b255-ede4a7f412a2 | -8.48364 | -70.28184 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cfd8325-02f1-341d-a16d-e65b1d6ad819 | -8.89863 | -68.8952 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7daa719f-8049-3798-8363-ba962c266d4c | -9.16263 | -67.84892 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bede816-195b-394a-b07e-0758fb5e0048 | -9.07462 | -65.49038 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6e0783a-5c0a-33e8-a53d-6754aa0adc1b | -7.82357 | -73.09518 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17f0e25d-e785-3a4a-90f3-7d9debfbeb08 | -9.11622 | -67.82716 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45a02ec5-b118-39e3-8462-8053ed412d1d | -10.15428 | -68.57209 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bc6a527-9b60-34f5-ae0a-787807a095ac | -8.59926 | -67.04556 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92d4ea69-d93e-30e2-a3bc-cf483e47dad5 | -9.6727 | -66.81484 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86e83ff3-048c-318d-becb-269922b5255e | -9.09749 | -67.67889 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15f1fcda-fc2e-3847-a2be-37cccdff9810 | -7.67397 | -70.07784 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5017f2-0c8d-34c6-8de4-1a859136b0cc | -10.24762 | -68.30131 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f67aedd4-24e0-3fed-906b-7c467b0bb920 | -7.76664 | -69.92181 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00fd4411-56f7-3595-9756-4c14a9f0529f | -8.97575 | -67.51068 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5942acd-f27d-3445-b15e-067aca2b1009 | -8.56298 | -70.08712 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b28fe819-3e8c-3d5b-8170-43499d62a291 | -9.13779 | -65.30222 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8345cfbc-1bcf-31b6-bcd6-a49efc8ebd92 | -8.62968 | -67.05411 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 79291b7e-f20e-366d-8008-26db3ddaf37a | -9.44757 | -68.40357 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5ed023a-b0aa-3f62-93a6-b4bfaa25409d | -9.33519 | -65.45861 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9011b084-8a85-3fa8-96fa-9aa8818d41f7 | -7.95605 | -72.61256 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe94935b-4ad6-376b-98ea-decb9ec647f9 | -8.73811 | -69.41521 | 2026-10-07 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b35f785c-b233-3145-8fed-e9dff4bc145c | -9.1077 | -67.72533 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1634ffd-461c-3d98-ba2c-722748f5ba72 | -8.97378 | -65.44014 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ae425e-c969-3002-ba25-55df17c23b32 | -9.60671 | -67.4844 | 2026-10-07 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff528e33-187b-3e21-9240-e8bc5f2a3a45 | -9.11566 | -67.83079 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa04cf00-c1c3-35e0-a99f-065abb38335c | -9.88459 | -67.29414 | 2026-10-07 06:01:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04ea96b3-3eb0-3215-8c9d-389d9097050b | -7.7116 | -73.04445 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46b92960-47fa-3136-aef1-a48435c3057f | -9.11511 | -67.85665 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a1c9e75-a62b-3e50-80e7-87bfdb83cfc4 | -9.08767 | -65.46258 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 644f012c-ce42-36f4-8bc5-511adec873a1 | -8.56713 | -67.00181 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6985217-a82a-3fbb-9cf7-076b41a0b47f | -11.01659 | -68.5687 | 2026-10-07 06:03:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d90f0d6-976b-38ea-8104-8a16dc827814 | -10.95075 | -68.47018 | 2026-10-07 06:03:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a27f129-5215-332d-81a2-517f3d499016 | -10.7344 | -69.44368 | 2026-10-07 06:03:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34294a8b-a808-336d-bc74-7d014eddaf12 | -8.33583 | -70.80294 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 453063ec-5574-3516-9cd0-84405992352d | -7.95186 | -71.33792 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ff749f9-6d70-3988-a18d-6b77d8606f1d | -7.88256 | -72.34922 | 2026-10-07 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 51fc69d0-8357-3bc3-91be-68d73c07299e | -7.44536 | -73.20118 | 2026-10-07 06:46:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61835b3c-a900-365c-a652-5386db69f2c3 | -7.95687 | -71.3377 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ad44c3d-ce1c-3289-953f-3e21ceb35b82 | -8.25313 | -72.78014 | 2026-10-07 06:46:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74a9e104-6b51-34f7-96fb-e339c1917f9a | -8.24609 | -70.8359 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c9b33d0-cd84-3c87-b566-60b22d38aff8 | -7.81767 | -72.71239 | 2026-10-07 06:46:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 543b25ca-a42d-3a74-9d5d-a2fa03108ce4 | -7.02854 | -71.74997 | 2026-10-07 06:46:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6f4b756-3d55-34a1-ae20-579e0f69ff4b | -8.33391 | -72.60924 | 2026-10-07 06:46:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4219be1e-77fd-3068-a638-3d6623c4e612 | -8.3385 | -70.79971 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6dee2a55-ce6a-3f47-a528-db5d62317f50 | -7.88748 | -72.3535 | 2026-10-07 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3e2fc99e-e907-3e87-9780-f9cfd92aeb39 | -7.44495 | -73.20415 | 2026-10-07 06:46:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88c37747-b806-3583-bf7d-19d7d28957ad | -7.95238 | -71.33385 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7477e24-6de9-3213-9c0a-9ce9562f6be3 | -8.87382 | -69.1739 | 2026-10-07 06:46:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4474a63-16eb-33ab-9b68-693e84c4fb3f | -8.33643 | -70.79836 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0d4004d0-f5a3-32c4-8eed-3d2d624c47c7 | -7.2693 | -72.99611 | 2026-10-07 06:46:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 549b05e0-1786-3af0-9879-95a0818db918 | -7.88162 | -72.35619 | 2026-10-07 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c5d41677-8eaf-3732-83b6-1f02750acbcd | -7.4403 | -73.20043 | 2026-10-07 06:46:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99262258-1f66-35de-a37d-2fadb4f37d7f | -7.02905 | -71.74626 | 2026-10-07 06:46:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba7d3b6c-f95e-3791-8883-6db6345c9c21 | -8.33248 | -70.79894 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7479d9c3-54b7-3877-be75-e35741cdeae3 | -7.9511 | -71.33684 | 2026-10-07 06:46:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d63aced-23ff-3dbd-b9ac-d7273137442b | -7.88209 | -72.35271 | 2026-10-07 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5961db33-7966-331e-ab80-30a2acf2835e | -8.86714 | -69.1729 | 2026-10-07 06:46:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2d6510e-79db-3880-b59b-e569991d6136 | -8.33347 | -72.61263 | 2026-10-07 06:46:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a62a2700-7bb4-35a8-8d1b-0bfd329ba31b | -7.85632 | -72.46352 | 2026-10-07 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 146f4858-99e6-3ef3-8340-787062860331 | -7.88702 | -72.35694 | 2026-10-07 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.6 |


[Clique aqui para ver as próximas entradas](README123.md)
