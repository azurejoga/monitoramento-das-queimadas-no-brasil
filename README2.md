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
| aa3deb10-9d8d-3509-8b53-84a3f6241c1d | -21.59226 | -49.14271 | 2025-09-07 00:09:00 | TERRA_M-M | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 2589e7e8-18a1-386b-be8d-e9562017f5e3 | -18.98835 | -44.23205 | 2025-09-07 00:09:00 | TERRA_M-M | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 29e01a29-83e7-3505-8e0f-cc34e7337d78 | -19.53553 | -41.55089 | 2025-09-07 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 6ceabcfb-a691-355a-9e7e-f0f55ef48e3a | -15.54461 | -42.66556 | 2025-09-07 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| a8310679-a3ae-3997-9de1-440f7f435687 | -11.51811 | -43.25129 | 2025-09-07 00:09:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8f64f7cc-9385-3eb0-890f-45acda00de1b | -16.33315 | -41.95484 | 2025-09-07 00:09:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7394d99b-11d8-36ee-ad11-e305bbfd2137 | -11.41207 | -43.62218 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d68bf764-46a3-3964-8a69-2139681aad52 | -17.55248 | -44.40203 | 2025-09-07 00:09:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 67e2d43e-77b4-3c55-b76b-23949497db01 | -13.00796 | -45.22346 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 83e13929-18ab-36e3-a6cf-ce7a5986438c | -17.69018 | -43.54425 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c2a1098c-8024-3116-9a37-10302d38ab42 | -21.20344 | -44.32889 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 00a5d08a-7d99-39d3-adc1-d910a6a2bd5a | -13.11134 | -44.84502 | 2025-09-07 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 090c28f7-6eac-3881-89e5-b7e0de08cb9b | -21.58962 | -49.11092 | 2025-09-07 00:09:00 | TERRA_M-M | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d1a3d48b-aa56-3202-ad7b-7220feec9d72 | -13.11452 | -44.84967 | 2025-09-07 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8ad6c4cc-73cf-3437-a6ec-c52eab8f2ff6 | -13.83367 | -46.26963 | 2025-09-07 00:09:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ffd35bff-128b-33f3-9f72-8f78ee9fe49f | -19.8981 | -41.44202 | 2025-09-07 00:09:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.0 |
| 47a7544c-26e8-3f30-8b82-c89e938d340e | -11.40956 | -43.60342 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 689186ca-710e-3280-b171-22f17b9bb699 | -21.20897 | -44.33372 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.4 |
| cd872572-411e-3a8c-8c34-260ea8f91133 | -13.8227 | -46.27045 | 2025-09-07 00:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c3298c28-d962-3c93-9ab2-744f958c772e | -16.1716 | -42.19017 | 2025-09-07 00:09:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 77ebb124-320c-34bf-996f-57697522431f | -12.73888 | -45.11424 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| eeb4dd74-cfa9-3400-82cb-997f0a2318da | -21.65167 | -45.19762 | 2025-09-07 00:09:00 | TERRA_M-M | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 2746165c-5f12-328d-8b13-9ce4ae907296 | -16.94318 | -45.765 | 2025-09-07 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d63a2df3-c938-32ee-8dec-2ca01674fafc | -15.10885 | -48.07767 | 2025-09-07 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| db1ec2d0-3759-30ee-b8e9-f6103da92d40 | -17.68199 | -43.55643 | 2025-09-07 00:09:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 839df3d2-da10-3489-b233-a41ab92fa903 | -14.74603 | -47.5104 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ddf2d7ac-f9c7-3705-b433-ab61406de733 | -21.17738 | -44.94189 | 2025-09-07 00:09:00 | TERRA_M-M | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 0e40e508-fcde-3591-a241-05a6b52ff054 | -13.82479 | -43.85833 | 2025-09-07 00:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 75254d5a-f2e8-374b-a5f9-683b533a54e6 | -15.53561 | -42.66687 | 2025-09-07 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 0c313024-40de-3d47-9fb2-4cd06bc0c48d | -17.55365 | -44.40788 | 2025-09-07 00:09:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 34.9 |
| b5442032-c59b-3380-b5dc-64456bbfa600 | -18.63581 | -43.26759 | 2025-09-07 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1d01ce41-3486-384a-8bd1-e067081645eb | -16.92461 | -45.79739 | 2025-09-07 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3522d13d-9e9c-301f-a492-ba03e4ed4937 | -17.55212 | -44.39567 | 2025-09-07 00:09:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8d7117fe-b294-305e-ae78-113beb89da4d | -11.41332 | -43.63158 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 71b5dafc-d462-3db9-8777-de9b9e26adb6 | -21.20496 | -44.34255 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 56d0c87e-cc17-3d13-b4fe-9e09c06adf21 | -13.18877 | -44.4791 | 2025-09-07 00:09:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8cb2e837-afd4-33f9-9a7e-689b6e2021e4 | -11.40304 | -43.62344 | 2025-09-07 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 3156279a-0605-3324-b58a-321f73e00aac | -19.66349 | -44.87812 | 2025-09-07 00:09:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 830ccd84-345c-309f-b61c-fcc0cbfa547e | -14.84535 | -46.68436 | 2025-09-07 00:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 51d97247-47a5-3399-b3ad-a89af41e7d45 | -13.47674 | -43.50839 | 2025-09-07 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3ac6edb0-3a34-3843-8ed9-e65df2044cbf | -17.55399 | -44.41471 | 2025-09-07 00:09:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 55d03e05-1f7c-3c15-8fdc-404fd6ccb5af | -20.73793 | -43.29175 | 2025-09-07 00:09:00 | TERRA_M-M | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 6d63bac8-6cfa-36d2-bb5a-562e11225d63 | -12.57447 | -44.62676 | 2025-09-07 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3e903d1c-dc60-36d4-89bb-01796fd57ea9 | -14.29388 | -43.56829 | 2025-09-07 00:09:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e6b71cf4-52b9-3c75-8ac6-8a21c1884dab | -17.68867 | -44.5164 | 2025-09-07 00:09:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e934374-fbdf-3646-936b-484ad3e98683 | -18.63446 | -43.25679 | 2025-09-07 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 4a53658f-8750-34d3-9455-73589445dae8 | -14.57138 | -43.72628 | 2025-09-07 00:09:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0ae7cb85-0f74-33fc-9708-7cbd0d96adfd | -11.29138 | -41.999 | 2025-09-07 00:09:00 | TERRA_M-M | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 268cd9bb-8c8c-312a-96ad-cf25ef0043e4 | -19.88787 | -41.43379 | 2025-09-07 00:09:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| f886f3b0-91cd-3714-9001-ee498aef113b | -15.53436 | -42.65746 | 2025-09-07 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 2da7e188-47ed-35cd-9ff2-7e55044c7de4 | -17.01577 | -49.18014 | 2025-09-07 00:09:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 4bb7e9cc-9a95-38df-bcce-dd0493a2c40d | -19.4143 | -44.31108 | 2025-09-07 00:09:00 | TERRA_M-M | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| efa8d65d-ac6f-320b-9ad1-34cc3ee16a9b | -21.18024 | -44.95038 | 2025-09-07 00:09:00 | TERRA_M-M | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 4b08303d-9212-39bc-8f94-ece55b5e5baf | -16.92288 | -45.78247 | 2025-09-07 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c390701a-d27c-32e7-b5ad-b8bb762f9f6f | -13.78968 | -43.16584 | 2025-09-07 00:09:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 48bb10fb-8241-333a-95ab-e120fc5064de | -17.95319 | -45.30035 | 2025-09-07 00:09:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 11cd2699-5600-3536-abd2-255d9bafe771 | -12.01423 | -47.7827 | 2025-09-07 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 4ec33de3-0d7b-3c5a-b87d-4e2e71e47ad3 | -13.33191 | -43.25151 | 2025-09-07 00:09:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 7d070a4f-1b95-3ec5-b763-0e79c0486808 | -10.6128 | -44.3284 | 2025-09-07 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ccd1e145-ee56-3e1a-8237-3737b8fa39d9 | -10.1479 | -48.744 | 2025-09-07 00:10:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2a71e988-9be8-3e27-8773-7075fbb0691a | -12.7832 | -52.9477 | 2025-09-07 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| d5cfb2e0-5c18-316b-9578-1764efc7374e | -1.9484 | -56.5868 | 2025-09-07 00:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| dafc61b7-232f-3932-9dfd-61922e0b2e99 | -5.9899 | -44.1528 | 2025-09-07 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 239.3 |
| b38d2ea8-b8cf-30a0-8b3f-ab1d7797d7b4 | -1.9301 | -56.587 | 2025-09-07 00:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 18c3b48d-da13-3d4e-b32a-1403ea987d9c | -7.7591 | -48.8189 | 2025-09-07 00:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f0a88a41-55ec-36b2-9c24-2e4681730601 | -3.581 | -47.5149 | 2025-09-07 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 0794d6b9-a2bc-3955-9d2b-2a3bee0b20e1 | -9.4309 | -62.3683 | 2025-09-07 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 5646f135-3095-3d59-b7f0-37dc31358036 | -7.7404 | -48.8204 | 2025-09-07 00:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d787cbe1-f135-3557-a901-e467c37b09f2 | -11.5958 | -47.1588 | 2025-09-07 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a0e7f7b2-c750-3dfe-8655-56bf3f7f8fd2 | -11.4085 | -43.6046 | 2025-09-07 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b027ba57-aab4-3cb4-9cfa-f1749baf5c18 | -5.0454 | -45.3125 | 2025-09-07 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f06c4ff9-d2c7-3352-8dc9-76098e311980 | -11.408 | -43.6283 | 2025-09-07 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 5c929c7b-32ef-37eb-ab24-4450881da746 | -10.3741 | -44.9615 | 2025-09-07 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| d6ebfeba-0a68-316f-a90f-af2558bae616 | -7.7589 | -48.8405 | 2025-09-07 00:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 047089ca-e583-38fe-bfe5-cddbb677b081 | -11.0407 | -54.1772 | 2025-09-07 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0874c15f-02ef-3bc2-8ee3-4b32744f4325 | -15.1044 | -48.0659 | 2025-09-07 00:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 76090022-075f-338a-ba0f-5a740998fa85 | -3.5995 | -47.5142 | 2025-09-07 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 79cd78c4-f723-36a5-bff9-cc27fcbd6b28 | -19.8853 | -57.9031 | 2025-09-07 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 0566d836-574e-39b7-81ef-9b3b8132ef53 | -6.0086 | -44.1513 | 2025-09-07 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 77995b9a-ceb5-3f25-8f12-9700896b6a35 | -11.4961 | -55.5613 | 2025-09-07 00:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a047c8b1-4578-3d08-88e8-4845b5478a26 | -11.6149 | -47.1563 | 2025-09-07 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 26af6f7d-50aa-3401-9788-dfd22581b423 | -15.124 | -48.0627 | 2025-09-07 00:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 10001379-62b7-3ef4-85c2-3ff03f2bcc0b | -11.4076 | -43.6519 | 2025-09-07 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 2790130a-60a5-3805-8e20-c3d2f7117a53 | -19.9021 | -41.4455 | 2025-09-07 00:10:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 6430e62a-55cf-3b9d-89ef-5f96556f926a | -10.3932 | -44.959 | 2025-09-07 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f1b9b2c9-fadf-3ff4-9bb3-21a5ec605b9d | -17.6785 | -43.5334 | 2025-09-07 00:10:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2f859196-35c3-3365-a7ca-254c79b7cb57 | -9.4495 | -62.3675 | 2025-09-07 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 7a527aa2-9cfd-3d2a-8b4b-8cf5cc47d7fc | -11.2194 | -55.0178 | 2025-09-07 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 51776951-142e-3f23-ad27-6e54135ee5a1 | -6.8095 | -52.8154 | 2025-09-07 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| c612208a-a1cc-3f77-b384-58359b0bc44c | -9.4311 | -62.3493 | 2025-09-07 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 4ab7303d-5485-376c-a349-ed2b9e212801 | -6.8281 | -52.8143 | 2025-09-07 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e5f1bf01-30ff-3380-af1a-ee0d0e8a0787 | -6.59173 | -44.00005 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 91a6538f-5e5a-3fba-bb5e-f6a55b96cbf7 | -6.59815 | -43.98103 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f9675b92-b934-34f5-b044-3c282f6eeca5 | -5.48809 | -45.90692 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 66260668-9c76-30a1-9894-45c6bcdccd09 | -8.11609 | -45.31773 | 2025-09-07 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 45891135-34ef-3354-ae75-174a4f1f0a01 | -5.46166 | -44.1658 | 2025-09-07 00:11:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5d9b6c81-7f00-344b-a1f2-a0bfca30da7e | -6.55594 | -42.9447 | 2025-09-07 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 515f0e76-02b4-31a7-ba72-29028d480487 | -6.97026 | -46.51705 | 2025-09-07 00:11:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f552ee8a-06f1-379b-a545-7c5bfff47a14 | -6.23142 | -42.60093 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8b3e80a4-0eb5-3b5d-aef7-a91c074fcd77 | -6.5905 | -43.99111 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README3.md)
