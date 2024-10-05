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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81d171f4-18d3-38f8-bd7b-4713b65d85b2 | -5.28627 | -47.32685 | 2024-10-05 04:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b3b200c-4e82-3288-9ea2-c055b425d298 | -5.43827 | -47.61395 | 2024-10-05 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d1e78608-af2e-3ad7-91b9-41c291e9931b | -5.43544 | -47.60982 | 2024-10-05 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e036fcb-c0aa-3d84-a21c-25145667be1f | -5.39738 | -47.69986 | 2024-10-05 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aaa2a1da-ef2b-363c-842e-a1576ade4d91 | -5.39401 | -47.69935 | 2024-10-05 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19436b7b-354e-3f58-9b70-a61e1ec72ff2 | -5.02285 | -47.71317 | 2024-10-05 04:36:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff9eedb8-0306-356e-8cb6-61d280bb90c5 | -2.02091 | -47.99258 | 2024-10-05 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 746be21c-997a-3d26-9542-0affaeb55434 | -2.02037 | -47.99603 | 2024-10-05 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df072c70-08a0-3e0b-81af-9ff75b02699f | -2.0176 | -47.99207 | 2024-10-05 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f53020e2-7c1f-3f8b-a5f8-705e5829b89a | -2.01098 | -47.99105 | 2024-10-05 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22072bc9-2d36-3a6c-a6a6-3548408741d5 | -2.01044 | -47.99449 | 2024-10-05 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 366ddbfa-d7f6-3a29-8508-3f1277ff7ed4 | -1.95458 | -47.87312 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a83f085-ea5c-34e1-acdb-b9dc8d619485 | -1.95404 | -47.87657 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 721f246a-bed0-3126-aee3-ce36bc95fdae | -1.5423 | -48.37866 | 2024-10-05 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 093dd15d-d3ce-3a83-b573-1cc047a54cdf | -1.32984 | -47.95914 | 2024-10-05 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 021fadf4-d5a2-38a0-a0be-025b081a3e3d | -1.0691 | -48.01625 | 2024-10-05 04:36:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cad3219a-d95b-339f-91f3-44ed5cef7df7 | -1.05891 | -47.93031 | 2024-10-05 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3aa2e704-bc31-3ca8-aa9d-ea9edcba3393 | -1.05837 | -47.93374 | 2024-10-05 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e610a5b8-cfe8-3143-8ca1-61ea635b8353 | -1.05561 | -47.9298 | 2024-10-05 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 96031eec-1cf0-34ba-9a3e-c412991d08a2 | -1.05507 | -47.93323 | 2024-10-05 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 50595660-a2bc-39ec-8faa-e66b6fe59e7e | -1.05453 | -47.93666 | 2024-10-05 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b69a7771-c724-377c-87d0-647dace26a46 | -0.7356 | -48.04176 | 2024-10-05 04:36:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ad74e6c-ce51-37eb-a6fe-6e101e1ae057 | -0.7323 | -48.04125 | 2024-10-05 04:36:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea02855e-35d2-3c1c-b62e-c729efb60412 | -0.73176 | -48.04469 | 2024-10-05 04:36:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c5ad276-3b96-36b7-a00e-99a85940872a | -1.7105 | -47.37323 | 2024-10-05 04:36:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1dfd65c-2a9a-3769-96d9-f34f161ba203 | -1.26405 | -47.66296 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 177aa050-0df7-3b77-8454-7413e5ce1e73 | -1.26351 | -47.66641 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64c7d961-8e0b-3f32-ac97-f3abf346e5e6 | -1.26297 | -47.66986 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a6ceeed-097f-361c-8a48-7061dabf5c0d | -3.27648 | -48.80189 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44912525-f1c0-3502-b882-eb47b7fe4230 | -3.12113 | -48.62233 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d667531-9af8-3997-8060-9a90f105adad | -3.1206 | -48.62577 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f63f47d9-1800-3b11-877e-31f63d8e81be | -2.93791 | -47.8205 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c2aa3bf-0397-3c79-913d-430c9f35da9d | -2.74831 | -47.8371 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ba72e7f-d622-3093-8e29-dfe9d410cfe4 | -2.55272 | -47.46074 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec3e7304-85bb-3bca-96cd-0d7f745eb728 | -3.46446 | -47.66586 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 338ff377-fe28-3c93-bcf7-cdd311ab7a09 | -3.34794 | -47.67303 | 2024-10-05 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10610bd2-61ce-38fb-ad7e-a80ea52ad27e | -2.91421 | -48.70636 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 480d5e04-6e18-3048-8713-151018e4492b | -2.91037 | -48.70928 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b24444c-bb41-31a9-b5b7-b8d5e263e95d | -2.87903 | -48.90866 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 630ba19d-f7c9-3fbc-bda4-e270462093c9 | -2.87573 | -48.90815 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9feea65-eb78-3ed3-a99b-f166197a89f9 | -2.79242 | -48.57474 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74860552-99e9-349c-a69a-fea3b3679be4 | -2.7902 | -48.56736 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65993faa-598e-3dad-b477-311c1ef8f5da | -2.77759 | -48.58299 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 944a4710-d63e-3beb-b339-66a66211e974 | -2.73447 | -48.90017 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ca9570c-e600-3358-acfa-207855f36ad8 | -2.72107 | -48.83464 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7d1bd89-3fad-3e40-984a-3455be7b2c3f | -2.43936 | -48.68074 | 2024-10-05 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b7aa4f5-b6c9-3a25-888f-d784aa558a9b | -2.43882 | -48.68418 | 2024-10-05 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc9d1da-5033-3c91-9a5e-cb628402eced | -2.39051 | -48.66661 | 2024-10-05 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e6073ec-3d65-3f0a-8d85-8bd27cfe469a | -2.30169 | -48.56092 | 2024-10-05 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3a8c906-7b52-3db0-bf06-d5e71ce0cbcf | -3.49443 | -48.90618 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4092e629-4355-362b-9264-04bdb28b2249 | -3.49389 | -48.90962 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b8b86c-fa76-34bc-bf4a-b69b163c3277 | -3.49113 | -48.90567 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 820b81ae-f865-3ba6-9beb-4b3c15cc5c35 | -3.49059 | -48.9091 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4670c8a-f5b1-3c51-ba96-aa92b19985f5 | -3.49005 | -48.91254 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9bfd9fa-760e-3785-ab8a-0e7aabce15ab | -3.48782 | -48.90515 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f2f8742-45d8-34f8-bfa3-54eb853e6487 | -3.48728 | -48.90859 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb171879-ea8e-3c70-9ae1-9ff5ffb1f2af | -3.48674 | -48.91203 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f39e569d-d188-3704-9744-fd2ecfab453d | -3.45318 | -48.82222 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d236ef-cfe3-33da-bb87-01c2b25b1210 | -3.45264 | -48.82566 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb57cbc8-9002-3558-b6c2-984955f19383 | -3.44987 | -48.82171 | 2024-10-05 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f7244b4-3435-3c8d-a87f-0bd66143e399 | -3.27702 | -48.79846 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b109d53d-64de-3a27-84a8-b90ad1ce9487 | -2.9092 | -48.91318 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 863e5d5e-17f0-3bce-a6af-93068529a42b | -2.90589 | -48.91267 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6964a356-ab41-3301-97c6-5621f65ec78a | -2.90535 | -48.9161 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c58a6f2e-3ed7-305d-8331-5363b7711cb9 | -2.78089 | -48.5835 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d65620c8-6076-3600-88bd-2ac05a388f1e | -2.7802 | -48.71709 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbe70298-f6d2-34cd-a9b0-8a47fd75970c | -2.74541 | -48.68 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5305fa6e-120c-3835-b064-6bf9e5bcce71 | -2.73501 | -48.89673 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f5e5ebf-f793-3afa-82bb-14d7022e2bab | -2.72053 | -48.83808 | 2024-10-05 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4be649c-94a8-3709-afe6-d55f3a3012c7 | -2.59814 | -48.03656 | 2024-10-05 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9668861a-1f49-3faa-9a5c-3fff4baf84f5 | -2.25787 | -48.45214 | 2024-10-05 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de62d11c-baf3-33fd-85ba-147ecbee2858 | -2.20213 | -48.15851 | 2024-10-05 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0591a215-6e18-38a9-afba-f83d17791764 | -2.20159 | -48.16195 | 2024-10-05 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e678a037-6ed8-3908-a81e-3dcd9015d1c9 | -2.1258 | -48.73054 | 2024-10-05 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ce15a34-2e3e-3092-ade0-1701b2609001 | -4.77833 | -48.0374 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9dcfa39-b0e7-316a-ad6d-58a2e68b1ca4 | -4.48193 | -48.10999 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e3574d4-5a81-3b8b-aff1-e076a8e202b0 | -4.28136 | -48.0679 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9961bbc-384e-325b-ba3f-b295f1aacb90 | -4.28082 | -48.07139 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41070105-e601-39ef-ae64-ac5b9f53936c | -4.19551 | -48.14016 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0ea6d7c-ed91-3f6d-9ec5-ffb8260f0b77 | -4.09593 | -48.27743 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0716291b-99a3-33e3-baba-1ffa4b7876d6 | -4.09208 | -48.28037 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 55b1cace-869b-38b2-ac3a-3b0725f45482 | -4.08751 | -48.26516 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6398044-4296-32e1-8f11-feb44f5ecd90 | -4.07949 | -47.94693 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3bcdff0b-fa50-3b05-9778-f3549216dc94 | -4.07617 | -47.94641 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f1444e03-80ac-394a-9629-079d28483196 | -4.07508 | -47.9534 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d400f24b-cd93-34d3-a84a-c15535fb8790 | -4.07284 | -47.9459 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1ed87567-8054-31db-9fca-57fa6e24db8e | -4.07229 | -47.94939 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 52011708-0fb2-37d7-9562-942a6bbbb52b | -4.07175 | -47.95288 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6f0f24dc-26a7-3185-81eb-78393227f9bf | -4.06896 | -47.94887 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c190179e-7504-3d42-afca-f5ba305a4f4c | -4.06842 | -47.95237 | 2024-10-05 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9d01584-f431-3f44-a0cc-4925161622e1 | -4.77851 | -49.33783 | 2024-10-05 04:36:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a862a70-117c-30d7-94ec-bef596d30be7 | -4.77521 | -49.33731 | 2024-10-05 04:36:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68c7691a-e59b-3bf2-88e9-fdfef56f9314 | -4.73838 | -48.83747 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8359ef33-e5db-3513-9eb1-0c1cc4f554d9 | -4.73561 | -48.83351 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90f8418a-fcdf-3276-8e2c-b37767e9abc0 | -4.73507 | -48.83695 | 2024-10-05 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d167b1-c380-3a72-bce7-8528a7a5c64f | -4.6202 | -48.07373 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c59c8c8-2b41-3b77-9965-452844ff22d1 | -4.61741 | -48.06973 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ab1834-9b14-39df-872c-25526e949bc5 | -4.57451 | -48.01665 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea47aee-6597-3228-a71c-1c0895833a07 | -4.38669 | -48.69775 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d863863a-0a3e-32fe-90e3-3b86713c668c | -4.38615 | -48.70119 | 2024-10-05 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README91.md)
