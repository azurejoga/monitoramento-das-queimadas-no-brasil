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

## Dados Diários - Página 234

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57ae2fc1-803c-3243-b760-f40cd464a683 | -1.03223 | -47.91452 | 2026-10-07 16:39:00 | NPP-375 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 46dfb79d-d4c6-303c-8b50-1d9a5a564251 | -2.93976 | -54.17327 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 56926154-d663-3017-bac4-0b9821e22cd5 | -3.2649 | -54.0466 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3ba0a2bb-2669-3566-a3a5-192c2c6b133a | -3.65922 | -50.95058 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b021f735-9062-3df5-83a0-ced96ee1f122 | -3.03879 | -53.92105 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4a3938f0-c310-365a-831f-7c70e1a074eb | -4.0616 | -55.32633 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e38900d8-2533-32eb-bba5-35c3983b3c62 | -3.01923 | -54.06279 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| fe15abe0-ed82-355b-a4ed-2fdaf99cc660 | -3.30026 | -54.024 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67b0967a-b706-36ea-9a40-ec5740f36a4c | -3.72659 | -51.04122 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 1f501079-4755-3571-9756-2445e6f4c56c | -3.09769 | -54.28763 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb0877fb-2cbc-3ea6-bffa-3a1920a9530b | 1.4825 | -50.7626 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0e0d2cc6-ce14-3b0a-a458-09ce63e2fe4e | -3.73783 | -51.20952 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 55e2614e-1786-388f-91e0-4a5593df226a | -1.28957 | -54.56322 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 04874bfa-29d3-3384-98ad-ffb1c919821d | -2.04977 | -54.30619 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ebcc8d7f-1bf2-3ac9-b212-4ca39409fd59 | 1.87283 | -55.73152 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca613112-83b3-3a93-99b5-de81e3b81e93 | -0.83635 | -48.5942 | 2026-10-07 16:39:00 | NPP-375 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7f87f391-d374-392b-aa0f-75e049374f4c | -4.34756 | -55.133 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 39c60656-80fd-3e60-b378-e6149436510f | -1.28554 | -54.563 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 785ceaeb-4f91-3443-9af3-b3eb34bab40a | 1.07891 | -56.20025 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 151ff69c-5d93-3baa-925a-0b8f6a6f3b66 | -3.86983 | -55.99391 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0fe34ae8-5990-3624-ae5a-6431361b8ff3 | -3.24303 | -56.80488 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 80040bfd-51a4-3938-b57d-20d042068363 | 1.88024 | -55.72123 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f35c0854-53d3-3b09-8fff-e8e3996ba198 | -4.54425 | -55.61438 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 82503f71-d439-32f5-b859-5afdce9c0729 | 2.17703 | -50.96697 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 97c181ba-4d42-3268-9335-d7582f7712ef | -4.1087 | -54.02305 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a3700159-a416-3b1b-99f3-0ded508856a1 | -3.64852 | -54.06179 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9c0e0508-a5d3-3999-977b-8b00266f7d03 | -1.79965 | -57.11125 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ea6d6131-5b9f-3126-9b95-f8c1c3dda9ff | -3.286 | -54.03975 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 913bbdb7-e0c6-3fb3-87e4-8b923642d378 | -2.10805 | -52.05943 | 2026-10-07 16:39:00 | NPP-375 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9b6a20eb-fcdd-305e-962e-2a5312693597 | -3.26199 | -50.40457 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 83476979-17ff-3288-9d38-e97a16494c08 | -3.84902 | -55.98895 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f212f1a9-236b-3e02-8e48-fa157e373ece | -3.52531 | -54.63205 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| f703054a-c926-34fc-ac8e-f89efb2bd154 | -2.44552 | -56.54652 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 31e281ed-401a-36ae-b20b-0bfb06b4ff2c | -3.24785 | -57.87002 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fe02fd7d-d754-3957-a1a9-0fc290b022a6 | -3.674 | -54.50678 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f4e4cca7-b7f5-3077-9643-1fb9bc43c906 | -3.93727 | -54.57508 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 329a8d5b-3174-3c96-b679-6926a3dc3974 | -3.44444 | -49.25765 | 2026-10-07 16:39:00 | NPP-375 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 28e8b9ed-5dbf-39b7-aa3a-c2cc73f49100 | -1.47904 | -53.61506 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b26a9e83-d307-365b-abf0-7f4e6cf35815 | -3.69089 | -55.4916 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 60a90914-0eae-3962-b642-5f2ba7114bf0 | -3.64801 | -54.05834 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 76d5fa56-17ca-34fd-9672-fd0351777d14 | -2.99783 | -54.10432 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cc8c0023-ad3e-3d95-9961-b695c76a0f36 | -2.26659 | -48.74889 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 31e065f6-34af-3d35-b3a6-fbb9200e8cd0 | -3.30199 | -51.10737 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 5516799c-3568-3782-b597-5260b8e93f08 | -4.13936 | -54.90698 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 68cbb056-a0c2-3bcd-b566-b4e90bb716c6 | -3.29154 | -54.07771 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9cca31f2-6b05-34d8-a8c5-4770f8acae18 | -1.63599 | -55.41655 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78e25cb3-3092-3cd2-a7c1-393a83fddd6a | 0.71905 | -51.36487 | 2026-10-07 16:39:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 03471bfe-fce0-3d8e-a2af-b5515c29e8b5 | -3.4295 | -49.26488 | 2026-10-07 16:39:00 | NPP-375 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c16915ae-724e-3ec1-b138-ba70c92880ed | -2.4315 | -56.53841 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| cbfbde76-3411-374a-8778-a799a28af9ab | -1.73196 | -54.84282 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3ebaa2bc-533b-3527-8710-c4c62bdc4f2b | -3.49488 | -54.62112 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4175525e-5efd-3110-ab81-5d89b7f77650 | -3.09797 | -53.73474 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cacf2b9c-b369-3e4c-9488-fb102610f5b6 | -2.46863 | -56.06422 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fbd8f02f-29ab-344f-a758-79967dcaf2ef | -4.53898 | -55.61867 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e73a1073-0b47-3a32-9369-95d37ab4dffe | -2.77347 | -54.10589 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 7edd446c-de43-3686-b8ad-1fc8c48119e6 | -3.22535 | -53.88636 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f292a211-c832-3f83-9a65-2cc185dbf08d | -2.93883 | -54.15492 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fea3717e-7d77-3bd5-84f4-71c5234c04fc | -3.04944 | -54.15302 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6c4b70ca-b42a-3574-b7d4-f9dfd473950b | -3.29385 | -49.12838 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b8629c95-6f4d-350c-ac22-672364368a42 | -3.28926 | -49.12413 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 79e58472-1e53-3ceb-b161-604dbb3d0998 | -2.91314 | -54.10686 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f826e8ea-c1b2-3c1d-aa63-5a4b146c4b69 | -1.27786 | -55.86782 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 956d4b8f-73b2-3693-9620-05b0f5ccc865 | -1.79863 | -57.10406 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 64bfe6bb-4fbd-346f-9109-0e1f6d144de8 | -3.26283 | -54.26349 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4062cc8-321b-3b97-895f-cee33ae2a2a4 | -3.19802 | -50.55597 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2743a367-0cd4-3dfa-9bc2-a5d2f5e9a9ce | -3.1091 | -54.17513 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 616a45b0-f38f-3420-98c5-01a3a83bbc9e | -2.22071 | -53.701 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ae8d2aaf-064e-3e37-b1e1-f4d3f650c87e | -2.05397 | -45.97195 | 2026-10-07 16:39:00 | NPP-375 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 557171d3-703c-3690-9bac-867eaf1a75b3 | -3.85519 | -55.98788 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f03fad8d-e53f-3f36-a6d2-85a77d91b95d | -3.25056 | -56.8098 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 492e0e21-6c11-33d6-92b3-2babb914785c | -3.03793 | -57.4847 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 1b9b5911-cfec-31c9-88c3-e74ce2ba822d | -1.26585 | -55.39354 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 320bc755-ad3f-39d6-891c-56a4ee7dacec | -3.28742 | -54.0117 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ed62292a-98d0-3656-930d-fcd1a571f855 | -2.00732 | -54.09575 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae69c3b7-d3dd-374c-b3b8-6311af37e8ea | -2.57696 | -56.16211 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2f83ec60-9512-33b9-9532-0e27b946d263 | -2.77868 | -54.06692 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b7cec6d4-75bb-365a-aad1-c8a11cbcbb23 | -1.2191 | -49.03723 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5c21b2f5-92b8-3c49-ac2d-65b08b2d0a28 | -1.14007 | -53.11012 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0da5c0f1-3855-39f9-b19d-4a0b8c8bafae | -2.65672 | -54.3076 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 87122124-f17a-3cd5-a7ad-a263d53cf2b3 | -3.30704 | -51.11097 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 667b3de5-0275-3a59-bb45-b3092a2cb910 | -3.44071 | -56.94251 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d499988c-efd1-3a20-a964-2f363745f677 | -3.99004 | -56.26009 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 618735d0-7183-3282-b5db-aec2a0c2f703 | -3.00512 | -57.74969 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 30d7a20a-08d7-3d3b-9a8e-11abdb2f87c3 | -3.09748 | -53.73151 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3ed6f37-4201-3642-ab34-3756659ea643 | -3.74942 | -51.22599 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 139b8bb3-4c61-3011-abb7-652bfd9bdff3 | -2.87994 | -43.01516 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d06bf1e0-2c8b-36e8-be33-134254211c11 | -1.10754 | -52.26418 | 2026-10-07 16:39:00 | NPP-375 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eaaee865-cdaf-388d-9dd9-c5753fc252e7 | -3.2479 | -57.86792 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c9fdda61-6501-3b0d-a149-384722a6c033 | -3.4887 | -54.6183 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7b20a2ee-266d-3175-b20b-3cab0ef36257 | -4.14911 | -54.031 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 258b3b84-f1eb-32b0-9691-d58b705557b9 | -3.54928 | -54.66311 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7cb14f43-5b12-3a2e-b8b1-7a76fdbb0950 | -2.49431 | -56.14925 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 718094be-b3ef-3844-b21e-719661749553 | 2.43816 | -51.38518 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 92cec9b4-4c82-3503-8af8-afdf71bf5cbe | -3.10392 | -53.77394 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b54d038a-05ad-3617-a99e-431110bbc7dc | -1.71126 | -55.44115 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 41b0449c-30e5-3d41-bdae-5aa84896e97a | -3.04965 | -54.14821 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c851b4ac-9b1b-31be-886e-127dc220ea06 | -3.27661 | -54.01318 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cc3c44fd-74a9-3f5d-9ae0-8b02735f06e6 | 2.2822 | -55.9501 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5441a33-feb2-359c-a6a7-3b45b414a29f | -3.54773 | -50.0956 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 00652343-b7e8-323a-8c22-7f5321cfb73b | -3.15848 | -48.58248 | 2026-10-07 16:39:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |


[Clique aqui para ver as próximas entradas](README235.md)
