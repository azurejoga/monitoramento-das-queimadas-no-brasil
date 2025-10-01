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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d5ae1ac-01fb-3aaa-b77b-e8af346e259f | -16.37464 | -47.03191 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 267a7035-1565-3003-8fda-e03aae93bf3c | -14.95368 | -47.51528 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f063170a-6bbb-37ae-8bb1-757aae7fc63c | -12.86961 | -46.89945 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d188f39b-1d94-3e2f-b932-7d5b870b447b | -10.94903 | -46.53996 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0ae2cfd-aae9-37b8-be37-a6fc91ba4fe8 | -14.72044 | -48.1394 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a634908-f07f-3ece-88d6-3f7293050050 | -12.82057 | -47.01549 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 241d4327-a49f-3b84-830d-3fbaf1530702 | -16.38505 | -47.05199 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992f7424-a49f-3704-90b9-ab82e4a89411 | -12.77566 | -46.86959 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8727f833-2993-3544-a0b0-6d2aacce8746 | -16.24375 | -44.05909 | 2025-10-01 04:21:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffefe8f9-5436-346e-90b5-429b579a7b78 | -16.37184 | -47.04977 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 413c7aa1-9360-3638-b2a5-2885238f51c1 | -13.67096 | -48.06182 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f2743b4-8901-3ec0-9323-660b9cf0a46a | -13.53375 | -47.26157 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0471f556-af67-374f-a216-88c6abba3954 | -11.75303 | -46.83553 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8476308d-281f-300a-a2de-1db2572c4307 | -13.29936 | -47.57771 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4aa40161-ce37-3629-9fdb-8adbf511b6a7 | -12.86172 | -46.94926 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58e356aa-0825-3e6a-94ab-e8b163cf53a6 | -14.90074 | -48.11655 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a98e1f3-89a1-34a4-99e6-c96e46fda31a | -13.78529 | -47.98525 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 137ccb02-2379-3242-9424-b66f2ceebe72 | -15.72999 | -48.88992 | 2025-10-01 04:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d048d21a-5f68-31e3-9c89-63469a78e645 | -9.41834 | -54.70675 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c5f0d7b-a0ba-394f-92b2-196162d2ee7e | -11.84419 | -44.98934 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ec9f977-8058-3245-8da0-c2f9f4125719 | -12.22139 | -43.74375 | 2025-10-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6dd792d-5e0a-37e6-8c53-44af3d5cde87 | -13.30304 | -48.69906 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37f3e124-d95c-30ee-914e-155adbaafd1d | -13.37656 | -48.10414 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2099454-bf16-3b0f-ae11-213caf387dac | -10.04106 | -52.10345 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4240b57e-5b84-3eee-81b8-81bfec4695fd | -15.00868 | -46.9755 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1442303-0a70-3de6-86f5-14d22e3a6a28 | -15.40181 | -44.98071 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a5def06-5ee1-3608-bef4-4fade643f6b3 | -13.76381 | -48.40087 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 799860e9-a998-317f-92b7-a403e85ff895 | -14.03337 | -47.98212 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba7ee98e-e896-3889-b8b7-18adf039b66f | -13.10269 | -47.04044 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 856a9f2f-9506-3af9-8d32-a7305380cff0 | -13.82148 | -47.50518 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88f2b797-516b-3f16-8927-d93da95afde3 | -16.0299 | -50.89254 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56dc481f-0115-3cb5-aa4a-e353ff0261ac | -14.54625 | -48.22057 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ce084b1-262f-3bf8-8470-5a2b41e5d30c | -12.01355 | -46.63133 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8abe2888-8a1a-3403-9576-24cd152a6e88 | -11.35678 | -44.97491 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3368ca2-0886-3c4c-9ee4-fe37cf2ec040 | -12.23064 | -47.8212 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 577f869f-99bf-34e3-974d-3d8124f270ac | -10.04101 | -52.10188 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c700d94f-354a-329f-9b51-90279f4d4ed0 | -17.40084 | -47.16737 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c51aa44-249a-37ff-a628-1bbf381c3e4c | -13.36115 | -48.15545 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ef28d3b-f59b-35c3-861a-e5409441a88a | -13.5378 | -43.49832 | 2025-10-01 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55dd1b92-22d1-3711-bc0a-1133fcfe6f55 | -12.66 | -46.93439 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87ece48f-e583-3cf9-8d52-f29f5984e526 | -13.22504 | -48.44694 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27d0f613-713f-3cf3-b8d4-d74f7f1add75 | -12.97598 | -48.42129 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 190bf3ff-f363-3e2d-a9d1-9486f703c8d6 | -14.14012 | -49.19679 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da2a7148-0dbd-3cce-b140-820f1cb7a148 | -13.67914 | -51.22606 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76852020-c58b-3abb-8a3d-00db70d90d55 | -15.25606 | -56.78086 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07e4b138-9c9f-326d-8684-879599c0bf05 | -10.62478 | -48.59207 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac9a2821-2e02-306a-8249-4582c98fc03f | -11.5685 | -50.19137 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9c3a7b2-4776-39db-99f8-612af970e63c | -11.82804 | -44.96124 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8423f28-4ba8-3fe2-8869-2be7e2ebd70d | -11.81835 | -48.25452 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d0237d2-a025-3086-a3d9-4f2aa5ba47d2 | -14.69475 | -48.12753 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5555cc1a-32b8-3074-b9b1-a224b568cf39 | -12.71262 | -46.90296 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10005fbb-58fc-377a-a228-38af77b2ab78 | -10.38418 | -52.03449 | 2025-10-01 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 371eead5-3aaa-3ff8-9e21-c3b0abdd9794 | -11.85143 | -45.00875 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efca8985-c294-3990-afdd-baecd327d68d | -11.84305 | -44.97453 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 268dfa60-f590-3ed6-ad93-6bd5118165bc | -14.73135 | -46.83464 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2cd81497-7d72-3dbc-8a01-3dbcaadbc688 | -11.82695 | -44.96836 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac9f2643-750a-301e-9921-245e630ab0f6 | -14.89554 | -48.12721 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b399aaa-dceb-36c9-9f9e-d72ddca2b39b | -12.35717 | -43.21289 | 2025-10-01 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5706f70-7801-3c7a-9ed8-7382d66c6e0d | -15.47133 | -45.87664 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f5b2f1c-c304-39bc-b603-186e35ca9021 | -14.0496 | -47.98857 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b884cbfa-9f76-3f0f-be17-00dec3a59184 | -11.83246 | -44.95463 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b0cbd95-cdc9-33f6-ba4f-7593646efec9 | -13.6511 | -47.20868 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 654c89f3-b40e-388d-8d77-6dfe07ff3364 | -14.68416 | -45.19191 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e6a5b16-3559-3926-9d3f-4cf17db1839a | -12.92609 | -47.20847 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f251d8a2-d2a7-3aac-a139-586a0e4f9faa | -13.81455 | -48.02905 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ec4cd2f-17c7-3575-bb39-341e335d7adf | -15.75737 | -43.68881 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd0410c-027d-33ed-8d31-8928e318a104 | -12.95387 | -48.42992 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef6aa4f0-faeb-380f-8f54-8ec27a94c027 | -15.61831 | -46.9088 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7586f6fc-1660-32f3-b9b4-c2f98c42f6f2 | -13.15185 | -47.4122 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9b62b60-5d89-3e88-bff6-fb6864bd524f | -16.36652 | -49.12304 | 2025-10-01 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af430ac6-c12e-3dcf-a2cb-929196d85810 | -12.84986 | -47.02393 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24ce7f02-8ee3-35fb-b246-7a67ace2d8fa | -15.15279 | -48.01291 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 911966b3-19bc-39f1-989a-568cd0a2b9bb | -12.1611 | -47.77155 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9507070f-362d-3ef8-b42b-0a0abe6d4160 | -13.77638 | -48.3248 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 011800a2-917e-3dfa-9831-d28a9a72cc20 | -12.84929 | -47.0275 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e550b614-caaa-3117-bbe0-5bf11d2c5e89 | -14.71768 | -48.13512 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dce70db6-2769-3d34-b5db-13c60f500d1f | -10.66684 | -48.53584 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75c25680-9443-36db-9b01-8169f239161d | -14.35039 | -45.91748 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9009d0b7-e6ff-34eb-8f64-47a2fb6b4def | -12.83707 | -47.04015 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2e7535d-4219-3025-bac7-f326cba54047 | -12.77635 | -46.8879 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cf42b47-83c0-3a29-a7bc-4392c0e4eea8 | -12.95569 | -46.41821 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76105ffd-dee1-31d5-87df-4162baf1eb6c | -15.12819 | -46.44926 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14c4ef91-ad93-3171-8412-c79f63f090da | -15.03085 | -42.33025 | 2025-10-01 04:21:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3a2f194-8546-33b1-b63e-543334bf0725 | -12.43105 | -50.17497 | 2025-10-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a737fbcf-999c-3d7e-a9a3-8593279e05b6 | -10.17439 | -44.90346 | 2025-10-01 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48b7a505-eba9-3727-8b15-a527c7bec424 | -11.76176 | -46.86622 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ca60514-3d99-3810-b405-d7609756f69f | -12.66394 | -46.86551 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 012c65bb-76a8-3617-8cbe-3c77b3da5112 | -13.80937 | -47.49548 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16b91cbb-3bf8-32d3-be72-1f335a6df7ee | -12.76285 | -46.90759 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feba316a-32c7-3e87-8d9e-010420ebffcc | -10.64538 | -48.53278 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 468fbc3e-7f85-35b1-8340-5c7f66d6c8c0 | -14.71158 | -48.13019 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26a71664-dc31-3a3a-8e77-44c9a51a92ec | -9.80263 | -48.97733 | 2025-10-01 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4091d65a-aa8f-3002-8a73-12b891d3d9fe | -11.4417 | -43.50187 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4c2347d-369b-3a20-842c-11b9771f46da | -15.47909 | -45.87043 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc0103f9-e223-3673-bad7-3e7122da3d6d | -14.02268 | -53.88964 | 2025-10-01 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9e32760-2d06-3e80-a936-5fd7b49981fb | -14.90624 | -48.12506 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d72e693-fb58-37aa-893d-319a9faf02d4 | -15.55032 | -48.18609 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d08a7cf-d4a6-3caa-a997-3c6472026a70 | -15.24632 | -46.97827 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d063abc8-5718-3b02-9100-946c9093443a | -11.46778 | -45.07196 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d5a5a76-9049-3460-8922-130247073759 | -11.47616 | -45.10593 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README65.md)
