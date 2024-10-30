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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c35a2988-2800-3e1d-a262-94111ab9b44a | -6.63591 | -42.8295 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8a7e081-f34e-36eb-b4de-90308b4eeebf | -6.63365 | -42.82151 | 2024-10-30 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 27e254bc-235e-339f-9423-0e002c0cc427 | -6.60073 | -42.30064 | 2024-10-30 04:19:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 549d4c36-fef0-386e-9f58-9d966633ec63 | -6.50305 | -42.82826 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6abbed56-7ba9-3bce-a15b-a6e8e1509839 | -6.70498 | -43.52826 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35028964-20f5-396f-8b6e-ae37bc86b01f | -6.69666 | -43.05275 | 2024-10-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 743e914e-6cfc-3d77-9719-469b006e9b1e | -6.47595 | -43.14157 | 2024-10-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8cb5148-b5b0-3b12-a169-f6d632d59fa8 | -6.47539 | -43.14517 | 2024-10-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c342b3e-eca9-3737-bd39-3b29f60e73b9 | -6.47202 | -43.14467 | 2024-10-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54b2b073-2ab2-32f8-b460-c0ceccd6f824 | -6.46639 | -43.1364 | 2024-10-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e4f889d-6c2f-3347-bc33-89731e355e2a | -3.1635 | -43.96825 | 2024-10-30 04:19:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddb674e1-b2de-3ea9-99e9-645a286d9ef0 | -3.53489 | -43.61869 | 2024-10-30 04:19:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 8f3c0032-12d6-3ed6-b137-8aed9b4bd4c5 | -3.53159 | -43.61818 | 2024-10-30 04:19:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38e445ff-c047-3b6a-afbb-c041a4fbc7f9 | -3.29128 | -43.5416 | 2024-10-30 04:19:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad2e096e-d1b3-33d2-9479-a89d58021bb1 | -3.45089 | -44.1542 | 2024-10-30 04:19:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9733926c-9bf2-3d90-a7d1-c96f9dda5b9c | -3.42354 | -44.45643 | 2024-10-30 04:19:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bbb32a4-5974-31e3-a186-ad3783cd3e94 | -3.32323 | -44.38015 | 2024-10-30 04:19:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4beb13a-efcc-395b-8584-fb1410170e0b | -3.23969 | -44.41296 | 2024-10-30 04:19:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db2b4bc-7d6f-3be3-92e2-7bd89e769123 | -2.53836 | -44.17527 | 2024-10-30 04:19:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 760fa8f7-ee5d-39f1-8a26-174398b152ca | -2.48669 | -44.2025 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3ba5882-d79b-3169-ae02-81abbe0457f3 | -5.08496 | -43.36388 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20d95aec-64f4-3a7a-9d84-684613819be0 | -5.08163 | -43.36337 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| beb73c04-85f3-3dfa-a33e-3c6082708c11 | -5.07831 | -43.36285 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b4ad527-2319-3940-b447-af70c2cafb55 | -4.66041 | -43.81669 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1ac21c2-4442-378d-b80d-b6da37206434 | -4.6571 | -43.81618 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4280b6a-2b3c-38eb-b2a8-eb81cb758864 | -4.36014 | -43.53963 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26d1286b-fea6-3dc2-9723-545ffc038245 | -4.35959 | -43.54309 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b29592cc-3074-3e14-84d9-578052f138f7 | -4.35871 | -43.61381 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e2c5b4f-4f1a-37a4-a3b6-c92ed7d3c2c7 | -4.35647 | -43.77951 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a992d43d-c342-30a0-8e11-c7a3fff05a68 | -4.35316 | -43.779 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72cae4ea-90bd-343d-909f-eb2fd6376129 | -4.35262 | -43.78244 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f48dd4ba-d7ec-3611-b1b5-ea8ca40750ee | -4.35208 | -43.78588 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba8cefc6-1d2e-32bb-a529-f83a3eaa13bd | -4.35154 | -43.78933 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da45289a-d621-3ce7-9b51-9c60339adca4 | -4.34986 | -43.77848 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cebbb6bf-e00b-39f7-a772-e90297692fac | -4.34932 | -43.78193 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea7eb031-4fe9-393a-92de-eeea8bb21a92 | -4.34878 | -43.78537 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efe18b57-d39d-3d63-8b4b-57b3c48c5711 | -4.34817 | -43.76764 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8d728c7-fed0-3931-b8fe-b292d709db2c | -4.34655 | -43.77797 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe6af285-74e9-32ed-93c9-687e5da2ce16 | -4.34601 | -43.78141 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 886809c3-8daa-34d8-bcbd-7212720cffb6 | -4.34487 | -43.76712 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b869f1a-3bc1-3e3f-a8a7-3217eeb8f8b9 | -4.34271 | -43.7809 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c3ad284-19ef-3e1d-8d5b-40b1ee1d2427 | -4.34163 | -43.78779 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a809d57e-9c49-3996-9ab8-5a1dff544bf8 | -4.33941 | -43.78039 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be7f4d21-260b-3ac1-9f1f-3677824db19e | -4.33833 | -43.78728 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c96adff8-a8cd-339b-b05f-1f9e00c134a7 | -4.33556 | -43.78332 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f91f4e8b-693e-3604-875e-cf27bdf89582 | -4.32901 | -43.63043 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a29a4b1-b1ad-3f82-878f-9aa0d08dd8f2 | -4.32847 | -43.63383 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1c3a123-5e87-39d0-bf78-d3ab438204e1 | -4.3257 | -43.62992 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04dceb97-aafa-3152-90dd-cd0a0499e38f | -4.32516 | -43.63332 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60b798fd-e5a0-3d7b-ae1a-37eeade09f97 | -4.27355 | -43.44093 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c47598d-84df-3ab7-a987-d73183327a41 | -4.27301 | -43.4444 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed1a6a62-c092-311a-b71a-8779bbdac5ba | -4.27247 | -43.44786 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48cb1a84-a219-3694-b82c-84442f1cf4d6 | -4.27193 | -43.45132 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90157aef-7043-3191-9786-f89386a58711 | -4.27024 | -43.44042 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e527db35-4ed1-38be-9678-283ff4efe2f5 | -4.26969 | -43.44389 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6096937-c296-3186-9a2c-4f1a774b4bd5 | -4.26915 | -43.44735 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6097e6ae-c555-3699-9300-c619ce72e44c | -4.26861 | -43.45081 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6ccdd5a-f588-3f7e-9051-c41b3e93e6b5 | -4.26807 | -43.45427 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 116b6ad4-49a1-381f-a966-323a38f03526 | -4.26638 | -43.44337 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb114e5c-f3b7-3c52-a4c2-801f144972d6 | -4.26584 | -43.44684 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0a2ea5fa-836c-3a13-8a6d-2a873fb0bd3d | -4.2653 | -43.45029 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 50f0ade1-4857-3f94-a41d-8919aadfdc1b | -4.26307 | -43.44286 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b37fd872-f7e0-3587-9ab7-4e918cd2da3f | -4.26029 | -43.43888 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74bc05c3-e862-3e25-bff6-a16901e2523d | -4.25975 | -43.44234 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dc5ba34-3b6c-307b-a513-11a0b39f3bb7 | -4.13987 | -43.83675 | 2024-10-30 04:19:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49338242-a0ce-3788-bbcd-125729021e53 | -4.13886 | -43.0838 | 2024-10-30 04:19:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed76206a-fcec-33ca-8e76-20b8dd930fef | -4.13657 | -43.83624 | 2024-10-30 04:19:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9c9e828-505f-3878-9a09-cd3f707bc9e3 | -4.04893 | -43.24538 | 2024-10-30 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d04dd11d-34a7-33c5-a7c1-8352e40e9e19 | -4.0456 | -43.24487 | 2024-10-30 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5061926a-ff03-3724-97de-9c8ce0164d23 | -4.04506 | -43.24835 | 2024-10-30 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87a01a51-e19b-3ea8-a9a9-303fd8b5f494 | -4.60468 | -44.30124 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7aa270c6-dc0c-3c8a-b1ff-4233ab119e67 | -4.60414 | -44.30468 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e14168ee-5370-37db-8374-72be70cdca80 | -4.6036 | -44.30811 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0580510-f5b5-353f-97d0-db29e94268b0 | -4.60192 | -44.29729 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81c2aac0-6cb0-38b3-87be-a4ccbbe044f3 | -4.60138 | -44.30073 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec444dd7-6333-37bb-bb4a-a6a3420bfabd | -4.60084 | -44.30416 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c004d2bd-1a1a-3e33-aaac-ad09a4ac8a47 | -4.6003 | -44.3076 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26b1d1cc-7d0e-3c6a-9451-4a0e88cf3b2b | -4.59808 | -44.30021 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a8eed4f-c17b-3f70-87d8-aa04d26e8d53 | -4.5976 | -44.32478 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a460dbc1-592a-3a20-a3f6-b8bba3454655 | -4.59754 | -44.30365 | 2024-10-30 04:19:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f72fbf2-1d6f-3501-bd74-adc1c865e6a7 | -4.14441 | -44.20052 | 2024-10-30 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b299481f-6c47-3a6a-b337-cdf03e46e499 | -4.14111 | -44.20001 | 2024-10-30 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d633b60a-fa07-36a5-8660-179e13c2facf | -4.11207 | -44.23419 | 2024-10-30 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98aecfcd-8b2c-3aaf-a534-1d9df961fe6e | -3.60959 | -44.46087 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9f21f3f-05aa-3239-a9c9-bc237ed943ad | -5.0705 | -43.67558 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af65d753-8bbf-3edd-bba8-3320cb730b69 | -5.06772 | -43.6716 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a27b00f0-68a8-312f-a0fa-12c57afc369e | -4.87124 | -43.86081 | 2024-10-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4785aae-ff63-3565-857f-dbcae89b0c0e | -4.77594 | -43.64365 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54798dd7-a1af-3eef-8ba0-e253ccad9872 | -5.00664 | -44.36481 | 2024-10-30 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e90b4751-da4a-3ad4-9fc0-62d8f0ac00a3 | -5.00334 | -44.3643 | 2024-10-30 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2645aca1-ab08-30b8-9000-519885fc5854 | -5.0028 | -44.36773 | 2024-10-30 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8280f0b9-f7f6-397d-9170-58d0e0ba0d49 | -5.00226 | -44.37117 | 2024-10-30 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36d4379e-fb9a-3ebc-9b6f-4584b17ecfe5 | -5.00004 | -44.36378 | 2024-10-30 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51e501f6-a014-3503-8f71-defd4e7dcff1 | -4.9995 | -44.36722 | 2024-10-30 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08462641-ae6b-39d8-a052-f4abe916161b | -4.99896 | -44.37066 | 2024-10-30 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c02f6e98-8e4f-35fc-9cd2-52f6a27dc77b | -3.92029 | -43.96089 | 2024-10-30 04:19:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcabfb4d-a7cf-391b-a9c6-8853ddc164de | -3.89649 | -43.13211 | 2024-10-30 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caca7836-9293-3cfd-beee-50a2f9201e20 | -3.82936 | -44.14719 | 2024-10-30 04:19:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f09d34e-3353-3a3b-950f-579ccc7a715b | -5.29143 | -43.41415 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b89264c-6720-3e42-a8ab-1baa1d1ccf62 | -5.28755 | -43.41713 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README36.md)
