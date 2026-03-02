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
| dae2d2fb-0285-3685-ba42-2887b24fb613 | 3.04315 | -60.6746 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fee4aa0f-3501-3ae7-bc03-c8479748bcf4 | 1.49142 | -59.9303 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 423860ae-e04c-389c-9725-12a5aa45c8cd | 1.09535 | -60.17585 | 2026-03-02 05:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f2f3751-0c86-35da-b47e-22d276ff8df7 | 1.47609 | -59.93265 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7739020d-64e6-3382-b36d-d8e5ce148aa6 | 1.72064 | -60.29611 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b520f55-b72d-335f-a1c8-79f35d33c720 | 4.2566 | -59.90575 | 2026-03-02 05:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cc4a5c2-a5bb-343e-ad63-e554390c9361 | 3.60438 | -61.66537 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| aea87bc2-7ca2-3143-bc4c-c517d7d0f73f | 1.49865 | -59.91052 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8690afe2-c9d4-3b8e-9173-98251197b9ce | 3.60876 | -61.66466 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| dae1782d-254c-3672-943a-f8269c46cb7a | 3.60803 | -61.66037 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 374ac735-2d78-3035-bccf-3d8b5da8034e | 2.85082 | -60.84806 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 837f9d75-6239-3d63-8e95-30c1d777d2d0 | 3.08147 | -60.00985 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 958b9ea0-f2c8-328f-a91d-6b35b8192a68 | 1.86602 | -60.40326 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f6f000ea-6f01-33ed-967f-25c3a9480deb | 2.85916 | -60.81099 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52c7a0e9-92d9-37e1-927e-7377a99c25da | 3.61241 | -61.65967 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fae9b28-0602-3b08-80b2-a14e82ab2978 | 1.51183 | -59.92691 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d6187e3-eeb3-3644-ab7b-6bf97e0ac44b | 1.50723 | -59.93085 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f634a3-ab36-3913-9b3e-b2b79eeb480e | 1.49914 | -59.91348 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 428c81c2-a335-3e78-8cba-89e5f3018664 | 3.0565 | -60.66722 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be7b06a-c458-3e4c-87af-2b7682019880 | 1.08395 | -59.25145 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 495ced69-64d5-3394-9389-78b940e2beae | 1.10089 | -60.178 | 2026-03-02 05:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f6c910a-79f0-317d-bb1f-0c7272dc082a | 1.8611 | -60.40406 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b73f5838-6f52-330b-8413-b7d3f5cce600 | 3.04704 | -60.66877 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 841b8fe3-bbf6-3765-b799-b881914005ab | 4.25468 | -59.89416 | 2026-03-02 05:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3153329f-4974-3e34-8c2b-fd8a8045a73c | 3.03842 | -60.67537 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e805dc9-75eb-3ce4-ac35-6399b53bedf6 | 1.48939 | -59.91796 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6bec388-0399-3b38-9d35-a26a8da07d44 | 1.1004 | -60.17501 | 2026-03-02 05:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bacdc24f-6481-3b17-baf2-604a20868980 | 1.0624 | -59.2548 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a208b884-65f6-362c-98d3-d754a173fdf1 | 1.49652 | -59.92945 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59f56fdd-1ea0-356f-937b-05ac7d4ffd2a | 3.05177 | -60.668 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dd169ec-cfa7-3451-ab6f-75d9c8da7eb6 | 1.86022 | -60.39852 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| acb8f945-3f9c-3f98-a700-2a39b114ac03 | 3.60732 | -61.65609 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fa678bb-e1ba-357d-80b7-61e93ea8031c | 1.50675 | -59.92789 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ffe3bf1-197e-3b04-9de7-8116e51d0dc2 | 1.17248 | -60.82687 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e03d24e6-03a4-3cd1-adec-383d8673dc88 | 3.05733 | -60.67226 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4d1fd79-28bf-3b88-a2d7-0f880b580462 | 1.16484 | -60.83587 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d8ee876-0bf3-3cce-b960-96fbd4c4203d | 1.85686 | -60.39771 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3cce0387-6861-345a-b3ff-d6da64480e33 | 1.11992 | -59.20013 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2201dc2-c259-3b8d-af91-7ebddcd72159 | 4.37579 | -60.6249 | 2026-03-02 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 286e9157-9444-3c76-83c4-a6485beb45bb | 2.85998 | -60.81598 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f84545e-0f4c-33d9-b767-406b66a2738c | 2.85387 | -60.8374 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81e30965-1405-3cc1-ae55-fc840659b0ca | 1.50625 | -59.92483 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f89dd32c-8700-35ef-b222-fef1e4cbf0a3 | 2.84918 | -60.83816 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a8614fb-74be-3940-b67c-4d8e06fd205d | 1.48683 | -59.93423 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b135769-f12f-3a32-a374-5b629c694453 | 4.25886 | -59.903 | 2026-03-02 05:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1206a552-b711-31de-8521-9e2e545b7353 | 1.48531 | -59.92502 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9be2ad63-7e7d-3057-816f-ac84b91a6303 | 1.49091 | -59.92723 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2d006e5-9f21-3aa1-9339-399108f4fef2 | 1.50114 | -59.92563 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8a84427-35c5-301b-9134-144969ba1e44 | 1.49601 | -59.92634 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53cc1c69-d953-39c9-a1b1-c16ba157a351 | 3.17781 | -60.6879 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66221805-8c1d-378d-b6d2-d248c7d3eaa0 | 1.48122 | -59.93199 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f6dd0b3-a575-30b5-a65b-2ee1b27ea3c9 | 3.01731 | -60.69437 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2881c7d-121c-3bcf-9a74-e32aebfe8616 | 1.51278 | -59.93275 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6289759-c227-3352-80cc-604f5bbee983 | 1.49499 | -59.92015 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae82239b-43e4-3f9e-8441-eb63ae541d29 | 1.49352 | -59.91122 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 36a78738-4cdc-32b9-b7f5-bd628f45885f | 1.47236 | -59.92854 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cddc909f-0c5d-3fb0-b589-a3093c77bdc7 | 1.47284 | -59.9316 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f567e4d-8d2b-333f-acb8-de6cbbaf2796 | 1.50062 | -59.92248 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4468bbad-eb54-3f03-9ace-5740e318de1d | 2.84836 | -60.83322 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5914454-bd90-32ef-825d-b10799b8b968 | 1.16883 | -60.82982 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a99ea6fd-fa1a-3393-a893-1c87cbef8ed4 | 1.5046 | -59.9306 | 2026-03-02 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 256900ea-0477-3381-98cc-c19cdc8fbaed | 1.4864 | -59.9117 | 2026-03-02 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 33f714b0-6a2e-3cc5-9914-cbe4adba718d | 1.5047 | -59.9116 | 2026-03-02 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.9 |
| daeec5ad-b9f0-3da8-911a-1a4d5d886c98 | 0.47401 | -60.39548 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce3dad1f-4d8a-35fa-ad3d-c5beec9fb132 | 0.69927 | -59.96951 | 2026-03-02 06:01:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe91adaf-261a-3308-8c51-35fbe3dca87b | 0.44999 | -60.40409 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 918cf57a-0672-34da-a918-47f35be12c06 | 0.23157 | -60.51529 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b82698-b7c7-3b4b-b75a-9b598dc2de93 | 0.4532 | -60.39169 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d2598444-b257-36d3-bf67-ab7b68e8f1a7 | 0.09077 | -60.62796 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8036e65c-77e7-3511-9cfd-5f8478d0bc40 | 0.47448 | -60.39837 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54b3ad6a-3368-383d-9bcf-e04b4efd887a | 0.19504 | -60.44739 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d5d1e45-5fb0-3d00-817b-e6659bc23548 | 0.18907 | -60.44233 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82638c0a-f942-3ae2-8b27-647db9f0b829 | 0.92063 | -60.52764 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 424ea8ef-3ed9-3a3d-a60c-129af69f2f6d | 0.92557 | -60.52684 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c438126-6a08-3580-b222-eea9f37a6d3c | 0.18954 | -60.44527 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b58857b-c473-32ab-94b7-ef8cdfdc2316 | 0.49366 | -60.5158 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c580d929-399b-3eba-af83-d5f2498e5a76 | 0.09575 | -60.62718 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3075e4fc-d7e2-3461-98c5-887411e9d3b3 | 0.09757 | -60.63849 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58d5ff87-c384-3300-ba3a-748d881a2935 | 0.23112 | -60.51246 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30072a4b-d694-324a-9792-bc721811408b | 0.09666 | -60.63284 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c3a2bcb-c5df-326d-8d24-d2a542e906fd | 0.49588 | -60.49807 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04938d0d-d38d-34d1-8287-f6ded39e9583 | 0.4692 | -60.3951 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1323c28-2e7b-3dce-9a9b-d537dd61b834 | 0.47467 | -60.39718 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35c15795-e0ec-3c2c-aee8-877347606405 | 0.9217 | -60.52546 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91370c20-df71-3ae2-8f5a-c11d9ff23c4f | 0.45868 | -60.39378 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76f441e1-ad0b-3999-bea9-826ae47d2d06 | 0.64587 | -60.66431 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4334af5f-b2ba-3235-bd7e-f6ffd08b4265 | 0.45365 | -60.3946 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 624a9363-4714-3575-9695-f0aedd35b327 | 0.85507 | -60.40343 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02fdfc15-a536-3b45-a034-3ae2eab5a560 | 0.70492 | -59.97181 | 2026-03-02 06:01:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 560c609f-ec77-3646-875d-0b28bbf39854 | 0.09529 | -60.62435 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba91d4f6-86a9-3810-88b3-51706745d478 | 0.64722 | -60.64143 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ba19c6d-166b-3e09-a19d-4330479fe7bd | 0.69976 | -59.97261 | 2026-03-02 06:01:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eba377c9-5e99-305d-8829-2cb680805dee | 0.0962 | -60.63 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf8db58-00e9-3c5b-a4a2-c994618ecdf6 | 0.45044 | -60.40699 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf795ad8-a312-3012-b4bc-afa082c94897 | 0.46371 | -60.39296 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 240f1ae5-bc69-38b8-8998-2c872087c1b0 | 0.49866 | -60.51507 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 834ae90b-a6c4-3723-b478-5cb30ad34e61 | 0.85553 | -60.4063 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cac6173-59e7-3650-a487-d1612736f0d2 | 0.49274 | -60.51017 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96f2bc75-0360-3a98-907e-697df9cc1af0 | 0.46416 | -60.39586 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0abae02-3b30-37f6-8fc0-f69a6f5b15cd | 0.1886 | -60.43939 | 2026-03-02 06:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
