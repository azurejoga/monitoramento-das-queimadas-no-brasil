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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 820424f9-8048-373c-818f-b1e6bcdaaa92 | -3.62494 | -58.61689 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e9f332d-ef3b-38ae-be25-c7368e31586b | -2.93602 | -54.11129 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| b3865ed0-9cd0-3bbe-8f86-0354336ccec0 | -3.54409 | -60.51976 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| cbeaad6d-8206-3695-86d5-020c614e443c | -5.98235 | -55.37992 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6c2aaefb-d726-3c08-a10c-0c6d9dbbc7f2 | -4.21914 | -53.62234 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b0ac038-d759-3fa3-8676-76dbd8a2c012 | -12.29102 | -64.16181 | 2026-10-05 17:34:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c714283c-bfba-3ccb-8516-38ce0a57e2d5 | -11.08148 | -45.714 | 2026-10-05 17:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 603ede05-16ab-3685-a560-03a48af15efc | -8.81836 | -72.72647 | 2026-10-05 17:34:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d395c38b-2120-3c87-a3e6-9896d3a8c48b | -3.23669 | -57.86882 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cf234559-c658-3ca8-b7a1-4edb8ba098bd | -3.65321 | -59.16013 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bfb3d2bb-c6c3-315c-adb3-96e445dc66e1 | -6.37514 | -55.21224 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 47690c19-7e1d-3329-914f-ecfcfed59ebe | -3.66932 | -54.53364 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ae9f4865-4431-35b4-897c-d0f4c1e84dba | -3.76669 | -59.40163 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0f4d2e71-ae26-3fc3-8125-59e9d996c967 | -10.593 | -63.55913 | 2026-10-05 17:34:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0cf0fb1e-d772-38a7-af67-52b3f9ae3eac | -3.0969 | -54.17498 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 43445eee-1b5e-3872-bb83-448042c74d52 | -5.95873 | -55.34499 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7da4c5f0-d3c1-37af-8fc8-520c11a2f0c5 | -8.27103 | -71.12497 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9dc56ba7-bc4b-3b5d-aad9-0a5a6519acc2 | -2.90254 | -54.07802 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6b01ee1b-6d06-376c-a059-87a463441df3 | -2.89091 | -54.15161 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c380d764-5da8-3937-a942-b62de62a1c22 | -7.27979 | -72.71567 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c4e32033-6044-354d-8a64-787841f25745 | -6.81539 | -70.45139 | 2026-10-05 17:34:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96ccf9df-0e3f-3841-9da1-5cd8108601b3 | -3.18181 | -57.8595 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 248298d3-d52a-3acc-bf3c-633e569b7136 | -10.3083 | -63.39559 | 2026-10-05 17:34:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8c57b376-c082-3e21-b204-4660c58bfe77 | -3.19254 | -54.09905 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7519451a-1ae6-396c-ae2b-dac59a5e03da | -3.5047 | -58.54207 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 511be9a3-0363-3305-85b6-9cc62cf423cb | -9.10649 | -48.80608 | 2026-10-05 17:34:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e889563c-50a9-34da-9ce8-c0aba1488945 | -8.43525 | -70.26919 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92b20461-a116-30b0-88cb-585e8a70dd40 | -3.21799 | -57.87927 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 46cc99dd-ef0f-3787-8f99-b6cd517c99a7 | -3.59442 | -55.29093 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ffaa0ead-ae59-3f95-8577-a2eb83c7746b | -3.01626 | -57.91818 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 24321c83-9162-3e73-a3de-bfd7cfb21721 | -3.74476 | -59.41599 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52cc3680-9e59-3b89-83f0-35e56b1eea33 | -3.0087 | -57.75361 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 58e21bc8-54e2-3670-a723-61fdc7156cbc | -10.92233 | -69.80891 | 2026-10-05 17:34:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b6585d85-a8e1-3aa1-a55a-c6cbe38cccda | -7.6216 | -73.09911 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 82d32caf-50da-3d8a-98a5-65d45e99d76b | -1.85573 | -50.6307 | 2026-10-05 17:34:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1354f4b1-9df7-3e1a-b36c-6647303f643e | -3.06279 | -54.16602 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 12e6a792-f29f-33b2-a998-ff7252b20bf4 | -3.67376 | -60.61248 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 01922df3-81b4-32dc-ba1b-1b1271880b0e | -2.43763 | -54.83499 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e029af6f-2c2c-3b49-8eae-24ac7c150b64 | -3.00738 | -57.74523 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ebb65058-f212-3e61-a9f2-bb109c863734 | -8.35721 | -70.07533 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 42.9 |
| ab609956-9778-3379-8611-817983f1db26 | -3.82207 | -55.61306 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 04469c62-b9b9-3059-bd34-b0ea4813e16d | -3.6997 | -60.16233 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ff91189-76f4-3c84-ab38-9acc36168f32 | -3.40114 | -59.52488 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 16b89079-d965-3370-92ad-d69284ff45c7 | -7.24124 | -73.09514 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8dd79d17-e768-3f0f-aa9c-b8e5badcb3ad | -2.98126 | -54.10068 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2f6adca1-53c4-33d8-a269-e4ababee8833 | -2.95102 | -54.14702 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 370251e3-f957-3c00-8876-190fdbca404e | -2.68929 | -49.03371 | 2026-10-05 17:34:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b5a3f542-12ad-3fb9-aaf5-fda447873f5a | -2.95484 | -54.14159 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e36b32c4-e8d8-3675-977b-d8349efb834d | -4.37071 | -55.42375 | 2026-10-05 17:34:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 23468fbc-066e-39fd-a67b-9660c5f44faa | -2.945 | -54.13849 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 8fd954a1-2274-3ebc-9432-d90e20801af5 | -7.63697 | -72.50059 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 30e03be3-03a5-3fd0-bcfe-e7d3f18c33e3 | -7.36784 | -73.14556 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 01d7dca9-a977-37ee-a949-ed60ac607372 | -5.8923 | -55.53199 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d8918da5-c1fc-3493-8bef-f7cd68b1f2be | -10.31803 | -64.97595 | 2026-10-05 17:34:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 67751929-6fd5-338a-922c-71db09173066 | -2.77209 | -57.06766 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a87b1e29-ea53-3520-a53b-a8f9a1711916 | -8.07663 | -71.30434 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7d792f09-0a16-3131-a819-4b722647bdbe | -3.11821 | -53.70376 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 25f74b3b-a231-3461-810f-aa75bf6a4a38 | -8.54543 | -69.9831 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d6d243d2-72e8-32a3-8559-82b22ac1f066 | -3.51506 | -59.55844 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a84e1202-7eee-3799-bedc-74f8582951d9 | -4.39425 | -59.55751 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f69bba75-0934-3f91-906e-ff3f75b94b13 | -3.48055 | -55.42669 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0583f752-ce55-3255-b5aa-aea72c9dadab | -13.50879 | -61.13087 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 041c48a2-963c-3b41-acbe-6fb136438e37 | -2.94089 | -54.14029 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 89dd7191-77ac-38cb-aac5-7be5e0d56e9d | -2.98589 | -54.04222 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 60a2f2b3-32a7-3010-b87e-70cd2064a773 | -2.93366 | -54.126 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d40e0eb2-f0b3-3dfd-812e-ed8e46d7fcee | -3.77006 | -59.40112 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 162e7936-97b1-3923-8a11-231eccabae21 | -7.84233 | -72.83794 | 2026-10-05 17:34:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4478ed47-e3eb-3a10-82f8-a450fbcf0c1c | -3.62795 | -58.93103 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 15335756-ce74-3f59-ba47-e520d5cac175 | -3.62377 | -58.60931 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 07f775e5-cb14-31ed-a1a3-5b6a39fb3efe | -2.99951 | -57.78927 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6ae8118e-b6df-376f-b1dc-581f94a3035a | -8.12566 | -70.15858 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e2b5ce4e-2836-30a6-9f42-dde2284d6520 | -3.75259 | -59.42212 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a2b2128d-6d0f-3895-ba28-41044ad1cdea | -3.54943 | -59.49111 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9423ba9a-b066-3680-8705-622cd464b025 | -7.46693 | -73.38234 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3455727d-707c-342d-b807-f9f31c6058f9 | -9.78229 | -47.79568 | 2026-10-05 17:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ca287576-5911-3b3a-b3c4-97f9ad95952f | -3.0698 | -58.42187 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e53adfa-bef0-3f18-9ca9-1466e6ddc097 | -8.28969 | -70.37297 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ca615f89-3edf-3f9a-9572-a74e071dc4f3 | -3.84499 | -61.29136 | 2026-10-05 17:34:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 29f3a5fc-cac5-3975-b7fb-912b3eb2a933 | -6.17239 | -55.37668 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e169d7b-b73e-3574-bdf9-9279cd201ad5 | -10.86767 | -61.4164 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8e8446ca-900b-3663-9927-5887cc3cc3df | -8.78638 | -72.80739 | 2026-10-05 17:34:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fa939572-e592-3ba3-8a81-575d5c212e9f | -3.37624 | -58.20284 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 4574e329-4f1f-3556-96ca-e52594939c48 | -3.28644 | -59.41809 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a25e20b0-52ad-3c78-9f42-628ebb4faa9f | -3.54078 | -60.52026 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 730b9dc0-85ef-3b54-a6d1-fe1fe60c671c | -3.62095 | -58.63692 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55f8d487-0b65-30d2-9717-515d3a2604bb | -3.06928 | -54.15363 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 910915e7-15c0-3312-b851-9047078a44a1 | -3.32623 | -59.4746 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 3a178849-6fc2-34d4-9cf7-bc267e8a39de | -2.85745 | -51.28193 | 2026-10-05 17:34:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a8ab5a3a-7ecd-3084-9bf1-d44a59de0abe | -3.7442 | -59.4124 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f4c107a-1f63-35c7-a1ea-484214be9577 | -10.87514 | -69.42343 | 2026-10-05 17:34:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 99.3 |
| a066e3a4-e1c6-3a6c-9a77-6d9b0e3436f0 | -2.96446 | -54.11267 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ff23df43-0433-3739-b529-a3aaea51dc52 | -5.81465 | -53.84314 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 73a266b8-1f33-3c52-9d1d-67728c017883 | -3.28982 | -59.41757 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ed6cfff7-3f4d-3c79-b121-54de86a592b4 | -4.12151 | -55.0145 | 2026-10-05 17:34:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9f39506-29e6-3c24-9ce6-a6c00a959401 | -3.40826 | -58.01385 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ccd82be1-02db-34f5-9b7e-9d4863218d6d | -5.13279 | -60.32073 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 12e9130a-e3c5-389d-b1e7-bad9e05ec41b | -3.67977 | -60.54109 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 62bc0f42-a692-3d33-b33a-d2e7ebfba8fa | -6.35627 | -55.14622 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 51618ed2-418e-3170-97e3-f9765858b0a7 | -4.06263 | -54.04359 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 92dfa28a-8e0c-34d1-8efa-09296bc9cdd1 | -2.99674 | -58.43702 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README140.md)
