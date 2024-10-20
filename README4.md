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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 931e79e2-e77c-3197-83cb-ca11145ffa3f | -1.0343 | -48.254002 | 2024-10-20 00:15:17 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5474ee4e-ffba-3be8-b6b9-8f03706f03a2 | -2.2199 | -50.4594 | 2024-10-20 00:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c3d3765d-7cf7-351d-80b3-c3a6f037fe66 | -2.2808 | -48.5941 | 2024-10-20 00:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 05b1eb8b-f790-375b-87b8-802aaba42d21 | -2.2993 | -48.5936 | 2024-10-20 00:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 209.0 |
| 8534bebe-ed19-3782-82de-9e8b8ea0f56a | -2.2994 | -48.5722 | 2024-10-20 00:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 8a43bb85-3a11-3e98-bef4-792aa4528fee | -2.3178 | -48.5932 | 2024-10-20 00:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 25cc7aaa-8d8c-3819-918c-80198e2b870b | -1.765 | -52.040798 | 2024-10-20 00:15:19 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea4c0a9-b154-3b42-a438-3be97abbb6ab | -1.7554 | -52.0429 | 2024-10-20 00:15:19 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd7e6e4-8932-39df-b7f4-6a9a8666e436 | -2.7773 | -49.3067 | 2024-10-20 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 35e680ff-f219-38f1-bb41-ecb7a28c8256 | -2.7774 | -49.2854 | 2024-10-20 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 95f7f696-5aae-3cd3-9395-5dbfc5a6fc79 | -2.7958 | -49.3062 | 2024-10-20 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 191695cc-a4e0-3041-ba95-f4a3db41dd4e | -2.7959 | -49.2849 | 2024-10-20 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 341e9ecd-cc70-38fa-8aed-039b8994b730 | -2.7981 | -48.6873 | 2024-10-20 00:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| b86595a9-98c8-341c-ac8b-c77795cc0ae9 | -3.0478 | -51.0226 | 2024-10-20 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bb4e8321-e663-377f-bb96-2bb1dc682e27 | -3.1278 | -54.3662 | 2024-10-20 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e80c742d-f730-32b4-bf06-75d063878de9 | -3.1279 | -54.3462 | 2024-10-20 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d0184d23-8b6d-3373-94d6-9c88b28d808b | -3.1462 | -54.3658 | 2024-10-20 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 64ecf9b1-49a7-3ce7-a076-7c18ed7fe0d9 | -3.1462 | -54.3457 | 2024-10-20 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| adb9fe79-77fd-3d3a-99d5-a6be69efaa9f | -3.3813 | -50.6788 | 2024-10-20 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 54299918-4dfb-3b77-817e-d009bbe92561 | -3.3814 | -50.6579 | 2024-10-20 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| fb418856-ebdb-318c-bdc8-ee3601496464 | -3.3997 | -50.6782 | 2024-10-20 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| d29cdd90-6d5e-332e-8277-475dadd75643 | -3.3998 | -50.6573 | 2024-10-20 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| c49c6a49-917c-3f65-a6be-798f40ce85d0 | -3.586 | -54.6941 | 2024-10-20 00:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 18588de9-3767-3b05-a780-1b9c1b7972ed | -3.5861 | -54.6741 | 2024-10-20 00:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 656f13de-007d-3f04-9323-161fc2b90366 | -3.6045 | -54.6736 | 2024-10-20 00:15:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 20c2517d-ea88-3bad-badc-f88aaabb5be8 | -3.815 | -48.866 | 2024-10-20 00:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 85437133-eadf-34d2-982e-06e970e4440a | -3.833 | -48.9722 | 2024-10-20 00:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| b51bef1c-78d6-300d-9cf7-db7d9542b04b | -3.8331 | -48.9508 | 2024-10-20 00:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 4fc4548d-616c-31e9-b471-2bd99260c724 | -3.8334 | -48.8866 | 2024-10-20 00:15:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 90be4626-96b7-3f9e-af51-406bd4d1cc87 | -3.8686 | -45.8254 | 2024-10-20 00:15:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 279a0ce4-8020-3040-9991-09323b705e7a | -3.9018 | -49.9884 | 2024-10-20 00:15:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 8389fb48-fd72-347a-ace7-9f1a05a76175 | -4.1985 | -46.6318 | 2024-10-20 00:15:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e36d2ff4-36e9-3d73-bbb6-fd20997dd0ec | -4.2478 | -51.0018 | 2024-10-20 00:15:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 40253b63-6c53-3d9f-9cc0-c49c03b74194 | -4.4899 | -44.7564 | 2024-10-20 00:15:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1a636233-f128-3295-ac7b-a00e3482d603 | -4.5085 | -44.7554 | 2024-10-20 00:15:31 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| cd97fde1-8d54-3642-9dd9-94012dfa5532 | -4.8925 | -45.8162 | 2024-10-20 00:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 468ec479-bc99-3e5b-b258-58e47aea7873 | -4.911 | -45.8374 | 2024-10-20 00:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| afe715ee-2b11-3024-beeb-b375486f2999 | -4.9112 | -45.8151 | 2024-10-20 00:15:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 81f109b6-b608-3184-8474-b56c05934339 | -5.2072 | -46.11 | 2024-10-20 00:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| e43b4e78-be66-3565-a935-48bfe8391311 | -5.2073 | -46.0876 | 2024-10-20 00:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 1438985c-02eb-310c-bfe4-7e39accece36 | -5.226 | -46.0865 | 2024-10-20 00:15:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 211c5051-1108-359b-a262-ab88ffefe0ec | -5.3873 | -46.9191 | 2024-10-20 00:15:36 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 79357fe5-813b-3fe2-8f20-085db68d488e | -5.3875 | -46.897 | 2024-10-20 00:15:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 647c2465-fc7b-3a36-8465-af0a4c88f9f9 | -5.4059 | -46.9179 | 2024-10-20 00:15:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 7c5b2552-0268-32a3-8bd4-c88fa4df47d8 | -5.4061 | -46.8959 | 2024-10-20 00:15:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 262.7 |
| 31cdc2e8-4f90-3b0d-855a-f7514aa6f2cd | -5.4246 | -46.9168 | 2024-10-20 00:15:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 867886c0-9fb2-33dc-a816-d5d3cdd8d978 | -5.4247 | -46.8947 | 2024-10-20 00:15:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1191be1a-e790-317d-a471-ec48f5387317 | -7.3637 | -72.881 | 2024-10-20 00:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 82d0b4b7-992e-3a87-95c0-0048238af0a3 | -7.3638 | -72.8628 | 2024-10-20 00:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 989f9a74-6295-3167-83ab-0fe9e43749be | -7.5841 | -73.0436 | 2024-10-20 00:15:50 | GOES-16 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 57c3cec1-0240-38a5-b5bf-80f9b31050f1 | -7.7679 | -73.079 | 2024-10-20 00:15:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8734af64-d308-3844-810f-30a990c207fc | -10.4759 | -48.2928 | 2024-10-20 00:16:05 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b1b61f8e-22d2-392d-95c8-3ee27390d9a1 | -12.4967 | -63.1874 | 2024-10-20 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a83e4980-a9b2-33d7-a56a-938684c96e83 | -12.5147 | -63.3014 | 2024-10-20 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9729bd01-939f-3602-beb8-008ccf3fb2e6 | -17.5939 | -40.2245 | 2024-10-20 00:16:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 108.3 |
| 20e90529-6661-3e6e-b7a1-811f6562b255 | -15.60651 | -39.61759 | 2024-10-20 00:22:00 | TERRA_M-M | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| d5883ca4-145c-3956-83c3-df0605b98bb0 | -12.61651 | -39.62502 | 2024-10-20 00:22:00 | TERRA_M-M | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c00b1988-7258-36c3-8bb9-66f7a327b494 | -18.4056 | -39.92713 | 2024-10-20 00:22:00 | TERRA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 58957bdf-0b74-3edc-869b-6fc29e613d01 | -17.93629 | -40.5613 | 2024-10-20 00:22:00 | TERRA_M-M | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f47244fd-4a6c-3435-912c-44541a2ded08 | -17.8737 | -39.80412 | 2024-10-20 00:22:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 95ed0d90-c2c5-39e0-999f-b481e9021d5d | -17.8724 | -39.794 | 2024-10-20 00:22:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 059419f4-6b9b-3f33-b846-327f5991f23a | -17.86446 | -39.80543 | 2024-10-20 00:22:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f4ded61d-7793-3b5d-894e-975a72307bf2 | -17.86316 | -39.79531 | 2024-10-20 00:22:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 0e4165a7-c31b-3d84-8405-526806054653 | -17.59828 | -40.22364 | 2024-10-20 00:22:00 | TERRA_M-M | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 152.3 |
| 18193082-4a82-3112-9125-040a9deabacf | -17.59694 | -40.21323 | 2024-10-20 00:22:00 | TERRA_M-M | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| eb407227-116a-3f8c-9607-1f6fb2b29bad | -17.58889 | -40.22501 | 2024-10-20 00:22:00 | TERRA_M-M | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 253.4 |
| 21464213-80a6-3acc-bd49-25f10f59e814 | -17.58755 | -40.2146 | 2024-10-20 00:22:00 | TERRA_M-M | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| dc5124e7-53fa-3676-b6bd-063affc7f414 | -16.88145 | -40.588 | 2024-10-20 00:22:00 | TERRA_M-M | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| beaede4a-4704-3d5a-87c8-ec4078b65e71 | -16.88012 | -40.57749 | 2024-10-20 00:22:00 | TERRA_M-M | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 71ac5f80-7563-343f-91db-32f56ffd4295 | -15.6078 | -39.62715 | 2024-10-20 00:22:00 | TERRA_M-M | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a1c93a0d-a101-305b-9139-34bd50471d5c | -10.01088 | -36.34493 | 2024-10-20 00:24:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 76cef552-edbe-3430-9e70-247ef2f08c59 | -10.00909 | -36.33322 | 2024-10-20 00:24:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a2c66fe2-05f0-31f2-affb-4938f3ca79c8 | -6.78208 | -46.42247 | 2024-10-20 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 32f44008-be8e-3757-9d4c-29719b4b810d | -6.63342 | -47.373 | 2024-10-20 00:24:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4917d789-43bd-332c-ab90-ecc0e75919d3 | -6.63043 | -47.35035 | 2024-10-20 00:24:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2740610a-46c7-3933-a103-274a440498ac | -6.62806 | -47.36807 | 2024-10-20 00:24:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 5926122a-9a9b-3970-a0eb-4ded3e76e094 | -6.15779 | -44.42934 | 2024-10-20 00:24:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ca485f62-3578-3691-b5c8-01ca3b2ffaa3 | -6.15397 | -44.43692 | 2024-10-20 00:24:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e05d925f-d041-349b-b031-a117a0f622e7 | -5.92504 | -45.50002 | 2024-10-20 00:24:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a4c2c94-fe69-3948-8512-1377867b4e89 | -5.82994 | -44.04964 | 2024-10-20 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cd75e917-a673-3f6b-a88a-be6a27e49747 | -5.82904 | -44.05618 | 2024-10-20 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9d2ae35d-eace-3189-b5f4-246c78993fbf | -5.82747 | -44.04416 | 2024-10-20 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6d22cda9-03bc-3d9a-b0a4-7962daa459ad | -5.56938 | -44.88337 | 2024-10-20 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9b2bf303-a54e-39b5-bd0e-091d834e4748 | -5.50682 | -50.57984 | 2024-10-20 00:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 988bc20e-766b-30cc-a612-b03265554138 | -5.47013 | -44.18419 | 2024-10-20 00:24:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0681831a-13ff-300b-b028-c9b639ae7e02 | -5.46846 | -44.17206 | 2024-10-20 00:24:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5c81cacc-6678-394e-b7a4-273152f47030 | -5.44289 | -46.36968 | 2024-10-20 00:24:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3abedd9e-c69c-3648-a716-3d781df09564 | -5.44062 | -46.35235 | 2024-10-20 00:24:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ae2bf38d-87a2-34bc-b5e4-e4ba76e1f63d | -5.41139 | -46.9268 | 2024-10-20 00:24:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 05f3c271-9353-3c17-bef4-1dbb7f55f41b | -5.4089 | -46.90755 | 2024-10-20 00:24:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| bcbd76ad-6945-3749-ac85-2b132fe8c8e4 | -5.39863 | -46.93466 | 2024-10-20 00:24:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 05b73361-c411-33a2-98f1-a5d417f6ba44 | -5.3986 | -46.92814 | 2024-10-20 00:24:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f09ec5aa-a9df-31cf-b4bd-04f2e9287b5a | -5.39615 | -46.90908 | 2024-10-20 00:24:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 01ed928a-987d-3614-b0b2-056aac5758c9 | -5.39602 | -46.9155 | 2024-10-20 00:24:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 039d68fd-cb9b-3fa8-a59b-97bcd1e089fd | -5.39341 | -46.89629 | 2024-10-20 00:24:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 82f15ae5-298c-380f-882f-e4edcd4d3506 | -5.3814 | -45.1245 | 2024-10-20 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 59fd4e3d-5bea-363c-88d4-355e76a2a328 | -5.24861 | -44.21429 | 2024-10-20 00:24:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bbb36103-9c03-33bf-aff3-cc1f9ff7873f | -5.22372 | -46.09689 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 632ad39f-7d96-361b-b5b1-844e3fae709e | -5.214 | -46.11485 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| db1636a3-ad7a-3bac-84dc-7faa2dba8458 | -5.21175 | -46.09773 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 122.9 |


[Clique aqui para ver as próximas entradas](README5.md)
