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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a5fd6c9-4115-391a-b41f-06daeea2e79d | -1.21122 | -51.78329 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bac7f249-8216-3052-9c4b-57063a3f4fd3 | -7.89687 | -44.21824 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d54fb6a-81fd-39ca-ad9e-8843bab6326c | -3.76559 | -51.92951 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1fcd955e-773c-3892-96e3-a32b2f2e3f6c | -3.50669 | -51.01965 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35c3dca1-d777-3173-9428-a80e02791d79 | -4.10192 | -48.48093 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4885bb1-21d0-37d8-8e10-259431eb23f1 | -2.28788 | -50.59285 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a29653e2-4a96-3b82-a4ab-ae38fe4ec8a7 | -5.76353 | -46.17426 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c52ceea0-1fd2-369f-9df1-bd3af5bcb1ae | -3.71019 | -53.7519 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 30628247-84cd-329c-9862-cf60e825bdb5 | -1.63608 | -52.67547 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44e79bc1-a896-3d0d-8a87-803c926735a8 | -2.00119 | -44.79589 | 2024-11-19 04:46:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1ebcbba0-6d09-3486-a3c4-6e4fd4bf6b38 | -3.8972 | -50.08694 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91efd1f5-984c-3275-952a-fc42ff43b5d5 | -3.69252 | -51.15863 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 825eddd8-da52-3c66-971f-cdbf13e724ce | -1.24342 | -51.78436 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be951c8d-581c-3fb8-acaf-0f4aa4c5353b | -2.28181 | -50.58841 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07598974-d322-36b0-aa7f-4a2a4ce15f4d | -3.79624 | -50.25515 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8541b98-9987-32ec-9157-d12a8541ddb0 | -1.37548 | -52.08209 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5a47c50-b730-3a98-b1ed-5a538641a2bd | -3.59701 | -53.99548 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 180d5127-95fd-3675-9af5-5164fe991dc0 | -3.3446 | -45.36245 | 2024-11-19 04:46:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7942649b-8749-3561-ae5e-8622444e439a | -3.04528 | -49.46246 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29b80904-cf37-31ee-ae73-c108236c8025 | -3.10485 | -53.74303 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 164ebad2-2d74-37a1-a380-e4daaf972749 | -0.85834 | -51.86394 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8b56a61-e7b6-3d0e-9189-6bfc87981637 | -3.91901 | -42.41505 | 2024-11-19 04:46:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 56703b8f-4b5c-3176-acb4-bed34753595f | -3.06997 | -53.2829 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e06e43ae-a2b8-3ee7-a407-8b57cdaaabd5 | -0.0032 | -51.23238 | 2024-11-19 04:46:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c523345-a5c4-3aaa-9895-1ac21555c2ef | -1.9866 | -53.13892 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1995218-2773-3e33-b8c7-8e1bae44515e | -4.05714 | -49.99845 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2009dd1-364c-3491-95e6-d676bd035dc4 | -4.16276 | -40.71231 | 2024-11-19 04:46:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcf1b690-564c-32e3-be64-e8ba852d6e0c | -3.05227 | -54.40327 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 946237be-532d-3ddc-9420-fd2877163052 | -1.99756 | -45.34831 | 2024-11-19 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f5d9ec99-97d0-3df3-88f5-289530096f0b | -2.38513 | -53.66866 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9b0f853-6515-3dc9-b1da-aa1cbccad0a8 | -1.50634 | -52.12115 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61c0f914-7422-3bf9-ace7-5a936274680f | -3.29051 | -50.61984 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c8e121-e186-3355-94b0-04b0d0547d9a | -3.23132 | -42.69538 | 2024-11-19 04:46:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df5f5380-cadf-3043-8eb2-b7c89e0c8caf | -2.95875 | -51.41342 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eeb2c3c3-ceee-3aa7-89bb-d16016a489b7 | -1.06255 | -51.74892 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e111944-6d5c-305c-9b9a-4ae8b53c8b94 | -0.11228 | -51.42945 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7dabd52-b603-31de-b31f-8c84fd665a96 | -1.39166 | -52.42657 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d3477c-9622-3ed7-8ba5-dd1a757b033b | -3.14326 | -52.98118 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 840f4bd8-1ec0-38db-9635-a16eba4ee8b7 | -3.52656 | -50.24121 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f47d53b-381c-3291-9dd3-9dceaacdce98 | -3.32969 | -52.99775 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 018c6c9f-28d1-3a4f-ac7b-40d4eac5fe6c | -3.0888 | -54.66155 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8c6dac0-a90f-31c8-9661-16ff4ca51d75 | -3.40792 | -53.30106 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e435fd6b-e2d3-3c1f-918a-d900b616bb72 | -2.54481 | -53.98522 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6070289e-3e8f-3753-b580-59ea3f08ac42 | 0.07775 | -51.40748 | 2024-11-19 04:46:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5fd76a9-4b0b-3155-a40b-c7ae72fb4590 | -2.39686 | -45.79191 | 2024-11-19 04:46:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71fe1340-1ba5-3ff2-8847-a80fda63009b | -3.37455 | -45.32998 | 2024-11-19 04:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90009ffd-ea77-3a3e-8965-741e3eb132fe | -2.59183 | -51.7134 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aff32425-203a-3589-894f-7d6696ba8aab | -6.30885 | -47.86761 | 2024-11-19 04:46:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4bf78b4-ea92-3e8e-a0ad-04386bf6fc81 | -1.5466 | -51.11081 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74404d88-3310-3fe0-a0eb-1b16307fc862 | -2.16464 | -51.97099 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a57e9cc3-841c-3e67-82a5-9b00b204dd54 | -0.20559 | -49.39521 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 709b1dfb-4a31-3a07-86a9-15dfd7fda2d1 | -3.60294 | -51.05642 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62ca4973-c0c5-3ae7-aa84-2d34e932f2cb | -3.0082 | -51.44609 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c772e254-6a91-3b50-8102-1a05208c6cf7 | -3.08499 | -54.66094 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b79d441-197e-396d-9bf7-ed2921dfe8e8 | -3.95481 | -49.99999 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2cafbb67-0653-3aa6-a106-8446b552f8d9 | -2.12283 | -48.55045 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3eaae73d-923e-37af-b594-9ede02a7cdff | -2.25926 | -48.98409 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89471fb1-36d8-3cd0-9e7e-272a95f137a3 | -0.92818 | -51.64678 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b17beb81-0758-3a67-afc0-faf3297a84fb | -3.52063 | -52.10313 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce226d8e-f93e-3b2b-a395-c998424ca428 | -0.12298 | -51.4274 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 90b3067f-92a3-3f87-bd91-a525fe32abd0 | -3.36497 | -50.81797 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 062e5ec3-00e4-3420-b686-debd9fa71b56 | -2.69037 | -51.80143 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9726fe3-7405-3040-a0dd-27b0e8ce9cce | -2.72796 | -49.38128 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f25527a6-216b-3ed2-b79b-c057847e7f14 | -7.99701 | -44.37859 | 2024-11-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dee6d002-cc19-3ecf-84fa-d3e00269aede | -5.50697 | -46.5498 | 2024-11-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3c3a324-2d50-3fda-bd78-35ee26261d7e | -1.76237 | -51.4499 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b24d4193-d740-333e-a164-55bdf9cd4817 | -1.06413 | -52.38907 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfbe15fe-e7ad-3495-b370-7397368de66f | -2.59463 | -51.71747 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7de3967c-30d1-3882-8c7b-940e0053f8be | -2.69093 | -51.88576 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f9d0b33-409d-3e5d-b937-eb291968fa81 | -2.19537 | -50.68344 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91e6a5e2-57c8-37a4-9c83-79edbeaa7a80 | -5.45537 | -49.68788 | 2024-11-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dab0ccb-6f7b-33be-b384-c33bc9e8d249 | -3.28138 | -51.24314 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2aeecd14-d0d6-3506-b474-73abe2a438c4 | -1.92259 | -54.06096 | 2024-11-19 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84e64355-7523-3f9f-98f5-631a75e9e7bd | -3.76993 | -50.16283 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cef1773-29fb-368e-86b1-6cd4796c592c | -3.50338 | -51.01914 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 435ae02a-5b4a-3604-a5f8-f96a0f47a3f2 | -2.95138 | -48.31828 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5176be90-ad51-343e-a333-0f6d636c5b68 | -1.04842 | -51.75048 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a094dcb6-e625-372b-afa4-9594d1ffc74c | -3.57616 | -54.55068 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0931a227-7651-3624-97a6-cce500481c09 | -3.75412 | -51.02705 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d269e3c1-e7c9-3ecb-b1a0-03306614ae9b | -1.62698 | -52.40379 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e60588c1-69cb-3709-bfdd-a9c6ccb03b08 | -3.00433 | -51.44907 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e525d7ad-586a-3af2-9936-f9a2019a986b | -6.23779 | -42.50816 | 2024-11-19 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b5b6a0b-c227-3791-90a6-d04ba6b692c3 | -3.98824 | -49.91615 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3fe159d4-5ca8-31ab-b7d1-6d56b72a2398 | -1.24461 | -52.04346 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b5398b6-9d00-3505-91b3-ff71940f9525 | -1.20783 | -51.78276 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 184ff4f0-0a28-3f56-8137-c988dd42a0c4 | -2.18272 | -52.74928 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c93b34-1a6e-311b-9a01-a2f87bd66a21 | -4.27502 | -50.58786 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4af41ba-c77e-3ce9-ae14-fa973a6e0db7 | -4.3866 | -47.75714 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e52cad3a-5a68-3c0c-8149-486d7129eb46 | -5.98516 | -45.35497 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e961eed4-f29d-3c84-9439-c8726b81d815 | -1.21795 | -51.79162 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e6381a6-c26c-3205-973c-c9d476860707 | -1.06293 | -52.39671 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a692124-f662-330c-96b2-1451806cf4df | -1.81623 | -50.91042 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 903caee2-f75d-3a29-a675-61b59cc9ef13 | -1.86592 | -53.19599 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aede7097-5def-3d5b-b107-618d62fb0ca2 | 0.04307 | -51.70367 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8772dfc-e792-30ee-a6d6-a7c5b0b78fcf | -1.20444 | -51.78224 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1613d19-db2e-3614-9f44-75c10f5608e9 | -3.80253 | -52.25428 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5ba769d-0d01-3dd5-bef7-ad2f52d324f7 | -2.93236 | -48.33101 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b09056d-262e-3da6-9bcf-a7e161dadbc6 | -4.55732 | -48.01661 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| bdbd3131-7104-38ed-8c64-899df855cd7c | -1.62494 | -52.6224 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1468083f-6780-3079-9e8a-1c17abf81350 | -0.85294 | -48.75332 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README29.md)
