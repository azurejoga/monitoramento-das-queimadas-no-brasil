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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4f15e30-c878-3309-8715-d4af1b06095f | -6.7664 | -59.1515 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6c3eeabb-830c-3b6b-9473-18c9c37ac0d7 | -14.1821 | -52.93 | 2026-08-18 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 75c1f1d2-56e9-3678-a310-bfa5b059767d | -6.8411 | -58.9939 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5525c9b8-607a-319a-9447-f4e7ee688adf | -6.7294 | -59.1723 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 4cf7a73e-d3b6-3cea-b7f9-8e58cc510804 | -8.2036 | -55.0228 | 2026-08-18 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 853a35cb-8e98-34ea-917e-91f87d4103af | -6.748 | -59.1523 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e5a04559-1cdf-391f-bd23-8422f702359a | -6.841 | -59.0132 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 8ebddd78-f216-30b4-b957-d85150c65fe8 | -22.0762 | -55.9924 | 2026-08-18 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 95.8 |
| c8d6875e-7a9d-3c15-8899-d43e8d306978 | -6.8596 | -58.9931 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6709c031-de40-3361-acc8-37fb0575f486 | -6.7478 | -59.1716 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 173.4 |
| be26763d-71a0-3d92-93dc-547382e361fb | -6.7477 | -59.1909 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c346692e-72c0-30f4-9485-965d190ef2cd | -10.8497 | -44.9903 | 2026-08-18 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3975d353-2996-383a-831b-84d841ff5701 | -6.8594 | -59.0125 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| f0b6651e-85b0-3fc0-9999-5ea8ed56aa6c | -6.7663 | -59.1708 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| b0b74cbe-2b6d-3b5a-be0f-4965f64b6f25 | -8.222 | -55.0418 | 2026-08-18 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7d1c0ecd-a70a-3a49-9eb6-1fbe70ba7223 | -6.4048 | -54.9441 | 2026-08-18 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 99890a10-19a2-3e74-ba81-860ac4687bae | -8.2222 | -55.0216 | 2026-08-18 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 597b5064-9ccd-3c41-8d0c-4ff9752393c5 | -10.8691 | -44.9646 | 2026-08-18 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| df5002df-f9d3-3319-912f-b0a88ffac642 | -6.8593 | -59.0318 | 2026-08-18 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| bf2aca8c-83de-3ba9-8f89-5960a807e01d | -22.06802 | -56.00348 | 2026-08-18 01:05:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b08cb6de-3d9a-380e-b278-c12fa0cf21ef | -22.06646 | -56.01042 | 2026-08-18 01:05:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0e9e4149-b0ee-3cb1-930c-c3129ca81294 | -22.06447 | -55.98427 | 2026-08-18 01:05:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c69180c5-4c94-3e18-b8ce-98e62a3435a1 | -22.07536 | -55.98825 | 2026-08-18 01:05:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 5c765875-7e5d-3255-8bf2-d241a567dd7b | -22.06295 | -55.99071 | 2026-08-18 01:05:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 48a19526-8565-364e-9a69-8bb521cc859d | -15.26622 | -56.5093 | 2026-08-18 01:07:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| f3c65938-a5d2-36fe-a0c6-ba454964c0aa | -15.22639 | -57.65298 | 2026-08-18 01:07:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ec90bd31-e6db-38d7-9b77-9d1cb31c4bd4 | -13.42988 | -57.08055 | 2026-08-18 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7e1fdabd-addc-3189-b4ba-63e3833ed3de | -15.26195 | -56.48502 | 2026-08-18 01:07:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| f0a5604e-d8aa-33b0-b0d9-74c4a49fe5e0 | -15.29905 | -56.45356 | 2026-08-18 01:07:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 7fb877e4-9fc7-300f-bdbd-322584d7383c | -14.02894 | -53.677 | 2026-08-18 01:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| fdcded80-765d-3f34-8df1-b8513048572f | -15.24821 | -56.48758 | 2026-08-18 01:07:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 2b2fc930-72d2-333f-b0c1-154d34407c89 | -15.25615 | -56.49161 | 2026-08-18 01:07:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 04e12d6e-8031-36a2-8ae8-170dddc43aaa | -15.26029 | -56.51612 | 2026-08-18 01:07:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 2ea54e2a-c91f-3390-b4de-9aa1354a37d6 | -16.24149 | -57.65616 | 2026-08-18 01:07:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 0995358c-9432-3a1f-91bc-18b1838d7db1 | -14.48639 | -59.34057 | 2026-08-18 01:07:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6d7bd291-0fcf-3da9-990d-93e131de0888 | -20.63825 | -57.92221 | 2026-08-18 01:07:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.8 |
| d9722f17-b05c-361f-87dd-87d794959c38 | -6.74797 | -59.1554 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| bf1eebe7-1a17-3363-83ad-f15f2e4df27f | -7.88819 | -63.75769 | 2026-08-18 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c2ca77f8-32a2-3e89-a84f-74706a1d2878 | -9.42457 | -60.43361 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| bc6141c1-26dd-3d30-9bf5-b4cee12bdde3 | -6.95178 | -59.02367 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 4c5a9efd-97c1-374c-87b4-d3c8b395aac2 | -9.42906 | -60.46366 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 45184fa9-ec0d-3b5e-bc26-fb1b67f1b70f | -8.8963 | -60.59462 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| dade56a0-aaf6-37d8-bcc7-fd83f521db47 | -8.21453 | -55.04285 | 2026-08-18 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 4a48b0d7-5d4d-306d-b0b4-8b56c7a18552 | -11.3708 | -55.43591 | 2026-08-18 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ab00c2f7-e254-3065-9fea-e1947f7dfa6e | -9.42592 | -60.44301 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 27a1ddd7-9b09-3b92-8cf6-f8609783c82f | -7.88035 | -63.76878 | 2026-08-18 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| afeb28ec-ee22-3b51-9df0-5ca9c09f97c4 | -6.85633 | -59.00176 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 0946ece2-0250-372a-8d59-1c7cb25790fc | -7.60468 | -60.96357 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 2d44ca46-eeb5-3b52-a91a-23fb8b25f68a | -9.15892 | -59.68953 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a75f184a-d6ca-3d07-b145-da4fe23a2273 | -7.61583 | -60.96189 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 909c336a-63f7-3354-adbc-169ffafca9c8 | -9.44984 | -60.29906 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| aa0b1520-ecc5-39a3-8d2c-f98eb0defc27 | -6.75413 | -59.18276 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.0 |
| d367bbb2-0518-3744-82e0-2de6f35027a5 | -7.63674 | -55.6446 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9d593275-9a02-3486-ac7b-9426acb958ad | -6.84645 | -59.02541 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 38f3d5a8-6605-3c38-add9-11fc7d191f0c | -8.19663 | -55.05089 | 2026-08-18 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6039aa58-98fd-3959-b915-6a73d8cba971 | -9.43247 | -60.41128 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 9280e522-765c-3134-868f-22aef272c7f8 | -8.20754 | -55.00785 | 2026-08-18 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8d4bc7a2-8296-3913-946a-0e645335ef90 | -7.60246 | -60.9489 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 09ee806f-fcde-3c46-b6ca-3e0db5b9f202 | -7.88955 | -63.76742 | 2026-08-18 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f6038039-0751-3e5d-a716-e78c8e0b2185 | -7.4585 | -60.00618 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 65d32fdf-62e3-3d84-b8e5-7ed6e4c1bfcd | -9.42232 | -60.41858 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 1fc8d947-4478-31be-ab07-6416ab2828fb | -6.84312 | -59.00409 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.2 |
| ea701341-52c3-3e4f-b3ff-e1c32e444a66 | -7.61363 | -60.94721 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 41b1b10c-1c2e-356f-9446-621e2c182f80 | -8.90285 | -60.56286 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 3ef4ee10-c4d6-3bc3-975a-12777c2f70d8 | -7.87898 | -63.75904 | 2026-08-18 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f3d62a63-98bd-3d02-832f-f00426b9d4b2 | -6.73779 | -59.16319 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 848a3e17-b31c-3e40-8b7b-709f7cec6edc | -9.17364 | -59.70506 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7be968f8-7f89-3117-8ee2-dd580a2adf02 | -8.90052 | -60.54791 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 51f32ced-2d0d-3683-95b5-c756107253a0 | -7.61984 | -55.64747 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 50b0e5ef-6f4e-3817-86fa-767ad8a73d58 | -8.94782 | -60.55595 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| e0f2eb6c-e9d6-3584-a8b5-3b4afdfd7960 | -8.72328 | -62.9061 | 2026-08-18 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 95077d38-959f-34b7-9ae5-931ec0afcbee | -8.83724 | -64.14827 | 2026-08-18 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e73ac92-471e-31e5-b9aa-f5ffc651a440 | -6.70086 | -58.94381 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 7314e3f2-c64d-3fca-b0de-543ee18950a6 | -9.4212 | -60.413 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 15771b5c-7cc3-3f6b-ab60-d73e052906e0 | -9.01884 | -60.49209 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cf5aed20-7e03-3900-9951-e01ec5c3249c | -6.76108 | -59.15335 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b936287c-2464-35a3-b085-b5a0951bf5d4 | -8.90143 | -60.5535 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 7f424086-20ef-3e4d-959f-843239da2adf | -7.46405 | -63.63365 | 2026-08-18 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ce613800-efef-3d98-9215-fe2d8a6506e9 | -10.91672 | -62.76556 | 2026-08-18 01:09:00 | TERRA_M-M | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3b280aa5-3e27-3a81-a5e4-8631f9341ebe | -9.42681 | -60.44862 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 790a80b7-784e-3008-a60e-2e910f871105 | -7.62337 | -55.63979 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 61d5b2a6-de8d-3dba-92fe-ba80d5c8afa1 | -6.9181 | -62.90204 | 2026-08-18 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 108ddebc-21a0-3f86-8994-586c11b80d21 | -9.42828 | -60.45803 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d65dbd2f-f1f2-391f-9eea-55658c5befec | -6.91967 | -62.91307 | 2026-08-18 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bf487050-a0e2-3429-9c20-da1cb6159439 | -7.64022 | -55.63663 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 481270ef-d59a-364a-883d-51568b5e3bf4 | -7.6092 | -60.84136 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b67511ab-4998-3871-8b4d-e3e3b43444bb | -6.60334 | -58.971 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b319b926-1897-3b14-8ac6-924abeb07a39 | -8.89688 | -60.60035 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e97b90ef-f93b-3010-b16c-88438f2849e1 | -9.43359 | -60.41681 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 91cfb903-821e-39db-ae8c-d060f35e5e73 | -9.60817 | -63.73104 | 2026-08-18 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5e154e09-516a-34d6-ba2e-0e89f5c7fc77 | -9.16167 | -59.70704 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d3e4e239-bace-31ff-bff2-ff988779e1af | -6.70549 | -58.94931 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 2e9b70bc-e90e-3d01-b75a-c5ede446881d | -8.90364 | -60.56847 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| cedb94ed-1b3d-3c83-a8ac-40810646f167 | -8.19031 | -55.00642 | 2026-08-18 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3bccb8ba-17b8-3564-be55-154632d6dfd9 | -8.19707 | -55.04583 | 2026-08-18 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b2ceee39-9fc2-37f2-8a6b-663a424676cb | -6.75132 | -59.17664 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 249.1 |
| 596b674a-6401-3a14-99dc-be180ad1b4dd | -9.02042 | -67.02614 | 2026-08-18 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6a346440-ae61-3bb5-8ee9-658efd3ea8e6 | -9.52654 | -67.16128 | 2026-08-18 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4b7ed815-f3d0-3864-8133-3920ded6d200 | -6.74096 | -59.18425 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 589bf2e7-489e-33c7-9782-a3ec3289a46d | -7.46546 | -63.64359 | 2026-08-18 01:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |


[Clique aqui para ver as próximas entradas](README4.md)
