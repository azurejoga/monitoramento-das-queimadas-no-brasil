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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abbf6753-aee1-3db9-8956-f3ad7a52e31a | -11.18775 | -47.61618 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5b5b89d-dc60-329f-9ad2-75a86c227811 | -11.08199 | -47.80872 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdbb9631-eb22-3470-a3c8-efac8023dc13 | -8.84548 | -46.57952 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1ce096a-80ae-31d3-83ae-067d55714c77 | -11.8174 | -45.0157 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba42cb22-c968-3516-8335-dc62f991e9da | -9.93185 | -43.72701 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 372564b1-60f3-3ec9-b259-daf797aad90a | -6.82016 | -45.99168 | 2025-10-02 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a99b34d3-1eb2-3b45-90c1-88909ffafc84 | -11.05548 | -47.81194 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c12e4b1-e0ef-3793-b67c-1e0b5c579e23 | -9.93231 | -43.74902 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 5af2c6d1-0e96-3125-a9eb-c7a83a1ac3d8 | -9.73545 | -48.08139 | 2025-10-02 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cebda5d8-ecb6-31c0-b278-477dbb5b4e69 | -9.33536 | -45.69806 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8cbf7fe-6fbd-39a3-bc17-926897cffa34 | -10.39025 | -45.12176 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 353b6afb-8ea9-3d14-9fe3-1ef980285d30 | -11.12546 | -47.72892 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44715d03-9109-3bc9-b2f9-2a9a9bd170a4 | -10.85977 | -45.42078 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7e28743-db8e-31f1-8693-781fa7161899 | -11.17239 | -47.26003 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97c70db-8272-38b2-9542-2e7931f95c8c | -10.23191 | -50.31669 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0958dec1-1bdc-33f2-a518-aa8a669a4601 | -7.41464 | -45.19592 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 523af6ec-288c-32c1-a020-07c4da4bbabb | -9.94652 | -43.65384 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0443517-f3ad-3a18-be05-49ea1404474e | -6.96471 | -45.3294 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 544662af-6d8b-39bd-922e-a26d45b9e891 | -9.33425 | -45.7052 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ce6b86d-5166-3ba2-b649-c4038a90eead | -11.99999 | -46.57613 | 2025-10-02 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1c20ffe-2c3c-3cf0-8607-2347c2c43f11 | -11.14013 | -43.38527 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0cc2aee6-0911-32f8-ab02-b171102769f3 | -10.86574 | -46.60677 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cebe04c3-b0f8-3ab3-a231-426272b6b85e | -10.42496 | -48.30441 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9b66cb9-4193-3ecb-a85a-3717cdd681a0 | -8.90588 | -46.06303 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df0bcd2a-4fef-359e-82e7-01d4d663ca5f | -11.41981 | -43.4991 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6abcca77-af91-36c9-b043-e9bd17db8c1d | -11.68185 | -45.3231 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fb414dc-d930-36f8-9788-283fba5c4378 | -11.59212 | -47.64563 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 14d6c969-6c22-312f-9fdc-b9a436c5990f | -10.91878 | -44.31492 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ba02b32-7ef0-3df2-a524-25be86f53d37 | -10.22901 | -50.31188 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f0b3f35-95ff-3f6b-9c6b-f5e468d2ab33 | -10.84233 | -46.60307 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ff030a2-8e56-327f-82e8-c359bf4c7e37 | -10.66949 | -48.52495 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b7a5c5e-fe25-3f2c-9187-b23fe4d97bc2 | -7.72476 | -46.22274 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0020988a-f118-3b4a-b901-b84fe5398634 | -6.31807 | -43.04121 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f64c3f6-abd2-3d1b-a901-54306cc63f7f | -11.1674 | -47.27004 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be444931-e553-3548-bdb8-5cd3f6692f0b | -10.23334 | -50.3083 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b302648a-0f02-3983-97a8-9dbba3f367c3 | -6.77501 | -45.58975 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c6c18ee1-9dd9-3f85-ad11-2cf6d34de357 | -5.89723 | -45.64691 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caea9675-455f-330a-a41b-0c9bc1b51d03 | -11.00262 | -46.5554 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e526ab0-d0cb-3771-8ee3-692ac7e7584a | -11.03991 | -47.82388 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86886f09-46fc-34cd-8808-bd01c648cbac | -8.81179 | -46.6852 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79ec441a-4fce-31f3-9dbe-cbbed5beea15 | -11.56791 | -47.02697 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9e3738d-6347-34cc-9a66-bdc2767a5aca | -10.95483 | -46.66439 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 831fa1f7-d85f-308c-a475-dcaea870cdc4 | -9.40031 | -47.57984 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 221337df-b6b5-3d76-b3f2-842f671ebd94 | -11.43666 | -43.89315 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97324787-068f-3f6c-99d4-e95b7fe58ec5 | -9.39753 | -47.57578 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e43d992-5f4d-35a8-9fe5-cf5b0dd2b761 | -9.92945 | -43.71788 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c0723195-6a6e-3e21-8f14-0d769673aa8f | -10.81788 | -46.62823 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea3d4659-7a67-313f-86c1-e00d12b96be1 | -9.79622 | -45.94647 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee8338a1-8353-3465-9dcd-f6b3aba523d7 | -11.19575 | -47.73287 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f311286c-93e1-3171-bb91-16dc29afb057 | -10.82397 | -46.61103 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be7a9165-ee3f-34c7-9ddf-1555498aee70 | -7.17173 | -41.69714 | 2025-10-02 04:29:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dfe614bb-1aec-3290-b094-c83746a89197 | -5.84455 | -45.74873 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bf2d61a-c793-368b-bf7e-673756242425 | -10.83572 | -46.64564 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e15dd996-cf63-34bc-990d-edb2c76b151a | -11.00597 | -46.55594 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 775d8dfd-fd1d-3b16-8183-d4a8d196da96 | -10.85246 | -46.67012 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcaa9965-8c5b-3df6-9045-b258a4de2ceb | -9.40256 | -47.56576 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d6f82fe-afe7-3be3-a9e3-f8a8244d0041 | -7.29956 | -42.89044 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8cc316b8-0cd5-384d-98cf-98512cf88c76 | -11.44631 | -43.50308 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 722df6d7-a5ce-359c-8acf-cb43f73477ee | -9.43174 | -47.36138 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb4d8eb3-7fe2-3cb2-bbf7-078aa5e13e77 | -10.95872 | -46.66138 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86927226-bccb-3c7c-958a-81dd9dd4aea0 | -10.14369 | -45.29805 | 2025-10-02 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80f0c0b3-6a06-3af8-9f17-f1d25613d228 | -10.99707 | -46.59104 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a7ad378-771c-3be6-a604-b5214c4cb4cc | -9.82151 | -48.28367 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f02a17e-dbfd-346c-985f-b7bc2a74f445 | -11.75542 | -46.82413 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fceee22-c3d5-311b-8b30-ba16dce5f2cc | -11.0071 | -46.57072 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82289fe1-8c0a-3717-8aab-862812f05b2d | -11.47412 | -45.00246 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37c17c75-016a-32de-99a1-c4e28b800ca9 | -11.1962 | -47.77285 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2a54eb1-1d8a-33d6-b810-59c0b72d19bd | -9.92626 | -50.4918 | 2025-10-02 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 885896db-ebcd-31db-ab4c-dfb562759be1 | -9.79342 | -45.94234 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8ea58d1-23d2-3d2c-a851-6cb98ea0d347 | -6.73016 | -44.14138 | 2025-10-02 04:29:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b09388d4-6d93-3b5b-8234-b2984f530b21 | -11.80157 | -47.5817 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4dc4a96-4b2e-3bdf-948c-410afde432b1 | -10.25792 | -50.31684 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 84b3700f-fc42-3907-8e70-6bf55db19e7e | -11.79105 | -47.56189 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f83efba-59a6-39b1-ab8f-c639a87c9770 | -11.19129 | -47.73938 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8754a3f-2d29-3d24-b44d-1d70c8f0443f | -10.99544 | -46.62355 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fc7c3d3-3ccb-3f20-9d35-ca01ac346efb | -11.87108 | -45.01875 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4634086e-1864-3c79-96a2-57662148d03f | -7.51634 | -44.27941 | 2025-10-02 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9571fd77-737f-3608-98c4-bab0defcae0a | -11.86349 | -44.99702 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3e0272f-130c-3ae9-8ee1-7c9759e51cbb | -5.9621 | -45.89946 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8380d55c-a0f1-3d52-89b7-20a36acdfc1e | -10.63915 | -48.51984 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8273f41-444d-34fb-92ac-b65203c9903b | -7.60862 | -45.40621 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65876816-eb38-30ca-b292-14816c4ac817 | -11.10025 | -47.84428 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63c53a98-1ccd-3884-8d56-36790c982165 | -7.09552 | -46.58728 | 2025-10-02 04:29:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 428238d1-4f51-369b-affc-b70376f61c7b | -8.56086 | -48.64262 | 2025-10-02 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8582dc6-3c5d-3c57-9540-557458bf604a | -11.85174 | -44.9789 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2f35c72-3c11-3994-af1b-9c01650ca9ad | -6.68665 | -46.69347 | 2025-10-02 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d300795-8a35-3034-88ee-87940dfade92 | -10.86625 | -47.82473 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b8befd1-8bcd-3731-8c85-a033d4d6d98e | -11.61704 | -45.03395 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f2c80de-7c26-377a-8a90-6bb8ded28e41 | -6.28186 | -44.06026 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31af8df1-e793-3246-9621-91e3c8b1880e | -9.80396 | -47.84801 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 733f7f37-6b5e-3390-b0f1-2f6ecd8f7c08 | -10.34875 | -48.19971 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e691a39e-9824-3cdb-a849-18ba0f209948 | -10.24567 | -50.32337 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| afad8422-ab83-3bda-953c-4509297e45a4 | -11.09968 | -47.84781 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7c4ec79-5b23-385a-95ec-4b8306503f52 | -6.89566 | -43.13325 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11cd6325-e6a3-3017-b208-074c0d4ac879 | -10.44601 | -48.08714 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e797dc2-99f3-3a1e-964f-953554541f7d | -5.96265 | -45.89598 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ff6f02c-b9b1-3377-8206-be485e45ca9e | -11.81276 | -44.99874 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a573dac-3460-3bca-b76c-9653c9fe2ad0 | -11.00967 | -49.57998 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b535f731-6ee6-3fa4-b0a8-551793cd781a | -11.17239 | -47.28167 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| de76b249-15ed-3fb8-978a-2894e88ed357 | -9.80681 | -47.83025 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README76.md)
