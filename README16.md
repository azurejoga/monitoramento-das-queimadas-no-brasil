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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd144ac0-255c-3f5a-9ece-547bece11dbe | -12.91726 | -50.56979 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1ec1c93-e58e-3037-abbb-5659d7ea95d4 | -13.56223 | -41.6119 | 2025-09-19 03:55:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d697c887-4094-391a-82dc-c398637d0fee | -10.4859 | -45.15965 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53892e31-00f6-3561-8c29-f477edc35c8f | -17.46255 | -44.78232 | 2025-09-19 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4c8f3b8-2f46-336a-8fbd-c1a9d41abf47 | -10.30709 | -50.22657 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9f930849-6661-3950-aef3-bbc446249a4e | -11.51328 | -40.64334 | 2025-09-19 03:55:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0f4405a8-bcd4-3bbc-9920-72083b0c4fca | -17.09031 | -43.34365 | 2025-09-19 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d008ffb-f187-3f64-be9b-aba1cd0a28c6 | -14.42828 | -47.38167 | 2025-09-19 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9678e6fa-c5d4-3e19-8653-3f9f6fa0c07c | -11.50455 | -43.61362 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 131b3494-5115-3f96-8556-a4c5f7851bde | -11.98884 | -43.37705 | 2025-09-19 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d95f4d54-c9b3-33f8-95e2-eb7aff04cf53 | -10.24798 | -48.04055 | 2025-09-19 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c72f3a2-6156-3fa1-aa97-0c3a10812827 | -14.55337 | -45.52696 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 197c148f-7367-30ec-9c00-0e64061ecb00 | -12.89936 | -50.5414 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 476d6de3-4777-3bac-a128-2be13bdfccca | -17.17764 | -45.90189 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b2d09c0-238e-34f9-be56-a120ad2a5b3d | -10.92135 | -45.65963 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69dc800f-607e-38fa-b3f2-d8b51b2762b2 | -10.48094 | -45.16292 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 190043f6-5d17-3e9d-9cb5-b4901df59e01 | -17.08539 | -43.33014 | 2025-09-19 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96532096-37d8-3c5f-b7a8-0e2f82efa70c | -11.50474 | -43.6158 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ebb3d0f-807b-3a49-8782-e60bd5637a48 | -17.34072 | -46.79874 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7a26f37-1840-3d84-84a0-caa8dc25cdcc | -11.49657 | -43.59473 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15eab13f-8efc-32d3-8f76-661228639371 | -11.1607 | -45.32633 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3629ae4c-ca41-30e1-9592-54aae1bd86ae | -10.91778 | -45.65451 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddc5c5ec-ce3f-3e11-b711-f2b5eba69c74 | -12.91148 | -50.56854 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61d0a599-44ac-3cb8-8baa-509555675857 | -10.91679 | -45.65539 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e5f4799-8b2e-38ba-8402-3aa4a977992d | -11.33701 | -43.48235 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a718d2e9-3913-326a-9cc9-868c00060d6d | -12.87952 | -50.55025 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a10d2484-2d20-3646-9e04-f7962991e24c | -17.2234 | -45.95476 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 05233f99-76ae-33b0-980b-cefba2332cb0 | -10.32274 | -45.25214 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13d82f2b-1bd7-3cc9-936d-c0db660941f7 | -10.91754 | -45.65115 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e3104b7-154d-3f32-a360-676bcdd57b14 | -11.41616 | -41.41289 | 2025-09-19 03:55:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 006fa306-012b-3633-86af-9bc145eb92ca | -10.87718 | -47.80936 | 2025-09-19 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46e34cf5-a478-310f-ab9b-938fac284615 | -12.08964 | -44.84488 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9226550d-b65b-38e2-87b6-684969fd2885 | -17.35048 | -46.81638 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef031b45-3100-30e8-8a80-6bf7fabbf08d | -10.87255 | -47.77872 | 2025-09-19 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb94f196-1c72-3e5b-84ea-e983d2f98d97 | -15.431 | -45.44752 | 2025-09-19 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06a2c762-ad6d-342a-bc68-dca5c67eb997 | -10.29074 | -50.23146 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e2a92f0d-70ba-3d42-83f3-f8b311a7f9ee | -10.48519 | -45.16365 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60c1c5fd-160f-3c49-b0d6-89d7aa54515c | -10.66461 | -46.44496 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a9e2181-1d47-3f33-b1fd-b1e38adc5f77 | -12.1489 | -44.95834 | 2025-09-19 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bb8ffb2-8b88-37e3-87cc-4403ae2f676b | -14.58004 | -45.16621 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 606f6ae4-c547-3e55-af0c-7a900a87084d | -17.08819 | -43.33487 | 2025-09-19 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef37a90c-3ad1-34c4-a1b9-d26d6325aa02 | -12.09893 | -44.816 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb4c14a6-b1cf-3b66-b7e9-9dcdee61edd6 | -11.33027 | -43.47638 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0891727-9c5d-3089-b1e8-126a684428da | -11.1848 | -45.36385 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31e809e3-e6d5-3f51-8720-f50574820941 | -17.16521 | -44.78986 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9c8a281-427f-332b-8b26-2ee437126101 | -11.16 | -45.33029 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e871db9c-bdcd-3816-a214-3e185158eabc | -9.76275 | -48.58213 | 2025-09-19 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c65f27-a2d4-3528-9d63-3784eced06e0 | -10.93138 | -42.85068 | 2025-09-19 03:55:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b82213d-451f-39f3-a3e0-756eb70dc8fb | -10.6642 | -46.44091 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6174cc78-1090-3cce-a92e-0f6244b19d3a | -10.92009 | -45.64188 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cffcfd3-1c30-36f0-85a7-128d241d29c4 | -12.09302 | -44.84938 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc10642b-a32d-3a0b-9ca4-443a372eeb15 | -12.69783 | -44.97735 | 2025-09-19 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c718659f-d4e1-3a13-8fc9-91672562c730 | -11.50373 | -43.61832 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ada685c-5246-323a-b795-12352792fc4a | -14.12905 | -44.59108 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b55cc3d2-f8c4-3c3b-b686-a347f571bb9f | -15.3282 | -42.056 | 2025-09-19 03:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5de4a260-2bde-3887-9d44-e1b15cd057c3 | -12.11773 | -44.80387 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e8d510a-2911-31cd-a5a0-3644cd296804 | -13.16536 | -44.59665 | 2025-09-19 03:55:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 945cb24b-f016-375f-8d8c-8f54d4e0428e | -12.09486 | -44.8154 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4ad9408-3a16-33e7-9d6c-b921fa25be6d | -17.22671 | -45.95923 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9e7e83b-41b3-36e7-a343-98e54e6db2be | -12.08824 | -44.8292 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05e2c896-1a4b-3d78-ad9c-87fc76cdeefd | -10.68754 | -46.46942 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 195bee48-591a-35ce-8aae-a7e33bb1a75f | -16.51856 | -43.55025 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2668309c-0453-3864-82dc-fc3e99023fd7 | -10.69215 | -46.47031 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83f912b7-2568-3a3d-8a0f-f70dd1134bd5 | -10.29928 | -50.21942 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 51678528-f025-3309-9ecc-1658dbff44c3 | -14.25026 | -44.3852 | 2025-09-19 03:55:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28ef8711-3705-326e-b0bc-bf6c15589159 | -10.73044 | -48.46825 | 2025-09-19 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e8af714-a72f-3d86-ba23-2b118e4d1e67 | -10.2434 | -48.03639 | 2025-09-19 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff32a469-8012-3c26-939c-c62164acefb7 | -15.76332 | -49.9504 | 2025-09-19 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b3354d4-d815-3cf6-b28e-5ee1ca148ba0 | -12.61819 | -45.07312 | 2025-09-19 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79173f33-bc72-3ee1-b93f-2135a6a60d0a | -13.57883 | -40.92322 | 2025-09-19 03:55:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 69e1a050-55c8-35c5-bd72-46437f535007 | -10.30607 | -50.21621 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cd8de016-102a-3797-9419-5b3d2d0cdbcd | -16.51383 | -43.55263 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dc00a3e0-2535-39a2-9f63-71a7312a192c | -14.47834 | -40.69437 | 2025-09-19 03:55:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f83e7e13-4276-3ecd-b8fb-97e02b9fc4da | -14.58307 | -45.17228 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c42f9c3-d7f1-3540-bd32-1b80d634bd27 | -17.1988 | -45.95362 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e517107d-9b04-30ac-b0f1-a6f9a1ecc1ff | -14.61236 | -41.04453 | 2025-09-19 03:55:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8f7afb0-0ed2-35c5-8a9f-21a87f13cb0a | -12.92491 | -50.56445 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c118d2b6-e85c-3dd1-8d75-10d359864fff | -17.22738 | -45.9556 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 403dd236-62c3-3404-9928-2bd5113e4d95 | -11.1855 | -45.3598 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57f58d00-a1a0-3f35-9021-5731366efac1 | -16.61151 | -43.36568 | 2025-09-19 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d286819a-63c9-3f48-b01b-5c0d8f1c7423 | -11.93448 | -38.3316 | 2025-09-19 03:55:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 38185fb0-bd41-30e5-a2c1-e2a894acf73c | -11.16704 | -45.36504 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a6a7aa7-05a6-3efe-8f92-2f3f8205a3bd | -14.69288 | -43.98251 | 2025-09-19 03:55:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7b925ab1-3094-3cda-9759-f56481535ca6 | -12.09368 | -44.84564 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e14ce447-15d4-358b-bc2e-f4707a5fea8e | -11.16278 | -45.36433 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84b75eb1-6a6c-3d93-b39f-c7219accf136 | -14.26302 | -44.70268 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1c87cdca-cb0c-308d-b9d8-1e463cc83886 | -10.04392 | -49.2042 | 2025-09-19 03:55:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15bae56f-f980-3e37-8426-db22e765f766 | -16.51572 | -43.54542 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 61c7468f-99e4-3069-85bb-49bf1fc34870 | -17.06156 | -45.96518 | 2025-09-19 03:55:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1edc6fb6-293b-37ca-adcb-7191430a824a | -17.56654 | -42.40022 | 2025-09-19 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c096ca0-d487-3dd4-8c41-7109b80f7b3c | -10.30116 | -50.22535 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 43bcb583-d90f-3812-914f-ca9e47e41a9c | -16.36811 | -42.30527 | 2025-09-19 03:55:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0d1f016b-ac70-3fe8-aa60-6d3296566aa7 | -10.91828 | -45.64691 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c239d732-3c17-3624-8dcd-2f21885c2786 | -14.49552 | -47.35273 | 2025-09-19 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b25a379-7219-3749-9e3c-2ff6ce3127b1 | -12.32367 | -43.43903 | 2025-09-19 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 419bfd44-e198-3d83-a644-bdb9e3485a1f | -13.12326 | -41.0517 | 2025-09-19 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 66642070-0be1-3752-a2fd-3d6da2636519 | -10.30033 | -50.22977 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4d395b80-9f7b-3e19-b4b8-a7a07d75cbe6 | -14.25406 | -44.38593 | 2025-09-19 03:55:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4b4bfe5-8f8e-319a-bff9-0f1b52884449 | -12.10585 | -44.84774 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f16fad7-898c-36bf-b41c-34974f88ef29 | -17.21414 | -45.96015 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
