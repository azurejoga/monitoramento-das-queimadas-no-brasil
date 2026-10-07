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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4d81885-5620-3341-9742-d6e3f511c8d3 | -2.96063 | -54.16747 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6d9116d-1106-3602-a355-4dc5b5f0cd2b | -3.48439 | -55.43661 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eef2e82-1cba-3066-ae68-d4a39429a2c9 | -3.11454 | -53.70462 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e155f38-040f-3349-871a-036a2d1901a0 | -3.05881 | -54.1503 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecc08aa1-e9f1-3d4f-9e49-54ca99f8312e | -2.92258 | -54.19408 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4391a61c-96fe-3e42-93c5-f5b46e7b08db | -3.66802 | -60.62804 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 764897af-0530-333b-8046-b1f4e10e97a9 | -3.2763 | -53.8652 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa036630-eb7f-382f-8479-b9c95b9219f3 | -3.73468 | -59.44671 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52338bc2-2a5f-30aa-a991-19c7090b0543 | -2.92234 | -54.10795 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a68e866a-87a3-3a2e-b41f-a4279eff2de5 | -3.27465 | -50.40215 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eb53a3a-c461-311a-9eb7-ef370d33abd1 | -2.94697 | -54.19068 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1f3123c-2fb5-3478-a837-2e212a9a4e64 | -3.07657 | -54.25346 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 578730a0-554c-3aab-8afb-af6dd6e926c2 | -3.68047 | -54.19939 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad9b73d9-11eb-3b72-a9e0-0bba53bfcab3 | -3.10731 | -54.16492 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6432da64-0e8a-330c-9a1c-c0d0ebb663c4 | -3.38129 | -58.19508 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25e6c71f-b765-3c0e-a7bf-050837f2a4c5 | -3.51573 | -54.66729 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 22c5715e-fe3f-31f3-905b-cec6b98a8fc7 | -5.68378 | -53.49361 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 727de8b0-6baa-3a9c-8b6f-791d4cff8a34 | -3.28444 | -54.03382 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6a38f05b-4dc9-3723-ae3c-ede5426f9ab2 | -3.51119 | -54.63114 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a0eb863-0f95-3ea4-bf68-03464b2bb05e | -3.52058 | -54.63615 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4544d90-f2c2-36bd-bd17-8ce0efbbee31 | -2.95775 | -54.1419 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb37328-dd16-3f1c-92ff-0142f9ca8c08 | -3.29279 | -54.02422 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 975f9ab2-1979-370d-b86d-bc6594c86c4e | -3.2822 | -54.02623 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74f9319d-bacc-3f22-8439-54395ed19484 | -6.731 | -45.8007 | 2026-10-07 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4fd9af7-7b69-3e2e-991a-2f439d8f38b0 | -3.06948 | -54.14474 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6ba8833-4440-30d7-b3b5-0e4562e1f424 | -3.96976 | -56.05587 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a110e27-9bf7-3329-b81f-2717b05429c4 | -2.97604 | -54.13392 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5dac8f6f-b8f3-389d-9a34-f9abc21b3c1e | -5.01567 | -50.94506 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2b0b7ea-1259-3014-867a-48d06a3fa8ee | -1.79642 | -57.1098 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fdb52435-808a-3c96-9b38-7f54b833bee0 | -3.18474 | -50.57213 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 591820b0-cf32-3b4a-ada6-9b526d576bed | -3.67716 | -55.94617 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f014201b-602d-3797-ba32-ef3c5103fc60 | -2.57278 | -54.01444 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 043f9709-aa4f-318e-80b5-84396e4b52d3 | -2.77616 | -54.08498 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ae25f4e8-bafa-3a1e-bf08-e31ec9a63e46 | -3.26942 | -54.04237 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 0c49ecb1-5feb-3f0e-918c-57d307934c83 | -3.22306 | -57.88662 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44c85eed-50a2-3406-9499-b2b28db7b205 | -1.7976 | -57.1023 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c6d748ad-bd12-3d3e-a053-2ce72107e99f | -4.38265 | -59.90693 | 2026-10-07 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4792e74-fb47-3026-91cc-fbb5d06f064a | -3.07665 | -54.27492 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb8a123-28d7-39df-9813-099089e30d41 | -4.10343 | -52.06454 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47d4bc35-dcef-3c20-9e78-9450d111a4eb | -3.5262 | -54.66536 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 485ffa85-2ac8-319b-87af-eceb4e43085e | -2.84277 | -54.07365 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8dcdc03b-8750-3466-83e4-1c2bfca7baae | -3.73566 | -55.98352 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95b50d35-3fb5-31d5-8bf0-3414274c85bd | -5.95819 | -55.34934 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c283e463-0e93-32e7-b4ce-60ba0eecc344 | -2.37819 | -56.13359 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb934a4-e9a9-3d90-987a-34259d73b958 | -4.10278 | -52.06876 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 464580fd-fdd5-3eec-877f-24426b4b2e53 | -3.85258 | -55.8462 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8771319e-e1f4-3964-9c42-ac7ce3a0570f | -3.85913 | -55.99904 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6495434c-e7f0-31f7-88f6-715df3aef7b4 | -4.58889 | -54.92284 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 581cd435-05bc-3368-8325-08b8bedb3543 | -3.53704 | -54.64208 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd256d23-eb61-3b3f-a596-7d9a06b8b40d | -3.5316 | -54.63073 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06da7922-ca97-3b77-a190-fbdda3da895b | -3.22209 | -53.88243 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d042681d-0335-325a-a7fc-f026e6923bc8 | -3.01712 | -54.13311 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0bc77fa5-6aa2-3306-8d3c-4a537d9d0d37 | -2.7366 | -58.19023 | 2026-10-07 05:04:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b1c9477-7080-3057-a286-426146ac3b2f | -4.52467 | -54.98401 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ace299c-96d6-3100-b133-20345801152f | -3.01744 | -54.24076 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6708574-4488-3315-8265-5624cdf8d95b | -3.86794 | -55.83447 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee6f473d-a8c6-3c68-ab1b-5693b859a61b | -3.89794 | -59.32758 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64dc28bc-5b0b-36a4-b618-91c00bf9e419 | -3.10343 | -54.16793 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12e33b59-0597-37dd-9121-1bdbff4ef5b5 | -2.38873 | -56.13165 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80553ce6-1aa9-30c4-94b3-626e8f5db785 | -3.29227 | -54.04951 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f3697c76-c6c0-3d0f-ab41-409696a7af08 | -1.28386 | -54.55827 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 01468d0f-a796-32c6-a5e2-38f6a1479792 | -3.36945 | -50.67768 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1abb0c76-5b3a-3ad3-a291-dc7bfa2c4ebb | -2.87661 | -54.20493 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6990741-4371-3cec-a2c6-2b4966e9de9b | -3.52943 | -54.64461 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e73d98eb-9bee-3e86-b690-aa26138ad7df | -3.6213 | -54.60185 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2cbcfe2-e85d-3390-b5da-5e2cde9bd146 | -2.78037 | -51.67791 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 624b4675-fb6c-3b79-bdc0-7920da95c82d | 0.79093 | -59.19779 | 2026-10-07 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89e05a9f-c822-35af-a67b-eab39181af03 | -3.23606 | -53.88094 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0076432-e19d-3364-b6f7-7ce48fbf38a2 | -3.5048 | -51.69145 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5b45c79-74ec-33b8-9ca1-bebd20aad0da | -3.10064 | -54.16389 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31cccfdc-43ca-32a5-a39b-bd3f831a08fd | -6.00151 | -53.50071 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9ef13faf-c0f4-3680-9da3-8a501f90f59b | -6.21595 | -52.78772 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e148a894-74bb-3eda-98a4-e27bc4825ba7 | -3.08268 | -54.25798 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9770610-4b92-3149-a719-dc12e3f7cfc6 | -2.85553 | -59.21438 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7d78b9-b3e8-3a62-a91f-e88b8e41c912 | -3.23496 | -53.88807 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df20b05e-2050-328a-a827-c5cf1a3271fe | -3.5041 | -54.65486 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3422f975-ab61-3394-a671-6867224a8f85 | -3.0594 | -54.16835 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a196903-2010-3fa6-94b2-a58753d035f9 | -3.66336 | -60.63102 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cbb6004c-d231-3cea-8cd9-ef6e27bbb163 | -3.09241 | -57.64066 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11a4adae-219d-3301-954c-0767e5905bfc | -5.67628 | -53.49631 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5921fb98-000b-39b3-9923-0e0768c5b54a | -3.96569 | -55.81865 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a86251f-9550-3f06-993f-8715d6d87dac | -3.97031 | -56.05241 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22f03de1-12ea-3e1c-bf0e-63f8bd525da9 | -2.87684 | -54.11533 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6229b7b5-4a8e-3afe-8c7c-fab238826ca3 | -2.7757 | -54.11003 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 2b3d9316-b569-3e4a-ad55-7af72cc809e8 | -5.6757 | -53.50016 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe7888f9-35fa-3652-a7d2-f43600d429a2 | -3.14054 | -51.02578 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3ba8c68-73d2-3310-9734-8645e981c8f5 | -3.11179 | -53.76663 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dca3c9b0-cd6a-34cc-97cd-0eebbfcca876 | -3.93542 | -52.18753 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9599cbf0-8d81-37d9-923e-23195c67ebc2 | -2.13143 | -54.79631 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| bd9b8e75-2f6f-3a41-b2ed-6cf64569227c | -2.57684 | -56.14692 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df4d306a-2dbe-3629-8587-e3789a209e5b | -3.00274 | -51.11797 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25cd3bfe-155e-3545-9a45-deba50efead9 | -3.27653 | -50.41658 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dd2e8595-2094-353b-ba76-f0ec4b515ceb | -2.9224 | -54.12951 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aca6513d-ddf7-3d7f-951e-9a7f674317f9 | -7.27169 | -45.57118 | 2026-10-07 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7fca749-130e-3aa8-80b8-6aa7abc6abdf | -3.05334 | -53.94368 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 477fc856-704f-3e59-819c-ef757d437608 | -3.12859 | -53.7031 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be17c654-7bf7-3390-8189-ab6dc2eaca0d | -3.06104 | -54.15783 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 815f22d8-9d81-3a53-8faa-797b4e5d6e98 | -3.87669 | -55.82174 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9676668-4368-37ae-a5c8-1418955ec490 | -3.67444 | -57.06939 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3065ad83-61ae-3a89-9d4f-fe73b99995ba | -3.18076 | -50.5458 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README77.md)
