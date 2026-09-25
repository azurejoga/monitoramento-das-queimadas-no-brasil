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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9239351-6033-3b62-88b7-c36d08cfc315 | -13.78282 | -54.04561 | 2026-09-25 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c7df3e8b-bfad-34be-b731-458390fcce43 | -12.20833 | -50.80098 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 80dbc5a5-9e66-36c8-92e9-ee8acbf226dd | -9.02857 | -60.52647 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22bff3d8-642f-341f-812e-ef387e4fc899 | -12.19431 | -50.80523 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69277954-aaed-3d16-aea5-6be7fd3ea047 | -9.2963 | -60.53293 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ffa6118-0002-3e1f-a993-ec5b617cd684 | -9.13856 | -57.55429 | 2026-09-25 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1655a6d1-fb90-38e9-87c1-819271f4e3bf | -10.42362 | -53.78419 | 2026-09-25 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74af63f9-e5a7-3351-ab53-ad6483efcf6b | -12.22497 | -50.77274 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 15313550-0b89-31f1-a8fc-b35ec4dcf89c | -10.62189 | -53.98967 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80043d69-ebd2-3c50-84d6-0f7596cd6136 | -11.28738 | -51.30143 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5e8d4a94-d346-34f5-bb56-89be1bcf262f | -9.15246 | -59.48531 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a837e15-45e1-36bb-b028-0b48b35998ab | -10.56393 | -59.49078 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81592dcf-3ee2-33ee-86eb-9f048fd21623 | -9.15432 | -59.4724 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bafe14ff-f2af-3955-974e-9a663025a9d6 | -9.02452 | -60.55355 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22abded3-2c6e-3870-8d3c-8a7dfc1e0817 | -12.22825 | -50.74263 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 25cfe195-e294-3106-a6fe-b9f879cf4d11 | -8.26647 | -70.80655 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae5a3d48-91e0-385e-a2a7-08aa5bbbc090 | -10.41897 | -52.79438 | 2026-09-25 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f71bf9e-f64f-3909-a6bd-859c6c10742b | -11.18208 | -51.36846 | 2026-09-25 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1796face-422a-374c-a875-3c09aaa2c9ea | -9.23717 | -65.74907 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f08b261-43e3-3ea8-afd2-4b3734fb9ee5 | -10.41846 | -52.79853 | 2026-09-25 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 06f57d60-b6ee-304d-acac-f75d3fa35b6a | -10.6202 | -53.98511 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77ce08e7-9aed-3662-8aa7-8aa4d998c861 | -9.12828 | -60.32031 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a5abbd7-8e8e-3ad7-9003-ecb5eb167dd4 | -12.19061 | -50.80355 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d857dbd-787c-3664-adf1-7b25e1984d1f | -9.58682 | -60.51912 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86a877e7-8b1e-35ef-8457-ce1973ee0467 | -8.90165 | -71.34747 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdf6904e-227d-352f-a920-140e35057dfa | -9.20228 | -60.86419 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 024f0929-56df-32ef-933b-30f11523bcbe | -9.02451 | -60.52983 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edc666ae-7a53-3d70-a477-77940172b2a0 | -11.28258 | -51.30025 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 64b747de-6df1-3933-a8c9-1ff092c03125 | -9.02682 | -60.51435 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20865710-f3af-3eba-85aa-48f51b6cb496 | -10.62101 | -53.9965 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bc2f50f-3b1b-3ff6-9b1a-785351e5ce46 | -9.02161 | -60.52543 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 396ba157-7ffa-3f88-8b97-beebc1a9ecf9 | -12.21566 | -50.79586 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4a7cc255-b373-313d-bbfc-46cd1d801030 | -9.15495 | -59.46806 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3908cc7-fb34-3971-9516-66af5df74ca2 | -9.01871 | -60.52102 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d93cf4c8-3c83-32b9-b771-283c1557acef | -9.27669 | -61.38825 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72a4f914-d005-38be-8ba7-158908543d15 | -12.22957 | -50.73053 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2b4728e7-933d-3ccd-a12e-899421494243 | -12.24639 | -50.76325 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6d783168-7524-3553-9166-5d5d94efd442 | -14.99484 | -56.31241 | 2026-09-25 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4579a6d6-d7f6-3c52-b005-e5fcbef5dc1d | -12.20962 | -50.78902 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 037d1bc1-c686-3ec2-84ff-16aee1d369a1 | -12.17777 | -50.70549 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1ea50426-a9a3-3cdb-adce-1ebe8caf37b3 | -7.52376 | -70.38863 | 2026-09-25 05:31:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a714a4f2-97fc-3d3e-92ed-773207d85eec | -9.63802 | -61.82428 | 2026-09-25 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e8aa698-5b17-320b-989a-893f02dbcf98 | -12.19534 | -50.73229 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c0a95005-2ba6-3c09-85ee-4e1462311158 | -10.62514 | -53.98924 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3801d82-77b2-39c3-bc05-151fd4790117 | -9.10938 | -61.43306 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac5a0cac-e206-3e4a-8c02-9a1c2c32f174 | -12.21631 | -50.78988 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 46e4533d-25b9-3a37-988e-537da13e0d82 | -12.19934 | -50.78648 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2eb913cc-3576-3ab8-bb4a-f8a3875431ad | -9.1951 | -61.09695 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 565c81aa-b79f-3c40-a0bd-3ff9f4fcf8fe | -9.15861 | -59.46861 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfbbf775-5b7a-378d-bb6f-bf586478686d | -12.21073 | -50.71585 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4a300ca5-c6ae-352e-a425-5bb9cda8bc6f | -9.3532 | -61.16624 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5616379-bc17-3c3d-bf88-02da24ae2bd1 | -9.13908 | -57.55059 | 2026-09-25 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b43ddfc-7d25-35dd-9a5d-97adaaeb55e7 | -15.18751 | -56.058 | 2026-09-25 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 224f19a5-ae3d-3869-b38b-df8283e2ffe3 | -9.10656 | -61.42891 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2831d8d5-de4e-3200-a291-0daa9222eb0e | -10.90384 | -53.94899 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7c1ca4e-7dff-3e9a-92cc-23ac4426d231 | -10.29597 | -54.23466 | 2026-09-25 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ebcd96c-61de-3b23-9b2a-4b6a98994320 | -10.97962 | -58.95693 | 2026-09-25 05:31:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8cd6cf3-a029-3096-8223-fc4b9faf940e | -12.20828 | -50.70824 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03ea1679-f24e-37f0-bdf9-be469d09dcf3 | -10.90559 | -53.93501 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64619743-bdcf-3dc3-b264-b1f34b0c04d3 | -9.46804 | -67.07584 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6d16d16-eee2-33bf-be9e-f42de9cde071 | -12.205 | -50.6771 | 2026-09-25 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cddb3a70-aed1-3636-a441-a870d1f01a85 | -9.16317 | -67.67725 | 2026-09-25 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e795888a-6c45-3596-b308-111b213d81a3 | -12.20018 | -50.71951 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d59df5e8-2706-3d7d-b3c3-ec7a4e2d4c68 | -12.21679 | -50.72276 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1778e828-6f63-3425-92d3-1c1b0a64bda8 | -7.70647 | -71.98479 | 2026-09-25 05:31:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 632818b7-999f-393b-9948-6bff729c06c8 | -8.78975 | -66.60084 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c410878-fcbd-33a8-8382-e01dc0a2a201 | -9.02799 | -60.53035 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2127a12-abb0-37ec-9f28-c304de116022 | -12.22416 | -50.71756 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 26a379a4-7a91-3142-89a7-f4bb991a3b0a | -13.22716 | -51.55604 | 2026-09-25 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bfd4242-6e01-3dc3-88bc-9ea77fddbde2 | -10.56829 | -59.48684 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b8ec235-765e-3685-965e-fdba51402977 | -10.90515 | -53.93854 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32394f9a-5502-366a-af51-f6deb2c6b567 | -12.20336 | -50.72105 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 97c5f402-6343-3709-af6e-bb7145b57939 | -10.62057 | -53.99992 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62a28acf-d064-3dbb-bfbd-d3c75af2a87a | -9.8352 | -59.46915 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e07b0e47-5688-3fae-aa10-2b454ecf0214 | -9.1537 | -59.47671 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 33143fd4-bab0-3d36-b4a0-e35f3441fa4a | -8.22786 | -71.04718 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd0d5d03-f79a-300c-9072-d5792f50f616 | -13.22657 | -51.56151 | 2026-09-25 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f6fdc03-8554-35c7-89b8-2cd9a8b0e010 | -9.41674 | -60.4672 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e0a15e5-6a2e-3aeb-a777-de6a382f4377 | -8.66315 | -70.91761 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 476d10d8-0916-3834-a00e-b450a5f60962 | -12.23562 | -50.73744 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 63b72322-e211-3cdb-b175-739093d61c40 | -11.5647 | -61.23554 | 2026-09-25 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67d2bfaf-5770-3c1d-b50a-7e214f1603b1 | -9.41734 | -60.46327 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee225ddd-59b3-3181-86fe-ccef48e6485c | -8.78309 | -66.59514 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94efce62-36b0-3bc7-83b4-1a4f534a72d9 | -10.62389 | -53.99954 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e1661e2-bccf-393b-9dfa-b1da4fcc0aed | -9.26832 | -57.18487 | 2026-09-25 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 715b7f80-bda7-361f-86bf-6bc3a4aed1f0 | -9.21774 | -59.57441 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48a7d0e9-293d-360f-ae31-0783f63f0f62 | -10.41505 | -53.80803 | 2026-09-25 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de323961-90b7-3058-b856-12791762176a | -9.04553 | -65.40954 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b696e84d-2aa0-381c-a05c-7a314cdaeb40 | -12.25176 | -50.77612 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d99bf9e0-99fa-3674-8f04-99e71b79347e | -12.25171 | -50.71494 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b21847e7-6b2c-3ac3-ba2a-5580e0c96ae9 | -12.20942 | -50.72796 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 492786c9-815a-3463-a511-bb01e39fe063 | -9.22597 | -71.86406 | 2026-09-25 05:31:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38a3645d-e8bc-3335-9e62-f720ffda417e | -12.23628 | -50.73141 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 798e562a-74e7-3f89-93c3-be1b8408306d | -9.04363 | -65.42125 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da9ba37c-3678-3510-b2e2-790346598ac4 | -9.29814 | -60.5336 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aed8081d-9a35-39c2-badd-e24d6f5c2eae | -8.78234 | -66.59959 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad613c36-a70e-3704-bea6-5feca1af56d7 | -9.02219 | -60.52154 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a22d53a-342c-327d-a429-181cb7e15a92 | -12.23221 | -50.70628 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dda48d27-ed2f-376f-bb57-b049e56e6f0d | -11.93999 | -62.39377 | 2026-09-25 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55d85000-35fe-3044-9cf9-6777857d9b01 | -9.15066 | -59.47184 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README34.md)
