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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66e337d8-5b8c-321b-bb66-78c413e78fc8 | -14.01342 | -42.14478 | 2025-10-16 03:28:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3805d294-7897-36b1-a5ea-70723c56f297 | -11.57948 | -44.07283 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b4e18f59-a764-3ceb-adb7-7262048d0ae5 | -7.9277 | -44.13061 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c17d1b55-eb97-39bf-8690-5b45f108571a | -9.71942 | -44.51725 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d459dc5-7bac-36df-8fcc-e8ed97494d89 | -8.29228 | -43.42503 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0fec0bd-6d4d-32dd-ac0e-fb9931a350e2 | -12.67722 | -43.44054 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e5ba0d71-4121-3c3a-a2e7-db3c2b0c1bde | -10.61596 | -45.24819 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fba9798d-4d94-3562-8e76-19b97a2ee2ee | -8.29479 | -43.42163 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8841a1b3-61ba-3e06-9c97-ac4f0e24054c | -10.05438 | -43.83869 | 2025-10-16 03:28:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d439b87e-c6b7-3846-addb-6e48841dad0a | -10.53204 | -44.50767 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c529baf-6632-34d8-98b0-1d8ca2f06250 | -7.46812 | -42.67054 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f890dc3-9740-3593-8361-f8a66bd6eca0 | -11.57561 | -44.05931 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b16726a0-0105-33dc-b4f4-468231496e64 | -10.61474 | -42.31829 | 2025-10-16 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fd4c0519-06ee-340c-9191-926f7ab3271d | -8.24299 | -44.04016 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7953e420-d17f-3af4-97b5-c06a01947b81 | -7.48143 | -42.14297 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a796380b-c564-37e5-833b-ce6841b25a2f | -8.26284 | -43.43618 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc6b3f42-d39f-34c1-bedf-cae20f91c4aa | -8.18621 | -43.3255 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 0c2057b2-9340-3c47-93fb-adaac31314b2 | -7.96841 | -44.13945 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48bdca26-d2b4-3e7a-b3de-2e3204051979 | -8.46946 | -44.18959 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 3a90b932-09a9-3487-99a9-f9751017e359 | -7.94144 | -44.13338 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd599586-b365-3e46-8fa9-e9bf86381df5 | -10.62301 | -45.24944 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac041fce-a4b8-3f70-b746-341d2d51dbeb | -7.9265 | -44.13698 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4634a112-acca-3fbf-ae5f-d24b9a28b754 | -11.43047 | -44.14256 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b094f6f-8018-3b30-af66-606b73bd9dce | -9.15701 | -41.05838 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9e6caa08-9c13-3cad-8ad6-eea1ecd13d97 | -7.94224 | -44.12729 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 015f0761-ef0a-3992-86ae-91df42d6968c | -7.48232 | -42.1382 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 657cebf6-5428-3fad-b71c-9ad456b79a67 | -9.72069 | -44.51092 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9edbce93-fd4b-35d0-9b27-ab93f51de9eb | -7.48639 | -42.75407 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9af58bc8-1390-3359-9a34-4f2e0f4975b8 | -8.25628 | -43.43489 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6834224c-784d-3169-bb1f-39aa493dd184 | -11.57986 | -44.07167 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f774347-66f8-3ee2-94bb-0db8198979c4 | -14.74547 | -42.37787 | 2025-10-16 03:28:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e13edaf-5f1f-3c87-9248-0de13818431e | -7.47998 | -42.75296 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6cb448ab-737d-3820-b469-b6633dcab23f | -9.6811 | -44.4973 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4ee68b9f-dd13-38ab-8c87-bccd7c64ac7e | -9.15202 | -41.06615 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| e1ff2d5d-2c8f-3f4d-890a-e0e88d8d390d | -7.67083 | -42.56341 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e2e76580-0620-39fd-bbf0-779cdbe169c6 | -9.1563 | -41.06214 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1685aeb0-4302-3689-ac51-fd80b6c225c0 | -7.46947 | -42.66884 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c560d90f-573d-38f4-b177-e3b82b52f77c | -7.96155 | -44.13801 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f3b6d26-b943-33af-bc85-d9b04bd2f1e4 | -7.3469 | -43.86599 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aeb82b79-c953-3b47-8a6c-3ac9f4c2562c | -12.67208 | -43.43446 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 299ec998-e6f2-3964-8e84-081d71666ba4 | -10.5116 | -43.38761 | 2025-10-16 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fe3814b-e8b9-3e8a-8208-1b314d558a61 | -11.44532 | -44.16897 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a65f131f-cecb-39f2-ad34-312cfef38219 | -8.46968 | -44.1901 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0e3660c0-541a-3054-a248-ea0bc5caf7c8 | -7.47263 | -42.75686 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f9a144b-3b69-33bd-80a0-eb6dcbce3219 | -11.32716 | -41.67376 | 2025-10-16 03:28:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5fdf273a-e8a8-3026-82f6-8ee401037303 | -7.67716 | -42.56444 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f882f16-5982-3ebd-99ec-3ae7ba22fa78 | -7.93577 | -44.12564 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30522c9c-382f-36f2-a029-ea7fd1f8bfae | -11.5057 | -44.07246 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b26b4cc0-731d-33aa-9604-f0c357e7ecb0 | -9.71258 | -44.51596 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e96b08f3-622e-3678-9641-3ef96f0ca186 | -10.05209 | -43.8502 | 2025-10-16 03:28:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1ad1e40-59ed-36b4-9bfb-66e383cf9e30 | -11.57416 | -44.06602 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6685e623-c577-32f9-b726-d44c5d6b7571 | -10.53348 | -44.50702 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 093746b5-d616-3d14-8515-8579fc9cd6ca | -7.97081 | -44.12706 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 837d547f-90ba-3519-a7be-02f123beda87 | -11.06007 | -44.78625 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9fa9464-4185-3469-a995-b75f92f623ce | -7.47385 | -42.68047 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2bf25f4f-fc88-3c16-ac43-71157f69b278 | -8.2579 | -43.43676 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e988334-1bd5-335b-af94-2eaa81437623 | -8.18424 | -43.32481 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 520df073-e3d8-3cbf-b38d-42a5c967424b | -7.95349 | -44.14276 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 974185b2-389d-316e-9989-7f8cea42ec58 | -10.61647 | -42.30958 | 2025-10-16 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42e0ca15-010b-3291-be59-ac0392a86ead | -8.26384 | -43.36178 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ce1922c-7abb-38fd-a085-c4163fdb1598 | -8.29275 | -43.43251 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b379fd7-46bf-343e-9f0f-a76acf45ecca | -7.57349 | -42.68575 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67d2454a-db21-3e4d-9f8b-584288602ce5 | -8.27153 | -43.36473 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a6a3b804-595a-3204-a726-47bd06ef6f6e | -8.44939 | -44.18482 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6ccea0d0-2237-33e0-a68a-c5005eabdeb9 | -12.67236 | -43.42979 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0c51636f-2163-3073-a25e-a551315fda14 | -11.45066 | -44.17595 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f2228c8-3bc3-3508-84b8-9df9f9fbe90c | -10.83329 | -43.95449 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7096c34a-17db-3325-9ee7-ae033a572579 | -10.05747 | -43.85733 | 2025-10-16 03:28:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17285239-a812-371b-9bf2-2a9908c98cfe | -11.42594 | -44.13878 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a80fc0b-a1fe-3184-b58f-9a5e2bd48c2b | -11.50037 | -44.0656 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 706ce364-85dd-3902-84c7-c1656553dd71 | -10.53226 | -44.51301 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f974750e-90cc-3767-94dd-0ee91ae59132 | -7.47438 | -42.14657 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ffc2f47a-01bc-385a-be88-7b76e650ff60 | -8.56197 | -44.59341 | 2025-10-16 03:28:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7e4eb54-ba26-34a8-9d26-7d10216b1273 | -9.69209 | -44.51185 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 657f2a96-da29-3d0e-8ec7-65ea07ee3910 | -10.12266 | -44.56441 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cda1692c-6f5b-398b-84e7-06239a3f50fe | -11.58061 | -44.06736 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3b2d5af-f915-3bb3-ad78-c575686642d4 | -8.26176 | -43.44173 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84ce0350-e377-35e5-a451-83e62e578787 | -10.30551 | -43.995 | 2025-10-16 03:28:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6dccdf5-99bf-3eab-a311-e8cd2d788dbf | -10.83584 | -44.00811 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d872dd21-259f-32b9-b6b5-31477f9c6562 | -7.46718 | -42.67573 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 109e9231-5599-34f3-9492-e884dcd93478 | -10.80381 | -44.0075 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdea1819-bdc7-3764-ad0b-1afe1f10a63d | -10.82804 | -43.94716 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15638d60-ebd9-3b16-833c-eed5eb8a0625 | -9.68132 | -44.53 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c0cd21e9-18c5-3482-9ae2-b2786079116d | -13.27684 | -42.40666 | 2025-10-16 03:28:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 723fe6b3-2a1e-3f64-b486-18bcd3f8e61c | -8.19077 | -43.32611 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| a49d9c7d-153c-3109-87cd-9f4dfa5ff8b0 | -8.20495 | -43.3229 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f7f5b5b7-b532-36dc-9275-cf1777316b7c | -8.56045 | -44.58772 | 2025-10-16 03:28:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a76ce50f-67f5-397a-a336-0ef8e429e5cb | -10.03365 | -43.8404 | 2025-10-16 03:28:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e0c4338-11f2-3ccd-abd0-c395010acb68 | -7.92601 | -44.13729 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a22cf5ac-df91-365b-8706-30688f66c5a9 | -7.35498 | -43.8606 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4cc3b8cd-b5e4-32bb-ad6a-233f5e838b15 | -11.45601 | -44.18291 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff89c5cd-cec9-373c-b13b-009da07dc0f0 | -8.29333 | -43.41961 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b4c8190-0313-3cbd-b22e-cdfe0350e460 | -11.45818 | -44.18069 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d04651fa-5acb-3042-a016-ee595ca6c6ac | -8.2515 | -44.10671 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 594c4246-12ef-385e-86b2-8c04748cd8ea | -11.42706 | -44.13324 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8b4a176-2ac5-3545-9381-1dc1c152de31 | -14.00904 | -42.14477 | 2025-10-16 03:28:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 418b2293-863a-305a-a09d-80be03f86a21 | -7.39553 | -44.75092 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76a8ba0f-b8af-31df-889e-8daca86f81ab | -8.46823 | -44.19774 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5015a29e-e0a2-3b05-95db-5d71e9fb6690 | -9.67305 | -44.50219 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9099c318-3633-3d09-afa1-b6dcfe78f8b2 | -10.80989 | -43.94313 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README18.md)
