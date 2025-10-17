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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e1eaa47-8200-3b7b-99da-58289f5e1f31 | -13.71341 | -40.9904 | 2025-10-17 04:21:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1727a3fd-6ad3-300e-af1b-7326d3a73e53 | -14.32945 | -51.44508 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ade1c6eb-691a-3d5a-885a-d177afb262c4 | -14.33076 | -51.43098 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 10bf1cec-b8fe-3935-af6c-e51c77b3d2f5 | -12.1737 | -45.05844 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67e2d1df-94ca-305f-b9b5-71701c318878 | -13.3403 | -47.2739 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b386a17-9f7e-3bd1-ab16-09082183f310 | -14.33516 | -51.47433 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3f67836d-6d7b-3ea0-9e85-0cc2f55e34e9 | -12.43042 | -51.3091 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 34569f42-ea57-3e29-a27f-70d63f7ae2b8 | -13.4806 | -43.70481 | 2025-10-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12517498-bb98-3b4b-96cd-f6002e2aa8d2 | -12.78304 | -44.875 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16c3bd89-d728-38f7-917d-d9b48b743e35 | -14.32885 | -51.44147 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 19e3e537-77a5-38f6-97e4-57bfd471ce0c | -11.36313 | -49.25176 | 2025-10-17 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffe84734-36f2-38be-9aeb-520bed8fc26a | -13.29226 | -49.58115 | 2025-10-17 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05f20465-cfa3-38dc-8b22-f457cd40ae6b | -12.09578 | -46.56021 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d766515d-1de8-3859-89ad-799e34f3cc12 | -12.31687 | -47.83622 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29585001-551c-3d0d-a6a6-3f3b98af1fd3 | -14.89655 | -52.42948 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f8b54a7-72c9-361c-b0f5-03561f65a3f6 | -13.70934 | -40.98967 | 2025-10-17 04:21:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1518882e-c364-3144-af48-57dd475c55d5 | -11.8889 | -42.17629 | 2025-10-17 04:21:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19b70b17-4a01-3e42-b9e6-774153e63672 | -13.93537 | -48.68929 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d2b6d40-9d94-3a5a-b9c7-a61416627842 | -14.3392 | -51.43603 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 69d958a6-7484-3f65-80b5-85ce11f7fb81 | -10.95092 | -49.77262 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 324aef71-e680-3c02-a89a-9a8abe9d9eaf | -16.00962 | -42.36707 | 2025-10-17 04:21:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0f8e0ccc-3a36-3b24-9b20-a3d2d058e31d | -14.24111 | -54.89757 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4316b239-96ac-378c-94bd-54cb80956ab6 | -13.947 | -48.69907 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74b863a2-ee89-3b54-a372-b3ad74d42381 | -13.08294 | -43.505 | 2025-10-17 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef52cc0-a5a5-3f7c-8750-365bd350e28a | -14.08608 | -43.62145 | 2025-10-17 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cecfd42e-a65b-32e9-b5b5-ab266705f8e7 | -13.43081 | -48.07938 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fe831ec-3b80-3212-a156-626045fa47d1 | -14.66782 | -47.40424 | 2025-10-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c50eead-59d7-33ce-a08e-e4d96fb0cae5 | -13.42396 | -48.58701 | 2025-10-17 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39dd0c17-4414-3e12-b228-b9aa2261b7e5 | -15.65274 | -48.36338 | 2025-10-17 04:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66efea54-2fc3-3123-b78c-d92667debcdb | -14.16034 | -47.93497 | 2025-10-17 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2139866f-5751-3564-bd22-579819fe552c | -15.65672 | -48.36023 | 2025-10-17 04:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c396478-8509-39ba-bb3b-65b9ad6ca52f | -14.23933 | -54.90444 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28c9d119-018c-36dd-aa5e-e4a837450c4e | -11.17613 | -49.79838 | 2025-10-17 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41c6fb32-2926-3dd1-b633-404989919f4e | -14.34167 | -51.43841 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 21c1a3eb-567b-3bf7-be9d-0a6a30b5a65b | -12.09135 | -46.56675 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e3f9165-9341-3bf5-a365-9bc45906b227 | -13.12966 | -43.68227 | 2025-10-17 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6be2ca5c-2898-30df-ae06-7a8c00691562 | -13.41687 | -46.70943 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39d7b4f3-f541-3994-8b5e-a840699b3491 | -14.23769 | -54.91486 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 142c3219-27d0-3214-ae9e-f52bfde00f5d | -12.45149 | -51.33172 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1968a255-28fa-339d-b0e6-e7bd43ba5875 | -14.33829 | -51.44129 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 3e6226fb-aa77-3210-b127-884a60cc41b8 | -14.33569 | -51.45621 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2653df2a-3252-3728-a791-835b1b9fd913 | -15.05444 | -46.61783 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b7e5fc0-c878-34f7-9841-50efc801908f | -13.48324 | -48.65823 | 2025-10-17 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 565da98b-223f-3088-bf68-e35a1d448aae | -12.91725 | -41.82513 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 626c8764-f2e2-3ccf-a425-489cb02586de | -9.45107 | -56.65763 | 2025-10-17 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39ed7296-8973-3038-af84-790b075d0734 | -11.75391 | -51.1517 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dbebbf7-9ae2-38c3-808f-3471d64b1714 | -13.45346 | -47.94115 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9cbbd62-d632-3735-bd39-2c17f1103eed | -13.9303 | -45.6189 | 2025-10-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d39df583-7365-3051-b075-9c0a54771d71 | -14.31552 | -51.47789 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b2a6138d-b636-3b28-a1d3-a5e5797b1159 | -10.97834 | -47.91834 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cec71f22-0cc8-3a46-8740-8875bdf6379e | -13.92644 | -45.62193 | 2025-10-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69f6b913-ff66-3d39-a235-cbada589b16d | -14.19905 | -44.8128 | 2025-10-17 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61b27147-eecd-3edc-ac06-ed7a0b776825 | -15.11426 | -41.03059 | 2025-10-17 04:21:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bbf4c512-4a91-3433-b200-fe5d1544c940 | -12.58893 | -43.36922 | 2025-10-17 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adfea577-e7fd-3239-988f-cb4798ad633d | -11.95418 | -45.35717 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 789d0951-5b3d-32d3-96cb-f75c5782b15d | -18.72832 | -47.46696 | 2025-10-17 04:21:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44f49a2e-a8f9-3d6e-97e5-0e942d18a62e | -11.97899 | -44.79684 | 2025-10-17 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e9d6c80-7886-3f85-87ad-fcf291a99ce2 | -11.47537 | -45.08976 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fd9e626a-9bcc-3dac-9329-a2a838769a9d | -14.34373 | -51.44963 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a5a1ef61-ce3c-359a-97ef-139338bec53d | -11.1904 | -49.80563 | 2025-10-17 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f17754e-2ffc-31ab-8c7f-df5a2afe1e39 | -14.23436 | -54.90347 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae1d3670-b541-3d96-a88b-cc160d935986 | -12.44726 | -51.30836 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74e3c607-4b06-3692-9afb-dceda529ca02 | -14.33786 | -51.45941 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b1ca0986-a8b1-39b4-9592-61ab63eecf6e | -11.06248 | -47.59452 | 2025-10-17 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c070a110-02c1-31c1-98bf-0eb512ada4bd | -13.24439 | -47.10731 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80348651-a542-3e37-84bd-0681e71b2edb | -15.82433 | -45.76662 | 2025-10-17 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 146ebcf9-e628-3de9-a2f4-ebb5dd8a51f0 | -13.00524 | -43.21955 | 2025-10-17 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4b052d6f-9b7c-3e35-a27d-79da29d2357e | -14.86865 | -52.44049 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e31e835-4eb3-354a-8f35-6d1d6802bd7a | -13.43056 | -46.4944 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a225375-af7c-3b32-a3ce-cc393230e562 | -14.09314 | -43.62254 | 2025-10-17 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15a2ee4-2821-35d2-8209-b3ef97ac4e4a | -10.00302 | -56.11362 | 2025-10-17 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17f06b6d-87f6-3f93-9272-9cfff9c026eb | -13.33629 | -43.63078 | 2025-10-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2982d90-16d8-34ed-bffd-f3310f36864e | -18.00004 | -43.41714 | 2025-10-17 04:21:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a3f1084-7b1f-311b-b894-2e651972bed9 | -14.93394 | -46.71444 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 546c169e-aac4-3ea7-a18e-79946f18d632 | -18.08872 | -42.81513 | 2025-10-17 04:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f2908793-b36d-3407-af32-d5c38915b10a | -10.97615 | -47.91008 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ceaa6d13-f2e3-33c4-9f05-3acc16300b7b | -10.95469 | -49.77327 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 56f01f97-0cb5-37b3-ac79-40c07218e4fa | -12.41996 | -44.19501 | 2025-10-17 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b8e0aa1-a578-3b84-b7b2-ce6b35a30c22 | -13.08162 | -49.34154 | 2025-10-17 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f9a8231-0935-3240-a115-f49c543b4769 | -17.39268 | -46.64908 | 2025-10-17 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab854f66-0ba8-39d6-886f-fbedb38f7641 | -10.10159 | -56.7697 | 2025-10-17 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2935b606-d77f-30b9-8ede-5577dcbae26a | -13.39229 | -47.20529 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44e1b419-3874-3546-ae2f-3a8a9ded50d0 | -16.68729 | -52.12899 | 2025-10-17 04:21:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7a631d1-21f9-3174-97b8-553b32e67fe9 | -14.23491 | -54.90058 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a255b61-33fe-3ca7-90a6-72598a39891c | -13.39173 | -47.20879 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cab6513a-dcaf-3565-8057-eb9d581b9a02 | -14.17048 | -47.93634 | 2025-10-17 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 011e9521-0035-3245-800d-b0003fcca00d | -13.45745 | -44.28846 | 2025-10-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3968127c-c189-3579-91b8-71f57dde3461 | -11.59371 | -44.06927 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c7bf7f2c-6465-3429-8b4b-7cb9482b44a7 | -15.66224 | -48.36883 | 2025-10-17 04:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb69885a-af4e-3dc7-ba82-bd107beed07e | -13.41913 | -47.9388 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1732aac3-369d-3dfd-8aad-cd8ed11afa84 | -14.33324 | -51.47027 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e081ca3f-4eae-3f2a-b1fa-2fde714d7a1f | -12.78249 | -44.87861 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7594a57e-b1a9-314c-8366-fcbe5dcaa973 | -12.30753 | -47.26157 | 2025-10-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 990268e6-59f5-320b-a6a0-d02efbf8acf0 | -12.91048 | -41.82658 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a506057d-cb57-33d1-ba74-0bf82a7740b2 | -11.13078 | -47.47993 | 2025-10-17 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b5cc955-ccb7-3c7e-bf50-19eef0f34e84 | -14.4164 | -47.88283 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b36c36-e2b6-3d2b-9420-674d99c4a21b | -12.16651 | -45.06096 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c9ebd61-7972-38c1-b893-fe485c76b746 | -10.95629 | -49.76395 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a63aea7f-8d2d-3da9-9573-88321f9df828 | -14.32469 | -51.47232 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2377020-f48c-3c98-8715-4c4b1d7d385f | -16.66049 | -51.55839 | 2025-10-17 04:21:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README68.md)
