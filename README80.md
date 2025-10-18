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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1661e0d-895d-348d-b8e4-dbd52b396d57 | -10.49618 | -43.43534 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac1d5bb-e1bd-30d6-a07a-fd1f6a73b2ac | -8.63447 | -54.711 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7629ff42-1fe4-3303-b3af-66984c09fd9c | -11.85714 | -45.44901 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3d68e4b-9e64-3c36-9b28-9e14554c1523 | -12.9868 | -48.45576 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea149d50-b562-3d83-b990-4c5c5f978721 | -13.07932 | -43.06039 | 2025-10-18 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0b6d8a94-32ef-353e-9cd2-5006199ff1fc | -12.80212 | -48.64976 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2dbf295-1109-3d6a-9c57-74d08a2f761b | -9.549 | -54.58775 | 2025-10-18 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a101ee8a-5ef1-34ad-87d7-9122e00ede32 | -13.40912 | -48.58054 | 2025-10-18 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a364fcca-a355-363d-adda-bc679e519f47 | -11.3653 | -44.28238 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0701608d-7fc8-318b-8d5a-09c79a91a344 | -12.36273 | -47.17737 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afc087ab-d6d7-330d-ab11-466e893bb72a | -11.60345 | -44.08578 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf4505a4-c33b-36a6-bb73-2853d88eec64 | -9.7433 | -59.30443 | 2025-10-18 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7fb0a2c-31a2-399e-ad90-27722a7c2269 | -9.88745 | -47.65135 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ad499c6-8d0e-372b-b968-650c487e7579 | -10.30247 | -44.03448 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 377d5ca9-84d6-3486-938d-4d132a08626c | -10.49525 | -43.44272 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bbda4e2-25fb-3b13-a1ef-13a0fb51ce85 | -11.73653 | -59.31341 | 2025-10-18 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd55cd50-6d3f-3dd1-bb66-64f683d6d2c3 | -15.4509 | -45.93914 | 2025-10-18 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55bb3f1c-6a2f-3b5d-939c-5f7adfee9d57 | -10.92231 | -47.97854 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92d90b85-533a-3939-89aa-1a3787ae9878 | -13.77487 | -48.23899 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec293633-419a-3ebf-bb15-956425d5c563 | -14.12977 | -44.71391 | 2025-10-18 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4e87bf8-10f0-3cd9-a754-5a5fa07a55db | -14.90953 | -52.40243 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5576274b-3ad1-3743-9630-f4b868e0b76e | -15.52906 | -45.69653 | 2025-10-18 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 435e604b-6650-32b1-9c19-167aee14a3aa | -9.88331 | -49.11894 | 2025-10-18 04:51:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd212c7e-6a8e-369c-b6f5-e0b917a77244 | -13.25184 | -48.54259 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b93a7efa-3565-385d-834f-4420528780ee | -10.441 | -49.48001 | 2025-10-18 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d42b77d5-0bfe-3d19-a60b-39c8e7ed5d20 | -10.62439 | -42.30558 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 53929d35-789f-3301-8b0f-7d508a7817de | -12.15573 | -45.09214 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58b3810c-3dc5-3266-bb59-cc1661791250 | -10.52347 | -43.39996 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03bb1fc4-6f74-3dc5-82a6-d4240854e912 | -14.90611 | -52.4019 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aef25a2-3e09-3f85-b1e7-8a902c82ead3 | -10.02859 | -62.16514 | 2025-10-18 04:51:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a11ebbd2-6afc-3c22-9fab-d9bde3469533 | -9.66222 | -48.52578 | 2025-10-18 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8fd36e5-4df1-3def-8543-da9377438290 | -10.48452 | -43.43755 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8cd26cd4-d301-3876-86ca-b17a084bd439 | -9.96992 | -50.90807 | 2025-10-18 04:51:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df520f7b-8e24-3d37-a54d-9b08e7456f73 | -13.04442 | -48.19678 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de950fa0-d81a-3cb3-9f68-cc1daf9f3378 | -11.38891 | -44.2681 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae7c9b27-dc9a-3e6f-bc5a-ded3195fcb7b | -17.49475 | -43.46816 | 2025-10-18 04:51:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1645c036-083b-3ee1-9add-cfba2b4c4a1d | -13.22452 | -43.98128 | 2025-10-18 04:51:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2daa886b-de42-3533-a7da-8838a57e08db | -10.53517 | -44.51042 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36b46e70-2b41-36cd-b32d-b21cd82eb277 | -12.65301 | -54.77242 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d17d5221-986f-37a4-b2b6-11660e3bc340 | -13.42513 | -48.08553 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c1d6302-ab54-3909-b632-f580a1817aae | -11.60434 | -44.07867 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70755091-c62b-38fa-af80-eb42823e1480 | -10.80782 | -44.02166 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7458c862-408c-3f4d-8e4f-92d0b1768a7a | -11.25105 | -43.21571 | 2025-10-18 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8b3a9b3-9fe3-3ccc-8c34-d4f7ee60641f | -10.59409 | -48.00082 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89041cec-4a2c-32ab-815a-927237441c2c | -13.25232 | -48.53902 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d91f5ce5-90f8-324d-a6e9-dab8727b44db | -11.61389 | -44.09072 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 77be4d4d-6ea7-3860-8131-12623fbeb4a6 | -9.66147 | -48.53084 | 2025-10-18 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cdaf75b-a733-324f-b8b2-151975ebbc48 | -12.15458 | -45.08192 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a1e7f01-c8c1-3ce3-93b6-1d3450be7651 | -13.5172 | -48.00414 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f85b33d-c1ab-326d-a0ef-ffd26392806c | -14.89926 | -52.40077 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb7ef717-c871-33db-afb1-142c2a4fcefb | -13.7738 | -48.24685 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71529267-4e0d-35be-8d40-3ea9e33b9663 | -13.7502 | -49.79969 | 2025-10-18 04:51:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd68d578-845c-3e22-9fa1-8d5749ad268a | -9.91191 | -47.65883 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74a4ef11-0a0c-3a34-ab0d-52e34ebe8333 | -11.37126 | -49.38015 | 2025-10-18 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbeb4459-b9b4-377a-8caf-212607397a1a | -9.88993 | -47.65351 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26ce773e-fb36-3e34-a617-0ea5d40559fd | -13.45594 | -48.11436 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54b33784-e3ee-3969-a71a-bf0abf7d6fb8 | -10.18815 | -44.54103 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3f304df-4644-3cf0-be56-431e3cd55f42 | -11.40193 | -44.27491 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eae7a702-6e93-355b-be04-bc1dc3b7c662 | -10.24387 | -44.04048 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6bbad6b9-2731-38a9-abba-c691edd34b77 | -10.29746 | -44.03097 | 2025-10-18 04:51:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e6a66e6-964d-3889-8f28-9bb2e80669fc | -12.1778 | -45.08225 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 843d22d1-d9b7-3a9a-a203-0687e8807d82 | -13.48593 | -47.95724 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3f29500-d5e1-33c0-a783-ef4c2d4558e9 | -9.38324 | -54.59817 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1e6720-3606-3f9c-afd0-683aff8f871f | -10.23102 | -44.05533 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 835ecab4-ca06-3a13-8872-8f90af975cef | -13.42137 | -47.98237 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6ee91b1-c4b7-312f-a9c8-a78b8038c280 | -11.18904 | -51.96365 | 2025-10-18 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af66370a-7344-3ca4-b61a-c8b6591d69f5 | -10.97942 | -44.3299 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d935d5c5-8f19-30b3-9561-8d94d1de4d09 | -12.78773 | -48.63364 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e11ac62-fc89-3857-b199-819af4bb5e9c | -11.59978 | -44.07092 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9575ef6b-55db-3bb7-8684-8bfed5046fd4 | -9.8916 | -47.65203 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fa331d1-278d-3500-950e-c7b86054a9b0 | -12.91077 | -48.58282 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 388156db-f918-36fc-9db8-2356f7392776 | -12.43092 | -57.81703 | 2025-10-18 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a2ccba5-f822-3182-9b4d-859e676eee38 | -13.70723 | -40.98884 | 2025-10-18 04:51:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d0a508d-1a31-3e55-9574-dfb159cb169c | -9.23871 | -51.82393 | 2025-10-18 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 98e7737d-9037-32f5-b739-882c2434c3aa | -10.43525 | -45.01786 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f2fe1d7-fc26-36c9-b943-be2475a70bef | -9.87952 | -49.11836 | 2025-10-18 04:51:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7f5f9ad-1100-3e06-bd9c-ac344334a6cb | -15.04726 | -46.61235 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b66255-02a3-3643-b449-7547378d960d | -10.42165 | -47.7476 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3df0e5d9-157c-3d51-ba14-c9f946a67d43 | -12.15027 | -45.07494 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f55f8b01-17f2-3ba8-a17f-8465cc7d0391 | -9.91021 | -48.14217 | 2025-10-18 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04168577-3c8f-3d6b-9029-255a5b9ba2ae | -12.39092 | -47.2042 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bb04b13-363a-389f-8bcd-93ca07ebaddd | -15.55325 | -42.35276 | 2025-10-18 04:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7196b87-f159-351d-8c8c-897efcf18b28 | -12.65967 | -54.77353 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c68cf96b-aba1-3d24-8543-c87246e94a8c | -10.23215 | -44.89654 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5638da0d-f017-3bf8-8c2a-a2c08e572853 | -10.41686 | -47.74044 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1024ed47-21b0-33aa-a95a-267d9bff6c4e | -13.77971 | -48.23515 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21f61433-8f33-3506-bdd6-d9e2033f5532 | -15.79978 | -43.56993 | 2025-10-18 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a706fe71-23e2-3723-be03-11b17abe8314 | -13.73697 | -48.32832 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20925867-b1af-30fb-8de8-480a9afdfb0c | -10.67722 | -44.56772 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afd9ec04-774b-3f76-ba67-f9e3801e7bf3 | -10.42216 | -47.74385 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5915465c-8987-3acc-a912-8de1cbf752fe | -11.5952 | -44.06318 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e7d25a5-ad40-3423-8e80-bd1e208b49d1 | -12.15848 | -45.09203 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7e51d74-f37e-39ef-a4d7-ab9b8a92e27e | -11.00119 | -47.91375 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5b9a979-fa21-368b-9452-eda72704b92d | -14.90152 | -52.43247 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cc253d4-c905-3597-8824-451e62061e43 | -14.89809 | -52.43198 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ff34ed9-c508-3159-82ca-da7cf9bd25d5 | -8.63387 | -54.71471 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c525f66c-dbe0-348e-af63-8f8c0c634631 | -10.418 | -47.74317 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e95d33fa-f945-3bd1-ad7d-d0d183e31bb6 | -11.50092 | -44.18271 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 597bf37b-927d-3312-bca2-5ff10ca1daf3 | -12.92928 | -48.60001 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8caf7799-8bb8-36a1-8e2c-eba05c934e23 | -12.39537 | -47.20481 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README81.md)
