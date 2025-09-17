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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dec89800-f751-39aa-8189-454d41723a6d | -13.32287 | -48.74582 | 2025-09-17 04:34:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b39a8da8-c1c3-3b4c-a13a-78bfebfb8861 | -17.35912 | -46.65611 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae060fe3-a3e6-3d58-b42f-8395de57bfb7 | -14.70272 | -50.2471 | 2025-09-17 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4046d241-4e04-37b5-b1e2-d29dc226b84b | -13.62854 | -45.36978 | 2025-09-17 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1e5d64ba-f50f-3147-b889-4f92b5e5f5f0 | -14.78279 | -51.71243 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c40b8889-ced3-37b8-96c4-8bb20df307d8 | -12.71701 | -47.99021 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22b31da6-b6a9-30ce-8115-924174f0cd87 | -13.08942 | -50.09594 | 2025-09-17 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bcdbb95-cdfc-3a68-b31a-bd9f6032ebb9 | -14.61016 | -46.379 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ba06f9d-fb13-3c59-8d4c-38464efd3a11 | -15.39411 | -46.13957 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 379cf200-da08-331a-a177-49ff41a095d7 | -12.60272 | -47.98349 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 168150ef-57e8-3589-885e-ccc005a08973 | -15.55882 | -47.16449 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a12922c-4041-3f90-893d-41e308d39250 | -12.86335 | -47.13752 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6259f422-bd82-3a90-b5a4-a223bcd133cf | -12.75124 | -47.95836 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70696f60-65b3-30af-b72d-93241965572b | -14.90514 | -51.69407 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| d5ac46de-eb8d-3732-afb6-a6e8de777642 | -12.94514 | -47.96288 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c53e5439-ac13-3fb3-b99a-a34a355d3372 | -14.90577 | -51.69026 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| f9ba6472-5df0-370b-951d-74f531a7f010 | -16.8826 | -45.77758 | 2025-09-17 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7fe1868-bdb6-388e-a09c-4d6eb0e509cb | -12.86488 | -47.13418 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 132aaf90-111e-3f3c-ac31-01a70809d855 | -14.60352 | -46.39984 | 2025-09-17 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fb2e0be-6cff-385b-acb8-22c9bf2adf4d | -12.72654 | -48.01778 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ccc6029b-b064-3a8d-ac8b-e7d7c856b87d | -14.92006 | -51.68886 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fafc7e0-479f-37e9-b4db-b8e893330377 | -12.69653 | -45.81044 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92eefe33-4abb-3db4-bc2d-aa58eac20460 | -14.61075 | -46.40113 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88ca4886-e118-3fca-8872-8b49b5ef5e81 | -13.20354 | -47.32049 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4212aeb4-5fe1-3710-be6f-75c280612173 | -12.69513 | -47.95317 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6233846-eac9-3ee2-93c1-e4f95d55ccad | -12.85519 | -47.12822 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fa58b4d-2c36-337f-ab08-6810fa48dae5 | -15.98675 | -46.45155 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a1a6a078-506e-31b1-851b-205619d1660d | -12.44007 | -44.75074 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a66e83a6-457b-3242-8511-94277f641def | -13.2258 | -47.28939 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4170261f-dc3b-3e5d-b46c-731b414ce92e | -12.96864 | -47.95544 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a1887b6-fc5e-38a5-826f-3d7ea24ed6d1 | -12.3858 | -51.41761 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5846eadf-01ef-3c26-b73c-a629da1fa046 | -12.99443 | -47.94461 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01481a8a-230f-35ba-94f6-2ce1ae825f0f | -12.86512 | -47.14944 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59c55392-fe45-3234-9014-9e229c7d1096 | -18.53895 | -48.13431 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a1fdef0-e34b-3a36-a733-602dd0a8123a | -13.14112 | -49.2142 | 2025-09-17 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63af1e78-2f6f-31a2-b602-004dbb7e168a | -17.74554 | -44.43872 | 2025-09-17 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 211b12df-1eb7-3f01-8345-0ce135a43b31 | -14.55147 | -47.35867 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5bf97c0-e20e-3613-8790-291f9a7c7299 | -15.55822 | -47.16857 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f72928ca-2d43-35e1-af77-40e419894ed9 | -11.59835 | -49.81721 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e5436c6-8459-366e-a791-ddaa1215b2fa | -13.20971 | -47.27906 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14757fb7-41ca-3981-b802-2bbbc2ae6845 | -17.00268 | -45.86246 | 2025-09-17 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 086bde6c-03ad-383b-b51b-4e44fe092944 | -11.35156 | -50.85633 | 2025-09-17 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbf41515-fcc0-3473-86d4-510ff34f019b | -15.4123 | -46.15922 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f520725-bad4-3382-b185-00b52b64c7e3 | -13.21317 | -47.27954 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35b9d542-2ff3-3634-855e-c5405d10301b | -12.9692 | -47.95169 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 640752d5-da0e-33ad-b9a4-cae0563cd730 | -18.19192 | -44.54055 | 2025-09-17 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2737500-dfe1-3aaf-9849-11ae75374faa | -13.36808 | -43.77417 | 2025-09-17 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02ebbb7c-b5a0-3637-a252-b8e35fd6de10 | -14.87532 | -45.52589 | 2025-09-17 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1adbd6d0-62ad-3d32-959b-33d3aef9dffc | -14.97348 | -53.41124 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db4293b7-7579-3c80-88b0-3a4e3b8bc781 | -17.7085 | -44.75835 | 2025-09-17 04:34:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b2e6f9b-ca38-3811-aa7e-a7ed626ac120 | -14.89489 | -51.69226 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1143517b-6e0d-352a-9007-419adbdfef6f | -14.49862 | -47.37973 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cb0eaf8-cbb4-37f8-866a-fcea36ac9d60 | -16.28399 | -45.68169 | 2025-09-17 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 920145af-1af0-3817-8106-13b310d0ea04 | -18.52898 | -48.1537 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 572ddb8d-a5c1-3d95-9206-90a620a13649 | -14.84937 | -51.69276 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41864ada-2d20-351f-b9f8-1fbc3d00414f | -13.08667 | -50.09183 | 2025-09-17 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bce5567-c308-3d42-bddd-6019ae05c863 | -12.29209 | -50.1286 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c069ee29-6c21-30e6-8d25-bd5c91b34f92 | -12.72879 | -48.02557 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e379644-4214-3af5-a042-77b52ab413b0 | -14.60107 | -46.38779 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab9658db-2db4-3f71-a64d-2424b08090fb | -16.79576 | -49.11998 | 2025-09-17 04:34:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25331db6-babb-3646-abde-7ddd826b9e93 | -12.71289 | -47.74569 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25f0de97-23b0-31ac-9503-8f6d90750190 | -13.3262 | -43.10111 | 2025-09-17 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 77b95982-34b4-3d8b-aacb-de333c6b1ae4 | -12.09692 | -44.82767 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ca5049b-c8ee-33e3-a911-985ec0ef2754 | -15.40552 | -46.1535 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85f1b8c3-3c42-30e2-a31d-fcca6f348f04 | -12.69176 | -47.95265 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c395b460-23b3-3c36-bcc1-919ef5240dd9 | -12.7086 | -47.9777 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1bb4d98-827f-3c46-8418-e2253a5bfd17 | -12.27228 | -45.29549 | 2025-09-17 04:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fde5a76-a9b5-3eed-b498-3aae5321e539 | -18.55018 | -49.24344 | 2025-09-17 04:34:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 66b80ea2-22ab-385d-8c5a-346be9708ebb | -14.62284 | -46.39436 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fce3a20-a1f7-3b58-be28-5724aee1a770 | -14.60714 | -46.40047 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e75bcdde-bb18-37f7-9ae8-247f61992d28 | -14.81141 | -51.70962 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d23111c-5085-3fd5-a12a-f84018731661 | -12.39116 | -51.40665 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38e4b574-ac66-3d25-9f40-dc0c70547572 | -12.70103 | -47.73251 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdd0e662-9084-3bde-881c-a3e2175393da | -17.31775 | -46.81609 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d26b22d-b9c6-30db-942b-d14b3ca3969c | -14.87348 | -50.24311 | 2025-09-17 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bafc58ad-4a9b-3e01-bfd2-05dd99e79868 | -14.82996 | -48.11401 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72122bde-e696-3d59-b158-c6f9d4d03056 | -17.11478 | -43.59754 | 2025-09-17 04:34:00 | NOAA-20 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aec26eb6-b6f1-37bf-bd0a-8f6e9927248f | -12.96194 | -47.95407 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 490911a8-15be-3240-b3d0-475ce531e265 | -14.61437 | -46.4018 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e52a17a1-0ae8-3fe3-be87-1f72f44a1146 | -13.9452 | -43.98896 | 2025-09-17 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7e8c300-bbd2-3cff-9424-0c66d977891b | -15.55762 | -47.17266 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66cf13c6-5967-3978-92a3-33f5c8af51d0 | -14.30688 | -52.96413 | 2025-09-17 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69259ccd-1f7e-3c85-96ee-6d3160d0770c | -12.59936 | -47.98295 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10c2da67-d103-3ee6-8183-92fbc00474a6 | -14.91386 | -51.68385 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32765910-7d5c-3892-9db5-3ab2ccdb8df0 | -12.31051 | -50.12064 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 753940c9-c2df-388f-b470-6e9f2f980c26 | -12.09187 | -47.54865 | 2025-09-17 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffaba805-b5a9-3c8c-9764-78ffe5a9591b | -14.14121 | -46.98532 | 2025-09-17 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b84e547e-48f7-38f8-9974-a413c6e1c8eb | -16.84953 | -44.07604 | 2025-09-17 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b468be7b-35e1-3f8b-a9b3-02e6732357e0 | -13.17723 | -44.48087 | 2025-09-17 04:34:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09666849-68d4-38ac-a826-d3a09d563872 | -14.14062 | -46.98935 | 2025-09-17 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 026abcd8-6dc3-3719-86bc-2b9c78454019 | -15.93025 | -42.64144 | 2025-09-17 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 468e5fd0-da51-35d8-83af-6c3babc6181a | -10.81254 | -50.65672 | 2025-09-17 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33ebfed4-93de-3b31-bf32-ba83f7122237 | -12.96472 | -47.95856 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e47d7d2e-54a1-34c2-ba0a-bf88544fba78 | -16.42684 | -45.66657 | 2025-09-17 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b93d09e0-15b2-3424-a758-bf6d201236fe | -12.94908 | -47.95972 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3628972a-a0bf-3e6f-8c8f-ca285af58a10 | -12.68805 | -47.72667 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b1a7add-c6d2-3036-89d8-687e9e3e70dc | -14.78247 | -60.20726 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 550c4dfb-c9c2-33a6-9e0a-a5fa83ffc1aa | -14.89894 | -51.68906 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c99bd5e-624b-3855-a856-22756ef996f4 | -18.24797 | -43.32497 | 2025-09-17 04:34:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25f32f8c-eee0-3919-8100-aeff5ae11de4 | -13.03089 | -47.95439 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README47.md)
