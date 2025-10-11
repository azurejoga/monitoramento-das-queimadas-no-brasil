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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1feafc9a-a562-3c3b-ae4d-3c0b6c15859e | -8.00486 | -44.45144 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ed587d7-0bcb-30b0-b5de-83d477a3852f | -7.5014 | -45.14135 | 2025-10-11 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5139bd5f-7898-38a3-9381-621147ad5d41 | -8.20939 | -43.34599 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a05cc148-6163-35f9-bd9c-bb7720c6bde8 | -7.67711 | -43.99175 | 2025-10-11 03:42:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7b123342-f977-32b8-9b7f-f3bb32142171 | -8.14608 | -43.33374 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3df40440-7ff3-3ab1-b208-2d1041f9eac7 | -11.44994 | -43.48556 | 2025-10-11 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cd95962-c4ef-374c-b840-d2dbaec1a177 | -7.8563 | -44.495 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4d0998d1-f246-3112-af32-e534d0910e41 | -11.75773 | -46.36767 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76797f85-fb70-382d-9b2a-488f80659c8f | -11.75471 | -43.3208 | 2025-10-11 03:42:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 785b2681-71eb-358a-9b63-62abfae58522 | -7.45768 | -46.86103 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0c48b30-733c-3a2e-bb1b-0348c5efa117 | -13.20555 | -42.33951 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 2b47d677-6dd5-3670-912b-cb67d305408f | -7.40813 | -42.97753 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 76b33228-bb48-3fb1-8e12-7f0af55b539d | -13.20831 | -42.34814 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| f60ce36e-8702-3866-ab1b-86244a48d253 | -7.33575 | -43.86905 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e2a4c8a-7584-3226-98dd-62666c0aa39b | -9.11606 | -45.07245 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1b667a9-6d4b-3796-bc3b-9df24011f4e8 | -7.85854 | -44.12431 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5c747cc-b2b6-376f-83c7-6faaeb40d658 | -10.15038 | -44.56427 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7b101b0-75f4-315d-8c2e-7347009a227f | -7.40681 | -42.97738 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 57bebc27-5deb-36dd-ad63-2eb67ed3703d | -13.21462 | -42.3372 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 71.0 |
| a55d18dc-8c42-3beb-98c5-e56aa7a48e95 | -7.85272 | -44.48444 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7cdc5d50-f234-3078-aa63-239ab76afc41 | -7.46161 | -46.86511 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d411327-6aa1-3db5-97aa-534d1cc9446f | -7.7387 | -42.41432 | 2025-10-11 03:42:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 91b12eeb-9755-3ca9-af48-ce2f5f36c890 | -10.15227 | -44.61242 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39f5120d-9eb0-3494-8714-dbcb4be0339e | -10.15731 | -44.55522 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8a549cb-4e1f-36f8-bd63-12f2849a2fd5 | -9.33335 | -46.11155 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 2b0d659a-d9d2-376e-8b5b-fd7b0a473cf1 | -11.89246 | -45.49567 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb825d2f-14bd-3db9-809a-953ad05b562a | -10.13828 | -45.77066 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c9744093-00ce-32b0-8599-e2199d458dd2 | -8.21033 | -43.34057 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3e74b9fd-6c98-3c4f-9b91-1ab669c952c7 | -9.34576 | -40.33987 | 2025-10-11 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eac943f7-15f0-33e9-9bc5-fa5209e6adc1 | -10.87299 | -44.19417 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c9701d84-2a73-3c04-a831-5e3f58a71704 | -8.01294 | -44.46111 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b1fb962-7591-304e-9a53-07cbaee8e397 | -8.20082 | -43.3232 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 4a9860c7-4c48-38c9-bdb5-13c4424a2fe1 | -9.1586 | -41.06308 | 2025-10-11 03:42:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f5979ca-54e4-301e-b43a-38eef729997d | -8.18788 | -43.32514 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1a4173a7-ad39-3003-83ba-f5ce89824c45 | -10.56655 | -44.51086 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d07dd118-e51d-3070-b93d-229b1d7b6ac9 | -7.42711 | -42.97515 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c8d6b07d-73e5-35bb-a943-ae60df294810 | -13.47351 | -42.25092 | 2025-10-11 03:42:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ea2fab5f-4106-3f6f-b0e7-a62a814a2f9c | -12.99583 | -45.22459 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e101b23d-60c8-3774-8ddb-a2fc7c2537c7 | -8.21731 | -43.37104 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f7b644cb-a180-3060-bd03-c85a1b93c0f6 | -8.19275 | -43.32606 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| e1f6cdc0-aad4-391a-bb2a-8f3c66cf206f | -7.74901 | -44.22097 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5a3a022-2d4e-313d-b9c9-0a8bafc4eeca | -10.20327 | -44.6051 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d31fd7cd-6ac2-3f7c-9d48-2253533f893b | -7.52932 | -44.60692 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c443b131-d6cb-3c5a-a1b8-b1b83196f9e6 | -11.13335 | -40.90352 | 2025-10-11 03:42:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0ed3a3c1-bca2-3793-adc5-11581d644619 | -9.11545 | -45.07573 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2835ca0-12ed-35e9-95e5-1f0b29218983 | -10.13446 | -45.76652 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6a110e1c-3317-3405-8124-166434da2e00 | -12.64 | -48.31828 | 2025-10-11 03:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0e96387-ba84-30a9-9a95-7ae01cade81c | -7.80332 | -42.42588 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 06ef2344-1a32-389a-81ef-b372ac7e43b4 | -11.7398 | -46.39931 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e86aa4ba-f649-3b68-a006-a48fadd8f59f | -8.21539 | -43.36944 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9eda0df2-84f4-3019-a6c3-6cc92b5a8f99 | -8.01341 | -44.46472 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9a2412c-ef68-39c6-b7b3-0f2e2182d59e | -13.21881 | -42.33796 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 71.0 |
| d1471be3-b9da-3953-a4ec-75a74ee8898d | -7.77646 | -42.41613 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3a17c97-c9b6-329e-9547-481208dafcc3 | -7.66436 | -42.57612 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e0024435-32d6-3465-a38f-81cc9391ad4a | -13.21391 | -42.3411 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 71.0 |
| bc65e2ba-0e0d-3cd9-b461-4dd6356d75fb | -13.21738 | -42.34583 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 3bf29692-b2a7-39c9-b2d6-8ccdfd0ff749 | -7.79461 | -44.11717 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bad4223-ef53-3844-ac2b-2b7bfd073445 | -9.32933 | -46.10618 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ca2c32a0-c211-39fe-b0cd-b1aca0aa575e | -8.21335 | -43.3522 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f5af1af4-3298-3275-ab8f-f52f15af8f8b | -7.342 | -43.8636 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9cd7ffe-a474-314c-a3db-20aeef0bb9a9 | -7.5347 | -44.60786 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf82c1e1-f4c0-3978-aa58-8f85ecc175f5 | -8.17422 | -43.317 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15b456c7-d59d-3ae5-9997-a222514db8f4 | -7.77101 | -42.4201 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46b0d8c9-17a7-31b3-bac9-62e24c50fcae | -11.76016 | -43.31689 | 2025-10-11 03:42:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bfc34cd9-c2a2-3570-b592-71d4fba671e0 | -7.40783 | -45.91846 | 2025-10-11 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2672f27-5754-33cc-bf42-bc90adabf719 | -11.75645 | -43.31123 | 2025-10-11 03:42:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2cfd2b5c-db9f-3768-adc6-956ca2d5d09d | -10.42307 | -44.99414 | 2025-10-11 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3055e37-24bc-35a4-9681-071c36a1b2f6 | -11.88718 | -45.4947 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31f7096d-e219-345c-9ed4-adbd77d5710e | -7.35393 | -43.85587 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdd1b8e2-65ee-3062-8e21-8e9b75545e7c | -9.81035 | -45.52308 | 2025-10-11 03:42:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1643ec20-eba8-3f88-995d-8df60945d5ac | -13.48633 | -42.01378 | 2025-10-11 03:42:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5c88c7b2-cf1a-397d-bbce-5f57e7e031d9 | -8.15869 | -43.31953 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 508180ac-a200-3b2c-8a63-71af63e9ebdc | -7.29264 | -45.56628 | 2025-10-11 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15661411-77c0-3bfd-b5fe-e5389e882969 | -10.87186 | -44.19428 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a9ac346d-25fa-3e57-a7d1-6e92a0711b0e | -8.21049 | -43.35302 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 44b159ad-a8bf-343c-8435-75c7b0e34532 | -7.52873 | -44.61021 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 249cca09-aefb-3596-884b-ad34bc8c1dec | -7.40906 | -42.97211 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| eb33c43c-52f5-3aee-b143-61230234f50c | -9.11669 | -45.06908 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b27f369-818c-3066-a730-2506ccbd16bd | -11.025 | -44.64655 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b502930f-9ad0-3b96-aec7-5fb8693a0600 | -7.46068 | -46.87003 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c6d646d-d783-3a4c-b208-ddf81106b0d9 | -7.34824 | -43.85818 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12b25e32-b61a-3a61-9ede-9a89d9185a86 | -10.1964 | -44.61351 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1efbda74-8e0b-3467-8977-42e21b8b00c2 | -8.20856 | -43.33596 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f476b79b-7f6b-3a7f-9522-6a1261dc18c6 | -8.14703 | -43.32842 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| af3c68b2-4046-3995-91de-fcea624de392 | -8.16355 | -43.32045 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ad7c4023-0552-3f2e-b5aa-b3585bfb2772 | -11.78358 | -46.38392 | 2025-10-11 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 690fbcaa-a7f9-3f54-b446-f52b32d05f3c | -11.9123 | -44.18209 | 2025-10-11 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| efa695de-6fa1-3930-b267-fcdeb5763aef | -10.163 | -44.55304 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a39e7da2-9b26-3f52-a8cb-a98a45258f30 | -9.81652 | -45.52044 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab4d92e2-e1ef-366d-a9bb-ff0deb604409 | -7.8646 | -44.47922 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1b6857c-d174-32db-b15b-04bd23bad140 | -7.85867 | -44.48177 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45f9f0cf-e2fc-3f96-af7b-b3a600a23bf9 | -8.40129 | -45.09321 | 2025-10-11 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b85175c4-135e-3ade-ab34-a8351e13dfec | -7.41204 | -42.98373 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5e474a63-5928-3641-966a-d4e4f157d509 | -8.20641 | -43.33419 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 6a7ad409-2f91-3b9f-9f35-24b6f46af23e | -9.39928 | -42.67453 | 2025-10-11 03:42:00 | NOAA-20 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 26ba9458-7743-32d7-9118-6215dcb8f280 | -9.4001 | -42.66983 | 2025-10-11 03:42:00 | NOAA-20 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1e9dad56-9319-3309-a1dc-93898d7964f4 | -7.67654 | -43.99487 | 2025-10-11 03:42:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eae8da2c-4007-3cbe-9b80-b6b8f867b174 | -10.13276 | -45.76952 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 187efa98-7c0e-3a18-82a1-2db5bd6e9011 | -11.74706 | -43.38903 | 2025-10-11 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c29363ec-3e3e-3e9b-a13a-02c77d09d28a | -13.22299 | -42.33872 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |


[Clique aqui para ver as próximas entradas](README12.md)
