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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e48ce74c-3ede-3914-b2b6-6577f2e97f9b | -2.67783 | -57.52753 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7ee59541-8edf-3132-91cd-59e805f1a633 | -3.733 | -61.7515 | 2026-09-13 05:53:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a51fa9a-8ac6-3dc3-960d-1675a547d382 | -3.79227 | -59.36611 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c56204e7-6f61-3cec-975b-253d1d725497 | -2.73935 | -57.63496 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d65674a-b65f-3b40-b257-eb5ecd3329e4 | -5.13713 | -55.96718 | 2026-09-13 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64379876-57b0-367d-93ad-7c42972a9a7c | -2.68177 | -57.54046 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1cd0816b-515c-3876-81f1-687f87dc48d0 | -3.16392 | -58.64724 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38dfff7a-fb5d-39c1-ab9a-b829002be8f1 | -2.67873 | -57.52751 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 84bcf4f9-0d62-315a-bb22-ed8db2d89283 | -3.76764 | -58.84408 | 2026-09-13 05:53:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8ebe2b0-af27-3e35-97e7-4a4d30f54f62 | -2.67087 | -57.53469 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7875d03d-d69b-3062-8f35-b3d96214d70d | -3.40679 | -59.2452 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf360478-1644-390d-8048-ddd17e7938f7 | -3.17127 | -58.65258 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04cfada2-f68d-340f-af72-dc745be63ed9 | -2.72044 | -57.64418 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb059a39-fd9f-3a60-9404-4e64b8d22c24 | -3.40764 | -59.24957 | 2026-09-13 05:53:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c409b63-3d1f-3dd9-86df-18da5c990af4 | -3.16685 | -58.64501 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 953ac24d-c9ac-39aa-8e8d-37c711e18439 | -3.44712 | -59.51875 | 2026-09-13 05:53:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40ec7072-2e24-3161-b1a4-72cb5bcb64f7 | -3.44668 | -59.52172 | 2026-09-13 05:53:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8f62d8c-ed37-3006-a9bc-7627f5573c3d | -2.68056 | -57.54847 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 93f1176a-1663-39e7-ab66-c021f09fd392 | -5.12348 | -55.96083 | 2026-09-13 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a5938e0-723f-350e-8ad2-f3ceaf2189cf | -3.13935 | -60.6274 | 2026-09-13 05:53:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e796453-1b85-38b2-b5ab-26aeea217cd5 | -5.12271 | -55.96667 | 2026-09-13 05:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 887c1aa9-994e-3a9e-a3ca-e905d9349dee | -3.16443 | -58.64386 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d730de4a-c99d-3362-bde5-49605792b2ce | -3.73738 | -61.75217 | 2026-09-13 05:53:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a48b7afd-eed1-31a8-8b75-80804cc015fe | -2.68238 | -57.53645 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ec0cd808-28e6-3c35-ac72-7c8e585a5f0f | -3.76714 | -58.84744 | 2026-09-13 05:53:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe10355-738e-37ce-be5c-f5cd0a964279 | -3.89415 | -60.59348 | 2026-09-13 05:53:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 959cb2f8-748a-3a29-853a-f2bca2f340ce | -2.67027 | -57.5387 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b396de5a-6b79-354d-8bf8-17380cc34415 | -3.72798 | -61.7551 | 2026-09-13 05:53:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a08dc3a-70d2-3df5-b75b-dfd054b0e96e | -2.21537 | -60.08633 | 2026-09-13 05:53:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27c7b6e0-e44a-3f6e-a750-4fe243657dda | -2.677 | -57.53959 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a76cdbbf-26ce-3ba2-b1f6-48e8a124938e | -3.16879 | -58.65144 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1e6a23a-584d-30e6-8cbe-58bf4a71007c | -3.16588 | -58.65176 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bc52313-0ae5-30e3-8c93-5da63f7e9481 | -2.67355 | -57.52256 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b0400bd1-bd3e-32a0-8a3e-d19f9e7e7dc8 | -2.67758 | -57.53557 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57fa2a78-9da0-3e6e-980c-a50c91a6874e | -2.72102 | -57.64022 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d0d53aa-9fa3-325c-9bb9-11b1778b13ae | -2.66994 | -57.50161 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61ee8348-6acc-3aa6-bc6b-e4e2bca6c25f | -3.15905 | -58.64302 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05b8b92a-b37f-3480-8ea5-462394b0e634 | -2.67723 | -57.53154 | 2026-09-13 05:53:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 44cbcae8-c41a-3a54-b62e-2c3942131aee | -3.1693 | -58.64807 | 2026-09-13 05:53:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2111fcd1-f3fd-30ea-af3a-09a4af24dfb8 | -6.75685 | -58.96142 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6af20fc-ca88-3a25-94b1-a1002e7ea534 | -9.17422 | -59.42395 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81627f5f-97e3-3cbf-8f6b-fdd88fdddab7 | -6.67728 | -58.87844 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 90446dc4-0f2c-35a2-a163-b6727ff2a3c0 | -8.53947 | -70.60589 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bb85fc1-d116-3487-9a59-61b69598c902 | -6.59209 | -58.84344 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9c023f94-7871-38a7-90b8-9893e292368d | -9.46202 | -59.19695 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78c5e80e-1c03-3b9c-8bb9-f8be75122833 | -6.59718 | -58.84796 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28c2307f-0a91-3638-b959-0cb6219942d5 | -8.77294 | -61.4075 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e77f2f94-6bd7-3064-b7f4-87a7c34c60c5 | -6.96277 | -59.74924 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69d4eb36-241f-3d39-8afa-ea5271155cbe | -6.10958 | -57.66759 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 309bc2af-12be-3485-84bc-8af820c59739 | -6.07225 | -57.87056 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff468c3d-afc1-3e96-b462-ea953dd7c699 | -9.1876 | -59.45268 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93442c81-3c7e-3777-8c6e-a2c4a2a7afbc | -8.86759 | -62.52489 | 2026-09-13 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d37ad1db-2f26-3f74-a764-9fd7346cc5fe | -6.08311 | -57.86512 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a44f26f-ff14-37fa-a6b5-16da4deffa69 | -8.54699 | -70.86166 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf17f67f-4e29-3c08-9fb8-2425be2f76ef | -6.31631 | -59.97149 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35d04fae-2165-3ba4-95f6-e6bd8920dd70 | -6.1085 | -57.62983 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c36698b6-5934-3cbd-b0b4-868bc289cae0 | -8.76882 | -61.40152 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6dd366a-1214-35a5-8663-175235c8d40d | -10.49052 | -69.69601 | 2026-09-13 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed18ed41-68c7-3179-ae0c-a497f5367b86 | -6.78273 | -59.85083 | 2026-09-13 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f78cfb20-c980-31c7-8431-8e3f328505f7 | -6.07133 | -57.86299 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f96c0edd-c1fc-3502-8e0f-cfda46928572 | -9.17664 | -59.62673 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d14805d-1e3a-3ba1-ad95-302abc59724b | -8.29546 | -71.05034 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb6819a3-a29d-3fdb-9519-490a7652f389 | -9.33714 | -60.28957 | 2026-09-13 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f38cb61-f581-374e-84bf-1843fee6b48a | -8.16494 | -70.18177 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21507cbc-9588-32ab-9a02-3ee7b3e4b21c | -6.74304 | -59.43369 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 625bb9f6-2972-3981-b9c5-9adf97c202f0 | -6.78317 | -59.84756 | 2026-09-13 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ac4c487-1a8d-31ec-a38c-7758044e77e3 | -6.30769 | -59.95742 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18a73cbb-5873-36d6-a67f-cb4e1e289172 | -6.67225 | -58.88171 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ce256bc-21aa-37be-9836-b0ab397e1245 | -8.4344 | -72.62006 | 2026-09-13 05:55:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d95b6d0b-49ac-3c10-a842-1dcf620bcbbc | -6.67887 | -58.87506 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e09a380-32c0-3a9a-a05b-33c77e5be487 | -6.75632 | -58.96524 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d611980-233a-30db-8cfd-6168cec8b0c9 | -6.13653 | -57.69403 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aea97f94-3fd1-37af-9deb-50939306ff70 | -10.74205 | -69.43544 | 2026-09-13 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11c92d83-fba8-3a3e-8ccf-68bfc9e002db | -6.27812 | -59.92848 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a73e938-801b-3435-9fcc-2c8ce52a5477 | -6.66109 | -58.8801 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6029efd4-11b9-3929-b9c1-0b816f1f23a5 | -6.67864 | -58.71253 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2af92399-c6be-3fbb-b7a7-2d5ffb9b77de | -8.03689 | -70.09176 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a394281-2da4-3c2a-8984-2383b7a33709 | -6.59259 | -58.83974 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8f759964-9056-3296-9067-7b78d15c9c5d | -6.76599 | -59.4265 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eba7e6f-daef-388c-b2a0-4a7d1805ba53 | -6.66719 | -58.87718 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8da2e5c4-3ac7-37a7-84cb-72f98d762517 | -6.30778 | -59.9956 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9de5c15d-0377-344b-ac7e-f2919aae4d8b | -9.18251 | -59.44808 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4d0e58-43db-37f5-9136-6f5eb8749fd8 | -6.07723 | -57.86402 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a5ff50f-9394-33a7-acca-936c38810dda | -8.86698 | -62.52941 | 2026-09-13 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e80b12c-17ce-3419-ad57-ca7f0bcb452d | -6.65958 | -58.88327 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0206c70e-b37d-3a19-b19c-d66f469445e1 | -6.60734 | -58.85706 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d96e5cd6-9cd7-3707-9dbc-4c9ed12e810b | -7.68129 | -69.92964 | 2026-09-13 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d745de4b-a9fc-3eeb-9033-1c1763c3bb0b | -6.28799 | -59.93333 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eecdedfe-8afe-3dc7-bb8d-53eef83d7a04 | -6.95702 | -59.75186 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9735bcd-d376-3f7b-8559-0986ab4efcd3 | -6.19112 | -57.7182 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3cc793cf-fed0-34fe-a848-e424b583cdd3 | -7.49695 | -73.25369 | 2026-09-13 05:55:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39649d2c-d159-3010-95ba-04727e9afd8e | -6.79748 | -58.79274 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bc40b110-cbd8-3a5c-b2f3-8f97b99f58c7 | -7.81451 | -69.99123 | 2026-09-13 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6550a373-74e1-336e-8c1a-258d0709f156 | -6.28888 | -59.92703 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48634a7e-26b6-3437-a24e-7c4c3e4c1175 | -6.31074 | -59.95863 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 518a0474-d8d0-3c0e-b1ac-ec3872724737 | -8.14246 | -70.15632 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bdd75c9-ae22-374d-9fa9-02aede29a6dc | -5.96802 | -57.76664 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3af2c207-2eb2-311e-86bb-03eb786fc515 | -8.75558 | -71.02796 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2f43723-d144-3154-b4a2-7408805a492f | -6.67122 | -58.88129 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b258fbbc-fc55-397f-8eda-46dc4e19c128 | -8.82076 | -61.40952 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README56.md)
