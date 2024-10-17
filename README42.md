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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| addc8d7e-3325-3d5a-ba83-fb111e19f77f | -3.76898 | -52.07173 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37c35645-8e89-3e9f-ab98-ef1982f35676 | -3.76835 | -52.07585 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fbf879b-607f-3316-8ceb-29ac91213f86 | -3.76011 | -52.05769 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dbe4e10-6756-367a-98a9-166be9a456dc | -3.75948 | -52.06183 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4e3d043-1318-3690-a9af-8dce2b20fef0 | -3.7533 | -51.93334 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 252921e5-142e-3fe1-bc33-f30160786204 | -3.74969 | -51.93275 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe185a41-db7a-34ff-9161-2968c174e46a | -3.74905 | -51.93692 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ac42c6a-d42b-30f1-8b7d-165dc6cb4d19 | -3.68993 | -51.27339 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6777c097-ce6f-36c8-b5a0-fe5907f3ba09 | -3.68618 | -51.27285 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 252d12c8-9f33-3393-8dc1-e97178665ccf | -3.66882 | -52.11181 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fec43c6-c5bf-3868-a20b-f327aacfa231 | -3.77018 | -52.20595 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d35938-ad18-343c-b131-5ba0cd9ca2ef | -4.16685 | -51.04137 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97cac587-9310-37bd-8179-2c37fbcc6b8a | -3.88746 | -51.15004 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b09684e-4e41-31f6-a2bd-217cf244a17e | -3.88676 | -51.15462 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4257052f-d238-3b90-8188-32b1a45c4809 | -3.883 | -51.1539 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65f0493c-b6a6-3074-b3ba-eef0b42046a6 | -3.88232 | -51.15838 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dec5f9e5-1472-3247-8de3-d2ec67641aa8 | -3.85298 | -51.0224 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0781f92d-0197-3cb3-bed4-887224e3ca98 | -3.81684 | -51.15554 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 842ddead-e748-3fdf-918f-e6ccb2a98ae7 | -3.79026 | -51.12688 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17627c26-b44c-3296-a172-7bfbf342d15f | -3.78647 | -51.1263 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3e84a61-f273-3671-a0d6-6af92c5cc482 | -3.78576 | -51.13095 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d2f8b0d-0d51-38d0-bd14-335cb9b2a46a | -3.70423 | -51.05501 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36443355-2e8c-37fa-892d-4bee00b9647b | -3.70351 | -51.05968 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7eee9563-d424-3e14-a6b6-4a195f5170ea | -3.7028 | -51.06433 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 869da7b1-fdaa-3d6c-ae5d-f25a3d1e3b56 | -3.70114 | -51.04976 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf0dccb3-8b0b-3c46-b30d-8a7d3c41d145 | -3.70067 | -51.07822 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ceec1b2d-be7f-3f0d-8528-0b3d92c38bc1 | -3.70043 | -51.05443 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33372965-5b9e-308a-bd61-cea0c6b9b466 | -3.69971 | -51.0591 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 020f96a3-4f35-3746-9e89-60975206afb0 | -3.67665 | -51.03179 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee7651af-acae-3e2f-b784-ddda59351494 | -0.60673 | -52.12157 | 2024-10-17 05:04:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff431778-7f43-3a98-bd29-b8500730e7f3 | -2.2136 | -51.95713 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c59328b-4495-3c2b-ba4d-6304817584a6 | -2.0056 | -52.10657 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1a4bc49-aa92-320a-9228-1f9a1bf41853 | -2.00208 | -52.10602 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 016473e5-d8d8-35a7-a2bf-e27dd6da9d13 | -2.03967 | -52.40488 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d359fbe8-565e-3c19-8752-77f8b6aec07c | -1.97282 | -52.90511 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c1f674c-384e-3a1d-9837-58df23ab2aa8 | -1.71323 | -52.6997 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc90e1de-683b-3f8b-9fa4-ce9690690955 | -1.71097 | -52.69175 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0723b1c-dc3b-3b4c-ae50-115b56c7e6e7 | -1.71083 | -52.53475 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aadee7c0-4d62-399b-a8e9-e22bcdc2241f | -1.70981 | -52.69918 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d7bfd5d-c1e5-35b0-9104-7b3f245a5b3e | -1.70696 | -52.69493 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49bc048d-5839-3485-8d7b-5d2cf89f91e2 | -1.7047 | -52.68697 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 730dbe5f-a5ee-367c-85a5-b4de6b217c32 | -1.70127 | -52.68644 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f3d18fc-f975-3f04-a17b-37c7bca90426 | -1.43149 | -52.8865 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96582744-7e90-3795-beae-421bf06f9b22 | -1.34501 | -52.38399 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a801ee9-1df6-3282-acca-d1210ff1c6c1 | -1.34442 | -52.38777 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 165582ad-45f8-3282-9efb-08ed594dbb26 | -1.07204 | -53.00936 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d15b16-bd99-3622-8834-22a91e60e89f | -0.97906 | -52.45575 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e880f103-cb4b-3129-8aea-dbee7eb571b6 | -2.01435 | -53.31564 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8095e22-2208-3c30-8eae-b140c2451312 | -2.78228 | -52.10132 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4616474-fe42-3d15-9e04-ace8bf89540b | -2.77935 | -52.09677 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30103c67-d7ae-332c-94f4-b46d26965598 | -2.77873 | -52.10078 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 254ca156-5641-369f-bfee-8ccad94f0445 | -2.77811 | -52.10479 | 2024-10-17 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de93c632-da1e-3418-9d4c-317f8fb59d13 | -3.35373 | -53.21217 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fba82e76-9bd6-3739-9fe9-45a92f1eb79a | -3.35315 | -53.21587 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23bf500-bf61-3f9d-a679-bda6061f2e35 | -3.35032 | -53.21168 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8878988d-114b-3cd1-986b-b208123ff8f5 | -3.34974 | -53.21537 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ef75e5c-9685-3bfd-8276-60a30bc2083b | -3.34634 | -53.21486 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dadc8d25-bc1a-3294-926d-c4a86e20083d | -3.21349 | -53.37042 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adb97438-97d5-36aa-a9d1-4ccfe8ea1308 | -3.1434 | -53.16508 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 342a89b4-1d42-366d-8728-f34ffcd5dbbf | -2.91761 | -53.21748 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47049b3d-9114-3d17-b5ac-ecca796de0cc | -2.84599 | -53.32178 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b51bf900-6ae8-3194-993e-2c3e8eb2e1f4 | -2.09221 | -53.40475 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 946b5fcd-72ee-358b-bfe3-503e4c0273ef | -2.08885 | -53.40423 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2f57ec4-f13d-338c-8a76-3ed3b9c17186 | -2.0883 | -53.40779 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 085c8bce-e9e0-31b6-9b06-5b1b0aa9c850 | -3.63795 | -52.24023 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc1d646a-75b7-3c5d-91bf-1df9fff71491 | -3.21255 | -52.46254 | 2024-10-17 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 376568a6-ad6a-3e61-9015-3fb062d204b3 | -3.10444 | -53.05364 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71434cdc-f044-3f15-9281-c9624402c8b0 | -3.10393 | -53.03455 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 962fe1f8-7439-3d8c-b171-d3388a37f64a | -3.1016 | -53.0494 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef8de3b0-9507-3983-8bcf-1702262acf9a | -3.09993 | -53.03774 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65f3a44d-bb09-3904-b80c-f3fe1bee458d | -3.09876 | -53.04516 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e1d35a-bfa2-3ec4-8548-5c03c9e49f49 | -3.03549 | -53.04686 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28e60d23-24f3-3e5f-97c5-9c7ca2401692 | -2.79414 | -52.92707 | 2024-10-17 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01c8ea82-48b0-303e-b3a1-7ddf4ca25b25 | -3.90654 | -52.37737 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34f353d0-241e-3824-b70c-327a4bb55940 | -3.90592 | -52.38144 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4a2a87c-3158-34ea-8e98-39c0825a142c | -3.89701 | -52.3923 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66e1e197-ac8d-3780-b96f-565e3e0bea6f | -3.8964 | -52.39631 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d07c8fa4-7c3b-3826-ae86-fcd56c832275 | -3.79592 | -52.29548 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3056312f-4361-3873-9d69-5c76e3618e3e | -3.78768 | -52.27781 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39a85a61-1268-3cab-bc46-d6437d0a7585 | -3.7771 | -52.39539 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75fee2bb-93ca-3c0d-981c-db69ed28b22d | -3.7765 | -52.39933 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c13cdb1-80f1-3ae9-ac8e-566d3f54a336 | -3.77357 | -52.39474 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd1dd442-8c20-3169-872c-20f98b94887a | -3.77297 | -52.3987 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b334c7f-4847-3bf2-a9bf-bfbac4d60a1b | -3.7455 | -52.31783 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5561e3fb-ce1b-3a7c-a489-9f67463bec82 | -3.74488 | -52.32184 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b47aa94c-4406-358e-a2db-4b2bec0100cc | -4.1082 | -53.50585 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29b8fb24-9b5c-3946-952d-a4a42465907d | -3.739 | -53.73429 | 2024-10-17 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e55cec20-79aa-3cc5-954f-0f2840ec7777 | -3.59551 | -53.53563 | 2024-10-17 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b89ca3ce-e528-36d5-93fb-f6db22c567de | -3.58468 | -53.47097 | 2024-10-17 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78d94718-d377-3185-b63b-723929a15e7f | -3.5834 | -53.26955 | 2024-10-17 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fce72767-9001-3e85-9ecf-983708ae83e7 | -3.5832 | -53.47115 | 2024-10-17 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc60811e-61e4-331a-ae44-7dd67c9b2245 | -6.23668 | -53.32836 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e813e838-a591-33f9-87ba-693d406b5fec | -2.21283 | -53.65915 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47173573-bde6-3161-8eaa-65550e08bbd3 | -2.20615 | -53.65811 | 2024-10-17 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 910e30fd-9add-3e4e-b5d3-d705db5e0db1 | -1.95294 | -54.07919 | 2024-10-17 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92dfefeb-58a1-38b4-90da-d007d58cfd28 | -1.95017 | -54.07524 | 2024-10-17 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abe8fc44-364d-37c3-be24-6bc2f9e6409c | -1.42573 | -53.46876 | 2024-10-17 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 468f90d2-5a0e-381d-8af5-f469d8fe5cd7 | -1.13899 | -54.1707 | 2024-10-17 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cbefc4c0-896c-33b9-80a2-db2887a037ec | -1.13845 | -54.17414 | 2024-10-17 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ee6215e-134a-3f05-bb58-ebf00dff9139 | -1.13569 | -54.17019 | 2024-10-17 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README43.md)
