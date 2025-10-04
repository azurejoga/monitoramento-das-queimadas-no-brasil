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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14c1dcac-29ff-365a-8eee-e1924c67b7c1 | -12.9663 | -50.9815 | 2025-10-04 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c0082d62-1cd8-38d0-9c7d-35fd1eddb39a | -6.7167 | -42.8101 | 2025-10-04 13:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| f27857d1-0cea-3f05-824d-4af8d2b68ec7 | -14.2131 | -46.0596 | 2025-10-04 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 202.3 |
| c1eb5d42-c0b6-3254-b4a9-139903655a43 | -10.202 | -50.3536 | 2025-10-04 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a208fc83-92fd-3618-8f1e-f80d747c186d | -13.1164 | -47.8178 | 2025-10-04 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 481d88eb-bc21-3ede-893e-55a6ae1782ca | -11.9331 | -46.4153 | 2025-10-04 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5a82ddb5-ac34-330a-91f1-fdef8a26518a | -10.2973 | -50.2799 | 2025-10-04 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f8a4c19f-bbf0-34d6-9bdd-a954ff39ba7b | -13.3131 | -47.5876 | 2025-10-04 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9ec043ff-0a04-3fa8-b914-4849c21d231a | -13.3426 | -48.0742 | 2025-10-04 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 58d154b9-e8ce-354c-a5f4-7ed0eb03a41d | -9.1716 | -49.9408 | 2025-10-04 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 88b9f8c1-820e-3b1b-9bc8-d159e12256f9 | -7.7687 | -46.2255 | 2025-10-04 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8d8e2714-2504-3fd5-bf50-b563dec7a9fe | -7.0555 | -42.8018 | 2025-10-04 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 4a2cb20c-b820-39d8-b0f7-dd6bd08dd8ee | -14.6716 | -48.3157 | 2025-10-04 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2af03fc4-1c94-336f-85d3-a79d3174027a | -7.8593 | -48.2037 | 2025-10-04 13:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 310.0 |
| 262e42d7-83b0-3986-b8bc-e3425a5cc934 | -11.1268 | -47.9077 | 2025-10-04 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e01f3700-e14e-3ed9-8d9c-b5a12b4086be | -7.0604 | -45.7946 | 2025-10-04 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 243.9 |
| ed4f2658-e723-304f-8279-d700e2e8c188 | -8.8529 | -46.7897 | 2025-10-04 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2f19b4d7-841c-3ff8-9653-39f0e1a82675 | -7.0558 | -42.7782 | 2025-10-04 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 158.1 |
| 65d42b68-279a-3339-9f47-e96203af668e | -15.5211 | -46.838 | 2025-10-04 13:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| bd38f088-5b01-3af1-921e-0229acadddfb | -12.4171 | -44.0821 | 2025-10-04 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6fbea309-373e-3e92-9bc9-417a4ea3d48b | -7.4416 | -46.9666 | 2025-10-04 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ae6b1d3e-ec95-32b3-8915-ca2492697eb9 | -11.8442 | -44.9408 | 2025-10-04 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 1e23fe7e-8e13-3040-a3aa-47daf2089655 | -11.5069 | -46.7671 | 2025-10-04 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 251.9 |
| d8a94594-9ae2-349d-bddb-0fa574a7e566 | -16.097 | -51.0611 | 2025-10-04 13:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| f9fc4fdb-77d3-3525-ab86-a5d1a2799ceb | -12.3853 | -50.2595 | 2025-10-04 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4af979ad-21c4-3869-bf76-1275f5fda475 | -10.127 | -50.3184 | 2025-10-04 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 858ac983-36b2-3c33-95d8-4e71e13d427d | -7.5504 | -42.3965 | 2025-10-04 13:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 160.9 |
| 8b2be98f-29c6-32fc-86e2-681f70578bee | -10.5835 | -48.7178 | 2025-10-04 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9b5c8c98-fc2a-3e6b-ad02-d210d26928d9 | -8.9664 | -46.7557 | 2025-10-04 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1fc7e175-83f9-3bd6-90c1-9c987d9467d9 | -10.1081 | -50.3203 | 2025-10-04 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 6df655b2-217a-33af-82f3-11a362ab60d4 | -7.7489 | -46.3168 | 2025-10-04 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0824fffb-14fc-3cbd-acc7-b3c50fcfc95e | -11.4486 | -43.504 | 2025-10-04 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 2e4250f0-58f5-3da6-8981-7f5da860d177 | -12.9663 | -50.9815 | 2025-10-04 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 8de83122-b5d1-321a-b30d-5a81809650bd | -14.2321 | -46.0794 | 2025-10-04 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 474ce3bc-d0a2-3b8f-9905-4e1d63df2777 | -7.7563 | -42.541 | 2025-10-04 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 6dfe340b-e277-3823-a824-7cf534cf0eef | -13.3127 | -47.61 | 2025-10-04 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 8c0716b7-6328-399c-946a-9a580503afc3 | -11.1458 | -47.9054 | 2025-10-04 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0fa3bd69-48a3-3ebc-8ff0-028df4f4d327 | -7.878 | -48.2021 | 2025-10-04 13:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 38fda61c-bb8c-3728-910e-b3a8e46588a1 | -7.813 | -42.5349 | 2025-10-04 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 187.1 |
| c648e254-e097-3fb9-ac4b-e864b73a1daa | -11.4877 | -46.7696 | 2025-10-04 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d3d0ec3e-a6d0-313b-bc66-3800de9338ed | -15.5408 | -46.8344 | 2025-10-04 13:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 149.0 |
| d1dc4a1b-0723-3dcd-92aa-036244e563d7 | -10.1459 | -50.3165 | 2025-10-04 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 98223997-a21e-37d2-9c8d-8016ceebadd6 | -12.7194 | -48.5611 | 2025-10-04 13:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 0c1d95fa-890b-3f7c-9d35-c3abbc309a61 | -8.5458 | -47.264 | 2025-10-04 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 973572f2-3949-3f4a-a4cc-19dfffd2f108 | -7.7935 | -42.5845 | 2025-10-04 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| ec3c28cf-7958-379c-bcbf-4a0980766ad1 | -14.3899 | -45.9601 | 2025-10-04 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 55561d69-ee55-33d8-a650-1a6949737546 | -7.7938 | -42.5607 | 2025-10-04 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 3ce4454a-5c4e-37d6-ba5c-427e091eb745 | -15.3179 | -46.3011 | 2025-10-04 13:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 121.9 |
| cf677834-cc86-3714-b442-a142b7536431 | -11.5683 | -47.6749 | 2025-10-04 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 9d3d7f2d-6cfe-3644-8576-196db78ded29 | -15.3797 | -47.952 | 2025-10-04 13:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 18bd8e83-1b90-3be3-89d2-eaddf6773d9a | -14.2131 | -46.0596 | 2025-10-04 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 09933fa9-ede5-3a30-8e5d-d17fc51b2d25 | -11.8635 | -44.938 | 2025-10-04 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| fcbcd3b1-63d9-3d33-938e-1723aac4532a | -12.8401 | -50.504 | 2025-10-04 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| c7d4ba62-66b6-37f0-99b8-530c3d7af68a | -7.7941 | -42.5369 | 2025-10-04 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 149.5 |
| 0576397d-c1b1-3023-ad03-2c929b31e502 | -13.1156 | -47.8625 | 2025-10-04 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5bcad0cf-e8ec-3d2c-8f21-df8f2fc8252a | -8.1372 | -50.2428 | 2025-10-04 13:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c0daaff6-446b-3aeb-b4b5-e4e5f2f10e39 | -8.8526 | -46.812 | 2025-10-04 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 29b667e5-8245-3d7b-a33e-19ee4f21c589 | -12.0891 | -45.1814 | 2025-10-04 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 983fae17-d36d-3a98-9c72-8849d37b4c22 | -12.3158 | -45.3776 | 2025-10-04 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 41c43f49-50f9-3a06-9e11-ed6cffdb10b8 | -7.7491 | -46.2944 | 2025-10-04 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ba75ca6d-1262-35f9-9fef-4cf8ad436e15 | -13.6717 | -51.234 | 2025-10-04 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 6c834843-a3ed-3659-8e52-535e9c86e272 | -15.958 | -43.318 | 2025-10-04 13:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 189568e8-2471-3e59-9d00-2d62c014e26c | -11.8818 | -44.9815 | 2025-10-04 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 72b64252-3065-3ff4-9393-f86dceb90610 | -13.2938 | -47.5905 | 2025-10-04 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 93a4db15-945f-3c76-8823-d67941929269 | -13.3233 | -48.077 | 2025-10-04 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 529ba809-535c-3644-af98-be302e68017d | -12.6512 | -46.9894 | 2025-10-04 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 5535e6e0-36e9-3c37-b82b-5cc5e9e5ffe1 | -12.9471 | -50.9838 | 2025-10-04 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e46cc6a9-80cd-358f-b894-b85b365c69da | -11.7924 | -46.8184 | 2025-10-04 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| cf8f6e5e-5bb5-30e6-b322-0f606e9b276c | -10.8241 | -46.5863 | 2025-10-04 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e4fe249b-d98d-366a-80a0-e08ae63dd34c | -13.2934 | -47.6129 | 2025-10-04 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 135.0 |
| acbbab2c-ac4e-3d39-ae0f-0f9d5cbbc3ef | -13.0959 | -47.8876 | 2025-10-04 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c1ec5619-8dee-316b-b896-6f14f7300de3 | -13.116 | -47.8401 | 2025-10-04 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a6f315a2-45c6-3daa-9ee6-6a4050d79d56 | -9.1114 | -44.4029 | 2025-10-04 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 27cc2ab8-fdef-37fd-abc2-ea77e1510f8b | -11.5492 | -47.6773 | 2025-10-04 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d823af14-1b81-39db-a9ec-058c03486d7d | -11.6841 | -45.3333 | 2025-10-04 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cb42d7a1-a342-3453-8da8-6d8413f9482c | -12.8761 | -47.2937 | 2025-10-04 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| d4c987cb-891f-3411-9bc8-e08fff9c244b | -14.2126 | -46.0827 | 2025-10-04 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 161.0 |
| d22ed15f-2a7b-390b-a786-78c08d741bac | -7.8689 | -47.3268 | 2025-10-04 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 407b0171-fade-309b-9c9c-72f6d633d2d9 | -7.7684 | -46.2479 | 2025-10-04 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| cac188d0-ca1f-3e71-aa80-9b6f9c7214c1 | -11.4414 | -43.9057 | 2025-10-04 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| d97214f8-e361-3248-a0a5-10b64423a2e7 | -7.7566 | -42.5172 | 2025-10-04 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 187.5 |
| 23fe4511-4d86-363e-88b8-3f94fc76e2d5 | -11.7962 | -48.9231 | 2025-10-04 13:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 69ab8122-efa2-3f45-8a17-ccbd8bbab205 | -10.6024 | -48.7157 | 2025-10-04 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b61da34c-2ace-3523-8470-5064dfae07ee | -7.0369 | -42.78 | 2025-10-04 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 228.0 |
| a9bc943a-566e-3e34-8e97-26006696e6a3 | -7.793 | -44.1535 | 2025-10-04 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| bcc4865e-0f7d-34ae-b96f-af29d45fbf07 | -12.8761 | -47.2937 | 2025-10-04 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 7075af8a-bd1b-3f76-abd4-d84b3c5108c5 | -15.3601 | -47.9554 | 2025-10-04 13:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 77d7eb24-08b9-3ad1-9509-cb81f60338dd | -12.3853 | -50.2595 | 2025-10-04 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 389.0 |
| 3fdd8a9b-e3f1-3f2f-bf0f-04ef75b59650 | -7.7935 | -42.5845 | 2025-10-04 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| e81ab3d7-7af5-3d5c-9855-7cc885ddeee8 | -14.6716 | -48.3157 | 2025-10-04 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7143e0ef-7d1b-3ab9-86ec-f9bc4d210390 | -10.5835 | -48.7178 | 2025-10-04 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 46c8ba79-2b2e-3bdb-8b96-4992eda233ec | -12.4364 | -44.079 | 2025-10-04 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 470a1355-3ea7-3474-8950-60a5ed8d6f57 | -8.8534 | -46.7451 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b523d02d-951f-3d05-ab38-42b1d1d4605b | -7.7941 | -42.5369 | 2025-10-04 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 159.5 |
| c753c834-f45a-3da9-acfe-38ea82c7189f | -13.3225 | -48.1216 | 2025-10-04 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 1ac5071f-69a9-35b1-8d92-f9295dd4d597 | -7.7563 | -42.541 | 2025-10-04 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 127.0 |
| 21318667-38de-30f2-9efb-b3ac3ef66d47 | -13.1333 | -47.949 | 2025-10-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 93f7e6ec-8a0a-3493-b3da-9cc70c1fb89e | -8.8523 | -46.8343 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 67ff2eda-ffcc-35fe-8aea-6fc2f869506a | -14.5751 | -52.4789 | 2025-10-04 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| dff9ed81-5790-3be7-8741-7172ce5a9dd4 | -7.8593 | -48.2037 | 2025-10-04 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 235.1 |


[Clique aqui para ver as próximas entradas](README150.md)
