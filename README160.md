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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f46dc6e9-a9f4-3416-ae7d-34f6e133cbc6 | -3.85791 | -52.03329 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfec9a58-d52f-390c-92eb-19026cf98d8f | -3.31471 | -57.48661 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 806b0827-520e-380c-b5bd-ec756e170240 | -3.51239 | -54.66329 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef9e08f-555b-3b30-9996-8fdf33c49a57 | -3.03183 | -54.23656 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92ef27d8-26ae-3916-8453-719bdcf1807d | -6.92799 | -43.65631 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3f34aaa3-8133-367a-8b3b-e49dae0f657c | -3.03924 | -53.93605 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94b47c92-e488-37c9-80ec-2650b57e1b73 | -3.08868 | -53.94366 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c6fc2c9-4409-3a00-86e5-b4b08f323576 | -3.10181 | -54.27378 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 901bdee1-2776-3eca-984a-84562670ab54 | -2.94386 | -54.15229 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6edb537-1570-3d18-b025-315a6c71ee3f | -2.93816 | -58.00078 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6981265-990d-3665-8a04-b5a93c573411 | -3.17395 | -54.08769 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 933be201-beb4-3c6f-a339-6f037c393da5 | -6.92545 | -43.65844 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 61c248c5-a45c-3964-8a0b-bd4bf75a48ab | -3.0228 | -53.92542 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 467caa39-1b6e-3e63-a8ca-2bf111df2b63 | -5.25789 | -60.17485 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 400a9eec-2380-3a41-84d1-8e92d6b1e164 | -2.99055 | -56.59453 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b6454ed-00f6-3b50-bcbe-a19f233aca4e | -3.0008 | -54.76365 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5da944e7-5de0-3d0e-93c2-d0036ffaf069 | -2.95345 | -54.20485 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfdca55e-8100-3c70-a631-5829cfe8435b | -3.58888 | -55.59412 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bbaf1de-56a5-3de0-aee2-17aea0db9bed | -3.67085 | -60.62793 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 252ede60-78f5-324b-ad92-07739f65b303 | -2.90353 | -57.65047 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12caa8a0-311f-34f0-a6fc-87372ee095e2 | -3.48078 | -59.58353 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3f4a94e-0ec7-30dc-b15c-e21175dbf04c | -3.27172 | -53.99401 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e66015c-82d5-3e6e-b93f-9d6b96921f96 | -1.52899 | -54.5362 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eaca522-6119-31c7-a302-9ec322093e41 | -4.79768 | -55.7266 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d07babba-3ce2-3024-8213-89a9fa326b83 | -3.47857 | -54.6312 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3179ef6-47d9-3705-a2ab-fdb7878c2ce1 | -2.99441 | -54.13239 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5393e8ab-c7e2-303a-8891-4ea7d3a969eb | -6.73442 | -55.13087 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4eed1da-add2-3448-92a5-206cd5058ab6 | -6.66575 | -55.08184 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16dd0da6-957f-3dc9-a503-4831d5affc68 | -5.72912 | -45.14482 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 320425a1-c78a-3820-9fad-185dfe012f80 | -6.11781 | -55.7828 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4859f75-5940-315c-a375-d999d2be8447 | -2.62913 | -56.65492 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6af61e3-d9df-323e-9d4d-ebe167a1a328 | -3.03836 | -54.10359 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d03026b3-5fcc-3f6a-afaa-ac1a95fd63e8 | -2.58407 | -56.16935 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9000c857-aa98-3c8d-bbc6-8347b0714557 | -1.24976 | -55.88171 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcf9edf8-a5e9-3b1d-80a5-8abac6bb146c | -6.11791 | -51.73835 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32063fbf-0ba7-3b7e-abb5-8b7eb13c0ac4 | -1.52219 | -54.51273 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ff275ac-0c86-3e7b-8ee2-82f36b23be74 | -5.73751 | -53.46291 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46493e2e-a051-3a1d-b970-d79b009cb04b | -3.20815 | -50.55901 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbac8ccd-d94f-3287-b4f2-88c6320cdd4d | -3.58613 | -54.68179 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d3a50595-edec-3124-add4-10acfbaf5dc1 | -3.04053 | -54.53078 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0974006f-cb3b-3d6b-9b52-829db86bca15 | -3.01602 | -54.13181 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b0415cc-5e42-3bc2-b797-a01ac2936e61 | -4.06391 | -55.32761 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca1a7179-81a4-3a6d-8b4f-5fbf50a41381 | -2.76569 | -54.11466 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51097987-d042-36f5-b449-3cb06fc1bc7a | -3.29412 | -61.01204 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f4bcb5a-ca63-3312-a998-ff95da981c22 | -3.18345 | -50.54689 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62035036-11cb-35a9-a89e-735c7f3adf9b | -3.53995 | -54.66754 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aecdbae0-e6e0-39d3-b3c8-dc9790d9f1a1 | -1.36691 | -56.92886 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f18e85a-2b85-3a90-ac04-f58ecd4f72e8 | -3.27908 | -54.03934 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f047bd46-d9dc-344a-a025-bfb0dda32155 | -3.08848 | -54.26776 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab89963c-b1a6-3087-8468-5a267ac68e88 | -3.5229 | -59.32149 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0375c3f-cabc-3ad6-8986-fb6de337ccf8 | -3.11908 | -56.66133 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae16bf51-1279-387b-a62a-07220fb515f6 | -2.84518 | -54.07091 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7e088d1-f3d3-326f-b6d5-4a4c6267fa04 | -3.19211 | -50.54819 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c684efaf-cb15-333b-9adb-495ebc4e61f2 | -3.0357 | -53.9355 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 573044d7-885d-3fa8-83f2-5a584928ef74 | -3.8705 | -55.998 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4477a70b-bf08-33bc-87ba-ece744f67457 | -9.48098 | -64.34867 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b752489e-5b5b-33e1-a5bd-ca8bd90f3e97 | -3.53319 | -59.49527 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ca85e7-19c7-386c-8f27-db687235d9a7 | -2.23766 | -51.92694 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed1bb249-b947-389d-9a17-0cb80764f7db | -4.41617 | -55.75151 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd81fca-4421-3f16-b8b9-d7b47e64b717 | -2.69269 | -49.04713 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7bed039-95f8-3221-966b-93f2c08c4252 | -3.52566 | -54.64625 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43f9e01f-ad28-385a-9c40-75c7e446db9a | -2.93048 | -54.14628 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f39c4c35-b452-32d6-86a1-a44df89aff95 | -3.97625 | -56.11433 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abb959d3-ee60-3241-94ef-2ef1225fc69c | -8.60282 | -67.30215 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22e69c6c-48bb-3b1f-b1a8-b27ad2c36864 | -3.05553 | -54.2674 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91255779-6f0f-3254-8095-4521d815ab34 | -2.94993 | -54.11377 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7a71200-7fe5-3a4e-be9f-297bc96c9136 | -2.97961 | -54.13017 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04bcfe9c-359a-369c-a0fb-60e6e87c0680 | -3.63376 | -59.54353 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f17bfce-f13d-3f70-8c03-07cd06ac686a | -3.80519 | -55.70407 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 686b3694-ab0a-333b-a40a-00c77d805287 | -8.73259 | -45.16663 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5764864d-a195-34dd-85ff-505a8c31116b | -3.06777 | -54.25772 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 817adcbb-d3b8-36f6-8609-71326ff51dac | -3.30541 | -54.05542 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dedb23ee-769f-3502-b0f5-6aafcabf2de8 | -3.06551 | -54.2495 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bad94da-aa19-30e0-9510-50c7ddee150f | -2.49636 | -58.07718 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c650001-959b-339e-bb60-84a7223ed202 | -2.98004 | -51.24344 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bef78fa1-406d-3c76-803f-586df3804206 | -3.47531 | -59.50328 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d663bb52-5c13-36e1-9ae3-cdba3d4d4077 | -3.31698 | -54.04802 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a4ed342f-47d7-3d3c-bb7f-b4cb490ed13c | -3.35182 | -59.5055 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5cb6351-18b6-3103-99a0-1a64b7f37bb0 | -5.06852 | -56.90882 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 540dd0a2-72b3-353f-8718-f48a3a6187dc | -4.57214 | -54.9602 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1868433b-be92-3509-aaa0-0c34a73224ee | -7.22425 | -55.10474 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 21ec1dc8-e8cf-3682-9cf7-cbe5003e8559 | -3.05181 | -53.90169 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c7f35b1-c03a-32ab-98f8-586e12bed217 | -2.37332 | -56.13295 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb4dd098-3f9b-31ef-854c-edfdff519a74 | -3.01482 | -54.1395 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6afba672-96fd-33aa-9fee-b4c6827fc076 | -1.18795 | -55.67373 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f6a2fac-bac5-3191-be1e-ab591d1fcedc | -2.48915 | -56.1511 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9415a65-9711-3d38-98ee-94bd7f2b7290 | -2.86125 | -59.30805 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b26965fb-ee50-3e9c-abd2-f974457012c1 | -3.98959 | -59.22317 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 285ce36f-c575-3d86-97cc-41be260f88f6 | -4.11998 | -59.87657 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30e94cbe-0148-3b47-898c-06eab7130eeb | -2.50528 | -56.17842 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d171982d-01bc-3383-8fb7-b457e80483a2 | -1.5023 | -54.83855 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5060b79-5682-3bd9-946c-3f6ee2190054 | -3.02021 | -54.75156 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6de13b95-cc2e-34fb-8555-2baea75d4404 | -3.31338 | -53.86687 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cfb9d5c1-d1e5-33cc-bb26-854d3ceb99b9 | -6.09175 | -55.72683 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c85e528-d27c-3e82-a647-c2ce1905699c | -2.5023 | -56.06812 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6ac10ee-e56d-33fc-a4ee-0aa9e91cd1b9 | -1.50849 | -54.82124 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29d8079f-19d4-3b99-9cfb-25486537d7d6 | -4.35147 | -43.78811 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 156aa1a2-3370-3148-987a-bcbfb8ef86cd | -1.20077 | -54.14028 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8001a61-4743-3777-9ab9-aac3dac3dd5d | -3.13045 | -54.36388 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf5cdc43-1652-34c0-a2f3-f825d84d7feb | -6.89809 | -48.71712 | 2026-10-08 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README161.md)
