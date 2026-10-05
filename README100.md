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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8095776d-d0da-38c9-8181-279bc1628892 | 1.16537 | -50.73433 | 2026-10-05 16:41:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b25a0890-6a3e-3f56-a6f5-2a92aaa25660 | 3.94695 | -59.62272 | 2026-10-05 16:41:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f168f946-0ac8-3253-92c6-8db038f3fe1d | 3.46707 | -51.53284 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 17.7 |
| b4f28e70-76a5-3924-b9cc-7202b56d9a36 | 1.85667 | -55.79094 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2d8551fa-b7bd-3235-a250-8939e8abf19d | 2.2903 | -55.90149 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b053fd9d-de1c-3a00-a602-b5214be54518 | 3.57498 | -61.34085 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3f961598-210f-3d74-9b39-7e6c7f7c433f | 1.84009 | -55.81056 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5b53f51e-01c4-30fb-98d9-1d0e9fa17db6 | 3.53488 | -51.50645 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 69a19267-ee43-3052-a6bc-ee764c408334 | 3.53432 | -51.51009 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 03b7ba76-b1db-3a30-b223-e44d2dee7642 | 1.835 | -55.81421 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 495373d7-bd5a-3260-bfae-a3d21b2c6661 | 3.52866 | -51.50179 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e6f04a1d-2a71-3247-ba11-6e7c2531f9a5 | 1.5046 | -55.64799 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fd4bdbda-d451-3772-bd54-2acdd232e2e5 | 2.54845 | -50.91512 | 2026-10-05 16:41:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 430e1935-c9b8-315f-8256-b6dc29942b0a | 1.85092 | -55.79891 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b90172ef-ff68-384b-86cd-f6e5bae44c80 | 1.73365 | -55.62545 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 44a83f3d-b671-3763-8031-80037a865479 | 3.56543 | -61.35924 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1b0b56a9-203d-3128-bf63-dbcf6d9982c9 | 3.11789 | -60.58794 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7e938b53-2629-3ebe-98ed-3131dd969391 | 0.80323 | -51.15118 | 2026-10-05 16:41:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fe9cdbb5-7ddc-342b-aa8c-1aa4f9fd56f0 | 1.11099 | -52.59642 | 2026-10-05 16:41:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f5445555-bfef-3e49-a442-f19de8a7736d | 3.07451 | -60.60781 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d277a166-801d-3231-adbf-bb81377f98c0 | 2.07051 | -50.88833 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b29e28a3-bf9a-34b1-beaf-2c394b9bb4a2 | 2.14454 | -55.9691 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5a63b1d2-f440-3aff-96df-ca02f0d0fa8e | 2.4007 | -50.89991 | 2026-10-05 16:41:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e6debb76-09fb-374f-9186-ea1c08630bb3 | 1.83941 | -55.81489 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2eb55b96-e2c1-3ba8-8665-c09011a11f75 | -0.68479 | -57.99768 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c0333319-e8b2-3113-b3d1-017eae56aca7 | 2.62856 | -51.01167 | 2026-10-05 16:41:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 42919f7f-e67a-3697-9755-153d2ac5103a | 1.8181 | -55.55165 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| ff053a41-d591-331c-b397-3494102c620f | 1.86372 | -55.77441 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f8f5efa6-78b5-3f4d-bc1f-70a81043ac3b | 3.35659 | -51.34169 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 42250a6b-421f-385f-946a-083d3462933b | 1.88118 | -55.7502 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 50df0b0a-2086-3bef-85dd-5a60789609b6 | 0.37113 | -50.67851 | 2026-10-05 16:41:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 219cf42e-4f02-3f4d-afa5-25d736f72593 | 1.9276 | -50.93211 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2ebfe616-c6b0-399f-8f8d-a3c7123f4b2e | 3.62862 | -59.97013 | 2026-10-05 16:41:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 916e99b3-a33c-3462-80c5-1c2711015ce3 | 1.89102 | -50.66058 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d94756b2-b0cc-369c-b63b-d1de6a13fab8 | 3.52471 | -51.50491 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 08402666-12c1-3c23-9326-1de6d743ab67 | 4.45986 | -60.10984 | 2026-10-05 16:41:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 11e7ebfd-facf-3b2a-ab0e-e0faa8660ee3 | 2.26944 | -55.86322 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 98afc91b-b0ff-3a7a-9427-ca6be4e60cda | 2.15274 | -55.97486 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d53b3313-4dd6-3b52-a445-c1ff6c097330 | 1.51404 | -55.64507 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| d419f86b-b459-3d12-895d-d2bce27f9a59 | 1.51337 | -55.64931 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e6c9d21a-2725-34f2-8f9f-d82ba40923ce | 3.9525 | -59.62347 | 2026-10-05 16:41:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 302299ca-8f72-3337-ad0f-8d5a450db765 | 1.85494 | -50.69498 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 90800c38-9222-3d7c-851b-3a65dc41021e | 3.57872 | -61.35629 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 40c933e7-51de-35d3-a74c-8d539ca6d884 | 1.15981 | -50.92881 | 2026-10-05 16:41:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d700a31-6ac8-3f87-9468-bfab77730a99 | 1.78994 | -50.62726 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4ea3fbaa-ddf9-3851-b0cb-f2cf225e9bcf | 1.70631 | -53.1351 | 2026-10-05 16:41:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 5079bbfc-e137-3ab3-ae04-96844bab6842 | 3.53036 | -51.51321 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5504b5c0-8461-3582-a991-7ad9280c1298 | 1.50526 | -55.64374 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f37294da-817b-39d6-a981-a41657fa3540 | 1.058 | -50.03606 | 2026-10-05 16:41:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdb8ac07-ba08-37aa-9955-f46ce8c0afae | 1.86894 | -55.77028 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| cbc3b713-aba5-3afd-a711-af23ca5b621d | 1.17391 | -50.76862 | 2026-10-05 16:41:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 71ea8e28-75dd-3427-8483-326c7e5a0e6a | 1.81744 | -55.55577 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c51b5ad7-aecc-381e-8a3d-f028bd02631b | 1.60076 | -51.00335 | 2026-10-05 16:41:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 58c7b7cc-b59a-3113-9980-1fe92dd7c4df | 3.0731 | -60.65303 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 55b911c1-87d3-3f94-828a-803fb72d9330 | 3.78782 | -51.77403 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8d6976bd-1365-3471-91f3-2cb902fd4e0b | 2.28334 | -55.86093 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 784ba47d-69a1-3517-a35b-29b8c84f60a5 | 3.56627 | -61.35436 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d737a971-fd46-30db-8ed1-33ee37b16166 | 3.5671 | -61.34952 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 45a32c30-6f98-3d98-b7ea-bb56bd2827d9 | 2.48688 | -51.26982 | 2026-10-05 16:41:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e8b4734-b811-3de3-9359-076ae7b41b08 | 2.06661 | -50.8914 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c94a653d-a978-3a7d-927c-a6faf087f0b1 | 1.84517 | -55.80689 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2c72dc56-7823-301b-a78b-2fec9d5a0e90 | 1.73999 | -55.61353 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b424c1c5-4e66-340f-9f23-98ff14a391d7 | 1.90352 | -55.72294 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b7d34735-dd9b-35f0-9d56-b57c477eea16 | 1.84434 | -55.81065 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4d22415e-8d5e-32e3-823c-4de548daaab2 | 1.92869 | -50.92493 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 4efb85ac-d92f-3a30-9a99-501da642cce0 | 1.79639 | -55.54848 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dde72417-fb79-393a-af09-be5725aaf230 | 0.94083 | -50.20307 | 2026-10-05 16:41:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ae1abf92-fd1c-3147-9494-e1a4578a3a16 | 2.08711 | -50.90614 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cd4dfb18-dcba-3662-8242-73c190e714bf | 3.87178 | -51.79856 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9f52d149-36e8-30ea-80d7-d092d2dc905a | 1.85026 | -55.80321 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0a369f31-3a13-338e-9c2d-b4bf2429e255 | 1.6151 | -55.77823 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9166dc75-23fa-3433-83a7-e6732d73230c | 3.53205 | -51.5023 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f03e2ba-e7de-39a6-bc89-85ea70c86b88 | 1.72862 | -55.62904 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2b9818d7-5e86-3a08-986f-f36059a5f200 | 1.91431 | -55.71155 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| eddff60f-a23a-3965-8938-7989e28bc1a0 | 3.5281 | -51.50542 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b40eba5c-f197-3898-b7b5-351988ac8731 | 3.07967 | -60.57698 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 5800a6e1-ed0e-3eb5-ab6d-7723da503936 | 1.86385 | -55.77391 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a1e8ab30-efd6-3672-ab64-775d2d6f5e8d | 2.14521 | -55.96477 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 80075f73-966e-30cf-baac-d0b8de417e58 | 1.85666 | -55.79041 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c1e1c96-c3bf-3972-b519-18dc8f659daa | 2.01065 | -50.91952 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1fc8d3c9-79a2-313e-8bc5-ea8f2e956e3e | 2.44313 | -60.09869 | 2026-10-05 16:41:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29a84446-3d20-303d-86b0-68d5f076a14d | 1.16592 | -50.73074 | 2026-10-05 16:41:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ced59bf-41d4-3723-9b88-8a453f7fbe36 | 1.85016 | -55.80266 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 66ee6f0a-f2ee-3b21-afd6-40a5bc21b561 | 1.61068 | -55.77754 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bfda630b-f86c-311b-b333-2fde809721e0 | 1.84584 | -55.80258 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 569c0f92-1616-353f-a7fd-753435b3333e | 1.83433 | -55.8185 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d51b52d4-ec29-3bfa-8149-e13738d66f51 | 1.11163 | -52.59222 | 2026-10-05 16:41:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5c9f1fee-8c17-3dbe-b0c6-23d6075d1937 | 2.44387 | -60.0985 | 2026-10-05 16:41:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 42aa48e7-fd5b-3a65-9387-5dbb03ed862e | 3.77571 | -51.58071 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac66b43b-be27-3479-9e83-b3044dfe206b | 1.07091 | -52.49577 | 2026-10-05 16:41:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d35a056a-c616-338f-bf29-6773aab0879d | 1.81009 | -55.5462 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dc0ded99-3b32-3265-99ef-f638716fb100 | -0.71809 | -57.96572 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 514a2c04-9a47-30aa-bebc-b12c6e8d8f36 | 2.14388 | -55.96863 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6c5e52fd-3870-3d2d-8b41-b63794df0c7d | 4.02996 | -51.613 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9d3de2c7-ed25-3de6-96ff-e35b28ad0553 | 3.35321 | -51.34118 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17539562-8e95-39e0-89c4-509856ffd49d | 2.14902 | -55.96497 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f3aa3354-b9dc-3157-91cd-b0c534bf7eb5 | 1.45796 | -55.65852 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| fd4b4905-935d-30cd-a306-c4967421e566 | 3.58201 | -61.33703 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a7eb2e7b-076c-3ee3-8d1c-ba95f33f1f5a | 1.93248 | -55.71004 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59439221-b3b8-3014-a351-e1679706be71 | 3.49862 | -51.4855 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README101.md)
