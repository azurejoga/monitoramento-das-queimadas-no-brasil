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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9675970d-3733-3abe-980b-192658a3a500 | -6.53149 | -44.42222 | 2024-10-16 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c4ca0289-2523-3d1a-92d0-07c43c248658 | -6.53094 | -44.42531 | 2024-10-16 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ef2f946c-d8a9-3bb0-851b-fbab380f4d8f | -6.52025 | -45.64752 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b9baf65-afdb-3064-ad9b-b73b3d5d4b98 | -6.44686 | -45.85638 | 2024-10-16 03:45:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fcdd646-0863-3f06-bee2-af8276f9af61 | -6.44614 | -45.86042 | 2024-10-16 03:45:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb685954-2926-3d2b-8e13-13ab28822acd | -6.25353 | -45.87017 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0716d1b3-aca4-3c81-bc71-143d01668b07 | -6.25279 | -45.87438 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8372198-17c0-3a6f-8273-f87c7e914bea | -6.2523 | -45.86861 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85e913da-830a-389e-8e6b-eede66dfca53 | -6.25152 | -45.87286 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f865e876-7fdb-3f1e-ad5c-98524349ef98 | -6.24764 | -45.86916 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a320cdaa-cc38-3a42-b2fb-3dda67046b0c | -6.2469 | -45.87341 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 854abaa0-8596-3a03-bf94-50787a9fb600 | -6.24641 | -45.86765 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13b4e499-bd62-32ee-b823-c419513f66d2 | -6.24563 | -45.87188 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f87a7790-7ca3-3a88-9003-c1cdc8a5c83d | -6.24485 | -45.87612 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84674570-06ee-3769-9f20-f59db6d25e32 | -6.22915 | -45.89544 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d10248d1-330c-304a-9926-3c6a9112b465 | -6.22473 | -45.89578 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b3cfafb-8643-39f6-b656-a62e6b6327cd | -6.20199 | -45.58654 | 2024-10-16 03:45:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e50dc29f-b72a-3597-9019-e934bbd46c82 | -6.20185 | -45.58516 | 2024-10-16 03:45:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57c86f6e-a635-39de-b99f-762de4b2b645 | -6.20128 | -45.59047 | 2024-10-16 03:45:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29ad0acf-4040-31bf-ab8d-8cfb9879a9df | -6.20115 | -45.58913 | 2024-10-16 03:45:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2fab375-5219-3f63-9805-ad066abec8e7 | -6.19988 | -45.59817 | 2024-10-16 03:45:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9fa69b3e-96f8-3084-a834-dc3b02d4eccd | -6.19916 | -45.60211 | 2024-10-16 03:45:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c74bbad9-c79d-33cf-a7dd-47b707759f60 | -6.19912 | -45.60078 | 2024-10-16 03:45:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fd9a68b0-86ec-31ec-b3c0-b562464b8c85 | -6.09431 | -46.09447 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9238a41c-e6ac-377d-9657-73ee53fb15c8 | -6.09077 | -46.09475 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ef15501-495a-34f3-a03d-e03d8c2bd164 | -6.08832 | -46.09343 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42c2faf1-5fdf-33e7-99a9-34ed792220f7 | -6.08476 | -46.09385 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a66fd89-14e5-36cd-a384-6c52fb56728d | -5.98901 | -45.73816 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be47cda2-fca1-3cd4-aa7f-f08a497af730 | -5.98823 | -45.74253 | 2024-10-16 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 312d07c3-79b7-3919-a552-384c1548ec36 | -7.60566 | -46.8012 | 2024-10-16 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b1e805b-492f-35d8-a325-7bf0d8293522 | -7.60506 | -46.80106 | 2024-10-16 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55a33100-f11b-3fad-aaf4-c7737660e5cb | -7.60465 | -46.84009 | 2024-10-16 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 648018f2-4890-3ef9-89b4-9407650b0720 | -7.20456 | -46.26204 | 2024-10-16 03:45:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fd574fa-a464-37ae-b14e-737062e1ad28 | -7.09798 | -46.77347 | 2024-10-16 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71c74fb6-14a0-399c-9691-289f08c9cc1d | -7.09711 | -46.77818 | 2024-10-16 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6a6f0b5-7af4-3c1c-8d5c-9a71eb0b668d | -9.17026 | -46.97655 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a59005c-0376-32a3-adeb-c3bfcd8a58ae | -9.16837 | -46.9754 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95ade05e-d2b8-36d7-934a-d6d17d130efc | -9.16669 | -46.9949 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be9cf9d0-ed36-34c5-8bd6-e259c3b59461 | -9.16577 | -46.98933 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8eb05843-609a-325b-8fa0-8ac9ed3e0666 | -9.16492 | -46.99386 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6c9dc44a-3dc2-34fb-8973-de58f29b3384 | -9.16425 | -46.97544 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 422fc432-8a3a-3ccc-8ff8-254d57356a97 | -9.16406 | -46.99843 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 098b9dbf-0a60-3b37-b88d-824b6803ee38 | -9.16334 | -46.98011 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b8b617fb-fc17-34a7-99f8-ed6edbdd3766 | -9.16243 | -46.98479 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6945748c-4278-316f-bf21-89319d06f4de | -9.16236 | -46.97429 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ffbe78a7-1717-3f06-aa52-cbb2d7790683 | -9.16153 | -46.9894 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b59d62f0-d5a1-34dc-aa73-2edeb49ef0e8 | -9.16149 | -46.97896 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc5a6f08-8b38-3fa5-bed6-23c3171d1a49 | -9.16065 | -46.99392 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76c1766e-3342-3dd3-be67-b9566b7ebaa0 | -9.16061 | -46.98364 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0137aa20-726a-3bdc-8c3e-d61ce4db9a27 | -9.15974 | -46.98827 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e869a16c-9811-31a5-af80-a92f051c2705 | -9.15889 | -46.99283 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0dfe421f-e53e-352c-8174-094c5f534016 | -9.15822 | -46.97444 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 832faf09-d5a2-3010-83c3-8ac7e8c2c072 | -9.15732 | -46.97905 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3a6c7609-92d1-36ad-a59e-07238e561e29 | -9.15642 | -46.98367 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 96c66b4c-3275-351a-bc2d-37cc485e00f4 | -9.15633 | -46.97333 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7f20416-a45a-3228-9185-641126a013a5 | -9.15553 | -46.98825 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f8a13ff-a952-39b0-aa06-93c2012b321c | -9.15547 | -46.97791 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 50a6a75f-be72-372b-bf9b-96d775bbc1ef | -9.1546 | -46.98251 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a97908bb-d45a-360d-9e5f-9ce01b64c797 | -9.15374 | -46.98709 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03a8b702-e66c-32c9-b3f4-4e45e88a2cd5 | -9.15131 | -46.97798 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e13c7f40-2554-3636-990c-4e54a69dcca9 | -9.15042 | -46.98254 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d942ae06-d314-3e09-9aed-f394236e6045 | -9.14946 | -46.97679 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 261b9caf-9316-3d92-82c6-53ce330d976b | -9.1486 | -46.98137 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b719cfb-0f42-394b-b1c9-8c7b900091bd | -9.11938 | -47.00416 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5973dd9d-c319-368c-a6e2-7b63d3a2f5f0 | -9.1185 | -47.00878 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b965471d-4b87-3089-9aab-7541aab31043 | -9.11763 | -47.01335 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7ba8d0b-b07e-30d1-a574-d05f1f75d291 | -9.11513 | -46.99373 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f200d1d-0e56-3233-b83f-d5a0970a14f5 | -9.11426 | -46.99834 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ed18ffb-82c3-3107-94b0-aa318ab180be | -9.1125 | -47.00759 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e901171-cabc-350a-b9ba-2d1143f57700 | -9.11164 | -47.0121 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69991aab-b4b3-3566-bf80-b6884dd930a8 | -9.10913 | -46.99256 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7066d696-de08-364b-bcb7-e4e1ab8e1017 | -9.10902 | -47.02585 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 148e6a79-4905-3f4d-9df1-0616f49aeced | -9.10825 | -46.99713 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 58c350d2-68b7-3f99-bdf8-a72431a99c77 | -9.10815 | -47.03041 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf0e5698-b14c-3fae-be52-2690e8398309 | -9.1065 | -47.00635 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 353f556d-de1d-3231-9e2b-4ec7f4e52b50 | -9.10301 | -47.0246 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8279a0dc-4c81-35ca-8c61-50f8a3986c29 | -9.10215 | -47.02914 | 2024-10-16 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fb3bd9a-11ac-3a04-bd6c-ac4910d58a03 | -8.92664 | -47.05488 | 2024-10-16 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e0d35a6-ea12-3189-9a50-78f444c25c9e | -8.92619 | -47.0519 | 2024-10-16 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d114a31a-889d-3a47-8087-d9c0ce7f2305 | -8.92532 | -47.05656 | 2024-10-16 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acd85fde-64b7-30bf-b524-ab7f41c0a443 | -10.25445 | -47.30421 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ef938a6e-e065-3d6c-8dd9-d22b11afdf6b | -10.25107 | -47.28952 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce279329-9728-3f03-80ca-6df7d52147f3 | -10.2502 | -47.29398 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 67c19dfe-43f2-3185-99c9-8c89f07e9afa | -10.24932 | -47.29853 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e33b7ebf-9638-3178-93ab-67cad99a3f4f | -10.24843 | -47.30312 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e5827c1c-d491-3cf2-ab89-a319144eb8af | -10.24679 | -47.27944 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f179ef9-c0d8-3de5-9c03-8a6a31a2e48f | -10.24505 | -47.28839 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c5d3ef9-97d8-3389-8216-5b26f6402673 | -10.2434 | -47.26486 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43f15c9b-3a12-3d09-b060-410e348bdb8c | -10.24253 | -47.26933 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd5e5ec1-8da6-3eb4-99bd-b121da8a6d59 | -10.24165 | -47.27383 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f820421-5b96-33d5-9d14-cd7d460d49a8 | -10.22938 | -47.20937 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37538a50-7631-3cd3-b3a1-354f787801f0 | -10.22849 | -47.21391 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d63a197-658d-378f-9573-4060a9543d91 | -11.64058 | -47.58382 | 2024-10-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26edbd4e-0e63-371f-bcda-50ebde37a362 | -11.6374 | -47.58149 | 2024-10-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb179363-7e91-3113-a8a9-1f791f85af39 | -11.6365 | -47.58591 | 2024-10-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b880a58e-565a-324b-9143-5c75f1d9131e | -11.63462 | -47.58257 | 2024-10-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3bb94d9-53f1-3b83-95f2-b22a404e2c5f | -13.38823 | -46.94671 | 2024-10-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be1ffa4d-f0da-3a81-a4f5-03f7287c8889 | -13.38686 | -46.94607 | 2024-10-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99b9773f-2339-3f0d-85bc-2d0d0e2e5ebd | -13.38612 | -46.94967 | 2024-10-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38197cab-483d-3ffb-b07a-0fa2a4fdd13e | -13.38198 | -46.94908 | 2024-10-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README28.md)
