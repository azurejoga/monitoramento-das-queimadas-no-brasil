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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5c35c08-85f6-35d2-8cf5-0cd1ba99d148 | -13.0082 | -55.9699 | 2024-10-20 02:26:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 31350656-e507-372e-a14f-1ae6c1f78a83 | -2.2993 | -48.5936 | 2024-10-20 02:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 776f31ee-4b19-3a82-a07d-e709ba23a12c | -2.2994 | -48.5722 | 2024-10-20 02:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b699bc5b-f414-330e-9b61-754792ee656b | -2.7773 | -49.3067 | 2024-10-20 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1be3202e-5f62-3ae4-942f-ecc06b016214 | -2.7958 | -49.3062 | 2024-10-20 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a3bb32bc-5353-3cdc-957b-51637a86dd93 | -2.7981 | -48.6873 | 2024-10-20 02:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| cf043830-2588-32fd-b220-33c41eda921b | -3.0478 | -51.0226 | 2024-10-20 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4dce6308-36b1-37af-966e-511c1d5a212a | -3.1462 | -54.3658 | 2024-10-20 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 027739f7-7ce5-37e6-9eb1-22ca6b7112ab | -3.3813 | -50.6788 | 2024-10-20 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| af41614c-c050-399e-82a9-65c0870647f6 | -3.3814 | -50.6579 | 2024-10-20 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5d3ffa05-cb1d-3448-b8c5-4f9c2b711dd8 | -3.3997 | -50.6782 | 2024-10-20 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3d488226-5f36-343f-8ef8-bb7940264113 | -3.3998 | -50.6573 | 2024-10-20 02:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 29b679f8-f83e-3bcf-81ea-a3558e06479a | -3.586 | -54.6941 | 2024-10-20 02:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 9bb79526-c414-3a02-b053-051326bd7b53 | -3.5861 | -54.6741 | 2024-10-20 02:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5efd8ebc-3fcf-3484-b629-b826296e33a7 | -3.6045 | -54.6736 | 2024-10-20 02:35:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 4b4a9082-297c-35ba-8ef3-9f7af1aed29f | -3.9248 | -45.7557 | 2024-10-20 02:35:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e630bd3f-9703-3a81-92c1-a13a3a870edc | -4.1985 | -46.6318 | 2024-10-20 02:35:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 77bb6093-0bce-30b3-b910-be221877e600 | -4.2478 | -51.0018 | 2024-10-20 02:35:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 1a342733-3338-3a72-a0fc-11f74f0de015 | -5.2072 | -46.11 | 2024-10-20 02:35:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e6abbfce-e3f1-3ce5-b13e-5b340d4ba5e5 | -5.2073 | -46.0876 | 2024-10-20 02:35:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 87746fa6-5d1b-36d5-9af2-748174d3c4ed | -5.721 | -68.6862 | 2024-10-20 02:35:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5918d41b-31b0-3a40-bd76-bdd0fae09cbe | -7.6815 | -47.3213 | 2024-10-20 02:35:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a013d093-fa0b-3549-bbab-ee3ef2c85c25 | -13.0082 | -55.9699 | 2024-10-20 02:36:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 819aad58-577c-34b3-a680-d7e190f76d6e | -1.165 | -53.6571 | 2024-10-20 02:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 0b3a1152-9aee-3a52-9e4a-70995056ab6c | -2.2993 | -48.5936 | 2024-10-20 02:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 027d497e-2fdf-3081-9773-afb228cdfc90 | -2.2994 | -48.5722 | 2024-10-20 02:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8c78dbb4-a1ff-3d7c-8211-7c0e025a1b5f | -2.7773 | -49.3067 | 2024-10-20 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 22b70808-6e92-3539-8681-2513e46c8a95 | -2.7958 | -49.3062 | 2024-10-20 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 668d4b99-2e38-30ad-9b51-79623c6fc032 | -3.0478 | -51.0226 | 2024-10-20 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f47ac74a-302e-3db7-9fcf-4214c91f1d59 | -3.1462 | -54.3658 | 2024-10-20 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d904ea07-3fd0-3d72-a9fc-b74a996075d4 | -3.3813 | -50.6788 | 2024-10-20 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 581ffe9b-4e3f-3eab-88f6-2299e8257d86 | -3.3814 | -50.6579 | 2024-10-20 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e7d136fd-5619-3b8e-b364-d782e35213b4 | -3.586 | -54.6941 | 2024-10-20 02:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ec72eda4-f822-3dbc-9253-f71b53572eba | -3.5861 | -54.6741 | 2024-10-20 02:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 34a6b435-e5a3-3682-9000-dade0aefb83a | -4.1985 | -46.6318 | 2024-10-20 02:45:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c2a3d2af-1ee3-3963-9cb8-4677c9f3caeb | -7.3637 | -72.881 | 2024-10-20 02:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 99b2cf38-e451-3822-b3ea-f3eeb6edf134 | -7.3638 | -72.8628 | 2024-10-20 02:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4bd5b58e-346f-3b65-9d08-b03dbb83383a | -7.6815 | -47.3213 | 2024-10-20 02:45:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 1b3e4404-15d9-3588-8a7e-3d5b846cfc20 | -13.0082 | -55.9699 | 2024-10-20 02:46:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 34b71aef-3d44-3a31-89ba-cffead996ca4 | -17.87018 | -39.8016 | 2024-10-20 02:53:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9706dcf0-c8dc-3e31-aa71-127e42defa10 | -17.86314 | -39.79951 | 2024-10-20 02:53:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 344e75cc-7ba7-3d77-86f8-7f2b2616b5a8 | -1.165 | -53.6571 | 2024-10-20 02:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| f4eae901-72e1-336b-9bf5-e536e7743e7d | -2.2993 | -48.5936 | 2024-10-20 02:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1b6b2246-e922-370f-b234-c8a85c997880 | -2.2994 | -48.5722 | 2024-10-20 02:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 87871b9b-5cab-3b0d-afc4-2c43293d32a4 | -2.7773 | -49.3067 | 2024-10-20 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 072e93ef-9e1f-360e-aaf5-2f02fda7d349 | -2.7958 | -49.3062 | 2024-10-20 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 95d4a5af-4622-3ed6-87cc-c9d8736ad0d7 | -3.0478 | -51.0226 | 2024-10-20 02:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| ac69b30d-5c06-35c4-866a-86ddaf0efb52 | -3.3813 | -50.6788 | 2024-10-20 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8007ee3e-e12d-3649-a112-71008307bd75 | -3.3814 | -50.6579 | 2024-10-20 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f190b156-2d8b-33d8-8b3a-fd96f5dfec7b | -3.5861 | -54.6741 | 2024-10-20 02:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 62d8c2a8-0c08-3c29-af0f-ec6375b45089 | -4.2478 | -51.0018 | 2024-10-20 02:55:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 5b10f89b-6918-3e83-aa55-999c67ee4b5b | -7.3638 | -72.8628 | 2024-10-20 02:55:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d1337bde-8c44-330f-b250-2b4d00397890 | -13.0082 | -55.9699 | 2024-10-20 02:56:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 904d1586-eb26-3ff1-bed1-9d5a3b5bebf8 | -1.165 | -53.6571 | 2024-10-20 03:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| bba417d4-ec0a-340d-8de2-5d99492037de | -2.2994 | -48.5722 | 2024-10-20 03:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 267b5564-4ac6-3de5-87bd-7aa4251dc54b | -2.2993 | -48.5936 | 2024-10-20 03:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b2d8fc6e-6598-3f34-a262-9fa6d0a6a413 | -2.7773 | -49.3067 | 2024-10-20 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 54fd8ac7-c7ad-3237-8435-b70945f46997 | -2.7958 | -49.3062 | 2024-10-20 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8700b8d7-b23d-3eae-a39f-7df5ef1ebaab | -3.0478 | -51.0226 | 2024-10-20 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| f981e526-4db3-3711-9b93-f086879a57ed | -3.3998 | -50.6573 | 2024-10-20 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| fae0dfce-cd77-3a70-a0cc-da750e8e94d9 | -3.3997 | -50.6782 | 2024-10-20 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5eafcf1f-b6c7-3983-8a52-61d7b22b3889 | -3.5861 | -54.6741 | 2024-10-20 03:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a9e7bf49-c456-3a58-86c3-897bd8174343 | -4.2478 | -51.0018 | 2024-10-20 03:05:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 5458eb42-bfc1-3e94-a83b-eaee773017ae | -7.3638 | -72.8628 | 2024-10-20 03:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bcbca601-e606-3aa4-a072-26ebaf375e59 | -13.0082 | -55.9699 | 2024-10-20 03:06:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 659c8925-8bd0-3d68-8426-eb54d853b7bd | -5.49911 | -35.41924 | 2024-10-20 03:13:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d28ac5a7-d43a-3064-adec-05497de520be | -10.13501 | -36.33532 | 2024-10-20 03:15:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| bec262dd-a1c5-3ffb-8b25-3ab613f071f2 | -10.13419 | -36.33986 | 2024-10-20 03:15:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 2eda3b9e-ce1f-3005-854b-580a2eb3354d | -10.13056 | -36.33448 | 2024-10-20 03:15:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5bbb6dd1-4288-3a9c-8733-06ea2a481c17 | -10.12974 | -36.33903 | 2024-10-20 03:15:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b17e86b9-2b20-3beb-a883-ee4c9a55a170 | -9.9175 | -36.19149 | 2024-10-20 03:15:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35c3fdac-3138-3d88-bc04-2ec82bf7fa50 | -9.91662 | -36.18918 | 2024-10-20 03:15:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 353c540c-110e-3a51-81b3-cdf445335a4d | -9.91582 | -36.19358 | 2024-10-20 03:15:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 468e12da-fb50-35eb-9411-a7e9f5a537ac | -8.9935 | -35.30153 | 2024-10-20 03:15:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 972eee30-2fcd-3ee0-ae7c-749fe7962b84 | -8.07288 | -34.97715 | 2024-10-20 03:15:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75c09513-9525-3097-891b-58da10a99813 | -7.63294 | -34.96145 | 2024-10-20 03:15:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3eb824a4-0995-39ad-92c9-1e6e6973a7b8 | -7.47453 | -34.84578 | 2024-10-20 03:15:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ecbb3a4-3914-3c17-994b-6f1ad3b38d53 | -1.165 | -53.6571 | 2024-10-20 03:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 33766bdc-b69d-36bd-8585-bb58bd5bd2af | -2.2994 | -48.5722 | 2024-10-20 03:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9d3b2be5-8b9e-3cfb-a260-1606484224f0 | -2.2993 | -48.5936 | 2024-10-20 03:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| f22a76bd-8d17-3982-9993-5aa22bcfa96e | -2.7958 | -49.3062 | 2024-10-20 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 65633328-321a-3848-99dd-a5b8feca1dfd | -2.7773 | -49.3067 | 2024-10-20 03:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 2eae88cd-0e59-3b53-84b4-24fcaf584507 | -3.0478 | -51.0226 | 2024-10-20 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 1b1c0fe5-be01-34dd-8146-2a6ac43fb1ef | -3.3998 | -50.6573 | 2024-10-20 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e80bcf30-5e77-3383-9ee1-33e57e9b9eb3 | -4.1985 | -46.6318 | 2024-10-20 03:15:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 947ba317-7fed-316d-9018-66981d20991e | -7.3638 | -72.8628 | 2024-10-20 03:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9302a092-7023-33a3-9e5e-9f13d79d747f | -13.0082 | -55.9699 | 2024-10-20 03:16:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| dd72ad8f-e327-30b1-a371-f9a58bde9ff9 | -17.86735 | -39.79923 | 2024-10-20 03:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| e2d00fd5-75c3-3c07-a0a8-0a12df97e9a6 | -15.22466 | -44.77521 | 2024-10-20 03:17:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4470b11e-dad4-397e-942a-585e9ba6696e | -29.86495 | -51.17216 | 2024-10-20 03:21:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 1543f3cf-b34a-3b14-9aa3-3f413caca7c7 | -29.8603 | -51.16785 | 2024-10-20 03:21:00 | NOAA-20 | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 731eff68-2b53-3005-bd9d-b3af6baca0e9 | -29.85787 | -51.17604 | 2024-10-20 03:21:00 | NOAA-20 | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 2d3a76b1-407d-37c5-b775-627bdf18b759 | -1.165 | -53.6571 | 2024-10-20 03:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 73568671-fda3-37a1-9edc-a474e16c37d7 | -2.2993 | -48.5936 | 2024-10-20 03:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ae898286-529a-3b5f-9496-a71a889f017b | -2.2994 | -48.5722 | 2024-10-20 03:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0bf4bd20-6611-3c92-96d2-963183597adc | -2.7773 | -49.3067 | 2024-10-20 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| bd4713be-2602-3b8e-868f-aad0ea5738c9 | -2.7958 | -49.3062 | 2024-10-20 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c149808e-c456-364b-8a68-e6c86f9af796 | -2.7981 | -48.6873 | 2024-10-20 03:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 389c3d8f-7369-38b6-9019-a5423907be83 | -3.0478 | -51.0226 | 2024-10-20 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| fa6d99e5-0b56-377f-8294-91837f11a802 | -3.3998 | -50.6573 | 2024-10-20 03:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README15.md)
