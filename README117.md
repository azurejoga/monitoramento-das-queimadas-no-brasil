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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ee2656f-bf69-3ac5-ad01-5678ee210807 | -10.21476 | -54.12555 | 2025-10-05 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df33ef56-a3e3-3540-9fbe-bb33bc17395d | -9.56714 | -46.12488 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1764c8c0-1a3d-307b-9a4e-041f068b9957 | -5.95702 | -43.51615 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c233f73-efb3-3c06-af06-6a5ddea42157 | -10.84018 | -47.98049 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 875b97db-29b1-3408-bec3-c19e94d94353 | -9.33408 | -54.52666 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2240fb34-e267-3170-a23c-454d8ab2b1cc | -11.82058 | -45.05667 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b65091c4-8391-3f71-9f7a-3f880dbc2f3e | -8.55606 | -46.26274 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a8eadcc7-18c1-3549-80c6-6c45b283af7f | -11.12268 | -47.1766 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9168d0f5-93e2-35ac-a709-39fb15e0a9d4 | -11.44769 | -49.71949 | 2025-10-05 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c39e936-f2bd-30da-83eb-31565aabfbc3 | -9.40666 | -56.89265 | 2025-10-05 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54382e32-fbf8-3257-aaa8-22e3936a7e71 | -7.71018 | -46.27216 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 536c5938-f195-3788-847d-3ada9e9142e0 | -5.34597 | -45.29837 | 2025-10-05 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 927f9bf5-f4e6-3a0a-a0c8-836f4ac37263 | -10.75764 | -46.61245 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 466679a4-edd1-3851-b261-f5a5c645a243 | -5.93525 | -43.33335 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8d0086f-7102-3851-afee-3acde0972290 | -8.60381 | -46.28986 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cb944501-527e-38e5-9e43-c926090057d4 | -5.00448 | -47.21539 | 2025-10-05 05:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8284f045-785e-358f-adbd-d1ece4a49b3d | -9.855 | -60.27858 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ce18f64-cbfb-354a-aba4-270312243192 | -10.35822 | -48.16049 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 064989e7-d55d-3e21-bb2e-aec8c3d74867 | -8.86638 | -46.84673 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d860b3a-e119-3c1e-9786-bab201ba28f1 | -9.83374 | -58.07975 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdd2dcdf-7a78-3ae9-880b-370d1bf880c9 | -10.36048 | -55.38451 | 2025-10-05 05:14:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bfaa3c7-a749-37c5-9e71-fe36b790f008 | -10.94345 | -47.06551 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9307f252-c349-38a4-9f0b-e4a2a59b8086 | -7.71706 | -46.26812 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 773219b5-6983-3464-9ead-2013f1c9d86c | -9.2981 | -46.01756 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9bea1c9b-4755-3686-95bd-f129ad1bd5ad | -5.54117 | -51.44193 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1752eda3-462a-335f-93d5-3930a0696c3a | -11.78543 | -47.92508 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 059dc8f8-d28e-3ebf-998c-d188578c8ab2 | -9.03892 | -61.64511 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8946196e-8612-3275-aead-11a9a5cf3395 | -8.62117 | -54.97162 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9774155e-94e6-31a7-9a5d-43cc11fc230e | -10.34692 | -48.15796 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d1daed7-953c-3b7e-9ded-bee5e8223e8e | -6.7376 | -48.17826 | 2025-10-05 05:14:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd40492e-5247-35c8-b394-3e628b5adf34 | -9.53046 | -62.80759 | 2025-10-05 05:14:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4b781ab-3064-3344-9178-1dbcdf88f7f8 | -9.34726 | -57.43044 | 2025-10-05 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 348793c5-96ca-30f7-9925-d736b74e0490 | -11.52913 | -47.67215 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51fab135-e917-3eff-a938-15736ec84582 | -6.40163 | -44.77764 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 810d884c-0cc0-350d-8821-3dc79e268460 | -9.83431 | -59.46599 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fefe45a3-ee33-3540-b7e3-1636e8a461ae | -8.61521 | -54.96237 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c29da16-dbdf-3dda-9746-81e6d8e9969f | -10.46823 | -57.4866 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1e7bd15-e276-35c2-94e1-42f1e1c26058 | -7.20931 | -46.85844 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2991aa85-4a46-39d7-9000-57f770b84ba6 | -10.94847 | -47.07613 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c25fa86-bb69-3994-a729-87ad53a02fb3 | -9.32972 | -54.53054 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3e7e053-aeb3-3102-b266-e2e7e0215d26 | -8.61161 | -54.96183 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8240e2d5-f88e-3783-8d18-c3f6325966d9 | -9.29882 | -46.01197 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bda55f9f-a9ca-334d-a515-90ec6e2e986a | -11.45881 | -51.51021 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 392ef880-a8c3-3cc3-bb00-f4513a1088dc | -10.17955 | -58.17827 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4d54e97-7a85-38d7-b771-61fece3524bb | -6.17756 | -44.5942 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e8addb2-e68e-3151-b076-8b6256228ff4 | -11.48829 | -46.79266 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78089ece-6bbe-3ae2-aba3-9c2d4edc6ca8 | -9.04142 | -61.6396 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b0d7e0e-37d0-3a50-894a-3349a03f05da | -7.1585 | -46.08644 | 2025-10-05 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79efe80a-0e46-33cb-aaf5-29df6b525ccf | -6.1569 | -44.62862 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b05d348-1c8f-3f3f-a79c-a9729d7b1f79 | -9.14385 | -60.29842 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a93d1ae-cd78-3a75-8347-4dc175aa94d2 | -9.29282 | -46.00505 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| da65b9e9-3ca7-33bb-b931-97bc86c78e43 | -8.54201 | -47.68674 | 2025-10-05 05:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 296a7b14-4883-3afc-9613-0d86f513ed73 | -8.57227 | -46.33545 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 48938aa0-c886-3bb1-9501-309366afaa83 | -7.45958 | -47.17938 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58da5761-6613-3fb8-ae5f-682cc9c6af43 | -10.35776 | -48.16407 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 612edc5f-3c10-3ebb-9c15-50ca29549ae9 | -10.95125 | -47.06042 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58bbc20e-d3ab-31ee-bac6-22eaf2e381a3 | -10.39191 | -45.41136 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43165dcb-6372-389a-9e04-a6492ec0f5ba | -8.5346 | -46.33058 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 042a0fb8-a3be-31b5-8c32-6960e74eafd2 | -9.20785 | -59.68647 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6432825c-b418-33dd-b9fa-4c80d92de22f | -6.16425 | -44.57468 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b0cc2d0-012b-3e04-9875-5a7ebfd9f676 | -7.7588 | -46.31733 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d0ec321-8a8d-3ec2-92f6-781c5623df8f | -6.17946 | -44.61464 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc4f912c-1906-36d3-8433-df61661e04bc | -7.31589 | -45.55872 | 2025-10-05 05:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb51c5bf-d019-3968-a8a3-e6b7b655ebb2 | -11.62539 | -47.74729 | 2025-10-05 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd4d54c1-370f-35bd-bfd6-b9572d019348 | -10.6852 | -49.27776 | 2025-10-05 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aee45667-06a2-3330-ade7-1644bbeffef7 | -7.31265 | -45.98816 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b1139cf-f0d9-3fb8-a5b4-0a38c7f56aba | -8.6075 | -46.28165 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3f85de8a-50ae-3d3f-98c8-3e5d0fe60cb7 | -6.17527 | -44.59501 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81da1cee-3b43-33d4-8773-5a5429d23b9a | -6.59872 | -48.05325 | 2025-10-05 05:14:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e67e7310-1f29-3a4f-9413-d03494b49c53 | -6.15609 | -44.63457 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2bcc1500-2a48-3a6c-bb20-8ecc9d47e610 | -10.56572 | -48.71866 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d505e4a1-3769-301b-aba0-06b07621cc33 | -9.32732 | -54.52112 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9986495-d357-3880-a41f-8b7fc2b3b782 | -10.78192 | -51.63246 | 2025-10-05 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6179338c-2e6d-3d3c-9611-01e72b139cb2 | -11.09244 | -47.74052 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed433288-698e-378b-a8db-fd8abc1d6a2c | -6.1399 | -44.60177 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43222ef2-1a8f-3190-b7a3-6e110efd838a | -10.84126 | -47.97483 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de7cd1f4-a9b1-3fa8-a4f1-4e110fb42cfe | -5.99074 | -44.35703 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fd42bf5f-7f36-378a-bdb6-223d1ae2a34d | -10.49523 | -48.10738 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceca14f1-874e-33b3-8dfe-fa1af520b4fb | -10.63787 | -46.30441 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bff5765-a667-306b-907a-8869640e9051 | -10.50097 | -48.10826 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b102fb9d-77dc-3111-8789-a0d5ac28e5b0 | -9.03965 | -61.64067 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08fbb47d-f1a4-3397-8f31-463c39952e84 | -9.95652 | -48.76101 | 2025-10-05 05:14:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d73e761b-c0c7-30a4-9241-4f9800a7b297 | -10.93954 | -47.09867 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 99149977-06b9-3716-bcc2-9585c648966b | -11.06014 | -47.77682 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b123964-3653-3b5e-a3b0-aaf330d2f50c | -6.9837 | -44.21635 | 2025-10-05 05:14:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b414e550-915f-3a9a-a769-b6185f6456d3 | -7.54132 | -47.27905 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f47935f8-cd6b-38cb-a01a-c53e3cd8d128 | -8.62645 | -54.66038 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5589019f-1ada-3cc4-b303-76353b4e9512 | -11.11001 | -49.86151 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79ba072f-e730-3245-8523-68c5e08a57b7 | -11.59672 | -46.70952 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d075ca4-4af8-3e67-9439-02d5671a6d19 | -3.81261 | -53.83697 | 2025-10-05 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7a36427-77a7-3802-804a-094e915e4e89 | -10.2272 | -59.0884 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 184aacb5-6514-37c7-bf4e-07a1e82677e2 | -8.58607 | -46.32758 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 07e2c1b3-8442-3f64-af5e-3b19eb56c8ef | -3.77611 | -53.93195 | 2025-10-05 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ce7db36-9c1b-32b0-bc46-d64d87200bd4 | -6.14233 | -44.58375 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02b14fd6-3b3d-39f3-9d48-8e28bd4faf2f | -11.80807 | -46.84568 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1af91404-f2a1-3e61-a836-e72307123e4b | -8.051 | -54.89651 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23c038b3-f5cc-3928-9538-0b53a3177a85 | -9.91232 | -58.563 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd76aebf-1d7f-37d1-856b-77638cb64093 | -11.23027 | -49.92926 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e4a75ea-c097-3746-a65e-f7f8e3f5d894 | -8.62477 | -54.97214 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c63a793-d1de-3c07-b5f5-4f5abef1ec03 | -5.76201 | -43.98746 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README118.md)
