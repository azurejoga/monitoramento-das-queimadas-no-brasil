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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dff24e72-a892-3e4d-ba23-9a28a21193bc | -11.78247 | -50.43191 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cca4a69b-8499-368c-8ab7-30cb8791ea8e | -15.79441 | -52.21932 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 638500ed-0b5c-3d36-9aa3-32abfb00f121 | -11.81219 | -50.44424 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca8ddd5f-4e53-3b24-930a-d79b6588662d | -11.85544 | -50.52314 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7eacfbbb-f161-3593-ac24-1c117ea719dd | -11.07887 | -49.72545 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42224758-ca72-3605-99e9-fed7538de418 | -14.14126 | -46.25947 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22af5ac0-c837-3cd5-994c-08317ebee69a | -13.19298 | -47.28927 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 224d97a8-4a86-3976-91bf-4b5c8b33d941 | -15.69201 | -54.34015 | 2025-09-15 04:51:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 020d1efb-aca8-3cfe-bf5b-43532eab251e | -12.11788 | -44.83654 | 2025-09-15 04:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a7e4ea5-5cf8-3427-b046-91d4acf7df96 | -11.08115 | -49.71265 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 302c1007-789d-3d16-a6b9-6b03bca00261 | -11.47157 | -43.59258 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e498e6a1-c520-36dd-8058-90f75b7f9eb8 | -14.4966 | -47.35327 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb13b2fc-4b57-3979-a1ed-7d6e186324fb | -12.08421 | -44.87264 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7867918-343b-3d62-8c47-0f4ce7d53597 | -11.13029 | -45.31369 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00182ac5-6816-31db-8bab-fc355012b125 | -16.48857 | -55.10527 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 10460e87-ad88-3b44-8269-b277fa3f0e1a | -12.4512 | -57.78955 | 2025-09-15 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 312d1e19-da2b-31e6-a71e-bc6e9984b566 | -16.67342 | -49.77517 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3901f639-2675-3eb3-8760-98e56470c8da | -16.70648 | -54.97058 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a16493e6-9bf3-3516-9a27-1900a6749faf | -11.80591 | -50.43941 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ef52ceb7-7c6a-3b05-bedf-b9c78a6056c1 | -15.90246 | -49.98752 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77d5e748-a8f4-3d38-8689-07f292d0f295 | -11.33537 | -43.49479 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3665212-b278-3429-9d3c-56246a657cde | -13.88774 | -48.31115 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1342cb4a-ea8a-343c-aca9-5ee870d501b2 | -15.79373 | -53.46247 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7915c313-b31f-3c58-bd91-7415c49af86b | -12.01317 | -46.65772 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3faca4b2-4932-313e-88b1-e7867ffa4213 | -15.78826 | -52.21452 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1e568e9-fc44-3115-98d6-1b4f0e4b8a54 | -15.10118 | -52.48623 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58abfd94-208d-3dad-ad3d-58f2f806bf4b | -12.09564 | -44.85885 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b61e039-7dc8-36e3-a100-6ec76cb6e5ef | -16.66784 | -49.77668 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4cf43ad0-a682-3757-9cf8-9c0f78f1f06d | -11.79476 | -46.65442 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a2c3de3-7f8f-34b8-8e55-e1e0da7f2f03 | -11.85484 | -50.50389 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 989369dd-07b0-330f-baad-445a48e03f63 | -16.7096 | -54.95169 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2ea189e-56c6-386e-8e6b-4c879d4ad513 | -15.14001 | -56.15497 | 2025-09-15 04:51:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8074341-02b1-39c7-9173-35f8c130be37 | -11.79333 | -50.42976 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e27d9e6-c900-3c6b-9a5c-d59f585f681b | -15.79106 | -52.21875 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea0b14b7-cffb-3279-a92e-67cbd0a0a4cc | -14.63927 | -52.01942 | 2025-09-15 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6abf2832-0a18-3c14-9f39-f8b9e91d2210 | -14.509 | -47.35559 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91d915c8-af2c-3a79-966e-e1224a72e727 | -11.07537 | -49.72492 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64e24837-6843-3ace-88cb-37a2a8148282 | -14.46198 | -55.96325 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d09d735-fe2b-3bb4-974d-b6684f61bf47 | -11.71203 | -46.4793 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 190fc93e-1df4-3c78-ae7d-a9de8a8d64c3 | -12.1131 | -44.83601 | 2025-09-15 04:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6ab2d50-262d-3ec4-a95e-cae73c746fd2 | -16.72318 | -54.95415 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b00c5cb5-3446-35fa-9f5a-db872745e3bb | -11.82705 | -50.43887 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4127f14-96ad-3817-970d-4fc4806409c0 | -11.83533 | -50.44706 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd4c317e-0392-3579-9d72-a14d9e6380c1 | -15.76267 | -52.21394 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dc8773b-b193-3cf4-9df0-8a92302b003e | -11.07941 | -49.7244 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7538887d-e3d5-3fb9-bc41-21d31c54a5a0 | -11.31045 | -50.85156 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8c602d3-9296-3562-8b54-4d1510407a6c | -16.70435 | -54.96229 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ac2c34d-505a-3e06-985e-3cacaf63cd52 | -12.99727 | -47.96154 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62c367ed-901f-33f6-b3fa-642e0b07267e | -17.7266 | -47.9522 | 2025-09-15 04:51:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb0d28d7-0e3b-3285-9f31-6eb958a92bb5 | -14.20423 | -48.77686 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53966809-f0ed-3e78-8bea-3fbd0905235e | -11.08066 | -49.71373 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4009733-a957-3106-8aee-cca79aaac58b | -12.78027 | -47.97604 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6cacc5fc-4b1b-3264-b880-46da225aafee | -12.04307 | -46.53489 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b23a7292-63af-334d-8603-1f6de948d001 | -11.28109 | -50.79472 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35d2bc01-547c-36bc-8100-49fa072154e7 | -15.80163 | -53.47101 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93e24bf7-df6c-3332-95f6-61580c7464ff | -15.69261 | -54.33648 | 2025-09-15 04:51:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dba311cd-c579-3462-80d8-307a5996454a | -11.13159 | -45.30412 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f449d35a-3fa1-3743-88b4-02203ccac712 | -12.03938 | -46.53032 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c0751d7-1d14-3da0-b644-75692ea3d516 | -13.8854 | -48.13062 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c7bf2c4-a55d-35d7-ad14-d4b8eed1dbd3 | -14.50131 | -47.3498 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71e4656e-ede6-3112-9dd1-b40ab9ba9702 | -11.1614 | -57.19075 | 2025-09-15 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de14ed3c-da14-3836-8a23-5ee67feebd77 | -12.98555 | -47.95965 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18eac0e0-4d6e-3905-bf56-b77e38864ece | -15.66925 | -52.23973 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e0b3da2-1b91-3a7a-a8db-1b7c3b73e121 | -17.2449 | -49.47115 | 2025-09-15 04:51:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cd0421b-5366-38f8-86d4-6b63726c6e56 | -17.13646 | -48.52216 | 2025-09-15 04:51:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9fbee50-ef5b-36c9-89db-a267891f2efd | -14.3981 | -52.89629 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b24a354-d6d4-3e5b-8ffe-36be49de961e | -13.86969 | -48.1284 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dd124d1-cba7-3106-b594-5bbc86496a3b | -17.83016 | -50.42491 | 2025-09-15 04:51:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6af16e37-4f50-3ece-9246-1f5a28a11181 | -11.79562 | -50.43781 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c12fd5b6-30c1-3579-8ec9-b6ab1a6415cf | -11.81677 | -50.43726 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dfef0498-eed5-3d4f-8857-05cf66041fa6 | -15.68864 | -54.33956 | 2025-09-15 04:51:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58239d12-3810-33be-b829-7d370e749772 | -11.85601 | -50.51941 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7754f65-4767-36d1-81f0-a4a84fc72b89 | -11.0771 | -49.74002 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d79d76d6-4e55-36f7-abb3-ce070715eb83 | -16.66842 | -49.77261 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cbbf9e9-60bc-3785-90f6-5be5c12fc7e6 | -13.21345 | -44.07873 | 2025-09-15 04:51:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5943cba7-22f7-3ec3-9983-bafa06372907 | -16.67286 | -49.77926 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7df331bb-7b6f-3ef7-b723-33befcba64c8 | -15.14876 | -53.5131 | 2025-09-15 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c10cb31-21bc-3a36-97e5-d8c1ca37811f | -11.88054 | -50.5424 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22c1c0d2-5e8d-3b7f-9cf8-bc75e31dc59b | -11.07591 | -49.72385 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a915204a-547d-372a-9393-3e7a76445b05 | -10.93645 | -45.49806 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e792e07b-24a1-3a5d-8f7d-dc602a269672 | -12.00058 | -46.65578 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce0b3365-6e8f-3195-ad9d-5284f96b4037 | -14.80237 | -51.61399 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ec9f25d-83e6-3058-997a-984ed22be1d0 | -14.42729 | -53.3701 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 342d58e4-9e5b-34a7-9fb5-a8477b5924ca | -11.80305 | -50.43512 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c78e152-5899-3905-8fbf-5b3e177de0d1 | -14.14311 | -46.26111 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac03bbbb-3fb3-3ee7-8657-ead37af9c9ad | -14.82382 | -51.63259 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5e15e143-da46-3ae6-9bd5-d1d25e84e7e8 | -17.17109 | -49.38814 | 2025-09-15 04:51:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86528c3d-a394-332c-9f59-9b52e9014f59 | -15.08173 | -52.46485 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9872d548-9dcb-30fc-83dc-732a5ec27f6e | -15.79217 | -52.21148 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ba25750-9069-33f9-ae9e-b11277b3655e | -18.71257 | -44.27875 | 2025-09-15 04:51:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4431d411-d615-37d0-a823-6411dbfa6441 | -17.4066 | -49.26248 | 2025-09-15 04:51:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7419272-ee6b-3bcc-aa2d-4433ada4c422 | -15.79161 | -52.21511 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86c59f23-870f-34fa-ab88-79ef71ec9435 | -17.40277 | -49.26189 | 2025-09-15 04:51:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 223d6f69-1cd9-3db7-b304-fbf5563af698 | -11.28674 | -50.80308 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aa3e2c1-f30d-370e-ab7c-e12a69eb11e8 | -11.85371 | -50.51138 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f9e2ae3-2211-33c1-a874-4b39eee67322 | -17.14523 | -48.5176 | 2025-09-15 04:51:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdbf6853-02f1-3073-ac11-5e46e642ec38 | -11.27554 | -50.85352 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27faa9c0-e14c-3559-9f1a-1c2a7f838316 | -12.04361 | -46.53093 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6c67b44-1b8b-3911-940f-d2dbbb04e53e | -11.07478 | -49.72881 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34350ed5-ef80-3e92-8cdc-7d338f03eabf | -12.11915 | -44.82668 | 2025-09-15 04:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README48.md)
