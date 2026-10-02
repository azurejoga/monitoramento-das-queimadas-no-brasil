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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70a19ff0-3688-3ce2-881f-5395e913885b | -16.48771 | -43.14843 | 2026-10-02 15:52:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75b5add2-40e3-3d5a-beb0-984ed5fbce7b | -15.48784 | -41.53484 | 2026-10-02 15:52:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3e0de627-6146-392f-a95f-8e512e1768bb | -15.74467 | -43.65253 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ac69df31-fe7e-37ed-b058-d48982c1a9bc | -15.86157 | -44.29554 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 28bbcaf2-bdac-36ee-b99a-c9d5aed30c97 | -14.47619 | -41.21424 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 2434598b-de56-3a34-9f6c-7d319c8b1a6d | -15.87228 | -44.29039 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 224.6 |
| d13268a1-f7a5-33fb-8adb-d7d19c161fa7 | -13.83323 | -45.23529 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0fb12836-8896-3b65-98a9-e029224b8886 | -13.81066 | -45.2423 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b20af6dc-47b9-39a8-870f-9169a8f889a2 | -16.17391 | -41.84571 | 2026-10-02 15:52:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 4a200c0a-f7ef-3e6b-98ac-c7e9c77a2d7c | -14.37687 | -41.53246 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 5a8a2122-75bd-3425-8f5e-975437c8443b | -17.99132 | -43.65152 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b06d5a6a-c1cc-387a-99ff-4fb2eb62cdc5 | -14.02909 | -41.5988 | 2026-10-02 15:52:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 662f8190-85b1-304e-989b-baa0b19bb5a3 | -14.49043 | -40.89801 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7fbfc3c9-8ed2-3a70-bb15-86af8c8d2ee1 | -17.2097 | -40.28537 | 2026-10-02 15:52:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7a16e3ad-a62a-384b-9322-f7e68d75ea92 | -15.19212 | -41.55999 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 5d7e22c8-250c-3d9c-89cb-6e9c7c27f801 | -13.86592 | -43.64428 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 252a3d6d-a218-35af-b9e1-a4c87a8fd058 | -15.13379 | -43.58278 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 33.6 |
| b86cf04b-bcee-3617-a6b2-2815510e1282 | -15.77169 | -43.65291 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b305d27e-9836-3726-9746-a09cd1c8d945 | -17.77508 | -43.61833 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 44c10849-284e-3dd0-88cd-0a211f0d2d42 | -14.14152 | -42.12096 | 2026-10-02 15:52:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3d8ca5e0-1a45-390f-8a0b-d4d191cc3051 | -15.47799 | -40.49609 | 2026-10-02 15:52:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 00971018-7d82-3219-90d9-f34dd254513c | -15.877 | -40.77696 | 2026-10-02 15:52:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 79cb47cf-bc1e-3f8b-81e6-33e973ef2507 | -13.7457 | -41.10439 | 2026-10-02 15:52:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3dda0816-f9a3-3f1b-a54d-7947fafd42db | -13.86965 | -43.63107 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bbd6d267-9099-31f9-b755-13ffe734f3e2 | -15.77585 | -43.64231 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 66805df3-c0b6-3109-a4b1-9168e0364445 | -15.13001 | -43.59665 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 3a4f8186-abe6-33dc-95cd-652a88151b25 | -14.07287 | -40.55592 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 2e927197-8922-3e09-86a2-38b9abe92de6 | -13.78608 | -45.24072 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3b00b1be-aa80-3592-a9f1-01e0501a80f6 | -17.53348 | -39.93887 | 2026-10-02 15:52:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 43b9e390-cf99-3ae0-84a4-4e3840293d3c | -15.74959 | -43.64848 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9f14c5f7-fdb0-3be5-8448-9c7987a4a37d | -15.97942 | -41.43583 | 2026-10-02 15:52:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.1 |
| 19906c20-8780-35f6-8c79-bf32b1577731 | -10.28106 | -36.78578 | 2026-10-02 15:54:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5a03ac2b-0826-316f-bc01-c8a81664247d | -8.7982 | -45.81078 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4723acf-f7b5-35a8-bb4a-8c1cbac1840a | -13.33912 | -43.84812 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f49a3ab4-dffa-3da6-a718-5b4e42c4565f | -8.12089 | -44.80368 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1e9e8e84-6564-3233-badf-a4565c04bb74 | -9.95215 | -43.46148 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a41a62ee-05de-3382-bfbb-1d3d3065ce8e | -11.77653 | -43.58333 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c67f5e82-fd11-3c50-80bf-a96f9294193a | -11.70995 | -43.62024 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 3b0c78ce-d23d-3ab0-9d67-3e943a0af86c | -11.7124 | -43.60103 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 548f54f3-4ce4-3372-acc5-dc148beebf13 | -11.11694 | -44.58699 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aafdedd1-53a8-395b-91be-2399486af404 | -12.89753 | -44.7336 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 93c3dd71-a25d-3580-aeee-3410663757be | -10.88631 | -40.64616 | 2026-10-02 15:54:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c566aa97-df5d-3dd3-8f25-368d8ca33f05 | -7.52954 | -42.05917 | 2026-10-02 15:54:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 19fa7e26-e3ed-3580-9d54-41978f1cef84 | -11.28694 | -43.54911 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8f3414a8-c3ef-3077-b9da-85a271c21190 | -10.69613 | -45.3186 | 2026-10-02 15:54:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6824f40a-0651-313e-a0e6-66618ac76ddf | -13.33872 | -43.84488 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 80d562c9-1aea-3350-8512-b4552457e091 | -11.65111 | -43.59919 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bae3cd73-de05-3b83-bfba-d04dcc40bef3 | -11.47398 | -43.41687 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3f1a48be-a115-38f8-a9e3-037f4c17496b | -12.78029 | -45.17007 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3fe664a6-942b-3d35-a7c2-68d5a58cda86 | -11.14404 | -44.58738 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9da8870d-9d45-3bf7-a1b0-ea680010210e | -11.72613 | -43.42548 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| c0a2fe3d-a4b6-3b2e-b77a-03823fe9c525 | -11.27795 | -44.24723 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f5cade6b-4726-366b-9adb-55fd0a31a5a3 | -12.53589 | -43.08675 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 4c545562-f6d3-3b95-abef-77db108dd3a0 | -12.77424 | -43.28273 | 2026-10-02 15:54:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 3f09b365-4f9b-3803-95a3-2bdfbb85e2f1 | -11.52555 | -40.88979 | 2026-10-02 15:54:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d4cf11f3-4c71-371b-a1f9-d47761731d65 | -11.70242 | -43.60152 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e438fe26-bdb8-3d6d-acaf-f41c87d4b3d0 | -12.17107 | -44.65822 | 2026-10-02 15:54:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| abe7e5eb-ff07-3110-b16d-28af626df439 | -11.70197 | -43.51605 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cd9ed652-863f-376a-b401-2aabe3585b5a | -11.64707 | -43.56717 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a88fa395-23d6-34c3-89c9-b0efedf19596 | -12.48413 | -44.15031 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 351.5 |
| 3448d4b1-3883-35ac-b1a5-f868d230bd79 | -11.48816 | -43.52479 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b52f6e47-6b59-368b-af19-64a1a46b0c68 | -11.49739 | -43.51792 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 75dd52e5-5ce3-3585-bffe-6ce20ab218fd | -11.47319 | -43.4387 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| eafa1c69-b83a-3274-a61b-6bc2404a00ac | -8.78848 | -45.8124 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b6127ba1-d93a-32ef-89b8-bd396ad4a50a | -11.41717 | -44.88697 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 5fd9798f-0ee3-3808-bc46-1703ca1655a6 | -11.71664 | -43.59401 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 868ef8fa-8d35-3db4-99d1-49480aca3a6f | -8.1269 | -44.79562 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| d8265045-cc24-36b2-baa0-9f5d80bc221a | -11.469 | -43.40477 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| aeb479f1-936f-35dd-81c3-2fb2663bb3cd | -8.12734 | -44.79899 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 60600972-afe1-3ac9-90b7-89540c3129ee | -8.11708 | -44.80114 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a3b09f12-92a7-3c44-933a-6f53f00e75b5 | -8.80427 | -45.81374 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 77705dfc-f39c-3dae-8c9a-dcf3c81bb7df | -12.44114 | -44.19317 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d788edaf-fafe-3860-a364-316fdf71d515 | -13.33948 | -43.84311 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1ce708a2-34eb-3623-953b-869a8a2a5e92 | -13.34177 | -43.86287 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8a49cfcf-33ad-3fc8-91f1-c27dccec7572 | -12.47806 | -44.14441 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| cdac6ae6-6632-315c-9e73-1603b3e39595 | -11.68374 | -43.4966 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f8b55f93-f105-39eb-868a-e69e781a8060 | -8.81075 | -45.81992 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 952f4268-26fa-3eeb-9f33-cddeb45530e7 | -12.50075 | -44.15496 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 59c3fc2e-fe5e-3ec6-b3cf-5ab378578f67 | -11.73507 | -43.57811 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| d0be4ac0-ab06-38c5-8ddc-db0a2393f967 | -11.61092 | -43.56278 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16c99a2e-2e55-3b18-a3ec-94fa11439c7e | -9.93617 | -43.45267 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 215906d5-213b-3f3c-b1a4-1ebef3331140 | -13.3447 | -43.84251 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c88505f4-13eb-350d-a495-3db4c42433a6 | -11.71497 | -43.61952 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 7f749714-0f5d-3d86-986b-2b340908b29e | -12.5678 | -43.06304 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1c263c8e-f60c-3590-96a6-bba03a44f6f7 | -7.00916 | -40.35564 | 2026-10-02 15:54:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4c850036-e6df-3749-9985-a32104b68b27 | -11.71096 | -43.58867 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 694fd21a-d2ba-30b9-99ed-916ee2725710 | -11.46334 | -43.41238 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 48bcb714-014b-3daa-9944-f52f0ff23067 | -11.24752 | -44.30711 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 312d2994-c400-3012-bc8b-d09e31cf5ec8 | -12.19065 | -38.4002 | 2026-10-02 15:54:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 43239583-6c37-35ac-b4a4-8dcb4e2f8870 | -11.64524 | -43.55269 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4092e428-b341-34cc-a884-533172f606be | -12.86442 | -42.74808 | 2026-10-02 15:54:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| d166e379-8408-3d69-8084-b0c11ce09162 | -10.92734 | -43.84588 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 37ecdd81-3eb1-3d51-a9fd-88b0d89c0b94 | -11.69749 | -43.52435 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4f12f490-5919-3e1e-ba2c-2d4e9c6feece | -11.16341 | -44.61213 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1be14203-795c-35d4-b022-979171b293f2 | -12.37673 | -42.22544 | 2026-10-02 15:54:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0b57cfcc-f9d3-3882-b96c-af92bb90c3ef | -11.71173 | -43.51677 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 30780367-e5bb-303e-8220-637ff7a32f54 | -12.17425 | -42.06791 | 2026-10-02 15:54:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 903a864c-55c7-371b-9ef7-31c534024763 | -11.73253 | -43.43629 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| feccc19d-3408-3453-a86e-b8960a969ca0 | -12.49426 | -44.14571 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1dd1d392-34bb-3a76-8792-361d98687912 | -13.3563 | -43.85099 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |


[Clique aqui para ver as próximas entradas](README96.md)
