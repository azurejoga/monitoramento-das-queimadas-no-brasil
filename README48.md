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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18aa3911-8487-3eb8-8c06-ca484c492145 | -12.9873 | -47.97574 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fa1d736-4b80-3429-b25c-1ed6fdbd6523 | -13.76304 | -48.77109 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9f9b340-774b-31f9-964a-ef8e95f541d2 | -12.43626 | -46.88675 | 2025-09-15 04:51:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31248546-b0a7-3654-97e7-0014b70c64fd | -15.7826 | -53.46797 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69915afd-b854-388f-a5e2-1eb78f7dc971 | -11.73226 | -50.46247 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef990604-0b8d-3867-b385-fa0736fe2115 | -15.8951 | -49.9838 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba42debd-1c61-386f-9bd0-987954d3a582 | -11.78009 | -46.66797 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4578abd7-066a-35c8-bf5e-32f245644b1d | -13.87753 | -48.2989 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5654c411-912c-30da-9c0e-cbb46cdb6c62 | -13.93456 | -44.80107 | 2025-09-15 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d75d390e-f0b1-3bb4-bac0-0994e45d4ed0 | -16.70711 | -54.96676 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5f0be42-6156-362b-8308-7c68afb345f3 | -13.9101 | -44.82349 | 2025-09-15 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 901a4741-e576-30bf-b1e5-e808582a0fb4 | -11.27948 | -50.85041 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4770256a-56cb-3349-b432-c0997ad78e3f | -11.80019 | -50.49993 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d88592d-efb6-3d5d-8e2c-4fee108830d6 | -12.00576 | -47.76021 | 2025-09-15 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 63eccc2c-0337-3be1-9c2f-e17388f3e2cf | -11.86056 | -50.51245 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5550dd44-b5bb-3521-a40e-7c6e0f82a792 | -11.2945 | -51.14081 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aefcedfc-8430-3857-a2bd-8a67088185e6 | -11.7819 | -50.43567 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b63b1c5e-1ef9-3e7b-957e-f8ed1c14ca80 | -10.32578 | -58.73114 | 2025-09-15 04:51:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16faf17c-7fe5-39a1-80f6-7f7bdd9cceb0 | -11.12888 | -47.65555 | 2025-09-15 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bc2e71b-2938-3b36-8b2c-3e553e7ac649 | -17.2411 | -49.4707 | 2025-09-15 04:51:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6018341-94e1-30ce-ad23-219a334a0b8a | -11.74652 | -50.46087 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43027f51-1e27-3462-8393-a178528fa397 | -12.01264 | -46.66154 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ae654a3-0d51-3ddc-a02d-be6a3f8ca5f8 | -15.89459 | -49.99074 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 079772e2-8af6-38a2-ad6e-6f9700c29ae2 | -13.18889 | -47.28864 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 622cbe8a-922c-3381-9bad-e3765f582381 | -14.39861 | -48.35992 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0196217-8284-3710-b1b2-cfced1bd350e | -11.7661 | -50.79064 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce520fd4-ba68-3fdb-a7c8-ea20886f8820 | -14.33861 | -46.0891 | 2025-09-15 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eed60ee-e583-33f5-9246-8f5208183bd5 | -12.9912 | -47.97647 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ca21eee-cab6-3086-9b5d-93c36613be7f | -14.63647 | -52.01524 | 2025-09-15 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ea6cd9b-db92-304a-9e78-7a889588fff1 | -10.92397 | -61.96422 | 2025-09-15 04:51:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1f5cdb0-2b35-3d06-881a-51117d32bdc7 | -16.65866 | -49.76157 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c647c41d-ed25-3aa0-abbb-efe0b97815c5 | -12.01683 | -46.66224 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccbb3297-5baf-3ec8-8e2e-1b93e9b2c163 | -15.78937 | -52.20722 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77585b74-1f67-3c2a-a70f-dc25be5198a2 | -11.29786 | -51.14134 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c3db7f1-5582-38d2-94b3-04b984026eaa | -14.50075 | -47.35397 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4e07539-a63f-3e9f-847f-bbe28c52ce04 | -15.71378 | -53.06958 | 2025-09-15 04:51:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e8e5eac-926c-37cd-b425-babf9f8a6152 | -11.12964 | -45.31844 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b72dd2f7-2dc8-3718-b2d6-8d1976a108af | -15.79104 | -52.1963 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 161e77f0-aaab-3044-bc5b-dfc9b3f1cdc5 | -15.10174 | -52.4826 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db4fe5c9-d94e-33a1-8d68-294f811c7946 | -16.57993 | -55.16418 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dd428679-b511-3527-9a1a-ea886b1d5220 | -11.79619 | -50.43405 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ca1a194a-f2d9-39f4-a85a-60b0e2fa31ec | -15.08117 | -52.46846 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a6f6bd7-f845-38f6-8f3f-549657397961 | -17.33679 | -42.6471 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38906c3f-d6e4-3d53-98f4-fba389a73dd0 | -17.34311 | -42.64357 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e08fef9-fd31-3816-a257-3dec65d944e7 | -11.9922 | -46.65446 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e673e64e-a13c-340e-a07d-b1f08c2d8692 | -11.29841 | -51.13775 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fa40449-0a7e-3c49-898b-e941fe35fe0a | -12.96702 | -48.00692 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3ef79fc-77bb-3064-9d9a-760ba86964bc | -11.76391 | -46.66142 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aba3a1c2-7e37-32dc-860b-5a8d252488c9 | -12.95922 | -48.00567 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2b9fb037-8ef3-3d7f-bdb4-e1b3db72f305 | -11.07828 | -49.72936 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54d7f85f-b98b-3600-9912-0476c999ba94 | -13.93035 | -44.79482 | 2025-09-15 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fd1dc53-0152-3393-a958-4815289fd4b4 | -11.78933 | -50.43298 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 84082c79-ae3b-37cd-b521-03a279aa5cce | -11.48108 | -43.59982 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 446913c8-f9e2-3a66-b5a3-728fd7d0075b | -13.18983 | -47.2817 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bca0029-139b-3950-85a0-a9290accb812 | -15.78713 | -52.19934 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19f087a2-70ee-3799-8503-263b21154175 | -14.80349 | -51.60659 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3618652d-b5bc-37d5-a42a-c921e7596153 | -11.08465 | -49.71318 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15e8ebb1-59de-3cc8-a0eb-ae5a699cacce | -15.77984 | -53.46381 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0240e006-cb91-3822-97b9-f84cb8b8a3a7 | -12.40907 | -63.89435 | 2025-09-15 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f1c1c9a-a04c-3b88-845d-ea34b492dbea | -12.04731 | -46.53545 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2923bd48-e67c-330c-8905-dfcb5f1759f2 | -16.67156 | -49.77711 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4af7cdc1-d616-3bb9-ab2d-8a699f313016 | -15.76546 | -52.21817 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a068918-8276-3274-a337-bb2905257d1c | -15.89382 | -49.99253 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1166c110-d9fb-33df-ac18-f339d371f81f | -11.07247 | -49.72048 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f767a6-e9be-3f36-a1db-6c8729dcb91e | -14.50714 | -47.33809 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 818d6bbc-bc93-3c11-a74e-9a2691733da2 | -11.85773 | -50.53117 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d07e210-d938-3cc5-bbc7-713deae3a34e | -14.39087 | -52.89875 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50d71998-1a62-3ed2-bed5-da426f9d6d6c | -15.79041 | -53.4619 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 23cbf852-6039-3a32-b289-1cb7b7c8f68b | -15.8011 | -52.1981 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fcb7d5e-42aa-37ca-a1e9-e8faf4857197 | -14.81761 | -51.6278 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 17d34380-5577-3196-852f-308adb41d487 | -11.31576 | -51.13683 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 274ababb-a691-3eaf-a182-d447a8b9e519 | -11.61061 | -46.58972 | 2025-09-15 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9aea771-079a-3737-9939-b5d34750c1b4 | -13.94566 | -47.94598 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 557080ee-91b8-38ca-a000-61f1a33a2483 | -10.9247 | -61.96051 | 2025-09-15 04:51:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fb03a53-99d1-3930-ba64-e3e2dc2cae98 | -15.8952 | -49.98637 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 63a312b1-4aa0-36b6-b109-dc22d462cac4 | -11.08006 | -49.71764 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90919f60-863b-3307-8123-a88865c89658 | -15.42283 | -52.9846 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87b62896-7932-3433-97ec-a35d4598f5de | -12.12198 | -44.84228 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f591931-063d-3610-a4d0-5e04ab5a0b3d | -15.76095 | -52.2474 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09135b0f-fb55-3e14-a499-6f3b9e18b3f5 | -12.95985 | -48.0011 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18a73b74-dee1-3f14-899a-c8fde8c3ce96 | -12.7613 | -48.70614 | 2025-09-15 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d6e7f6e-2779-37f5-a049-1960265bdd28 | -17.1445 | -48.52305 | 2025-09-15 04:51:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e52f36d-f83d-337c-ad37-f875fa4072fd | -15.76881 | -52.21873 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe280c3c-9475-3bb7-92ce-16c15563bb16 | -11.2761 | -50.84988 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4b511d9-a114-38d9-bf69-443289ba7380 | -14.63648 | -52.03757 | 2025-09-15 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccd7af9f-e700-3f72-b9a4-65500b6a3a0a | -15.78993 | -52.20357 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2274ee89-cc1d-3d62-8301-a711ea822b19 | -13.748 | -48.76847 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eae2448d-0918-3bdf-8c26-48b275a93b25 | -15.25374 | -43.09089 | 2025-09-15 04:51:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 117e8a5c-1cd6-3433-b474-2f68ed640e66 | -11.08173 | -49.70872 | 2025-09-15 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1916e7a3-d77d-348c-be49-a66957958b22 | -15.139 | -56.15564 | 2025-09-15 04:51:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82b7f876-e153-3742-b0c3-3db66fe07203 | -12.44434 | -44.74694 | 2025-09-15 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 819a3095-bf2c-3e7f-804d-70770484a354 | -15.66589 | -52.23917 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c713c85d-673b-37cf-ab86-37ad9eb74a70 | -8.45118 | -64.1401 | 2025-09-15 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef7ffdbb-3284-3d09-a9cf-6935c65f15fe | -15.69598 | -54.33707 | 2025-09-15 04:51:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd6bc3bf-2259-3976-949e-1760155494c9 | -11.073 | -49.74051 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bc067be-6e11-3a5e-adc8-7c5180a1a29c | -14.47349 | -55.96103 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 258c2129-0821-3d9e-999a-690d9e9f31c1 | -11.08125 | -49.70981 | 2025-09-15 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e0e91ba-63e5-3b47-8acd-d7fb135b3f9f | -16.58271 | -55.16863 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 04ded641-d92d-3c0d-bdca-2a9ad8084a57 | -11.71572 | -46.48388 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e0fd3b2-f0b7-30ed-8596-0146a6ca8d6b | -15.75649 | -52.23167 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README49.md)
