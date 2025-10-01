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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9351fcc-0540-3956-8e57-226bb61cd2fe | -19.71174 | -45.87332 | 2025-10-01 04:23:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdb7741a-9ce8-3d56-a541-fe94674b1d42 | -20.59196 | -45.8853 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e162451f-5bde-3ede-965c-6e28d2292fc8 | -20.79793 | -43.51848 | 2025-10-01 04:23:00 | NOAA-21 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7d96322c-d24f-3639-8cab-cbe506895e14 | -20.79714 | -47.54717 | 2025-10-01 04:23:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0f45551-4796-3d6d-9915-5b37a102863a | -19.59862 | -43.83867 | 2025-10-01 04:23:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09b22e5a-5aa7-3064-a90a-87083a45fc45 | -22.11779 | -44.70414 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| df4d7179-4bc2-34c2-8ce5-2b1376e76f20 | -20.53017 | -43.45021 | 2025-10-01 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 006f96a3-58ca-3fa7-ac62-31246d2166be | -18.25642 | -43.13962 | 2025-10-01 04:23:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 64474356-d4b9-3e52-8ab9-104fcca775b7 | -22.43736 | -48.30943 | 2025-10-01 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4965b271-0a3d-3cee-8373-af8115bbc15c | -18.76645 | -47.24495 | 2025-10-01 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db920508-d1e9-3ef5-b5bb-62bf4bbc95a6 | -21.57468 | -44.21855 | 2025-10-01 04:23:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| be5d6e74-8045-3db8-b53b-9b9b9d00cdd3 | -19.85844 | -42.58626 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c219eebb-9069-3632-8461-77816fd839b4 | -18.6193 | -46.29185 | 2025-10-01 04:23:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf1475ac-e237-3f80-966a-65e778cafb52 | -22.26868 | -46.71135 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 20796278-681c-3cf5-9a80-df38140020d0 | -19.86335 | -43.82716 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 4644be25-2a7e-3a64-91ce-2643e587cc27 | -20.42665 | -48.86464 | 2025-10-01 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99e9f51c-4620-3617-b09d-68e1654a4319 | -21.0442 | -45.67999 | 2025-10-01 04:23:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 112ed219-c716-34c9-8ffe-ca4f963574d1 | -19.8677 | -43.82317 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7f98fabb-909a-3472-80b5-b91ffc848197 | -20.47999 | -43.94321 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c6179ee8-00fb-3d8e-a861-f680bb1b86c4 | -23.36539 | -47.15778 | 2025-10-01 04:23:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3fb1a7b3-f0b8-31e9-8cf7-090297a850e0 | -20.03191 | -44.54789 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0b2feeba-660b-3164-897b-8475b81394d5 | -17.96656 | -45.01198 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc64bbc2-08f3-3f49-8bdf-248b28aaedc5 | -22.24061 | -43.41385 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5be42b5f-0ad1-32b0-b437-cd4c29db392e | -22.11605 | -44.69294 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c4e2eb70-966b-3c0d-9b0c-16d96ba48790 | -21.46604 | -45.11285 | 2025-10-01 04:23:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74efc9e3-c03e-3379-98fd-c0abcab456c1 | -20.62442 | -46.21964 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff39d1d7-ccb7-3b65-b673-9f414d462346 | -22.29562 | -47.74953 | 2025-10-01 04:23:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b873c07d-6221-3af0-b36d-0ea626c5a507 | -21.04146 | -46.91496 | 2025-10-01 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf65ffe1-fccb-3a2a-8702-34af23309ffb | -22.10652 | -47.80849 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0df5ffa6-106a-3475-aad4-395aa805888a | -18.60554 | -43.27222 | 2025-10-01 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 84e52ff2-d410-3ad7-9bb1-5ddf8de61a29 | -17.95682 | -45.03054 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5db49875-cecf-3c0d-9f28-3d08e576ff53 | -22.65462 | -46.74968 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 42dc998c-bc09-3ef7-aa18-2ecc6885fd12 | -19.16454 | -44.53045 | 2025-10-01 04:23:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 39113f68-a4ae-36c4-85ce-62b304e5e860 | -19.89446 | -42.62548 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fab93482-3d17-3444-bb42-4ecd6f292fae | -19.9305 | -43.89642 | 2025-10-01 04:23:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9eb28e68-05e3-350d-af24-2a4e9017b724 | -18.32455 | -44.77834 | 2025-10-01 04:23:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30867222-8ee3-33a9-b1f8-5c94839d53ca | -19.38951 | -46.542 | 2025-10-01 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbbfebd7-1a1e-3163-8db5-539214d6df2c | -17.83969 | -46.16637 | 2025-10-01 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5647301f-c47b-3a60-9c97-12c8084d9f4b | -22.11725 | -44.68409 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 53a22b66-d280-3660-8edb-35af703e4b2f | -22.12011 | -44.68643 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 184b8148-13fc-3b51-9f63-3f39df951769 | -20.59253 | -45.88135 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 72d868fe-4e6d-3f56-8a33-e6d39473c7f9 | -22.3447 | -45.17961 | 2025-10-01 04:23:00 | NOAA-21 | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 03a4cc53-7183-3807-8321-0041d92d0b8f | -22.11545 | -44.69739 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 31a2454c-2f4b-395f-8b20-cc4b6a5b3340 | -22.26929 | -46.73112 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1a380503-ce79-3df3-85db-6ae674d004c9 | -22.28851 | -47.72906 | 2025-10-01 04:23:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08d112af-c03e-31f1-ade6-7c9b9502e602 | -22.58057 | -46.78092 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 128c1e93-47ee-3198-8562-634d27068e63 | -20.03007 | -44.53439 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 378038a4-1a59-3793-a010-1ff505448048 | -19.96632 | -43.71632 | 2025-10-01 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e276dbb9-2769-3854-9c9e-fb91ee82f506 | -22.2923 | -47.74897 | 2025-10-01 04:23:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 331296e6-33b4-31be-8777-8e2527846b76 | -23.46949 | -46.20905 | 2025-10-01 04:23:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 085b27ea-1dfd-3c33-ba25-5e20480b29ac | -21.57028 | -44.22297 | 2025-10-01 04:23:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f5964737-d2d7-3f4b-9405-14f6c0bf5749 | -18.30828 | -44.02903 | 2025-10-01 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb08f9d7-2779-3fc7-b3ac-c35eb1cdbc72 | -19.93543 | -43.88821 | 2025-10-01 04:23:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 35b3c7d4-e5ee-37af-b1fe-42790dd384a1 | -18.96423 | -43.70433 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a200e1d-d0d7-3ced-9693-418b35d5399e | -19.84997 | -44.5906 | 2025-10-01 04:23:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 877c3b04-5fa5-351a-9760-6e8acae38dde | -18.75133 | -44.85116 | 2025-10-01 04:23:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1efc503-d3e1-352d-9aa2-acf565650d1a | -18.44933 | -48.03074 | 2025-10-01 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7df98129-20d8-34bd-a40a-258b7ea16781 | -22.1104 | -47.80534 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77a05616-a6ae-3520-9d91-196b68b8f084 | -18.52954 | -46.05091 | 2025-10-01 04:23:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdc1444f-136f-3623-9e01-ccc12a92c8e8 | -17.70234 | -46.71414 | 2025-10-01 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d53db9cc-67f2-34a6-bad4-311845f63509 | -20.50086 | -43.93713 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 47b86b4a-cf9c-378f-b776-a8202e9875ad | -20.00838 | -47.03637 | 2025-10-01 04:23:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68668650-7c39-365c-9c2a-9a58ef6e2f8d | -20.49328 | -43.93663 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e5fda40e-912b-33e9-bb7a-fc728cd474ad | -18.96492 | -47.87033 | 2025-10-01 04:23:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae391cba-d962-39bf-a7ed-84e36b468a3a | -19.37878 | -42.77654 | 2025-10-01 04:23:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d1f2ae30-e983-36e2-a9f8-20964052ed4a | -19.79937 | -49.05859 | 2025-10-01 04:23:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f06e3bd-3051-37c3-b26b-9fb27e57ba9c | -20.1265 | -46.33914 | 2025-10-01 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1bb5a1b7-7e81-3373-84c1-9778caaf99c4 | -22.11529 | -44.69455 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 677033ea-1299-3f8b-95ea-0c5e36064fb8 | -18.71503 | -49.17064 | 2025-10-01 04:23:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7af80818-df51-3725-9898-c9b94d28e19a | -23.59069 | -46.21856 | 2025-10-01 04:23:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a210c13d-ef20-39ae-a987-b2c04ab81cd2 | -20.53082 | -43.4452 | 2025-10-01 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1221c6a8-ded7-3f6a-ad13-ac614a4dd445 | -17.95917 | -45.03896 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bc21c9c-f3ca-3e81-a757-bf988c05c5e0 | -18.92303 | -43.11695 | 2025-10-01 04:23:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc1890fd-a2b7-3925-944e-6a53cd144b5e | -22.98504 | -48.35257 | 2025-10-01 04:23:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6236d6c0-173d-39e3-93f1-7cae089cbf77 | -22.25831 | -43.43322 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ab5cc1fd-092d-313f-a691-a3c573b1b7c0 | -19.70636 | -44.01003 | 2025-10-01 04:23:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65fd147d-e787-3f70-8d83-a90cf1e5d6da | -22.74825 | -46.29448 | 2025-10-01 04:23:00 | NOAA-21 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 98b35de7-c433-3f2c-8077-258304a5316c | -20.48669 | -46.30106 | 2025-10-01 04:23:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecff2c2e-3148-3490-a510-76b7a3650de9 | -20.84908 | -49.43319 | 2025-10-01 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b578f58b-3552-3247-a85f-9aee228f5be6 | -17.67943 | -47.25839 | 2025-10-01 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18aa059b-8b68-3618-8af2-365574c1cc75 | -22.11371 | -47.80591 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4a5225e-d243-381d-acff-c725bd8942df | -20.74185 | -49.42176 | 2025-10-01 04:23:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bc086c9-10f5-3d9b-ab37-2c9e4837bc63 | -22.26813 | -46.71521 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8f735a14-b7d9-364c-8964-efb375006206 | -20.48312 | -43.94843 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 187e10ab-363e-348a-b029-445f8f8c5d06 | -18.276 | -43.71591 | 2025-10-01 04:23:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cfa278c-92c7-33bb-b9dd-3302b5293534 | -18.70171 | -44.33465 | 2025-10-01 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ff9c6a4-c66d-3650-a4fa-30189af40a51 | -22.29127 | -47.73337 | 2025-10-01 04:23:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95e14c26-10f5-3880-9c06-d9f43bb912c8 | -22.43689 | -48.37801 | 2025-10-01 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ec100e1-12ce-30bb-ba49-f2740385281c | -20.62101 | -46.19506 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bca43a9c-ec41-3bf3-8dbd-870e948c87f6 | -18.90068 | -47.21162 | 2025-10-01 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f133850c-e0a6-30c6-8a5f-5c06ee4ad727 | -20.43669 | -43.59755 | 2025-10-01 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a15a9c85-7e75-3549-8954-f982d2f90887 | -18.92103 | -48.16862 | 2025-10-01 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e9d6afb-1d40-3187-960e-420bd6b89767 | -20.98631 | -45.54989 | 2025-10-01 04:23:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97415cb5-c3bb-322e-9a4c-478155bef270 | -22.10434 | -47.80052 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f7590d9-9671-3d43-867d-a697672f83a2 | -20.03251 | -44.54352 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e848ea3a-8983-3f13-81c3-a097ea309910 | -21.35009 | -44.89913 | 2025-10-01 04:23:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2c42bfcb-81f8-3bef-b35f-68de1e0ea346 | -20.11525 | -51.80346 | 2025-10-01 04:23:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9d941ae-1c34-3ba4-a8b5-01ff948aa65c | -21.66294 | -45.33461 | 2025-10-01 04:23:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fbbb6dbb-0c50-3627-8598-3aeab505c27f | -17.97293 | -45.01705 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3fefdce-aa5a-3c4f-8d44-a8512e6a9e07 | -19.24306 | -46.54898 | 2025-10-01 04:23:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README80.md)
