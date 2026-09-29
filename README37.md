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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba46fa69-2da2-3ce6-9883-bbe69cc8cc42 | -5.73458 | -45.17471 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84bd9381-c4d9-37ee-9f0c-aef0351ea3ae | 1.67527 | -55.90462 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89b13549-bc7d-30ed-9932-4920bb10e7a9 | -6.05329 | -46.15747 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a56b082-e2ac-3e70-99a0-49dea3d2b8a5 | -2.90617 | -54.09331 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 171e7a39-c584-3c4a-a12f-fbf645e8e56c | -2.29803 | -48.54615 | 2026-09-29 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49635700-91e2-3dd9-b95d-ed303f34b4bb | -4.45692 | -47.92185 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6e6f44f7-4854-3708-95c0-3a166d0f67f6 | 1.04037 | -50.02034 | 2026-09-29 04:49:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5646c854-7f0f-3300-83b7-885ae1f77de3 | -5.43196 | -43.44797 | 2026-09-29 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cac7fd7-ed4a-3511-915d-da8709e8ceac | -5.61031 | -44.99972 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9499b351-260c-38bf-93bb-996756de9bd4 | -6.13952 | -44.13905 | 2026-09-29 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23e01d9a-36b5-3afd-b368-7d5694f6e0bf | 1.67347 | -55.89284 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e6b8d09-4d17-3d6b-b2ab-758f3d40b33a | -3.15782 | -54.08281 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b27ad394-7a5e-355e-8dda-e4967d4c1579 | -6.12882 | -43.73534 | 2026-09-29 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d89ce5e-50ba-3e81-9a27-1600cd9d5822 | -3.88847 | -49.50377 | 2026-09-29 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bb28c09-648d-3a65-bd8b-904718a4f0db | -3.14537 | -54.08062 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8daf206-a36e-37a9-9b14-d67aa5afa2f1 | -2.5774 | -50.78727 | 2026-09-29 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81e6ea93-6897-395b-b913-102a5a68aefc | -4.04665 | -54.92403 | 2026-09-29 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dbe0bc7a-8453-34bd-92a0-ca13a296eed1 | -3.94476 | -49.67786 | 2026-09-29 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 249cffa5-594a-3ab9-8c34-3e42b689f54b | -5.73372 | -45.02531 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f05a334-424f-36b5-8782-2957d1dfd2d8 | -3.92419 | -48.37987 | 2026-09-29 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4017f56-9cd1-3d41-afd6-177a5e8afc30 | -4.71631 | -50.64155 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c315ec25-62d4-3253-8281-4993ef09dab3 | -5.73388 | -45.17934 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e0192bd-141c-35f9-97bb-d95a88a64245 | 1.05854 | -50.03794 | 2026-09-29 04:49:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc37fe5d-7cbe-3794-8328-883b2aa4cabd | -6.05263 | -46.1589 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f100685-9100-370b-9ec2-b8024b9240ff | 1.8217 | -55.62754 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 950ae8e1-e7f1-379c-b977-0e594f0b8d62 | -4.4992 | -49.64044 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e8727de-520a-3949-aa83-3c2e6dc1c812 | -5.73685 | -45.03064 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bacd1a7a-c5bb-3df5-a508-6232ca362a03 | -13.53666 | -49.17442 | 2026-09-29 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a782172-b9c3-3e7f-8113-c345b7fa227c | -7.57234 | -47.36597 | 2026-09-29 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a4ad273-239e-3984-a75c-e49c2af5019c | -12.95075 | -46.64137 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b0d3b92d-f721-32ab-8228-419be7c78679 | -8.23723 | -45.44245 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c02f978e-c223-3b09-b3d2-a75aa818a91b | -11.86496 | -47.07745 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 126cd81a-adf7-3e8e-8785-5bea027fee77 | -8.21882 | -45.45986 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3492b4b0-d38a-3f8d-b9ae-682252a301f9 | -11.38143 | -43.39757 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2948af0a-a46c-3dec-b9d4-6517d074edaa | -13.07176 | -47.45 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 272cb462-9754-390b-befc-be1f64bd3c66 | -8.43234 | -47.89042 | 2026-09-29 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14f8fba3-f178-3a63-bbc7-58c39480224e | -12.79054 | -54.01772 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72e2a7f6-5884-3559-bff1-b7849db150bb | -12.0593 | -46.4985 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa4987f6-78cf-302a-94da-a04124275274 | -11.64679 | -43.50844 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edcba46c-2ab7-30ce-9667-2b4a63c37e6b | -12.78622 | -54.0213 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0a9051e-d4cb-3c60-83fc-cc251fa25917 | -14.11746 | -46.28928 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a3df4b7-9c9c-3249-ad83-7580053aa3a4 | -10.4282 | -49.37507 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab99d0b2-2f31-373f-818a-04fc502e344c | -11.40822 | -43.44632 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7334d8ed-c982-3de5-b2a6-988f6a7ee7a5 | -13.54067 | -49.17117 | 2026-09-29 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cb149d8-0770-3fec-8152-a3cf4a0bcd25 | -12.76818 | -50.98674 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71627f4a-0b49-313d-9b7b-d4ae8ab7a2f5 | -10.81013 | -48.72713 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5806140f-f982-366f-8d44-19423ba89f01 | -9.76175 | -44.82847 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2115545f-ef45-34a9-aaae-e69a6038fd0a | -7.27413 | -44.30745 | 2026-09-29 04:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41993694-39e0-3874-9663-f4291732093f | -7.4283 | -46.87516 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7094b6a2-89b4-3b54-a856-5defd34dd181 | -6.76882 | -47.16179 | 2026-09-29 04:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 546fa24e-f9a3-36c7-a3d4-b7b5d7030718 | -11.42152 | -43.45304 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2c4db89-4320-368e-8d73-c5da1dde8223 | -8.72699 | -44.91847 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa4c2715-cd0d-3b0c-b027-edaab3b4e5c1 | -9.06995 | -49.86829 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad578167-ed54-3a12-bdfe-78307315af6b | -8.72021 | -47.60956 | 2026-09-29 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edb76f2a-3482-3ce9-b3ab-dbf1d90ffb71 | -12.72355 | -46.99011 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd1a725b-87b0-31d5-b21f-cfca8d92cb45 | -8.49372 | -49.60097 | 2026-09-29 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cc7c83f-6f61-3aff-92f3-7625c7dbb6db | -11.15089 | -48.31718 | 2026-09-29 04:51:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35d1ae66-08c8-36e1-a17b-bb971efbb6a5 | -13.17758 | -48.52425 | 2026-09-29 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67a495ca-001a-32a8-88f0-20f728819e7c | -9.14126 | -49.97348 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15dec1c1-7447-3001-9905-1863d9f9eeec | -12.69598 | -47.2635 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e70835b-b040-33c3-bfd6-7d3d3bebb347 | -12.24469 | -50.42893 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95048d31-4fad-3162-8a64-60d74f8526d2 | -7.21728 | -45.08369 | 2026-09-29 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fa63c55-4728-381f-a85b-d4a87ece81b5 | -9.9569 | -50.14349 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af6b7b39-fb7d-3e6c-b719-5790e7ef8404 | -12.60954 | -47.27542 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d8a5fe4-1224-3ce4-a637-601597ac296c | -5.72491 | -53.46494 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0f00a5b-f476-319c-a385-e1db61df19f5 | -10.70027 | -44.42226 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9edddc42-a47e-340a-ae20-9e3b986c6b47 | -7.53372 | -45.8834 | 2026-09-29 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c6aa57d-89f0-3e22-bf35-c725cf74bbcf | -12.7231 | -46.99187 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de268569-59de-3fde-bb62-84a2dacceb9e | -14.11818 | -46.28399 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77e2738b-6c61-3535-a6e9-884d360b0ec3 | -11.44278 | -43.47087 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 991fbe0f-6800-392f-ad51-3ac410e2dde8 | -11.17793 | -44.80608 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90d04b36-34c1-324b-b86d-dc0babd92ae3 | -13.20046 | -48.56327 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0c28c43-0f24-38d8-ab3b-72b9178e2039 | -7.7184 | -44.57208 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4352a10d-9523-351b-a2d9-fecc49a62356 | -11.37303 | -47.44708 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eae0b44e-1cdc-3914-9be4-6b4020ab7b4f | -13.18995 | -48.56165 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3011c82-c27d-3214-ab80-113dff219201 | -12.05471 | -50.21698 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9058f6d5-b52c-33c7-98a9-c154833f8337 | -12.73235 | -47.27387 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5e913b95-b222-39e8-bc50-d2c9e4e18f10 | -11.79782 | -49.05931 | 2026-09-29 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5476d329-ba93-3ace-aa44-2df28cbc0d74 | -11.90086 | -50.61629 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a632ec2d-8e31-3004-a34e-1c2f43c00356 | -9.95579 | -50.15051 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cd29680-3ee1-3d53-ae62-cd58e3f971db | -9.96022 | -50.1656 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec09f314-fecf-3cc5-92a7-9a31d0a1035f | -10.90327 | -44.65665 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b8fffc5-0519-3b26-8dce-68a6945d4f2c | -11.9767 | -50.92607 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a71937e-953c-3188-9a77-0afe34158bf8 | -9.96578 | -50.13054 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 596375bd-e077-3677-8545-2c0dd57d65be | -9.07051 | -49.86479 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76f66bc6-e13f-338b-990a-eac79e2f26c0 | -12.76247 | -47.30087 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3e21c80-b8f4-39dc-8751-e7f325349c89 | -12.75626 | -52.81673 | 2026-09-29 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef689911-0116-3e1f-ab1e-b7ac9fe05921 | -10.92775 | -47.59297 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 926518c5-d907-3acb-b804-3db7dc113362 | -12.32849 | -46.95442 | 2026-09-29 04:51:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1125946e-0957-3bc8-9ef1-8bdd57c6142b | -12.90149 | -52.03637 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2974c3de-1f2e-3c4a-9cee-63c67689e2eb | -10.41828 | -53.77753 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c266c08-9b1f-37e2-bce2-bff572079eaf | -12.71914 | -46.99395 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13e2ef89-8296-37ba-93f1-e5512b5516aa | -8.36172 | -45.43791 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e207a7b-1f85-34b0-a9f1-bf4af712d446 | -11.98275 | -50.95241 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c361096-2b11-36f3-800f-2c1f6957fcaa | -10.24912 | -44.60548 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eeba4fe8-0a16-388c-8410-5f061523cb47 | -12.75081 | -54.05442 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2876acd-5c1a-3141-a47c-97cf100bbe9c | -11.43284 | -43.47447 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3cc42340-f47a-3d03-99d6-63889e26f85f | -13.53092 | -46.90748 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 499e634a-9918-3a22-9b22-4d5284d275bb | -13.20452 | -48.56004 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 489f21ce-39dc-3464-a288-1a9dac9ad3da | -11.95389 | -50.94046 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README38.md)
