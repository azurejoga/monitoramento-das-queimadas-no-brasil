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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50332c26-129b-3229-bfa8-4f8ed884fbe1 | -5.5729 | -45.3102 | 2024-10-26 00:34:32 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56c20ec8-f14c-3a89-8bc5-8bb9a9c3ffa2 | -5.5612 | -45.304001 | 2024-10-26 00:34:33 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1421f09f-bd2e-368e-8c0b-19d22aea7ca4 | -5.5631 | -45.3125 | 2024-10-26 00:34:33 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddf79d43-ecfd-3358-b2e5-9c2910f1d19c | -5.8487 | -46.553699 | 2024-10-26 00:34:33 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d084a98-8359-3c13-b91b-69005c6b6188 | -6.7948 | -50.863701 | 2024-10-26 00:34:33 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb3ec4c-89ed-3668-896b-009d8e365d9f | -5.7601 | -46.526901 | 2024-10-26 00:34:34 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59591666-7fb8-30eb-b141-c87659caea5f | -5.7618 | -46.534401 | 2024-10-26 00:34:34 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c5cef5c-4be4-3afe-a953-fa275322ef48 | -5.8488 | -47.186501 | 2024-10-26 00:34:35 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60394627-2074-3d13-98f9-29ee2087a5b4 | -2.1929 | -53.7234 | 2024-10-26 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0c87c511-8cd9-310e-addf-db54f444d45a | -2.3709 | -66.4527 | 2024-10-26 00:35:19 | GOES-16 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 936ced3a-4d99-3124-97eb-ba78aaea84df | -2.6949 | -51.7979 | 2024-10-26 00:35:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2e1971bf-c051-30c3-a106-3ca248da5e2e | -2.8739 | -53.3252 | 2024-10-26 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8e969e59-35d6-300f-b300-8cd0423c0cd7 | -2.874 | -53.3049 | 2024-10-26 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3320651d-f030-3e71-aafd-a012db4c6f16 | -2.8923 | -53.3247 | 2024-10-26 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f2a8b5db-57b9-3e2e-b579-958a31ed45d6 | -2.9501 | -52.5708 | 2024-10-26 00:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 49169414-103b-3d61-a305-d280066fe1f3 | -3.0932 | -53.7239 | 2024-10-26 00:35:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 6d36e88b-210f-3d87-b599-5f3a2ae99985 | -3.1116 | -53.7234 | 2024-10-26 00:35:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 40d23f9a-368c-3739-9260-d7831d6c1916 | -3.1232 | -50.6033 | 2024-10-26 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 38966a13-70cb-34fe-ba73-baf370c5f8f4 | -3.2368 | -45.8077 | 2024-10-26 00:35:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| a7937c9a-6b1f-30d4-a944-1091db6e8b9e | -3.2553 | -45.807 | 2024-10-26 00:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 63229e94-38de-3c2a-95cf-ca3a902ba264 | -3.4729 | -43.3377 | 2024-10-26 00:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9ad9100f-c3ff-38bd-8daa-a4abaf71cd3c | -3.473 | -43.3144 | 2024-10-26 00:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d4600adb-d054-33d1-b03b-e37c4ab9982c | -3.4915 | -43.3368 | 2024-10-26 00:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 72a1ba12-af3e-3c9c-a0c7-f144904c23e0 | -3.4917 | -43.3136 | 2024-10-26 00:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9ac5d022-a671-31d9-a623-f3b98cd32505 | -3.5943 | -44.9833 | 2024-10-26 00:35:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 74de1990-f9ea-355c-8c1b-968c5888e4d6 | -3.5944 | -44.9606 | 2024-10-26 00:35:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 231.0 |
| 9e98fafb-9621-3237-bfbb-61073198df95 | -3.6129 | -44.9824 | 2024-10-26 00:35:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 133.5 |
| f937f968-c189-3bce-9dfd-5ac55492eed7 | -3.613 | -44.9598 | 2024-10-26 00:35:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 214.4 |
| 53f0347b-c8e5-3999-babb-9e2b49accbc8 | -3.8982 | -41.0154 | 2024-10-26 00:35:27 | GOES-16 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 8b283ec1-1a9b-3f1b-a5db-46b4e88a1208 | -4.5613 | -48.0358 | 2024-10-26 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| d1d14e11-540e-32cb-baa7-de9692dde1b5 | -4.5614 | -48.0141 | 2024-10-26 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 3acf4ac0-a4fd-3246-8ce5-33e7c76d5ed9 | -4.5799 | -48.0349 | 2024-10-26 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 44c1ef8e-2de7-3b27-a883-dcbab387f25e | -4.58 | -48.0132 | 2024-10-26 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 95c62f31-2766-31ee-a53e-23f8d54d4af5 | -6.5592 | -41.7062 | 2024-10-26 00:35:42 | GOES-16 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 7932be26-71c9-33a6-8a31-cd068a64b38b | -7.6474 | -63.4584 | 2024-10-26 00:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a469c48b-fee6-30cf-bebb-f3330ca0fa64 | -9.4996 | -47.8068 | 2024-10-26 00:35:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1b454923-c807-3a3a-a0ea-4c14badd73c2 | -9.878 | -35.999 | 2024-10-26 00:36:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 51a008b9-e187-3c09-8b19-44de0f1bcdff | -9.6346 | -47.5942 | 2024-10-26 00:36:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 8b1f1fbb-e3a0-3ec8-bb8a-74c73a601aba | -11.5037 | -45.8167 | 2024-10-26 00:36:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ae8ce75a-c5de-33a5-ac62-0e435719af70 | -12.0012 | -63.9013 | 2024-10-26 00:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 1932047a-6340-3544-b8e3-249ee62b38f7 | -17.4222 | -39.9353 | 2024-10-26 00:36:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| dbaad234-e49c-3c2d-b41b-3b88bbc94de5 | -16.94 | -57.5268 | 2024-10-26 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| ae7ee9ae-8a28-3bcd-98f6-7259045086c2 | -16.9789 | -57.5428 | 2024-10-26 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.3 |
| 46596910-78ac-3ca2-afdd-d74cf82d411f | -17.0499 | -53.452 | 2024-10-26 00:36:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3cc13ebe-71f2-32b2-865f-bc68b24095af | -17.0377 | -57.536 | 2024-10-26 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 485bf6aa-a3cf-3b1d-ac8c-6d0c97b403df | -17.0381 | -57.5155 | 2024-10-26 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 4be77870-e364-3fdf-9652-270d2593d36f | -17.2393 | -57.1845 | 2024-10-26 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| ece342a5-6ef8-3808-bd2c-80d7cdb43bb4 | -17.2537 | -57.5108 | 2024-10-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 8d39f6a4-def1-35ba-aee1-8721f2687370 | -17.254 | -57.4903 | 2024-10-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 146e9e6a-557f-3c3f-8fb5-7ad6754e16d5 | -17.2733 | -57.5085 | 2024-10-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| f123da22-6a66-3f31-b739-809b577998cf | -17.2737 | -57.488 | 2024-10-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 200de1c3-5fc4-38eb-985b-e11b2b4c13c5 | -17.1987 | -57.2714 | 2024-10-26 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 9e7e828e-05d7-3c36-b075-c468b2aa450e | -17.199 | -57.2509 | 2024-10-26 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| 0fc1c420-8ef0-39a2-ae26-1c2ad3ef2e5e | -17.219 | -57.228 | 2024-10-26 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| c2b09662-8bb6-31ef-91f0-8d3b539cf771 | -17.2193 | -57.2074 | 2024-10-26 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| 61b329c9-d451-3de7-8d7d-5d9ba57e6ec3 | -17.2344 | -57.4926 | 2024-10-26 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 474f41f7-4741-3669-8e73-7716d300bab0 | -17.239 | -57.2051 | 2024-10-26 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 3ce63432-2a53-39e5-8d96-f17bb14fc5aa | -17.9415 | -57.5516 | 2024-10-26 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| aa753191-fa50-36fa-87b3-c48472b9e383 | -18.0653 | -57.2274 | 2024-10-26 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 2915e444-d5c4-3bf9-87a9-039508abb127 | -18.0844 | -57.2663 | 2024-10-26 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| dcd15b09-3ebe-32f6-aaa8-f8503f3ab605 | -18.1039 | -57.2845 | 2024-10-26 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 4828297e-e379-35a3-b60a-256a0261affb | -18.1042 | -57.2638 | 2024-10-26 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| a92850c3-799a-3a0c-8281-99100e8d362e | -18.2649 | -55.9975 | 2024-10-26 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| 4950accd-d750-356e-af23-19461c003869 | -19.4866 | -56.6857 | 2024-10-26 00:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| ef06b329-fd22-3ab5-a676-304263995f12 | -19.487 | -56.6647 | 2024-10-26 00:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.0 |
| 7cbda529-3732-398a-8efb-db1f75080f68 | -19.4874 | -56.6437 | 2024-10-26 00:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 099cb0a0-2eae-376c-a772-e18c76941840 | -19.5067 | -56.6829 | 2024-10-26 00:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.9 |
| 1ac98c11-2ce3-3e80-b844-8efde71a3b81 | -19.5071 | -56.6619 | 2024-10-26 00:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 98f1b1c1-941c-35f7-96e8-e9f78a0a770b | -19.6063 | -56.7108 | 2024-10-26 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 23f5cea2-52e9-3a62-9688-342d38fe7454 | -19.6067 | -56.6898 | 2024-10-26 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 139.1 |
| 33a8fd51-aa0c-3c28-8ceb-3f6a7a24da83 | -19.6264 | -56.7079 | 2024-10-26 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 56ca152d-52cf-3325-8e51-469f58f32aaf | -19.6268 | -56.6869 | 2024-10-26 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 164.5 |
| 1e52747d-109e-39dc-9db0-6250c158cdd6 | -2.1929 | -53.7234 | 2024-10-26 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 7a861cb9-9861-354f-b4fe-4e7c56b8f7ad | -2.6949 | -51.7979 | 2024-10-26 00:45:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ba2462ea-6fdb-304b-b690-e96a04c9d7c4 | -2.8739 | -53.3252 | 2024-10-26 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 069eef62-0869-33b3-aa44-08d3adc0562c | -2.874 | -53.3049 | 2024-10-26 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| ceb20dbf-ccea-392b-a494-e42f8e68c610 | -2.8923 | -53.3247 | 2024-10-26 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 16c1c851-5660-3200-aa91-669d87435e2e | -2.8924 | -53.3045 | 2024-10-26 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| b7015d8f-8452-39c9-b4b6-7abde7686440 | -2.9501 | -52.5708 | 2024-10-26 00:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fd7a5fa7-0860-3d5b-8d75-177ed06b70a0 | -2.9501 | -52.5504 | 2024-10-26 00:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 25c0ed51-2bb1-38d4-9327-f6f56dbb51d4 | -2.9578 | -50.4198 | 2024-10-26 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 0ffbf1f6-730b-3cb4-b814-607493833f51 | -2.9661 | -53.2621 | 2024-10-26 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 46ed3cc8-70bb-3fdc-832b-c4099f2ca011 | -3.0932 | -53.7239 | 2024-10-26 00:45:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 15f4b87c-45c8-344d-99be-0a535e00b5a7 | -3.1116 | -53.7234 | 2024-10-26 00:45:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 4c03c6c7-077a-3b60-8fba-dae77bd38bda | -3.2368 | -45.8077 | 2024-10-26 00:45:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 2fae61d5-d6dd-3243-b76b-47ab620c84ed | -3.2553 | -45.807 | 2024-10-26 00:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| a7933626-68cd-34a6-8dbd-c8136efae9f2 | -3.4729 | -43.3377 | 2024-10-26 00:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| ea491f7b-8628-37d2-a5b2-bcb605ea07de | -3.473 | -43.3144 | 2024-10-26 00:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 67829107-4102-3266-b88c-0d8045fbdf3e | -3.4915 | -43.3368 | 2024-10-26 00:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5b50fa4b-00b9-34d9-88ea-27db5f151f97 | -3.4917 | -43.3136 | 2024-10-26 00:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 98499c0f-f3f7-3344-bf6e-d14b4bbfc725 | -3.5943 | -44.9833 | 2024-10-26 00:45:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 9e30863b-541b-33cd-a8b6-0eb7a5ff1418 | -3.5944 | -44.9606 | 2024-10-26 00:45:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 7798c8f3-45ce-3228-86b3-a7033384cb1f | -3.6129 | -44.9824 | 2024-10-26 00:45:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 3f592b3b-1db1-38b1-b181-82545a432f2b | -3.613 | -44.9598 | 2024-10-26 00:45:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 9c3c0696-8b58-3612-86e1-bf7a2463ecdb | -4.2979 | -48.6523 | 2024-10-26 00:45:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 24c10013-dc85-3f0c-bab7-e3a5a17750a1 | -4.5613 | -48.0358 | 2024-10-26 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 40402226-438c-3d9a-9e9b-cc231a15335c | -4.5614 | -48.0141 | 2024-10-26 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| add87f03-99cb-35ea-9532-492bf6985f5e | -4.5799 | -48.0349 | 2024-10-26 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 195.7 |
| bfcdd200-d40d-3390-aa26-3e7e16e5afd4 | -4.58 | -48.0132 | 2024-10-26 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 91a5f40e-8cbd-3560-a739-fc21f9995b53 | -7.6474 | -63.4584 | 2024-10-26 00:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |


[Clique aqui para ver as próximas entradas](README8.md)
