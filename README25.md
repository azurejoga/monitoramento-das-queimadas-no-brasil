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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98415506-f9f5-33a7-afff-8964dd782e31 | -3.4915 | -43.3368 | 2024-10-26 03:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ba4a88cd-c056-34a8-a492-7ba824a029ac | -3.6084 | -45.8147 | 2024-10-26 03:15:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 133.0 |
| cc46e893-e957-3529-a967-2f1d62293c2a | -4.5799 | -48.0349 | 2024-10-26 03:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 212.6 |
| 264838ef-342c-3ced-9ca5-d3637bf507c8 | -4.58 | -48.0132 | 2024-10-26 03:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 225.9 |
| 564335fb-695c-300e-8a95-85f8b2fb81ff | -6.8534 | -45.8794 | 2024-10-26 03:15:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 119bf52e-fcec-35a2-b14c-8f00d24a2965 | -7.6475 | -63.4396 | 2024-10-26 03:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1e36a684-1cbf-3845-ac98-ce0eb87cf2f7 | -7.629 | -63.459 | 2024-10-26 03:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 07bf06f9-248d-37ff-a90b-21768256fcbd | -7.6474 | -63.4584 | 2024-10-26 03:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 41bcd145-3321-377e-875a-4cac353f8ef2 | -16.9012 | -57.5108 | 2024-10-26 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 6759f2de-691a-3ba4-bef0-8b3fe906e43c | -16.9207 | -57.5086 | 2024-10-26 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 0d3eb2cb-e062-3508-a229-e6fec3d639d6 | -17.0499 | -53.452 | 2024-10-26 03:16:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f359964e-d9f2-3a49-aec2-72917bac14e1 | -17.254 | -57.4903 | 2024-10-26 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 03f8c4b9-5654-3617-bc74-7d8c3a5aad75 | -17.6667 | -57.4822 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 2a32070f-a71e-35c8-bc4e-47c8c6a2031e | -17.6865 | -57.4798 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 93ce0719-a4d6-329c-8f89-3c51a111ee4c | -17.7443 | -57.555 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 61d73242-018c-315a-827e-042fb6e095ce | -17.7446 | -57.5344 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 90501b07-b27a-32d4-a2b4-de7104977521 | -17.745 | -57.5138 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 2f36306d-686c-3a34-8037-a683d27c783d | -17.7647 | -57.5115 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| fd246f11-be49-3087-b518-0e5d0280cfde | -17.7868 | -57.3649 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 35c7ae10-6db5-3b7f-8a37-b4b73768cd9a | -17.7872 | -57.3443 | 2024-10-26 03:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 1deeef45-f01c-3c35-ac72-49c408ed70f5 | -17.8631 | -57.5201 | 2024-10-26 03:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 527600e7-afc7-3f30-b507-b313d79f261c | -17.9415 | -57.5516 | 2024-10-26 03:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| ad54c678-7ec9-3bac-bb6b-7ff09a50f1bf | -18.0629 | -57.3721 | 2024-10-26 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| cfe1e9ae-19f8-352e-930a-a59f8385c3c7 | -18.0653 | -57.2274 | 2024-10-26 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 8bb91dc6-5693-382a-88b4-16ecb035af76 | -18.0827 | -57.3696 | 2024-10-26 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 134a4422-bcd0-3c26-bcaf-53a8dcc23ae2 | -18.083 | -57.3489 | 2024-10-26 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| e0479ad8-0108-377d-8945-75efcc19d6af | -18.0851 | -57.2249 | 2024-10-26 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| e3d28a2f-a5c4-31d8-b051-0c7472e310a8 | -18.245 | -56.0002 | 2024-10-26 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| f91b1059-ad81-38b7-b300-dad6aaca180c | -18.2649 | -55.9975 | 2024-10-26 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 61f5ec03-9155-3e87-abf3-20ff126aed4a | -19.526 | -56.7221 | 2024-10-26 03:16:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 22f4da31-a327-3d68-a48c-9f92201ea00e | -19.5264 | -56.7011 | 2024-10-26 03:16:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.0 |
| 44dfa04b-280e-3ce5-a582-c28334dcf2e5 | -19.5465 | -56.6983 | 2024-10-26 03:16:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 35a9679a-2a45-3ae4-8de7-bef89ade17a3 | -2.1929 | -53.7234 | 2024-10-26 03:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 3ed5570f-9df2-3f74-9f70-8ce9150672b2 | -2.9944 | -50.5025 | 2024-10-26 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 356adc9d-927a-326f-98fd-fad044901781 | -2.9945 | -50.4816 | 2024-10-26 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 730f6b6d-bff5-38ee-b7fd-103b292f0a52 | -3.0129 | -50.502 | 2024-10-26 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d47904ba-1fb2-39c2-9dd2-8fa7a9f37cc4 | -3.013 | -50.481 | 2024-10-26 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 3405da44-fde1-3270-88b7-2056a221206c | -3.4729 | -43.3377 | 2024-10-26 03:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 087ff261-c6ea-3d61-be7b-256c3e0d185c | -3.473 | -43.3144 | 2024-10-26 03:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 59dc3f14-69c8-38d0-9471-de17d8cefca3 | -3.4915 | -43.3368 | 2024-10-26 03:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 66170d57-9539-3ee3-822e-6ec2f5e302de | -3.4917 | -43.3136 | 2024-10-26 03:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4da8aaa2-7807-3129-88dc-657605613e76 | -3.582 | -51.2137 | 2024-10-26 03:25:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 7244f2c0-4c9a-3df0-bd43-d5caf4815295 | -3.6084 | -45.8147 | 2024-10-26 03:25:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 175.6 |
| c37ef02f-80d4-3a8e-b7b5-655d9cfc6bf9 | -3.6085 | -45.7924 | 2024-10-26 03:25:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ae9dfadb-0e8a-31e3-ac0c-68b65052fafe | -4.5613 | -48.0358 | 2024-10-26 03:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4d238b0d-8d9d-3412-bceb-ce28bc104baf | -4.5799 | -48.0349 | 2024-10-26 03:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 219.8 |
| e91a296e-4fc5-3a59-b349-747a3603db84 | -4.58 | -48.0132 | 2024-10-26 03:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 722f797e-4e3b-3383-b09d-e1e13a536f34 | -6.0744 | -47.2263 | 2024-10-26 03:25:40 | GOES-16 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 377165ee-ce1a-39f1-a0cb-e514b72f3678 | -6.0931 | -47.225 | 2024-10-26 03:25:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2f9b4b4a-f097-3cc1-b6d5-1fbb78602d6f | -7.629 | -63.459 | 2024-10-26 03:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| be5b433d-507b-3b6f-aad8-68527aed89ed | -7.6474 | -63.4584 | 2024-10-26 03:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3ad10977-8b1c-3aeb-ae1a-c5d883041d81 | -7.6475 | -63.4396 | 2024-10-26 03:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 67182f13-3118-3567-96a0-3c3eba1be1c5 | -17.0499 | -53.452 | 2024-10-26 03:26:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4543ddf4-0b77-3cf0-97a9-53233b7a72b5 | -17.6667 | -57.4822 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| bf5efc5a-b981-33f1-b0d8-97c141b8ed47 | -17.6861 | -57.5004 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| e8d37bca-5a42-3f5b-ba6c-dc42cbc84747 | -17.6865 | -57.4798 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| 0fa34be3-4880-3d6d-8c7f-19786c75d766 | -17.7443 | -57.555 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| b17e0229-3e0b-3f0f-a9a7-66a62b324155 | -17.7446 | -57.5344 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 184.5 |
| b07a6bb8-3b64-3f5c-9552-9b7f6a7aa394 | -17.745 | -57.5138 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 223.9 |
| b1e571e8-4191-35ac-a76c-cc45c23f2afd | -17.7453 | -57.4933 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 47bbd548-d126-3857-85d7-826364429d47 | -17.7644 | -57.532 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.3 |
| 00919545-bd6e-34b7-b61f-9eb5c6e68709 | -17.7647 | -57.5115 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.3 |
| fe584d32-6488-33eb-a46c-7d7553c60233 | -17.7674 | -57.3467 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 1b779b0f-122d-3ebd-aeed-1e76faa1276a | -17.7868 | -57.3649 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 4d54525d-2a8a-3acc-ac47-4916ccc30549 | -17.7872 | -57.3443 | 2024-10-26 03:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| c8c62120-b606-35f8-87dd-0de783e83adf | -17.843 | -57.5431 | 2024-10-26 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| ec04a7b0-f43c-30ba-988f-9a345d90283d | -17.8631 | -57.5201 | 2024-10-26 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 0d0eea3a-f9b9-313e-b5f9-f6726f68f0a3 | -17.9415 | -57.5516 | 2024-10-26 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 1d07e0c2-484b-39ad-975e-92f04aaed4ec | -17.9418 | -57.531 | 2024-10-26 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 700446be-225f-36bd-ad3e-57b68e21601f | -18.0629 | -57.3721 | 2024-10-26 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 898a0e41-2147-362b-8cb2-69a5b6c27fa6 | -18.0827 | -57.3696 | 2024-10-26 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.0 |
| c0c9a423-4619-363c-b366-a3833ca3cb8a | -18.1025 | -57.3671 | 2024-10-26 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 99cf1c34-0a44-3531-8d1a-039f3272fa32 | -18.2649 | -55.9975 | 2024-10-26 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| dddc1b18-2c65-3dca-ae89-fc6c9d752373 | -19.5264 | -56.7011 | 2024-10-26 03:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.4 |
| f5aea619-8307-3c12-8467-79ab1bff435a | -2.1929 | -53.7234 | 2024-10-26 03:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c9d5c4ea-27ae-3e79-b638-20be300a0309 | -2.9944 | -50.5025 | 2024-10-26 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 86a1a0fa-6f12-3318-95b0-e9f4b1837391 | -2.9945 | -50.4816 | 2024-10-26 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 55c5e10a-1f27-3401-9028-bc6cc359b53e | -3.0129 | -50.502 | 2024-10-26 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 69bea8c3-1c5d-38cb-a188-e0f431a68b84 | -3.013 | -50.481 | 2024-10-26 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 4aa6f29b-0433-3f6b-8f05-e7d7381010ce | -3.4729 | -43.3377 | 2024-10-26 03:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e32c910f-a084-3f35-915d-d45fc161c1f7 | -3.473 | -43.3144 | 2024-10-26 03:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8a5415a3-1ff5-3261-b7dd-b81d5d847d7e | -3.6083 | -45.8371 | 2024-10-26 03:35:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cc8fd4dc-e504-3778-b239-309636219030 | -3.6084 | -45.8147 | 2024-10-26 03:35:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 206.2 |
| fbb42bab-7634-38b2-a397-cd6ff4017933 | -3.6085 | -45.7924 | 2024-10-26 03:35:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7c41a4e7-018d-3ec6-a03b-723da24f38d0 | -4.5613 | -48.0358 | 2024-10-26 03:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a17395f1-153a-3af2-bd95-a4957cb50d94 | -4.5614 | -48.0141 | 2024-10-26 03:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c2233155-080f-3c7e-85aa-3e6f3edc38d4 | -4.5799 | -48.0349 | 2024-10-26 03:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 210.4 |
| 66998ebb-abea-304f-857f-12812965bae4 | -4.58 | -48.0132 | 2024-10-26 03:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 2b98096f-6b35-318d-9aa4-1f18227428c9 | -7.629 | -63.459 | 2024-10-26 03:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b995b8b8-8bc8-328c-9c66-f68c7f107a90 | -7.6474 | -63.4584 | 2024-10-26 03:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7a055458-69c6-36dd-ab7d-cd9fb289c3c2 | -7.6475 | -63.4396 | 2024-10-26 03:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d69e48f9-2e05-3011-aac1-cc531ef2796f | -17.0499 | -53.452 | 2024-10-26 03:36:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6032ee79-2cae-3bde-a40c-602857354307 | -17.6865 | -57.4798 | 2024-10-26 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| f3c11c19-5730-356b-b946-b5e87ee4364c | -17.7872 | -57.3443 | 2024-10-26 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 12649697-a6ba-3648-964a-ea28295bbd0f | -17.8239 | -57.5043 | 2024-10-26 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 63d6d6bd-8f28-3a53-af18-6cacebd42668 | -17.7674 | -57.3467 | 2024-10-26 03:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| bd8827fc-acbe-33b8-8e41-323279f4cd10 | -17.843 | -57.5431 | 2024-10-26 03:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| f28021a9-4a80-3aaa-8ec6-d24e4e52ca12 | -17.8628 | -57.5407 | 2024-10-26 03:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| d1771e90-922a-3ad2-bda3-4d58c4815113 | -17.8631 | -57.5201 | 2024-10-26 03:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.7 |
| f520e360-fe5a-3644-aa71-7d04dba10d25 | -17.8828 | -57.5177 | 2024-10-26 03:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.1 |


[Clique aqui para ver as próximas entradas](README26.md)
