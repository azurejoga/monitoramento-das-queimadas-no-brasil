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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e86e0920-3a84-3585-9640-83d28cc38544 | -19.1995 | -46.5714 | 2024-10-07 13:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 424b2967-500e-37e1-b802-903ebfd69e81 | -18.8903 | -54.4733 | 2024-10-07 13:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 304a33db-dba8-3e94-9533-4c97628c4bde | -18.8886 | -54.5587 | 2024-10-07 13:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 7158711e-4c35-39c0-8c3e-8a2f02c9fe0a | -7.8359 | -42.2228 | 2024-10-07 13:35:50 | GOES-16 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 62b0d18a-e24b-3fa2-9681-32199a7f941c | -7.8548 | -42.2207 | 2024-10-07 13:35:50 | GOES-16 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| a185e66e-7716-380b-b841-1cacbad47157 | -8.6373 | -40.4514 | 2024-10-07 13:35:55 | GOES-16 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 102.3 |
| b8663530-63ff-3147-af34-906415d9c86b | -8.8366 | -45.146 | 2024-10-07 13:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7384a940-d885-30f3-aa6d-00ea703419f8 | -8.7996 | -45.0815 | 2024-10-07 13:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a60bdb32-3177-3476-8787-5c8044cf5635 | -9.9505 | -44.0908 | 2024-10-07 13:36:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5eea6479-a64b-3c1c-a5d7-bdd4bfd2e7d2 | -11.7566 | -44.4897 | 2024-10-07 13:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 350.0 |
| 8f74e1b8-d167-3244-80ce-a4adf14995d0 | -11.7369 | -44.5159 | 2024-10-07 13:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 86db7e8c-96d6-3351-84bc-764eb7ae4b77 | -11.7561 | -44.513 | 2024-10-07 13:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 317.3 |
| a37f12cc-9f4d-3069-8bbe-6e788319f27b | -11.7373 | -44.4926 | 2024-10-07 13:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 410242d0-245c-33ba-9438-a73a7916b2e0 | -13.0017 | -44.7357 | 2024-10-07 13:36:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| deb6c4ad-460e-3d68-aedc-6f770b322e4f | -13.2359 | -45.5783 | 2024-10-07 13:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 85ba9ef0-98b5-33d0-a7d8-f6e797cb4e4c | -13.8549 | -44.6363 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3d07aadd-9835-3e2d-8223-93dec4021673 | -13.8754 | -44.5858 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 4b6536cc-13b6-3b9d-9aff-781a7b8f7d02 | -13.8948 | -44.5823 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 21899c96-c46b-3814-9d1c-2b041aa89d36 | -13.8559 | -44.5892 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 46c627b2-8378-3642-9798-0336dc897526 | -13.8165 | -44.6197 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 90e3f907-d11f-3f3d-b631-44f241054e23 | -13.8359 | -44.6162 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| f5476c28-ded9-396d-a3fa-540806ac55dc | -13.8354 | -44.6398 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e386643b-e8cd-3988-838a-311fd3a0ef9c | -13.8749 | -44.6093 | 2024-10-07 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 27c0ada9-7315-3f99-8299-0b7f6183a6a3 | -14.0387 | -45.118 | 2024-10-07 13:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b6af5e52-55c5-36a8-8caa-06e182a5de39 | -14.0392 | -45.0947 | 2024-10-07 13:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b0b36e4e-50a9-34e5-9c68-1c33658520ee | -14.0198 | -45.0981 | 2024-10-07 13:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 32a8f0bd-b110-39ba-b785-c477c6e48d2e | -14.6996 | -45.1389 | 2024-10-07 13:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c16e06a8-4c0d-3b5b-8a1c-4fdc40f442b9 | -16.8899 | -47.1532 | 2024-10-07 13:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 80d84bdb-bc45-3cd7-96ec-acc073be165e | -16.9098 | -47.1493 | 2024-10-07 13:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 132.9 |
| fcc7c8ee-1f40-35cb-a6f0-74259005da8d | -17.6882 | -53.0573 | 2024-10-07 13:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 187.7 |
| ebe85b44-414c-3010-93ce-5bb782530c42 | -17.6688 | -53.0389 | 2024-10-07 13:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 2c7546b4-9131-3add-bb2f-2b8f73028aef | -17.6877 | -53.0788 | 2024-10-07 13:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 683e2c33-8369-374c-a791-1427d8a73dfe | -17.7926 | -53.7675 | 2024-10-07 13:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| dac09d8c-3a48-32b2-a47f-078ee8ebccab | -18.3211 | -47.1382 | 2024-10-07 13:36:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 7766cdc3-44f5-3bad-825b-ba06057c421e | -18.8882 | -54.58 | 2024-10-07 13:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 757a81fb-6776-3e89-b92f-5851d4e0dbba | -18.8886 | -54.5587 | 2024-10-07 13:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 144bf527-9657-344b-9e71-d0ebf2befed4 | -19.1995 | -46.5714 | 2024-10-07 13:36:53 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 38bd66f7-e388-393e-a004-d1a10dc058a9 | -8.1759 | -43.6957 | 2024-10-07 13:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d0128a57-e8b9-39b2-b477-a0f1b127b940 | -8.6373 | -40.4514 | 2024-10-07 13:45:55 | GOES-16 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 136.3 |
| c7875fc2-14df-3527-9b8d-2a1205193c91 | -8.8366 | -45.146 | 2024-10-07 13:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d96116f2-c89e-3808-993f-89c09830827d | -8.8189 | -45.0566 | 2024-10-07 13:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e2bf59b9-400f-3bae-937d-bb71dd68ba82 | -9.9505 | -44.0908 | 2024-10-07 13:46:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9a83f40e-cac4-31cd-b85c-687b8643071f | -10.6794 | -46.1085 | 2024-10-07 13:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bdb0fdee-4595-3ce4-af98-ed471d63b3c8 | -11.0345 | -46.5143 | 2024-10-07 13:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3c3865ef-8c05-3911-8529-af55d6d9ba23 | -11.0918 | -46.5069 | 2024-10-07 13:46:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1b5c3954-eb75-3ef0-9084-86783f455d25 | -11.7369 | -44.5159 | 2024-10-07 13:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 1859074c-2cc2-3bdb-8f7e-008361428851 | -11.7566 | -44.4897 | 2024-10-07 13:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 360.9 |
| 9cfe9502-03d6-3ff2-bde9-c7fc6a655b58 | -11.7373 | -44.4926 | 2024-10-07 13:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 4f8ca541-155b-3d8d-ad00-fdc803886aa6 | -12.103 | -50.0139 | 2024-10-07 13:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 93c9a055-7b1d-3113-a06b-03992d8837b5 | -12.1027 | -50.0355 | 2024-10-07 13:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 3f9f804f-3d4e-3b04-a289-26046e5436ab | -12.4584 | -47.0398 | 2024-10-07 13:46:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3d7fb111-e6dc-3bee-bf04-37cd5a02f03d | -13.0017 | -44.7357 | 2024-10-07 13:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 065500ce-ebf9-3fb3-9a3d-e660c2975194 | -16.8899 | -47.1532 | 2024-10-07 13:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2df30213-ad9e-3a18-a63d-f8634287f529 | -16.9092 | -47.1724 | 2024-10-07 13:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 144.3 |
| d742befd-0ec0-343e-8fb8-b30c1df8a3de | -16.9098 | -47.1493 | 2024-10-07 13:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 27a06661-e018-3d55-bdf0-e9fbc45782a8 | -17.5525 | -43.7577 | 2024-10-07 13:46:43 | GOES-16 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| cacb2fcb-1e86-365a-8c89-57b9597b15fe | -17.5325 | -43.7624 | 2024-10-07 13:46:43 | GOES-16 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ea8ae1ef-6c87-31ec-a63a-d9f089a8cb6c | -17.6882 | -53.0573 | 2024-10-07 13:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 123.8 |
| e0d4d616-5b2c-3ee2-9aae-0281ac28b8fa | -17.7926 | -53.7675 | 2024-10-07 13:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 16543d4c-c779-301c-96d0-b28aaa9b602e | -17.7931 | -53.7462 | 2024-10-07 13:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 3e87348f-fa1f-3ab5-b1c4-62c3a0be442f | -18.8882 | -54.58 | 2024-10-07 13:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3ed644ec-164d-3975-b871-a2756bf0adc1 | -18.8886 | -54.5587 | 2024-10-07 13:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 53aaa160-f1f6-3c65-91e6-3484e731abec | -18.8903 | -54.4733 | 2024-10-07 13:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 127.0 |
| fd544218-205d-3422-94ef-94f3c168ca8b | -7.3069 | -42.2551 | 2024-10-07 13:55:47 | GOES-16 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 61643a1b-02c6-38e4-a354-353f3a241f70 | -7.6447 | -42.4103 | 2024-10-07 13:55:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 68530826-0a90-374a-ae95-f01372a10c4a | -8.6373 | -40.4514 | 2024-10-07 13:55:55 | GOES-16 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 120.6 |
| 4010fe05-e969-3fa0-b20e-8c0e260d5d27 | -8.8189 | -45.0566 | 2024-10-07 13:55:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 730d904b-eb1e-3ab1-8c0c-714f62e202e0 | -9.5248 | -45.9543 | 2024-10-07 13:56:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5282872b-4656-33bd-9b9a-f81c3c76ab4d | -9.5251 | -45.9317 | 2024-10-07 13:56:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ec7b08ea-90d7-3bbd-b920-176077a10abe | -9.9505 | -44.0908 | 2024-10-07 13:56:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5694e089-aebb-3108-a644-9e1db47e7267 | -10.2908 | -45.4305 | 2024-10-07 13:56:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1fa0d465-8efa-3ffa-912f-a5ec0035ba33 | -10.3129 | -50.5341 | 2024-10-07 13:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1d36d820-5529-3f9c-a84c-4ac6751092f7 | -10.2942 | -50.5147 | 2024-10-07 13:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 85523755-e30c-3aec-ae2f-b115b9f6741c | -10.294 | -50.536 | 2024-10-07 13:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 6db2a1c3-78cc-3e57-9f81-535d67b96d55 | -10.918 | -46.6642 | 2024-10-07 13:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e0ef95ba-a5d7-32df-a01f-5aae4ece7987 | -11.297 | -46.7724 | 2024-10-07 13:56:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2f0a8074-ad48-353a-9adc-97657f6d87e1 | -11.7373 | -44.4926 | 2024-10-07 13:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 32e99cd9-4a55-3939-b2bf-13b86a175441 | -14.0378 | -45.1648 | 2024-10-07 13:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 7b2cad6c-7dd2-36b6-80cb-90496b2381ee | -14.6805 | -45.1191 | 2024-10-07 13:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 508e4093-0e4b-3426-9311-3579aa272746 | -15.0422 | -51.24 | 2024-10-07 13:56:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2f902b03-49e9-3134-8ab0-cc846623737e | -15.71 | -47.1463 | 2024-10-07 13:56:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 4913d87a-d24b-361e-a7fe-974bffbc8d0c | -16.8899 | -47.1532 | 2024-10-07 13:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 8c2e9846-c604-35dd-9317-c8e8931bdb94 | -16.9092 | -47.1724 | 2024-10-07 13:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 119.0 |
| fd2fbbed-a7bf-33b5-b261-4aafa1005177 | -16.9098 | -47.1493 | 2024-10-07 13:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 2747d269-5ef8-305b-a4c6-47b8f8df03bb | -17.5325 | -43.7624 | 2024-10-07 13:56:43 | GOES-16 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a6673246-1c59-340f-8bd9-ff0fd2a71f4a | -17.5525 | -43.7577 | 2024-10-07 13:56:43 | GOES-16 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ba894b6b-0f4e-32cb-9c0a-014799befb70 | -17.6882 | -53.0573 | 2024-10-07 13:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 8146ebbf-6bb7-385b-b4ec-7e2cfc2305b2 | -18.8903 | -54.4733 | 2024-10-07 13:56:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 5b0f7841-860e-3131-9ae1-a9882ff74f78 | -18.8899 | -54.4947 | 2024-10-07 13:56:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 6921efcc-6a24-3252-a2a6-48d8b4e135d0 | -18.8882 | -54.58 | 2024-10-07 13:56:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3a993186-fc3b-3aa9-8388-be820c8a67d0 | -18.8886 | -54.5587 | 2024-10-07 13:56:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 146.1 |
| fb3fc058-46b3-314c-a35e-6873d7f2d835 | -21.4152 | -57.2472 | 2024-10-07 13:57:05 | GOES-16 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e27e545d-5696-31df-9473-e8028e0b5dfa | -9.5248 | -45.9543 | 2024-10-07 14:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 675450b2-900d-3dcc-aac8-756ab41d2839 | -9.5251 | -45.9317 | 2024-10-07 14:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2b543875-8b37-31f5-a410-a3c94d076ee6 | -9.9505 | -44.0908 | 2024-10-07 14:06:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6da070b6-9b30-39df-be50-e06b8a81cc43 | -10.2942 | -50.5147 | 2024-10-07 14:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 7faa5e8e-11c2-30fd-803e-cc6d557c95c4 | -10.3126 | -50.5554 | 2024-10-07 14:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 6781aa6c-e4a8-3ac7-bbe5-f0e6c53a09c6 | -10.294 | -50.536 | 2024-10-07 14:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| c1434908-04df-3b46-ac53-c56379ad8056 | -10.3129 | -50.5341 | 2024-10-07 14:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f32654b8-f8a2-381a-bdfd-8b0124250e65 | -10.7834 | -45.5495 | 2024-10-07 14:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |


[Clique aqui para ver as próximas entradas](README153.md)
