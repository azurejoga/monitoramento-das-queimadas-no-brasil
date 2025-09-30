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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c733a968-008c-3391-80d1-fd417157aedf | -7.835 | -46.9986 | 2025-09-30 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 192.3 |
| f677acd0-b74b-302d-8e39-d5ce0390edbf | -10.6419 | -48.6021 | 2025-09-30 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 682b2cc3-4f43-3e32-a837-d07977c85638 | -12.2348 | -47.7863 | 2025-09-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 35fcd97c-0464-37aa-9f74-83fc668b976f | -12.8774 | -45.1742 | 2025-09-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 16df2439-7113-34c8-8f4f-64f8201f0dae | -15.7719 | -43.6714 | 2025-09-30 13:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 114.2 |
| c8926072-4f1a-34fa-abb1-5984f44ffd89 | -12.2153 | -47.8112 | 2025-09-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 47285553-b4f4-3056-8468-38a8bbff1989 | -7.8696 | -47.2606 | 2025-09-30 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6a6969a2-4bbc-352d-9c10-835cd2691f74 | -7.1193 | -45.5417 | 2025-09-30 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 979ee27a-3470-3773-8661-0ab9805835b3 | -12.952 | -48.4185 | 2025-09-30 13:20:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| dd85062c-8fd8-3aef-b0ce-9b4f2476cbe4 | -11.1735 | -54.1242 | 2025-09-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| b8286fe3-d8c3-35cc-8178-98d796a4ce04 | -12.877 | -45.1974 | 2025-09-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 1159d225-122d-303f-ab8b-31a673f6c8ef | -15.9268 | -46.2334 | 2025-09-30 13:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d5297b23-ea29-3103-80c2-3e91d90899f0 | -15.2746 | -49.263 | 2025-09-30 13:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0510a80f-d131-3939-bb5b-06ba47cb245a | -7.9191 | -44.6245 | 2025-09-30 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 2af76b09-f0ed-38b6-87b8-ab9885eb8555 | -7.8348 | -47.0207 | 2025-09-30 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 01b69884-2987-3c0a-ab45-16d2f107d8fc | -10.0531 | -50.1978 | 2025-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4e1e637c-adc8-3a51-b904-0d5c6b37a57d | -6.6567 | -41.4079 | 2025-09-30 13:20:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| b5e66c90-9391-3a2e-904f-9cbfc1bf1eed | -10.1855 | -44.8709 | 2025-09-30 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7e5dd441-070b-389e-bff9-addf7c9f3705 | -6.657 | -41.3837 | 2025-09-30 13:20:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 05ab33c1-00f1-3b9f-b1fb-36e94da5241d | -13.3812 | -48.0685 | 2025-09-30 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6833ba27-7210-321a-8b04-3cfbcc74ad79 | -12.9524 | -48.3963 | 2025-09-30 13:20:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f76ef5c9-4f30-3104-b9ca-7d14d2f859de | -9.2682 | -48.2034 | 2025-09-30 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 86efe5f8-0349-3a38-b5cc-26f0f8c72f0c | -9.7684 | -46.1293 | 2025-09-30 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5f6a13d0-06de-3c37-8464-ca570adbc198 | -10.0339 | -50.2211 | 2025-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b59a0884-1504-313e-b06b-4faf41315ac7 | -11.1948 | -47.211 | 2025-09-30 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| a1bf6a6e-fced-3a43-b4c6-711fa287a56c | -6.523 | -45.207 | 2025-09-30 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 2af2db10-3fef-357a-9721-46a829c647a0 | -6.2996 | -45.066 | 2025-09-30 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 194a544a-a142-3f94-b04b-ebd7efd553b1 | -16.7575 | -51.3482 | 2025-09-30 13:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 52407887-6628-3b5a-9af4-f176e84b94e2 | -6.4319 | -43.0707 | 2025-09-30 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 1f931852-1670-3139-8494-2e0e3c67aa1a | -8.2474 | -45.5037 | 2025-09-30 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 07809d76-19b6-38ee-85c9-a2edd23da40e | -10.0528 | -50.2192 | 2025-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9fd7afcf-7009-33d1-9a61-9f0144ad609e | -10.9586 | -46.5016 | 2025-09-30 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 1d2c6526-f91e-3e00-b0bc-983c913f796a | -7.8375 | -46.7766 | 2025-09-30 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 27f8f8e7-b477-3b17-9ee7-53f2758fd554 | -9.1248 | -47.6256 | 2025-09-30 13:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| bb411b53-8697-3af2-9391-85622c013a23 | -7.9194 | -44.6016 | 2025-09-30 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 389abd89-7f30-31cf-8b22-cb1662a27711 | -10.1847 | -44.917 | 2025-09-30 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 9df565fa-7331-3017-92bb-9a2ae8f286cf | -10.1851 | -44.8939 | 2025-09-30 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 279.3 |
| 461d8cb7-7f54-3b4f-96a0-c1da1d7b9465 | -15.9273 | -46.2101 | 2025-09-30 13:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c5e7b8fe-3aba-376a-9452-2ea4c4f4a04a | -11.2138 | -47.2086 | 2025-09-30 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8cebd87a-5acb-38cc-b61b-ac2accb069a1 | -8.8229 | -46.189 | 2025-09-30 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 39c6ae0f-6563-35f1-b079-c44b9e54d674 | -14.5712 | -48.4877 | 2025-09-30 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d1970599-a215-3a0c-bc55-a1531682b82f | -11.1548 | -54.1054 | 2025-09-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 1dc0832a-8b99-30b5-adb5-5ed0db7c5cb9 | -17.921 | -57.5952 | 2025-09-30 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| c8840f5a-8af9-386f-9616-62c4f747ab0b | -10.8246 | -45.3611 | 2025-09-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5054311b-484a-3cae-8ac9-774413159865 | -18.4862 | -44.0191 | 2025-09-30 13:20:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 8f3cae53-31c7-3fad-9c84-3e89b9da2b0e | -8.541 | -44.6515 | 2025-09-30 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a21c10b3-3b78-34ad-aa3c-df35c27c2598 | -14.5141 | -48.4299 | 2025-09-30 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ba828c87-df94-3068-99bd-d3d77a7ddc4e | -13.8354 | -47.5076 | 2025-09-30 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 27365477-4f7d-32a0-b9c3-67d2b9643582 | -7.8378 | -46.7544 | 2025-09-30 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 8973f081-80d8-3578-bf6a-4ea4f3bff9b1 | -10.0717 | -50.2173 | 2025-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 13a2cae9-cb62-3338-87e5-a10ac3dcf3cd | -9.4007 | -54.6984 | 2025-09-30 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| bb840dc4-eab1-30b0-964d-4d133e046361 | -6.5042 | -45.2085 | 2025-09-30 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 0d43c455-b019-3535-a98e-5c4637dd0f04 | -12.7018 | -45.2947 | 2025-09-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b55f448d-448e-306a-a91e-ff6b1b744bd6 | -11.8868 | -48.0323 | 2025-09-30 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 9fadf78d-1d20-3e36-9f5e-53f87eef2556 | -6.5227 | -45.2297 | 2025-09-30 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 0d033c48-490c-3778-a071-72f28d16d7aa | -9.1246 | -47.6476 | 2025-09-30 13:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d48d338d-9670-3ee9-8f47-c7152ca9bb95 | -9.0425 | -46.7032 | 2025-09-30 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| de021115-1682-3fbe-b08c-9809eeca5b0a | -11.1944 | -47.2334 | 2025-09-30 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8ff1ef92-d980-387c-ae18-59c8a50ea063 | -7.2999 | -42.8486 | 2025-09-30 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| f6dc40b4-2ef0-335d-8324-4e30a0197aac | -14.7166 | -45.2525 | 2025-09-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 273.9 |
| dc7abd62-2b63-38cc-8d3a-a2574954105c | -10.823 | -46.6538 | 2025-09-30 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 580d24ac-424d-301f-b263-f1730ec7384d | -12.2344 | -47.8086 | 2025-09-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 18c95526-7ef9-3b35-b26d-18fb1168ad72 | -10.3058 | -48.2681 | 2025-09-30 13:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| e1cf61da-964b-370b-8ee0-58e06877b70f | -18.2176 | -53.3177 | 2025-09-30 13:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 417.3 |
| 0cb15c43-711a-3012-9599-56668c98db63 | -11.1546 | -54.126 | 2025-09-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 9627066d-bd0e-355d-be33-a6c5376a1f6a | -14.5517 | -48.4907 | 2025-09-30 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| f2667e28-9121-38d1-b205-26a2f3b73981 | -14.7171 | -45.2291 | 2025-09-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 3f6700cb-c81e-3595-98db-8246a6261a63 | -7.8188 | -46.7783 | 2025-09-30 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 5f5d99bc-6ec8-362b-b7f2-c7ec8db8c23c | -8.672 | -47.7144 | 2025-09-30 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2517e629-75e8-30be-bdea-0b643ead7ffe | -6.504 | -45.2312 | 2025-09-30 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 0e71e58f-aa98-379e-9959-877afefd1712 | -5.8612 | -43.8858 | 2025-09-30 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ca07ab57-4e6f-3965-9a54-7d1d3bd29495 | -13.8264 | -47.9794 | 2025-09-30 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 08b12e1a-9277-31c7-b3fe-ba413d4a229e | -14.5323 | -48.4938 | 2025-09-30 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| bdfc3560-bd85-38c0-a08b-2ff6d4911b55 | -14.7361 | -45.2489 | 2025-09-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| efdc949f-7f77-3e81-b223-b2316124c01c | -15.2654 | -49.7273 | 2025-09-30 13:20:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 69131467-8209-3a17-89ce-5740321ecfcc | -18.218 | -53.2962 | 2025-09-30 13:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ea9cd2dd-103f-36a1-b83a-84c5af4d4fd9 | -7.2996 | -42.8722 | 2025-09-30 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 4a5dac2a-f456-31c4-892e-a0646faec37d | -5.9189 | -43.7193 | 2025-09-30 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 87b7c311-b4c7-382b-9fed-39dac2d0d7df | -10.0342 | -50.1997 | 2025-09-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 20f07822-030f-334f-9e21-3f4cb25d4a97 | -14.7367 | -45.2255 | 2025-09-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| dcf6148f-2205-399d-b3c4-8264c62d7080 | -9.4194 | -54.697 | 2025-09-30 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e901b0bf-80ef-381c-bfde-7f48416da4ba | -11.1944 | -47.2334 | 2025-09-30 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2030587a-5963-321d-bd43-7eebdcda103f | -14.6947 | -48.1332 | 2025-09-30 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 813501dc-0a93-3e20-919f-ec2a2fd51a28 | -5.7223 | -42.6826 | 2025-09-30 13:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 456107b1-ed5e-3c03-a7a7-7717df751ee3 | -14.697 | -45.2561 | 2025-09-30 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 0140b74a-4e4d-3064-90ad-5dc4ed2b76ce | -14.5133 | -48.4745 | 2025-09-30 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 51481288-88bc-33ff-a727-5a7ce080d01a | -10.1847 | -44.917 | 2025-09-30 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| b43d52b1-628b-3376-b7f1-a6ce1c4029dd | -17.921 | -57.5952 | 2025-09-30 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| d0a19816-1656-31a9-8675-ec7a4ef8b73d | -7.1815 | -41.6931 | 2025-09-30 13:30:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 77cf7ea7-f96d-3370-8ffb-cd71bec1f12b | -6.523 | -45.207 | 2025-09-30 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 988a918b-c4b7-3a2a-b569-2b2d5faaf55c | -10.0531 | -50.1978 | 2025-09-30 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5bb82163-25b6-37ea-9bf9-284165e32669 | -5.8615 | -45.9551 | 2025-09-30 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 68c076d2-47bb-3cc9-a2fd-1125abc3da93 | -10.3058 | -48.2681 | 2025-09-30 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bbedf181-aeaa-313a-90c4-dfa894504cde | -16.7575 | -51.3482 | 2025-09-30 13:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a69e9825-f086-3a75-856b-4e3f049bd131 | -7.2999 | -42.8486 | 2025-09-30 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 6a93eb33-7a04-33f6-a964-ab3938962bd4 | -10.3828 | -49.5418 | 2025-09-30 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 7f8b20a0-01f9-3250-bd9b-f072a046bbae | -15.2942 | -49.2599 | 2025-09-30 13:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d01e8008-9bf4-3490-b280-31697f2d2be1 | -11.1548 | -54.1054 | 2025-09-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 532431c1-fb2c-3219-a39e-9b059f376015 | -7.8696 | -47.2606 | 2025-09-30 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| e109d49d-22d4-3876-a4df-a8a430d42f2c | -12.9524 | -48.3963 | 2025-09-30 13:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |


[Clique aqui para ver as próximas entradas](README115.md)
