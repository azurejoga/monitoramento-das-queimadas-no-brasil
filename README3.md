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
| 5f3623e4-6955-3ea1-b344-cd9acd8e5945 | -18.2 | -51.3481 | 2025-07-03 00:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 0eae36ae-8880-359e-8bc5-eee11bb44d07 | -14.6484 | -53.8785 | 2025-07-03 00:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 188.9 |
| bc707d68-175e-3f61-ab4b-b9df66c5779b | -17.957 | -50.665 | 2025-07-03 00:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 551.0 |
| d76d709d-6e38-3167-b205-34ac6a074319 | -7.2028 | -43.0936 | 2025-07-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| a3e4e1f0-fb1d-31ad-ae47-c009bd218fc1 | -6.1792 | -48.0494 | 2025-07-03 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| c793c83f-b431-3826-a4bc-201aa7de9cb0 | -25.25912 | -50.01333 | 2025-07-03 00:58:00 | TERRA_M-M | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| eb773663-bbe5-3d99-8378-d375e020acc6 | -20.72939 | -56.65588 | 2025-07-03 00:58:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 21af5aab-dcfb-3c6e-a51c-c3f48ae1bb1a | -7.2408 | -43.0664 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 4ee0af20-5f84-3bdb-8599-5ff377ead242 | -9.186 | -48.7559 | 2025-07-03 01:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 085d3514-a955-33c4-9100-aea18ebd9d1f | -6.9793 | -42.8798 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| e19abacb-338f-3c94-924d-e65a16f4f9d5 | -6.9605 | -42.8816 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 449.4 |
| a8969b6c-8266-3a90-9938-a81c1f483294 | -14.6287 | -53.9018 | 2025-07-03 01:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 55db32a5-bc6e-33b3-8bd7-195d9a3462c5 | -7.2219 | -43.0682 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 260.0 |
| c3cce7cd-2006-366b-b8d4-a5710cebfb01 | -17.957 | -50.665 | 2025-07-03 01:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a27d1e21-46ad-307f-b8ea-98802fec0224 | -6.9414 | -42.907 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 55d1813f-6181-314d-b414-035848cb1dd0 | -18.2 | -51.3481 | 2025-07-03 01:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e12804b8-a211-3292-9e6d-d497539926ab | -6.1792 | -48.0494 | 2025-07-03 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 49e2ed38-0e67-37be-bf00-b2f51c27c59d | -6.9416 | -42.8834 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 213.0 |
| 84a8e33f-958b-3547-90a7-f68c3b039f94 | -11.6588 | -44.5974 | 2025-07-03 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0997bb2a-7cd3-30c1-b740-6814daad885c | -17.9371 | -50.6685 | 2025-07-03 01:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| bf39c95f-b9cf-36b7-817e-314acedc9323 | -9.1668 | -48.7794 | 2025-07-03 01:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 58.0 |
| de843376-fc8e-3c19-87f2-270cbce77acc | -11.6383 | -48.0644 | 2025-07-03 01:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 9000a872-583a-342b-873d-dafbde5d0f91 | -14.6484 | -53.8785 | 2025-07-03 01:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| a75b1bf4-01cc-398d-81d0-56d67990f4c3 | -6.6112 | -43.8941 | 2025-07-03 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6111ec8e-49c6-308f-a010-c82d09d9a958 | -7.2222 | -43.0447 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.2 |
| cabf4085-003a-3b1c-a55a-9cd47108eb5d | -6.9607 | -42.858 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 15c4cb69-f588-3307-aa8a-0b1b43d9ec6a | -9.1857 | -48.7776 | 2025-07-03 01:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 258dc00d-5837-3287-a177-e0c8e4585209 | -11.6592 | -44.5741 | 2025-07-03 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| ad003757-ec8b-3a18-93de-db9741b562d8 | -18.2195 | -51.3666 | 2025-07-03 01:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 0f254e5c-582e-3ce6-993d-488f50eaebc7 | -18.22 | -51.3446 | 2025-07-03 01:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 257.9 |
| d920fc18-cdb7-3300-9d56-0e73e55ecda5 | -14.6481 | -53.8994 | 2025-07-03 01:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 921b68da-030f-382a-921e-5f839c21cb3c | -6.9602 | -42.9052 | 2025-07-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.0 |
| 31048dcd-c673-34fe-8d83-33f6c117c52b | -6.1606 | -48.0507 | 2025-07-03 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 975848f4-d00a-3a53-b231-a71890b225d5 | -14.6291 | -53.8809 | 2025-07-03 01:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 249.7 |
| 5d1727e6-0ad1-37e8-9a78-d6eb13fb3635 | -16.07243 | -51.56315 | 2025-07-03 01:00:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adc24f45-60ef-3d5c-a10f-223fb02814ef | -17.94217 | -50.66788 | 2025-07-03 01:00:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4750b3f8-2929-35fc-ab4b-4b3945f33991 | -16.42407 | -49.90891 | 2025-07-03 01:00:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9ca6b772-b975-38d0-aa35-cd5ee6159151 | -18.65488 | -55.74767 | 2025-07-03 01:00:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.0 |
| d10c3a14-eaf0-3b10-ad1f-a11bfd96b760 | -16.42235 | -49.89775 | 2025-07-03 01:00:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4a151823-ec5e-3943-886c-f36eb877a7a3 | -17.95281 | -50.67643 | 2025-07-03 01:00:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 5e1b1783-0e16-3148-ab8a-4a4f5b57678e | -17.94366 | -50.67788 | 2025-07-03 01:00:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 31b6317c-9b29-34a3-88df-35844d6eff52 | -18.21648 | -51.34559 | 2025-07-03 01:00:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 07713206-ea47-3311-b65e-d5e97f0ebe17 | -18.66499 | -55.74632 | 2025-07-03 01:00:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 1e845e0d-8c67-364c-b94b-ce9d2c05eea8 | -18.21029 | -51.36606 | 2025-07-03 01:00:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3daec874-b103-3ff0-b0f0-a1c1d67d11ba | -16.41443 | -49.91066 | 2025-07-03 01:00:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 784055ed-dbb8-3533-964b-a44f8fb57fff | -18.21785 | -51.35509 | 2025-07-03 01:00:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 195.3 |
| c1d874a6-91fe-395b-9a9e-bb77e7a3f7fd | -17.95134 | -50.66645 | 2025-07-03 01:00:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 409.9 |
| 3d8fb3a8-9d7e-3a00-8a39-af4626da67da | -18.20892 | -51.35656 | 2025-07-03 01:00:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 1ff19edb-c967-34a8-b1dc-02939a4d981f | -18.65337 | -55.73539 | 2025-07-03 01:00:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| ebe8a99b-1c0d-38ff-9e72-2c2651060176 | -18.20754 | -51.34707 | 2025-07-03 01:00:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| d4cfa314-926d-3b9d-9ec8-77fe3b0d81d1 | -16.41269 | -49.89947 | 2025-07-03 01:00:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 34.3 |
| fac7fe5c-ff64-3326-ace8-854f6b9781dc | -12.57167 | -48.88947 | 2025-07-03 01:02:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| bf46aad2-bdb6-3b6b-b5d4-5706ee9eff5b | -10.29833 | -57.13491 | 2025-07-03 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3388f42e-65fd-3d26-a155-0d98c685a083 | -12.63036 | -54.21525 | 2025-07-03 01:02:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| eab468aa-02ae-3607-8956-c68efb967bb0 | -10.08306 | -48.00144 | 2025-07-03 01:02:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e48c048a-e00e-36bb-a9e6-829aeaafce3a | -9.79353 | -47.7462 | 2025-07-03 01:02:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 828d34b6-57c4-311b-bda8-3aa7696b2dd1 | -11.6354 | -48.07784 | 2025-07-03 01:02:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8c51b0da-341f-31c3-b1ac-b42d54fa341e | -10.29685 | -57.12366 | 2025-07-03 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dea9c81d-23bc-39f0-a747-d5de7119ca8c | -9.63272 | -61.4729 | 2025-07-03 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 227c0338-7525-3b1f-9063-4145ae405e79 | -11.66554 | -44.61508 | 2025-07-03 01:02:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b1a1a6a6-337c-37b2-8125-766b7e0b2bc0 | -11.65981 | -44.58284 | 2025-07-03 01:02:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| baca5b74-5886-3f2b-a49c-8260cea866e8 | -11.14451 | -43.34521 | 2025-07-03 01:02:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 35.3 |
| b5ea516e-2b9f-344c-85ec-e4f4c103b1b7 | -12.43362 | -50.02589 | 2025-07-03 01:02:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 074ffc70-8bfd-3e8d-8af3-8bfc7cf8be0b | -10.89467 | -56.45137 | 2025-07-03 01:02:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d1506919-374c-3245-adc5-ceea9a6864f6 | -9.70286 | -56.18532 | 2025-07-03 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| af9b66dc-7c65-3dcf-b6de-9b1d8adf450e | -11.64738 | -48.07586 | 2025-07-03 01:02:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cc9a1739-01e7-3716-a0b2-fb79852b5dae | -14.62969 | -53.89303 | 2025-07-03 01:02:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 885c0ce2-f25b-38d7-8622-cc0fa91b835b | -9.16827 | -48.78117 | 2025-07-03 01:02:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 872af683-68c0-399c-bf2b-57c1fb7b66ba | -11.53761 | -47.31396 | 2025-07-03 01:02:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| a831e13f-31d8-3cc4-9008-93f211a7efb0 | -11.1175 | -48.8766 | 2025-07-03 01:02:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 709770e7-27cb-37fb-8f97-4f620cf49aa2 | -11.65589 | -44.62218 | 2025-07-03 01:02:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 490f0287-badd-335d-a0eb-fcfef12f21b5 | -11.66605 | -44.58696 | 2025-07-03 01:02:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b49e3ff6-dd8b-3c9e-9371-771103d5389c | -11.11507 | -48.86118 | 2025-07-03 01:02:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 77ce1c6d-80b6-329d-9aad-7bdca64cd7d7 | -12.6316 | -54.22437 | 2025-07-03 01:02:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a9e7383b-a063-3f72-ab90-ef9f193cd2d7 | -9.36132 | -48.41063 | 2025-07-03 01:02:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 263e593a-b251-3324-9f16-23a4072f39a0 | -14.63734 | -53.8825 | 2025-07-03 01:02:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 43bbaf75-12cc-32f4-8920-355f8e3bbd41 | -7.85862 | -47.88597 | 2025-07-03 01:02:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 18a1e64f-2a6f-3d5b-9b23-7765bceafcc4 | -10.66603 | -49.45545 | 2025-07-03 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b4634591-7d69-3721-854c-6f89301c3803 | -9.16567 | -48.76454 | 2025-07-03 01:02:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 0431bf63-a0c2-379a-9c70-077cd4372b60 | -9.62993 | -61.44983 | 2025-07-03 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 1a337243-f9d0-394e-9e66-0d59739bb1f5 | -9.18014 | -48.77935 | 2025-07-03 01:02:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 92a6bd8c-a210-3da2-afe8-6e557929ccd1 | -9.79401 | -47.75174 | 2025-07-03 01:02:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b08207f0-a200-3de5-b205-655eb4ad86f4 | -9.17756 | -48.76275 | 2025-07-03 01:02:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 89ecab72-01dd-33ae-9e0a-f8cce0e08368 | -12.42344 | -50.02762 | 2025-07-03 01:02:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 88716dd7-a265-3127-90f6-3c4aa1db9da9 | -11.65037 | -44.58989 | 2025-07-03 01:02:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| bc939c5f-ac11-3496-ab7c-a73b4f675576 | -14.63984 | -53.90094 | 2025-07-03 01:02:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7c0683c6-16ef-31c7-b3a0-8a098c348d0f | -11.64413 | -44.58574 | 2025-07-03 01:02:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f7de71ee-9628-36b7-93f6-82b65474720e | -11.49926 | -48.96 | 2025-07-03 01:02:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 197ee5e2-1f43-3b3a-9f49-1f5ac4822ca1 | -10.7109 | -49.67577 | 2025-07-03 01:02:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bc4ce7b8-9527-3df5-bf16-6cd2356095d1 | -10.88513 | -56.45266 | 2025-07-03 01:02:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a8eb785-e52d-363e-8764-0ce50fd245fe | -14.63859 | -53.89171 | 2025-07-03 01:02:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 246.4 |
| eaa8b9d4-e0a5-36f5-9a28-e1e68f667871 | -14.62844 | -53.88381 | 2025-07-03 01:02:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 214ee71f-427b-32aa-841d-69b8054cb4f2 | -5.86731 | -50.14555 | 2025-07-03 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f97bff90-8da3-3fc0-a4e5-dbc8b89e79e4 | -6.97592 | -55.28689 | 2025-07-03 01:05:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a3ff4f1-f464-3512-af52-c91c4d7447ea | -6.1765 | -48.04778 | 2025-07-03 01:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 0415240e-3fef-3467-b8a6-9191c3c5e257 | -5.87861 | -50.14397 | 2025-07-03 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b6b99569-53fe-3b1e-a7af-f3cbc0828388 | -8.52504 | -54.77313 | 2025-07-03 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b889a69f-ef35-3d1b-9037-4a68885e2b29 | -6.17088 | -48.07672 | 2025-07-03 01:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 669d5e28-1ef9-3327-9b26-0ce7084ea964 | -6.01687 | -49.22843 | 2025-07-03 01:05:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 96f1fcb3-9e10-3f6b-bf10-a63a03ea21a1 | -6.029 | -49.22663 | 2025-07-03 01:05:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README4.md)
