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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d0f4f9b-b700-3045-a56b-eb8eadc582c6 | -10.09765 | -48.30021 | 2026-09-14 04:34:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331bed1b-1722-333d-881c-dfdcf93ae105 | -10.63573 | -45.99913 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c727a7b1-8f4a-34fb-98c2-dc826a3810d2 | -11.78405 | -46.39631 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d49b589b-b8c3-3dfd-8d78-4c3143be76d1 | -10.9577 | -48.36468 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b12c97f-a057-3011-8847-17179fc2bf7b | -15.54373 | -48.79148 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 54af6e3e-3ce2-3f57-acf8-905256ce28a4 | -17.35727 | -44.39839 | 2026-09-14 04:34:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e067343-491c-3fbf-80e3-12207990e9a0 | -13.30646 | -51.31171 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae7982f7-114d-3695-b4fc-7c458226840f | -10.74846 | -54.0876 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e060417-0281-3763-b8ea-5ca5e65eee7f | -10.68676 | -54.14974 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1bd70d7f-a379-3e00-95c1-7f39be433ea1 | -10.66553 | -54.15156 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 22070980-15da-3ffb-ba57-96476d57702e | -11.17884 | -46.38774 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37d2b128-ecbb-3b82-90e2-7f0c6a2a1b03 | -13.61865 | -47.90324 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3715ee5a-a351-3720-8312-d51adce15368 | -17.3537 | -44.39783 | 2026-09-14 04:34:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93de46bb-497e-3996-b9b5-37202a61eced | -10.10804 | -48.85339 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22b1ed4d-6194-3a95-bfa5-f257750ba59d | -10.43623 | -48.65623 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb78d74d-bc1d-3cab-8be0-2ba3a169f168 | -9.80049 | -55.30729 | 2026-09-14 04:34:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b4ad777-5bc0-32c2-a6f0-2f848dfbdfdc | -14.17699 | -47.39874 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef27beb6-5bb3-336b-90ee-1c058e1ca4ce | -10.67001 | -54.15561 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| a54efc89-e688-3cb7-81a9-b12db1ceeeff | -10.67902 | -54.16352 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 97afd353-b946-3544-aeb3-a71c32853f3a | -15.55534 | -48.78556 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c537291-be08-33f1-892e-c4e8e905ef63 | -10.56518 | -51.33073 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f74cb1b-f34e-3935-966b-7d050c7db911 | -14.81479 | -48.15371 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aae1f468-3dfc-33df-90e0-b5be483e575e | -10.5444 | -51.3021 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8380e7d6-ccc5-3d9f-b210-c8da2823197d | -15.55816 | -48.78985 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5971a2a1-d8c5-38e9-a082-fcf94540b647 | -10.10584 | -48.86627 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21b429cf-4e76-3e0a-b54e-06decb72c5a3 | -10.70364 | -47.52322 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54a07d1d-1cc3-344a-9c25-e5b8761c0306 | -15.25063 | -42.77335 | 2026-09-14 04:34:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 901814ad-b6d2-3163-a126-427eef9f90bb | -10.97791 | -51.44449 | 2026-09-14 04:34:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cd2d1f0-5fc5-3564-82b6-32ed9ad062da | -10.68578 | -54.17126 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e53765e8-6083-39ff-92ca-e56bc8b31438 | -11.21373 | -46.42616 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c10d5a9b-31e1-3a82-be1b-3e74b3da54ba | -11.37392 | -43.9511 | 2026-09-14 04:34:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6188a93d-c4b1-331f-8d1b-b61fee5420d8 | -13.31046 | -51.31247 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef5665be-d137-329e-a511-54211503cd19 | -13.58657 | -47.88611 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49a1fc18-5823-36f9-8069-1d72c75991a4 | -11.23097 | -46.4254 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 957e9424-76d5-33cb-98fa-384a42794a7a | -10.66211 | -54.14171 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 34dc1a78-dc7a-3026-ad32-519315ab2cb1 | -11.23176 | -43.43834 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e28a873c-55eb-3424-820a-a3c5da684a18 | -10.10681 | -48.86392 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ec4937f-9b1d-3535-aa8a-b31577f879ef | -13.32065 | -51.71729 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5174bfa0-2188-3aa9-bf90-5a3e8bfa59ad | -9.68339 | -54.84712 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebc86aa4-f6a0-320d-a167-0e3c880a5853 | -11.22487 | -46.42074 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b904a930-87a4-3708-ab30-ec91ebe47fd0 | -10.68016 | -54.14582 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96f0c615-2f43-353f-83f9-1df4d9ad1101 | -13.58596 | -47.88978 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 838fbed2-56be-3faf-83aa-5d4b8803021a | -12.39753 | -46.49402 | 2026-09-14 04:34:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b00a4ce7-cb86-3fe1-8a27-121fd6b26819 | -10.67905 | -54.15165 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 6b7f9010-51b7-365b-9d1f-d49544d03934 | -10.10366 | -48.85709 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d477aede-e751-3c30-b048-94a387eb7508 | -15.50536 | -47.90789 | 2026-09-14 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a2696ee-0243-3620-a086-d93830a227a8 | -15.0439 | -48.58443 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b337d8fe-0e18-3753-b33b-6df07b058334 | -14.17304 | -47.40185 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2fb7be2-ed39-3a26-8bbd-e101bab91187 | -10.68072 | -54.17034 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5fb18719-c112-31e1-bbf2-1f74d921daa9 | -15.04411 | -48.54124 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ae079b-f070-3de0-97cc-7cc35b2c06cc | -9.71571 | -50.84319 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 494f2bdc-28a8-3f5b-b4fd-ce040a934764 | -13.59458 | -47.87976 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ab2fe64-201e-34e4-8116-1dec4890adac | -11.37277 | -43.95864 | 2026-09-14 04:34:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 027af9d2-f9b5-36d6-8f31-4cadfa52e576 | -11.23468 | -43.4428 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 552eca2a-21a3-3dd3-82ec-0791f2b628d8 | -10.5421 | -51.31511 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72f700a8-02ff-397c-a1c4-a6b6d6ecdb6f | -13.46148 | -48.4704 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7744d99f-21e7-3e97-b27c-807c4d7e1f16 | -11.2182 | -46.41963 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7747f96-7cd7-3380-8072-9fbdbc244932 | -10.67613 | -54.15073 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fb39878a-b04e-31e1-969a-62de0a5a5352 | -14.18153 | -47.39198 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8d841751-dc13-3e16-b312-5e32e17f16a0 | -10.95418 | -48.36406 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a7e0596-973e-30b3-a406-48dd7bca2fec | -14.83421 | -48.14169 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47c63374-5fa5-3b4f-baac-e7457ce8eeba | -11.17921 | -42.79615 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 929c1b31-144e-3885-9138-3b2dfc8efe48 | -10.10752 | -48.85961 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd46d7ad-7e14-3197-85e8-7b270e56ee11 | -11.21763 | -46.42317 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d43fa5c-cd37-3979-8f7c-aaa7bb5e6bd0 | -13.59556 | -47.89503 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b455c9a9-fc37-3f00-8771-6245f77bc798 | -13.62983 | -47.90097 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f76fc043-1ead-3e49-890c-c294ff404130 | -10.91905 | -48.35865 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a710ff57-ea72-3819-921a-ca131cc1a6b9 | -10.64771 | -50.58189 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afc2fde8-53f0-38fd-9c03-7560f432df5f | -13.44353 | -48.47138 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e56f2fac-871d-30e7-b7c1-9f0e7369696e | -10.52127 | -51.36036 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 090a7149-77d0-3d6d-8baf-2af4646650ca | -10.6515 | -54.14257 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c9d07f0-e48f-31e5-ae48-905d3999318c | -10.66389 | -54.16045 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bdd593b7-b81f-38ab-800b-c48c1a9ff1f8 | -13.99389 | -52.52142 | 2026-09-14 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c3108f2-1af5-3070-a880-bde2b5621b8b | -10.6768 | -54.16344 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 6ca60fd5-3447-32bf-9269-a8c8300011a5 | -10.6738 | -54.1349 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e21b12ab-9760-3bbc-b08e-8d1e487928e0 | -10.6666 | -54.14573 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 4ec4d989-a197-337f-b214-cff61156bbf7 | -11.22185 | -43.43279 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b840549-0490-3fca-bb29-6d11435521d8 | -17.37047 | -42.61838 | 2026-09-14 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fc118b6-d7c9-3a54-8300-b46d24ca1af2 | -15.00668 | -48.51583 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e919ab4c-f92c-3f9e-98ee-86f888652ccc | -10.43405 | -48.64713 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b14dff3a-0941-33b1-8acf-e7062ae11391 | -10.73048 | -50.60887 | 2026-09-14 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06664242-5fb8-3ab8-80ce-ae1e3e70f56c | -11.20763 | -46.42157 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f07c0a5d-c0a6-3d5c-860d-35463d1d52a5 | -11.80583 | -46.59298 | 2026-09-14 04:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9e3ec91-18d3-3b0f-95c0-a4f2647633f3 | -9.59235 | -55.14776 | 2026-09-14 04:34:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a31a00c-0d40-317b-bbb2-c6a2ccbbe913 | -15.23845 | -48.06608 | 2026-09-14 04:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1839524b-949e-3dc4-86b3-9775652ca96f | -11.22885 | -43.43388 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 931e6c75-d34c-394c-b112-10c1c736eae4 | -14.82341 | -48.14375 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01dd0435-adbd-310e-9a6c-481b431ccecf | -14.17364 | -47.39818 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8129345e-9b4b-320a-8f1a-2edc9173c290 | -10.67401 | -54.15067 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 19c13121-4d85-31e6-b838-5d73d69fe10f | -15.56159 | -48.79045 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7475323-5920-39ea-8be5-9e1fa120b9f3 | -10.55178 | -51.30906 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76c88595-399e-3f58-8747-fc8cb9f7827f | -16.2286 | -52.64879 | 2026-09-14 04:34:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6d695d3-fbb5-3abf-b1b1-e3958bb28e87 | -10.65259 | -54.1367 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 017d3876-0d83-38d5-8de6-b1748aff7ccd | -10.47037 | -51.3295 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6f982e3-89bb-331f-a0d3-c071ca5edc00 | -17.83677 | -44.44199 | 2026-09-14 04:34:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6898862-48a3-3e83-b0cd-dd5cd0aee269 | -10.11171 | -48.85387 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c6d4d9d-f850-3965-955a-acf6d84385b0 | -15.2406 | -48.07409 | 2026-09-14 04:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 240a9283-6c30-330f-944f-6f9b91ef3a3d | -9.70921 | -54.37325 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0fdea64-4e5a-38aa-b4d0-d786ca7ba8ea | -13.56017 | -42.41637 | 2026-09-14 04:34:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3b832d03-72d5-3004-adfe-c0ac1a899f1a | -9.5525 | -51.35955 | 2026-09-14 04:34:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README31.md)
