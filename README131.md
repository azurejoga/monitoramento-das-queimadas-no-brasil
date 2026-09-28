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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 665cd130-d044-3b4a-b238-f19cc81a7933 | -11.6797 | -43.51328 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 040b1bff-bda8-3607-9891-7093bc815320 | -12.68557 | -47.36481 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 42d5781d-b674-3159-8364-534dc8ba73ed | -13.76105 | -48.52523 | 2026-09-28 17:07:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eca07698-94cf-3e5a-9b06-ccd7bbef15a0 | -15.41141 | -47.90529 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed6b64ef-301f-39a9-98eb-33d130ff98a6 | -15.8279 | -42.56248 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| c46d552d-39c3-3d9d-b3d8-c4dc6bdd7cb1 | -12.05272 | -46.48391 | 2026-09-28 17:07:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4bbbefb2-8a17-322f-a519-64ac754dfb56 | -13.04861 | -46.91232 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f80fca3d-8abe-3330-a090-6b6902a6332c | -14.8683 | -41.0224 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d3db0f46-ae01-3f68-8df4-8bb981b8d646 | -12.4367 | -44.14239 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a0b216fd-a333-32dd-9b27-1c754230d160 | -16.33797 | -47.69682 | 2026-09-28 17:07:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c21b9ad8-3874-32d4-972d-886925605e9f | -15.13169 | -43.62519 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 6e4d74c0-5a08-3093-8e6c-c51b0c28ab57 | -13.49055 | -48.02672 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5cbbc74e-24eb-3701-b227-1dcbbf88a7ee | -13.17883 | -48.54953 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 88e8d661-c457-39f9-8fa7-9a0f5e1dabb0 | -14.07605 | -46.33022 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6fc617be-aaaf-3e72-a10f-7fcac36172c0 | -15.11308 | -54.70908 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b4243966-1f49-3112-92ae-7697e48ede90 | -11.43891 | -41.98787 | 2026-09-28 17:07:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 48.5 |
| c4ba2a3f-10f2-36a0-83ef-ca1d63a91ca1 | -11.70069 | -43.46878 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 056ca5f4-184f-3546-b655-9590db99b6dd | -13.16242 | -48.55191 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e4f210c6-c24e-3a28-8002-b4f046233e20 | -14.63712 | -52.11518 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2a5db8a3-bb24-382e-a382-7996edb6fea0 | -14.5331 | -41.15899 | 2026-09-28 17:07:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 9e634c27-9826-3abd-aa87-bd8c8fb9cfd0 | -13.67876 | -41.01954 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 0392dbec-346b-340c-a9fa-c033dfcacbb9 | -12.51637 | -49.97831 | 2026-09-28 17:07:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 2af04f0c-296f-30de-95a8-ff7b42628eb3 | -13.14884 | -48.54297 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2af783ab-92e7-37f7-8995-de044ef71ab6 | -16.69235 | -50.6658 | 2026-09-28 17:07:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48cb89d6-6630-35d2-b90f-4f2094a457e0 | -17.15774 | -44.701 | 2026-09-28 17:07:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a37f8513-386a-345c-be9b-8bcedbb8be7b | -13.34674 | -51.32545 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 7001e215-8da7-3032-a679-a23ce8da3079 | -13.67902 | -41.89408 | 2026-09-28 17:07:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e527d680-7095-3e79-9dc2-f8c7cf0be26f | -11.90642 | -47.02362 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7d618eab-f78c-3145-866b-72d3a905bb1d | -11.39566 | -43.4432 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8f904b31-e108-32f8-ab2b-c0794878f7b6 | -11.38552 | -43.42239 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d993e5e3-aef2-3237-8cbc-4dcec800134c | -12.96956 | -51.08453 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 3e7aefc8-e6b4-33f0-a2ee-e327abbc0ca4 | -13.39919 | -51.31647 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbc612f7-0374-3f36-9c4d-0fad8f08669e | -11.26915 | -43.5353 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 72097ea4-bb35-346c-b630-2fb87acfb132 | -14.49469 | -45.23925 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a4381c73-1613-379a-ae07-129d1d3fc9c8 | -14.74954 | -41.96108 | 2026-09-28 17:07:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 2bf0a761-11fc-3b5f-be47-2097b93c94af | -16.35294 | -42.57009 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 6ff4467d-6be8-379a-a84c-d776d3107175 | -15.80515 | -47.83502 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53dc9339-fcf5-3ca9-8851-f76d9417278d | -12.67428 | -47.35303 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| ae41fe6f-6aa6-3d1e-b28d-41cdda3bce72 | -11.6789 | -43.50909 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| db72a5da-aa4c-3227-aba1-00f09c07e516 | -13.1113 | -47.41401 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 12a788a9-9f4c-374d-9f9f-0c72c7fa5cc2 | -18.76727 | -47.61553 | 2026-09-28 17:07:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a4d54ecb-03c8-396a-9089-b52e7427b9c5 | -11.60889 | -44.13767 | 2026-09-28 17:07:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 762accef-d330-372b-bc4e-701070d188db | -16.44875 | -43.37352 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1534c292-88f2-3694-9f45-c57c2044f601 | -17.33014 | -53.95901 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a454404-4734-3cf9-9d4c-d75842ef2220 | -15.1581 | -43.61604 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 94a88c87-04bc-3a7f-ba13-6875f6a95f0c | -11.3931 | -43.43002 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| a667f439-832d-3830-a6c2-05ef69330796 | -11.68772 | -44.51672 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 55d5bbd0-f648-3b0e-883c-5461db79b6e9 | -13.57151 | -46.36031 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 62e3b895-7e03-3803-8adb-44bc16e94773 | -17.59157 | -45.80589 | 2026-09-28 17:07:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 95609652-8016-3bf1-9b62-1942b149f4b9 | -18.09162 | -44.36238 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| adab78a7-a67e-3e44-8182-b2e93b207a0c | -16.07045 | -41.7595 | 2026-09-28 17:07:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7844eed5-d425-371d-8c91-0eefc171d6d8 | -17.18152 | -47.42074 | 2026-09-28 17:07:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| cb397317-a2f6-3926-b813-98706b5d4f98 | -13.44767 | -48.60162 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f0d0d52d-e18c-3a0e-adec-2c85a342ffbe | -12.63478 | -47.26181 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d181e9ed-3c62-39ee-92cd-98549f508522 | -11.66667 | -43.44505 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ca52da2-2d19-3ea7-b983-e13fe6a19fcc | -12.96111 | -51.07753 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fb673a87-f278-3452-945e-80e618eb305f | -11.66553 | -43.53376 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fe10794f-f356-3dc8-a8ff-007e652e0efe | -14.51278 | -52.48683 | 2026-09-28 17:07:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 93baf095-7b88-370a-b3a0-e7126129ed72 | -15.39634 | -47.91563 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 98904973-5cfd-3eb9-a338-3a025689f09e | -14.45939 | -40.32717 | 2026-09-28 17:07:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| a588fe13-c2ae-3cd9-b62f-e36befa23123 | -15.51823 | -41.64761 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 206ce0ea-1e70-3dfc-a927-1cb1313d1891 | -13.70923 | -48.83035 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d6da30ac-92f9-3738-abd3-5b8ff3dc6bda | -12.74443 | -50.67988 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d677ba01-a60c-31ae-a08c-d4a87019d2d4 | -15.66285 | -43.02701 | 2026-09-28 17:07:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a4935d1-4c0f-3758-955c-ede2f32c0ca7 | -15.86645 | -41.27392 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 7cf7d920-98a5-32ad-8148-8fc403420617 | -17.99768 | -41.91603 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c04d2fab-0d97-3530-8aff-749313b0a981 | -12.1783 | -41.84824 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0d2a8c43-b317-305d-8d85-627acbdf07e2 | -15.43388 | -57.40693 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5d6abbb4-246a-3b85-9a66-cae7cefae4c1 | -15.85204 | -41.26682 | 2026-09-28 17:07:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 5e8440c6-6705-36e5-b2e8-798d2ab50ce9 | -16.69891 | -40.26749 | 2026-09-28 17:07:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| 9826d324-b50c-340f-9c1e-bee1a2bc3f6f | -13.40511 | -40.94165 | 2026-09-28 17:07:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 526e15ea-5ebf-3177-a26c-7318f677cf8d | -14.73877 | -41.05371 | 2026-09-28 17:07:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 7d1957af-134d-3995-b0f5-c8ab7dce3786 | -15.46381 | -46.15578 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6c9be305-b3b2-337c-9778-a69f9d58caf5 | -12.75619 | -47.30614 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e58ee3d5-fdf6-3082-b7f9-697a0d087b6a | -12.67136 | -45.03819 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a49afecc-a3ae-3a29-9109-49357e117e5a | -16.30829 | -43.13683 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5f6ec73d-5168-3a3e-8601-618d4176545c | -14.13198 | -40.67906 | 2026-09-28 17:07:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3fe3a0d7-63e2-3941-b02d-2393e4768b95 | -12.96601 | -51.08514 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 30fdf122-3719-3aa1-98c0-4fe2734c34ad | -17.83151 | -44.38983 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| eed7e35c-7494-31c5-8208-ab995fdafec4 | -11.83677 | -45.0113 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ba28056a-e1e8-3763-a84c-f219de44dbe3 | -11.89878 | -47.01208 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 08d56949-8ce1-3d65-89e3-b375e360cde2 | -15.19282 | -46.149 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ed8ddc81-1e45-3672-9a5e-7b497b0a0dd4 | -12.44073 | -48.21979 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 74e921f7-1fbe-3472-90fb-43608fc48267 | -13.40118 | -40.94587 | 2026-09-28 17:07:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| dc6e0f62-7f30-3d32-bea0-0d8344c9dbcc | -11.90338 | -47.0112 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f5c3fd1a-f328-3637-be8a-37838bda0a40 | -14.52004 | -52.48938 | 2026-09-28 17:07:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 51cb2831-178f-31bd-9a4f-aa646742a44c | -11.9071 | -47.00552 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bd491430-59c2-304e-8eb8-09b9001ba8fa | -18.25502 | -42.96974 | 2026-09-28 17:07:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 64e796a4-3fb8-38c1-a158-5640e61e98ca | -11.91017 | -47.01795 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 12d4c56b-2f8c-30f1-a22c-c277dcec3178 | -18.84525 | -46.90404 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 31362f39-d2b3-384d-9064-77af61c848fa | -11.26428 | -43.53577 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7dd74390-9e28-3b89-a82d-5b77ae2951b0 | -12.72737 | -47.27441 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 654abeeb-ba37-388d-86d0-b532ac80efb9 | -13.56795 | -49.08764 | 2026-09-28 17:07:00 | NOAA-21 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 961fb482-d7ac-3039-a2b3-f9009a336afe | -20.90721 | -57.83046 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| b9483157-f65b-3891-95fa-e62beb222fc8 | -16.79041 | -43.00548 | 2026-09-28 17:07:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3d3b55f8-fea1-3180-953d-d9c0e3a10b36 | -11.67821 | -44.52612 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 14362265-40d0-3d84-922a-0458a734c27f | -11.67891 | -44.52972 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 26d96997-ca6b-3aba-bfc2-53e8eca41f30 | -16.28556 | -40.20121 | 2026-09-28 17:07:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2fb35326-aee6-3db7-a425-1ec27d429100 | -12.96246 | -51.08575 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c88dbfe2-252f-32da-9600-d9ca07d78e22 | -15.11125 | -53.90145 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README132.md)
