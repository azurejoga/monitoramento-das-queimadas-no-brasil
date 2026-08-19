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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb098b60-9edf-369d-a44c-3c9934f7fc49 | -14.46836 | -45.62982 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23f77347-20e7-3bce-afdc-795cf5a965a7 | -15.88605 | -40.93204 | 2026-08-19 03:47:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 51c952d0-dae3-3595-8e7e-789441c9ec2c | -19.61656 | -42.05362 | 2026-08-19 03:47:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3e710e77-1741-3af5-8bf6-6423819bef9b | -14.48709 | -45.66685 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fd876bf-f598-33d5-a09a-bf0b3b43515e | -21.04574 | -48.47512 | 2026-08-19 03:47:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbaca35b-0e40-3168-af17-0685c33cc441 | -14.48767 | -45.66391 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9ec1752-e9d9-38bf-94d9-2cadad35a507 | -21.39981 | -45.95528 | 2026-08-19 03:47:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1f6e6626-29ca-333e-96b0-6bcf21ebe930 | -14.49266 | -45.66493 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad257cd8-c460-348e-94f4-8e734b04e733 | -20.58326 | -45.92152 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58f26624-15b4-3960-8131-f704d6fcaa86 | -14.45783 | -45.6307 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a94501bd-cd87-3c89-bc75-49cda26d7e6d | -19.67379 | -45.90752 | 2026-08-19 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87639215-47a9-370c-9055-cf807dd37abb | -20.57556 | -45.93637 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0e709b0-65a8-3cc0-8f8a-0db16a4fe07e | -19.11453 | -44.47235 | 2026-08-19 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 708e8500-4af8-3fdc-9a73-6bedf56c1382 | -15.07424 | -45.32963 | 2026-08-19 03:47:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2079fbb9-e92b-376d-8f9d-52bec378a09f | -15.88643 | -40.9292 | 2026-08-19 03:47:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 45c44a43-938b-3729-abad-9d8f4a5b6947 | -20.18891 | -45.40519 | 2026-08-19 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a3a8e8ed-e36a-303d-9154-8681b20c596c | -17.92051 | -44.34267 | 2026-08-19 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72587444-c6d0-3c72-9d62-893de65594ab | -21.50517 | -42.06413 | 2026-08-19 03:47:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8c47ad0-c137-36cb-b2c2-7ee689d8a16d | -19.118 | -44.47728 | 2026-08-19 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 561b80e8-f237-3612-b1d8-6e677b50761c | -14.48214 | -45.66627 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da045af7-938e-3c30-a17d-cd3479b9cd1b | -14.49092 | -45.67377 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 753c313c-aa4f-3865-b032-dc9f9ca8615d | -19.66915 | -45.90669 | 2026-08-19 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf787adb-2e38-31af-b7c3-51b14dca7316 | -19.75132 | -44.31997 | 2026-08-19 03:47:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1bddec3-d59c-3afa-8a62-0f43f38411a6 | -17.59414 | -44.59928 | 2026-08-19 03:47:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3b48499-5041-3aa8-99ee-c16fba8c32f1 | -20.18988 | -45.40036 | 2026-08-19 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c8f37593-a26e-385e-93e3-ef6294243731 | -20.13627 | -41.4906 | 2026-08-19 03:47:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 931f8867-cecc-34d8-9bf8-99adbbca337f | -15.07224 | -45.33121 | 2026-08-19 03:47:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70809b45-8d83-3875-9819-8d9a9d6381fb | -17.95493 | -44.44459 | 2026-08-19 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5a49e8a-9d64-32a9-a10d-2b0e8b78807e | -18.84832 | -47.14342 | 2026-08-19 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a537bb92-e7b1-34c9-81b9-30a3b54a4720 | -18.87671 | -44.20703 | 2026-08-19 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0553ec0e-15f6-3604-9a9e-c816dafbdefb | -19.57508 | -49.43515 | 2026-08-19 03:47:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25ef1f2c-135b-3bde-9cb8-8084f48dc628 | -20.28987 | -46.46363 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 101f26cb-ba7a-3896-bb5b-405591813017 | -14.46225 | -45.63465 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0342f898-e629-3772-9bf6-8b7acc2a3119 | -19.67742 | -45.91329 | 2026-08-19 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8762da43-dba5-34c1-a529-af2b4202f178 | -19.46711 | -44.18274 | 2026-08-19 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a055bf3b-813c-3780-877f-5064111ca819 | -15.90904 | -42.6602 | 2026-08-19 03:47:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6416caa2-29c9-3a72-9582-8d7c4b072c69 | -21.09007 | -45.10588 | 2026-08-19 03:47:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 166f4560-a040-3bec-8da5-2a4f5ee0580a | -19.75022 | -44.31961 | 2026-08-19 03:47:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5576f35-705d-34e7-9429-bd788c5a06a6 | -21.22944 | -43.996 | 2026-08-19 03:47:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b543f96-d879-3a2d-84fe-249c10519db1 | -20.29449 | -46.46515 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2498de8-45ad-3317-8a81-e5ebb967d347 | -19.46783 | -44.17896 | 2026-08-19 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9949a796-bc29-37aa-b133-7f0dc337b9e3 | -16.71509 | -46.40449 | 2026-08-19 03:47:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7a1610f-a00b-348a-a697-8568426591f3 | -20.1327 | -41.49007 | 2026-08-19 03:47:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ac9e8168-c695-3b52-818e-8b243cf16719 | -20.32775 | -42.40132 | 2026-08-19 03:47:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e9624563-770e-3d59-915f-8268ab1cfc93 | -20.60523 | -42.94529 | 2026-08-19 03:47:00 | NOAA-21 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f38323a1-9bcf-36ec-85f8-2cbe30103544 | -20.29617 | -46.4813 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3e575f5f-65d3-359a-9a0e-ec05f819dbbf | -17.60072 | -52.62808 | 2026-08-19 03:47:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ec2a027-df19-36fc-a88f-50de7068c448 | -20.59323 | -45.9189 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25de1c41-8ea0-3b83-b88c-58a9c6147ecc | -14.90236 | -44.80479 | 2026-08-19 03:47:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 919a05cd-4c43-33bc-b044-6024dd5b4022 | -14.48534 | -45.67572 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f881dff1-8eca-39ce-b3ce-d21c947e2369 | -20.88142 | -45.29266 | 2026-08-19 03:47:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8fb21259-cd80-3f38-aa24-3e9ad219045e | -20.30084 | -46.48256 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d9633dd5-2159-3579-ab90-7d07a01ea264 | -17.94081 | -44.42421 | 2026-08-19 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8169cfe2-db56-3819-afe4-06d04f41c42b | -19.10946 | -44.47574 | 2026-08-19 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc8e37c7-958b-35b5-bebb-ee7bc8278fd3 | -14.46282 | -45.63171 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d098ea64-ae29-3ecb-8a5d-789bd41dd184 | -17.99019 | -48.54302 | 2026-08-19 03:47:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ada210fa-30a6-3bd4-b24f-6620af2a472f | -21.04497 | -48.47866 | 2026-08-19 03:47:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ac9991d-b297-35d2-b2e8-c1fd4d524fe7 | -15.06941 | -45.32866 | 2026-08-19 03:47:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cce2c82c-d386-3be9-a724-e42aa023ecc6 | -14.48592 | -45.67277 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b90a2d6c-143a-30b1-b1b7-0922c54f86c9 | -15.01358 | -41.94803 | 2026-08-19 03:47:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a956eeb-4e46-3a15-9863-13b26b08bd49 | -15.71297 | -47.80322 | 2026-08-19 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6da9317a-89d0-3ed7-b0a1-75da34ae7435 | -20.35124 | -41.55162 | 2026-08-19 03:47:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd870266-faa2-35f1-99b5-48981109f08b | -18.5855 | -41.32825 | 2026-08-19 03:47:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4225c708-92c0-3612-b910-37c335c203d1 | -14.4678 | -45.63272 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ca899db-f13c-31f4-a094-eb7f65115df5 | -19.56938 | -49.43363 | 2026-08-19 03:47:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95568121-02e8-33e6-acba-a9bc045999a2 | -18.84323 | -47.1425 | 2026-08-19 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84b7bc00-b639-39f7-aa0e-227eace05110 | -21.44633 | -48.51599 | 2026-08-19 03:49:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b088b215-5a76-3bd9-8d7a-77e10eb6affa | -22.47271 | -45.37177 | 2026-08-19 03:49:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a2a83f22-45ed-3c24-be3e-fefc996a1694 | -21.52267 | -52.00631 | 2026-08-19 03:49:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ec788502-a393-3801-8672-8f729c74a205 | -23.29199 | -46.16329 | 2026-08-19 03:49:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dd3d130b-7982-327f-9083-5905092eb5a8 | -22.91359 | -47.21833 | 2026-08-19 03:49:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1bd7ae8a-3f73-3455-a7dc-918358d1645c | -29.14083 | -50.39634 | 2026-08-19 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d159f3f8-9b30-3072-b221-baad82791476 | -21.52904 | -52.00798 | 2026-08-19 03:49:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7b62e0d9-ad56-3c58-8456-0237039be217 | -21.7649 | -47.54429 | 2026-08-19 03:49:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a54149a5-311b-3f0d-9bf9-ff96848ffcc4 | -23.75788 | -46.80457 | 2026-08-19 03:49:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 8c77fb8f-75ba-31da-980f-2e9b81037216 | -21.40339 | -48.71198 | 2026-08-19 03:49:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7592dc32-89e2-31b8-bd0d-c77eb26b4951 | -21.44709 | -48.51252 | 2026-08-19 03:49:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 34548cf6-0d9f-3958-85db-64ba11fb83b8 | -29.14233 | -50.38993 | 2026-08-19 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7a123bf4-abbe-3cbe-b9dc-cb6ce69efce5 | -29.14158 | -50.39314 | 2026-08-19 03:49:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f8922ebe-7f12-3e46-a513-622fda83d38a | -23.29105 | -46.16795 | 2026-08-19 03:49:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 56205d16-ce0a-3901-b085-d091b5418d17 | -5.92 | -43.6032 | 2026-08-19 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4df5bcbc-36c0-32a0-885e-4f031ce91813 | -8.56 | -54.7377 | 2026-08-19 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| caa0a719-48a0-3e0b-bded-405651770e31 | -5.9994 | -57.8639 | 2026-08-19 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 411f14a0-1cc2-3cbf-a471-0bb3f56c2283 | -8.5412 | -54.7591 | 2026-08-19 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f99783f9-b252-3fe6-9300-6611b170800f | -6.0178 | -57.8631 | 2026-08-19 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4d462202-f49e-30a4-949c-306dd715b78f | -5.4319 | -48.3996 | 2026-08-19 03:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| b48eb53e-e6ab-3655-97cb-6a761d793d4d | -8.5787 | -54.7364 | 2026-08-19 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d01faa12-ffa0-3b80-82c0-9d98b962b2c6 | -5.4317 | -48.4212 | 2026-08-19 03:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| f4c3e028-8c29-3738-a2d7-6b043f40cd0a | -8.5785 | -54.7566 | 2026-08-19 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| cae42740-967e-3753-9db2-09a2850b6334 | -5.4503 | -48.4201 | 2026-08-19 03:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b01fdc0d-9bbc-3380-be68-1625c55a0941 | -8.5598 | -54.7579 | 2026-08-19 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 43261518-0bb7-302d-bec7-002fd7f55176 | -5.9011 | -43.6279 | 2026-08-19 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 8c9cd769-673d-353b-acfc-18a44a479cc1 | -6.0912 | -57.9187 | 2026-08-19 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| af708032-8673-3ed0-802f-ba6dbd5bfba5 | -8.5413 | -54.7389 | 2026-08-19 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 390423b4-4f88-38e8-ab03-8f51770646da | -5.9198 | -43.6264 | 2026-08-19 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 974a9fdb-74e5-3c49-a4a4-1a4f14b368f2 | -9.3875 | -60.5528 | 2026-08-19 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b9027eaa-674a-35ef-8dab-84684bc898a4 | -5.9198 | -43.6264 | 2026-08-19 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 9d2b4434-ebb8-3e58-aa63-bee0a0d09dc8 | -5.9994 | -57.8639 | 2026-08-19 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 82463069-86b2-3316-804b-e2aabf4c9a30 | -5.4317 | -48.4212 | 2026-08-19 04:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 762595e7-70fb-3594-aa7b-9c6566115498 | -6.0912 | -57.9187 | 2026-08-19 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |


[Clique aqui para ver as próximas entradas](README22.md)
