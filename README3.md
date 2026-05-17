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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226980bf-eac7-392f-8394-948c156ca38e | -20.99705 | -48.6856 | 2026-05-17 04:02:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ed7c6aa9-b7b5-3f85-b1bd-2166bb04df4c | -19.18886 | -49.12302 | 2026-05-17 04:02:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bfa8968-8e39-3164-8fa0-e42253f022c8 | -19.19356 | -49.12414 | 2026-05-17 04:02:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 383870dd-7681-363b-91c6-7b20fe721902 | -19.18944 | -49.12331 | 2026-05-17 04:02:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b430dfc9-e61b-3625-97de-0ddf76b30191 | -21.00145 | -48.68675 | 2026-05-17 04:02:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 30c76a37-ced3-3d04-9ea6-2bedc4d4ca95 | -28.82066 | -49.25212 | 2026-05-17 04:04:00 | NOAA-20 | BALNEÁRIO RINCÃO | SANTA CATARINA | Brasil | 4220000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8424217e-8f07-3eb8-97c9-050d27e122c2 | -7.37539 | -46.04731 | 2026-05-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70a28685-1aba-3388-9af0-a534e2d0c6dc | -7.71798 | -44.56053 | 2026-05-17 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85ca081d-cf5b-3dbd-a0db-8669f7e2fc48 | -9.45483 | -46.10567 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1191b8e5-cf9e-390a-809b-fceac52aff02 | -9.46567 | -46.11868 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 447b81fb-3e3e-3fdd-9b6c-168895f73b52 | -7.38237 | -46.2248 | 2026-05-17 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c4f6417-c8b3-30ae-9621-a332b8b2d037 | -9.45846 | -46.10994 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 469619a6-929e-34fb-be93-0105cd0a5361 | -10.4066 | -44.93754 | 2026-05-17 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c55f45d2-0d81-3d56-97cc-82c7ad23d108 | -9.47262 | -46.11483 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b92b3647-3cc2-3492-b3b7-27b5eea8e208 | -9.22764 | -46.65154 | 2026-05-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7358decb-9331-3328-84a7-4d4b54970f43 | -6.66476 | -47.5552 | 2026-05-17 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9537520-de19-3a87-8906-829570b143da | -8.47633 | -46.41027 | 2026-05-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d413d1b-3de6-3308-b835-847a12c1e5c5 | -8.45831 | -46.42223 | 2026-05-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00f77113-4be3-34fc-a340-1861211e630a | -8.10393 | -43.15808 | 2026-05-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| d92cabbf-1119-3aec-9c5a-5fb0785ef6e7 | -9.44439 | -46.11961 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30701e38-fa09-39ba-a34e-5bd29118fab4 | -9.44962 | -46.11259 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b05f2f0f-14a8-3cd0-878d-d0bcfe96c80b | -8.8577 | -50.20909 | 2026-05-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9da4487-446a-3a37-925b-c28965404d71 | -10.39976 | -49.44218 | 2026-05-17 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bba84d60-b448-389d-8394-052333a04d58 | -9.4543 | -46.10941 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24a6e63d-9daa-35a4-beeb-08464e3b2be2 | -9.45016 | -46.10881 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24266cc0-707e-34e2-b24b-a65fd464c515 | -9.47211 | -46.1186 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15f5ecbd-2b74-3415-bb55-daeb0fc44256 | -9.23163 | -46.65212 | 2026-05-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc2aad41-d50c-35f0-8186-de804d6a9263 | -8.85715 | -50.21268 | 2026-05-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a65f2aac-cd5c-3d7b-8c05-918bbbb197d3 | -9.46744 | -46.12184 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29bbe8c1-6727-30f3-8d03-71a386b4e4b9 | -9.4709 | -46.11167 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed13496c-3dcf-34a2-9cc9-47d761b35eb4 | -9.46621 | -46.11487 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd8ca8fd-cd9b-318a-8d5b-3a2d81cdb679 | -6.66443 | -47.55783 | 2026-05-17 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ffa5a53-c30f-3019-a32e-af1f316b4183 | -9.44493 | -46.1158 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdb108f2-4a8c-33f2-bd3e-3e20c343c36f | -8.7253 | -48.32497 | 2026-05-17 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a061e9b-96a4-35ab-8d32-413b52abfab2 | -8.8605 | -50.2132 | 2026-05-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d25162eb-0d56-3183-8664-5b5ff1193a0f | -9.79231 | -48.08075 | 2026-05-17 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e01ed5a7-b6a3-3b38-8ea8-457e7dbaa6be | -9.46847 | -46.11421 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7710f4fc-ec65-396c-b47b-e2e5cff54767 | -9.46796 | -46.11801 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 805e760e-0898-3616-b48e-6aea0af8438a | -9.44386 | -46.12341 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c25992da-894e-3a6b-9b55-10657d898ad7 | -9.78862 | -48.08021 | 2026-05-17 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1fd02dd-b6ef-3ecc-ba32-38b0b8f937d8 | -9.46432 | -46.11362 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 794848be-8336-376a-9329-c98eac3b39d5 | -9.47036 | -46.11544 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31ab05ec-a7db-36ba-8b37-9e4c21513c49 | -6.29769 | -43.63658 | 2026-05-17 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97591481-faa3-342d-8865-fc0e35efb14c | -9.46982 | -46.11922 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70d8ad91-3094-3733-bb9d-7a3a67fc0ece | -10.97947 | -45.09239 | 2026-05-17 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49da4d72-7500-3952-b8c1-b2dbe63d6ae0 | -8.09475 | -43.15095 | 2026-05-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f269f15-26be-37f9-94a2-2948eee7acf9 | -8.05387 | -46.45412 | 2026-05-17 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31aad6ba-ea94-34df-b2a1-f4f8ae5558e9 | -9.44548 | -46.11198 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b08b0d1-d8e9-31a2-bafe-39ba4822d986 | -9.459 | -46.10615 | 2026-05-17 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e44ac733-7433-34fe-a06f-a738ddab0576 | -9.23562 | -46.65269 | 2026-05-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9aba6d2-ddac-3a1a-97a9-df90fd9553c2 | -6.29839 | -43.63158 | 2026-05-17 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d98a1a2c-bf21-3f90-bc77-e3ac00484483 | -13.31417 | -47.51595 | 2026-05-17 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e192b018-0f48-3aca-884c-8124dc282ec5 | -11.43536 | -55.10467 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8428d66-cb06-3f56-b5cc-11103e1f6da2 | -12.91337 | -45.282 | 2026-05-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f82546d8-e8d4-3225-940b-279411085e4b | -11.04913 | -49.59996 | 2026-05-17 04:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8026b390-2a76-3788-b189-5cf21c144e56 | -11.4617 | -55.11625 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0366f557-ce8e-3753-a9f8-bab108341226 | -11.88429 | -43.80746 | 2026-05-17 04:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5e95b4eb-30ee-3e7f-9791-eef679afd988 | -11.8789 | -43.80968 | 2026-05-17 04:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c769919-a83c-33b5-a371-f9c10566f963 | -11.61458 | -47.09736 | 2026-05-17 04:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e39ce888-07d5-3a61-a0a5-504965d7d77b | -11.12574 | -53.9477 | 2026-05-17 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4ecd41d-8f20-397a-bbd5-55654b139903 | -10.70221 | -52.49919 | 2026-05-17 04:49:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c300de89-1da8-3072-a9c1-d772b16f4205 | -11.61057 | -47.09678 | 2026-05-17 04:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37946d78-fa17-3721-94de-04e129006ece | -11.46527 | -55.11685 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb305f99-1ca7-398d-aa97-eae128b286aa | -11.87927 | -43.80676 | 2026-05-17 04:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08a342e1-497d-3107-8d0e-2b0b0df69b44 | -12.04351 | -45.28577 | 2026-05-17 04:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4ea23d8-6062-3454-b2af-02914a6b9878 | -12.44733 | -44.7497 | 2026-05-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b646e1bf-c4f0-3afd-ad58-cedd092d6883 | -11.44301 | -54.0924 | 2026-05-17 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab67a224-45b7-3981-b661-8fdc1ede1b58 | -12.45057 | -49.58618 | 2026-05-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eaa66dd-048e-395a-9044-22c1465754e4 | -11.02699 | -48.92937 | 2026-05-17 04:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa93d00-bf09-3678-8d47-a6c0e33b74f5 | -10.91079 | -54.12311 | 2026-05-17 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae9a4419-c328-3f3c-9cdc-09287ab228bf | -12.26938 | -43.50554 | 2026-05-17 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c1b6b922-0197-36f9-9026-a7be0e2095e5 | -11.87387 | -48.99321 | 2026-05-17 04:49:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9d3daac-8ea2-3e72-a0c6-30a4b1200538 | -13.31459 | -47.51288 | 2026-05-17 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d10330f4-42e2-3f1f-9599-f9d889e8f577 | -12.4477 | -54.48074 | 2026-05-17 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41f86471-7a1b-3ee0-9d32-a6ae77fdf1d2 | -11.43616 | -54.09127 | 2026-05-17 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c600976-68e4-3901-8628-b490b77151ae | -12.37506 | -54.45298 | 2026-05-17 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52cf9bf5-62d6-392a-a188-2602eaad00ea | -11.45254 | -55.11179 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a16cb5f4-eb60-3a14-b4a7-32215269db5d | -12.26898 | -43.50868 | 2026-05-17 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 640ae236-f783-380c-aa4d-2e5db1f98ec5 | -11.45186 | -55.11594 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba1a7a9-5846-3638-977c-be6eb51da448 | -11.45968 | -55.113 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c43d1f30-2a92-38d2-ad62-646433d85fcf | -10.91142 | -54.11929 | 2026-05-17 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60b6396d-8964-3261-bb57-4fb7dafee898 | -12.91388 | -45.28101 | 2026-05-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35218603-99ee-3554-9cb0-f88e3db2e51d | -11.74826 | -54.79589 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5563f23b-9646-3058-a242-db2d497e9c4a | -11.61409 | -47.10095 | 2026-05-17 04:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b20688b-702e-3cff-826f-ed7c88d938ab | -10.91423 | -54.12369 | 2026-05-17 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b77fd51e-4ae4-3cb6-a1c7-330aca102652 | -11.46099 | -55.12038 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1253202b-3071-36db-89e4-7d451283b353 | -11.47905 | -52.92299 | 2026-05-17 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e4ea654-0e79-3735-9ba0-8e08eb53d630 | -11.75243 | -54.79251 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e94a219c-ef06-3d3a-9afb-994b1b0b2e59 | -11.45543 | -55.11654 | 2026-05-17 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1be3e2c-4630-37ea-8ca2-95133f6ef55f | -11.03057 | -48.92994 | 2026-05-17 04:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d79486f5-47a5-32a4-848f-0285cd5b9de6 | -12.26422 | -43.5049 | 2026-05-17 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 384bff77-febc-3dac-b6e0-895f4543bbc1 | -12.3785 | -54.45355 | 2026-05-17 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b145ad6-4a0c-3a5d-a3e4-6900877b6758 | -10.9183 | -54.12043 | 2026-05-17 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b582246a-ee15-3bba-b633-cfa244cc45dd | -12.28332 | -54.08837 | 2026-05-17 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 989fd396-861e-372f-be86-9d45270110dd | -11.12635 | -53.94396 | 2026-05-17 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8af8d47-c7c3-34cb-84f6-ccf656716fc9 | -11.87278 | -57.00991 | 2026-05-17 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60eff7b2-cf2f-36d0-bc28-77fcb140d509 | -13.40127 | -46.60014 | 2026-05-17 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 073b2457-1cf8-3ee3-9f39-6353626f3950 | -11.48017 | -52.91589 | 2026-05-17 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e70f661-68f6-3bd1-955f-78115b06bf59 | -13.40023 | -46.60818 | 2026-05-17 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee1649b4-9dcd-320f-ba66-36e3757234ee | -11.48294 | -52.91998 | 2026-05-17 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
