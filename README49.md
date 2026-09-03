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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53c0003e-7737-37e6-9859-5e6782701a24 | -9.71714 | -65.00447 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88b01a1a-0f6a-359f-a6f8-476ff4d1231f | -8.87285 | -66.67603 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f775ed5-2569-3539-81e4-32f3ba9aaec4 | -9.01161 | -65.41629 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a641c5b1-c82f-3167-a214-9712a2426d19 | -8.70459 | -70.97527 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc880a80-1e5b-3663-8a93-463b1c052469 | -7.35928 | -60.60412 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a1fc0b3-fa4d-37e3-ae78-11da91579eb1 | -8.46599 | -54.68443 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59ec515f-5fd2-38d1-9a05-1b375e8aff18 | -9.14157 | -61.60269 | 2026-09-03 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4f6241-436f-32f2-b001-4e7f779ab4a9 | -9.71994 | -65.00858 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afa8b243-42cd-385f-85eb-eaba535dbaf2 | -7.51717 | -60.72348 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a0f252-f2e9-34c1-9184-2c0e04e8f96f | -7.85024 | -71.77171 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a3fbdeb-07c8-3ec4-875a-72b30557bd52 | -8.43982 | -54.69494 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da30ad73-edda-3c81-9693-0ee38983da53 | -8.45506 | -54.67285 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be8ea586-a828-3c10-8d1d-fc99ee69feec | -7.20595 | -60.68859 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 914d0845-2f03-3e7c-9f98-b0c4052838c2 | -8.46236 | -54.66437 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9232ef12-f957-30f4-84fc-4b57d65a46f1 | -9.02055 | -65.44637 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3cb04a1-6374-3aab-86b4-6490a3701c2c | -7.27174 | -61.1153 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 78c60cfd-fa1e-3f47-8dc5-34d74a31e4f8 | -6.94565 | -58.98747 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2147c493-cb8b-3362-b82b-eb88854f97c1 | -12.01192 | -60.52666 | 2026-09-03 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01271707-44f4-3e2d-9d92-f650ead4277a | -9.03941 | -65.74239 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05ca2876-2c24-35bc-bc50-d10ff05badfa | -9.01946 | -65.45337 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c90345-38b9-3e61-ad83-263e79b20aa9 | -8.43456 | -54.73613 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39fe3171-4b16-3b1a-b81f-9695ea0b2e32 | -9.02171 | -65.72535 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02d28942-1f22-3c94-819c-f88318f0f111 | -6.91422 | -63.09687 | 2026-09-03 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab6a1627-eef1-3bd1-a1e3-0496a543d88d | -8.61313 | -62.55943 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 711019f6-f6e8-3fb6-9275-85b9fd5d4793 | -7.69229 | -67.12311 | 2026-09-03 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6b2a178-b5f7-3098-b4b6-f1a832b1ed47 | -8.3907 | -71.04845 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de05c76d-cdc2-347b-bed8-05ffd6137aa8 | -7.53022 | -60.71825 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22a738dd-6bec-32ff-9a3b-414b2be7741a | -9.02833 | -65.72639 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10cd92ff-5b42-3036-9c7a-d481805a3129 | -8.98884 | -65.38762 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fe65f6c-a8c7-3b78-bcbf-62945b4f15a5 | -7.29425 | -60.62677 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae90f465-ddda-32cb-8bb0-30948d91eda0 | -8.95631 | -69.42155 | 2026-09-03 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44af0859-1c6f-3422-9d6e-95b8fddfa51f | -9.0702 | -65.7187 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c0919bc-1939-36ad-9d92-abf882269dd3 | -8.46846 | -54.66525 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2657bf24-f7a6-3787-a825-207e38b2f070 | -8.43432 | -54.68938 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ceff6b8b-bdd2-32f4-a439-0429e92c9448 | -8.38603 | -71.05141 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0de81233-02fe-3e28-bd0d-acf0b6118158 | -17.0869 | -56.86326 | 2026-09-03 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 834d8a59-0b86-3ccd-9eec-0cd86ec3ca68 | -14.45537 | -60.10777 | 2026-09-03 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f64513b-2954-3a1e-a020-44bdf35dadb1 | -17.08868 | -56.84545 | 2026-09-03 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 59ca2487-2042-36d2-9155-8366644db2c3 | -17.0832 | -56.84026 | 2026-09-03 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8a7d355b-1938-3f27-815b-ca5d8cd35077 | -17.08734 | -56.85882 | 2026-09-03 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e1f16563-45dc-3a92-b8fd-b575d9b2ef6b | -17.08231 | -56.84917 | 2026-09-03 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 265edab4-cc46-34d0-bc1c-f3934e05d480 | -17.08276 | -56.84472 | 2026-09-03 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 97f1d340-31b5-38b5-b02b-a52f6c4e4bee | -6.6357 | -59.4459 | 2026-09-03 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 82dc00bb-ec59-3b03-aed5-7cc43e07468f | -6.6541 | -59.4452 | 2026-09-03 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 839f2efd-b838-3d08-905b-8b38ef7b7034 | -6.6882 | -59.9628 | 2026-09-03 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| df5cafc9-1ddb-366e-9474-1303b7c94be3 | -11.0006 | -45.0847 | 2026-09-03 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 1cd1ebf3-605b-3823-8944-a60c14df4714 | -6.3237 | -56.0434 | 2026-09-03 05:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 27d961b1-02df-30f6-be4a-ac674c0f936a | -6.6883 | -59.9436 | 2026-09-03 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a61c415c-4fee-3dcd-b455-a2ac8b25d9da | -8.5916 | -67.1788 | 2026-09-03 06:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| a5a177ec-934e-377d-be0f-2495ce996ab3 | -6.6357 | -59.4459 | 2026-09-03 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| f91751ea-8ad1-34e4-b2f4-878796388d8f | -8.0737 | -50.9656 | 2026-09-03 06:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| bdad5067-42a7-3086-9a59-d09dd8995fc5 | -8.0924 | -50.9642 | 2026-09-03 06:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 6c7605bb-862c-3b92-a450-08b7377c9452 | -8.0922 | -50.9852 | 2026-09-03 06:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d33fa456-3c99-3510-b7d7-7bf7b2f2fb0a | -6.6882 | -59.9628 | 2026-09-03 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 2f5acc9f-a5d8-36e5-8747-b7676b682045 | -6.3052 | -56.0442 | 2026-09-03 06:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 69919fb7-54ca-33df-a066-1727463a2202 | -6.6883 | -59.9436 | 2026-09-03 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4e623dd7-6cf2-325b-9188-53660ed32819 | -8.0924 | -50.9642 | 2026-09-03 06:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 058446ee-343f-3355-9c63-16678c927bf4 | -6.3052 | -56.0442 | 2026-09-03 06:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0bee8418-cc0f-3603-b895-d6a94627067a | -6.6883 | -59.9436 | 2026-09-03 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 181d42b7-068f-3c85-96a1-a85f086b8d84 | -8.0737 | -50.9656 | 2026-09-03 06:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| a62f4975-6a8c-3279-8280-a7e9f687ad0a | -6.6882 | -59.9628 | 2026-09-03 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 5ab220d9-0a52-33a7-94a2-297e55084828 | -8.5916 | -67.1788 | 2026-09-03 06:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 2cef2754-0ac9-316b-b1ce-f608e5bde540 | -6.6698 | -59.9443 | 2026-09-03 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 784b327b-c850-31e0-a2cc-22f351acf54b | -11.0006 | -45.0847 | 2026-09-03 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b4898573-9b3b-30ef-a10e-6d81628190ff | -3.61905 | -60.56972 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3218e6e1-1b37-3e11-8ff5-fad1520e097d | -4.2384 | -62.24438 | 2026-09-03 06:18:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f46b778-55b5-3cdf-8925-63f23714e58b | -3.61841 | -60.57392 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5b40141-9833-3939-b37e-e6a77d86f1c3 | -5.26313 | -60.18013 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc7e63e9-36a0-3c06-bc25-ee77763b5643 | -5.51164 | -60.18586 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 42403a63-8d31-37ac-a876-cb11188e8729 | -3.20112 | -61.21499 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82bb658c-51d3-3d9f-b8e6-cbcb7f1995f6 | -3.12439 | -61.22995 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efccd75d-9425-3dea-96e0-80f9a7fad89e | -5.21673 | -60.03014 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 453eecfe-2993-3d63-94c5-6eca1df81530 | -5.25631 | -60.18395 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2232971e-a04d-30b0-85e4-12d4a70bd779 | -5.25204 | -60.18187 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acba09ec-0fe3-3ef7-91c0-86977ec52741 | -3.20764 | -61.22994 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d69733e-61d5-311e-9c52-e85f7533911e | -5.20293 | -60.0379 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27d60cc3-cd8a-34c4-88fc-1ca434e58ed0 | -5.46609 | -60.05604 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c29f91b3-6ea0-37b6-8268-def6c7ff5a0e | -5.26439 | -60.18365 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1048ed3f-9e01-396c-a0b4-06ad49b89dcf | -4.23935 | -62.23784 | 2026-09-03 06:18:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f805b79f-27c3-32e9-97a8-e49c13e6ceac | -5.55402 | -60.23601 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb796492-c4af-309f-a374-d05a343918f9 | -5.46543 | -60.06092 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e9b2aa1-fdf9-37fb-8f1b-35b93f6d7e26 | -3.20227 | -61.20752 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0f2ff4-b798-3090-be17-7a4ccd6cd4eb | -3.61969 | -60.56553 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c077f773-d96f-3135-862f-364b0770dd11 | -5.21051 | -60.02921 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf1e829e-c703-3797-8eb7-d9e497805776 | -5.26248 | -60.18489 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26b34cb3-c0ec-3652-98e4-a6274cc0879b | -5.56248 | -60.17374 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7531374e-85c0-3810-b5e8-c633522e7090 | -5.32616 | -60.13578 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a4b5735-49b8-3d47-94ad-7a5c5ab9941b | -3.61748 | -60.56977 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4f917031-310a-33c9-85c6-04493a4d9250 | -5.51098 | -60.19059 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 689ac6d9-7f25-36c5-bc98-65404690cb78 | -5.20847 | -60.04374 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59baa281-10cb-39ff-bd7d-8df5fc0b6da6 | -3.6138 | -60.56464 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 739ff182-cbd5-32ba-b842-d85f1d69656b | -1.39512 | -61.74699 | 2026-09-03 06:18:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63c71f1a-e1a1-3578-8904-07118983ea78 | -3.20477 | -61.21045 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f39ca56-1bb5-37e1-b5ca-c6963faa35bb | -4.23888 | -62.24111 | 2026-09-03 06:18:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 795dc110-5d7d-36d7-8924-37609347bc6d | -3.2017 | -61.21126 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f8188fa-fc7d-371d-affd-3085f9540541 | -5.32548 | -60.14055 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea75fe20-80ef-3531-91d8-f1220b3a0e18 | -5.20226 | -60.04274 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c69b84-55e7-3540-8883-e0c17caabed6 | -3.39416 | -59.3602 | 2026-09-03 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de4cbf7-d969-386b-ae1e-f5b4981d8756 | -3.38456 | -59.42583 | 2026-09-03 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f2d4fce-3fe0-385b-ae13-d0b6ed54cb7b | -3.7031 | -64.55221 | 2026-09-03 06:18:00 | NPP-375D | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README50.md)
