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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acdc31ad-69b4-3885-ba61-bb6ba8c1b2f1 | -2.5748 | -49.99816 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a808de-5ceb-3384-b535-3d4b111eed12 | -3.21669 | -54.18063 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f0389fa-e758-343a-9517-634582bfb57e | -1.76194 | -50.85293 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3ea336d-b860-30c3-b960-ef5ca0f04a51 | -2.77427 | -54.06548 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d934863-f87e-3b47-bf2d-3da745ae23ca | -1.74061 | -52.92373 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55e14b88-ca1b-35b7-9401-ccbfdf793c1b | -1.43506 | -55.24834 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61c3111c-21ca-3b47-8fe7-adfbf14ad5ac | -1.15929 | -53.69019 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec7d2dd4-0ac9-3c46-8bc8-5ac539d652f0 | -1.63926 | -53.86436 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6cf3e5d-1060-375a-aa61-95f6f1c75b1f | -3.17434 | -54.32045 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84ef5506-0592-3c88-a905-b3fdffc7d52d | -2.79929 | -54.05862 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dee6b9cb-ebad-310b-914c-9c37f2a7e11a | -3.06344 | -50.33163 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73d02efc-59c6-3c53-ba1c-398d11e65140 | -2.84488 | -54.02982 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 532ce812-7eb9-3708-baff-13a772bb2d01 | -3.60921 | -49.98502 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74af083b-e24b-3631-8850-192525afba4c | 0.94104 | -50.75003 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d6948209-56b6-3f67-a45d-f9c79a6ff74c | -1.69755 | -52.63666 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63bd0494-a6e0-37ec-9ad5-c2be3c886be8 | -4.00094 | -54.61645 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b17799bc-27b2-3455-8f60-4a8aaba5ba7a | -2.36984 | -56.1181 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c444162a-5bf6-3c3a-8332-f1f7ad024d82 | -0.94022 | -51.6634 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27bae6f0-6dae-372c-b5a7-87a29559d1b8 | -1.20548 | -53.67928 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 235f82c7-e8a9-3e4f-a74d-48e17aa17fdb | -2.53388 | -54.03148 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcb63c16-2d00-3b56-9722-db362a7f627b | -3.28979 | -53.66703 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87f3603a-13d8-3f74-8582-3ccc0bfd0fb4 | -3.86036 | -52.35262 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25394a9c-f3a5-3599-ac3c-bd4db9f16a7a | -2.80877 | -54.06367 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbe58314-a102-3750-a933-1f3464efd9b8 | -1.69169 | -52.18414 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d70d118-2a97-3654-a26e-a3b1ae17f14b | -3.86277 | -50.16822 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e7c3955-2451-3a6f-9caa-78e776e45b2e | -2.3103 | -49.0753 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7662fa0c-70d3-3ea0-86d1-87b642be320b | -3.38968 | -53.2705 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2c688b4-3e14-3168-8e30-35e6e87079e5 | -1.44517 | -54.51801 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccd27ee7-3782-32c6-9811-58d9016e9e1c | -2.84385 | -52.53878 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e35e3311-1063-38ad-993e-d2a6c3ac4fa2 | -2.46872 | -53.69039 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 561112ca-24cc-3442-85dc-a5c67d42ff7f | 1.20889 | -55.93706 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83dd84f4-7f26-3a2d-80f0-da7801989b2e | -3.10742 | -53.26919 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb563632-32fe-3f32-85ef-151f990feb24 | -2.9823 | -48.72724 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fd919fc-a263-3c14-9664-9c9dcc8ffb9e | -2.61361 | -54.21147 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ff52dd6-c378-392e-81b1-5f80069bfbd1 | -3.32779 | -50.2515 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72638f28-6f05-36d3-a0e7-813e37b0c39f | -3.46492 | -51.33683 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34777098-872e-3fe8-9ddd-a423879fc26c | -1.68426 | -45.78357 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 380da3ba-2219-3064-bbfa-53aa08d78c44 | -3.14706 | -53.82394 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69b11845-fbbd-34a6-8d1a-95fec0030639 | -3.5105 | -54.53256 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08fa0d33-cd3e-3ef0-9047-da40b85ec793 | -3.86088 | -50.15342 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbfe9b21-955d-301d-bd5d-b5b5bdba13d7 | -2.37643 | -47.88302 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c054b624-0f54-352f-8a5b-bb220277d1ee | -2.83709 | -54.03579 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 729116c0-91fc-330b-ba7f-05b4acb7ae6b | -3.03216 | -53.03553 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53442766-12e5-33be-ae41-3285bfc88d3a | -4.07257 | -46.81992 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc4ad423-3ecd-3f5a-85b8-0d0e62a7bc9c | -2.58722 | -54.09675 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520b5fe0-0f2f-3ad2-b8ec-2edaf1499c8f | -2.86828 | -54.03345 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e9f7926-4387-35f8-a59d-0ede979ec472 | -3.46689 | -50.38018 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae9d6e5d-5f00-3107-8853-77f35f0b6f3d | -3.09259 | -53.29687 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92eae198-839d-347b-bfe9-e930597c6bef | -2.22532 | -51.43038 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94824e1b-5f06-3565-840f-f8e0c6a0e70a | -4.08189 | -47.02338 | 2024-11-30 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b7a33cd6-0030-3aa8-abae-f29b5b8fe104 | -1.2352 | -51.80413 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 227265dc-434c-37eb-b2e1-594ce7724ae6 | -3.2461 | -53.92597 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c8c542cc-8311-3614-968c-ed318b00feda | -1.74408 | -52.65534 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa6efaa0-a217-3e8d-9bbe-bd4ae4fbdd58 | -2.44517 | -53.66495 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c8f7890-9854-3efb-947a-7291294910b9 | -0.98768 | -51.74723 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9f7f1cb-67ee-3714-b032-ca3672df62b6 | -1.25722 | -54.55228 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e0a9304-0279-37a7-8c83-78fdaddfaf32 | -2.71711 | -46.1239 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faed9f8f-ac6e-3447-ae99-c5236d6cf5b4 | -2.61107 | -54.07547 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e342c505-0628-329b-ae91-0e84328d029d | -3.22391 | -54.17817 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a665ccba-493e-3767-9184-d8900f299aef | 1.95432 | -55.11752 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 695485bb-2fe8-3edc-9d5b-4111636cd16c | -3.0865 | -49.21472 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28c0d692-7a8f-34d4-901f-c5b6bab305d8 | -2.72852 | -54.10504 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 841a1f6f-54c2-3955-9a48-f8dd7e8bbec9 | -3.3013 | -53.8368 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d6dd6e9-2222-32b4-9a8a-db3570aecbe4 | -1.25255 | -51.78636 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fa23eb0-64c6-38bc-8383-5818b42b5281 | -4.0451 | -46.86464 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3a6a9f0-4d70-39ab-a5de-9d856c37a6c5 | -3.72446 | -50.20839 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f254999-2b8b-3a95-b191-cfd025f9bca9 | -2.72518 | -54.10451 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd46d8f5-03ad-3178-85bc-62c553138c48 | -3.16455 | -53.64433 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9678df3b-7f99-36e2-a4cc-e6467783d819 | -3.81582 | -52.2478 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e13ef8b7-897b-3fef-bd36-c15bfeecb852 | -1.53 | -51.61811 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2285e98-3c75-33b6-80a1-761ebe05fc6a | -2.64972 | -46.5786 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73adae1c-ba20-34f5-ba46-3c7988ffdb28 | -3.09674 | -54.56091 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 804f5ff8-1304-325c-80f9-3f4e00bae7f3 | -3.63702 | -51.02143 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ad30787-3f65-3241-9cc8-11b097ee5e24 | -3.48808 | -50.21114 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69ba7c16-b653-3ce7-bc00-7c087a872097 | -3.09985 | -50.35779 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3f54bf8-05fc-3eab-9bb9-43f308029a26 | -1.39006 | -53.64347 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1edf4b28-2976-33b2-aa7e-890aaa3d6b80 | -2.75302 | -54.12314 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d398cb3-2009-3aa3-881c-923cae0034dd | -1.17501 | -53.41517 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00e7bdac-ce1a-3ff8-bee2-cfe2ad3d7eac | -2.87155 | -53.99086 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77e5a256-5122-3659-9da2-80482fc65818 | -0.95596 | -53.20414 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49e1e979-5ad9-34e3-83a4-d4440073d2a6 | -3.99569 | -47.91364 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 708f2e44-6e7f-39d5-84de-772fa6df71c4 | -3.31646 | -50.02878 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 046bffdb-c1f9-3e08-8080-bcf55f6353a5 | -1.09299 | -53.38098 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a3ebcf-fa87-39cd-89de-92ac84f6839a | 0.9367 | -50.74636 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3265293f-d672-3d72-9c5c-e6f2437f8e21 | -3.01652 | -51.37097 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5071cf7d-0c90-3cf1-8656-3d8bbc7e5338 | -1.13987 | -53.70495 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad2b3cf7-b9ab-3bc0-bdc9-99603ae40c95 | -3.05461 | -54.05122 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8cb2209-65e0-3da9-8f7b-b6d4bed0631f | -3.11916 | -53.10526 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d39387c-dc45-3423-ae35-dae1e6037a23 | 1.28609 | -55.91364 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63a1d61b-d95d-3b81-afb1-53e3a7660dd3 | -3.45794 | -54.56348 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dbb02439-31ff-3bd9-862a-c7f4307be480 | -1.44463 | -54.52145 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 292479e3-67aa-341b-9131-6b5ad97aee46 | -3.67959 | -54.27378 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368a4df3-0d45-3ca0-9eae-208f800e64e5 | -2.75239 | -54.08372 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19427b2b-339b-30a2-8427-df911f820375 | -2.11894 | -50.34156 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f229700c-ad02-37e9-ac20-5511877b4998 | -1.65677 | -53.75247 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33f7293b-c8ae-35f4-a2d4-778102acfbb1 | -2.01687 | -52.08347 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c57715fa-c809-3790-b675-254e8a2a563e | -1.31977 | -51.74633 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e514d9c-e49f-3129-8983-5bc5abd1152d | -3.08641 | -53.24716 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f71e4b6-d2fa-36c1-be47-d3344349daa5 | -3.59512 | -49.9682 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9522054b-e644-39f3-afa6-f2fa252ab79d | -3.49582 | -53.80077 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README79.md)
