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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03dfe2e9-4cef-3bca-973b-be91e80041ef | -1.52763 | -47.20128 | 2024-10-28 00:52:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7cb624bf-52f5-32ac-b97b-f61f6edd391a | -1.40802 | -54.07858 | 2024-10-28 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 6ed004e2-b945-33e9-b77e-58cfe29ec0bb | -1.30219 | -55.73302 | 2024-10-28 00:52:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| a33f782c-11cc-30f5-9cf8-264e4621bd59 | -1.2907 | -55.72778 | 2024-10-28 00:52:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 4842586e-8114-387e-bf5e-4d068ca82f41 | -1.2733 | -54.13742 | 2024-10-28 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| f560f0a3-b72a-3f8a-8bab-e2658938c33f | -1.18949 | -53.51852 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| a2f5ddde-03d8-309a-a2c1-09a7107216f6 | -1.1872 | -53.50165 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| e3e97f61-f792-3799-9aa8-5ece6d57e117 | -1.1814 | -53.50878 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a49813ad-13cf-3e17-9661-901434b889ce | -1.17907 | -53.49242 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e490c04a-0f5f-319e-ac54-92d55e15ce73 | -1.17758 | -53.5203 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 937845b2-3f3e-374c-ab47-e05a79337809 | -1.17526 | -53.50304 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| c14e0d1f-cea2-397d-aea1-20bd778c871c | -1.16953 | -53.51066 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 27bb4d7c-ba1e-3b06-ac31-7ad309869a4b | -1.16714 | -53.4938 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 671889e2-7c49-396b-b439-2343138945a3 | -1.15053 | -52.00224 | 2024-10-28 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 09e4a32c-0867-3710-af8d-56030a3aa8be | -1.09142 | -47.24776 | 2024-10-28 00:52:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f9d3a841-46a1-3d03-a95b-9ebc78ce31fb | -1.09017 | -47.23883 | 2024-10-28 00:52:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| dbff8d77-a1d5-3de1-addc-a6d151ac9ce7 | -1.08892 | -47.22989 | 2024-10-28 00:52:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b240a023-a18b-3cf0-9211-59a34b3ef8b8 | -1.07524 | -53.66585 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 96ff5a10-66d2-39ee-9fda-224b1e10b467 | -1.08732 | -53.66444 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| fa95de08-ec02-36aa-9748-0935de6c9a27 | -1.05762 | -48.26244 | 2024-10-28 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4ed2ddd4-6374-359b-87a6-5c3b11c95238 | -1.05639 | -48.25366 | 2024-10-28 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 40d1204f-9b4b-3b10-8883-e83ec94e8f57 | -0.99076 | -53.71801 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 65a6e3f3-318e-34eb-8b70-03ad37c0b6c0 | -0.98837 | -53.701 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| abcc60fd-5fdd-33e6-868b-892cdf0660fc | -0.97859 | -53.71899 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ff7bfa33-8206-3647-ae76-b72cb0aa74ae | -0.97629 | -53.7025 | 2024-10-28 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1820670d-6ee6-38dc-be5c-b263e53ed851 | -0.66451 | -49.54256 | 2024-10-28 00:52:00 | TERRA_M-M | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ace69db6-1a20-368a-b8c1-056ecee6412e | -0.25662 | -48.72664 | 2024-10-28 00:52:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82923903-5c15-389e-8872-2c704d2038b3 | -0.24106 | -48.95174 | 2024-10-28 00:52:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b36c64a-bfbe-39ca-b889-65d52ac96b63 | -0.23981 | -48.94284 | 2024-10-28 00:52:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37b1b5d3-1cf3-36e4-8c69-87e5beaaf365 | -1.1836 | -53.5158 | 2024-10-28 00:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| eba763c5-d6b4-3841-ae3a-1858515603fb | -1.1836 | -53.4956 | 2024-10-28 00:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 209f0067-93b3-3ba9-a68d-503d2375f306 | -1.5349 | -52.0874 | 2024-10-28 00:55:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6a404d78-b148-3a86-ad48-fb9d03edb249 | -1.5532 | -52.1076 | 2024-10-28 00:55:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 114eae56-ac0d-3da2-9682-9fa42f76fe06 | -1.5533 | -52.0871 | 2024-10-28 00:55:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6a2b2ac4-bf05-30c6-a147-8c7b2fd574ea | -2.0499 | -52.0791 | 2024-10-28 00:55:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c06d4804-aaf7-3026-ad29-a73a36677ec1 | -2.2662 | -53.8027 | 2024-10-28 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| ed52ff9c-add0-3028-81aa-22876ab65671 | -2.2662 | -53.7825 | 2024-10-28 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 244.3 |
| 7d0427a0-3a8b-368f-b84c-e68cc0e3974c | -2.2663 | -53.7624 | 2024-10-28 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e9c006f7-03b4-3ab6-b905-34b09a565cac | -2.2845 | -53.8023 | 2024-10-28 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 7e137946-b2a8-3866-91f5-d9ec99b18569 | -2.2846 | -53.7822 | 2024-10-28 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 319.5 |
| 8fa68ea7-3b1f-3777-a6b3-91d09191ff80 | -2.2846 | -53.762 | 2024-10-28 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 875aadb8-10ab-3760-9352-f939d670097c | -2.3919 | -48.5484 | 2024-10-28 00:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d12a300c-6bc8-3173-b2c8-70d31a024cca | -2.4104 | -48.5479 | 2024-10-28 00:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| c1990406-cf86-3ebc-82e9-3255618de5b7 | -2.5251 | -47.442 | 2024-10-28 00:55:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| dd437e5c-1480-3a64-87c9-5df6b567de08 | -2.5594 | -54.0181 | 2024-10-28 00:55:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7004c6c2-15aa-332f-8d92-8bf4f6f2ccc7 | -2.6398 | -51.758 | 2024-10-28 00:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| a4904e7e-0931-36b6-aa67-c7c164dd30d2 | -2.6399 | -51.7374 | 2024-10-28 00:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 991af923-c048-373a-80a1-58e50a906f81 | -2.6583 | -51.737 | 2024-10-28 00:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| e63af485-1399-3bc4-900a-a403ab1328ec | -2.7033 | -49.33 | 2024-10-28 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c05f7cf1-56e9-36ca-a704-b830e153eb20 | -2.7034 | -49.3088 | 2024-10-28 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| d190d610-d729-3b76-b679-d486bf10dae7 | -2.7219 | -49.3083 | 2024-10-28 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0b27a176-559b-38f2-b719-fc8f0f2354ab | -2.8054 | -51.8157 | 2024-10-28 00:55:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a356b07f-f87e-34f4-a998-0d05e0f973b7 | -2.8054 | -51.7951 | 2024-10-28 00:55:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 1c63c07e-91bf-3b5e-81e0-26e04b834790 | -2.8555 | -53.3459 | 2024-10-28 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 55b0178f-a2aa-3ad2-8b8c-b2ebed975cc2 | -2.8556 | -53.3256 | 2024-10-28 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 1c4e09f7-5fad-353c-87c9-9a2086ec9228 | -2.8739 | -53.3252 | 2024-10-28 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 7a4c8696-97a2-311b-938b-28babbddf64a | -3.0538 | -49.4895 | 2024-10-28 00:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 879b6fb6-3df4-3fce-9909-0c58e3fb6ec6 | -3.272 | -46.2072 | 2024-10-28 00:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 39b5e45a-f630-37eb-a659-6a44dbef748c | -3.4013 | -46.3353 | 2024-10-28 00:55:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e7920acc-ae12-36d0-b427-58396b10e135 | -3.4014 | -46.3131 | 2024-10-28 00:55:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 673daa48-3067-3b12-90eb-66973c24f69b | -3.6911 | -51.5622 | 2024-10-28 00:55:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8c98eda5-133d-3182-a2cb-0828f40d6f04 | -4.2797 | -45.5362 | 2024-10-28 00:55:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 538004bd-94a6-3e8b-87ee-2f316b240021 | -4.4093 | -45.6641 | 2024-10-28 00:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 07a541c6-95ae-3784-b1e5-6707bc31caea | -4.4094 | -45.6416 | 2024-10-28 00:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 195.7 |
| a37abe05-2731-3ca5-b021-f4f30200ec96 | -4.4279 | -45.6631 | 2024-10-28 00:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 2b5eca03-29ca-3f59-829d-3e89a619718c | -4.428 | -45.6406 | 2024-10-28 00:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 0413d04b-a26d-35c8-84f1-d758ffadd176 | -4.758 | -46.4033 | 2024-10-28 00:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7a0128fa-d04f-32c8-be74-9e2fd1c69687 | -4.7581 | -46.3811 | 2024-10-28 00:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 775247e4-a798-3636-a768-103b595ef28e | -4.7766 | -46.4022 | 2024-10-28 00:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b9034855-826d-39c2-953e-b14751609ecf | -4.7768 | -46.3801 | 2024-10-28 00:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a19465ac-cfa5-3f87-a62f-bc0d0984abeb | -15.3686 | -40.1745 | 2024-10-28 00:56:30 | GOES-16 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| 91c021f0-54fd-35b4-98a0-7355e3fa3021 | -1.1836 | -53.5158 | 2024-10-28 01:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 03396aec-025b-37a6-8182-b9aab1b13cf8 | -1.1836 | -53.4956 | 2024-10-28 01:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e6e13c24-0fd7-3816-96ba-02e79a6c5374 | -1.5349 | -52.1079 | 2024-10-28 01:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 65f03307-c601-3576-a976-7262db00fbc3 | -1.5349 | -52.0874 | 2024-10-28 01:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 09d8bcfa-391e-3d74-a804-cbbda253c093 | -1.5532 | -52.1076 | 2024-10-28 01:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0ed7d392-e650-394e-9d77-f78bc29e56cd | -1.5533 | -52.0871 | 2024-10-28 01:05:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8c9c13a8-fc79-3c01-a943-480444ec1729 | -2.2662 | -53.8027 | 2024-10-28 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5243cf7e-0c84-3a86-9662-f627999a746f | -2.2662 | -53.7825 | 2024-10-28 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| f476d103-5bde-36dc-9507-8a1ddd226098 | -2.2663 | -53.7624 | 2024-10-28 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 2246f281-3236-3d40-a8e4-71f4a058edab | -2.2845 | -53.8023 | 2024-10-28 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| da492377-fa9f-3a4e-a532-44677c2adfd6 | -2.2846 | -53.7822 | 2024-10-28 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 195.7 |
| 1f558d3a-69f4-3399-95d8-cf72bb571331 | -2.2846 | -53.762 | 2024-10-28 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 612b2450-6125-31e2-8863-1a62e6af8e65 | -2.3919 | -48.5484 | 2024-10-28 01:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b64dcee1-c6e8-3dcd-bec3-f2dbe0a6600c | -2.4104 | -48.5479 | 2024-10-28 01:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 16fdc6c0-73d9-3826-aa13-47f24147184a | -2.5127 | -51.1821 | 2024-10-28 01:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 36452271-4711-3378-a6a7-5aaee4f10da3 | -2.5251 | -47.442 | 2024-10-28 01:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e1718057-c9e8-3bee-8fc7-a6b94f3f745d | -2.5311 | -51.1816 | 2024-10-28 01:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 11d947f8-25f7-3911-b0b9-da0d8f7b967d | -2.5594 | -54.0181 | 2024-10-28 01:05:20 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 65517f34-24bd-3975-a891-aa35b8cdf8d4 | -2.7033 | -49.33 | 2024-10-28 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 368d32c4-1133-3e79-ac42-b50188c3bdcd | -2.7034 | -49.3088 | 2024-10-28 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 642b4504-d2bc-3055-a5ca-566915923dd6 | -2.7218 | -49.3295 | 2024-10-28 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 35a9ecfa-0d4e-3375-938e-d0c73a8a2362 | -2.7219 | -49.3083 | 2024-10-28 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 778afddf-b8a9-3ff2-ae94-2c4e35ec8a69 | -2.8555 | -53.3459 | 2024-10-28 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9c49114c-4017-3d4b-a636-128c15ed2d5c | -2.8556 | -53.3256 | 2024-10-28 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 58dc16c4-8bb0-36bb-a1a8-a339dca23ca4 | -2.9048 | -45.2594 | 2024-10-28 01:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| de5bd730-0392-344f-8ca3-4cb368581c4c | -3.0317 | -50.4176 | 2024-10-28 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7bca085a-3c73-315d-881f-2c3d5f5ad3cb | -3.0317 | -50.3967 | 2024-10-28 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| c7a60d80-a1f9-3e88-9c53-d7cda51e1484 | -3.0538 | -49.4895 | 2024-10-28 01:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| cca891c7-d092-313f-a31a-80c274154ede | -3.272 | -46.2072 | 2024-10-28 01:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |


[Clique aqui para ver as próximas entradas](README18.md)
