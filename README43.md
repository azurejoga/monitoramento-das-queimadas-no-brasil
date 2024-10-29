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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8018a67-9222-3cbb-a487-0185ba86ea97 | -2.43863 | -49.03977 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a84b83c-af51-3601-a845-48e1af4576cc | -2.43787 | -48.9585 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0df27f75-667f-39a4-86bd-0924eb22d9a2 | -2.43733 | -48.96194 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc9a4f41-c208-3f55-9c7d-c681bc914853 | -2.43641 | -49.03236 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5a0a5e0-6b74-3bf4-aca3-6fbe4ef4906a | -2.42411 | -48.95989 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93bc9d95-b746-310c-87f9-dcb837fd62a4 | -2.42166 | -49.08306 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0737036-3bd2-35b9-a6b4-72987e2e0cda | -2.40003 | -49.02672 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 249ca821-3a38-380f-ada9-c4056ec3ad49 | -2.39673 | -49.02621 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ac1a2ab-8299-3026-a7a1-a4157604c8db | -2.35747 | -48.92818 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84325088-5180-31e9-9890-fdc9b1f4bc9b | -2.34696 | -48.90894 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03882b83-05cd-3319-b7c6-81d02f239545 | -2.34642 | -48.91238 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1eddd195-e84e-3c2a-956c-1af9d297c3f1 | -2.34588 | -48.91581 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92a088e3-9a98-3a71-a5b1-747f46406e43 | -2.34365 | -48.90842 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| afc31bbe-00d3-35fc-8748-e7c2d5028ecc | -2.34311 | -48.91186 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1ddd96e6-0fc1-3672-b462-ccb97eda439b | -2.34257 | -48.9153 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb756c2f-f96c-36ce-ac16-2a0fbbb0afed | -2.34203 | -48.91874 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96738e35-8508-308e-bbd5-c83756cb5918 | -2.31457 | -48.94268 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f624af4-77fc-3ec9-a3b8-b2f49df08472 | -2.31162 | -49.09054 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71b3493b-c9c6-370a-95b8-2c45e7d56d7f | -2.66741 | -48.99128 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0481207c-8406-3008-b7fe-4fd58f3dc1dc | -2.66337 | -49.12477 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca0d9cc-45fd-3cac-9846-f9cba48eb661 | -2.66006 | -49.12426 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee2f52e6-8df6-3dfd-b766-097ac73da7c7 | -2.65952 | -49.12771 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5db8bce-d337-392b-978d-b6e22524fa59 | -2.5768 | -49.11488 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4276b98a-8641-3ec6-8d9e-6300f28bc339 | -2.57275 | -48.96587 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20a0b1ee-790d-388e-b9c5-550bcedabf14 | -2.56999 | -48.96192 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1cadcde-5c41-391b-8476-7a9d5a7d8227 | -2.56723 | -48.95797 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c49c167-2858-3514-839d-9963b75023cc | -2.56446 | -48.95401 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd46af29-3046-3f1c-a042-27349e3faea2 | -2.56392 | -48.95745 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8bf6ecca-c924-36c4-b72c-63bbb1629f26 | -2.56326 | -49.11263 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f54b59f-d06b-30d8-bcfd-bf36bc1229dd | -2.56314 | -49.07021 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4585e04-3080-321d-afdb-edd6033c9a2d | -2.56272 | -49.11608 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5722d59f-7a95-314e-9a38-b6b897e1c92b | -2.5626 | -49.07365 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea936f60-90e5-3903-b0d1-754789e1ad06 | -2.56116 | -48.9535 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c2bd732-453a-3d95-87c8-d520276cf5e6 | -2.55983 | -49.06969 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701085e9-e65e-358c-8041-b9dd8c79001e | -2.55929 | -49.07314 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdd80e16-c2b6-3015-bfe1-0b704863fcb2 | -2.53218 | -49.0301 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45c8630e-53e4-3ea7-97fd-e389ef41c437 | -2.5235 | -49.08526 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a971b1df-e333-303b-8a89-d4ddce5f843b | -2.50198 | -49.07132 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5eef4fd7-6d28-31aa-85dd-de3a896f0af7 | -2.49867 | -49.07081 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f4573906-c883-39e3-a561-4eb4e114bc7c | -2.49599 | -49.10927 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f493175-b4ff-384e-b98b-80bb82449312 | -2.49268 | -49.10876 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc5cb311-c29b-3f88-b7f7-ba8ed7e32aad | -2.48665 | -49.12551 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a1150d6-c838-3aef-b1f8-3418c942ec80 | -2.48476 | -49.00864 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7d115e6-4a78-396e-a094-f902cb0dc903 | -2.48422 | -49.01208 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ea7ed28-dbcc-3048-93ce-1dcd94d3e789 | -2.47283 | -49.10568 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5fdbad5-2530-3b96-b92f-d72ecbbdcfaa | -2.47228 | -49.10913 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85321027-94e2-300f-94b2-c07c707b76e0 | -2.4722 | -49.06671 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0bf8a290-e144-3319-a8ea-799fd3677f2d | -2.45054 | -48.96399 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4996038-3c13-3362-8515-9fa047ca00d8 | -2.44026 | -49.02943 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61d02468-a506-3832-bc39-47336ed212e6 | -2.43917 | -49.03632 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ab10068-fd48-3b6e-b3dd-6dafff2cb3a1 | -2.42741 | -48.9604 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b84a5d2-a014-345c-b23c-7f34b6e5b7ee | -2.42687 | -48.96384 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3ccec0e-e03a-3ee5-b058-dfbe7a10db28 | -2.66076 | -49.25187 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2f6a346-7e6d-3470-b37a-498bb19070f0 | -2.65967 | -49.25879 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 80ee16fb-c5cb-3f69-99ee-138ce0e6955e | -2.65912 | -49.26225 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cbb5b6b-9ceb-3ff9-a353-019423be2566 | -2.6569 | -49.25481 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a546600c-d910-3eba-97ee-8452432d69f0 | -2.65323 | -49.25421 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10aea8da-1164-3d8c-9b94-7041ec711888 | -2.64991 | -49.2537 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 053f2b49-9924-30b6-93db-9a06d14bdcea | -2.63883 | -49.23779 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a58469d-3eef-31a9-91be-f48fd705bf9c | -2.63448 | -49.26549 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c7d43db-42a3-3041-8b0c-1d6dbc290a79 | -2.63062 | -49.26844 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ad8f3c5-9943-35d3-9cbb-4f0425cf7f0b | -2.62399 | -49.26741 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7398f64-105f-31ab-a5cc-e97f583e0090 | -2.61941 | -49.18871 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 676753a3-5705-344c-9e92-87b36f28bcff | -2.61845 | -49.25946 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc200d7a-ab49-3c90-894f-95fda10b9fad | -2.61383 | -49.15953 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09e579a5-7c51-33c6-87be-9cf2191b6e59 | -2.61296 | -49.2728 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b350bb98-7575-35a9-98b3-8e4ccd42cafc | -2.60118 | -49.17526 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24e03856-af87-30ef-bfc1-1c0280b04e70 | -2.59736 | -49.19946 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a83d9223-b58f-3274-baac-56857444b929 | -2.59459 | -49.19548 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d193374-f90d-336f-a245-4f2818908975 | -2.59405 | -49.19894 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9809d3a-825e-378e-ae45-06261a9adc8a | -2.59128 | -49.19497 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8638ceb9-d915-32b3-afc4-1cbd16f08615 | -2.59074 | -49.19843 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8b55bc1-ac07-3956-9dce-cc978f93264d | -2.58804 | -49.237 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 75b7bf39-72e6-3f6c-98f2-231fa13bace7 | -2.58797 | -49.19446 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6f0ef2e7-d2c9-38de-88bb-8f8d60753928 | -2.58527 | -49.23302 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2313db0c-10c0-3310-a5ca-05600af1f235 | -2.58196 | -49.23251 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5bf0622c-c8c6-307c-99fa-feb86ed99ca0 | -2.57575 | -49.14301 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 18c9d37e-b4a7-3655-93ee-e33bfa2f9296 | -2.57038 | -49.24136 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81dfeb5d-0f18-33ad-a516-2b6417000f34 | -2.56706 | -49.24084 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e486f05d-8e57-3cfb-ad7c-2674f8a4b8fa | -2.56485 | -49.2334 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aecfc56b-d245-33a8-a950-65a18ae1fbb0 | -2.5643 | -49.23687 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10bb10e7-5367-3cd1-a269-679d29cd52a9 | -2.56254 | -49.16219 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36b13d1b-eeb5-3807-8247-4de71b8d2b59 | -2.56199 | -49.16565 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ec0963c-93c0-36a5-a88e-b70bc9544266 | -2.55898 | -49.16149 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 42be150a-478d-30e5-9d12-edc262cbc068 | -2.55844 | -49.16495 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1eb0b8dc-4b83-3d9a-bd6f-790d1419a0f0 | -2.55301 | -49.19953 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1036a81d-b2a7-38c1-a7c2-f26e367a139a | -2.5497 | -49.19901 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 976d4c9c-78e5-3ebc-b6e8-935896c0c2e8 | -2.52652 | -49.19542 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6e1b5a6-2700-3365-91de-51d7e4202998 | -2.52202 | -49.1593 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df280ca-b0ff-3d3f-9b1f-9fb850a9ee10 | -2.51485 | -49.16173 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4699ef8f-aea5-30fb-859d-00e1a2f79a5d | -2.51272 | -49.19682 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b53ce77-c0da-3613-83b0-55cc34f8c470 | -2.51154 | -49.16122 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1af75a1c-b3bf-33f2-8359-8fc59cef305f | -2.50995 | -49.19284 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b7b3c7b-3889-3272-8eff-5cfdec5df172 | -2.50941 | -49.1963 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9d47e9c-7da7-3cc4-a8d1-a6baf0c5907f | -2.4852 | -49.2422 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13d8a75f-8abe-349a-ab81-739255e1323c | -2.48243 | -49.23822 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dfb6da5-b559-3884-9830-c7d46a2cfa85 | -2.47676 | -49.14521 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 072ff60c-23aa-3388-9596-dbc8fe3bed22 | -2.44336 | -49.16073 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25d44366-48e0-37a5-ad33-ddd65df9b17c | -2.43896 | -49.16713 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41b0b747-b5b8-3d9d-92c8-5062b183c9ee | -2.43027 | -49.22251 | 2024-10-29 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README44.md)
