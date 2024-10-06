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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23e0a4c4-47f2-311b-a9d4-7168342fb1d5 | -13.8915 | -44.60303 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4324c7cd-cb98-3978-bd8b-11ff928cb7d3 | -13.89068 | -44.60876 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72447cd6-c95e-3fab-8c58-982d51ea88d0 | -13.8906 | -44.60738 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16d9aa47-2a1e-3c51-a63d-44dccaad6e61 | -13.88968 | -44.61174 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 537eba7e-ec2e-36b5-96a5-06005a05cfdd | -13.88663 | -44.59884 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 316c96c7-286c-3343-bbf7-0a01ca51757d | -13.88574 | -44.60326 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4bfbaef-98c1-3a37-a8bd-06c7b53adc39 | -13.88569 | -44.6019 | 2024-10-06 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21801198-33ac-34af-b398-7edd11df59d5 | -13.57414 | -43.67505 | 2024-10-06 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb56d71c-934c-363d-8997-358c3154c190 | -13.29539 | -39.91542 | 2024-10-06 03:32:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1992ea6-4b69-3f71-b512-0567f3b26af2 | -13.10043 | -46.39431 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbeda0ec-72c2-3eb1-8530-f85b2630ceea | -13.09939 | -46.39258 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f211f8d2-4b5f-3400-825a-7cac1b02b53e | -13.09797 | -44.70832 | 2024-10-06 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fc55ba0-f989-398d-9f4c-b507fd9c5e04 | -13.09709 | -44.71256 | 2024-10-06 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e6895c8-5413-3c86-b569-d489abfdbda5 | -13.09577 | -46.35103 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6be671e4-3ca3-3208-852c-c79c96f693ab | -13.09504 | -46.38735 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5fea177-cae8-37e9-865e-c9e991fada87 | -13.095 | -46.34943 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eecdff53-3b75-3691-84d5-3659c825bf32 | -13.09408 | -44.71133 | 2024-10-06 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f5eaee5-441e-304d-93db-925ebbf41b95 | -13.09368 | -46.35554 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4f9936b-a057-3ead-82d9-bd003cebe967 | -13.09403 | -46.3857 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c469b5f-b91f-372a-8d4e-28ab1ae26567 | -13.08833 | -42.42073 | 2024-10-06 03:32:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a33b1918-2151-32eb-b29f-304d268f28ca | -13.04984 | -40.5212 | 2024-10-06 03:32:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b7c29a58-55e0-38ab-9089-22e5d61dbb15 | -13.04894 | -40.52593 | 2024-10-06 03:32:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c3112a9b-3899-340f-a842-6dfb36187afe | -13.0484 | -40.52305 | 2024-10-06 03:32:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bd1dcf42-3708-34aa-98a7-011f7385433c | -12.71733 | -40.21752 | 2024-10-06 03:32:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f7141346-c9c4-3439-905e-3ac0bbf2029d | -12.7165 | -40.22204 | 2024-10-06 03:32:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f788256d-1278-3f30-bd07-16d3a1b1ddc8 | -12.71286 | -40.21672 | 2024-10-06 03:32:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a44a13a1-1acb-3773-8911-a3e03ac3c931 | -12.71203 | -40.22124 | 2024-10-06 03:32:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0cc8cc92-391a-3018-a728-117a2116e86e | -12.5118 | -45.29381 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4592cfb-6ab2-37b3-bf55-5f313ba722ff | -12.51075 | -45.29892 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 61e58699-2777-3435-8f13-b587e1930a0f | -12.50971 | -45.30401 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b86bb8b4-7fbf-3b70-bd30-e1adb3484bc1 | -12.50351 | -45.30273 | 2024-10-06 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a8fc46f-bec9-38a7-a6e3-6cf3a1e7ee6e | -12.257 | -41.09608 | 2024-10-06 03:32:00 | NOAA-21 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| c15f6ca9-4105-3da2-a6a1-dc17c1252014 | -12.25601 | -41.10142 | 2024-10-06 03:32:00 | NOAA-21 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 33.0 |
| cba64b0f-a669-3a3a-a468-be3b50b3bc3b | -12.25223 | -41.09519 | 2024-10-06 03:32:00 | NOAA-21 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c411e8b5-630e-317a-ac30-6697c4ad51f2 | -12.25124 | -41.10051 | 2024-10-06 03:32:00 | NOAA-21 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d00afa56-32bb-3ac8-813d-d71c149f3396 | -11.72987 | -44.50276 | 2024-10-06 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4784b024-1f1d-321a-ba79-4fb321f3251e | -8.38757 | -46.29864 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 39d7c8a4-d6ab-33f1-bea7-41111bbdff34 | -8.3898 | -46.29908 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d738020d-3cc8-3356-a63d-cfec79510dd2 | -8.39112 | -46.29221 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f4d7b234-8a4d-39ff-bb2e-d9bd79ce5aa2 | -8.39469 | -46.29957 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 31aff16f-fc88-3a8a-9106-08e39602f7f1 | -8.39738 | -46.28606 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2b015a69-7a94-3be3-85c9-d7d871246051 | -8.39949 | -46.28661 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ee83ee7-0b1d-34e5-aaed-d4d827cb8b7a | -9.02517 | -46.57789 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a6e12b6-9a64-3cbf-af04-01ad3a35df99 | -9.03226 | -46.57917 | 2024-10-06 03:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1183a15f-1776-3bda-8eff-af9deea7ac1a | -9.33139 | -46.54268 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| eb4513af-e74c-3ba7-a45e-ef3efdc939b1 | -9.3356 | -46.55801 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0ff989ed-4975-3c4f-8449-f65b46ebabf7 | -9.33699 | -46.5511 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 39e46309-ef09-3b2b-9898-fac801907cc2 | -9.33839 | -46.54416 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 73630215-fa09-30b7-b81c-fe7f3680d753 | -9.33975 | -46.53744 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1de1ddb9-2486-3cdc-890c-aea29575f372 | -9.34258 | -46.55962 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| adc98521-5c7e-3b97-8d3c-b6d19e802058 | -9.34396 | -46.55279 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 34c2c61a-9ca8-3328-a92c-65f8a2b230b4 | -9.34536 | -46.54581 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a9f9fccd-bd65-354a-8007-8085b8b0a6a2 | -9.34674 | -46.53894 | 2024-10-06 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5f0d4c3c-114c-3d56-bb92-e9cd5d22abdf | -11.72207 | -44.51073 | 2024-10-06 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7d629da-992c-3df2-a31a-b00fea5c87d9 | -11.67031 | -45.2476 | 2024-10-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55490b1c-5d36-3624-8f7e-ccbc27f5f6bd | -11.66313 | -45.25081 | 2024-10-06 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1b16847-2034-36ea-9de1-85995dfc9635 | -11.30255 | -42.07873 | 2024-10-06 03:32:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 54ec6f5b-4006-39a2-8f7d-27c5702fe666 | -10.8418 | -42.85359 | 2024-10-06 03:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 792d89db-3d1d-3e39-9b56-7b6ac0b58a65 | -10.8411 | -42.85726 | 2024-10-06 03:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5bd1947-8f04-3d7b-9f4c-98f013ef1234 | -10.77041 | -42.6883 | 2024-10-06 03:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f49420a6-dfb1-3368-96d6-a1c3cc65f6c0 | -10.69618 | -37.04956 | 2024-10-06 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f7637f4-70e0-3307-a922-a29dab1d2a63 | -10.48417 | -45.18386 | 2024-10-06 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8c89fcbb-fdd7-3819-bebf-0a8d51f200d2 | -10.48314 | -45.18908 | 2024-10-06 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d4a771a4-6424-3ca8-b331-1127f7b40ca5 | -10.22907 | -42.39212 | 2024-10-06 03:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 69add396-1795-3546-bfa9-aa276cd4cd06 | -10.13091 | -42.42615 | 2024-10-06 03:32:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13f1036d-607c-34d9-b7bc-0d046d1221dc | -10.13024 | -42.42968 | 2024-10-06 03:32:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3077bacf-157f-317c-9245-ab31c12d7b73 | -10.05372 | -45.28448 | 2024-10-06 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 755cd6a2-f0f9-3428-8122-3c3059dbd7cc | -11.21169 | -46.58206 | 2024-10-06 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aed20ef5-60a3-3606-b77a-17addf40be6e | -11.21031 | -46.58878 | 2024-10-06 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 26193955-5134-3650-a12f-d7d6dc3a2297 | -11.3099 | -46.79995 | 2024-10-06 03:32:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79bb7f17-4a41-361b-a83b-212249e80265 | -11.31111 | -46.79576 | 2024-10-06 03:32:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8bdbd19e-f720-33a9-a642-036f17a35dec | -10.05251 | -45.29061 | 2024-10-06 03:32:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 914b78ec-c2e1-37a1-907d-ef00863e9f55 | -11.31155 | -46.79206 | 2024-10-06 03:32:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e708b294-167a-359a-bf07-8773d3f6388b | -12.38551 | -46.65857 | 2024-10-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7a3e5254-0e84-3174-b6e5-729a0ff6cf23 | -9.32598 | -40.69044 | 2024-10-06 03:32:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c232f730-715d-34d3-a9a9-9519009d0d5f | -9.24399 | -43.51595 | 2024-10-06 03:32:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c55390af-17ca-3069-b7b9-0ec90afeef5b | -9.24313 | -43.5204 | 2024-10-06 03:32:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0a2b1cf2-b877-3a52-af1c-593f781f0f73 | -9.23962 | -43.51717 | 2024-10-06 03:32:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dc2f5d00-6f77-3130-a096-84c9a85a45f2 | -9.23878 | -43.52169 | 2024-10-06 03:32:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7a1764fb-8db8-3615-9e93-29138aff9544 | -22.83274 | -47.49499 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| de11eecf-3c0d-3194-a2ac-2f849bc06db4 | -22.83045 | -47.48219 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 4e606459-57ce-3ef6-8181-6bb178227bf9 | -22.82942 | -47.48663 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 1cec07f7-421f-3d8c-9c69-02785a1ca319 | -22.82912 | -47.48444 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 0ea2e9a8-91b7-3f22-8bb0-359a970586b9 | -22.82836 | -47.49118 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 30ad93e8-da1a-3c0a-a0e1-0643d4a97845 | -22.82804 | -47.48894 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| c0b84b5c-9d35-303d-8e8a-3c382669c480 | -22.82728 | -47.49583 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 750bccc1-dba4-31ef-ba4c-cb052f642ee0 | -22.82693 | -47.49356 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ce30df92-ca78-3d9a-80f6-3bbd20fb7092 | -22.82362 | -47.48521 | 2024-10-06 03:34:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c5e9938b-1f59-3117-b6bd-dae02005a7c2 | -22.73748 | -47.03974 | 2024-10-06 03:34:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 161035ee-b97f-3b41-9b59-7026f5230ddb | -22.734 | -47.03722 | 2024-10-06 03:34:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b9fbd865-1641-3e24-9fa7-fe88a329faf5 | -22.53838 | -48.81271 | 2024-10-06 03:34:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d2e5e35-8acd-3ed9-96f9-b5631caf0355 | -21.96116 | -41.5175 | 2024-10-06 03:34:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 01aa6f4a-6be9-3cb6-8825-30a812a776d9 | -21.96038 | -41.52146 | 2024-10-06 03:34:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a5277f95-939e-3531-a1cd-11eb0c17d433 | -21.93279 | -41.55282 | 2024-10-06 03:34:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e16bb0c5-0f94-38cb-972c-b35b54bc89ee | -21.932 | -41.55681 | 2024-10-06 03:34:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fdb319a3-c6b8-39a6-b5dd-0c2db28fb08a | -21.85659 | -48.44233 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66b35886-9b74-3788-9cde-14b75ea587ae | -21.85524 | -48.44784 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 334f901f-5ec2-3075-92a7-b1e07c81d314 | -21.85331 | -48.44221 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 484c229b-0bc8-34d1-aa6d-0a5b77753c58 | -21.85201 | -48.44771 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53709205-cb57-3f93-aede-0a0517c528ea | -21.85068 | -48.45329 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README43.md)
