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
| d9a0b222-e604-3e5a-9b23-71af8e11c39b | -11.3588 | -46.4941 | 2025-09-11 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 69a8371b-2666-3c14-89cb-b08567516f69 | -14.2758 | -53.0866 | 2025-09-11 00:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| fba7014d-b859-303e-88d9-8f1efbbc2245 | -11.358 | -46.5393 | 2025-09-11 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| be636c3b-478e-3265-a207-5f6a81e6595a | -12.3976 | -63.8048 | 2025-09-11 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 90c1d228-2f40-3442-9e3e-a18ab341f12e | -14.7527 | -60.2321 | 2025-09-11 00:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1d67f4d4-f763-34dd-adc9-e9a0dceb50b4 | -13.1648 | -45.2665 | 2025-09-11 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| c61cd96f-d555-38c3-bd53-2ad054bd4a5e | -16.2934 | -50.068 | 2025-09-11 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1fa68e7a-c5ce-34c0-9dc2-ec716cf7e90f | -19.0268 | -46.2582 | 2025-09-11 00:30:00 | GOES-19 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1e2b77dd-f8f9-31db-879e-eba84b2fc3a0 | -15.5624 | -54.7662 | 2025-09-11 00:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| fe0a9213-dcca-3289-8586-9e7dbfc97af8 | -20.4039 | -46.2849 | 2025-09-11 00:30:00 | GOES-19 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f2858a19-17d0-3057-85bd-47c7fec4a3dc | -11.077 | -51.3462 | 2025-09-11 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6014c0fc-1e73-3a68-b85d-d60ba6f0d9f6 | -20.6963 | -46.0688 | 2025-09-11 00:30:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dbffc7f7-f4a5-3435-aa3f-fb85c4eb1b80 | -17.3372 | -46.6718 | 2025-09-11 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 52a34f59-3a69-36c0-a6e2-ed48c439e875 | -13.145 | -45.2929 | 2025-09-11 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 07317388-07c0-3fdf-9d15-d3f7389fd0cb | -14.3074 | -54.7492 | 2025-09-11 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 87754088-c6f4-3072-b761-069705b812c2 | -11.3775 | -46.5142 | 2025-09-11 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 39f36685-5712-3ea9-9531-9a57fe408ca8 | -15.2529 | -44.0176 | 2025-09-11 00:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 3cc60da9-6795-30c9-85fb-0578429adbaf | -15.1371 | -52.4252 | 2025-09-11 00:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 76b84c3c-e917-331b-b5f6-4691d1d0778d | -11.058 | -51.3482 | 2025-09-11 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ac48f8ea-e785-3058-942b-413e44cc25c8 | -12.4165 | -63.8038 | 2025-09-11 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ccdba7dd-541a-3842-9b77-5b90dc26e7ab | -16.3136 | -50.0427 | 2025-09-11 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 9ba4fbdc-abde-34e1-b00c-a67f88fb2169 | -10.0152 | -51.7241 | 2025-09-11 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 25fa86a5-53ef-3246-a8a8-0671f9918b02 | -12.4164 | -63.8229 | 2025-09-11 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b843638f-ffaa-34bb-81de-37e9fb9d92d4 | -11.3584 | -46.5167 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 272.0 |
| e7133e98-9ff7-3528-8ae7-4939b39e3a48 | -14.3077 | -54.7285 | 2025-09-11 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 94dfb8cf-4ff1-322a-8927-1eed3c24012d | -12.4164 | -63.8229 | 2025-09-11 00:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3ef0d5aa-d806-3e76-a5bc-b35429854175 | -14.2881 | -54.7514 | 2025-09-11 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 45836b51-281a-3cdf-a59a-4d4b413649be | -13.145 | -45.2929 | 2025-09-11 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 103da4f1-50cc-3758-b1ac-d9a3cb60a4a1 | -10.0152 | -51.7241 | 2025-09-11 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| ee508db7-bb26-3ad1-81a1-537a51f9c24b | -20.717 | -46.0636 | 2025-09-11 00:40:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 5285481a-f7c2-3453-8d1a-99a5373cd09c | -12.3976 | -63.8048 | 2025-09-11 00:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ff3aa49f-05cb-353e-8b32-711df44b5c7e | -19.9994 | -47.6271 | 2025-09-11 00:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 24033611-9ab8-3f2d-bef3-798e00dc3596 | -7.2374 | -55.0604 | 2025-09-11 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e0a21d57-c872-35b6-8996-58ab3700fd71 | -13.1648 | -45.2665 | 2025-09-11 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 88fbff6b-46bf-3bd0-9e2c-2f6cab4f3c52 | -10.1637 | -68.1583 | 2025-09-11 00:40:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 557ca2b9-84d3-3842-96d9-c07ffe71ae15 | -9.0234 | -49.762 | 2025-09-11 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 368f6b0d-fd4d-3e67-bfe9-1e76417f5f2c | -12.4165 | -63.8038 | 2025-09-11 00:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0f815615-d824-3589-8606-2839f548c8eb | -14.2758 | -53.0866 | 2025-09-11 00:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4533d2d6-cbe4-3366-97d8-af85efa19687 | -10.3171 | -48.8127 | 2025-09-11 00:40:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| af1905a8-f43b-3c2c-8f61-ae2d0c9567bb | -10.123 | -46.4926 | 2025-09-11 00:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 5c81ba34-11aa-340c-bc05-9d5d2440e3f7 | -3.1773 | -42.7907 | 2025-09-11 00:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9fd75ca4-ffbe-3b4f-92d4-1f2c57b35bc0 | -15.9865 | -42.9719 | 2025-09-11 00:40:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 193.6 |
| b7d8727d-6e87-3e1e-98e2-9f818d6d5349 | -15.9858 | -42.9964 | 2025-09-11 00:40:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 119.5 |
| fc7fbc70-022a-32e1-9b34-a05307f98b81 | -14.2754 | -53.1076 | 2025-09-11 00:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| aaf65352-21d6-3c2e-8ac2-c781927078e1 | -8.1947 | -50.1108 | 2025-09-11 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 76f2b709-21fe-3fc5-baca-6a911550de58 | -9.0753 | -47.078 | 2025-09-11 00:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3c178d5b-b325-39dd-ac80-de77c78621c5 | -11.3775 | -46.5142 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 0412acad-0c3a-3c49-b959-48f5c52db08d | -11.3389 | -46.5419 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| dec36808-e170-35fb-b246-c9153be47785 | -10.034 | -51.7223 | 2025-09-11 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 2d30a1c3-b2f1-3ed4-a405-11859136790d | -11.3393 | -46.5193 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 65ca9076-9656-3cd1-930d-b2831264872f | -12.4697 | -47.4864 | 2025-09-11 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 671370a7-1c49-33e6-b48f-9d0b0adb37a8 | -3.1771 | -42.8141 | 2025-09-11 00:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c9022667-3879-37a1-8039-89a5c6cfd03c | -11.0393 | -45.0564 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5c6f5e6a-408a-3ee6-808c-1a78bb626087 | -19.0268 | -46.2582 | 2025-09-11 00:40:00 | GOES-19 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e0ad5c9d-915b-3466-aa86-7638a3a65ead | -11.358 | -46.5393 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 78fe3d43-a0af-3f1a-8c6e-c1590ae46392 | -11.3588 | -46.4941 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f7b88c7a-3767-3c57-9e8d-0c2752399140 | -22.5888 | -51.8985 | 2025-09-11 00:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| 0de6e95d-0351-3540-9fdc-069c523b1653 | -19.2016 | -47.9889 | 2025-09-11 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 5afd312c-e641-3272-b275-0f57e57017a3 | -10.3885 | -50.5264 | 2025-09-11 00:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 19a099b8-b46c-3a7f-8ca1-a1465cc61f7d | -19.979 | -47.6318 | 2025-09-11 00:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 1c98d08d-ed5e-3227-95e8-43b6806824f3 | -19.2218 | -47.9845 | 2025-09-11 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 38c6b04f-608f-384f-8660-7063e9acb645 | -12.3975 | -63.8239 | 2025-09-11 00:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 0db252d3-b3df-3bb6-9c79-f19364286a29 | -11.5468 | -49.041 | 2025-09-11 00:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2a0c82fe-d06b-3006-9731-548f86675d2f | -16.3136 | -50.0427 | 2025-09-11 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 69d72f05-26af-34e9-8541-3a4187e4f2e1 | -12.1335 | -44.8508 | 2025-09-11 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 29723a31-daaf-3422-a3c1-43053f3eacda | -12.0086 | -47.5945 | 2025-09-11 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b145c4cc-b8bd-316a-b044-efb26b0dd04e | -19.2415 | -48.0033 | 2025-09-11 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 20dbaab2-19bb-3a26-955a-e06ef9eac429 | -9.0232 | -49.7834 | 2025-09-11 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0ab2771d-285e-386e-af3c-e20adc84ea34 | -14.3074 | -54.7492 | 2025-09-11 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 849d782c-e893-3dbf-8bca-3c6504ec89c3 | -14.3071 | -54.7699 | 2025-09-11 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 891ad0af-8ada-3198-982b-fb1ad6ca6601 | -15.1371 | -52.4252 | 2025-09-11 00:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4b4f9561-050f-342a-b54d-630a70b2fb6c | -13.1644 | -45.2897 | 2025-09-11 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 0d746e26-fe37-3b62-8725-5445a8d8fab1 | -9.9964 | -51.7258 | 2025-09-11 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 07164919-a3fb-31d0-8ff4-d2274dc954cd | -20.4047 | -46.261 | 2025-09-11 00:40:00 | GOES-19 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0cf90023-748d-32f0-af0a-8423f10d12de | -20.4039 | -46.2849 | 2025-09-11 00:40:00 | GOES-19 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2f6111ac-1862-3dce-bac1-4e88b08a500c | -10.015 | -51.7451 | 2025-09-11 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 6ba7b982-5184-38e0-a840-6f7ac88b3ae7 | -6.3226 | -53.4553 | 2025-09-11 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e9f3bcb5-0e36-303c-8567-3cf37764c818 | -10.3361 | -48.8106 | 2025-09-11 00:40:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| ede77d74-ba79-3c8e-afbe-744392d5afb4 | -10.0338 | -51.7433 | 2025-09-11 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7721d5d6-7041-3e92-bdbc-d812e64d0c16 | -11.0201 | -45.059 | 2025-09-11 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 4e258799-3a76-3b6e-8b33-9ef5dde2b2ee | -22.5894 | -51.8759 | 2025-09-11 00:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| e6c53c37-5d33-3269-ab90-7dd076c94c25 | -11.1621 | -52.053 | 2025-09-11 00:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0ff40c06-b5ca-3659-b45c-12ce0f6d9654 | -19.9994 | -47.6271 | 2025-09-11 00:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3ac94544-ff85-3844-8859-7ffa9bbf2efd | -15.9858 | -42.9964 | 2025-09-11 00:50:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5b41cedb-c152-3717-8f31-aba5be4c471e | -10.0152 | -51.7241 | 2025-09-11 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| d4fe3ee0-b01a-35d6-84b8-e1772f239b82 | -12.0086 | -47.5945 | 2025-09-11 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 42b3d24d-1429-38c2-bbd2-71377c0f1579 | -7.5597 | -48.207 | 2025-09-11 00:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 803ac8ca-2c49-3599-806a-244c40796039 | -12.4164 | -63.8229 | 2025-09-11 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f061c967-b866-30d5-9a49-01bf322d158d | -15.1371 | -52.4252 | 2025-09-11 00:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9291b855-471b-39c8-9ee3-6dbcd6470e4d | -14.7334 | -60.2337 | 2025-09-11 00:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a38a8781-8a44-3c19-aa91-432294207f35 | -11.1621 | -52.053 | 2025-09-11 00:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 9f69e55f-dd4f-32af-9ebf-1541a3bb34e4 | -10.0338 | -51.7433 | 2025-09-11 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| d6e237ca-a37f-32db-a7fb-431ca7a175a5 | -17.3372 | -46.6718 | 2025-09-11 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 66d60df5-18d4-39e2-a4eb-22278bcfaa44 | -11.181 | -52.0511 | 2025-09-11 00:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 739fce43-272d-3270-ab91-6f90aa898f5c | -14.7527 | -60.2321 | 2025-09-11 00:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f20ccd73-bb3a-32a7-be9c-44858a51bc11 | -10.1637 | -68.1583 | 2025-09-11 00:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2b4df884-b222-3099-a612-dc28346b33e3 | -22.6103 | -51.8715 | 2025-09-11 00:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| b1ca9f60-c8cf-3adb-8081-58ec5594bc6e | -9.0232 | -49.7834 | 2025-09-11 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9cbab791-560d-3a18-b2a7-c9af9012723a | -10.3171 | -48.8127 | 2025-09-11 00:50:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 826bff89-924b-3fd7-aa22-1577ffb7d769 | -11.0201 | -45.059 | 2025-09-11 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |


[Clique aqui para ver as próximas entradas](README4.md)
