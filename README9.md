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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 568faff7-099a-35b7-9b9a-fe14c82ea645 | -12.45913 | -46.52268 | 2026-07-17 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c55c9f2e-6ce4-3387-ba5b-e9d1713ee3c0 | -10.84686 | -47.26112 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b42624f6-375a-3cc8-a1a7-7d8bdefb2adc | -12.50627 | -46.34966 | 2026-07-17 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c688dd2-2159-32e9-b86b-14ddce4b8eab | -9.50981 | -47.13959 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 844c3947-0676-3873-b655-c718571a1eec | -7.9115 | -48.2625 | 2026-07-17 04:38:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e83e8856-10b9-3e1a-8fa3-bb7b458a5fe1 | -10.84741 | -47.25761 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 238aecdd-3f5c-3a93-bce9-e38f7a12c3c1 | -12.4526 | -49.58878 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8c55e6c-e18b-36e1-9ac9-5ef4cd7578be | -9.90815 | -53.36823 | 2026-07-17 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a43b915-ed95-3388-91f5-bde453c0a05e | -10.86355 | -46.50668 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 30c1e4c4-539f-355c-b6f1-1ab11cb2a953 | -8.50502 | -48.07056 | 2026-07-17 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19896bb4-64a8-3d45-89fb-0d5b64f95bfa | -7.96409 | -49.64491 | 2026-07-17 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8d3916d-b766-352a-8bd6-2ce6817cf0b8 | -7.72976 | -47.24378 | 2026-07-17 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a92233a-c431-3531-b218-588c48f09e57 | -12.69388 | -46.5138 | 2026-07-17 04:38:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9865d16c-547d-3f9a-953c-dcee32e59c28 | -7.29484 | -46.2476 | 2026-07-17 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9093a6b-3fe8-3e05-acce-4831fa164286 | -9.51313 | -47.14013 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 44911359-e62f-343a-9ab7-9ebadff3d18e | -10.8641 | -46.5031 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1eb2eef3-b75f-3ada-bf29-9cdb285c4176 | -11.78438 | -47.08972 | 2026-07-17 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33c55dc2-f3c4-3f76-9e45-abe54bf9a423 | -7.91267 | -48.25523 | 2026-07-17 04:38:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70d29810-4128-3872-a997-9f249c408f9e | -10.82174 | -46.53297 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1d087a81-1d21-3d85-810b-1904f6e3a58f | -10.83574 | -46.57545 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7663575f-4f76-354a-b665-87235719c9f1 | -13.25615 | -45.11293 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9bf0e261-de31-3129-ae2f-5eccd55b6784 | -12.45322 | -49.58504 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8285e2b9-bf28-3546-9feb-eada995a9181 | -5.63437 | -47.09841 | 2026-07-17 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fc03fd5-a962-3b38-bd19-67c745344c02 | -10.82114 | -45.13293 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bebdd3fd-e704-34a3-bbdd-973de3f244e4 | -7.89415 | -47.69827 | 2026-07-17 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3d69b02-831d-35de-9e37-2b3b21182c99 | -10.74762 | -47.90725 | 2026-07-17 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a13565c3-49eb-345b-a280-0c6e36fb4c50 | -10.82056 | -45.13682 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9c2ab220-fcb8-3ec7-85b1-775e058cf6f8 | -10.81806 | -47.37875 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab574f91-2df4-38aa-ba9d-227e9c3d12ca | -9.90339 | -53.32075 | 2026-07-17 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b62321a2-3dab-3573-bf4b-142875b463c6 | -10.81529 | -47.39629 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f57210f-1b95-3543-9c45-256bff69036b | -10.81912 | -46.53644 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f42699e0-9ec6-3666-83f5-4237c4f747e2 | -13.02784 | -47.93646 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4a7d229-a1e8-3ada-ab1a-a70654d9c41d | -10.82041 | -45.12983 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d5c1b905-e9a4-34f5-8483-15f5e82b84a3 | -10.8602 | -46.50615 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 72afd5ca-752d-37aa-8a69-53e60c6c1352 | -13.24603 | -45.1071 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 89e94c7e-8cb2-3632-b0dd-8d98f99844c6 | -10.81299 | -46.57563 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ab8bf7-3c6d-3971-a9d3-77911efc5752 | -7.91208 | -48.25887 | 2026-07-17 04:38:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80a35b9c-f6be-3663-9d8b-01feeb833281 | -11.78771 | -47.09026 | 2026-07-17 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfb1f62e-e8e4-3bd9-88c9-e817c4ec6f2b | -9.19338 | -43.14626 | 2026-07-17 04:38:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8b0eb274-2f62-3f1a-be8c-f3f1485f835a | -6.49969 | -42.21059 | 2026-07-17 04:38:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6329741e-ed68-30c1-b338-c204bc22bcc4 | -10.86131 | -46.499 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 486a56ce-0684-3968-837b-b71b1a41367c | -10.04119 | -51.66294 | 2026-07-17 04:38:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 397f2caf-eeb3-36c2-936f-e26909916183 | -12.4374 | -49.5747 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e049b7-721a-3f0f-b627-ed52071012a0 | -10.04037 | -51.66777 | 2026-07-17 04:38:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 046cf3d4-072d-3249-92cd-62e920886b1c | -12.12118 | -49.93869 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1af741c-655e-3d57-96f7-49039d6f66c5 | -9.95625 | -50.5545 | 2026-07-17 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ac03413-1680-3c49-891d-994c018891cf | -12.66235 | -48.23194 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e979e776-a88d-3130-a5d7-957e4ba52997 | -13.28614 | -45.20613 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b03e1609-84ce-3c44-8412-1529b29cea32 | -8.51117 | -48.07521 | 2026-07-17 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c11fc4ab-177c-34d2-b481-82e90d0f5227 | -12.45404 | -46.51068 | 2026-07-17 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c9b6668-6d4b-376e-acd5-715467063426 | -10.81823 | -45.12848 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 39f4eca8-1bc2-3e41-abef-1a2d63eb5bfc | -8.98623 | -51.47601 | 2026-07-17 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01104b82-af87-36bf-921d-559251a09f56 | -11.40366 | -47.53186 | 2026-07-17 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4faaac18-8def-32dd-b3b7-81fe1961a216 | -11.40698 | -47.53239 | 2026-07-17 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94a67f42-c291-3ec5-9fae-b46a9454c7c4 | -10.3878 | -44.92187 | 2026-07-17 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6e67cab-1619-378e-8cf5-d1ac768eadf6 | -13.44135 | -43.85683 | 2026-07-17 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5345b3cd-f316-339d-8211-1de49614fb6f | -5.89995 | -46.2118 | 2026-07-17 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24f0e4d5-81fa-36a3-b0f0-44bd034fc9af | -7.96341 | -49.649 | 2026-07-17 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6773bebb-be0b-3abd-a792-f3cb15a89ff0 | -12.19676 | -46.48188 | 2026-07-17 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e84fdbc-e879-35c2-a5b1-f58f101195ec | -7.6297 | -50.03563 | 2026-07-17 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6aa1a2c-1921-37b8-ad54-60c75f0499c2 | -12.45199 | -49.59251 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4cba070-ec0b-3697-b86e-ec91388f3079 | -13.50372 | -44.28023 | 2026-07-17 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f376369-9558-3c83-b15a-d847a018dd49 | -10.86521 | -46.49595 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1420dce3-1d25-355c-b4a6-836d75b698d4 | -7.91547 | -48.2594 | 2026-07-17 04:38:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 834daf1c-8af8-34a1-9ce7-d3a74a0fe59f | -9.90386 | -53.36733 | 2026-07-17 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a869366-d9e8-3ab5-8ff0-ff5a726c32a5 | -13.28025 | -45.19676 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 219927dd-196d-3ec4-8e92-ec2d483e8d70 | -11.78105 | -47.08919 | 2026-07-17 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6fbf9bd-689b-3c55-8732-2a51c2ba009a | -8.50838 | -48.0711 | 2026-07-17 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fd518e7-fc5e-3e42-aba6-c9c6b48ef799 | -9.69533 | -47.69332 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb338556-0489-35bd-858d-c53a85130d49 | -11.11652 | -49.71871 | 2026-07-17 04:38:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1040dbe-1097-3ea8-80c4-69d3fae8dde5 | -5.89664 | -46.21127 | 2026-07-17 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 373964bd-a388-39e7-b349-4f77fc292f24 | -9.90694 | -53.32565 | 2026-07-17 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3938c006-ea17-339b-ae2f-5a0487b2d1fa | -9.69477 | -47.69683 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a35076c-29d8-3928-b41b-ec58b3e1c3df | -10.84897 | -46.46777 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37e106af-c40c-3424-9af1-0bcb7e3c4098 | -12.11643 | -49.94578 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 703ed42b-d4af-3e92-ab16-b0b068ba33d0 | -9.69866 | -47.69387 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c69d3955-48c1-3640-897d-8d9e449bf552 | -13.26483 | -41.66293 | 2026-07-17 04:38:00 | NPP-375D | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f0a4d993-d093-3012-9ddc-d443fe419cdf | -9.95554 | -50.55875 | 2026-07-17 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b2666a4-48bd-3ee0-8a13-dba4817a7726 | -13.25197 | -45.11647 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e0513983-01dc-354d-b2e8-53572160818b | -6.01447 | -46.32201 | 2026-07-17 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 531c3bae-bb05-3cf4-beb7-b8fe82eee306 | -7.63334 | -50.03625 | 2026-07-17 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 107f037e-942b-3958-91c4-378bea541c02 | -12.66072 | -48.22078 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26f25f09-de28-3a97-863a-93b6e20e5e7e | -10.86244 | -46.51382 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d63a0e5d-ac49-3ecb-8b8a-d6595a70a238 | -11.20394 | -49.80401 | 2026-07-17 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2b17dcb-d3e4-36af-a9d1-a8b45973bc5a | -13.2484 | -45.11592 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0304f54a-01fe-3422-8c17-1386f4e0c00e | -9.51369 | -47.13663 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c67278e4-82c4-399d-95d4-1f4850bc2e28 | -10.83685 | -46.56831 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba73341a-04c7-3dbf-9878-3ee31b216466 | -10.82674 | -46.52281 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d81c61da-ae74-3b95-abb1-ddfe5a96d218 | -13.00405 | -48.52811 | 2026-07-17 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 814d7981-f40c-37bf-b4b6-d24aeaf0eab8 | -13.44516 | -43.85756 | 2026-07-17 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eab08570-0b5b-398c-b9d1-8d376c87e525 | -10.82023 | -46.52932 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec3510c3-d87c-39f1-93fb-b411202d970b | -13.25318 | -45.10823 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 67c8f710-4aaf-3f1d-9dd1-2211df638931 | -9.65137 | -48.57295 | 2026-07-17 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db672176-7230-3a55-935b-d3e3b5453fc2 | -13.249 | -45.11181 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 03248209-1a2a-34b6-af10-1d3aaa1c16fc | -9.90645 | -53.36814 | 2026-07-17 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bc9e213-049e-3277-8b0c-21d4a6d0fde1 | -13.24961 | -45.10767 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| c3222ef1-9860-3b2c-83bf-6d643a0d7876 | -7.96697 | -49.64961 | 2026-07-17 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee8d57f-5ed1-3632-aff8-62c284fa9cf2 | -10.81981 | -45.13372 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0d04b8e2-035b-3d9f-8ca2-e0161dba1336 | -12.69726 | -46.51434 | 2026-07-17 04:38:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2996c8b9-1ed2-32fa-9b4f-ce15e1279ed1 | -10.85073 | -47.25815 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
