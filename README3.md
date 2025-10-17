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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37b4c9d0-aa1d-3adf-ae16-b19b0aef3d75 | -13.8048 | -43.25149 | 2025-10-17 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 5bb95c44-6a7b-3abf-9c18-d6c57905d112 | -13.39604 | -47.21277 | 2025-10-17 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5291d6c9-f2f4-39c6-a744-c786d4ad8a6f | -11.47349 | -44.18872 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb2941a6-f2b8-3415-9e8b-18296a877ae2 | -12.04502 | -51.38269 | 2025-10-17 00:11:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cf603367-c78e-300a-8ebb-2af1227d5abc | -12.96671 | -47.10359 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 771b7d97-b6bd-3a18-b5f2-60fd77732128 | -13.73893 | -42.52188 | 2025-10-17 00:11:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e0aeea54-5671-3b2e-8442-709f93293246 | -11.45429 | -44.24669 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| dcb283bf-d4b2-3df5-a859-f72312347b0b | -16.02896 | -43.50126 | 2025-10-17 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 965780d8-dbb9-3c59-984d-3a3372c5fac5 | -11.48334 | -44.26095 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 43f5b9f3-bc1b-30dd-b627-9585258a2939 | -12.05889 | -42.89925 | 2025-10-17 00:11:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1acad1ac-2550-3427-8306-160755f71eb6 | -11.44331 | -44.24492 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a595758c-935a-3bef-bf0b-d6ecbf3a58a3 | -12.53408 | -42.21978 | 2025-10-17 00:11:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 9ca1db5d-6037-31c7-9522-3b332fcfd4c2 | -13.00753 | -43.22208 | 2025-10-17 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 897f5055-3850-3205-a228-11ee64754728 | -11.46017 | -44.02548 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 657369fc-03e9-385e-8b30-ce50f8ba009d | -13.1427 | -46.47427 | 2025-10-17 00:11:00 | TERRA_M-M | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ae667f8f-7b53-3e33-8c6a-5303ac97febc | -14.30467 | -44.02004 | 2025-10-17 00:11:00 | TERRA_M-M | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c8eb4376-e570-328e-b71e-e562d4eb51a2 | -11.46043 | -44.2919 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 58a7054c-78a7-311c-9538-fa795e06eed7 | -14.19787 | -44.81403 | 2025-10-17 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a724c2f2-1a77-3f9a-8fb2-7f4663ac4d1f | -14.46869 | -48.4368 | 2025-10-17 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c00d64ec-e224-30a7-bf8c-75bfa13f39b3 | -14.30342 | -44.01075 | 2025-10-17 00:11:00 | TERRA_M-M | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f9549cc3-1088-35ad-a672-b259e7cf8d81 | -14.74404 | -42.46066 | 2025-10-17 00:11:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b8e5a598-a982-3ff9-b146-ba5e9bcac095 | -14.92626 | -46.72642 | 2025-10-17 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a6535308-a604-366c-8af2-62c0cbcfba58 | -12.92888 | -41.82061 | 2025-10-17 00:11:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3d9112f3-7b9c-368c-8da4-20d55651da47 | -16.54754 | -41.65657 | 2025-10-17 00:11:00 | TERRA_M-M | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 31b2f9e2-284d-3c8a-8152-bb825a140b25 | -14.91595 | -46.72817 | 2025-10-17 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e8a5afdf-8a36-36e2-a87d-16260a746d23 | -11.47053 | -44.29968 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| eb0bcc41-2288-37b4-a2a3-1d1372b34a9a | -16.0277 | -43.49195 | 2025-10-17 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6c588dd1-2c44-3f5b-ac51-7c7c243d3f2c | -12.89982 | -47.1331 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 71c02d46-f0b1-3983-ba02-94035d1dfe13 | -11.953 | -45.35608 | 2025-10-17 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9267facd-d44b-3bf0-91e1-24a33e61abb4 | -14.08504 | -43.62354 | 2025-10-17 00:11:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71b4118a-1320-3200-b7e9-f4b71c45d4ed | -14.18888 | -41.60622 | 2025-10-17 00:11:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| baec943f-28f4-336c-9286-63c70be3c4b0 | -18.0937 | -42.43976 | 2025-10-17 00:11:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 9a73bfac-4457-303b-825b-025c4e24cb74 | -13.04466 | -47.33807 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f6eb13db-9a13-3658-9c9c-f8f764cc205a | -12.06016 | -42.90831 | 2025-10-17 00:11:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 32dd42a2-ed63-38c1-82f3-a6e64594967c | -11.48234 | -44.18744 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| d8f3a5da-f706-368a-a2d4-302719b34932 | -11.48996 | -44.17715 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| fbdf4047-5f70-3920-be04-525cebce64d8 | -11.45894 | -44.0165 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e3be9b6d-c2da-32bb-9440-d523dd0fe7b9 | -12.32447 | -41.40027 | 2025-10-17 00:11:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| d87475d3-b87d-3ac0-811e-0341761f7034 | -13.38784 | -42.71074 | 2025-10-17 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 719533b4-4866-3315-8a69-ed0e4d7485ea | -13.05979 | -43.6004 | 2025-10-17 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 564fedfd-4a13-3cd8-8a00-69bd33c33fe5 | -12.13708 | -43.26497 | 2025-10-17 00:11:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 06694ad2-c389-372a-aaa7-2510b6a1d1ee | -11.57476 | -44.05756 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 22363b89-18c4-3102-878d-84eabfed989a | -11.43941 | -44.28233 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3be6c816-13e6-3e35-8b7c-f0c7fc72cbb3 | -15.78721 | -41.49923 | 2025-10-17 00:11:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 09d97bc3-bddc-31ba-9aa5-936c6a19e9e9 | -13.9283 | -45.61654 | 2025-10-17 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 1d9bf246-8ddd-35f0-942c-bc8b437b0783 | -12.85174 | -44.16678 | 2025-10-17 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| fdddbc8c-31de-390b-b984-51e205549d95 | -14.96544 | -41.30173 | 2025-10-17 00:11:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 650ab842-3a94-3a1e-ba6a-4d0587ea541e | -11.50045 | -44.05631 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0c081faa-57fe-3d20-9b70-e3167285b4dd | -14.0939 | -43.62225 | 2025-10-17 00:11:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| feef8783-b8d8-3464-86cc-8d854fb4f382 | -11.4592 | -44.28285 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 925bbee4-7e70-3707-adc8-8ba0e7120261 | -13.39462 | -47.20108 | 2025-10-17 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 936a3e61-a806-39a9-93fc-c6c75efcfe94 | -11.4693 | -44.29063 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 71302d44-d8f3-3d06-abe3-3a90cc3fa3a3 | -11.45947 | -44.21833 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0b30dfda-5c8c-32db-bf63-ba7063ffa557 | -12.91078 | -41.82359 | 2025-10-17 00:11:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bedd409c-55d4-334f-a350-0326692fedf1 | -11.40048 | -44.19588 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| b8870309-2404-3715-aece-062f7af12063 | -12.85298 | -44.17593 | 2025-10-17 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 31e831d7-809a-30fa-836c-7c177970e477 | -11.47469 | -45.08512 | 2025-10-17 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1777fd29-07ff-3022-a190-8686109945a5 | -11.45184 | -44.22863 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 735b8c9a-ee74-367f-ab15-1c4f6b62e6aa | -11.4457 | -44.18353 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b723619a-37b5-31de-bcaa-35cbe3a94394 | -18.55212 | -43.94004 | 2025-10-17 00:11:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0f2443de-1ba4-3479-be0b-b20221ea4b97 | -11.45675 | -44.26477 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 8c85398c-2075-3a8a-a220-34aab9683776 | -11.44693 | -44.19254 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a21825e3-3493-3edd-93d4-233e7b873190 | -12.96994 | -47.12954 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b2289153-0798-3d48-8531-59049e0892be | -11.49921 | -44.04732 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c2e085d-2987-3c17-90fa-d6eb3e16bdd3 | -11.47249 | -44.11537 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b8c20088-c1c7-39b6-bfbc-50805a085523 | -13.04281 | -43.21685 | 2025-10-17 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6df58e55-f61a-3bbd-bbb3-526592dd5f0d | -12.94769 | -47.11985 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8cabfa9f-400c-3e3c-85b6-f1cd5a83dfbc | -12.47408 | -45.47892 | 2025-10-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 51456676-bbd8-33a4-9cb5-25b074da9c7f | -13.28127 | -44.48717 | 2025-10-17 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ddb9ff07-a44d-33b0-92a0-aa901ceb8634 | -12.78338 | -44.89311 | 2025-10-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 16b49a11-12dd-3d47-8f69-d5e7a64b130b | -11.59491 | -44.07301 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 111e1a37-dcd3-3d27-afef-d5c44130da7d | -11.45552 | -44.25573 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 8728fa8b-4356-30e2-aa27-0df02edccab4 | -18.05334 | -42.4743 | 2025-10-17 00:11:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 82e1f3bd-7155-3ab6-8f5b-effe1fadcfbb | -13.38912 | -42.71982 | 2025-10-17 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 837fd66a-dda7-3ef1-bf0e-8fd63471ad45 | -11.57691 | -48.5543 | 2025-10-17 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d974ecf2-e605-3732-8303-2a611e04107b | -19.07786 | -46.82999 | 2025-10-17 00:11:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 36.2 |
| a9458e66-4c8c-325c-8bd4-e4f723ca1acf | -17.96525 | -39.88243 | 2025-10-17 00:11:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| a5112e3d-014f-3cc6-b0ea-49bec9e6d29d | -11.47618 | -44.14238 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bab7a978-aef5-311d-bb99-2d443ab92402 | -13.49249 | -40.33896 | 2025-10-17 00:11:00 | TERRA_M-M | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| be8bf487-77a3-32bc-bd8d-05f1897b8bb0 | -15.78217 | -43.65066 | 2025-10-17 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a7828b65-72fa-3e74-bc12-cac2c190c8d8 | -11.45503 | -44.0537 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70fda6c5-4a09-3267-9632-c8e553060ffb | -13.50991 | -41.0037 | 2025-10-17 00:11:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2f803be3-1b24-316c-ba0a-5678a780c3d9 | -15.9754 | -41.52509 | 2025-10-17 00:11:00 | TERRA_M-M | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9fb37738-a0e2-3727-9d2c-d8efabdc1f41 | -11.43817 | -44.2733 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0785b181-4447-32b8-9cfa-31dee3699538 | -11.48827 | -44.29713 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 11739f80-a9c9-3673-a3a4-96d892dae7cc | -11.47694 | -44.28031 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 444.7 |
| b1b7af90-d45c-3396-a090-23cfaf7c9a0b | -11.46166 | -44.30095 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a6888fe3-dc96-3707-ae76-c6e15165a3d0 | -12.92873 | -39.93766 | 2025-10-17 00:11:00 | TERRA_M-M | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 62dce6d5-1796-3649-b7ff-1240fccc5453 | -12.31281 | -47.26041 | 2025-10-17 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d1be47f0-a656-341b-94cf-12cba0e581ae | -11.42352 | -44.10078 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c194a71c-5a0d-32ad-af9c-178b1a4f4f96 | -13.04307 | -47.32487 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e160d159-0f85-310d-aa8b-b69ad2eba556 | -12.12822 | -42.15313 | 2025-10-17 00:11:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 22dfbba7-63c9-337a-85f3-985586ade306 | -11.46807 | -44.28158 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 408.7 |
| 6f28aca8-1833-3d9d-b004-f8f8ce69772c | -13.35256 | -42.3331 | 2025-10-17 00:11:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7c80636b-3d45-380e-b4ea-b61c9b461915 | -12.58541 | -43.36984 | 2025-10-17 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 789e8b2c-f8e1-39fd-8762-affeb52c26da | -13.91879 | -45.61786 | 2025-10-17 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 973d6889-711f-38fa-8110-d14420a2bb3a | -11.39801 | -44.17786 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| be94d19d-8b64-35c4-b24a-eb05d0a87d88 | -12.87691 | -46.87077 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d37a9e75-53a0-3260-9f91-abfc7ae7efec | -13.44792 | -44.28949 | 2025-10-17 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 283a6706-1036-3284-9ff9-fcd694afa780 | -15.92174 | -43.52293 | 2025-10-17 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |


[Clique aqui para ver as próximas entradas](README4.md)
