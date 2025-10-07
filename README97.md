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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9ee36f1-4a9e-3be8-837c-99d426fdbc2a | -14.71851 | -48.35019 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f870b83-d1d3-309b-afac-cd37a3996d97 | -9.39807 | -61.4385 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39a288ef-0a48-3bba-bb12-6bcdd75d4aea | -12.89403 | -54.75948 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c66d79ab-be84-3ccb-bf77-50927d4e6f9a | -14.73889 | -46.03084 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 79797422-c15f-3af8-8248-ac5a0921244a | -15.60712 | -47.30169 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1eefef4-2e40-3109-87ed-fd75937ad19f | -10.35457 | -56.33295 | 2025-10-07 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef3d40cf-7343-36e4-8976-2d2c57bba88d | -7.43435 | -63.75073 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34133b03-2eed-305f-92ce-ac0815d41b07 | -11.87116 | -56.88973 | 2025-10-07 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fbb4b97-88b6-36df-b75f-2535127a8f51 | -10.39202 | -45.38091 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df63919e-0ec4-3bf7-af1b-130da01610f8 | -9.55434 | -63.50892 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628ecd3a-9dff-34d0-ba10-aeeadd3b16ed | -15.2914 | -46.33153 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85c7af20-f459-3867-8ab3-2a287d57d919 | -13.09256 | -48.00529 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2d701082-bcec-31f2-b856-b1f2afd7fc5d | -9.19386 | -47.816 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72a8abb7-739d-34ef-b039-776f74000334 | -11.38722 | -43.49379 | 2025-10-07 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e9723fc-7473-3416-ad62-73e05358b772 | -15.21736 | -49.29657 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c451600-d92d-34d9-af86-63a051e28b7b | -10.08851 | -48.17704 | 2025-10-07 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b1eb9a6-d235-3707-b6ee-417e4bed8dfc | -14.9406 | -46.81165 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a90d2242-bc13-3d9e-8331-7f9653445961 | -15.12022 | -43.86753 | 2025-10-07 04:57:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 630d9b05-68a5-3645-85e7-fd2f5dc2d14d | -12.06367 | -51.21029 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c12bab70-0be2-39c3-b35d-f367814e39e4 | -11.1675 | -47.73807 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed00454b-6ef1-3aa8-840e-62c84bbf1b56 | -11.80658 | -45.05648 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65c0a430-f2e5-337e-8aa4-e83c3c76819b | -10.44713 | -50.34699 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| deeee29a-c6bb-3407-a565-f3fc62c737dc | -13.07569 | -47.83488 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8630c2c4-0e11-35f2-aa79-8624857e6c8b | -13.22718 | -51.6867 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5c34434-8091-3fc6-b886-4438424f5726 | -10.81188 | -48.81424 | 2025-10-07 04:57:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b5b68da-fc60-3372-ac49-298a36b9950f | -10.64689 | -58.76482 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bfae28f-25b8-33a0-ad8e-cc6a29114929 | -9.91779 | -49.96197 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 511a1313-de53-3f3e-901d-c3f6ccb34b7d | -9.38699 | -59.42706 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65c3dbb6-f6ed-369f-9e90-bdf54993057e | -12.31953 | -55.11377 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b446f633-2f83-3c9f-ac3c-de527d2e7455 | -14.7628 | -46.01917 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac982de0-4586-31fa-a5bd-3bb450420b75 | -9.92178 | -49.96256 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c3dc42f6-0f69-36c6-b25a-49cedd2e152f | -11.41654 | -55.0691 | 2025-10-07 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470cb61d-44f3-3408-9601-611da8a68510 | -9.01807 | -63.65995 | 2025-10-07 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1845b243-7a3a-3be5-971b-7eb7154aa3fb | -13.27578 | -48.05886 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c1e29e6-632c-39d9-a557-34af821c9280 | -13.33708 | -47.76313 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd2d70f3-2a4f-3bf4-80f5-4b7c4a002c38 | -10.36038 | -57.85593 | 2025-10-07 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28255876-c1be-3452-9269-8eb60d189e95 | -10.39001 | -50.3007 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b4cf7a1c-5b58-3e4d-b3e5-45b289eedf4e | -9.61186 | -51.09146 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3b1c1f8-e65c-37a9-a038-c30deda415ee | -9.14494 | -61.23627 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37d4f49c-df87-36ee-93d9-bd7e2c675d45 | -9.76669 | -62.32507 | 2025-10-07 04:57:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d731224-d6e9-38b9-93f7-74f7ab7f6bad | -10.80807 | -56.24105 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9db107c6-a9ed-30ca-9792-ad85dc6c995e | -11.47157 | -43.49323 | 2025-10-07 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6781797c-925d-3d98-be16-be27b71308a7 | -11.13038 | -47.22159 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f1bc5a78-fcaf-3690-ae2d-43bcb1636864 | -10.39075 | -50.29565 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 012ee670-fafd-350e-a274-f33b45d9acb0 | -15.38847 | -48.01023 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c1bf9542-011d-3fd4-aaf0-95a84c32904b | -14.63333 | -52.50064 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfaeac78-19b9-3e9c-8084-537e6f6b8da9 | -9.51314 | -54.75552 | 2025-10-07 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da2e4298-c4e6-344b-aa13-c30cbe4d77d6 | -14.90554 | -46.83671 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1282b2af-5787-309e-9b37-8f42bf963379 | -15.38985 | -47.99895 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd02589f-142e-361a-b0ee-b1660b8ef66e | -8.17927 | -50.30161 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af07ca5b-526e-32b3-8586-e2c2b1bbf24b | -10.43608 | -50.34024 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2576aca-6b4b-32ba-9696-57e4f9205593 | -9.25502 | -59.02453 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b18f6f2c-21c6-3ad0-b862-831557a45c5e | -7.41301 | -63.03312 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cb65cd6-2838-3f32-a20a-18339655c8cf | -10.4132 | -45.38921 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19d48043-f100-309c-98dc-a786ebd98a24 | -11.0317 | -50.92425 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ff15fe9-4d69-3a45-ae09-f5bccf8cded6 | -14.76911 | -46.06173 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 399a3bf7-4a21-3630-8b71-56c28520f8bf | -15.11324 | -43.87229 | 2025-10-07 04:57:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 789014f6-4700-3be8-afd2-b815d9b07b19 | -11.50538 | -54.45535 | 2025-10-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbe06d21-54f1-3d6c-a213-def6ba93cdad | -12.92728 | -54.72092 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 507d7683-7cb2-3165-818b-c156e2bcd4ca | -10.36088 | -57.83091 | 2025-10-07 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 658b1b08-6235-3028-9ae8-f02365393746 | -9.14198 | -60.62772 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 334b3ce2-7d0b-3124-9a20-5e2ab75e2b98 | -8.84341 | -46.09605 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94c9af30-8618-339a-83b9-3d16a579db96 | -10.88099 | -56.06565 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba89cee0-621d-342e-8fe2-7750cf5c0e2c | -10.25506 | -44.38371 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b905aa62-e4ad-380e-bf67-bb577d2e1213 | -12.38214 | -51.08731 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b2237df-ad16-3298-ae2e-b0c565bb08da | -15.88233 | -46.2504 | 2025-10-07 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3492891-7c3c-3cfb-888d-4dfb205fd63f | -13.97067 | -53.89202 | 2025-10-07 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b09e578-d18d-337e-bff8-88fd96576495 | -12.48452 | -54.73089 | 2025-10-07 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc45976-884a-3e2e-91b6-c56739071dad | -13.29554 | -48.05567 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e63d2562-72eb-303c-bcde-bf3f69fc2733 | -11.81955 | -45.11247 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc07da03-6d9f-3cf5-aaf4-10c421cf8202 | -13.26411 | -47.16495 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2f29c5a-89aa-3744-b1f9-af241e723abb | -10.62532 | -48.70761 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a04ee5e-e151-3a62-8b4b-99ba60f1c4d8 | -10.40182 | -50.29917 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 041f33d2-1fcc-3014-a61d-9013e6e28f85 | -15.26962 | -48.06552 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fb6e74f-cb1c-3acc-94eb-6a101daec27f | -8.86919 | -50.88605 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e874a973-9adc-3ea8-b412-c1806ca69ea0 | -14.75212 | -46.01389 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53f717b0-498d-3314-ab61-9b8376080ac2 | -12.61705 | -44.75559 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a05702f-e223-36ed-af3a-20a194582d75 | -8.93749 | -49.85952 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f294e8da-d970-3b11-8bcb-c58615e20131 | -12.9101 | -54.7438 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc1342db-eab7-354f-a6cc-d15ab47f850e | -10.40388 | -45.38015 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8b3cd61-51c0-345a-9ee6-736de62a4f11 | -12.24189 | -43.78067 | 2025-10-07 04:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ada8a924-1231-3d62-bd5d-cf8681500527 | -14.73333 | -46.0302 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8d344c6f-b83c-3029-b981-47dbcf1c21a3 | -11.06454 | -49.56191 | 2025-10-07 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6042beaf-d008-3422-81e9-bd23c2aef19c | -14.76663 | -46.03472 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6af575cb-8647-30c8-94f8-673e83576aa3 | -13.02511 | -51.03802 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 690cbafd-5af2-367c-9077-36a705e8c77f | -12.93894 | -54.73378 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea6899cd-c461-39a1-80e0-31c171cf59e7 | -11.15985 | -47.95452 | 2025-10-07 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d73a224-31fa-3fc0-9c5b-98416b18c7a2 | -13.27914 | -47.16081 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b97528ab-1648-3d28-b634-cfcb1e9fe69c | -14.90557 | -46.84343 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d248abb6-670f-3d55-8dea-65feece5b5da | -9.67502 | -45.6701 | 2025-10-07 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ec4af85-bfd8-3e53-85ec-440964deb6b7 | -10.78925 | -48.59098 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3fecdb6-16eb-3498-8ed2-48ca86e77935 | -14.61556 | -52.54739 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9224592b-8815-376b-a646-42eaa8df1f97 | -9.60549 | -57.13651 | 2025-10-07 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e508e5d4-31b6-3539-8b99-54e4cd132080 | -10.6783 | -54.68806 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 341a7d62-6a5b-36af-919e-0b6304c23f2a | -10.27359 | -44.3779 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 310f48ef-a6b0-3652-a866-55d25fd2a924 | -9.04001 | -50.59688 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82327822-be77-3df5-a7a0-8e1a83b5b31c | -12.9395 | -54.73021 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5896ea7-0810-3330-b5ef-6d4b1b23375f | -10.42005 | -50.31216 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cc47198f-27c0-3574-9f61-1acd1cd17a60 | -14.93606 | -46.80441 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ce89829-a7b0-3aa4-9fa8-3e1fe9e71ab4 | -15.11572 | -43.86691 | 2025-10-07 04:57:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README98.md)
