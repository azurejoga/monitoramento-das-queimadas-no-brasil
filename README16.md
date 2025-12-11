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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37805387-12b0-3f8b-bbc9-ba18c34a0dca | -16.69748 | -44.96516 | 2025-12-11 04:42:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c808a657-b7da-3bbc-8355-34787f3f213c | -12.44336 | -63.63963 | 2025-12-11 04:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b45fc89-ac2c-32eb-9ba5-4b2c5e8274d5 | -22.9887 | -48.65651 | 2025-12-11 04:44:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3590bb4-9b78-3217-952c-ec1e8a1ee756 | -26.25527 | -48.55618 | 2025-12-11 04:44:00 | NOAA-20 | SÃO FRANCISCO DO SUL | SANTA CATARINA | Brasil | 4216206 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b3199f4f-e35d-3a58-a8ee-8bce84bdf7cd | -22.02876 | -56.3364 | 2025-12-11 04:44:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84f1f3c9-340d-3ad5-abab-0c49dcf66054 | -20.91528 | -56.3779 | 2025-12-11 04:44:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac0c025b-106f-334f-a8bc-e90b7b460875 | -21.00706 | -56.15562 | 2025-12-11 04:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53c48fdc-b843-346b-9b08-941992ef96f9 | -20.91802 | -56.38049 | 2025-12-11 04:44:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1baa76d-ed2d-38e5-a8d6-09d90596c7e2 | -18.71044 | -55.26406 | 2025-12-11 04:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| de715081-a776-34a3-85b7-4b16b5666fcd | -21.86582 | -56.14954 | 2025-12-11 04:44:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5de3fcb7-c14c-3fda-b79d-976b9c3d351c | -18.98033 | -55.3005 | 2025-12-11 04:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9bc14c32-8eb1-37c9-bb31-f6a0c4ad1083 | -22.04124 | -56.30775 | 2025-12-11 04:44:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ce80bae-1a9b-3d69-8a6f-2447e989084c | -22.02443 | -56.34004 | 2025-12-11 04:44:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 102da245-d099-3d2c-b1bd-244d319de78d | -2.2906 | -45.5933 | 2025-12-11 04:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3bb6bb85-7dd1-3f56-a091-5dbd3f630edc | -3.7589 | -45.4944 | 2025-12-11 04:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 107.6 |
| cbf5a51b-67d2-3d03-ac2c-bc16b9951e7e | -7.86422 | -38.70603 | 2025-12-11 04:59:00 | AQUA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 20.3 |
| acc8bd2c-634d-3da4-9b8c-e063c42cc878 | -2.2906 | -45.5933 | 2025-12-11 05:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 83fb1fde-a9ae-3a77-a6d1-2d70218f5e90 | -3.7589 | -45.4944 | 2025-12-11 05:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| f44c899a-5d51-350e-9fd1-3d557faf9826 | -3.7589 | -45.4944 | 2025-12-11 05:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| a7946f8c-fdef-3fe2-971c-b8cf50ca9996 | -2.2906 | -45.5933 | 2025-12-11 05:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 57d34434-4567-3cc6-890c-2848b10e3848 | -3.7403 | -45.4952 | 2025-12-11 05:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 87f8e252-35c2-3f10-93dd-26a043e1ff5d | -3.7589 | -45.4944 | 2025-12-11 05:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 5db232bf-c31e-3fd7-a985-64645f2422c0 | -3.48591 | -51.53342 | 2025-12-11 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 417c6fcf-ed0c-3a6a-bbfc-2f09189d8eed | -2.09133 | -52.11446 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8329a93-5a58-3b2d-8a33-55d909ef9729 | 0.31286 | -60.41624 | 2025-12-11 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e477a711-1d42-36cb-9e68-bb21741ec93f | -1.66876 | -54.57807 | 2025-12-11 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54dd828-9056-3d76-b415-2c0d270dbf19 | -2.26166 | -51.93359 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bfbbd5a-78fc-396e-b676-e00d78494923 | -2.88134 | -52.71733 | 2025-12-11 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb019aed-510d-33e4-9067-03922e2076e5 | -1.76049 | -54.18693 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d12d985-0869-3b2a-b7c7-e82b53eed5b8 | -3.48772 | -51.53955 | 2025-12-11 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8e10e9c-d6df-38f1-a0b3-065d34a9c0d7 | -2.88089 | -52.72026 | 2025-12-11 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59f104c-b7a3-3a2d-90c1-baeb5556fd72 | -2.02616 | -52.05095 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3b5588e-c621-31b3-9d82-c85709c0817b | -2.21484 | -51.89782 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec7a5b52-80ce-3621-9726-91d311768db0 | 2.878 | -60.26225 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aef02730-f736-3a27-961e-9c7439ab021a | 0.45699 | -60.42496 | 2025-12-11 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ca5b592d-4d19-3995-ab68-c6fd98b03e55 | 3.35668 | -59.99331 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fea76cb-2a25-38f0-9940-5693cb660b09 | -2.14987 | -53.75488 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ab770ca-11d3-31a1-b216-f8bd1729121f | -2.94231 | -53.02432 | 2025-12-11 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85e7b036-0f78-3e73-bfff-58ee8a835d89 | -1.49542 | -53.12921 | 2025-12-11 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82bb3ec7-0475-3ccb-ab97-59de24a81504 | -1.26975 | -54.10832 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d449ee34-71f3-3b44-b1ec-9940ce129aaa | -2.659 | -51.64575 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7daa9eb8-9d8d-3e05-a2b5-8efa6fd67b62 | -9.0971 | -62.33525 | 2025-12-11 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34622cad-286a-3573-81d0-3448a5e5a38b | -1.11501 | -53.68584 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5d24dfc-9add-37c8-85e7-4bac9223807c | -2.11403 | -59.32666 | 2025-12-11 05:29:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be17acea-854a-331c-820e-a01d8b2844ef | 3.12205 | -60.32217 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79276e3d-c0d4-3c33-83e5-e4da74ff9ee6 | -1.6643 | -54.57742 | 2025-12-11 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4309dfa5-a8f2-3df3-bd8c-082674ee639f | -2.26468 | -51.93378 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1667914f-4f84-397f-98a4-33908033aadb | -1.59052 | -53.75925 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 354ad172-597d-33cd-93a2-eefe4f13f437 | -2.02084 | -52.05004 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adc0b4d0-1842-353b-a947-b12943ed1f70 | -2.02466 | -52.04959 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11c7d844-3dae-3824-9673-fc997a96936d | 0.23791 | -60.61062 | 2025-12-11 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d198f195-ff65-377b-81af-c505c2818d25 | -1.74772 | -54.59912 | 2025-12-11 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15ce02b0-a1c8-38b0-95fa-5f3e38f5e37a | -1.48025 | -54.20498 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4813016-2166-3541-982e-c9528e8e0f96 | -1.01536 | -53.72454 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44fb5e6d-f049-3822-a339-3424ec24a2d5 | -1.80934 | -54.05334 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 245b8ffa-ee92-37d0-907f-4ae5e7e1203e | -3.48829 | -51.53572 | 2025-12-11 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e69f3ba-4f67-3b97-b720-a79b99042af7 | -2.92241 | -54.19645 | 2025-12-11 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea210a5-74f5-30b5-8f8b-576c51dc4e75 | -1.11894 | -53.6915 | 2025-12-11 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4635fb24-4fa5-3c1a-b54d-ee7dd8f0eff5 | -2.9368 | -53.02647 | 2025-12-11 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6a6df85-8e23-3c27-a732-d8edb22c796c | -2.47215 | -52.14844 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b712e1d-e6aa-3577-bb34-e6742e93d0cb | -2.21588 | -51.89089 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47c6978b-933f-3de2-9b6e-d3a5463a77a5 | -1.61735 | -54.71097 | 2025-12-11 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 719f852f-0de9-3d1f-a6bc-889ce42be5a9 | 1.12627 | -60.52752 | 2025-12-11 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59351241-3b49-3006-8e38-dcdd3c86a0fc | 4.06239 | -60.19903 | 2025-12-11 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cc306ac-d8d9-3c8d-a25f-f8f3f7fdc34d | 1.70799 | -56.02587 | 2025-12-11 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e81f370-c7d5-36f6-846f-6cc74bf254ca | -3.57825 | -52.1095 | 2025-12-11 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d910cbe8-1ccf-3901-9fc2-ce581f6f54de | -3.69981 | -50.94361 | 2025-12-11 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97ad4316-8bc9-370b-a2f9-9f3cb5d49292 | -1.05468 | -53.67106 | 2025-12-11 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f39100d-1227-3a4a-8eeb-1bba7dd85a06 | -2.47795 | -52.14617 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52f2567a-c05e-3976-8dfb-f375565cce37 | -0.64421 | -52.39421 | 2025-12-11 05:29:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f751c2b8-278b-3f22-bf44-bdf6f728efb7 | -2.56454 | -51.82534 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f310b86-eb4b-3825-9476-ea1846c97b49 | -2.69169 | -59.42474 | 2025-12-11 05:29:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcc8a1b2-963a-3cb5-9896-4852d63e759d | -3.70512 | -50.94854 | 2025-12-11 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1ccaae7-f624-3cb5-8206-af721593aec7 | -1.61682 | -54.71279 | 2025-12-11 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56582a84-c4a6-3790-b623-3b5aa11ad112 | 3.12151 | -60.31873 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdadc737-d781-3dd2-be97-8fd7fa7acbc9 | 3.11875 | -60.32268 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 792663ef-b678-38df-a85b-d7d701eacc5c | -2.77506 | -54.52601 | 2025-12-11 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca1698e5-7057-38d7-9b30-e6b0601f9fb3 | 3.02919 | -60.16498 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84293eef-912a-3ca5-a484-7383a1ffc5e6 | -2.77964 | -54.52657 | 2025-12-11 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce8f6bbb-ac71-3c02-ba29-185358a4954d | -1.48097 | -54.20036 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2dcaaf9a-5372-38a7-ab96-8b74cc9b4de2 | -2.65346 | -51.64491 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e22a238-8a0d-3577-b625-9066d8d90042 | -1.73843 | -60.93498 | 2025-12-11 05:29:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87e36500-7f57-3544-8bce-c0abcab9ddc9 | -2.69276 | -51.64733 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad9ebb63-5ad1-3e67-a597-79225eeaeffb | -1.80859 | -54.05817 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 87717bad-8c69-3c1d-a2c6-f7b1f54608f2 | -2.21536 | -51.89436 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82329609-55e1-3312-a46e-9f7952e0370a | 4.05909 | -60.19954 | 2025-12-11 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0bdfea8-581c-3e12-80df-efec22904b84 | -2.08438 | -52.05223 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbfe0e49-cf59-3cdf-bc99-811b371fdaa6 | -2.02669 | -52.04754 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26b73691-5a4d-336e-afaf-d35d805cce5a | -1.34928 | -54.60638 | 2025-12-11 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9143be9e-083b-335d-a465-0a80797186fe | -2.47166 | -52.15174 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ccc5c6-7bd2-3c11-9095-fae190afd2c9 | 3.02865 | -60.16154 | 2025-12-11 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 999132c6-a27b-3e32-8427-f1b94755e8ad | -2.41325 | -56.01643 | 2025-12-11 05:29:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd48cab9-1ec2-36e2-8917-0aac361a91e5 | -3.48537 | -51.53725 | 2025-12-11 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 293a316f-4697-372e-869c-3bad887ce32c | -2.07904 | -52.05141 | 2025-12-11 05:29:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfaa93c4-dbb4-38f0-9a86-039f543a7132 | -3.70096 | -50.94527 | 2025-12-11 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5161a20b-c4dd-35dc-a287-054bb8f8a2a9 | -3.84393 | -47.82209 | 2025-12-11 05:29:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c287b305-a2bc-385a-aea9-ae34773402a9 | -2.25874 | -51.93642 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff29851f-7f89-386f-b803-6c39b594bc34 | -2.654 | -51.64126 | 2025-12-11 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb6efcaa-d106-3cf6-879d-64ba42d102d1 | -3.11279 | -54.17292 | 2025-12-11 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5b8ad90-62e8-3f8c-918b-b1ffc58af15f | -1.30821 | -53.4859 | 2025-12-11 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README17.md)
