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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30b68fb9-d7db-3f6c-936b-58f60d6248a4 | -7.29572 | -44.08698 | 2026-08-26 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be6c4232-f688-3a88-8565-4b26cd968cb0 | -8.14186 | -47.5101 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6541eaa1-00e7-378f-af76-647ed038aa7f | -8.08658 | -47.49928 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7725edce-55c9-3b31-b7a2-1a47eb3e034f | -8.06623 | -47.52939 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d8e6d28-5433-3cd2-87ff-b3479ac27788 | -7.75338 | -44.74994 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 09ac71fa-c381-32b1-9ba0-b880f4192e51 | -7.31643 | -42.9839 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 901be32b-14ce-3f3b-a36c-645c60a3fd5d | -9.37598 | -40.51494 | 2026-08-26 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e611f72a-653f-3181-8ea4-e1107009ce47 | -5.31286 | -37.33333 | 2026-08-26 03:47:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16429798-71e7-33bf-9dd2-78b102b6fde7 | -10.37527 | -45.0685 | 2026-08-26 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 0f94d558-beca-3bd4-bd46-9314fa8c2d22 | -7.75688 | -44.76426 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83bcf5df-58bd-3de2-9252-6c95fb74b78e | -9.39704 | -45.506 | 2026-08-26 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0f8ac92-eef8-3da7-99c1-aaa2de04dcfb | -12.68083 | -48.40604 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38746bc8-7132-3402-b0bb-626dd4d81205 | -11.01401 | -45.06894 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fa3d27e5-6ef9-3a71-99ed-9d28f02277ef | -12.02872 | -46.02955 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2598d99-ddc9-32b8-93ea-241121aa6ab6 | -11.41925 | -44.54848 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26730723-fb13-3de4-9b91-340ae5d70654 | -11.80918 | -47.67022 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5111977f-7fee-38fa-89b0-882cb7ec67f8 | -12.02539 | -46.01509 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cda4052e-6bfc-3d1d-b37d-e7097dcad077 | -4.85189 | -44.3049 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d090f98b-6b05-3307-95ef-10fb66008b6d | -5.92348 | -43.64322 | 2026-08-26 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 898f4c76-e431-30d4-b2f4-0fb19589574b | -11.80685 | -47.67126 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8499aa61-6261-3356-8182-8ec37379508e | -12.76017 | -46.45578 | 2026-08-26 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b469adaa-2cad-3540-9862-5147a34b4c55 | -13.35095 | -48.23701 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8debb040-6b96-3eab-a5cd-4a63271e72e1 | -7.13994 | -42.77478 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bfdb38d7-4328-3771-a692-f417fafad047 | -12.67121 | -48.41022 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c953c10-cb92-3ae8-a34e-f87d0bb665d1 | -6.91205 | -41.12491 | 2026-08-26 03:49:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a5e18622-14a0-3821-9d78-251be850d610 | -11.81456 | -47.67749 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a335bc2-27e9-339b-9584-108d16cd129c | -12.02711 | -46.00634 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5064b04d-16b0-328c-b707-b414d94aabca | -18.54169 | -42.57684 | 2026-08-26 03:49:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e16357ef-6537-32e5-90dd-cdb9f202cffc | -11.7997 | -47.64948 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3072a83-4a25-3b4a-af47-9d54a3ced492 | -12.70104 | -48.41042 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8234204-99eb-39c4-80d9-a488e1d681a3 | -11.28624 | -47.07465 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10eab435-a967-31ef-b768-f364e13ce323 | -11.25849 | -47.05191 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de30c840-f1b2-3bbf-95a1-5d4cad594ffc | -12.03207 | -46.04398 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fc5ff38d-24cd-3bf3-a115-0011be4247ee | -13.37382 | -48.2138 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46177cc5-ed1c-35d9-8757-63e0743f9151 | -12.75914 | -46.46085 | 2026-08-26 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| baa5be76-b63a-3008-b513-c985220de51c | -13.34455 | -48.20219 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31259662-3fb2-3f18-87a5-4b651338be59 | -11.42676 | -44.53881 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71625014-8968-3720-9c16-e351ebf78e33 | -13.37266 | -48.21914 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93c55a99-9259-3581-8383-9baf2a4bda34 | -5.66018 | -46.95466 | 2026-08-26 03:49:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ed7adf0-bc9f-305e-a068-547a5f15722d | -12.02625 | -46.01071 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0e189c4f-f949-30a3-bee9-aa736fcedc5a | -12.76641 | -44.27018 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b99c0509-6f68-37a7-94d7-34d2faf08b0c | -6.24745 | -44.79825 | 2026-08-26 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 386fa44a-6eba-3829-8cbf-dbf202c02dff | -7.12086 | -42.79089 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5cb9fdd1-695a-399d-a156-c81b24a93c02 | -4.80726 | -45.7733 | 2026-08-26 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d4d668a-4c8e-3ceb-9fe2-3a43ddecce49 | -11.64444 | -47.15973 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc70712e-7e46-3be1-926c-4fb94fc82510 | -15.06505 | -45.32405 | 2026-08-26 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21441f42-c487-3b50-bfe5-c252330ae36f | -11.79872 | -47.64473 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d57cbb54-cddc-3f30-a24b-47b41e3c305c | -14.79614 | -48.79438 | 2026-08-26 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a397b638-5200-3cc5-a1b6-cd580b43eaba | -6.3199 | -44.84808 | 2026-08-26 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06e45ce7-6104-3978-acd4-be04f3df1e72 | -13.33699 | -48.20533 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bce88fa2-957b-3420-b2fd-104c5e9f99c0 | -6.91439 | -41.11655 | 2026-08-26 03:49:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3ca71a1e-57c6-3e19-9dc2-ad6b8b7f2745 | -10.9843 | -43.71313 | 2026-08-26 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5668d5f5-ead7-3ee9-b43a-8935c87c4bca | -5.33589 | -45.16151 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b8f6cea-d188-36bd-bd49-6a532ff57e3d | -12.69288 | -48.4155 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14952df3-e061-33f5-b423-ed23ae9cb07d | -12.72882 | -48.37962 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13bbf62c-fcfe-3e10-94bc-85c397949c37 | -17.16145 | -39.30062 | 2026-08-26 03:49:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a5a7710e-5eec-399c-a3ac-449ddc48053d | -6.1266 | -44.06818 | 2026-08-26 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f73b3ec-f762-3de2-bc93-66f74319cdea | -12.80738 | -42.73244 | 2026-08-26 03:49:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a815e2c9-b924-35d5-ab3d-eb1ccdb082b2 | -12.02926 | -46.03807 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7bfb240-9a97-3114-8cbc-8ded9e1eb3ee | -13.36543 | -48.20123 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 495c1495-e8a2-322b-8e2d-ebb3ac9ac879 | -17.69488 | -40.17681 | 2026-08-26 03:49:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e8c4a04-c600-3d36-bbcc-e40c96ceeb15 | -11.49121 | -45.11058 | 2026-08-26 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 281511ec-b181-375e-a0ba-1ef61c75929e | -14.79449 | -48.80211 | 2026-08-26 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4ba18256-630d-3802-a2c4-fd8a05dacf78 | -13.37117 | -48.20666 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a389913b-77e2-3b7e-83e1-236e68ad48b2 | -12.68781 | -48.40636 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4833d82e-14fc-3f56-9bc3-11ed5ba6eee7 | -11.42062 | -44.54133 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b098ec0-a6e7-3712-967d-ec49f1984f16 | -12.68898 | -48.40099 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edb11f29-e934-3616-b6ad-fdfbad19c515 | -12.68973 | -48.42278 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| afb92cd3-b6bc-30a9-b27e-76536e4284ca | -12.63505 | -48.41436 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a3128504-dc91-3e75-a4a8-af5d4f57dcff | -12.02366 | -46.00491 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| bc073f0f-4bbb-3e54-b0e8-c4f6e0339e52 | -5.84573 | -39.55102 | 2026-08-26 03:49:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d447491-e5cd-34cc-b602-af408b65f32c | -12.02601 | -46.02367 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b913a61c-e8b2-3799-9b5e-ca902aae393d | -13.36843 | -48.20688 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e2e1b8d-9807-3074-baa6-ac6c372f8448 | -14.79991 | -48.79214 | 2026-08-26 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5379f918-8590-36f3-a4b7-aba646ceea3e | -5.3443 | -45.16402 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3b1e1cf4-8820-3523-808f-6492e0edd668 | -11.42471 | -44.54958 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0989042-e91e-3c36-8ec0-2439bc94f2c4 | -5.51245 | -44.11481 | 2026-08-26 03:49:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f094b43-0f7e-3c54-8027-f6fd7c9c609f | -13.35953 | -48.2291 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b7b42a2f-6c75-352c-9ba3-f82cd73ec4a8 | -12.71233 | -48.38215 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2ac1cbd-4313-3d44-96ba-f461a0ca1a2f | -7.12668 | -42.78862 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4f7a8cc-4693-3847-a070-9f2f98bcbe89 | -6.2468 | -44.8013 | 2026-08-26 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4ad0231-bf01-3e85-8796-1f4b539a2a65 | -11.492 | -45.10657 | 2026-08-26 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 012539ff-c198-3ccd-9ac7-7a7e15a4e075 | -13.36906 | -48.2166 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 291d2ca5-6f04-3a43-9334-022e68315310 | -6.9129 | -41.11985 | 2026-08-26 03:49:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f88c735f-18c8-3d12-9411-5588ab9ec380 | -11.41856 | -44.55207 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3652c9e9-923a-31f2-87cf-94da66ab703b | -11.34099 | -42.12746 | 2026-08-26 03:49:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4947b4d2-92d3-3493-a5bb-91562d4d9032 | -13.36934 | -48.20272 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c41df19-1d9f-3859-afab-18a1d8b4fb1a | -11.01968 | -45.07016 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec7c0d17-e94f-3627-8806-3fb654afed22 | -12.76244 | -44.26256 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fd989ff-acbf-3169-83d7-79842ea49ecb | -12.76204 | -46.44654 | 2026-08-26 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37d3f424-91ed-3391-9a4a-39d04b7bcdf7 | -13.3526 | -48.22926 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 863de112-3bc2-3825-8371-492b100e6dbf | -4.85095 | -44.30347 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2842b99-fd21-3edc-b79c-06a3e39a0163 | -12.69164 | -48.41364 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45fcd18c-5a08-3247-a246-96c14b397365 | -18.54074 | -42.57502 | 2026-08-26 03:49:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4b5c051e-2141-30a5-b24f-d5da12270680 | -11.25202 | -47.051 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7dfe6d8-86c7-32d3-b996-51aa61a6e193 | -12.7672 | -46.45195 | 2026-08-26 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 037d91c7-868e-3652-8c06-cef07b4dc79e | -12.72027 | -48.37776 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 88fc12c6-abb4-3cec-8934-fdf9f85dd8d7 | -12.74111 | -46.48793 | 2026-08-26 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7da592b-153e-3ea4-8d9f-881de9d25daf | -6.3309 | -38.73438 | 2026-08-26 03:49:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 407bc62d-40db-378c-85f8-1f7938f29c18 | -6.9135 | -41.12158 | 2026-08-26 03:49:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
