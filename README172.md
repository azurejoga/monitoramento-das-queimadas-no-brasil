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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 647d3e2f-da06-3f75-ada1-71d2ecad8c93 | -10.82975 | -64.20163 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c3ad791-2cd8-3c7b-8a7a-4f146115641f | -11.00289 | -63.9144 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb2345a1-60d5-39c7-9824-1625265dea50 | -10.99977 | -63.57161 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ed3d17cf-b715-3a1d-a2f9-5194b69e3f2c | -10.99915 | -63.91361 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b3fa679-578d-3c89-a794-619c7fc70fa0 | -10.9991 | -63.57552 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a4f79c5-3693-3b2e-a7b8-dea3514c259b | -10.99843 | -63.57946 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 213e76b1-4d45-3515-9f8c-8f60224cd506 | -10.99611 | -63.57082 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea3e6437-d4d5-30f0-b0ad-7c416c04b08d | -10.99544 | -63.57473 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d767c48-68fd-3098-af18-2fff7ead0fe2 | -10.9924 | -63.57029 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4664e75c-1d0f-302f-832e-60cbf6f68adf | -10.99173 | -63.57419 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e78d8734-1011-3484-958e-d143f85f17a1 | -10.98802 | -63.57369 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e30b413f-32cd-3ab4-938a-08cfcae83c8a | -10.986 | -63.57082 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e5dc973-f63d-33f3-848c-85715c7a5647 | -10.9823 | -63.57021 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 174ca129-66e1-3d56-afa2-35ee32ec8674 | -10.91069 | -63.8847 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f60ef6b1-3af7-3aec-8596-bd29a94fdae5 | -10.90857 | -63.87422 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1e4f9b1-e0d5-3362-a962-0da4883093a1 | -10.90695 | -63.88389 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a60c298-8905-37b8-ba40-0707edba1475 | -10.90613 | -63.8888 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c53c90b-ad0c-3da9-a6a2-6e52273b667b | -10.90564 | -63.86864 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a6a30be-ee54-3712-9094-53afa26b2d6e | -10.89868 | -63.88705 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1661a08-637f-34f2-93a0-001bf76ee0fb | -10.89789 | -63.89171 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 584cd81e-4770-35b7-86cc-93b71853b826 | -10.89711 | -63.89634 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 53d66b9e-e06d-3f7b-a1f7-2c71ac19d3a6 | -10.89637 | -63.90074 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ffdbefc2-2969-360e-8d00-202c933b00aa | -10.89561 | -63.90524 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| dd4c3673-b324-32c0-b96e-2c996bb95c86 | -10.89495 | -63.88616 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b211653e-8609-3bbb-91f3-b6b17cfe96c0 | -10.89416 | -63.8909 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7309642-bfd9-3354-9c4a-1c469c9ce875 | -10.89337 | -63.89557 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8be530d-381a-34aa-a5d3-07b658cbfc46 | -10.89262 | -63.90003 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 043f83a0-5000-3c4d-b8ac-69933d513ea6 | -10.89185 | -63.90453 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5a3be8d6-bc58-3b6d-adc2-a8e51b965ae0 | -10.89121 | -63.88541 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 883c5eb4-e46b-325f-8dbe-2b0393d4756a | -10.88885 | -63.89937 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2966128-9f55-3539-88d8-392bc8be4270 | -10.8881 | -63.90382 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a36da52a-0450-34fc-b46d-885a06f6ff4c | -10.88506 | -63.89889 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 113fe53b-31d0-3b45-a5cb-f433ee413927 | -10.88125 | -63.89852 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0adaf3b1-3fa5-3888-843b-bfeef8cf555b | -10.87824 | -63.89341 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01e7e16b-45e0-3e14-8173-af6af3fecb4a | -10.87446 | -63.89285 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e2f2c6e-c443-38ab-b3f1-f37b0708250a | -10.87146 | -63.88776 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a90437fa-c02c-3cba-83bd-596bbe4354c8 | -10.87068 | -63.89232 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a3fb9c9d-3859-3b65-bb65-7fe738180650 | -10.8685 | -63.88238 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56cf23b2-8a07-3084-8f57-f26591163280 | -10.86768 | -63.88719 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5627aca-2af3-3468-8d17-f72b698ede13 | -10.85874 | -63.87149 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b46816d0-e45e-34a6-8fa3-30a971e522d0 | -10.85496 | -63.871 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3c853b7-b8f6-3a19-bc00-9e30540a56ae | -10.85417 | -63.87562 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c59c7a5-4438-30e9-ae3f-f593a38c5e5a | -10.99759 | -63.92285 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24f1c97f-00b6-3045-a1e2-06dcae97c3ba | -10.99303 | -63.92691 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef2b0197-0d48-37d8-87cb-6b54f2aaa801 | -10.99146 | -63.93621 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07ebd34f-bc1a-34ea-a7da-22ae9a661ea2 | -10.98766 | -63.93574 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 747b2be5-1aa0-32da-9b87-7b61789ee300 | -10.98666 | -63.96457 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cf17877-1762-3db8-9d16-929010a166c2 | -10.98613 | -63.94472 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e73278d-3ba0-3bcf-b66d-f6fdf65a289d | -10.98534 | -63.94941 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9831c33-bd3b-36d5-a009-e80fce05f0b6 | -10.98454 | -63.95414 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 834bbe61-cf6b-30b4-ae01-4aaca2ec66b2 | -10.98215 | -63.96826 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20527df3-b2cb-3cae-ae7e-82c06920f2f7 | -10.98153 | -63.94901 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11935cab-bd7a-31ff-845d-9acad023969b | -10.98076 | -63.95354 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d5bf06e-df25-3163-a309-d1151eb478f5 | -10.97999 | -63.95805 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81574594-9a63-3be2-b046-b3b2b1d93583 | -10.97923 | -63.96256 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd52314a-14a9-36ee-86c8-34aa163ed4d4 | -11.70017 | -64.26774 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2b43636-e3ff-308b-8053-e37f6426eebb | -11.69555 | -64.27183 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d8a421b-843f-346a-8955-6c7b9c8d33f6 | -11.69175 | -64.27115 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea8d1354-a015-3d29-8a48-c0336130b3e7 | -11.67602 | -64.24871 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 439c0636-180e-3696-bba7-6578a13e1287 | -11.6752 | -64.25346 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87993f6e-a23f-3724-8efa-7d56fe20e37f | -11.66763 | -64.18404 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 701e508f-af28-36e9-be6f-ccba6ca2ba9b | -11.66465 | -64.17872 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c94d51dd-1905-3802-8ddc-988d9ccee69e | -11.66385 | -64.1834 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f54bf27e-282e-3905-a5ec-fa8d1c5106fd | -11.65486 | -64.23527 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 471ac25f-ae32-3ed9-bcd2-a7cc309e9491 | -11.64974 | -64.21971 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a0dc48a-c03d-3cae-9675-cbaedbed5b99 | -11.64594 | -64.21906 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 118f1372-1326-3607-9511-590a3b77576e | -11.65207 | -64.0249 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3bda141-f39c-3a1f-961d-6f56ed759d58 | -11.64904 | -64.01998 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7aff6bf-9420-3439-b75e-4eb2bb5a58f4 | -11.64073 | -64.02347 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81bf3e78-b345-3139-bc32-dc9d592a6d7c | -11.63997 | -64.02799 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 110e9ad3-06c8-36a8-b475-d05cd2219cc4 | -11.63918 | -64.03266 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99eda710-3bdb-3e85-b26d-7ae438d8a919 | -11.63541 | -64.03207 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b69d9af8-1ef2-3870-ac58-136b42683d91 | -11.63462 | -64.03674 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40c23aa0-74d6-36a6-8a79-fc692bc41cc3 | -11.63087 | -64.03609 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4a0effa3-a5bb-3262-8870-1b010415ee6e | -11.62711 | -64.03545 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8eeb17c5-3c29-3aa2-ab50-ed085fe13997 | -11.62414 | -64.03016 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d4617bb-3922-3dec-bb8b-2e1b3f81e147 | -11.62335 | -64.03481 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4572ef5-6d27-316e-99ad-686814e0d19a | -11.62229 | -63.973 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cdd6aed-da9d-3f9f-8f35-ecc4b44897e7 | -11.62168 | -63.95398 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebeca246-35cd-3c3e-a27e-7735cc2b46f3 | -11.6215 | -63.97761 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74f454bd-11a5-3b9e-b7d3-71a26ef20812 | -11.6209 | -63.95856 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fcf523c-6663-315b-8c28-c61fa10c90ef | -11.62038 | -64.02953 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d340798-9d1b-323f-b072-dec569c01a33 | -11.62012 | -63.96314 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d3f2cf4-2760-3e06-88e1-7c8f9d747057 | -11.61961 | -63.8315 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29f525ac-751e-3fd6-86ce-f29f875aaa9c | -11.61855 | -63.97234 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5310b406-ffc4-34be-b51e-5416f529fbad | -11.61776 | -63.97695 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94ceccb2-f574-339d-8954-42e14bddda22 | -11.61728 | -63.84506 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27ebf0a1-de52-3d21-84d7-5a3c38bfab24 | -11.61716 | -63.95792 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 860cf000-a936-37cd-9acc-6d5775184b7d | -11.6169 | -63.67641 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7bb7db4e-9127-33d9-b985-92b3fc6e07cf | -11.61648 | -63.84974 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fec8ee4-0f57-35b4-aa64-9e053829e914 | -11.61617 | -63.68081 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 68b058ee-761c-3974-bbad-81421ad81077 | -11.61613 | -63.67476 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1c7adf06-72ab-32f5-8023-5f9e217a8223 | -11.61539 | -63.67907 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 38e5bc7a-60df-3d88-b854-5ae89ac87276 | -11.61469 | -64.08575 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b002ff28-5b04-3e26-96e5-6bfcd0a3bc31 | -11.61409 | -64.06649 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 676c3d2f-2f8f-3d8b-b6bd-be3f509ce217 | -11.6133 | -64.07111 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10bc3115-82d7-3c00-876a-2151688e7589 | -11.61263 | -63.96189 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5bbae6b-f7ef-37e8-96fa-acb5036c9cad | -11.61255 | -63.7253 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 85eb747e-3650-3811-98a0-13d9ca7c4438 | -11.61251 | -63.68004 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 788ffcc7-ba0e-398a-8e94-e8ae6505991b | -11.61184 | -63.96647 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README173.md)
