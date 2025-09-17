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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0c70db5-fe91-36fe-a904-79449fa0f9b4 | -15.81938 | -59.47082 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6deabfe0-80f2-3e70-90ba-23575fb38a26 | -15.82187 | -59.47945 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4510faa7-a54c-3c9b-9319-63488378f246 | -7.40125 | -50.00729 | 2025-09-17 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4b50fd4-fbaa-3686-8446-83b7c7335c83 | -12.38498 | -51.41 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e8e41b5-7a16-3c84-8734-1e6042c79c47 | -11.70024 | -59.31594 | 2025-09-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf3beaae-670e-3078-a894-acc8e465f423 | -15.82791 | -59.48929 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f83fe23-52fa-37d1-a9a7-6ec2b0d01423 | -15.80247 | -59.45364 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ffc882-9a5d-335c-96bb-094cc4fa3e28 | -10.16941 | -68.42888 | 2025-09-17 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba4c6ac1-2815-3625-836d-ea07c568801c | -11.69674 | -59.31538 | 2025-09-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff6fcaa5-2537-3563-9590-6730a1f07afe | -7.404 | -50.00888 | 2025-09-17 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1a16f5c-41e7-3be4-9661-89828fcba094 | -15.83093 | -59.49422 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebe9290d-d585-317e-b85d-53436c7d74cd | -15.8243 | -59.48865 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ac547b7-b89a-3a05-9303-cb64676b7f43 | -11.70083 | -59.31196 | 2025-09-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 276321c0-bb9a-3d6a-ab2d-3e3956bcbb0e | -10.05615 | -68.45419 | 2025-09-17 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 496430f9-c952-336c-ba0b-6d3b5e358a63 | -10.05788 | -68.39204 | 2025-09-17 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26e78699-0d1e-3e86-a9a4-2f3b221776b0 | -13.15289 | -51.61168 | 2025-09-17 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13dce9ee-4380-3784-a278-f02607eb7461 | -10.05244 | -68.44871 | 2025-09-17 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 230708e8-bb1d-3741-8fb5-8a6f0ff60c4a | -15.8394 | -59.48654 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb4b8e15-b7bf-35f3-bfa5-65c72102ae23 | -8.54252 | -48.9724 | 2025-09-17 05:25:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dcfecad7-ddae-3564-924f-5da657a75bc6 | -13.15281 | -51.61212 | 2025-09-17 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37127c19-1603-3575-a813-b8b1637302f4 | -12.39611 | -51.41599 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1fa9be50-1e3a-39a9-8da6-796cae2f4663 | -12.3903 | -51.41508 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ab41435-bf18-31c8-8038-219fe7f2a49e | -12.40737 | -63.88949 | 2025-09-17 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13bcd4c5-d6af-3003-a421-05722417440d | -12.38448 | -51.41425 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f33e0186-6a55-3032-8dc1-e7312adf71bc | -10.17393 | -68.42971 | 2025-09-17 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce7156b1-3f7f-3cff-8b80-3c5e20c9a851 | -15.82731 | -59.49363 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63073e75-5eba-3c97-b935-716e45e470b4 | -12.59395 | -62.95926 | 2025-09-17 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a4f0bfb-f767-3d1c-b6ad-bb967e4e1c7b | -12.39081 | -51.41079 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 88601bdd-4747-3c6d-8e37-f71f16cbdefb | -10.0587 | -68.38742 | 2025-09-17 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5378de7f-6b95-38b7-babd-a45d6621cacd | -15.82549 | -59.48003 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9fbf044c-5554-3c5c-88a1-05d090b0ff95 | -12.38398 | -51.41852 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8cd250b-e4de-3bfc-9985-26757c693a81 | -15.82851 | -59.48496 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b0eff89c-51bb-3bc2-bdff-32c05985096a | -15.83031 | -59.49867 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b834dabb-61ec-3fe3-ba23-8550319eabfc | -12.73057 | -48.02708 | 2025-09-17 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d68de821-7740-365a-9d17-29276ca69d07 | -13.14702 | -51.61127 | 2025-09-17 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3df4d46-f55f-368c-b2be-6c8fbe8fc654 | -12.72816 | -48.02243 | 2025-09-17 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| be1cadaf-9942-36d0-b4d9-dfd14793738c | -11.79506 | -62.73945 | 2025-09-17 05:25:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a2ac107d-5310-3876-b38f-877c984e2b31 | -7.88993 | -48.16626 | 2025-09-17 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78e2a1b4-43df-346f-a4ab-e0baed5b9b9b | -7.87722 | -48.15834 | 2025-09-17 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32b0765f-c352-3c8c-a6bf-643916c1c4bb | -12.40193 | -51.41684 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbc0611e-be89-3e6d-8420-2d8fdad40a41 | -7.6128 | -47.4662 | 2025-09-17 05:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d42479b-ab6b-33a3-9de4-4195ef2672db | -11.84335 | -63.2253 | 2025-09-17 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63f889ce-1510-3478-8090-f1604f2a25bf | -15.8388 | -59.49084 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f51a725-0a15-3ae0-a4e9-94ce03bef9a2 | -7.40457 | -50.00446 | 2025-09-17 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1eab0a41-9c0f-3a4c-bee5-c1823f676fd0 | -15.83576 | -59.48605 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d1e44f-61e3-3965-9a45-06ae6519913d | -15.82912 | -59.48061 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8c4920d6-4f8c-36a5-8a83-164dd686af0c | -15.823 | -59.47139 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04d58d64-c61f-3df3-acaf-1f5e9e18d780 | -5.57327 | -55.83598 | 2025-09-17 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e19ff45a-53b9-37f4-a768-d4ba3b0d8896 | -7.88916 | -48.17233 | 2025-09-17 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a17d793d-950b-3dba-8c92-bb40416854c6 | -12.14697 | -58.28635 | 2025-09-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7f6272e-40c2-3b76-b568-5ace03a1b5c1 | -12.37964 | -51.40508 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe01b42c-02ab-3583-99ca-c561365a00cf | -15.83275 | -59.48109 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45ac3300-5532-381c-a0a4-390adb880eb7 | -10.60819 | -69.259 | 2025-09-17 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f150c825-30ae-3e86-afb0-ab0261699336 | -15.8382 | -59.49509 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d2d87c7-9cfc-3503-92dd-cf5715bb22cf | -15.8031 | -59.44926 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d9c8051-b84f-3de3-92f3-98d7411caa15 | -12.39131 | -51.40651 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b143c890-4a71-3936-a651-f0d095a16aff | -13.98903 | -51.68241 | 2025-09-17 05:25:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7438926-00da-3039-bfbb-a0b0702fda38 | -13.9887 | -51.67915 | 2025-09-17 05:25:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5201004-ae74-37b8-80f0-2a2302683ec6 | -12.72894 | -48.01519 | 2025-09-17 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4a8be4da-64c8-30be-9caf-8ae1af5fcde7 | -11.69294 | -58.42862 | 2025-09-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69ddef8e-4055-37c8-a9e2-d905696cf9fd | -12.7313 | -48.01995 | 2025-09-17 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eca7518c-ffa7-3bf9-8657-70871087939b | -15.8267 | -59.49802 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 348b0719-c09e-3f5c-a3a4-f70c84ef5ceb | -15.8249 | -59.48434 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8961365d-7dd7-3f5f-b4e9-2272775817d2 | -7.40721 | -50.00819 | 2025-09-17 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 904f403a-759c-39cb-b246-cc968e6530e9 | -18.02728 | -50.94987 | 2025-09-17 05:25:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 96b0183d-f9ac-32d1-a2ed-61716123378f | -12.59727 | -62.95982 | 2025-09-17 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c604bb60-0d8c-3138-a4e2-6659168f1d22 | -7.60497 | -47.47172 | 2025-09-17 05:25:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 418df343-9732-3066-8909-a6ac06470636 | -14.60276 | -49.36754 | 2025-09-17 05:25:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c29ae4ca-bc9b-3ea7-9523-94bef89b7394 | -11.69358 | -58.42424 | 2025-09-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb57fc65-5f22-3eba-b571-5fc68b183401 | -12.39662 | -51.41163 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 222e24d7-3b14-3bcb-8d6a-624bbd32acb0 | -7.88395 | -48.15929 | 2025-09-17 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aecd1a67-136d-3ce3-baf9-b56c18fa2bad | -12.41651 | -61.11365 | 2025-09-17 05:25:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79bb7c71-5794-3068-94a7-02e150a60778 | -10.05161 | -68.45336 | 2025-09-17 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed4bca9d-7f7a-37ee-a280-e55fed663bd9 | -21.5669 | -50.12165 | 2025-09-17 05:27:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a19d3d84-98d4-324b-bd33-38afb3d7d22b | -22.35256 | -53.94106 | 2025-09-17 05:27:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b3b65c29-4184-3249-aa53-c6d7984c5b20 | -21.28339 | -50.39003 | 2025-09-17 05:27:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 23d72795-aba3-37bc-96d3-df81665a9e7f | -21.28917 | -50.3898 | 2025-09-17 05:27:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cce132ba-436f-3f21-a6d3-4d1eeca2b7fb | -21.55996 | -50.12086 | 2025-09-17 05:27:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| faff3368-7a3b-3b94-8f2d-d95aac7389ee | -21.60784 | -50.33059 | 2025-09-17 05:27:00 | NOAA-21 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e73b991c-2016-348d-9762-78a856c98eb7 | -21.56047 | -50.11372 | 2025-09-17 05:27:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4b13fb7a-37f5-3b11-8b48-a13bbb4c2974 | -22.35669 | -53.94262 | 2025-09-17 05:27:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cb5b2db2-3299-3aa2-99f4-e8ae9d7e7d4e | -23.58433 | -54.98544 | 2025-09-17 05:27:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 508e0cc9-e42f-31cb-bdcb-4440003d628f | -23.81114 | -50.97917 | 2025-09-17 05:27:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 91fd3ed5-7f2d-39d7-86e6-7d72a832a8fe | -8.84209 | -62.93015 | 2025-09-17 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c933bfbb-f047-39b8-a188-923a248e247a | -12.59931 | -62.96036 | 2025-09-17 05:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 540b2657-b15a-3ee8-a42e-d3437e80e233 | -10.06113 | -68.39014 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de28a127-17c7-3781-9c66-5a963f9308c4 | -8.23289 | -71.03109 | 2025-09-17 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d035a48-2c9c-3606-9c6c-fd5ebb268ac4 | -12.59468 | -62.96349 | 2025-09-17 05:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 261e4889-dc97-39e9-94d1-ad9606ca0055 | -7.53602 | -63.3853 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d200d1a4-1bae-3094-8bb0-bbfb6a5dfc67 | -9.62351 | -68.65458 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b763d0-0072-3d16-8ae5-e7705e48b321 | -8.72241 | -62.4424 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85e2d7c1-09b2-3465-b4fa-97ca9a722204 | -10.05779 | -68.3896 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97286ede-e46b-37e5-8273-fbc7ebae1633 | -10.0676 | -68.47841 | 2025-09-17 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b27ebca-80f9-3122-8ca3-17d8575436fd | -6.91939 | -63.02996 | 2025-09-17 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65e07c08-3d5e-3a18-a715-0abc6a1e031c | -7.56612 | -67.38489 | 2025-09-17 05:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c43249-b34b-3ee8-bc91-53c2b1b0e603 | -8.846 | -62.93072 | 2025-09-17 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edad1b3f-8442-3eb5-8144-4c6ec3ee9c5d | -8.65155 | -62.67676 | 2025-09-17 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e6d2358-9b68-3990-b722-242ec2958dbc | -8.114 | -63.68936 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d4638b-07af-3155-b036-705bea3f4195 | -10.58311 | -68.40551 | 2025-09-17 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e78397-3cbf-38cb-9ecb-0710d5e06748 | -7.53983 | -63.38353 | 2025-09-17 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README54.md)
