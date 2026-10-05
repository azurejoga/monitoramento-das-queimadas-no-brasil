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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a4f5197-1d3c-3aa1-a947-2378c3050da5 | -6.7199 | -44.2771 | 2026-10-05 20:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 66b7f139-5f27-3fee-9f43-a88a4a088250 | -10.2563 | -68.2673 | 2026-10-05 20:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 51e8d642-4751-3ea1-8dfd-921a4ec7cbac | -6.8764 | -43.685 | 2026-10-05 20:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2edb0bd5-ea5e-3f71-a389-8f170424eaaa | -9.3431 | -64.7143 | 2026-10-05 20:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 7fc356b8-1847-3356-86f0-1564fbe188c3 | -5.8509 | -45.0318 | 2026-10-05 20:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 271d96e2-53fe-3815-b30f-abb33264d40f | -9.0892 | -67.685 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 455c2a19-34c9-3113-97f0-ca4cb588af50 | -2.5353 | -65.8819 | 2026-10-05 20:30:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 5b7851c4-d51e-3a1d-a5d9-ec2634aeaa28 | -8.2674 | -71.1398 | 2026-10-05 20:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0ea710ce-d5b3-3bed-8d31-8ebe2251f790 | -7.3641 | -72.4622 | 2026-10-05 20:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 164.8 |
| a370278f-5fca-3a1d-90a9-2ad911a45166 | -8.6155 | -72.7453 | 2026-10-05 20:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 799546cb-0dac-30f9-bb07-83b843b637a7 | -9.0892 | -67.6665 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 176.5 |
| a09b254b-d9c0-3e0d-ad85-3f8d2d963b99 | -8.9257 | -66.8549 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| e0f49ec4-a59e-343a-ab15-20e98be2bd02 | -6.2558 | -43.7851 | 2026-10-05 20:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 209.0 |
| ec717ebe-e7ea-39e9-a96e-5d9bf4444994 | -8.7691 | -69.5368 | 2026-10-05 20:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 88.6 |
| f2a564a4-5275-3c08-8c6b-50b0b7208535 | -5.828 | -43.4243 | 2026-10-05 20:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 357.3 |
| 38b8d2a1-9f88-348f-b86f-38c483dd9532 | -4.4657 | -42.8877 | 2026-10-05 20:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6f91cfd5-8f5c-3169-aafb-3a5eb07ac090 | -6.2372 | -43.7634 | 2026-10-05 20:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 63ed10fc-84e6-3fca-9255-37f155e87d40 | -8.5971 | -72.7454 | 2026-10-05 20:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 97.1 |
| b408f536-aaa3-3fe1-b0f1-a0b957ab3388 | -9.7312 | -65.0944 | 2026-10-05 20:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 88f0ea9e-b919-3870-8ab9-297ff62dee40 | -8.8265 | -64.2258 | 2026-10-05 20:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 6e8f4b99-4cf2-3aa2-b0bd-5e5dffa35e8b | -9.1426 | -68.2941 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 56a2d977-e1ec-352e-8ca5-03a5fad5bc3e | -9.0429 | -65.4361 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 3d2bf1c5-1e2e-3b02-88f0-f051c656fcb9 | -9.1076 | -67.703 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 46d39e3c-a172-3bb2-9513-0db3eb952b87 | -7.2349 | -45.2599 | 2026-10-05 20:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 2a927ff9-06d5-35f9-bf24-37d8d51829fb | -5.7905 | -43.4272 | 2026-10-05 20:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8f85c5a6-a526-3e48-a387-a2f3dfad6c76 | -5.5066 | -43.7503 | 2026-10-05 20:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 98198d06-6ad4-364b-b4ce-6e3e4ab936b0 | -8.6483 | -66.8437 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 0e39a802-e006-3c79-9d7d-663da95074db | -7.8232 | -72.8418 | 2026-10-05 20:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 323.6 |
| 180e7dd2-0e28-39b6-875b-ee246ef00839 | -6.914 | -43.6816 | 2026-10-05 20:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a6bee310-ab61-30f9-bc62-30b142c4ff38 | -5.3258 | -45.2494 | 2026-10-05 20:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ae84f4e5-8ddc-3422-ada3-24ce335f23f4 | -8.593 | -66.8081 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.9 |
| ac56b7d4-69c7-3391-934f-6d2b3cc07de2 | -9.7126 | -65.0951 | 2026-10-05 20:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 140.9 |
| a90223a1-a477-3bbd-8c86-2db8b2b1d955 | -9.1611 | -68.2937 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 45dd1e4c-ae2c-39a4-b960-7e4170aa5e72 | -7.2537 | -45.2582 | 2026-10-05 20:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 9b9b66dc-8d68-340a-bc1b-5d0d7995ca64 | -8.6155 | -72.727 | 2026-10-05 20:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 140.6 |
| f6e8435c-5298-3ebf-8a9f-6c83ed8cee11 | -7.8233 | -72.8236 | 2026-10-05 20:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 258.6 |
| 2ef18aae-537b-395a-be28-b15ea70c0ba2 | -9.6858 | -66.8335 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2d95ce8b-3951-377e-9e42-6fc885839d6d | -7.4368 | -73.4448 | 2026-10-05 20:30:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ee1f59a1-237b-3a82-b102-c14b1ee74c59 | -9.1443 | -67.8132 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 70579a49-9ddb-3bf2-8e7b-38675601d728 | -7.8232 | -72.9329 | 2026-10-05 20:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 65e8e779-a8bc-3191-a1d9-0bff7d781c81 | -9.1077 | -67.6845 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| b354a188-d004-33bf-aa04-4e81e219876f | -8.852 | -66.7827 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 55c0b292-634a-3f4a-b167-6f6873d99d79 | -5.8092 | -43.4258 | 2026-10-05 20:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 289.9 |
| 8f7e340d-c89e-334b-a7ec-73d2cf4f2667 | -6.6871 | -43.818 | 2026-10-05 20:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 7bec6933-989f-3533-a27c-b3d63bf24783 | -6.237 | -43.7866 | 2026-10-05 20:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 97436195-2a45-30e5-8701-5993344a7a42 | -9.6859 | -66.8149 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 49daaee6-3ab5-3efe-a050-e97e12e4d4ab | -9.3259 | -68.8811 | 2026-10-05 20:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f1fb9280-fdce-393b-b6d9-00e4e660593e | -7.4184 | -73.4449 | 2026-10-05 20:30:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c1da6987-64fa-3f67-ad54-524a75b58bff | -5.8323 | -45.0105 | 2026-10-05 20:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 71e2971d-98b8-38d8-a450-cf848f40653e | -4.6873 | -43.2714 | 2026-10-05 20:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 74a6015a-a247-3b3a-8390-9f7e7f8aea1f | -6.1894 | -44.8472 | 2026-10-05 20:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7a10e26c-1305-3f78-b2ed-79b26ababdf7 | -8.5183 | -67.0139 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| e574f7c2-0b48-3a22-8d38-ec6a04c55a13 | -8.5929 | -66.8266 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 5dbf23f8-519f-3488-8c4c-425540cb0398 | 2.4769 | -50.8294 | 2026-10-05 20:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9a95d64b-cb12-35e4-b1e9-f614332d7a6d | -9.5425 | -65.6815 | 2026-10-05 20:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 117.9 |
| cc7d0624-a946-3dc7-a512-2414d4526f7d | -7.8049 | -72.8237 | 2026-10-05 20:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 161.5 |
| a8e133f2-3e54-30d4-95d2-c74209bfe2c4 | -5.8321 | -45.0332 | 2026-10-05 20:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| fd56c0d5-660e-30f9-9ab6-25951f224722 | -9.1055 | -68.3319 | 2026-10-05 20:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| b2647654-83ee-39d0-b9e3-edcf8603a0f5 | -7.8416 | -72.8417 | 2026-10-05 20:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0dd83bef-b94d-3c46-b753-7bb115496472 | -9.7313 | -65.0757 | 2026-10-05 20:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 7beccbbb-dbf3-350e-b94f-d63a5de320a4 | 2.4585 | -50.8299 | 2026-10-05 20:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 712a02b6-6fb5-3a5f-9a87-95fb5e1be359 | -9.6673 | -66.8154 | 2026-10-05 20:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 34168d01-3040-31cc-9bad-cf7225a2a0cb | -4.706 | -43.2703 | 2026-10-05 20:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 96e91b9e-d0a1-3d84-8b5c-760b653a3128 | -4.4342 | -47.5857 | 2026-10-05 20:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| fb48bdf1-bbdd-3136-bfc7-f490c8a76276 | -8.7875 | -69.5365 | 2026-10-05 20:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 00aaa5c2-2b83-3b1d-be44-62f4ddd7e332 | -5.8511 | -45.0091 | 2026-10-05 20:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2f3735dd-f866-3588-a72a-4444008ffce6 | -10.2827 | -60.5432 | 2026-10-05 20:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 0c6d893a-419d-3b1e-872d-d3a6c6003873 | -6.4732 | -42.7142 | 2026-10-05 20:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 185684e1-6bb2-32b3-bc0c-4c00f3ab5b13 | -13.5197 | -61.1319 | 2026-10-05 20:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 774cbe1e-58f8-3ea5-b0c7-4b030ed01e81 | -7.8232 | -72.8418 | 2026-10-05 20:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 531.7 |
| 651bcfcb-3552-3a28-afaa-5a25e32122f6 | -9.6673 | -66.8154 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d472fa96-9179-3f89-aa43-8e4c6ab715f9 | -6.0893 | -43.5433 | 2026-10-05 20:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 15981ab8-4d9b-34bb-a397-a64bfbaafc96 | -9.1542 | -65.4138 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 8ed0faa5-1b90-38ac-8d07-903a1294771f | -8.9688 | -65.4385 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 36917d1e-c3e0-3744-a7f0-459f43ada2cb | -5.8323 | -45.0105 | 2026-10-05 20:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0012fe89-3975-323b-8241-a2b6864f0767 | -4.4342 | -47.5857 | 2026-10-05 20:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 1be0bc0b-eb87-36b9-bf4b-3323afaaa72d | -5.8092 | -43.4258 | 2026-10-05 20:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 285.5 |
| 211fd0db-3bfb-3503-899a-b0ddd91ea22d | -8.8265 | -64.2258 | 2026-10-05 20:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 5e09a915-c477-3de9-a645-c6ae05a81f80 | -9.1244 | -68.2021 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 66bc4ed7-6f3d-3893-8dcc-cf6f273c271a | -9.7312 | -65.0944 | 2026-10-05 20:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.6 |
| d1acc3ca-16fc-35ed-b775-5a9ad0e0da83 | -7.8416 | -72.9328 | 2026-10-05 20:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 76.6 |
| b57a6ebb-f3f9-367a-8e34-5d1f9bfc66ad | -5.8282 | -43.401 | 2026-10-05 20:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 15e4aeb9-f09f-32fe-b0eb-8f84604a1d01 | -9.3259 | -68.8811 | 2026-10-05 20:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 77b9b31b-607c-384c-8d0c-5636a34bdcfb | 2.4769 | -50.8294 | 2026-10-05 20:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b8297481-168e-3c05-ab98-4d532fc8d6c3 | -8.6483 | -66.8623 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 70da54c9-50e0-3c6e-8a53-00a8b4e1e908 | -10.444 | -67.8908 | 2026-10-05 20:40:00 | GOES-19 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 71.8 |
| dc024878-a041-37f2-8eda-619912965dee | -7.8233 | -72.8236 | 2026-10-05 20:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 446.9 |
| e5585dc4-c5ee-33e5-ae00-43cc60804f3e | -8.5971 | -72.7271 | 2026-10-05 20:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 284.2 |
| 2e59f317-e067-34c0-8131-a8b946a8ac5c | -9.1613 | -68.2383 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b3f4dba2-96d7-31d6-80f6-93d68744b4d8 | -9.1055 | -68.3135 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 26cccc09-bd35-37f7-9c85-d1813f377f25 | -8.9873 | -65.4379 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 465bd084-5e67-3c50-9273-aceedae07c44 | -5.7789 | -42.6546 | 2026-10-05 20:40:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 5f203868-d2bb-3139-8386-d45511aaa967 | -8.6214 | -69.5026 | 2026-10-05 20:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 1b216d6d-9cb1-39ef-845e-fd9e9c8c2cd2 | -8.9257 | -66.8549 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0c088565-0f92-3b95-bd03-b74d0a93b50d | -6.1459 | -43.5154 | 2026-10-05 20:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d4b088fa-5f25-3524-8c99-ae9eb1ec9301 | -9.1078 | -67.666 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 24e0fa5f-1d5a-3601-bf8b-c04c1679422c | -9.1076 | -67.703 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 806538d9-51ac-3fdd-b459-8124573652a9 | -8.6155 | -72.7453 | 2026-10-05 20:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 75a51696-abd9-31fd-8bfd-6b20bf700f4b | -7.4184 | -73.4449 | 2026-10-05 20:40:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7a0b86b0-4848-36ed-b348-0ee2d1ca9aae | -6.6681 | -43.8428 | 2026-10-05 20:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |


[Clique aqui para ver as próximas entradas](README173.md)
