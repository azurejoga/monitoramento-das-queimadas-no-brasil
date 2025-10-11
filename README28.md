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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44646f60-bc23-33a1-92ab-f227428cd3a5 | -10.52491 | -47.3438 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87b220ed-44d9-37da-a147-1dfa625f77bb | -14.65169 | -56.21077 | 2025-10-11 04:34:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 095409ba-9919-3da7-99e6-2d51a592f660 | -10.51315 | -47.35316 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9998ef9-f41c-396c-9b0d-c7c9393ac3b1 | -11.75534 | -43.31961 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17a58042-ab4e-328c-a751-ab76aad12f0f | -14.9633 | -41.68639 | 2025-10-11 04:34:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cfc894e0-32c0-3557-ad08-c32462db2a5b | -10.16414 | -44.60592 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f465574f-accc-392a-afe2-43f6cfe54a9e | -11.76321 | -43.32477 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 453f6990-d548-3b12-a738-5d6a760eb18a | -10.42541 | -44.99416 | 2025-10-11 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e2b78f61-92ae-3d66-a32f-df6aba4d5e8e | -10.16397 | -44.55329 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 809accfe-e77f-33f1-971a-a259619863ea | -9.11553 | -45.0778 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f92d380-71ca-3ab2-9b37-ddb5511e0bfb | -13.32346 | -47.12333 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e54bad6f-9370-390b-a2b9-6dcfeaa5d8b9 | -15.69572 | -46.63261 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49bb19c2-cb17-31f1-bbcd-ad5bf50d761c | -13.08227 | -54.84799 | 2025-10-11 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83fcf8a8-7d64-31a1-9b53-74846a89dac6 | -14.95097 | -45.58745 | 2025-10-11 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be3aa3df-4bf8-3c50-ade5-70fa147dc3f8 | -12.95427 | -46.47595 | 2025-10-11 04:34:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e8ddba-90ce-3e2f-b6bf-2ef70239c148 | -12.75017 | -48.66364 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3a86d97-ccec-3d36-8b0a-5a9cdcfd608a | -15.40633 | -47.29628 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92efeea6-84a2-3468-81ff-207635ec9ca7 | -13.28447 | -47.99338 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad59fb96-6829-3505-9ffb-986d1daa5397 | -12.22828 | -51.11797 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3a1a83d-1311-3971-883d-058a5835bf97 | -10.18269 | -44.58487 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b002bc63-a8a6-3f55-be6d-b5fec37685ea | -11.76515 | -45.04036 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0d6b746-5fea-3039-8290-77d0105976ad | -14.94296 | -46.74762 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55d6ef15-b37d-3ccc-85da-1e86bea1d5b7 | -13.40227 | -47.75102 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a06e321-b54a-3312-adec-7a2b1da40939 | -10.51762 | -47.3464 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da8e1d7c-91a9-3ccf-adcc-53120cb3c7d9 | -12.14597 | -48.01298 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b3658e5-c1c4-3d19-8e32-91d4ef5ceadd | -13.49923 | -43.66895 | 2025-10-11 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7c17522-447e-3e6e-9ab2-d29217afc1d0 | -11.75643 | -43.31172 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a6bd5c3-0ab4-3f32-bf0f-24b64a882050 | -15.23084 | -46.98339 | 2025-10-11 04:34:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbd9e5fc-275d-3dac-a1eb-e55728059436 | -10.52661 | -47.35521 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7677d9df-934e-3c2b-a3bb-7cb35dbb0f8c | -14.73217 | -47.4547 | 2025-10-11 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1197ff4-a0b3-3d33-b421-3cff4d68aadd | -13.29384 | -47.99062 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66275495-f116-3de8-872b-7a2a599b4839 | -13.31109 | -48.48671 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc120442-48ae-31a2-9c4a-dbe7d42e9c52 | -10.0727 | -45.92072 | 2025-10-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37b15a91-7154-36d5-b5d4-069b9a3ffb5f | -13.30166 | -47.98435 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c89e7f2-85db-3ce3-bfe7-4a8c79d9f01b | -13.21206 | -42.33762 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ff349dc6-9e31-3149-a9c0-7641173cad04 | -16.2516 | -44.04089 | 2025-10-11 04:34:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47edb0bd-4f7a-3532-ae22-e5f37895ed4e | -13.49309 | -48.1114 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3b57396-3646-303e-b6c0-f1530f5d4178 | -15.70297 | -46.63374 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f739f34-b742-360d-a5b1-bb7bce2137cc | -13.21229 | -42.33521 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 927f680c-c865-3e45-b0e9-d77c6206b129 | -13.3367 | -48.47269 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8874fb34-00df-3ac1-abbb-f851dc58f43e | -9.11981 | -45.07404 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e05fe7b-edc5-37a4-8ee1-9f7e60ee6d98 | -12.76017 | -45.88626 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63a4bee5-bac0-3b7b-b880-e675a735afe7 | -13.2956 | -47.12828 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce810367-8a14-3cc8-a5c9-15bf24523d4c | -9.52448 | -47.88128 | 2025-10-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe019e6b-0629-3dc2-8d83-cc66e037f170 | -13.3133 | -48.49451 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 572536a1-204d-3ea5-8475-1e07417c6a67 | -13.22582 | -42.33968 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03ad4790-7578-3c6b-9ed0-ff917736dbbe | -11.76892 | -45.04089 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29438efb-8f2d-36fa-85cb-7c4d4159fabb | -10.56093 | -57.51552 | 2025-10-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42caf52e-f016-32a7-a437-ba8ab9f26fd2 | -9.11145 | -45.05489 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe3e3435-2243-3c08-af95-3f96ba3a9f83 | -16.07312 | -47.76431 | 2025-10-11 04:34:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c181872-8962-3e38-9572-6f5fb43dd1a6 | -9.1097 | -45.04137 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aed281f3-923e-3c00-a47e-ce8d3fca8efd | -12.74545 | -48.64865 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2eb096c-735e-366d-97f9-ba1e05e6eeee | -13.33947 | -48.47692 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4310ca9-8fdc-36f2-9878-0cfc49203e31 | -14.7027 | -47.43855 | 2025-10-11 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17b531d5-21c0-37f5-b947-3ef8a5b98e50 | -13.45848 | -47.70667 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e9043777-3502-3d39-b4df-71dece56248a | -13.26714 | -48.01685 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15fe9c9a-6ca4-3720-bd80-1d52db28c00a | -12.90056 | -47.04617 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5658d9e-9920-3ae4-be55-2b6bf7eec26e | -10.20298 | -44.60337 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b94be4d-d7a7-311a-8177-da9ac15aa1ec | -12.24008 | -51.13155 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0eb3d165-d45e-35ca-b196-04f5e245f392 | -13.45958 | -47.69933 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ff0ed48-ca58-3b5c-a932-e763b2ee44b0 | -13.29284 | -48.49466 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa9f3d99-3305-3aba-92b8-d2163a62ae94 | -12.77831 | -50.47401 | 2025-10-11 04:34:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bd9c7aa-711b-3381-a43f-62c900469b49 | -14.65523 | -56.21594 | 2025-10-11 04:34:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b1605e2-d3c3-3bbe-8917-8f9a854a4701 | -14.94174 | -46.7561 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a361071c-0225-3b0b-a094-79215a14e4b9 | -11.78496 | -45.03997 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2fa52ba-f803-3406-959a-8095baff8a14 | -14.28577 | -45.9004 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d79a69c2-8480-3bbb-b6c8-7b233bdb2c48 | -13.3042 | -47.11808 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8002458-b571-379f-8ef0-0ad2687f84d8 | -9.26509 | -44.37246 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 271d5f4e-6155-3de8-b9ad-5112e1ee3abb | -10.52099 | -47.34692 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5677e7cb-3f92-3047-b929-f4f2d56a376a | -12.71572 | -44.93734 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6644485-8627-3c2b-84c8-64761124fc82 | -10.19473 | -44.60702 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb4275fe-013a-36e9-96c8-97e028bb3900 | -14.27347 | -45.87996 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94994523-5e35-3074-a1aa-8a7ab3b1e8d8 | -11.59306 | -48.75551 | 2025-10-11 04:34:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc795e2a-fb0e-394e-8809-d04b49a96512 | -11.7589 | -46.36231 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1afd5628-5dab-36db-87b3-13b3c1139c20 | -13.67529 | -44.28124 | 2025-10-11 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4d02737-4a9f-3486-9516-fbe1367edc68 | -13.33684 | -47.74824 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4294e6e2-b878-3edf-85bc-8dadb1f4eeb3 | -10.151 | -44.58953 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e7fe141d-93e8-36eb-901c-db8e6e1a2bfa | -15.22206 | -46.38658 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56f5489e-a784-3470-8051-81c46e757fba | -13.30611 | -48.49696 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 217b87fe-c867-350f-a0b6-248c4c747bc6 | -10.1737 | -44.53967 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1bcf5f5-a581-3cf7-8e37-bcb1b754541f | -14.9465 | -46.7484 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0a6bfd1-b371-31af-aa75-8eddbd45df0c | -13.08161 | -54.85171 | 2025-10-11 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5edab5c-a235-3530-a7e7-dea59e70fd5e | -12.71957 | -44.93791 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb12e6d7-c6f6-3642-bc5c-f74fa0dc850c | -11.78183 | -46.37751 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8c463dd-5a23-3f18-80c4-30d31a4fe66c | -14.01588 | -47.05921 | 2025-10-11 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c13caf28-9a23-32e7-a8fc-b295c30402fe | -13.00069 | -47.90828 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0d6552b-76e9-3448-83a6-560747679a50 | -15.82857 | -42.02582 | 2025-10-11 04:34:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8e0dcbf4-3f58-306e-bbea-2c9c5033feda | -15.03063 | -47.04333 | 2025-10-11 04:34:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50e67bf3-f6b6-37c8-bd8e-37fb38f3cbb3 | -11.91189 | -44.17786 | 2025-10-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 757ab214-7e10-3239-bc4f-623485841a04 | -9.0025 | -45.49685 | 2025-10-11 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea0f6736-a63c-3747-9862-aa9676f8202e | -11.72445 | -44.29181 | 2025-10-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 337d84d6-3148-3d27-8586-f0723f226f78 | -12.7656 | -48.65165 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dca28df-ef4a-3ffe-8809-fe292164d24e | -11.6283 | -55.01112 | 2025-10-11 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48e903c9-5328-3c37-a55c-186e0484d6f4 | -8.35889 | -48.6773 | 2025-10-11 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16ca466-4487-3706-b91c-72aef472860e | -13.22124 | -42.33899 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 2b29a31a-e6be-3fe4-8464-a7fc76224d77 | -13.66526 | -48.7484 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b394e733-8cc5-3cd4-9641-e5333ea3b2e0 | -11.87832 | -45.49343 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8839846-c7bf-34f7-a990-c84f6a7bdf30 | -13.25704 | -48.01542 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27f14ac0-22e3-34b1-b351-c1262bd9713f | -9.93209 | -59.92183 | 2025-10-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c59fe280-5c3e-3d79-9fdc-baf1aeebaff8 | -14.92929 | -46.7666 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README29.md)
