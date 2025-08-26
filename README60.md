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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 641b97bb-4497-3018-b05f-462b9c0a4f9c | -8.88885 | -62.4711 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 015b4284-6fdd-300c-95ed-15f8f7361594 | -12.41722 | -46.8082 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8af5f8e5-f9d0-3ddf-b0bb-09271b790ea2 | -9.15914 | -59.55894 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 04c524b2-b17e-3c5d-a77c-bd510f7f6d3c | -13.10806 | -49.33519 | 2025-08-26 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e841683-5868-3841-b0ab-f679eab8ef05 | -9.18146 | -59.51878 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cb55df1-5798-396d-9c6f-c5fa61bafe8e | -13.61482 | -48.15678 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4058de4-ba72-3e2e-88da-9abea496b0b6 | -14.25606 | -48.0314 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70dbdbfe-efd4-3808-9488-0ab0348c705e | -13.5242 | -46.89965 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad2be4d1-a855-3fa0-ae28-ea91f7b34a65 | -9.15977 | -60.78171 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 761ef3d7-b74b-3c3b-8305-a3089b27423a | -10.43873 | -47.17552 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d981f1a-921e-37e1-a916-956c7a2a5c73 | -6.76841 | -59.66698 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0a474251-e0a7-3ab0-98c0-a0306fbc3ed4 | -8.5461 | -62.643 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee358aa3-9bfd-341f-90d9-ce4b001fe7be | -11.54758 | -52.12179 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 556cb4c7-ff83-31ce-bb05-cfd661f51760 | -8.99761 | -65.41492 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49395a5c-0f0f-3e0b-9838-cb47254852d3 | -8.84937 | -62.45447 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 65deafde-a15d-35e4-b430-1faa13a99f52 | -9.21029 | -59.4421 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49264fd5-6856-3ee2-9070-0b2ecc74df38 | -8.10948 | -62.8819 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3f6ab67b-bc5f-3da0-9ef7-ca26f0df920d | -12.93787 | -46.32816 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eb73838-e4e5-3b7b-8aa9-ee7a1aadf0c4 | -9.17978 | -59.4512 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b05f47fe-f0a1-3c2e-963e-1a7f9799d0c1 | -11.55531 | -52.11584 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2fbbcf9-57f4-393c-84cb-321de75793c5 | -14.11806 | -53.98401 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ee17014-07e4-32c5-8cbb-d0849d92407a | -13.40967 | -46.88608 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c61f3449-41ee-3857-834f-b5b782125718 | -9.15724 | -59.54206 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ea00328b-58e3-3fb6-8328-524bc9ab95d7 | -8.71177 | -49.52603 | 2025-08-26 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cb5f2b2-568f-3739-97a9-ec77837811e4 | -13.16674 | -45.28856 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 89ad38bb-5d6b-3a7b-b2fc-9fc6f530cfcd | -11.05087 | -52.02039 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed644f33-f24d-3189-b1e3-3eed634f882f | -11.54813 | -52.11828 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a45b5920-6715-38f6-9371-efa45143b86e | -9.15622 | -59.55708 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3b55d790-f65f-38a7-a071-9b66381c1690 | -12.43032 | -45.96688 | 2025-08-26 04:46:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ab745ce-e99c-392d-874f-45735b89fb29 | -9.61242 | -55.36662 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d9d9176-32a9-3d5f-9c9c-a8d8f8946653 | -10.89329 | -55.78005 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6393228b-8d82-3df0-948c-f1e9ee806391 | -9.27555 | -59.7915 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5663bd1-2b35-3337-b313-5430814655ef | -9.69417 | -48.33808 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 559cfbae-851a-377d-b0fd-f2aec2a62afb | -11.54648 | -52.12881 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c85ba88f-9a98-392a-9de6-028874448b21 | -12.76098 | -48.14936 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffb0c131-6b6f-31f1-ac5c-abfddbead8bf | -13.4449 | -47.00462 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9b3fe63-57a1-3c46-82f1-c0aa180c2649 | -9.03654 | -65.73197 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfd09d07-1f64-3737-8a28-fb11984dbedc | -10.93286 | -55.31931 | 2025-08-26 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d305808-f70d-3766-8875-9b591f233afb | -15.02864 | -48.15621 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba2db05e-9771-3a77-bb94-ac28baa14888 | -10.43475 | -47.17496 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cfc566c-e58a-32ee-a503-22a5e4ed3a0d | -12.74209 | -48.16065 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a998ef73-0187-34d5-b00f-8e513b9e8ae6 | -9.18336 | -59.53573 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d24a1acd-a4e1-3619-90f7-9032ddfe5e3c | -10.68711 | -47.14719 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae35c336-47a4-3446-9ee4-c1f18f9f3832 | -11.52882 | -52.13315 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 57107f04-93e6-3016-a091-6a3a54653b21 | -9.31218 | -63.44468 | 2025-08-26 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a95fa2a-42fb-39d7-949f-9843f9d63adb | -13.41325 | -46.92315 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd865a1c-cefb-36e1-8617-84d0f6b30d88 | -9.64304 | -59.63805 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 370a1595-ad8c-3af9-ae39-c9e8825046f5 | -12.77531 | -48.13128 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e195eaf4-3c84-36c4-ba00-d33a15a17cea | -13.61097 | -48.1579 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1a92f381-5fc2-33ad-90b5-739f5ed74ddd | -11.55475 | -52.09775 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358698c2-c506-3916-98f9-45c297bab614 | -12.77398 | -48.11248 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c58ad788-71b8-3947-ab5b-8470d9e5d61b | -11.04094 | -52.0188 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d31ac8ae-3c6d-31b9-9b29-a6891697f868 | -10.53646 | -46.80557 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2af95302-166f-3e74-855e-acad41bf497a | -8.80692 | -52.07803 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d80aae85-8811-3578-8ea3-bcf5e3bad30e | -11.5371 | -52.1237 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 5515af37-826f-3d77-927f-440583c9a6c9 | -14.30816 | -53.07166 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b74ff62-2202-30b4-888b-d0ba97a83338 | -11.56745 | -52.1034 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c3b1f37-c405-3cbc-ac45-5eda0b763dbe | -13.4425 | -46.86617 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7a3ac33-6ab3-34f4-a09e-f72e77ecc00c | -7.39521 | -64.34986 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07d4be2f-83b5-3445-be4e-1534f8c42bd0 | -11.55917 | -52.11287 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de653a69-a33d-39f2-91fa-843691bd1d26 | -9.16444 | -59.45381 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50f8e59e-3070-3c7e-8064-d76724850968 | -11.15065 | -44.74591 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43201101-278d-3c0d-a928-5fac6a447fa4 | -10.42004 | -64.3882 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8e75333-7c99-3ab0-9a89-11995b7556ee | -12.75609 | -48.09894 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ec306a3-1969-3844-b432-bd2d2f79c0c7 | -12.66782 | -47.8688 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27e1e62f-c843-3fc1-9545-fd2caeb5e04c | -11.04866 | -52.01285 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5614b154-53db-32c9-b607-457ec840c88c | -14.44141 | -56.46464 | 2025-08-26 04:46:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4722271f-847f-3627-9ae7-fd4fa477d980 | -12.75513 | -48.09753 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3897891d-42a4-3f4a-b7b1-0eb9dee48387 | -15.57161 | -43.85705 | 2025-08-26 04:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| efd28024-3b73-31cf-a2bc-3955257019db | -11.36231 | -51.28513 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afefd510-5fb4-3aa5-b79c-4d070edc81c0 | -13.35966 | -51.79818 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 368206e6-0e3f-35bd-9764-686bf237ec2a | -13.41009 | -46.91483 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25c164e8-cf70-36de-a64d-d7fa06bf1ff7 | -9.17656 | -60.80832 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cc81564-6887-37a8-aa72-c1c7ea865a2b | -9.38664 | -60.54588 | 2025-08-26 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1af4589a-7abf-39c8-88d2-c57b13eb42b4 | -13.44236 | -46.99215 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 392621f1-2b95-3a2b-be81-0318ad11481c | -10.54053 | -46.80617 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| a3524747-19ac-3f76-ac3b-7c570faad73c | -11.30927 | -55.1069 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 215c6b1a-ee68-323e-878f-cb308fab3040 | -15.04129 | -48.15259 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b50eec25-1ed0-33c8-a67e-8698ccdde605 | -9.21908 | -59.67124 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f116298-eca8-398a-9b75-e8baa17def10 | -14.23758 | -53.04517 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eb862e2-f30e-3b28-ac9b-8383e391b686 | -15.13246 | -48.68195 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a187c615-cb6a-3ce8-9e62-b01d600be0f7 | -11.19671 | -55.04252 | 2025-08-26 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4337e3e-3571-3170-b7de-ab4015389902 | -9.80187 | -64.25566 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d97c601b-b8ce-3bcf-b7ef-af56e770c147 | -9.25075 | -56.90346 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 455aed0a-620e-34f9-9444-925cfdcd18aa | -9.22544 | -60.92151 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d154c100-ecfa-3409-9787-dd665fa23bca | -9.15297 | -59.4626 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a462af2a-9e50-34bb-b31f-17cd4a304291 | -9.1679 | -59.53841 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 976ed9f0-021d-3901-83f3-176f6e1fbf47 | -12.41924 | -43.4884 | 2025-08-26 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fc41e92-251c-3067-82b3-3fc8130a1062 | -11.35842 | -51.28817 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 777c9ffc-b4e3-35e3-821f-136acda67cf7 | -15.08484 | -48.56899 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3e19a6d-42a7-352b-92db-88e65064c0da | -12.4167 | -46.81208 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b8e5ef9e-d981-334e-a8c7-babcc1dae523 | -9.15527 | -59.5528 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 3309e174-a20f-30f7-853a-0339ca058e35 | -9.55997 | -48.78979 | 2025-08-26 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e1f77cb-0010-3042-adc9-4d40ffe12687 | -9.17252 | -60.80077 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24d026dc-1e29-38d0-95fd-8bb663bb333b | -15.07667 | -48.65828 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d26f2c8-48b5-35eb-b543-45fa5d84cea9 | -9.17248 | -59.52125 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78f0ffe0-dbfa-3883-8ae2-d67f5492de94 | -13.63188 | -48.1506 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8093e25e-7ef5-3ed3-9040-f3f4c1c003db | -13.39803 | -51.77118 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a276601-ae45-3fe5-8c63-083f14aec2fe | -13.44735 | -47.0262 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71c26765-28f4-306e-9210-c336c4409ee2 | -8.88966 | -62.46681 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README61.md)
