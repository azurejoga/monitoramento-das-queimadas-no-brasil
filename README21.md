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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af9c4469-7d2d-3bb9-8425-7ff2ff40e6c8 | -9.84061 | -48.31958 | 2025-09-02 03:51:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37f2ed65-770f-3fa7-ab0d-d0f52f9483d2 | -8.70228 | -50.44421 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cde0bbe-9175-3be3-b091-18238a7ac4d9 | -8.46033 | -43.61961 | 2025-09-02 03:51:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 832c9ec1-f227-3b59-97f5-1e14c27ac55a | -10.05213 | -48.1465 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e1b90bc-1201-3b3f-8822-059f5b384b54 | -11.09414 | -44.6635 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c4ceda2-888c-38e3-ba40-5638d10d3efa | -7.79017 | -45.45385 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c05066-e478-397e-af01-1b266a8eb7cf | -9.73363 | -48.97459 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5577d584-0c2d-3e0c-99df-5b0a8bd7ddc2 | -8.13165 | -49.8358 | 2025-09-02 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e5d14fce-41ba-32e5-8e23-258139fbe013 | -7.92325 | -46.44847 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62f1f5bb-45a1-3f47-95bb-539abefbab74 | -13.89771 | -48.08363 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cca98152-80bd-3630-aa88-5d987bb5991f | -14.49583 | -45.94895 | 2025-09-02 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bce72fd-ba91-3a7f-9925-3a0f03bae7b7 | -11.65994 | -52.1833 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e919325e-d8c8-3f68-94f4-560576f1bd42 | -9.72836 | -48.96874 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a6eb776-76bd-3b6a-b381-077c81023f64 | -14.27057 | -45.24829 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1d2460b-706f-3e2c-bcec-685cf60e0ee7 | -7.55804 | -45.69775 | 2025-09-02 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22b7f31d-0d2d-3e4f-8c97-e5a2c6301213 | -11.97562 | -45.86959 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3840f2fb-cbd0-3e23-92a7-0c6d8c56388f | -12.94839 | -48.09104 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2521405a-e84c-3511-8ec6-814189bff542 | -11.91813 | -46.45507 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e3b7ef4-56b0-34fd-b2fe-8db6624c2293 | -9.72557 | -48.98319 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b2cbe8c-0544-324e-b8d7-faf701f6d020 | -13.59127 | -48.13986 | 2025-09-02 03:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ce330e3-ec0d-3cf3-8ad5-a831426ace9e | -11.64754 | -52.18091 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 5b5eafcf-b618-3da7-bf70-0e05d3dd4c32 | -11.85726 | -46.72023 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b66fcf0f-793f-379e-9d0a-9da256ba3ef7 | -12.94295 | -48.08957 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecb1c2a0-06be-3384-87ea-3e072b7f80f8 | -11.66754 | -52.19241 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 33a92781-7d94-3416-9950-61a20c39c554 | -10.28692 | -47.51934 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec657e2c-03b0-340c-9561-a5901598fba8 | -13.89307 | -48.10716 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e747f849-3987-30ef-a1b0-a7f1d5cb4a4d | -8.86186 | -45.79021 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d169f026-a0c1-3b11-9592-cc1d7e3eb13d | -11.04669 | -45.14927 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70df8e6f-dfae-3235-8c1f-6d30be831dd8 | -12.95308 | -48.09165 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daddd4d6-053e-3aa8-bf85-d4794b66f77f | -11.05629 | -45.39087 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67c7be73-15c2-3ecf-9ac4-96b9161e329c | -9.83552 | -48.61301 | 2025-09-02 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4059f62a-9ec3-3e2c-84b4-e2b38b0dc44a | -8.86755 | -45.78794 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25150dfe-c6ac-334a-a54d-10c8a17bab4b | -14.60607 | -48.03968 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09a4ba01-d527-328b-afe8-8725b42a1151 | -11.67707 | -52.2178 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 3c8f6c35-260a-3317-bd65-6823098a9f11 | -11.66198 | -52.18348 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e8a1771a-8874-312b-8c05-aa0c7a592311 | -11.65874 | -52.19842 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 52aa2d29-3511-3eff-827a-c088a5443a9a | -14.72366 | -46.75126 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6697e3bc-f4b4-3fe1-aa83-e6cfa02ae5cc | -8.19055 | -46.77979 | 2025-09-02 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c34778ae-1485-31bc-bcf0-1cbc6c0e36f3 | -11.4405 | -46.81298 | 2025-09-02 03:51:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0b1f5bc-cdad-3816-b540-9960cf502961 | -12.64513 | -48.2453 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08680de3-8539-36d5-9879-f380c95bf227 | -7.98312 | -46.46312 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a334802-953c-360f-9bff-13a22f2184dd | -9.73079 | -48.98937 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 89bc09c2-06d2-33a8-a4cf-ccb7156e8e9c | -13.28102 | -46.89079 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0068b9db-7425-3cfa-9cc5-5e8f412ba15e | -10.05086 | -48.09775 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cbd8e2d1-7df9-313c-b4b2-875411b4f854 | -13.32557 | -46.83693 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 911d0323-ce3f-3eeb-83b7-5423e900f05c | -12.76093 | -48.08952 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9054b8b-402b-3322-967c-0fd14c0731ce | -7.53704 | -45.35632 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50b12667-d9db-3425-b7c3-1d9e6ba81b12 | -11.04763 | -45.14421 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c700d397-1e07-3c3f-ab1a-bccff9ac9d2a | -13.28408 | -46.91442 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a9b21cb-5fd3-3e9c-a348-cd948bda7c81 | -8.84123 | -45.77359 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb132f08-98d8-36c3-9377-13ca6e3e4019 | -11.64463 | -52.04373 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8cc3a76d-ddcd-3ff5-bd7b-f59978019c4d | -7.71394 | -44.61048 | 2025-09-02 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af9537cd-877c-381f-a53e-90791744af26 | -7.48886 | -45.36236 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b13b02b-b695-3695-98eb-8a91a628cf31 | -12.85441 | -48.05197 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e50a89a-599d-31e6-9e15-48bf9c546a39 | -11.05535 | -45.39603 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2de58755-85a3-3783-83ff-bfbf25101091 | -13.49452 | -46.93128 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe56683f-fbd6-30c6-94a3-26dc694d56c1 | -11.37473 | -43.56466 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28b551b5-96b7-3f7f-87f2-2253ff65a22c | -10.05568 | -48.10419 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9e392470-2b74-3d38-8267-e01def9e9e96 | -7.77543 | -45.4483 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99244d1a-73fa-329c-8bd7-d9faccda8e80 | -7.98012 | -46.47472 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0c26d6b0-01e8-3385-b1a1-92ac6fc64a36 | -13.36411 | -46.93715 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b9120e52-4dea-3937-8e99-98a440ade298 | -13.5038 | -47.00435 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c1c21ed-1418-3681-9eff-98d400e6f062 | -11.0909 | -44.62907 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed2082b4-a487-36aa-aedb-3f745d50de55 | -12.8059 | -48.06558 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb977967-73e2-374e-b459-926c030bbecb | -7.9858 | -46.4789 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f1a7e7eb-fea1-3347-bb5b-cc76280b4e20 | -13.3342 | -46.84649 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8109a66f-1256-357b-aa44-6f45ca72d7ec | -11.66667 | -52.23118 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 0a0bde20-18cf-3617-bd3c-b1ff2205cd47 | -11.09746 | -44.64489 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5abaad0a-b70b-3dd0-b7be-67ffd34467a3 | -13.70209 | -46.89333 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc96c0c2-b1bd-3656-8ef6-32e020575b86 | -11.88597 | -46.68129 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e429cccf-5e64-3a0f-bfff-ed160bc8d044 | -8.46472 | -43.62063 | 2025-09-02 03:51:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5acab27-c783-3db2-b842-16937c7506d4 | -10.05742 | -48.09486 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ee09cc19-80df-3333-86be-5186e0f1e84b | -12.43754 | -48.71902 | 2025-09-02 03:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf4aff4b-baa1-3476-b5e6-fbee639f8255 | -11.4478 | -42.93549 | 2025-09-02 03:51:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3590f5c0-af0c-310b-ac00-6514134a247a | -7.4912 | -47.87821 | 2025-09-02 03:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4182a401-9d41-3f3e-b3f9-bc41cf157a1f | -14.60681 | -48.03604 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0789fcf-9d70-32f8-8c63-fe33dea49672 | -11.35437 | -43.67972 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e137986f-77f3-3070-b51a-58e48cafce7a | -10.75479 | -49.58106 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc7fbf53-528b-36aa-962c-743781b67955 | -11.06114 | -46.9087 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c19acf92-dc98-3124-9b6a-332aaa615441 | -9.48371 | -46.51107 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b0efd90-f3c7-3e8f-a7cb-ed81ac20709a | -7.63204 | -46.55566 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2f1d109-c5aa-3f16-8538-bf2502105308 | -14.05333 | -44.5549 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ad08880-3de1-38d4-9a13-de26695407bc | -8.15007 | -42.47196 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00f8ca21-da35-3952-ad7a-1973aa78349d | -7.97973 | -46.48138 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9c6cf570-bac7-38f7-99ca-ef79b6102ba2 | -10.75063 | -49.56919 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ade3fe5-3d15-3525-b582-b9db69900a92 | -11.6707 | -52.17782 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4e78b66f-7f8e-3cac-bca0-1a4ccd95bff7 | -7.98442 | -46.45612 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 175e40b9-9c15-3d5c-abe6-03b7fceed44f | -8.88646 | -47.97319 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e4ca80a-804d-3034-a279-ba59f47f328f | -10.05516 | -48.1309 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e848a35a-8f88-3538-8e12-536850876daa | -7.55748 | -45.7009 | 2025-09-02 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12e27cdc-8d40-33c7-aeba-1cda8ea560d7 | -10.45433 | -49.06285 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1321383f-b565-3eeb-a839-4b5f2e4f86b4 | -11.67207 | -52.23279 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 748bcb9f-eef3-3f56-bc79-5a67fbe15850 | -7.98125 | -44.05728 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5302502-f2a0-3137-9ad7-aabf63661382 | -12.06402 | -43.29094 | 2025-09-02 03:51:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b25633dd-8571-37cc-9031-46b1251187bf | -7.47603 | -45.37559 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaaf38d9-1df1-32ef-a8c8-98e13c18e814 | -13.30654 | -46.83902 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55b5b209-9bec-38dc-9061-8ec3eeeacfb1 | -14.59462 | -48.04141 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 880997ae-a405-3604-9960-a9cf6039347e | -8.83853 | -45.78868 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db817393-99b8-31b0-baf0-aa84103eb7a0 | -7.98807 | -46.46151 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7dc2eb9f-4ad9-36c0-bb5f-e8c246377aca | -13.28677 | -46.92762 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
