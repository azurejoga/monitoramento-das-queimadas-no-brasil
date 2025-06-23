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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6120fb21-eb9f-3595-9034-1a4e6cae8a19 | -11.18162 | -54.4075 | 2025-06-23 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb2bb5b3-a13d-3c28-8710-fdddb349b8ce | -12.47309 | -54.4285 | 2025-06-23 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b3a41f31-831a-349f-88cc-9db6d53a58ca | -12.25203 | -46.684 | 2025-06-23 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1f22a41-4178-3181-bc63-a7f952d454f4 | -13.27281 | -46.81848 | 2025-06-23 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e544a51e-78d1-303c-a0a2-9b8436cdf4f8 | -13.24292 | -49.83946 | 2025-06-23 04:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bb30c3ef-02b1-385a-b5ff-92219479fc9f | -13.95715 | -48.00613 | 2025-06-23 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e32dfca-48ac-35d9-9b8e-4a15a34151b6 | -12.24813 | -46.68701 | 2025-06-23 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35a84cc3-00d0-31c4-ae1a-e8df33bc6eb8 | -17.39604 | -42.63644 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5c6599dd-4072-32c3-8c12-f5150ee60fbb | -17.39744 | -42.62624 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| baa434ed-f8a8-339d-95a2-e2ded363e042 | -15.5691 | -47.85387 | 2025-06-23 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b933165-2795-3e3e-9183-9ddc5747f0e5 | -17.39584 | -42.63354 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8ba5943c-e2be-3438-9483-8fb0f7d89774 | -13.08235 | -54.85177 | 2025-06-23 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d56bab25-293d-38ba-88dd-2028af4dc971 | -16.68197 | -43.88416 | 2025-06-23 04:23:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39484157-40f0-370d-ad3e-c324a2212c7f | -17.39259 | -42.62783 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 79624e0b-880f-3fd8-ae20-7e275c48d719 | -17.39214 | -42.63585 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6654cfc6-da36-3e67-856b-c054976e9ed2 | -17.67108 | -46.75935 | 2025-06-23 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ea407a2-a16e-36e0-821c-2434080cb275 | -17.50094 | -43.95056 | 2025-06-23 04:23:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62260bd1-b961-3386-b4fa-a25f9386cec3 | -13.08178 | -54.85476 | 2025-06-23 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 185d80a9-177a-3033-bcc6-0ba6ce592e1f | -17.39353 | -42.62564 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cdabae34-e62f-33ea-a889-7f2e62a8d5a2 | -17.3965 | -42.62843 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 023ad31a-910c-3704-8c2e-6065edd1bf16 | -15.18485 | -43.75132 | 2025-06-23 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8f042212-8ec8-3c6d-9b4e-6aeb0e0481b4 | -17.38893 | -42.63015 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ef8b9593-56a2-326a-a9b3-8ca689d49c9e | -13.08349 | -54.8458 | 2025-06-23 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32d8b9eb-bccf-3d91-8205-38ed8608a473 | -16.98577 | -50.24669 | 2025-06-23 04:23:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 747ae4d6-ff76-3367-97e8-6a9988964a44 | -13.08406 | -54.84281 | 2025-06-23 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc67252-c832-3e9e-9089-802b18231098 | -17.39283 | -42.63075 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 705df5ff-4b48-341c-8da2-d275f6863761 | -16.98306 | -50.249 | 2025-06-23 04:23:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a576bb85-4743-3c54-96e0-b7654cd239ca | -13.08292 | -54.84879 | 2025-06-23 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| beb584a0-1861-388b-9655-119e74195d3b | -17.61816 | -44.48685 | 2025-06-23 04:23:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed7b7f43-a818-3b13-9b08-45f3b77c3c01 | -17.39193 | -42.63293 | 2025-06-23 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 2cad00c1-e5d9-3593-9a5b-9ba2f038c4cf | -19.2362 | -46.46202 | 2025-06-23 04:25:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59f29782-e559-3351-8b2a-df92fc2621e5 | -19.01226 | -46.39524 | 2025-06-23 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 672ff6b2-cf79-337b-9c3a-957827822185 | -21.48886 | -47.55703 | 2025-06-23 04:25:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 74e60345-d846-324b-b09f-d6d2df30d8e3 | -22.25701 | -50.04211 | 2025-06-23 04:25:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c1074baa-6da4-39d2-af62-ca07b294938f | -19.51932 | -45.31208 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa7b3813-e502-391a-b01f-3c9916ec4c6d | -23.63098 | -46.42797 | 2025-06-23 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c3a691e-6578-3554-a93b-8db3769d1d2a | -20.7063 | -50.06863 | 2025-06-23 04:25:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e739f8c0-9025-30dd-9247-85f238d0c6a3 | -20.72443 | -49.43586 | 2025-06-23 04:25:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82edfd0d-a18a-3f50-a82a-431d51ea3418 | -19.50825 | -45.31439 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| d16cdf39-aa82-3d48-8189-c18f8316fda3 | -19.83393 | -40.11499 | 2025-06-23 04:25:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ccd1dbe1-0197-33f4-a600-096cb1110694 | -19.45494 | -45.30708 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 689565ad-840c-30a5-8a71-2c11028751ac | -21.19354 | -44.93786 | 2025-06-23 04:25:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 320a691d-02b8-3084-bb39-038b730b09cb | -21.66547 | -41.94882 | 2025-06-23 04:25:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6390972f-fd01-3c38-8b11-b1bb9bbbbcf6 | -19.71805 | -40.35425 | 2025-06-23 04:25:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a9c4bd2d-f7cd-3d13-9de0-d16684a8eb04 | -20.70546 | -50.0675 | 2025-06-23 04:25:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 260b3a8e-3bfb-38f7-933a-0acfea0ea480 | -19.43936 | -44.34091 | 2025-06-23 04:25:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4238f128-6001-39a7-8811-232dc123e53e | -19.51874 | -45.31615 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 75d6c33a-fb27-318b-8e28-91d97032a51a | -23.40403 | -46.5563 | 2025-06-23 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| beee1a49-b0a8-39fc-a601-9569262006f1 | -20.70696 | -50.06467 | 2025-06-23 04:25:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ec180d3f-353f-31c3-9cea-380802957afc | -23.08633 | -47.44003 | 2025-06-23 04:25:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ae37c137-6933-3bca-bb4c-6903bf9a554b | -23.40749 | -46.55683 | 2025-06-23 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd69bc7f-8f83-3e4a-abf9-8f79451e013a | -21.3948 | -45.50898 | 2025-06-23 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dd64ce72-86ff-3cd9-bdf7-0c4cb7a75dab | -21.8587 | -42.89461 | 2025-06-23 04:25:00 | NPP-375D | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1af8f161-4fb5-36c6-94b7-3ca690c9dddc | -20.23463 | -46.16638 | 2025-06-23 04:25:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ed0e775-b69a-30ae-80a1-feed49504fc2 | -19.51582 | -45.3115 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f673a6c0-2891-3603-a529-ec974a1b7442 | -20.31317 | -45.58445 | 2025-06-23 04:25:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ee50cbe-0378-3862-9387-f3d8270f5c72 | -20.72507 | -49.43204 | 2025-06-23 04:25:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c64e19ac-dc87-39ea-bfac-635028203423 | -20.70889 | -50.06817 | 2025-06-23 04:25:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e2e3a779-9ee0-3a58-a9c2-425849d7afc0 | -19.51232 | -45.31092 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef736793-d99e-3671-8c22-0ae17b766670 | -20.23405 | -46.17025 | 2025-06-23 04:25:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4c67c1c-fb41-3d5f-8223-2226aa297621 | -22.53922 | -48.81386 | 2025-06-23 04:25:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64b38fa5-78a2-35ba-9e1e-5b565cca4823 | -23.59467 | -47.4383 | 2025-06-23 04:25:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 91319170-85ab-3d29-9ed5-7a030561ddc0 | -22.25362 | -50.04143 | 2025-06-23 04:25:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 467a25ee-635a-3190-b0db-18645b10b8a0 | -20.41526 | -43.55247 | 2025-06-23 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4584e3b3-960c-3889-92d6-61fcb7f86b28 | -22.25767 | -50.0382 | 2025-06-23 04:25:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32024de5-a7fe-3ade-ac29-faf5100b3fa2 | -19.51174 | -45.31499 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| e37152df-57e2-3316-b59e-93facd8b7520 | -20.30969 | -45.58386 | 2025-06-23 04:25:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 186c4027-6fe1-3666-a200-d505cc5ebdc4 | -23.04785 | -49.89439 | 2025-06-23 04:25:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 24d0b912-5d32-3c60-b74b-6910a99b2af8 | -25.19186 | -49.32811 | 2025-06-23 04:25:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0a6f98a5-d4b1-3b36-87bc-d529843acd9f | -22.25428 | -50.03751 | 2025-06-23 04:25:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 45fc8f7e-d3bb-3611-b79a-9f5025ad05ef | -19.48849 | -44.14561 | 2025-06-23 04:25:00 | NPP-375D | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41b2c570-a83b-36e7-88aa-a62c75209fef | -21.39539 | -45.50483 | 2025-06-23 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a27c3e52-201b-30f0-9c0d-be9fde76f377 | -19.64037 | -45.19128 | 2025-06-23 04:25:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 998c4dc0-12a3-372e-9e98-2903d4e4c985 | -19.51524 | -45.31557 | 2025-06-23 04:25:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 93b325ac-c73b-37a5-95d5-8c31f21e6cf6 | -21.39186 | -45.50424 | 2025-06-23 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cec05084-9e7f-3f98-a3e5-8c7a2aa027f3 | -19.23677 | -46.45823 | 2025-06-23 04:25:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f5ef45e-d8cf-3cc5-b288-67f339c4b8e3 | -21.23628 | -48.63147 | 2025-06-23 04:25:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d70bbbd-4100-3b4f-b2dc-d6aff7a73b47 | -19.07129 | -46.73769 | 2025-06-23 04:25:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82e29ff4-442a-3ea9-9b11-dd04692564e2 | -20.41912 | -43.55297 | 2025-06-23 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a1c64652-87e8-379b-b416-0d5ee0fc926e | -8.0703 | -43.0981 | 2025-06-23 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| 8eb07cb2-e2e1-30a6-8c83-ad5505560e19 | -19.5181 | -45.3098 | 2025-06-23 04:30:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 58a3f1fe-2c2c-3c95-a123-a2d2daa286dd | -8.07 | -43.1216 | 2025-06-23 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 446643f0-234f-3b2e-88ef-1b272aec6953 | 2.75332 | -60.36865 | 2025-06-23 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6cc722e-2ddf-3491-9d8a-a580e3a6262b | 0.6983 | -51.44092 | 2025-06-23 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10a05f2d-108e-3a42-920b-7eadac2c16c8 | 2.75226 | -60.36963 | 2025-06-23 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 954c6002-6417-305a-9ad2-da1961c06098 | -8.1142 | -43.14279 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe72af32-cb5c-3fe5-ac38-6f252d38b0be | -8.10873 | -43.14996 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bca94bb7-e42d-3b3c-b396-3888bb75af34 | -5.41734 | -45.11351 | 2025-06-23 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8454c42-48bc-39d7-b897-d624d86b89ee | -8.06328 | -43.10782 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5be25dc0-0866-3945-8dfd-87debf9c7824 | -5.57239 | -45.20581 | 2025-06-23 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f979985b-e918-3190-b6fb-3ac5d5e67614 | -8.06247 | -43.1137 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 922207c3-9c0f-3e18-ae26-ff10685c2619 | -7.44733 | -45.55038 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e77e0e1b-269b-3853-8c25-4ea19d9f7c0c | -8.11417 | -43.14774 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 14d1c541-1f8e-3949-b585-2f5e5bbfe937 | -8.37441 | -47.43914 | 2025-06-23 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 901bb906-a161-3ce4-ad93-e62c0cd1af0e | -8.11381 | -43.14571 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59818c29-3be9-37f7-baf5-eafd14caff26 | -8.38579 | -47.4407 | 2025-06-23 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16619e49-4882-35d0-9b5a-d141fea1098a | -9.14936 | -48.975 | 2025-06-23 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 637bdba9-b412-3e3e-add9-d07814baff63 | -7.94726 | -46.03985 | 2025-06-23 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 765a0cc6-d03e-38be-810a-a49cc5c02d79 | -7.3071 | -43.21847 | 2025-06-23 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31553a25-5271-3500-8c84-6d5aee38b885 | -8.06368 | -43.10489 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
