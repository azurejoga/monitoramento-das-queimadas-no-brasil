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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f5c1b0b-1e2d-3e44-89e7-9292d501ddd5 | -3.272 | -50.3263 | 2024-10-31 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7e53d4fa-2ae6-388c-b94e-e4b94458f017 | -3.2719 | -50.3473 | 2024-10-31 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3ed90659-73e0-3609-87d9-bfc1f6155b4f | -3.2535 | -50.3269 | 2024-10-31 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2b36b4e4-5481-352a-b2be-0ef735b1cfa3 | -3.2535 | -50.3479 | 2024-10-31 06:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c487f921-925a-3c7f-bc77-d0283beb5e28 | -1.0851 | -53.6562 | 2024-10-31 06:08:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd5e8806-2919-3bcc-a4e5-9a763d8ce646 | -0.87717 | -53.68068 | 2024-10-31 06:08:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5210328f-aed7-3d6e-8cce-07d23906c8a1 | -3.5017 | -55.41095 | 2024-10-31 06:08:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3143fa31-3609-322e-ab18-007cdba3e2ac | -2.20219 | -53.71779 | 2024-10-31 06:08:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eb1bbfb2-2258-3eb8-8366-9917d0e3b1b5 | -2.19224 | -53.71626 | 2024-10-31 06:08:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 79a288c8-78f7-3a54-a189-b62c765fbaeb | -2.11048 | -55.89862 | 2024-10-31 06:08:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7abaca4d-dfa2-3fa2-a9cf-0aee4fd86805 | -1.8406 | -52.1087 | 2024-10-31 06:08:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8333407d-665e-3f88-8cbe-c72e2c30fed5 | -1.83921 | -52.11636 | 2024-10-31 06:08:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bf76c5ce-750a-32fa-8263-2c9adb5fc6e0 | -1.83853 | -52.12319 | 2024-10-31 06:08:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2c19d0eb-38fb-3330-8f53-7f1040d4b1aa | -1.64429 | -52.5775 | 2024-10-31 06:08:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9a8f9508-6978-322d-a56b-b362f3be890c | -1.529 | -52.1128 | 2024-10-31 06:08:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d1aca429-d4b4-3ec6-9cd1-374bcf025039 | -1.43825 | -52.27246 | 2024-10-31 06:08:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| aa4280ae-4dc7-3a80-8537-967d082b166c | -1.43718 | -52.26551 | 2024-10-31 06:08:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0b6b67e4-7bb0-37b4-adaa-a63cbcddb5c8 | -1.39027 | -53.60281 | 2024-10-31 06:08:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| af7c9e5b-e7cd-3fc1-b944-589d0b9121e1 | -1.38856 | -53.61434 | 2024-10-31 06:08:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6e8a7d0c-a768-3049-a340-d320831f7fec | -1.08675 | -53.64496 | 2024-10-31 06:08:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 17214ba6-8705-31c8-8c55-d2d826634e63 | -0.69577 | -51.68324 | 2024-10-31 06:08:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 50f9a030-762c-309e-857f-493075b89d48 | -0.6966 | -51.678 | 2024-10-31 06:08:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ff9fa7e4-e97a-3172-8355-79b7905090c3 | -9.94955 | -68.62109 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6bd0036-1d86-3cfa-85f6-5ea1ceed1642 | -9.94581 | -68.62054 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 932dd7c8-1a93-3291-9f1c-7b1a8fbcf185 | -9.94517 | -68.62504 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28232dd1-1263-3e12-a616-aa3ca279f095 | -9.8622 | -68.96999 | 2024-10-31 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 742da5d2-d9f2-3fbe-9bc0-a97d6c25f8a0 | -9.78848 | -67.68059 | 2024-10-31 06:08:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 450aea74-1874-38b8-818f-10fd9625dc78 | -9.70683 | -66.97753 | 2024-10-31 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14c25930-aa60-37f4-b0ea-fe60b0b1a941 | -9.7063 | -66.98125 | 2024-10-31 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42c5ce1a-06aa-3023-a160-89af71585bb5 | -9.69912 | -66.97261 | 2024-10-31 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc4995e2-1dc7-3a6e-928a-b129b096437e | -9.67617 | -68.35414 | 2024-10-31 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d157d31-0db7-30a4-a39b-8850dd957364 | -9.65823 | -68.76477 | 2024-10-31 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04f6ef44-d460-3803-a54c-59db92dd4641 | -9.63937 | -67.24628 | 2024-10-31 06:08:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44097e85-a876-3956-98e6-959cfecd5ee3 | -9.63583 | -67.24214 | 2024-10-31 06:08:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14c08f77-38be-3472-a2ad-2ec97125650e | -9.63532 | -67.24571 | 2024-10-31 06:08:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bc14302-ee36-3948-94e0-09c86f9a4b1b | -9.63482 | -67.24926 | 2024-10-31 06:08:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 444686bb-e3bf-37e5-8c99-e83c0e04177f | -9.63178 | -67.24157 | 2024-10-31 06:08:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84fa1938-9386-3bd6-b4b2-d2d7e0505bff | -9.63127 | -67.24515 | 2024-10-31 06:08:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7acf2e6e-ba8e-3f60-ae9d-307f9f0c575d | -9.61168 | -68.56303 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d58cfb9-465f-3874-8a7d-3870a99d2376 | -9.59359 | -66.78172 | 2024-10-31 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8715b3f6-1bde-3596-8cac-d15aa6733dbd | -9.58329 | -65.98637 | 2024-10-31 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5e2b1aa-d969-37c0-83a9-505669cff5cc | -9.56239 | -63.13619 | 2024-10-31 06:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3cb035e-f91d-3254-933d-e9ce09606cd6 | -9.5575 | -63.13203 | 2024-10-31 06:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96f86954-b75d-3e2d-8994-55e560e2455d | -9.55705 | -63.13545 | 2024-10-31 06:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78b0da17-1525-3a9d-82c1-f4fb039202b9 | -9.50464 | -66.55608 | 2024-10-31 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7326e188-9636-3aff-999e-e393bbf4ef0b | -9.50409 | -66.56001 | 2024-10-31 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4211731a-cc82-37e4-97c9-c5d7d5eb2bc9 | -9.33772 | -68.77198 | 2024-10-31 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3465a759-1872-3e7f-87f6-d1e847ed4035 | -9.33708 | -68.77631 | 2024-10-31 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1394013-044e-367e-a739-42f464e7ebfe | -9.33067 | -65.68555 | 2024-10-31 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03df09c1-5e42-3a51-b551-ed4886e8013b | -9.28005 | -68.78094 | 2024-10-31 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4783ed09-bc4a-3b0c-b453-379a844f0096 | -9.25401 | -68.18727 | 2024-10-31 06:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caa88191-ce0a-3afe-a805-bbc9eb2b5e19 | -9.11842 | -68.43578 | 2024-10-31 06:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0861393-292b-34f2-ad3b-f1e9e81967ef | -9.00455 | -69.08929 | 2024-10-31 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c2ab143-6453-392a-b485-2eea18c6338c | -8.64459 | -70.13107 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eda73acc-8a96-3dc0-a808-8f3f92482b72 | -8.62664 | -69.71986 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9b8d7dd-2830-3067-a2d8-c0b3f2632473 | -8.62606 | -69.72372 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 406c2a62-2efd-3426-b4b4-7484bdb63553 | -8.62315 | -69.71933 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f1fbd74-f347-3c15-9fc4-64ee52b30aea | -8.62257 | -69.72318 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0adc41e-f0c1-3100-8f8f-cefc74e91a3b | -8.62199 | -69.72704 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15b740f2-7bd6-3bfa-94e2-0ab4003d6162 | -8.61792 | -69.73038 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0caf5ad-823f-3fc0-ac15-68b42194d5c1 | -8.49105 | -70.066 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 67316138-368a-34e5-9566-a859858aaa59 | -8.24066 | -71.07613 | 2024-10-31 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 018bc34e-2e5d-3c71-9d0a-24413fc00af6 | -8.11459 | -71.32352 | 2024-10-31 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 371ccd48-3cf4-3401-ab95-902268406ffb | -8.11126 | -71.32299 | 2024-10-31 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20257290-a4f3-3dbf-b658-6f2684fce25e | -8.07141 | -70.88322 | 2024-10-31 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2c30042-0286-38e4-b3dc-8b1df6b308e5 | -8.07086 | -70.88677 | 2024-10-31 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 040ca4fd-5fe3-3376-990d-e0a3dcb6d03a | -8.06806 | -70.8827 | 2024-10-31 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9235839-c256-3ed7-9ab2-a00a3a3fa695 | -8.02241 | -70.07265 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c4eaf1f-9394-34a0-9c60-db363462a252 | -7.84352 | -70.12605 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1344d5d6-c172-345c-bf09-3848d2437ced | -7.83954 | -70.12923 | 2024-10-31 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb005d37-de87-3d4b-a0cf-13d9984f8afa | -7.75284 | -72.28404 | 2024-10-31 06:08:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5eb4fd3-b85b-35f1-8d1c-356019bb0317 | -7.39355 | -72.65077 | 2024-10-31 06:08:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93634390-9113-3bdd-972a-ddc4969cca83 | -7.02857 | -71.79474 | 2024-10-31 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc3d15a5-7349-352c-a314-dd8f6a6a9b78 | -7.02525 | -71.79421 | 2024-10-31 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8306959a-187a-344b-b38c-999a3d78c4aa | -7.0247 | -71.79768 | 2024-10-31 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03a6ec35-35dd-3141-8d11-a17709758323 | -6.9032 | -71.51555 | 2024-10-31 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 944a9dd1-3ba7-3667-858e-f4cb25e0172f | -12.43513 | -63.27924 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f9782207-518a-3c5d-a93c-454b2a6fd0af | -12.43468 | -63.28287 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8bcd1639-91db-3e35-8f89-1a4a94716850 | -12.42962 | -63.27853 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3f0e3571-c215-3385-8d62-97dcd97e9de6 | -12.42917 | -63.28216 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 446f7e42-c926-3805-8b1f-dd7bb805c01f | -12.42456 | -63.2742 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68d257dc-2275-3f11-a6c3-738af1fa9262 | -12.42411 | -63.27782 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1590152e-0e1b-3b65-bcaa-bd863151e7c0 | -12.42367 | -63.28145 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c09790-1994-3081-b670-204b4144bfd8 | -12.4186 | -63.27711 | 2024-10-31 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01aa4680-4b51-33ec-b495-eb24b4d13b7c | -12.22787 | -64.20957 | 2024-10-31 06:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c6a39e4-c165-337b-9404-13c384735070 | -12.2227 | -64.20895 | 2024-10-31 06:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca5821ad-9931-316f-ad5e-3caff26ec971 | -11.10602 | -68.6861 | 2024-10-31 06:08:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2854dae3-1c12-3f8f-947c-140c47d4c9d9 | -10.94816 | -69.17019 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 074c5182-0371-3cd9-8159-e345a12c4e38 | -10.94094 | -68.36942 | 2024-10-31 06:08:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07a35645-79bb-3094-b74d-be1ab8dd6669 | -10.93834 | -68.37086 | 2024-10-31 06:08:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5b55a07-dbc4-3579-992d-881eb69126b6 | -10.91945 | -69.21642 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eb4c0cb-7622-3067-9ac9-42242a03ed19 | -10.91933 | -69.21453 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44d5c29f-5c7f-326a-a7ae-52d4eda60fde | -10.90988 | -68.89627 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db31f95-4231-3d1a-98a2-a08cf7fec143 | -10.90238 | -69.30602 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18fa6b39-aa84-3710-a53a-e229f397b7a1 | -10.89933 | -69.40107 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d148fb54-5f53-3cbc-9eca-14ae7dcb7fb2 | -10.89637 | -69.19538 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1df38192-d14e-38b2-a377-e67279d2f021 | -10.896 | -69.40321 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88b6acb8-94c0-30df-808d-82b192dec740 | -10.88971 | -69.39102 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9ce1bc6-5a90-31c4-bef0-d8ed61c09eb5 | -10.86482 | -69.533 | 2024-10-31 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f41638bb-145c-33de-b1a2-0e4025da6fdb | -10.78912 | -69.59792 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README52.md)
