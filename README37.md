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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d46eb1d1-03fe-3a0f-9a60-66a94ccba619 | -2.82538 | -54.12953 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3901efff-ca67-32f5-b9a9-443488e29cc7 | -4.02769 | -55.50526 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84adc740-8ea6-375b-9098-b386b32a108a | -2.81522 | -54.10476 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6788fb9-0400-36dc-8f9a-17e648a0eb68 | -3.10919 | -53.71484 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2ecde57a-6424-3695-9681-010e7f58c314 | -3.08527 | -54.17326 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| db194176-e864-3623-a33d-fe6f479cad0b | -7.22078 | -55.18685 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 235a87c0-a44e-3ebc-acac-790969ebe4fd | -3.58882 | -54.31294 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9680ce11-76dd-390f-add8-0e244a972875 | -3.10793 | -53.7445 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04d4442b-61bc-3b7d-83bd-0f918c9691d9 | -2.79962 | -54.11384 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d39237fe-6f9e-3c6b-926a-1b518b6260a0 | -3.72751 | -57.15088 | 2026-10-05 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7e217fc-a7b7-315f-aaf5-690d542e7b2b | -2.58008 | -51.87127 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f626541-7bc9-3d05-ba5d-7f7f7205d6c4 | -2.92868 | -54.07585 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b0f89a-87df-3f5e-8fb8-ab78d5d4470d | -3.57113 | -54.65473 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c3ef4a-4391-3cb3-a1fc-9eea7f1276c0 | -2.80996 | -54.11549 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c5e2ffb-45b1-3c4e-a27c-836f6833a57c | -7.43277 | -63.56852 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a418b21-9a9e-37d0-b255-b58c59d34d15 | -3.13416 | -50.34472 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 149e250a-8b10-3d8a-9f1a-0f9b2d514925 | -2.87664 | -54.11837 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e07a67e-181b-36d9-bdd6-1945d46f02d1 | -3.29991 | -53.83818 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 163a66cb-8d77-3ea5-89d6-61bf10854fe3 | -3.45807 | -54.59379 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| bdc5b124-6d4a-3d5b-a2c6-be1842572560 | -2.85539 | -53.92022 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59e9533e-da3a-39c9-a2cb-d43330dfb2ac | -1.98181 | -54.42223 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 037c39b7-9bc5-3e65-b0c6-55aa47464099 | -3.01874 | -51.37514 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e0d9ab6-ad31-3c28-a721-d6758b9a28bf | -4.11663 | -49.07018 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a81f0d7-c9e2-3b0b-9a3e-f4656420ed02 | -6.8903 | -43.67151 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 725e52b2-a687-3c90-b463-6e5fce014ba1 | -2.98871 | -51.04921 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f24c15e-0ae9-35ec-b676-bdb500fe5270 | -2.89804 | -56.67437 | 2026-10-05 04:57:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11cffac5-8e30-3b13-adb6-e974fb066e89 | -2.91474 | -54.09668 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 375f4bf5-83b3-30fa-af7a-2b6544f58ac9 | -3.80589 | -47.48724 | 2026-10-05 04:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7f0bffe-8957-3bba-8dc1-be54b48f3db4 | -2.91112 | -54.11915 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b1f234c-787d-3272-b714-d96684c525d4 | -2.94151 | -54.12788 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35218ae2-8047-32c3-9ac7-852967835815 | -5.50802 | -56.16611 | 2026-10-05 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34e75e07-bc58-3aae-93d0-5dcdad4e1d92 | -2.78076 | -54.09932 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 979c1023-74e3-3e1f-ac05-3c4ecbf99dad | -3.11365 | -53.73048 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57c3a6b6-80f3-3663-ad95-08eebd75ecf0 | -6.0883 | -53.48718 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 989defcd-2156-3132-9be7-aef0abffecb5 | -6.05505 | -53.48192 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe77b3b5-4147-305c-948d-8e6484963143 | -3.12111 | -53.70555 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 59490218-cc6c-3a03-89ab-37bf7f1871a8 | -8.65923 | -54.55686 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56f6faea-e0e8-3d0b-a82c-6b8dd53acbb6 | -3.10909 | -53.73721 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0a64d4-74ea-3773-91cb-fc9cd7de4467 | -2.93419 | -54.10744 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29099ef3-442b-3bba-9b3f-3ac504bdadfc | -3.30097 | -53.85334 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 183ad7be-c470-3505-82e2-2aa2d712919f | -2.53809 | -58.03261 | 2026-10-05 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdc1c2ca-ee60-33f1-905e-8c74c1d46ba4 | -2.91335 | -54.12721 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97fc5735-456f-3cb6-a621-674a5e0c3b5f | -3.05109 | -54.21029 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d210c4f1-bd3d-353f-861c-7be06107e87e | -3.46679 | -50.10083 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 072813ce-c85a-3885-954c-634eac3194e4 | -3.31798 | -53.85603 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d6ec8c7-c815-3760-b7b2-7760d6f4a21c | -6.2091 | -52.83459 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b49e3845-3d75-39d7-bb13-56f9bb3a9ee6 | -6.91132 | -43.67795 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c989d4fc-8374-3044-b64c-1c68ab5ce15d | -3.05425 | -54.16832 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25a8d57d-1c4d-3fa8-bd59-f723512742dc | -3.87712 | -55.81091 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ac85812-436e-387b-8b91-a89951655eae | -3.09833 | -53.73924 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 91fcf4db-6edf-3930-88a9-d2046c667ec5 | -2.78826 | -54.09665 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a979a49-661c-3cf1-8e20-dc6c0e7ff3c8 | -2.98795 | -54.03551 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f7aa0be-18cd-3957-9523-38a85e3da3b8 | -2.15251 | -59.22984 | 2026-10-05 04:57:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39c69b36-829a-3cd4-b18a-a0abd08121a1 | -2.84607 | -54.13282 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bda159b-de0f-3164-848d-a3a7dda773ec | -1.87969 | -56.28537 | 2026-10-05 04:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 028f4c50-0ff9-3bed-9c59-5ec027f4c934 | -2.79049 | -54.10471 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee86c4ea-a5a0-3f35-858c-dd2a15f624e8 | -2.82995 | -54.21177 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a87331b3-a7db-30de-b883-dd3adc4aef9a | -8.66096 | -54.54613 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fbf1f3fc-d850-37e2-a0d4-e2a3f3870285 | -3.15131 | -50.44014 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3844b870-a33f-3320-a823-a8532594710a | -3.30554 | -53.84657 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d07846c2-f304-30fd-96b6-e1b945592af1 | -3.07148 | -54.17107 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 38f0b446-b724-3e3e-bf09-1d33098913ca | -2.15395 | -59.22664 | 2026-10-05 04:57:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad08ef6d-bc31-35dc-ac6f-e88acf50dbc9 | -3.30777 | -53.85442 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1047c01-1aa7-36ef-9a5c-36c727ab545b | -7.19159 | -44.30709 | 2026-10-05 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1724f2e1-140c-3140-a992-7397ec9d62d8 | -6.20104 | -53.44024 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 538133e7-fd73-3229-a946-b2837642483a | -3.28056 | -50.01534 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 99ac9f82-2422-3bf6-8431-610dcd682d22 | -3.13798 | -53.73061 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ff88225-5d8f-36b1-bc68-c2c286db0c08 | -3.06638 | -54.1587 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4921e756-4737-38df-8cd1-c85a5aeb4ad9 | -3.27845 | -53.81989 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d67c0de5-65fb-30c2-9678-af333f6cc36e | -6.0099 | -53.51022 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7ffe2f4e-2850-39aa-8cad-e1ced2a102b9 | -2.22521 | -53.71663 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62999c33-ac21-3658-8c4f-b5a63d90e3f8 | -2.92799 | -54.16814 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af635aab-d54c-3fc8-8b85-3d6184b296a8 | -3.4777 | -55.43184 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a996c906-bf19-3a24-94bd-b683130c034a | -3.86251 | -55.83094 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf3e679b-39a9-3750-b12c-b5a0b5aa8449 | -2.82254 | -54.12521 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12a1a433-b10f-3b81-9dba-1467e369e3f6 | -2.24344 | -51.9165 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cbb4e24-5e16-3d30-942e-a130fc3262a5 | -2.93697 | -54.20055 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8478c8f-e6d2-3bb3-b1d1-d81bd320ed89 | -7.72277 | -45.46383 | 2026-10-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45b5ac37-ec10-37ad-a866-5a2d4be5e4ac | -2.95918 | -54.15003 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d7a6b091-7cc3-3110-9fc1-50f51b3d2210 | -2.80023 | -54.11009 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad2490c-5597-300b-b035-57bbf8cb9d37 | -3.50257 | -52.95444 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 986775e9-d260-36b3-95fb-91c859308a85 | -3.10241 | -53.71377 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0549aedd-30d5-314d-a7e8-242029b7d2ed | -1.47578 | -54.52893 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0b82e72-a52f-3584-a5f8-8822c3a85f07 | -2.75737 | -45.54677 | 2026-10-05 04:57:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8982a0c4-d153-3852-83a9-02eccf5f8caf | -7.32898 | -44.36707 | 2026-10-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60efbd63-aa48-3766-92e3-b4290a2fe1eb | -2.59415 | -51.84925 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be0655af-187d-3bd4-b1e9-08328d66eacb | -2.89187 | -54.08535 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb317960-6ed4-32a9-9699-b8e8b02e0c6c | -3.70782 | -50.64392 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ce9c9e53-445a-3533-8a37-1dc75fc3f9dc | -2.84911 | -51.28788 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e84ad082-5d9e-3e80-b5bd-258dda09408c | -3.30331 | -53.83872 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 394c58d8-8831-3a25-9e41-82ddfc278484 | -6.22283 | -52.79073 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c925dfa6-e453-32e2-b80e-3694e40c8293 | -2.98356 | -54.10762 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fb4294c-fbe5-3984-bd12-4ff80c91b496 | -3.11588 | -53.73829 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea367ce1-941d-33df-9734-b04e527482cc | -3.46964 | -50.10509 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25810e9b-60dc-385e-b3dd-1becf11fb291 | -3.13632 | -53.71915 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 498a6b6e-b7f0-3804-bc4c-0880e2e1e0b2 | -1.22767 | -55.91916 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 176740c7-ef8e-38de-b031-069e637fd418 | -3.47406 | -55.43129 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c909d330-480d-334d-9aae-ef487e9964bf | -2.92411 | -54.14823 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f31c9b9-1f74-3881-bf04-762fa8d01e79 | -3.37724 | -54.10005 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65f68bd4-1359-3313-9f91-ffe3c0befb0c | -3.11093 | -53.70395 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |


[Clique aqui para ver as próximas entradas](README38.md)
