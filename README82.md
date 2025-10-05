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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de58a509-51c1-32c1-9a6b-9cce0d61bd16 | -8.58286 | -46.31579 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 060a056d-2939-3dbc-8c53-15566508bc33 | -11.00206 | -57.06132 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9147d3df-ca86-37bb-8c89-e82b05c4ee2c | -7.45741 | -47.18496 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dfca0af-2aa1-3765-82f2-933b10740e72 | -8.56091 | -46.26414 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8a9e9e09-5a9c-36b8-a048-1c02b0ee0722 | -13.10756 | -47.93088 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a75e9ad5-77cc-3859-a6bb-74eb3d07e873 | -11.51258 | -54.47874 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dad5759a-a0ed-3980-9846-5eeb2aa0321b | -8.57402 | -47.65525 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01383957-2644-380d-8413-b617cffb20dd | -13.1012 | -47.83256 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad9eabe0-f5fd-36f1-89f7-dd624e10be87 | -13.25444 | -48.4948 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2c6e6c6-fb96-34c6-a889-2645d9492fc2 | -11.95574 | -51.47089 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75961980-1953-3d54-b590-a7414e45ad6a | -12.16962 | -51.42802 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40e5cd13-8877-3f6a-ae2d-5a971c2a6876 | -11.04183 | -47.7945 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6edde36-0817-3ffb-b389-83b3e582e757 | -11.26161 | -47.78802 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1c7b2ce-58d7-3f89-bb59-bbcd661585a7 | -8.04462 | -54.89495 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021cc591-ad2d-3917-ba82-7ed8f9ed2575 | -8.87419 | -46.72477 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ea5c51e4-64ce-3d1f-8c37-c02c45c2a6b6 | -13.30509 | -47.77723 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24bcdd6f-a465-344e-9b00-b5924dcbb04f | -11.81508 | -45.07929 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94625967-2c2e-34fb-af3b-93d7aa351bcf | -11.38558 | -54.35194 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86541716-7504-3390-b320-eacbe970959b | -12.2466 | -47.84497 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bfa28a1-f599-3066-929b-2d3e2f1eaead | -11.62331 | -47.7459 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e24589d-834c-32e7-8e9a-a198a1621092 | -12.78008 | -48.81819 | 2025-10-05 04:46:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97f4e086-6125-3781-84b1-b25efcdd727b | -13.09897 | -47.87597 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d169cf7-4de2-3fc3-859b-14c6070221d2 | -12.78315 | -48.82324 | 2025-10-05 04:46:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b1095bc-fdf2-3fdf-975e-3f3966a2b46e | -11.71385 | -45.34759 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d43faba4-5e36-302e-bf06-fb644dff872e | -10.57456 | -48.68962 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 241596b1-4225-3e52-a3fd-e477b38ae9a1 | -13.12302 | -47.96365 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e27ec7a5-d14b-33a9-9a5d-61e493e4a61e | -13.5593 | -44.10082 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8f96ae4-63cc-3043-96b1-eb71959d9270 | -9.27824 | -46.00801 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00e19430-b8af-30f3-89d9-712ae9471b33 | -11.51666 | -54.47546 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ea3de6e-0b33-3917-a3cf-f8cb64ab17bd | -8.58797 | -46.30905 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 23fc2b78-f019-3546-aa0e-4ca481642561 | -9.06867 | -47.01824 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a42ee78-03ff-3bcc-90dc-8be124c85f19 | -12.32 | -55.13892 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70e6f5dd-94bc-382e-b684-8ea94320ac24 | -12.31524 | -45.36522 | 2025-10-05 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 628eca5d-43cf-322a-9229-f0b9c6b7fba0 | -12.27341 | -53.92754 | 2025-10-05 04:46:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e48251e8-83f3-3ccb-85e2-748bce813984 | -13.68872 | -47.34517 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 315f1de6-a9e4-3869-b97c-30c39108b229 | -10.45589 | -51.27427 | 2025-10-05 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2e21f11-4ece-3b29-9e1b-6a9ff45770ae | -9.98526 | -48.27101 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c185bf1e-a924-3213-9e84-6bb526099b2c | -11.00144 | -57.0501 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a133268c-2bdd-3416-a013-d08a0b8f8312 | -12.98269 | -51.03888 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7c375ad-5091-3fd4-9321-395c366b7860 | -10.35505 | -48.16245 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70a1aa00-0ff6-3c4c-a842-3104643132b3 | -6.7289 | -45.98436 | 2025-10-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ccf2045-eecc-3c2f-b65d-96f28efec679 | -11.87197 | -56.88847 | 2025-10-05 04:46:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e1561919-32ca-3f7e-902e-44e5f9f8c82f | -7.42722 | -41.12397 | 2025-10-05 04:46:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 96f2cc7c-0549-3763-8414-5efb14a00c0c | -13.24952 | -48.47431 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16b5688c-dbd8-3943-b5a7-75376d4a337c | -12.2831 | -55.11708 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62d9f594-8ca1-30bc-8600-f8728c8ed0cb | -13.48496 | -47.28662 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef515d82-b900-3312-8c16-00ee88cfaa34 | -8.62894 | -54.99739 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b698200-2f99-3baf-bce0-85c81f530326 | -12.60734 | -48.12331 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3eaf538b-2e88-3852-bbcf-75ff1d33346c | -11.82976 | -45.07555 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0429bf8d-2d3a-36cb-a931-f7176383abcd | -13.26691 | -47.82005 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e8204628-4b33-3940-b408-041dc7c051a6 | -13.59185 | -48.16044 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0773d7ba-6357-3098-9b73-aa5d44935f88 | -8.19043 | -44.14293 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bf05d592-abdf-33f1-9957-a0f01de460d4 | -8.42187 | -46.8037 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ed3ad36-f61f-35dd-a212-7f0a0f758e73 | -8.81284 | -44.81882 | 2025-10-05 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 067c73dd-cf4f-34d3-871d-3cc80d68ef4a | -12.3114 | -55.1425 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04adb150-3d76-3145-bcd7-43df35b67385 | -13.14926 | -50.92879 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29d65599-4714-34b1-b9a3-68f17df6c531 | -13.55967 | -44.09785 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd3c50f5-a4b1-3512-aa4d-e3825520756a | -11.91062 | -46.23799 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c705734-efdc-3143-ba86-8624cedf683b | -7.7971 | -42.57042 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fc7a09b7-e3fc-3fb1-b24b-41ac6c9d0e5f | -9.75751 | -47.73741 | 2025-10-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a518c0a-fe75-32e7-8f83-77e6180f73ac | -12.23289 | -43.76982 | 2025-10-05 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91bb690d-1dc4-34a5-9bac-a53f8b2a509e | -10.99626 | -46.5093 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58699733-773b-3abf-89d4-c0f274351572 | -10.64951 | -46.33604 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cd09678-a64c-3b9c-a500-274b71c321dc | -13.14601 | -47.97023 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba6560da-d252-33ca-b1fb-74b148cbb5ce | -10.30102 | -47.94123 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2381793e-5c6d-3b51-8e7a-a24850204a85 | -13.35353 | -47.24443 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12d54fbe-5f5f-3e2f-a8e9-200221ca781a | -13.49901 | -47.27571 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d24bed8b-b0b2-3e89-982d-d66ede7aa904 | -8.62216 | -54.96677 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb11614-f267-3b47-a659-7db1342e4bf1 | -9.29445 | -46.01479 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c2d6254b-0433-3654-a583-2ecb9502862c | -11.19151 | -47.82379 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8c0dfc0-0c32-3d8b-a63b-92b73397981e | -12.41543 | -51.10527 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7dd4811-d3fd-3c3d-9ae3-1b88257fb004 | -11.06672 | -47.77439 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b609231a-c3c0-3929-b84c-5f00f36bcc23 | -8.65352 | -47.16539 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5888c1e2-d7d7-361d-ac3e-4a342f5729e3 | -7.46143 | -43.05711 | 2025-10-05 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c56f13fe-d3c4-360d-830a-74b41ef295e4 | -10.83026 | -57.19771 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0bd8289-d6b8-322c-b759-6b717271512c | -12.55511 | -48.16055 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 078beccd-d685-3aa1-8eb7-83dc8d8b6e26 | -13.26788 | -47.60382 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87d7c6b7-f3cc-3649-a56f-289a2f37ca86 | -11.7941 | -47.91789 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2262fe47-9124-317a-a4de-02f70d3898f7 | -13.13616 | -50.8772 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c596a923-0ff4-3cd5-a603-771e10afce55 | -13.08149 | -47.91705 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b0545ab-a9f4-34ac-9e2c-3533215b5124 | -12.88992 | -47.29482 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40b2e810-c9af-3707-8cce-daf1b2237aa4 | -11.11137 | -49.85809 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f27603c-f5ec-33c6-9be7-bf121917a420 | -7.05636 | -42.76733 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 991cb210-01b7-3843-9e31-5d3d3b02314f | -12.59795 | -48.16189 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fb1116d-716c-3e05-8f4e-fc11a4f7deaf | -6.58786 | -43.46293 | 2025-10-05 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 504239f1-8d77-3355-b886-3846e06f21e1 | -12.30921 | -55.13385 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11528e7a-90b8-3acc-a000-32036babf1f8 | -7.69258 | -42.59085 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ceba67c3-93c3-3e27-b597-2ea7a4e8528f | -9.29785 | -45.99034 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88cc9bfe-fe0d-328f-bbb5-1bb08d2c5284 | -8.62161 | -54.99308 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d669a07-a336-3bfc-910a-cdad9fd43a40 | -11.00269 | -57.05779 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77e9a2f8-f4a0-3e61-8e57-407bc32a48e9 | -7.44823 | -46.51757 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa9b3872-8f8e-3442-af8a-b3a5d1db4a2b | -13.13955 | -50.87774 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 72fe6a51-4444-312e-bdfd-fc90379120ce | -12.65351 | -46.98895 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e06c928-a971-351c-b330-45b356d9b91f | -8.62966 | -54.99309 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d5ccc42-6439-33c4-86cb-3bd81b9d3613 | -6.71498 | -42.83142 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 866821f2-448d-3e58-9822-7f31f0aa1eab | -10.74045 | -47.89686 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d8a1854-53b1-3865-a492-7eab41c51cc1 | -6.4642 | -44.58484 | 2025-10-05 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dee496ca-9865-3e8d-abee-45f8e7c88260 | -13.58796 | -48.1599 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7621c71-6d33-3162-b83a-711703439ae4 | -10.46619 | -47.81448 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21297754-20c7-388a-b7ae-ae99a7e21485 | -13.51681 | -47.2938 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README83.md)
