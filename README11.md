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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6878786-0bcf-3225-802d-874d2afe2ddd | -16.65382 | -41.89101 | 2024-09-26 00:41:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d034b07c-b866-37d9-b229-919ed989e296 | -16.58683 | -46.96906 | 2024-09-26 00:41:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f210d21c-df24-3ed3-8bdc-ef3f5e2670c1 | -16.58517 | -46.9556 | 2024-09-26 00:41:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 630a540a-9377-3b5c-ac9c-174d4739da74 | -16.51777 | -47.01799 | 2024-09-26 00:41:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f4c0678b-5e2d-3c33-bb7b-ca42466291fc | -16.51618 | -47.00441 | 2024-09-26 00:41:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a9662a91-c49f-37f1-8830-ecfb0f41d63c | -16.51114 | -47.01132 | 2024-09-26 00:41:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 42.4 |
| e4ede942-e457-3034-a6a0-fbfe45cfa3e2 | -16.50955 | -46.99848 | 2024-09-26 00:41:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| aaaaefbb-3600-3e63-b925-f7c1bcda2676 | -16.45444 | -49.03131 | 2024-09-26 00:41:00 | TERRA_M-M | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 748ddefa-7780-3298-a617-2e7daa5c3f94 | -16.36123 | -47.74129 | 2024-09-26 00:41:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4ab91925-1eb5-3646-9ad3-140aa1aec018 | -16.34671 | -47.71332 | 2024-09-26 00:41:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 960e96c0-0a18-3e39-8a63-c78b3fb4caa0 | -16.32205 | -45.67338 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8d7ecee9-8eca-3d9b-8d21-920f1ed07c3f | -16.2728 | -40.99776 | 2024-09-26 00:41:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| a9f6e568-3671-3eff-8b7e-0f2f19415aab | -16.27124 | -40.9874 | 2024-09-26 00:41:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 38b752db-c874-3cfa-858a-2e9ab0893405 | -16.11063 | -52.02033 | 2024-09-26 00:41:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| cb976e27-7109-34f6-a7be-8efad0950403 | -15.86086 | -41.95102 | 2024-09-26 00:41:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| c331c723-287a-32d5-a278-076fd2e8cca3 | -15.79938 | -40.98112 | 2024-09-26 00:41:00 | TERRA_M-M | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| bba45621-8de2-315e-9c86-4cb5f8807366 | -15.73871 | -43.90518 | 2024-09-26 00:41:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f2aade8f-2eee-35c8-8f29-990f76e22eb3 | -15.70631 | -41.08208 | 2024-09-26 00:41:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| e4c2046e-8d4b-3be8-857a-f1cb0047e22e | -15.53748 | -45.01857 | 2024-09-26 00:41:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cd575b4a-4fc8-3d31-8242-83a1ef6aaca0 | -15.53695 | -48.50911 | 2024-09-26 00:41:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b3952fa5-698c-32ad-8f4b-e25ba45c9409 | -15.33311 | -47.46297 | 2024-09-26 00:41:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fd5be369-d327-31a9-8c34-e1aa74cd8d72 | -15.32384 | -47.4764 | 2024-09-26 00:41:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f160169e-1241-396e-8db1-d4fb4e094a65 | -15.32244 | -47.46469 | 2024-09-26 00:41:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ace8a526-1725-3753-bc01-9a77eedfb140 | -14.79799 | -48.90981 | 2024-09-26 00:41:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 326fa8f8-0393-3e2e-a5a0-9ff78c86fe79 | -14.68773 | -45.47655 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 712217a5-861e-37c8-bcdb-71bb43359f5e | -14.67313 | -45.48497 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 62dce518-d34c-3735-b3b3-9effcb87bbe6 | -14.67178 | -45.47476 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 32a2473b-dfee-3f24-a1be-9735352f79bd | -14.66243 | -45.47613 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 03dcb5a0-9330-36ed-83a4-7bb917444184 | -14.57052 | -45.69379 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 5c872f31-1939-3ddb-bcc1-67f24df95ebb | -14.56781 | -45.67298 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4dd0a130-8dec-3d16-a085-96211de82525 | -14.5638 | -45.71613 | 2024-09-26 00:41:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e312a67f-6b48-30f4-bf4a-453ab45c8bc4 | -14.56244 | -45.70567 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 93101bc2-23c9-3e04-a7fe-7f1318faaf2a | -14.553 | -45.70701 | 2024-09-26 00:41:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 644b3dd7-9f56-3dc8-9ab2-20d8c903db84 | -14.50927 | -45.63506 | 2024-09-26 00:41:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 15e846d2-e7de-3978-8cc7-d0a2b5e442ff | -14.5079 | -45.62473 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 23ba2614-b471-3442-b6b8-4490cf613778 | -14.45807 | -45.25077 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| dc7e34af-79f4-33ef-9317-c9813923d684 | -14.45674 | -45.24086 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 0c7a926c-5ac6-3ab8-81b1-d51acd5afa93 | -14.45541 | -45.23093 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 0963f5b8-8226-30a6-81c4-018fe2c3906a | -14.45409 | -45.22104 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| aa910286-3131-3bbe-b6cc-ebd19c569816 | -14.45277 | -45.21119 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 53bd8936-1e80-31a5-a988-5836b78008a3 | -14.45144 | -45.2013 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 83982aee-5430-34c9-a170-ef6044960623 | -14.44617 | -45.23217 | 2024-09-26 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 242f965d-34e8-3ef3-aa72-dc3d4972d7bf | -13.90612 | -48.04506 | 2024-09-26 00:41:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b55f3438-4152-3801-83a1-2c7454f28fdf | -13.90259 | -48.03709 | 2024-09-26 00:41:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d9706031-f279-3ee3-9c6b-9a387ca4e02e | -13.82597 | -48.04679 | 2024-09-26 00:41:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5f6756d9-bb66-3653-8120-98766d1d85b4 | -13.78555 | -48.10077 | 2024-09-26 00:41:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 796a4da1-4b85-3de5-b2aa-1466e9a07281 | -13.30622 | -46.3391 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9861c6d5-5a86-3499-93cd-aafe4ceec8be | -13.30475 | -46.32793 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 99a3499f-f7d3-3f4a-827e-922fce11cff6 | -13.27196 | -43.57286 | 2024-09-26 00:41:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2b6e12d4-0692-30ab-a344-740ab76e4c4b | -13.20722 | -45.66406 | 2024-09-26 00:41:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1e79d9ba-c23f-38ff-a521-344002f07013 | -13.20589 | -45.65406 | 2024-09-26 00:41:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 05dda963-680c-3e16-a359-80c12ff11143 | -13.19793 | -45.66534 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed62f05c-4b08-33f9-8015-b44a316589dd | -13.1966 | -45.65535 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 0fb71014-5d92-35c8-8f3f-7aaa9351254d | -13.19527 | -45.64536 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 1463d67c-561e-3972-90b8-dccf9ea8bf9f | -13.19395 | -45.63539 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 2e823161-50c8-344b-b332-2669f6def149 | -13.19262 | -45.62542 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 509d9bce-a040-3df1-8cb2-a3460a488b82 | -12.92476 | -45.34532 | 2024-09-26 00:41:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e7e31043-373a-38c5-beec-9a83e4d4d02e | -12.59297 | -42.42588 | 2024-09-26 00:41:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 26c500db-3546-38d6-ba4e-3af457bc796e | -12.59161 | -42.41637 | 2024-09-26 00:41:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d873f7f3-a9b5-3601-ab9c-c486a02722ab | -13.41242 | -48.04538 | 2024-09-26 00:41:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 66f33bd9-1cd5-3913-b00f-98724a10edcf | -16.00867 | -48.15058 | 2024-09-26 00:41:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b199383e-4a53-3d5c-9618-823c2c840900 | -6.67988 | -44.65399 | 2024-09-26 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cfe8adaa-c08d-3aaf-be21-952f1189ba7d | -6.64018 | -44.96449 | 2024-09-26 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6e435a32-5618-3660-9617-f9c2bfc749cb | -6.63895 | -44.95564 | 2024-09-26 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d37be8c9-0313-3753-a927-68b61121fb80 | -6.40792 | -45.94649 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b271731-da03-3a72-8bba-e9579d237d5e | -6.26183 | -45.08812 | 2024-09-26 00:43:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 754d2cb7-8657-34ef-a151-f8b55e4dc711 | -5.9169 | -44.01584 | 2024-09-26 00:43:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee3ce85d-b2bc-387a-966d-c13a851b20a2 | -13.14251 | -48.54511 | 2024-09-26 00:43:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 4b606f4f-5460-389a-b17b-85b4288412e0 | -13.14181 | -48.53876 | 2024-09-26 00:43:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 80312e00-3d4e-3817-8ba0-871b2f39853b | -12.92188 | -47.70242 | 2024-09-26 00:43:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 81346560-cd36-34fa-a0e4-d11d77b9f8ad | -12.89282 | -51.45623 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 35d0fae3-bf20-3b98-a033-21b4139161ff | -12.8093 | -51.27295 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 402157e7-bd03-376f-9a86-ccc6bc2e6ef5 | -12.80659 | -51.37213 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| eb5efff3-6a28-3512-a734-2a619998ff3c | -12.80649 | -51.24884 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 68414f8c-29cf-3b49-b945-deab166543c2 | -12.80377 | -51.34758 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f7e5625f-d98d-3d89-9aee-0ffe1aa91f4e | -12.80339 | -51.2917 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 98c3d9e7-006a-3816-a45c-9fa4aaf64f37 | -12.80077 | -51.26746 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| bb186917-099c-3283-b935-62d8ed8775ec | -12.79816 | -51.24333 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| cc63758d-b3b2-3ece-934c-e4604e1b8c96 | -12.79776 | -54.06656 | 2024-09-26 00:43:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 89e292e3-1c2a-3f2f-9660-819711c85190 | -12.79258 | -51.25047 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 4e7792ec-0d7a-34de-8e06-3fa188d6af99 | -12.79255 | -51.37376 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 01a9bb16-aaed-3029-9e25-d1a4ccafd3fb | -12.78975 | -51.3492 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| a8ecfafc-5a1a-3d20-ab4c-cb3de9205ec2 | -12.77593 | -51.22808 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 71eb269a-915e-3351-b538-c9b638f8264c | -12.75899 | -51.32806 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 98681bf1-72ac-3109-90a4-76adf2ec5aa8 | -12.75384 | -51.33382 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| bb73cc0d-2a28-3bb4-a828-f868a6662c47 | -12.75095 | -51.30949 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ce4d1bd6-ae59-3cf5-a693-387aae880d2e | -12.54078 | -53.4944 | 2024-09-26 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 80ffa745-c3a8-353d-a765-c9879ad63ed6 | -12.53439 | -53.5018 | 2024-09-26 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 4d14e38f-899b-38cf-a185-451f4a73918e | -11.46611 | -47.32315 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4ca646c2-0463-3ea2-837b-454d4c3e30b9 | -12.52801 | -53.53189 | 2024-09-26 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 557d2ecd-05f6-36f3-be1a-1d094de59ce3 | -12.52432 | -53.49628 | 2024-09-26 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 98a44113-ecf2-3329-bbf5-bd376c100127 | -12.51791 | -53.50353 | 2024-09-26 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 5ea6f482-81f6-35ab-9f00-8198831303a8 | -12.50785 | -53.49807 | 2024-09-26 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e671cba4-7713-3d8a-a926-435d59163c80 | -12.50144 | -53.50526 | 2024-09-26 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| e66192a4-6331-3156-ac78-a52ec0298f6c | -12.17796 | -46.74541 | 2024-09-26 00:43:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 5e380c85-bedd-3050-b4e8-abdadc900585 | -12.17628 | -46.75132 | 2024-09-26 00:43:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 427f26c5-2545-3ec7-b1e9-b8979d5a526c | -12.17481 | -46.74024 | 2024-09-26 00:43:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bb57a63e-77c6-39b7-b341-8abe9b7defa8 | -11.94404 | -47.31292 | 2024-09-26 00:43:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9638145a-123c-3f50-ae61-727663097a35 | -11.93396 | -47.31429 | 2024-09-26 00:43:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3f992a92-7355-31f3-8546-1a494e3b6a3b | -11.85866 | -49.63738 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README12.md)
