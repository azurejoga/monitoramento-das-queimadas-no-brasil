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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b3b48f9-37a4-318e-b344-f00c324226e1 | -14.42622 | -47.35472 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d51c1e72-c580-3ceb-a3d9-7f4df60cc99c | -11.26654 | -50.82758 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 249a186b-6609-3abf-82d4-cfd144089f6c | -12.16572 | -47.58489 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b8805c4-7aa3-31c6-b65a-0a8504152fb5 | -12.97388 | -47.97524 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8dd965cc-a7c0-3148-b142-1c577934d111 | -14.94413 | -46.5517 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d74a234c-9abc-3a23-84de-09846349d1c4 | -12.01018 | -46.66661 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 95f9c19d-d54c-3ef3-9cf4-5db871c647dc | -10.64924 | -46.23523 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 885aca94-af6a-305b-a8d6-b889350b0a35 | -10.33651 | -44.98986 | 2025-09-15 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4ce0149-a00f-395d-a1f0-402d0ce4f112 | -11.07632 | -49.74321 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9ffcf2e-e810-319b-b173-7d8db512be8e | -10.75574 | -50.64922 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8d11f313-5285-36f8-af33-c7863f5e3519 | -12.08395 | -44.87706 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56cf7372-24e1-3757-bf8a-57327e4f1b31 | -11.78158 | -43.76102 | 2025-09-15 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa59aa99-7c47-355d-9549-0e3a0cd48b71 | -10.7536 | -50.63824 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 75ec32d6-f57a-3472-b20a-baa9beed7890 | -10.1788 | -46.15206 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69768e1e-201e-3656-8958-04b0048c7293 | -11.0559 | -43.30072 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3dc77bd-f2a8-381f-9edc-e0c871d52526 | -10.88153 | -45.44657 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35e0109c-51e3-3a6e-8ee5-ca209770a85a | -10.75916 | -50.65837 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90dd33ef-0072-373a-9b28-a30407daa269 | -10.65586 | -46.23626 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09ea1e04-0c4e-3586-83aa-2eca77845c94 | -16.07505 | -47.85812 | 2025-09-15 04:21:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b98601bc-3c2c-3805-afe6-452ba9120434 | -11.99918 | -46.65035 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9201beaa-66ec-3392-9739-bb4de2c788b0 | -16.99616 | -45.85905 | 2025-09-15 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9df3b16-9a9a-317e-8c2a-e5918a5b1115 | -11.61042 | -46.59021 | 2025-09-15 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4df2883-984f-3ea7-a12c-e58a053fa936 | -13.94008 | -44.79827 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d2bde93-d411-3330-bd3e-e7205aa99132 | -10.79163 | -45.97941 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb8c0812-6ba4-3c26-bb12-4834b8103885 | -14.63393 | -46.38086 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5450fea6-ff0b-35f3-8f51-4b1050680f1c | -11.77944 | -50.44063 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6160590-25d1-3f0f-b7fb-aa72f622b02e | -10.92063 | -45.45631 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80aad3b1-8302-3764-a566-acd62b731d11 | -12.11841 | -44.83086 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f081273-3318-34ae-a712-2fb2550d7b77 | -12.08629 | -44.72571 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de5ed485-ee9b-38d9-8559-972b40b604e2 | -14.94469 | -46.54816 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9f5813ca-0e7e-31da-a0bf-d3b7b9223817 | -15.79559 | -52.19922 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7f1d2b8-6ff0-39d8-af53-d28eb43619da | -11.87221 | -50.53577 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cdf6885-f6f0-3207-a169-9d1e1a170f57 | -14.5053 | -47.34965 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4f51500-e015-3709-9f4d-2612902665b0 | -10.92965 | -45.57239 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 956264e6-de43-37dd-9c45-e9a3590a5fe2 | -11.87387 | -50.52594 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6bb5a584-a1cb-3dc0-80e3-f4b58a32ba8f | -10.76454 | -50.64544 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 264db67f-a1cb-3036-90d1-cf37ac334eca | -12.44373 | -46.87249 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ef7cc75-9956-3390-9e36-79cbe5b668f6 | -14.27588 | -46.10062 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3396690-8030-361c-9bb6-37b56bd094f0 | -13.17814 | -47.28223 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e880e07f-3790-3871-96f7-dcc8aa56a0dc | -9.48558 | -47.93483 | 2025-09-15 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f57b040a-149e-38de-9c68-c21f350a985b | -13.18869 | -47.2803 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56a8b676-672a-3875-af18-6150c7611eaa | -12.69948 | -43.46827 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15a1ce57-9dfe-3e4f-913c-42c346fd73e6 | -10.07678 | -47.19774 | 2025-09-15 04:21:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e8cf1b4-8ff6-352b-8712-1eb59dabb542 | -16.03079 | -47.55898 | 2025-09-15 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d602a6ee-b022-322a-bd3f-6427aab4d716 | -14.20397 | -48.76876 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a6c9fc6-189e-36ed-9c69-f59b43414069 | -14.80278 | -51.60554 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6d26279f-f84e-38dd-93c5-f4c6bd481992 | -9.01626 | -48.02806 | 2025-09-15 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d052dee9-5561-3776-b138-f24ae8c92701 | -14.24799 | -43.19736 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a143d5b0-8254-3061-9213-6c1825d3e1ca | -13.87468 | -48.13834 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 397a4a69-183a-3f34-a96c-0d23d7f39fa7 | -17.3416 | -42.6465 | 2025-09-15 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ac694495-fc59-3da8-8935-9705d7eac7e8 | -14.94631 | -46.58109 | 2025-09-15 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a1d896f2-6762-3145-b424-762f451da1b6 | -12.04186 | -46.5308 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7eb0585-6e86-3282-92ed-cc540607ae83 | -11.33572 | -43.48961 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f6399e0-50e0-3add-9a2d-8e8d1f73be07 | -10.91423 | -45.56278 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f85074b5-a8d6-336d-969e-33025228a9c1 | -11.99806 | -46.65741 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a51ce7d8-ff13-3bf2-8042-0aa1422392af | -11.74457 | -50.45959 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef5f7af-c261-3575-bb34-e3ed44fd9b48 | -13.18087 | -47.28642 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38360182-f044-3eb2-96e8-acf97b65867c | -13.86578 | -48.12909 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bcae4a1-4cba-3a53-b4cd-bef83aca6bdd | -10.76538 | -44.71977 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f525a265-533d-38d7-88d7-d205607b7dbd | -15.09527 | -52.48039 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b02f114-b6a3-30a2-9c17-1c99153424b9 | -13.94742 | -44.79562 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2c0e09f6-c89b-391d-9b45-b3c394cd4c4a | -12.08449 | -44.87346 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10166864-7920-3852-97c0-07ee9539263e | -15.79966 | -52.19962 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94de00f2-43b4-37fb-8314-62466897f556 | -10.79652 | -46.42122 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34d80e58-99de-397b-8452-22764123abf9 | -10.39791 | -48.61055 | 2025-09-15 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53781b4b-d22a-3ce2-ae24-2cb3127a3719 | -11.81713 | -50.44056 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3ce740ff-064e-364b-ad5a-8e80546b3e47 | -10.92584 | -45.59684 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eeaeec1-e69f-3ff1-96b1-3b0d8416cd7b | -11.72228 | -46.48615 | 2025-09-15 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f631d31b-6f33-3f50-9f0f-e82e9c3ab607 | -16.40429 | -49.07269 | 2025-09-15 04:21:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b22c9dc-5c2b-3617-94f5-49c72c7186e4 | -12.6989 | -43.47232 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e871294a-26c3-3af9-89d0-324659ee283a | -11.47934 | -43.60215 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f65709d-659d-3a0e-ba5c-741d6f2bd9f5 | -9.55215 | -45.98275 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8506bf0-d860-383f-b711-44daafb7950f | -14.43518 | -43.22143 | 2025-09-15 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 620f3849-6576-33d6-963c-eedb43c5bc05 | -10.68779 | -46.24862 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cecb8518-d9b0-31bd-9f66-3d3b4e4af8d9 | -14.83059 | -51.6322 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2b6cd6e-a88c-371b-84c9-a5b53c4766b4 | -10.93836 | -45.51646 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b338a93-ad4b-3085-a5cd-fb5487c9f18a | -12.43654 | -46.87495 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cbeae9d-ce69-343b-ac1d-446f04541e07 | -10.86614 | -45.45847 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd6bb453-1bf9-37c4-b187-f7d30c888c5e | -11.0854 | -49.71214 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 695055e4-e9b1-3230-a7f5-f753aa808c14 | -14.315 | -46.06689 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a32a90fc-110f-3c94-9ccd-aee1a1c4176e | -12.43998 | -40.82163 | 2025-09-15 04:21:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 92f70fb7-fb2e-338d-a4da-0aed97cc3a77 | -14.13545 | -45.41653 | 2025-09-15 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 257ebfee-b3ca-3602-aa03-71fdcd034248 | -10.72663 | -44.77571 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52b303fe-1c02-31db-b0f2-7bb674cc5a63 | -12.60196 | -45.71119 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e60898a3-2af5-3f36-af6c-a405977a2050 | -11.43959 | -43.54472 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32d106ed-d921-3117-9a58-ab98f143d8fe | -10.79108 | -45.98289 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8bb584c-dbb9-32d9-83bd-a26b7c536b1f | -10.15577 | -45.30172 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9644356-cdc8-3836-9545-a40c1cdac752 | -11.08531 | -49.73539 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3126cf52-72ad-3ec3-88ad-cca7283795b3 | -12.16968 | -47.58176 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bdc9a7c-d7bb-3e16-b7d1-e226e5f67443 | -13.90647 | -48.31238 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a438523e-1bc9-32c9-a67a-0ffb082ba071 | -10.75475 | -44.69982 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04a5d3b2-0050-3fc3-b907-c15486ab70c6 | -10.74966 | -50.63755 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 43e9b857-75e2-324c-a66d-f9a16865b962 | -16.8858 | -45.77743 | 2025-09-15 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b9b2fbc-573e-303e-b00b-adbbf0443356 | -15.07939 | -52.47371 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 175ec5bb-156d-3b78-b75a-fc6220f86c98 | -12.98126 | -47.97261 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b6b25f72-45f5-3194-a8a2-efc8638c6416 | -15.71548 | -53.07241 | 2025-09-15 04:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a7d83f6-c3eb-31fc-838f-3adeac47aea3 | -15.76323 | -53.47421 | 2025-09-15 04:21:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 740e2052-a513-3bf6-a5d5-240372760f9a | -10.71404 | -48.69789 | 2025-09-15 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6c036ff-9d41-380f-9b04-5280d1277faf | -9.72814 | -46.86993 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4b945af-fb79-31bd-be75-a39102aeee23 | -10.64593 | -46.23471 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README33.md)
