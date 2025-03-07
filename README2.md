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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b25d053f-da2c-34a1-9eea-18a0f272e6c8 | -12.9093 | -45.07878 | 2025-03-07 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60e3cbf3-1e12-3af0-9442-9f54cc8bdd0d | -21.8058 | -44.8353 | 2025-03-07 04:23:00 | NOAA-21 | CRUZÍLIA | MINAS GERAIS | Brasil | 3120805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d4ae10f1-33de-3f9b-8c6b-b1622453423b | -10.39483 | -47.98661 | 2025-03-07 04:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b05bcdc0-7bca-3488-9d33-2d23ac91c013 | -22.53988 | -48.81312 | 2025-03-07 04:23:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2838e58-c1ec-3983-8b76-7af5ec1b2529 | -15.08001 | -48.94565 | 2025-03-07 04:23:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66d282ed-ccaf-3da1-a5b9-b6c6a0871cab | -10.23577 | -44.76197 | 2025-03-07 04:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5ec5ab4-81f6-334a-b167-305b0e31519f | -10.7175 | -42.33308 | 2025-03-07 04:23:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 660cac40-d6c9-3c52-be76-a40c175bdc7e | -23.20012 | -50.80657 | 2025-03-07 04:23:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| edb5cd70-a043-3d6f-8b30-86f668eaf318 | -12.775 | -48.19583 | 2025-03-07 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a44488d-8e46-3ea2-ade4-9b54730d6eba | -12.90876 | -45.08238 | 2025-03-07 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06179e18-29c0-3b87-9e45-2e7d59560948 | -10.71448 | -42.32824 | 2025-03-07 04:23:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 528d1341-d429-3f59-bc2b-587a31236207 | -16.68279 | -43.88506 | 2025-03-07 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6afb4649-7d8e-37c8-8f02-8b707616ac22 | -21.43614 | -57.26195 | 2025-03-07 04:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c6dcff4-382d-3f56-a1e1-abbe91c11b54 | -11.84392 | -37.5868 | 2025-03-07 04:23:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b0705257-a5c0-3cb2-9faf-e6b6192d5e58 | -13.4184 | -44.371 | 2025-03-07 04:23:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66adb9af-df33-3ae9-9f54-95df85267cce | -20.16205 | -45.71998 | 2025-03-07 04:23:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 965c9ee7-6e65-363e-a7f7-1e6942ef4eed | -12.90596 | -45.07825 | 2025-03-07 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c57767a6-ff96-3a7c-9272-7eaa4a5f3e12 | -21.43546 | -57.26516 | 2025-03-07 04:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bcb8539-90b7-3dce-b485-49c71308b89f | -21.58606 | -57.58414 | 2025-03-07 04:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dd0b0c0-7693-3174-aa3d-2302d5f7a369 | -22.82454 | -42.44217 | 2025-03-07 04:23:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2b352751-361e-3138-a3f6-26c5c0c5a06d | -12.91155 | -45.08652 | 2025-03-07 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf3387ab-ce48-37ab-9951-be5cdd4083e6 | -12.84625 | -43.8305 | 2025-03-07 04:23:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 58d3acbc-ad84-30ee-92a6-b3491d06ed8d | -10.39419 | -47.99054 | 2025-03-07 04:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93c2600e-0031-348c-ba26-9cc6bad98568 | -17.78002 | -42.80814 | 2025-03-07 04:23:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3104762c-ad3d-35d8-976c-f58ff579583c | -23.40661 | -46.55651 | 2025-03-07 04:23:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9700c0a3-4f4c-3ac0-a2ce-bd272c972cea | -13.7288 | -47.70887 | 2025-03-07 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c4ee851-dc35-3039-9a0c-5ed9f0145f4b | -13.3618 | -47.02377 | 2025-03-07 04:23:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 126bd35d-b223-3867-84ff-24ce407afb06 | -21.89268 | -46.50751 | 2025-03-07 04:23:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 19ba6a2d-2595-392e-b482-ecfc3511e68b | -22.89222 | -45.3171 | 2025-03-07 04:23:00 | NOAA-21 | ROSEIRA | SÃO PAULO | Brasil | 3544301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1eaea78f-6038-3631-a29a-fadc9477278e | -21.19488 | -44.93824 | 2025-03-07 04:23:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0aa8d15-bd7d-3d41-86f0-cb674841f69d | -20.47794 | -53.67656 | 2025-03-07 04:23:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfe5961f-7b67-34e0-b5fa-207acb0cdc36 | -13.72544 | -47.70835 | 2025-03-07 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7085eacf-e19d-3f9f-a3cc-4f7717339d63 | -11.84427 | -37.58701 | 2025-03-07 04:23:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7bea15e1-b45e-3451-af45-94c843abc9fb | -13.48388 | -44.0197 | 2025-03-07 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81051de0-2151-3052-9698-bf940bef16b3 | -23.45097 | -47.24645 | 2025-03-07 04:23:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f5b910d5-30bc-3d82-8ec5-b608956755a5 | -20.31104 | -45.58259 | 2025-03-07 04:23:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3746f5c-3069-3f30-82c0-38244c29976d | -13.72763 | -47.71614 | 2025-03-07 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4adb8407-4bad-3d1e-b244-c2257f58c1d2 | -12.91264 | -45.0793 | 2025-03-07 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f020cf06-6156-318e-89f0-01bffa8f8881 | -23.33755 | -46.77293 | 2025-03-07 04:23:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 773b8a00-faf3-3197-85e6-2ef5be86adbb | -20.8081 | -49.52332 | 2025-03-07 04:23:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 783b4f15-1c05-326a-89fe-a6f75f65a099 | -10.39766 | -47.99112 | 2025-03-07 04:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 902bf34e-5ebb-334c-a898-b3e465f3e915 | -17.11544 | -49.14157 | 2025-03-07 04:23:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e988d05b-b9f8-3e35-b158-ec81305a4ccd | -10.72478 | -42.33417 | 2025-03-07 04:23:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a19a6e5d-9b81-394a-9b6d-c6b7972d1787 | -11.82442 | -47.08116 | 2025-03-07 04:23:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 999280ff-2194-3fb2-b2ed-1ac890675a44 | -22.19966 | -46.77958 | 2025-03-07 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80f43201-c372-3240-8eec-95847c686869 | -23.20286 | -50.81124 | 2025-03-07 04:23:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cc73bd25-109c-33a2-9a61-34f43dd4d452 | -10.6617 | -44.4016 | 2025-03-07 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23e5f184-df50-32fb-a8a7-99e6ff93182b | -20.72427 | -49.43391 | 2025-03-07 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f33e38f4-239b-3de1-b1cb-4aeddedd2d66 | -10.3983 | -47.98718 | 2025-03-07 04:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3eb5531-9a24-3e66-bed8-74ee3bd8dfac | -20.99831 | -51.7922 | 2025-03-07 04:23:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4f5da823-7b47-3ec5-8413-2058522aae7f | -16.88483 | -45.34713 | 2025-03-07 04:23:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09ea36e9-2750-3b36-8070-7f36bd356d16 | -15.2968 | -47.88354 | 2025-03-07 04:23:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89a9101d-8859-30f4-8fb6-a32a63e940e6 | -12.27438 | -44.98674 | 2025-03-07 04:23:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7b17d57-f077-3981-8c48-5d855ded4925 | -12.90985 | -45.07517 | 2025-03-07 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 41e82225-f23a-3bb7-99c0-5d19876aad58 | -10.71812 | -42.32878 | 2025-03-07 04:23:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ebb4a5aa-8f27-3090-b938-366d496dddfc | -20.76636 | -46.76788 | 2025-03-07 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 247e2f4e-8d2c-3f7f-84ee-7af5f7592a39 | -13.72822 | -47.71247 | 2025-03-07 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c815db68-3ea9-3823-866a-651d58f3ba96 | -12.27384 | -44.99031 | 2025-03-07 04:23:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1b9c14c-93d0-3104-ad37-2280de3b7af0 | -13.42181 | -44.37155 | 2025-03-07 04:23:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d47b58db-abdd-37f9-abf3-4f62d12090a3 | -13.53852 | -47.93403 | 2025-03-07 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b5eb47f-e082-3597-97b4-fe884c550c81 | -10.53897 | -44.66798 | 2025-03-07 04:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e599141c-c354-3142-ade5-7ee79e860b01 | -11.45485 | -40.7128 | 2025-03-07 04:23:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ebbe29c2-5323-30e8-b23d-6fe9106867d3 | -22.84522 | -47.2417 | 2025-03-07 04:23:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19c041f9-f26c-36a1-9e92-abc94229914f | -11.82776 | -47.08171 | 2025-03-07 04:23:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e110775-330e-33c0-b377-3e86c5741ea4 | -23.25765 | -47.1314 | 2025-03-07 04:23:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 975b95b3-f08d-33b5-82ea-38c9b7babb31 | -12.4769 | -46.91727 | 2025-03-07 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd51b4c5-917c-38ea-99bd-53a5f57c7cdd | -12.84972 | -43.83104 | 2025-03-07 04:23:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4ec3a18-e713-3635-a5f9-41f6f2813849 | -13.67858 | -47.19334 | 2025-03-07 04:23:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5113e975-dac1-3dca-9ccf-7dd28e87d42b | -16.04412 | -43.80581 | 2025-03-07 04:23:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 138b4c0e-fcbd-3304-8f79-74fe48ca5333 | -15.29739 | -47.87991 | 2025-03-07 04:23:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f9ad7f4-da09-3d84-a585-84bbdb3b8e2e | -12.49351 | -46.92 | 2025-03-07 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c17611d9-5a53-3f64-87b3-f7071a8c2fe8 | -11.44936 | -48.00503 | 2025-03-07 04:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b83ed4a5-190c-388a-af50-5efd6788f25b | -10.39355 | -47.99447 | 2025-03-07 04:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dafb790-ebc4-3a93-b836-0e1f897e0ede | -17.67635 | -42.74495 | 2025-03-07 04:23:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93b45af1-bed7-3dc3-a64b-839bc7bef07a | -10.72114 | -42.33363 | 2025-03-07 04:23:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be141482-4ddd-3bde-8ef2-47c383e94a6d | -11.98095 | -44.30402 | 2025-03-07 04:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45716e85-6f1f-3996-ac71-121dfa88997b | -12.30479 | -47.26776 | 2025-03-07 04:23:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d60d3f7-a43b-3751-9d31-8455d8a736d4 | -25.19676 | -49.19862 | 2025-03-07 04:25:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dbf900f3-385d-3216-9123-327b80caa2fa | -28.41541 | -50.89083 | 2025-03-07 04:25:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a55fac0-a61f-3d47-a40e-103f5e582fd1 | -30.29362 | -54.99095 | 2025-03-07 04:25:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 5350a027-3685-30dd-823f-6ec8332fb409 | -19.68274 | -45.3774 | 2025-03-07 04:25:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36698375-4926-322d-85b5-1df26dee008d | -29.77891 | -51.17892 | 2025-03-07 04:25:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 2dddbc0d-b36a-339d-91ab-159f0074b0fa | -24.24247 | -50.74109 | 2025-03-07 04:25:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e102f7f1-28ac-39ad-93de-b93334b3bd3f | -23.43858 | -51.4282 | 2025-03-07 04:25:00 | NOAA-21 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 45113454-8184-3440-bf3f-5d31dc2ce0d8 | -29.89238 | -51.23577 | 2025-03-07 04:25:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| a87f71b8-1228-32a6-a4a3-382e40db35ed | -19.89878 | -43.96268 | 2025-03-07 04:25:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6f3d6563-49b3-3f6d-bd5c-0cb970685e25 | -26.22381 | -53.18515 | 2025-03-07 04:25:00 | NOAA-21 | MARMELEIRO | PARANÁ | Brasil | 4115408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86c48c43-05c1-3ccb-b4ab-dd8145d529b4 | -17.98415 | -47.221 | 2025-03-07 04:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc2e2ec4-f072-3cb5-b6c9-520fb2d67df7 | -25.14641 | -51.34743 | 2025-03-07 04:25:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7da617d9-5900-3f67-b170-877a8a32d8a3 | -24.03976 | -50.5023 | 2025-03-07 04:25:00 | NOAA-21 | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f441017d-8244-3723-ba9d-ef724584a5a4 | -27.0226 | -50.84633 | 2025-03-07 04:25:00 | NOAA-21 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7997c6a1-4ffb-3a6a-9c88-a4207ebe198b | -24.93884 | -50.93315 | 2025-03-07 04:25:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 517409e6-74ad-347c-b3ba-f1a04e4f02f4 | -27.66644 | -50.65698 | 2025-03-07 04:25:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 696dd379-00ef-38a4-9bb1-fa63cce2ec85 | -28.53816 | -51.82148 | 2025-03-07 04:25:00 | NOAA-21 | SÃO DOMINGOS DO SUL | RIO GRANDE DO SUL | Brasil | 4318051 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e52c6de2-a2e1-3ff1-bb56-a60327baced0 | -26.59021 | -50.04704 | 2025-03-07 04:25:00 | NOAA-21 | SANTA TEREZINHA | SANTA CATARINA | Brasil | 4215679 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| adc3758f-4656-3f50-a932-3a89dd345869 | -25.56872 | -49.36526 | 2025-03-07 04:25:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1a5d1439-b3a5-35ac-9d30-a273b58a29af | -24.04042 | -50.49835 | 2025-03-07 04:25:00 | NOAA-21 | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39a95f58-734d-34d4-bd40-f033af0743d1 | -25.80837 | -49.99703 | 2025-03-07 04:25:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97b1f25c-a197-345a-a438-5ac9c016986d | -20.11228 | -45.35384 | 2025-03-07 04:25:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 637b7bb7-d027-3056-bd6c-c4012be64df7 | -30.29734 | -54.99188 | 2025-03-07 04:25:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
