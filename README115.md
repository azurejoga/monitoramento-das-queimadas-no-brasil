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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01e29d16-66bf-3f75-8c0f-b926917e674e | -13.74202 | -48.08455 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eca6a47e-3e2f-3e0d-b895-30a2b5202e2b | -11.13105 | -47.85065 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46a601f3-579b-3485-8c83-880ea0f6c583 | -13.31884 | -48.12704 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fea05bd-9470-3115-b37f-853b5c9a9a28 | -13.96313 | -48.18297 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07a7cb6a-0a15-39dd-9fc5-6168e8843d43 | -13.29056 | -47.83153 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83e4dc5e-5040-34c6-8c48-79d90f76373b | -13.29499 | -47.60205 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4f187956-d351-3085-b3f7-62c138348ae7 | -14.46776 | -48.39709 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cbfef8c-8581-3e6b-98fa-05ad034898c3 | -13.60634 | -48.18764 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63d8bcac-6eb1-3770-a1a5-5119c7e55b37 | -13.33164 | -48.08129 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eee6377d-3925-3b57-8acf-412f0cf4e889 | -10.98115 | -51.10263 | 2025-10-04 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cbb19e4-3441-3134-8f90-0d634622752c | -15.37342 | -47.95275 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c732f7f6-c5a4-32ef-8fef-62140f3fe08d | -15.24789 | -56.84706 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 647c6b7a-ff62-3ffa-84e2-167faad5e814 | -13.39471 | -47.56177 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e5f12a7-d208-3d8b-858f-b96ed75c3d62 | -15.23011 | -56.8293 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64cf5802-d95b-34cf-a14c-68a18479a1ef | -12.72474 | -48.57304 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c572f319-46d3-37bc-9456-da7d363c0439 | -12.81758 | -46.86843 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 417eaaca-59a2-3a84-86e8-788d75f2bc62 | -15.58583 | -52.46285 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8fc9c73-8fd0-3920-8421-8b371230ac1f | -10.33668 | -50.33475 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e0b154a7-38e7-3d26-b4fe-3d34525a4ba7 | -13.26136 | -47.21525 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bb7a249-4fa5-31b9-a79f-69d202492367 | -13.29025 | -47.59462 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8974a048-c562-393b-a8fb-19973e6c7fb9 | -14.89496 | -48.28204 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c6e3556-d5f3-37bd-8f7d-af5688a9c1c0 | -11.569 | -47.67477 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74b64044-2a75-302a-950e-08338bc0146e | -15.73486 | -46.27244 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 551c9fec-a12b-3e4f-8731-8503b6530eab | -15.70971 | -46.27333 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cc4828c-7f92-3309-9afe-aafb9e7e5b35 | -13.33049 | -48.07315 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 14b6dd7a-ddc6-355f-bca8-e866881139dc | -15.36774 | -47.95155 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54c5aa13-faaf-333b-bc1e-f93e7525ccf5 | -15.66567 | -48.14716 | 2025-10-04 05:06:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11eb5eda-a29b-3858-9319-62442291a4d0 | -11.12016 | -47.8955 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b289de6-1b74-36d1-ba6e-13aac318246d | -12.71648 | -48.55576 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9c6a296-1bf1-38de-b675-7132cf747a0b | -13.27344 | -48.15874 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be3060a3-0819-3784-b09f-5cbbd51047a1 | -11.14685 | -47.89579 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5935408-aea8-30eb-b8a8-08b1d70a9526 | -11.55877 | -47.68597 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 564ea824-7da8-39d3-87b7-fd4ddca67fd6 | -14.24033 | -46.10642 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a623f89a-325f-3361-9247-2f7aa4d236e7 | -13.17606 | -50.92168 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4ff846bc-1a88-3cf3-b2ff-044d00e2c4a1 | -11.85724 | -44.95197 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a2032be-e256-30a3-9a77-bc244c1114a5 | -11.45485 | -45.14096 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca30f2d1-ae30-34e5-8b7f-7fdf16a8ae64 | -14.38843 | -45.94831 | 2025-10-04 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60722cae-8d5b-3b4b-b8d0-3ea7d0216ae4 | -13.9788 | -48.1885 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35514087-da13-306e-9f0c-29fe9a46c936 | -13.59655 | -48.17896 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26266533-2b6c-3978-8c20-13eef20739d5 | -13.11873 | -47.94205 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a970b43-0095-3d23-9a95-f81e9de5db44 | -11.91521 | -46.39264 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d338087-198b-3b23-8ef1-2fff5b2b6176 | -12.52894 | -45.9775 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5a106ba9-161c-313a-8f12-cd1f28d1a5c1 | -11.92513 | -46.40991 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| a99a6d39-34ca-39d3-84ba-a2c94ddc49ad | -13.31352 | -48.1262 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21fbc9de-d2db-354d-a8a4-e8ab94e58b55 | -14.6952 | -48.09539 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e97914e-d9e9-3535-9754-5a54102f0d74 | -11.78878 | -46.81912 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 065e7818-f47d-3baf-9871-92b2a5e56e4f | -14.88799 | -48.29586 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 742c493c-17f7-3e76-abb2-22284d462a80 | -10.63924 | -49.15825 | 2025-10-04 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65dfe706-a9c2-307f-adc8-8de25726011e | -11.92345 | -46.38021 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8407068c-6c06-393b-bffc-b813f46fa306 | -11.56011 | -47.67543 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 37df5d82-9f82-3460-b46e-1eca6d4181c2 | -11.31456 | -47.83381 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c4af3fc-19ab-3c7c-b0f8-890408336308 | -16.0521 | -50.92443 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d470b055-6235-36ce-a789-f2dcc5771d0e | -13.2205 | -47.8468 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a564c51-d8a4-38e7-8db7-2d959308ae3d | -13.97346 | -48.18767 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 700ee27a-cb70-3f7e-b579-69a8abc4d31d | -13.34696 | -48.07172 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd986dfe-ba3c-3bfc-9058-0e89088d311b | -16.01036 | -50.92294 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f98e56e-2a4c-3a63-8ee6-f7405d8c9176 | -15.59151 | -46.94453 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36d7b6c4-d00f-395c-81d3-af0c0cbf0802 | -14.92787 | -46.88451 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95cf0db0-4587-3ede-8bdd-19c078875e18 | -14.75233 | -48.14272 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa4e9994-b8ba-359c-b4b1-f2da84f0618a | -11.74624 | -54.72063 | 2025-10-04 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5e3e398-a6ff-3ca8-97d8-57c4d9c9d0ab | -11.91949 | -46.41278 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 77727098-d503-3671-a608-ca80d360c161 | -10.33728 | -50.33042 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f6dda5c1-9f39-3fd3-aeb1-cfa5b76062cf | -14.32336 | -45.86306 | 2025-10-04 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c4ee589-820e-3e7a-9352-40a523c8339b | -13.68664 | -48.0447 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 875ea25a-5c24-3051-9ab8-af3a4277568e | -11.86309 | -44.95792 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bd720bf-67e2-3442-947f-86e737249b38 | -13.12815 | -47.81968 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d2f4a92-00ca-3c98-b10e-5ee0707e9a37 | -14.65937 | -48.30765 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 26fe6871-48bc-3428-875f-ab24be696d57 | -12.81194 | -46.85722 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65836f6e-b1a1-3592-a73a-cecfc7c96ef2 | -13.31252 | -47.26766 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c5ae5c-1ca6-3ed3-831c-61c37dbd34bd | -11.13996 | -47.86522 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e349694c-3348-33e9-a809-c8b4fffb05fc | -13.99952 | -48.19737 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02a377bb-aa7f-3ff4-ace4-5c6688aa3fda | -15.21737 | -56.84577 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 165c4e29-1f99-37ef-9a29-4989d800a54a | -11.87999 | -44.98149 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be896e4c-9b90-3481-a2a7-6eba7a61d7ba | -15.59475 | -52.49107 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25abc770-85b9-38ff-9f7a-b8e980f888fd | -11.25107 | -47.78709 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bdece12b-0226-3b5f-8e60-2530240b4eed | -12.65629 | -46.97707 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81292f63-d5db-384b-bcb8-33a062639d22 | -11.13371 | -47.18447 | 2025-10-04 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 025bd998-023f-3fd8-bfdc-51cdecfce2a9 | -11.6904 | -47.49259 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1579e2e5-a0a8-36de-9bdd-647a2756308d | -11.07912 | -47.88036 | 2025-10-04 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fdaa269-c10a-3a3a-a885-6778484ae938 | -11.82566 | -48.06897 | 2025-10-04 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c85924c6-fe39-30be-9423-c118feae8ed8 | -13.75667 | -48.05388 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0987c0ba-b2e4-3090-a23a-2cdf36370508 | -11.53948 | -47.666 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb816ad6-59cf-3ca8-9cef-d2e20f4ee759 | -14.64878 | -48.30516 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e44fd39-a151-3378-b1c3-1d34646c0f89 | -12.29268 | -45.3632 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b94fe54-bcad-30c4-9192-30991ed3d287 | -16.29422 | -45.24394 | 2025-10-04 05:06:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9c22db5-9fa1-3c68-b82b-66e0361dd6ed | -14.92115 | -48.34068 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61615b6f-ca0b-3609-a63f-283a9e98bc38 | -10.5986 | -54.35554 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79e52c5b-5e81-36ca-8331-c28c191fb341 | -14.8954 | -48.2781 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4476c7c-7118-3c53-9b58-2061754cab60 | -11.0463 | -47.80075 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 415470ce-6ead-3e00-8edd-61cdffd282a6 | -15.3149 | -56.94249 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aed5f80f-02f6-37e0-9a97-7ca97fcacc15 | -14.88968 | -48.34871 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb48ce5b-835a-3fe8-881c-88fe42241af3 | -14.58246 | -52.48922 | 2025-10-04 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d164ae0-24a6-3a0c-90a7-fbdb3b1dd6b5 | -14.67962 | -48.27448 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d59df533-a441-3b9d-b059-3363f66a2180 | -13.35392 | -47.23721 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c656fa1-b5bf-3c24-9bdc-59f18c111955 | -13.11409 | -47.84486 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8c73c036-eea2-3021-b3e3-138032503401 | -11.08969 | -47.88129 | 2025-10-04 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d2c2ccda-c9f1-39e7-8090-5a6e90c82c5a | -13.92993 | -48.16102 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1990ced4-5ccc-39e0-b639-1583c2c3454e | -15.72828 | -46.27546 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9820b13-14a3-3bac-9ac1-01bc5bb4b720 | -10.05153 | -62.46246 | 2025-10-04 05:06:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28e36f00-c164-3973-84a0-87210f784e8d | -12.81855 | -46.85979 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README116.md)
