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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c31b2fb-df72-3ad5-81a5-8ab90d808f8e | -0.96442 | -51.71559 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eccb3497-d578-3bf3-a1c9-818d673337d2 | -2.4666 | -46.56129 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18ec94f3-7ab7-3fb3-8fdb-efc65d0ad88a | -1.94762 | -53.33717 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a8fdd9d-dd6d-36a4-a892-37161ab137e7 | -3.82436 | -46.59525 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d63037b-d9e8-3499-88f9-ec2c1bd5849b | -2.74714 | -46.10276 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0592784-75c1-31ee-9651-5c19aad4247f | -3.01363 | -47.79526 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 638bf2d7-5c9d-3747-a7de-4dd69035afac | -3.1143 | -54.47606 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e1ef403-824c-3fda-bb35-838a000bab05 | -4.09362 | -44.85833 | 2024-11-30 04:40:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0797c065-d76a-38bf-b859-320a6854ac5b | -2.78486 | -51.71885 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5c9ea3f-2dfe-3246-bb6a-2879cf9cac0e | -1.85607 | -55.61615 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9717278e-3e4c-3ccc-80e9-4ca3748885f8 | -2.48207 | -50.36613 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a103e467-0d75-3d53-b580-6f34693993f3 | -6.37897 | -44.76005 | 2024-11-30 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73c9c9dc-963e-3398-83c0-9e91c8e87adf | -4.11136 | -39.9897 | 2024-11-30 04:40:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f26c6048-e22d-3cda-b409-5486b2aa6f57 | -2.45684 | -46.53263 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b1e4e4d-6edd-349b-935e-0996d3f7cd4c | -3.75505 | -54.73235 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 673ed0b8-3a16-300f-b23f-4a3d40605f00 | -3.16209 | -53.23893 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 77d198be-805f-36d3-bbbf-acfb58060a86 | -3.10566 | -50.36737 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a0f20bd-d068-3a9d-9c62-01514b2a0eee | -3.21183 | -50.2742 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb5159bb-7838-3213-bfa3-81839ab09aa2 | -3.60265 | -49.99572 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2748e11c-23eb-3d1e-8b70-060159312a95 | -1.5821 | -53.85083 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 446960e1-787a-3211-a4bf-ef482a0f5179 | -2.62228 | -51.75988 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ed043d6-0453-32db-92c7-47a505ee862f | -3.5026 | -50.45832 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc8fd900-1ca7-36fe-97fc-1e1e6f8969ae | -3.36431 | -50.40411 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fe675b9-f63a-3506-85e6-0deaf2cf5778 | -2.77977 | -51.92915 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6817d247-322e-3a50-955c-4e5677bf03f7 | -3.02692 | -54.02831 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27534258-8d7d-3d5c-8865-7d186dc6a32b | -3.22036 | -49.22291 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2769a3ff-4230-368e-9a73-93e637eee035 | -3.46464 | -53.88174 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fd4d0a41-6f5a-3e27-8137-807b603c5b97 | -3.82252 | -46.55214 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 897f1e38-23a9-305c-ad55-07c0f4ddf6f6 | -2.68377 | -46.28247 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eedced52-1698-3911-85dd-19096f9528a3 | -3.53004 | -50.19682 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cae08404-87a9-37cf-ac07-104191ef90c3 | -3.8314 | -46.54837 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96472403-ad9e-39d3-a1e9-cefa9a224e7f | -2.43682 | -48.64256 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c9c207-5b28-3ce9-acc2-c457f941c7f4 | -3.84304 | -50.08747 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b4f46db-5ea6-39bd-b1b8-a44f2a6d5549 | -4.08426 | -46.83101 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0e955f4-2efa-30b1-a218-296d6cc729be | -2.29103 | -50.5491 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3a30a39-e372-358d-abba-921351e64682 | -3.13902 | -45.9823 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 187ec9fd-bb54-3596-b317-3ecb252ee321 | -3.63523 | -54.16687 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dc6e47c-b914-3422-b13c-51bb379e9d25 | -3.61951 | -50.18907 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ba5da0b-9e07-313b-a2a6-7eb35eeb242f | -3.77812 | -47.49526 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cbb41f6-1051-3cad-8ae2-184f7a409674 | -8.31674 | -44.94598 | 2024-11-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cf5c64d-d3d7-34f7-88e3-5c868a22790d | -4.52543 | -45.7326 | 2024-11-30 04:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ec08719-8d02-3cc6-b02c-96be89e9505f | -2.26918 | -46.43132 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b1ce99-e6dc-3c8e-896b-be0142dbab6c | -4.70386 | -44.46978 | 2024-11-30 04:40:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f274afea-b8eb-3c1e-921b-8aa2ad8f4892 | -1.2301 | -51.81031 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc0dc427-4c09-3dc8-b2a9-8fd35819e5a3 | -2.72078 | -46.2281 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a777bf9c-9662-3e42-9e45-a76545025459 | -2.5186 | -48.46518 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 45bc5459-6b04-32a7-af7d-1d886c558c74 | -3.05297 | -48.52771 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e667715-a0e0-37e2-a0c9-962c2c16e9d1 | -2.18382 | -47.90691 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55afc24b-8706-3abe-a455-d6a91bfdb7f8 | -2.21172 | -48.38206 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7640a7ef-e431-378d-97d0-1c874ce35912 | -3.03211 | -45.11919 | 2024-11-30 04:40:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 16e16f8f-62ce-3223-9565-425d1c1d8980 | -3.08739 | -53.24921 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 780e7035-314f-3636-b44f-b94cf13f6ac9 | -4.13758 | -42.15169 | 2024-11-30 04:40:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb3487e0-d03a-32e7-95dc-0cf49862f60d | -3.37555 | -50.77245 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a7aef42-010f-3414-8eb5-21fdd4da050d | -0.89237 | -51.71853 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39473f0b-c5b4-3b26-8829-f520169561f3 | -1.12769 | -51.67601 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24d68361-a882-318f-bd8f-85b5e1263182 | -3.08269 | -50.25059 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d43f0ffc-d3b7-3a60-8f93-35996376bf3e | -3.14486 | -53.84417 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c313165e-97dc-3dc3-8f31-5cc89ab7b57e | -2.69699 | -46.86448 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 364d351f-037d-3704-b8ac-a2593e4704a6 | -1.59369 | -52.1677 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d900f6-ff44-38d9-bb82-fafa2e65a087 | -2.18366 | -48.38831 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d23770a2-7f80-3ba1-bfc8-4f5d7ae90d86 | -1.44421 | -55.13313 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b13ee33e-c687-31be-87a2-736e36130505 | -4.06472 | -49.063 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| feb90e11-3fa6-3e47-82a3-66ecae284b9b | -3.95141 | -46.68578 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f9a8123-8cf1-3bcc-aff7-3fd41537add9 | -2.82911 | -52.94318 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d775dc17-8e5b-305f-8aee-3ca961bb4fe9 | -4.08661 | -54.34282 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af14e14f-ced4-34bd-b2ae-a536ab412a34 | -2.55197 | -47.28366 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 086d9f6f-ceb7-3586-a346-a0691426d19a | -4.09174 | -44.85636 | 2024-11-30 04:40:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb49db86-d536-3c65-a320-15ecaa36f1f3 | -2.76877 | -52.9077 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 365b6a90-b268-313f-b37f-fb6cfe2abfd2 | -2.3236 | -49.08198 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f8ead17-f4b7-3011-acec-dc1424fcda80 | -9.09928 | -43.19606 | 2024-11-30 04:40:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 09cc0a48-eedd-33c9-ab71-211d95f799e0 | -3.58356 | -49.8783 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 752356a8-3b0b-330d-bb8a-f922afc15dc6 | -1.9692 | -46.44546 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5900bd81-5672-39a1-86c6-853ca3ee34b0 | -3.3762 | -50.72391 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22ac8f7f-d056-34a6-8021-6d3880ab36b9 | -3.05703 | -54.04765 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a193e6f6-831a-34de-beea-3e6d6535b17b | -1.15334 | -51.70123 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58add8cd-82aa-3481-bc22-fdad38357bbc | -1.05816 | -53.21405 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc4f38c8-75ca-3d13-b5bd-907ab28f1d54 | -2.90255 | -54.76925 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 165d2346-7cec-36df-9bed-bf2a7960aa42 | -8.3774 | -44.47948 | 2024-11-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31c4436a-3c3b-39d4-889a-faf7f67cfe6f | -2.98935 | -53.20689 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cca3815-5607-313a-90be-0c6548cb67bd | -2.37089 | -50.51248 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a0dfee1-503d-3a65-bfc4-da6ecec2c2ad | -4.0511 | -48.07753 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa12bc75-e544-3762-add3-c84cac80c453 | -1.12575 | -54.19465 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1dfe32a-c237-3f26-ba2f-a87ecff02a8b | -1.43457 | -55.25129 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| af9a8909-4d79-3b4c-b7e9-5c5f33157e8a | -3.59544 | -50.36304 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 848bed49-4a31-33cb-bf67-b6cc1958aa41 | -1.11988 | -48.33818 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41f25ae3-8a47-3736-87a6-3d1d35765544 | -3.05131 | -50.27493 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 406bdf7c-8ae6-30e7-8791-0ec3502612ef | -4.14449 | -48.2213 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd7d1a8-af2b-3f0a-8aa8-1cadce2039ad | -1.59731 | -52.28925 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5ca7450-b82c-338e-a7e4-8eed20695d29 | -3.01776 | -51.37064 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84e818d1-ce06-3d35-997d-063017c3aac0 | -3.3802 | -50.6984 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c27de76-d3fe-3d6e-8011-d085e06be88a | -1.28361 | -51.72862 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 631d3615-4883-3b82-b600-d3c0e7b97028 | -3.60593 | -49.97472 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c037b999-2b23-3921-a327-361a3544b7eb | -3.4977 | -46.40462 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d16fe21-9472-3b59-acb7-d10670e66561 | -5.92157 | -47.8183 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 45e3014d-3a52-3a98-932c-fe8812452e4a | -4.12603 | -48.84344 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc10b9ce-8c42-3533-a686-164f2528b154 | -2.51324 | -47.23377 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b89f653-57d2-3406-b732-baa33b993114 | -1.32694 | -51.67456 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4d60a3bb-c7ff-3113-9532-265428a44555 | -2.67066 | -53.03757 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fd456b9-293a-3901-adc1-5eccf73dc541 | -2.27959 | -46.43293 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c31f300a-baf4-3ecd-bfad-ea4ff52b07b0 | -2.83713 | -49.84381 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)
