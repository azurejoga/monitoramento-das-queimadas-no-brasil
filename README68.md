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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63711090-16d2-3b4a-b5c5-4c43d02e441b | -2.82545 | -49.25051 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c4239ec5-a31f-3525-939e-c6a04c5fa2fc | -2.8249 | -49.25402 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c919ba15-765a-3925-8af3-50779adef271 | -2.82435 | -49.25752 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eac9f2c-bcac-3295-a633-0e8ed32b5aed | -2.82212 | -49.25 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| bcce627d-4295-3d66-972c-c79b867a2d5d | -2.82157 | -49.2535 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| cb788b0e-1dc6-37e9-8123-ca688a60dba9 | -2.82102 | -49.257 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 166ea18d-02ea-3b8d-92cc-4228cd914e80 | -2.82048 | -49.2605 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0187e551-7aa9-3366-b204-c35365a0e0e6 | -2.81993 | -49.264 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63163885-aa5c-3fea-8a1c-3486301e9377 | -2.81878 | -49.24949 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b120bdf4-17ac-3009-8876-9cab6a53795e | -2.81824 | -49.25299 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8739b2fe-4b70-3e50-9382-a8045ab92f5e | -2.81769 | -49.25648 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd9330e-41cc-3a08-b7c8-e0615070e314 | -2.81714 | -49.25999 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30f712d6-ec12-3e43-beb3-c82541ab7fc2 | -2.8166 | -49.26348 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c3cba50-32bb-3711-ba43-1e2395c887dc | -2.81545 | -49.24897 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0225278b-1f81-3742-a362-114a9e5a5cbf | -2.81491 | -49.25247 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2a4cc06-b90a-3bee-95b7-becd77b104ce | -2.81381 | -49.25947 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b296359-40fc-335d-8c02-afcdd3b4031d | -2.81212 | -49.24846 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 361a4420-48fd-343f-9c5c-0ee674c59ace | -2.81157 | -49.25196 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed6482c-e394-37df-acda-fcef19c69b61 | -2.80988 | -49.24094 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee174f7-2f42-3bdc-8d9a-12a02fcb8da2 | -2.80934 | -49.24445 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01bc7e83-89cc-379b-aab9-295a9710804c | -2.80879 | -49.24794 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c2186e5-e4cd-36d7-a435-356f9f432195 | -2.80655 | -49.24043 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63fc654f-9c8a-387a-83f6-e7aee47bcf31 | -2.806 | -49.24393 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24d7bd20-3685-34d8-be0b-15e260663bbf | -2.80546 | -49.24743 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ff060e1-acb1-3e98-972d-76807977e191 | -2.80322 | -49.23992 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 601f20c4-74b5-300d-991c-4c7fe6263fa6 | -2.80267 | -49.24342 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5f9a6e8-7f55-3442-a339-6589411ca953 | -2.80212 | -49.24692 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5706371-e438-3e0f-b32f-cc0ada795088 | -2.79988 | -49.2394 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e5a659b-0508-3b48-84ff-a23b84460056 | -2.79934 | -49.2429 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4db41e1-67c2-36be-b7dc-b30b6b963956 | -2.79825 | -49.2499 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 661be393-b646-3264-bbb5-7d91e0e18a4d | -2.7977 | -49.2534 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08f39752-69b3-3d39-9a16-e15428423c47 | -2.79716 | -49.2569 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b840c793-5189-3e52-b6c9-894eda7d898f | -2.79655 | -49.23888 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7f99745-dfa5-365d-a97a-689f6fd37f22 | -2.79601 | -49.24239 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce4d183e-74ea-3284-8d95-f00a7893496e | -2.78764 | -49.23034 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6170ed2e-891c-3f8b-9ed1-634385862bf5 | -2.7854 | -49.22282 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdcb8e13-2e6f-382c-a7f6-04139bf0f258 | -2.78486 | -49.22632 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c217f66e-3dee-3643-a331-48b03b34da02 | -2.78431 | -49.22982 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0324a77-fe42-35d1-b5b4-1df4e6cae16e | -2.78098 | -49.22931 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ac8e73d-b474-3c27-be17-bf33bbd756d8 | -3.50663 | -50.28101 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dcfae6c-b1b4-3549-a8c2-bd891bb0221f | -3.49749 | -50.53287 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b0f3200-42d7-3ddc-be7e-8eaf2f7e78ac | -3.48194 | -50.48119 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d4aa05a-6ae4-388e-ae45-f59fa77aec03 | -3.44418 | -50.15916 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcdada3a-e4b3-3210-9707-256d399765a5 | -3.44364 | -50.1626 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15869146-15d0-345d-a7c9-0a6811d8ec2e | -3.44087 | -50.15865 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e34b736f-b6cf-35f2-919c-59fe2be86050 | -3.43164 | -50.19593 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df62caba-4cae-3b0f-96fd-fce860df5100 | -3.37726 | -50.21915 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf51aeea-b5a6-3c7f-94ed-4243e6edb3b5 | -3.3734 | -50.39443 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82023898-2d18-3839-8390-57de6508c375 | -3.35716 | -50.10654 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b659bf9-9ad3-3552-8256-4a331391ca1f | -3.35386 | -50.10603 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de44f3d-ecd7-336a-8c21-573a59d2cddf | -3.34961 | -50.15466 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d4bdcad-d88d-37e8-8c11-c3e4f1bd7064 | -3.34454 | -50.29459 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d771f2a8-84e9-3df7-92ff-4a07fcee45b9 | -3.31921 | -50.11121 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d271f5eb-b0f2-3376-b14e-e908a2475dce | -3.30072 | -50.01323 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9b91db7-1ed2-3bd3-89dd-c7a11546fd2c | -3.29684 | -50.16758 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6b2b137-88f1-31b6-9785-fe9ad57eb1d2 | -3.29407 | -50.16363 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4a1cc55-dd3d-3143-baa1-2691d3791b73 | -3.2712 | -50.17757 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c545e66-3a9a-35ca-af7b-a348cfb73c0d | -3.25739 | -50.15783 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9230939e-91c5-3e07-8229-bf29f208a3bd | -3.25644 | -50.20694 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35bd8830-9084-362c-a989-9599914e89a2 | -3.25577 | -50.16813 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1886c7f7-e555-3099-a1c2-9264941d132c | -3.25313 | -50.20642 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aedf9832-7e1d-377d-86e6-b0d5bf128b13 | -3.25037 | -50.20247 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e20650b-04ed-3413-a11c-d6a01b4a5a3e | -3.2463 | -50.36018 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d7013a5-ef81-3fa5-bdb3-f21bf6f3adcf | -3.47898 | -49.67692 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f26fa79b-f6a1-30c7-b71e-8f5394398061 | -3.41001 | -49.53065 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22143525-7207-3ae3-8ee1-53f859c074d6 | -3.38622 | -49.70481 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be4613c9-565f-3184-b1cd-c013373ab8c7 | -3.38568 | -49.70827 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02476c38-064c-356a-9188-37955fa77f20 | -3.37905 | -49.70725 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1afcae1-9c33-3430-ba2e-7d262083062d | -3.28085 | -49.55341 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebe4d085-494e-357d-80ad-eaebfbd07eae | -3.25261 | -49.49525 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eafb9516-d4e2-354c-9de6-7b0d741dc822 | -3.24929 | -49.49474 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a7d8821-be74-3289-ac38-c023a6920cb7 | -3.16805 | -49.53562 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14f8ab52-b3c5-354c-b1ca-e36e14d04c0a | -3.14841 | -49.77026 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2076f57-42e1-3d04-8013-c80f85215a84 | -3.1417 | -49.53151 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6550334-0caa-3302-9a00-20a61d09f378 | -2.87064 | -49.46138 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82b16d4-0a99-3e28-8932-d2deadb541ff | -2.8701 | -49.46485 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5575c98-0894-324d-ba13-0123ca27e704 | -2.86841 | -49.45391 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbdbaa2a-e151-3067-9ee5-3b535889ef1b | -2.86732 | -49.46086 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d4eea69-e522-3f16-a625-4f28170a3d43 | -2.86563 | -49.44992 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 363349b1-40dc-3c9f-a498-c999ddf24074 | -2.86509 | -49.4534 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8ad72a2-452d-3524-a974-c500437530d3 | -2.864 | -49.46035 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cfe805c-e092-30a4-821f-9fb1b1b75752 | -2.86176 | -49.45288 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88de3c3d-df63-37c2-b59e-8561530b9c05 | -2.86122 | -49.45636 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26372f81-adbd-3b41-99ca-95df9079ba66 | -2.85065 | -49.37243 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3357378d-a8f2-3a64-ad46-11a40d2290fb | -2.84787 | -49.36843 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26917d4d-6f7e-395e-b041-ff5e0045e9eb | -2.82829 | -49.53623 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fd34e39-fe7d-3cce-a4f3-7578e544c346 | -2.82246 | -49.40017 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78cff50a-b3e5-3d3a-a654-27ac805d94fb | -2.80805 | -49.62173 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e40524e0-0da7-389b-ae03-4cc303f5ad93 | -2.80511 | -49.83718 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a07b26e5-83cb-385a-a8a8-63d57263ef97 | -2.80175 | -49.31487 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3d7321e-152f-349b-8e1b-1a5cf0326861 | -2.8012 | -49.31836 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc70ffc7-d08e-361e-9956-4846d0c46fb2 | -2.79788 | -49.31785 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab9af6cc-c8a0-33d1-8c9e-993db63433b3 | -2.79455 | -49.31733 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcc1e45c-57fb-3c4f-8be6-abb80b8b86cc | -2.79122 | -49.31682 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2d0f22a-6652-32c1-968b-59824e4de7c2 | -2.78789 | -49.3163 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0d4e60a-8227-311c-9951-37d920402eca | -2.78735 | -49.31979 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e2afee-482b-39e0-9bfd-eaf9ef98e52e | -2.77737 | -49.31825 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d863e625-8f10-3485-aeb8-4ec0544aee98 | -2.77404 | -49.31774 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84106fad-92dd-37f0-aaf2-fb6c6df7fb77 | -2.7735 | -49.32123 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdea3cff-55b9-3617-aac6-656ce42a81f6 | -2.77071 | -49.31722 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README69.md)
