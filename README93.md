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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5464a431-956d-3a57-a311-351c2b834405 | -5.95362 | -44.79464 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f60d517f-0a2b-3782-94f1-d02aa8485083 | -18.42913 | -39.95041 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| dec04cfc-754d-3de6-9715-e2d858d35a07 | -9.50152 | -45.65664 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0495c6b1-7474-31f0-85ca-b54902478218 | -14.49076 | -40.62262 | 2026-08-28 16:05:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 15a100af-1087-3231-8bc5-d89a491d2781 | -17.26621 | -46.02592 | 2026-08-28 16:05:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d757bb1b-47f4-3bdc-a6fc-756ed5ee11c9 | -8.08839 | -45.84589 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 50b6dbd5-6271-3234-91e1-fa46ce221628 | -8.78652 | -50.06437 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 68e9dc75-74f3-39a3-b4a0-241947431595 | -7.48918 | -35.0761 | 2026-08-28 16:05:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b7a469f9-9538-3b6c-9f32-b482799adeca | -7.34731 | -35.13939 | 2026-08-28 16:05:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 36472d17-4742-3786-b082-ff9ef8f403e6 | -15.63206 | -45.93131 | 2026-08-28 16:05:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ca82219-b877-32cf-b330-17c783f43bab | -8.08378 | -45.84941 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ba2d18f-582d-3b43-ba6e-63e0fc2efd39 | -14.18799 | -41.24689 | 2026-08-28 16:05:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| deef83a0-231c-3d06-b5c3-0fa14e408a28 | -16.48138 | -41.58932 | 2026-08-28 16:05:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d46b4412-8f49-3d5e-8527-6a7a76fe4593 | -12.77537 | -45.94761 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 53076387-1df9-34b9-9640-192b532e5282 | -13.60187 | -45.77907 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b9647adb-c7c6-3eba-9f4d-a9569402114c | -7.28126 | -49.95302 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ed1056e5-a9ca-39cd-904b-690c77874dcd | -7.15459 | -43.20546 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 28d8b290-55bb-35df-b0c1-882f9e91b9df | -15.41904 | -42.05866 | 2026-08-28 16:05:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 1982d4b4-d066-3fe8-a45d-d36b3a5731b8 | -5.96021 | -44.79183 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 78f21427-845f-37e8-bf11-4f94bfa07fba | -5.95876 | -44.79864 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e872cec6-2ac1-3c06-85a4-04ee301c432f | -7.98776 | -45.50659 | 2026-08-28 16:05:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 36e23df5-e510-30e2-ab39-ec9fb61cef24 | -13.77204 | -40.60502 | 2026-08-28 16:05:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a13d7352-ca76-38c4-b389-92b3787acfcf | -7.27552 | -49.85524 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 704d4de5-dc96-3b21-873f-4141aa12c8ba | -13.32885 | -46.90851 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 62ba955d-0ff8-3360-8e43-ede32e81890e | -5.96728 | -35.47979 | 2026-08-28 16:05:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5e6daec2-10cd-3e6a-8a04-79d4503785e9 | -9.50576 | -48.02236 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 595a4423-e8af-372a-ac96-ea8b24435889 | -14.88315 | -40.68792 | 2026-08-28 16:05:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a8f9c3d8-0fe3-30e4-8cee-c46bb72d5868 | -5.95174 | -44.7811 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1a17e7a0-dd06-3db0-b6f8-0bbc32ccd9a6 | -6.92957 | -42.68205 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 1eda5615-d66e-3bea-b129-03c5509aefc0 | -11.71618 | -37.66984 | 2026-08-28 16:05:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 894ed069-5672-34a5-bd3b-139c94419ded | -12.0906 | -47.16269 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 11851391-078c-3118-b2dd-36edd40d82ef | -9.49489 | -45.64546 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9e45f0cd-61c5-38d8-8345-fcf8d1f0a46d | -9.49723 | -48.18993 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8bc102e-66d4-3d9f-b18c-439e850d63bc | -16.0258 | -46.53964 | 2026-08-28 16:05:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bc0b0eb-4096-37db-9028-4164528594f2 | -15.72701 | -47.75416 | 2026-08-28 16:05:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cebc3d10-c314-39df-abf8-8d145f60c645 | -13.65303 | -47.74866 | 2026-08-28 16:05:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f1762cb7-eedb-3176-b544-4868cf6b0277 | -9.49993 | -45.64479 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 112742d0-2139-38d1-bb44-92befa55f303 | -6.93547 | -42.67408 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f40577e5-e590-318b-910e-a6cedbae5ef3 | -9.49529 | -45.64841 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b17a9d31-186e-369b-b42b-38eab945a6a4 | -7.12119 | -43.169 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e769edda-08d1-3d66-8179-f91e4d8fcc50 | -8.66905 | -49.53581 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bb32368c-b592-333c-975f-009e044548d1 | -5.32998 | -40.77993 | 2026-08-28 16:05:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9d7ba002-d4b6-3e70-b633-e6d93cc4ab79 | -17.9371 | -42.60783 | 2026-08-28 16:05:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| becd3d5f-9ffd-302a-a279-aabafa937e15 | -15.75451 | -42.59209 | 2026-08-28 16:05:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 05d0299c-36fd-3adc-b6f2-3896056f9435 | -12.38533 | -48.20447 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7b5df388-b1a2-3466-b5cc-4967654ff156 | -16.0993 | -45.13928 | 2026-08-28 16:05:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36405e81-fab2-32ba-8502-d6fd218fb079 | -7.08244 | -42.19511 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8bcb871d-3187-3415-885f-25d81ed86184 | -7.34582 | -44.09774 | 2026-08-28 16:05:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eaf40f76-5630-3079-94e3-a83c59065d5d | -12.49507 | -43.76879 | 2026-08-28 16:05:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 115c5408-4c65-31c0-9bcf-ac3e3c143aa5 | -5.95569 | -44.79234 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 7c4e8928-301c-3713-9259-57dbb249ea2d | -6.40368 | -44.97349 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6721e763-e73a-3968-b362-1d4fdb7c98cd | -15.7275 | -47.75904 | 2026-08-28 16:05:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b950e96e-5ed4-3e49-b50d-456869c3ac4a | -7.09697 | -42.82502 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a24467f3-fc2f-3d77-b9a0-cdb6664d6425 | -7.60599 | -45.83259 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5911f3b5-cd61-3b44-9afc-7934452ae499 | -8.04066 | -44.15854 | 2026-08-28 16:05:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7ab7bc4c-181a-3837-af9c-ab4069a50c3f | -9.49388 | -48.1873 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84f92398-51d1-3564-aeed-229d0d510c9b | -6.24816 | -39.19634 | 2026-08-28 16:05:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| c7655348-e39b-3a61-a8c9-fa0054d4e365 | -7.43858 | -43.07075 | 2026-08-28 16:05:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2d673b0d-863b-3f55-95dd-1fb07b18cf91 | -15.83783 | -48.00703 | 2026-08-28 16:05:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 937b3b2d-5c7d-3d50-9111-44b7445c27ca | -5.96087 | -44.79629 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 830debbd-092c-3f8b-94b1-a94644b8474f | -13.86251 | -43.64243 | 2026-08-28 16:05:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21695de7-b564-3fb7-a24b-558d4c8b3bd2 | -7.06998 | -43.5855 | 2026-08-28 16:05:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c37f562e-82e8-3000-aab7-efee077bdccb | -7.81007 | -43.88453 | 2026-08-28 16:05:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 96423714-daa5-3fca-9337-3b567f42b20f | -5.02012 | -37.63669 | 2026-08-28 16:05:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78c5c234-85b8-3f21-946c-8de3a81305df | -13.58539 | -45.77805 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 57edcf2f-2286-3ddc-b5dd-de8e062d6c71 | -8.07264 | -45.84233 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ff760f21-5f18-3166-b47d-4bec522126e1 | -8.08611 | -37.268 | 2026-08-28 16:05:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 03d60794-5705-344c-b9b7-2e56d8f2fc80 | -8.93968 | -45.76538 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79c410e4-23c8-331a-bd70-34889f3c8170 | -6.84297 | -45.07796 | 2026-08-28 16:05:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f928ea84-6d6f-3d1f-bf02-5b2bb63a0d60 | -17.86323 | -39.80481 | 2026-08-28 16:05:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 150bf670-c007-3470-bad6-3f0b4b80d540 | -13.01297 | -45.04225 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c28b386-a27d-3ab0-999e-62fdccfdfdbe | -5.94986 | -44.78386 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 836fe6e5-9e73-3b5f-aa01-06889e63fc72 | -6.56419 | -45.32903 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| a4209085-fee6-38f8-9623-a5ab3a75009d | -13.58279 | -45.78133 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| caec5c4e-9272-38bf-99ff-77790a79c5e7 | -16.38479 | -42.97743 | 2026-08-28 16:05:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1b4f902a-ba5c-34f8-9202-ed19935ecfbb | -9.48284 | -45.63196 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83d56593-fd6a-31d9-a8e7-7d9ed1336b1c | -8.16514 | -46.18346 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f7ee2a7-080f-3ccd-9c3a-50bfd8aa7686 | -16.26581 | -40.8536 | 2026-08-28 16:05:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8c49c705-e1c7-3e3a-be61-a04028d680c5 | -12.39718 | -48.19822 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 451fbcd6-4420-3872-9bc4-7d22f8a924dd | -13.33169 | -46.93344 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6101e575-d286-349b-bc23-736291d5945c | -8.02754 | -48.02117 | 2026-08-28 16:05:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 990f9805-77ff-3f72-9893-cf7dfa151b3b | -15.21044 | -40.10367 | 2026-08-28 16:05:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b94f3e60-0836-337d-bf45-5787cfb2631e | -7.16992 | -43.16554 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f8b03f37-10af-3822-8819-ebf5a5817b67 | -12.28619 | -41.98557 | 2026-08-28 16:05:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3f2ac2bc-9597-38c7-859c-e0e07c9f397d | -12.02444 | -42.04124 | 2026-08-28 16:05:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 94e930d8-3c2f-3dc0-9256-385c6b1efb0a | -7.629 | -44.8078 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 33cf1779-1dda-3554-86ed-035114d90a41 | -15.99629 | -41.32758 | 2026-08-28 16:05:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bfd08d08-4cca-3647-acdc-a279214d054e | -14.22794 | -45.25348 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f393935-d536-386f-9ca1-6ea7dc7eb005 | -8.67679 | -49.54558 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 4f417214-bf41-3fd8-abde-a79975537742 | -13.89154 | -42.34246 | 2026-08-28 16:05:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5c4b0c79-13f1-3307-9364-469161717634 | -7.2109 | -42.75086 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a95ec5f6-849a-3d4d-9038-868a45c351a5 | -15.723 | -48.25272 | 2026-08-28 16:05:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d79adde-3752-3e63-b7c9-290f8d1370f1 | -5.96375 | -35.48033 | 2026-08-28 16:05:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c3b196a-c5a9-3fc1-880d-e10a93aeeb96 | -12.8656 | -44.35648 | 2026-08-28 16:05:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 360d7eba-e193-323d-81b9-9819675a7731 | -14.90559 | -40.94469 | 2026-08-28 16:05:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| a7e8b0c5-14bc-3f8a-b3e7-049efd679f47 | -7.62567 | -44.81777 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dcfc4781-3e35-3098-ab99-634eff315bf6 | -5.95052 | -44.78839 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 3c372ffd-0fb4-3a22-86c5-e71407436a54 | -9.4871 | -45.62551 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ccc1443-5493-3ce2-a3cd-96423b5394e7 | -9.49647 | -45.65723 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b24783c7-850d-39ee-ad0a-f701f231ef5d | -7.61174 | -45.83751 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README94.md)
