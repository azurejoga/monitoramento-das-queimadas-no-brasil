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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70fd66a2-53ae-34c5-ab42-353f973a9e06 | -6.46249 | -44.57839 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 400e205d-e598-31a8-a96b-687de3a45958 | -10.63781 | -44.75107 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0bde6b5-cf60-3cb9-b29a-9969bd579506 | -7.25562 | -44.3301 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30887fa1-bff7-3f3a-9b44-661a155ba12d | -7.25396 | -44.33617 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e80055c-d071-30e0-b608-5d9de0d441bc | -6.56431 | -42.80622 | 2025-08-08 03:42:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e9fbd81c-b078-37df-9791-59ee70c7d713 | -6.96579 | -42.87397 | 2025-08-08 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2983438f-a018-3d9a-be0b-7264fc71f0a2 | -7.32411 | -44.69765 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4776dc39-894b-3de8-9a65-7eefacaed70d | -10.61997 | -44.76302 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97f2c2f0-1275-335d-a60e-a90771812958 | -10.43118 | -44.35979 | 2025-08-08 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98237da8-4c23-3b33-8179-ea3fb23a58f5 | -10.62446 | -44.76702 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 19d3ddd2-c233-3594-b45b-57aee291cc53 | -7.91657 | -45.53312 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01a8b9b9-3633-3159-b590-73aac0fff233 | -8.92845 | -46.73938 | 2025-08-08 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f637e8d-6d91-3ae1-b3c7-c35b364a2af7 | -6.14794 | -44.54331 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20dc5a92-5ede-3f47-a52c-863c2327451e | -10.46034 | -44.39553 | 2025-08-08 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30abf731-ee82-3c0b-92b1-ba63fc9304d4 | -11.54319 | -40.7791 | 2025-08-08 03:42:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| efcc62b7-9eb4-3766-b7f5-8b049e5cb968 | -7.91244 | -45.54678 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a99a3fa-7907-33a5-97d8-bc45f1dc2dfd | -7.90771 | -45.55053 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f01d1455-5096-3ee2-b8a4-0439c630fb40 | -9.65219 | -43.85297 | 2025-08-08 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 256c5d79-f518-3906-8d28-9c770cc379ae | -7.89432 | -45.33908 | 2025-08-08 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1e20b83-7b2f-3e29-a06b-aa041e1f383b | -6.96192 | -42.8681 | 2025-08-08 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| bcdc2cf8-7206-3690-9654-5fa6a205a526 | -6.96635 | -42.87662 | 2025-08-08 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2c160262-fa03-31c3-b631-304c3d3fc2c7 | -8.25048 | -45.06807 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90cddfdd-a091-390b-a51e-68311dede5a5 | -7.38157 | -44.65245 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a82f81b-bf4f-370e-8b73-e1e982e41125 | -8.3721 | -41.83269 | 2025-08-08 03:42:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4e0d7d7-be4f-3526-9db6-361e296d8e86 | -6.12454 | -42.96223 | 2025-08-08 03:42:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 93f2c0e2-000f-311f-a3c0-11973481085a | -8.5192 | -43.30858 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dca0912-5cb2-34be-8a62-a24467592bad | -8.92765 | -46.74364 | 2025-08-08 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6d46a05-a905-3c49-ac9e-ef83d3148341 | -8.97456 | -40.6167 | 2025-08-08 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f06f27b3-bac2-3718-b21e-90ffd19f571f | -6.6518 | -42.0086 | 2025-08-08 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bafd981-4da2-35a3-a8ab-bf18e68be7b6 | -7.10645 | -44.22591 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba2dfa5-4c27-3a0a-a431-6bca82cc40ed | -7.03373 | -42.55891 | 2025-08-08 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dd33988e-2647-3571-8ca7-ed402e6db437 | -10.5296 | -42.55169 | 2025-08-08 03:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d286869a-8352-3ffa-9630-fb53c4f04298 | -11.56701 | -44.85612 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cf3c0b5-ef46-3dab-ae61-1337dfa92229 | -11.02378 | -45.06506 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19393600-913d-3e77-b932-f706fd4bf18e | -11.80127 | -44.92771 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a7fa655-32fb-3891-a9bd-9d942af835b6 | -11.73656 | -45.02518 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d327547-01ee-3b7b-aaf7-db1fe4ab0acc | -12.57409 | -43.7951 | 2025-08-08 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b43a2403-be3d-336e-9f51-eff41c8d6a2d | -11.02323 | -45.06808 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2227f5ee-c0bc-3df3-bc38-86decdae732c | -11.74157 | -45.02631 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16a57283-c28a-3b8c-9dfc-e74fb3f98f90 | -11.73881 | -47.51085 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff2b08e4-c40f-35b2-944b-05d8c7a5fb5e | -11.77333 | -47.51027 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c62a6fe6-363e-33bd-af3f-cebb324e2c8b | -17.57536 | -49.0843 | 2025-08-08 03:45:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a830d0e4-f299-30c3-a6b1-2ef86cc45678 | -15.34928 | -39.44195 | 2025-08-08 03:45:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 80b43960-f53d-39ef-b5ad-ebef3734863b | -11.45672 | -47.31999 | 2025-08-08 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2071275-c321-30f9-a17a-dc9a736dc61e | -12.71958 | -46.37835 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aea869f4-a173-3fed-92df-2da32338bb47 | -18.61821 | -44.2682 | 2025-08-08 03:45:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 780c1d7f-cd14-3d47-bb83-570402478de5 | -11.76255 | -47.50282 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 10628da3-7d1b-3c01-8a1b-ac57e40b0cc1 | -11.74549 | -44.95005 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa1b14ff-64e5-31e3-86a7-3ea9e95dcd53 | -11.02212 | -45.07414 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d25083ba-31ac-3c86-8bcd-2f85526e0b7e | -11.75655 | -47.50217 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c847667-5c25-3cc0-8b97-9ec5d835860a | -17.61654 | -46.71549 | 2025-08-08 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c43829d-1c8c-3912-90bc-bf41b44e6b9f | -12.49424 | -47.50473 | 2025-08-08 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c8acacb-c497-3bb4-ab31-353c3b4824a6 | -17.18921 | -46.92231 | 2025-08-08 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8978cfb-cec4-39eb-af7f-77aea15116d2 | -11.79517 | -44.93375 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dbee2f0f-f299-34ce-bfb1-933b6e210324 | -11.45855 | -47.32012 | 2025-08-08 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 086bf686-ac1d-3202-a5e2-50a78f8302fe | -18.48099 | -41.05221 | 2025-08-08 03:45:00 | NOAA-20 | NOVA BELÉM | MINAS GERAIS | Brasil | 3144672 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b682310-8035-3d63-b26f-9a373496f2ab | -14.73746 | -46.30671 | 2025-08-08 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ccb4a53-07f0-350d-becb-06e13a8f3e43 | -17.85999 | -42.30833 | 2025-08-08 03:45:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a44c498d-965f-37ac-a9e5-02a1234bf4f1 | -11.80071 | -44.93063 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c77d3ee0-0c39-31b7-a62e-adacd022d373 | -12.09734 | -44.72813 | 2025-08-08 03:45:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba2cb51c-9cec-381a-b013-25383099a0b7 | -15.3469 | -46.0782 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b34275c-0786-33ae-a75c-217902d01c4c | -11.74576 | -47.50667 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f52bb266-7e39-3aea-ab02-5d2b44f799ed | -11.77403 | -44.96391 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7767eeeb-b65b-3b97-8818-6395378fdd22 | -11.74963 | -47.50605 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c0df725-5fb4-3144-a899-8187996fdbaf | -11.78319 | -47.52234 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a8ad85f-9260-352b-a98e-f8438b06afc8 | -17.61718 | -46.71233 | 2025-08-08 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 782b31df-eda9-30dd-94df-5d50c582134e | -11.02592 | -45.06599 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 50e3d8d2-f7ab-3f15-9009-d8602bbb0d6e | -11.74358 | -47.50567 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 820676b6-c8be-36e5-9010-4641e2ff57af | -12.61663 | -48.11515 | 2025-08-08 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92c90834-7935-3f07-8517-369ca9475100 | -11.74264 | -47.51032 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b08c685d-e806-3a3e-bf6b-523491936a1e | -12.40339 | -47.78386 | 2025-08-08 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8125bc78-b39f-3b7c-ab49-219546ae11b6 | -17.6115 | -46.7144 | 2025-08-08 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16bc263c-07bb-3569-87c4-be40a19be5ba | -10.82786 | -49.38305 | 2025-08-08 03:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f8f93c9-ddeb-37fc-8255-fff082d65af5 | -11.73486 | -45.00653 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af482cd7-0ae1-3c59-a3a7-0558bc21802b | -11.74484 | -47.51138 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 906fc22b-ec99-3fde-a31c-87cad01be3df | -15.4371 | -39.1236 | 2025-08-08 03:45:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| de7d4de3-b04d-3eb0-8190-28605ce065b6 | -11.75869 | -47.50312 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96eeda04-b45f-390b-809f-3ab1d54c026d | -12.71419 | -46.3772 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faf5d92c-841e-3db3-9608-83046b072bf6 | -12.71613 | -46.37532 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 684088f6-8fc1-386a-b5c4-061ff5fb1c75 | -12.40933 | -47.78506 | 2025-08-08 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb28ab5e-4259-3644-adce-55e5a520c2e8 | -11.02267 | -45.07111 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cde7a419-ab23-3956-b31e-a7c4fc910f98 | -17.34048 | -39.58886 | 2025-08-08 03:45:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 69582d87-7d0a-339f-960a-d06d6eccd0ce | -16.8848 | -42.06536 | 2025-08-08 03:45:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 63b4188e-ee50-3c92-aa3a-72731d7da600 | -12.46523 | -43.56402 | 2025-08-08 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7805840-7a0c-398f-863f-0a31d6e77003 | -15.6874 | -43.20824 | 2025-08-08 03:45:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4c527e6-3ba0-3434-bbd1-8ff400310823 | -17.68297 | -42.41002 | 2025-08-08 03:45:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3c2b7db-2b59-331d-b5d2-4190b77cfc94 | -15.34629 | -46.0813 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a017d0d2-1b2a-3403-a290-f7c1f6e22f8e | -14.73811 | -46.30345 | 2025-08-08 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2ca36c2-c92a-3b84-a211-38435d1dafc4 | -12.72026 | -46.37483 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e7c614a-0e6a-3112-b52c-bc579785f88e | -12.09137 | -44.73284 | 2025-08-08 03:45:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 45e75c1f-fde3-327f-b8c6-1fe3090b9019 | -16.72544 | -49.13082 | 2025-08-08 03:45:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8f8a2e7c-f5be-388c-8a08-5b412426c6e9 | -11.02835 | -45.06904 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2e5b596-2b13-3481-8a8d-12d19636cfb0 | -16.71953 | -49.12934 | 2025-08-08 03:45:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ad074b0-75b1-3bb2-9a87-f0822562734c | -17.68684 | -42.41061 | 2025-08-08 03:45:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8558d1d1-b3d7-3768-a2da-b08f9db1b49b | -12.89458 | -43.77558 | 2025-08-08 03:45:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b97b7a9e-9e9e-3964-8b43-aa23f3198fa6 | -14.48644 | -42.17972 | 2025-08-08 03:45:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c2299aae-39f4-3082-a776-32ca688309d8 | -17.2256 | -39.28491 | 2025-08-08 03:45:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d0587e0a-91a2-3f93-bbf0-56a85a5bd69e | -16.70651 | -39.62006 | 2025-08-08 03:45:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 773ec36b-ac69-3056-87d3-7ca4f8cfec6e | -13.29489 | -40.36092 | 2025-08-08 03:45:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e24cc427-fc85-3433-b197-9ece7b334f61 | -18.8421 | -39.99612 | 2025-08-08 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
