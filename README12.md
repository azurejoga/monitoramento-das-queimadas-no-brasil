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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1929b32-a0a4-34be-855d-d837f3fe6001 | -5.0027 | -46.0331 | 2025-10-18 03:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| aec73a9b-c1df-38a5-ac24-553d140f932c | -10.4937 | -43.4552 | 2025-10-18 03:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| aaa1d70d-0aa4-3626-82a9-8aafe76ea78e | -10.9564 | -45.4579 | 2025-10-18 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| eee2d945-4b1a-3752-a331-5e797eba2fcc | -4.4633 | -43.2152 | 2025-10-18 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 715f7099-974e-3568-bece-bb42da06053b | -11.6109 | -44.0678 | 2025-10-18 03:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d9b198f3-262c-3d3c-b474-93c4219288f5 | -11.6104 | -44.0913 | 2025-10-18 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 34d704a7-42be-317d-bdcf-ceeaccb24e1b | -4.4632 | -43.2386 | 2025-10-18 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 100c646b-e5b1-38f5-ac39-3dbc12319227 | -3.1431 | -50.2464 | 2025-10-18 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| dd993bf6-4aeb-363a-ab93-3a5b30f23a0e | -10.475 | -43.4342 | 2025-10-18 03:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 633e360e-ff9f-31b3-b126-3083d0ecc92d | -5.0214 | -46.032 | 2025-10-18 03:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 148191dc-5afa-357a-bccf-d2b7a0d32fc9 | -4.4632 | -43.2386 | 2025-10-18 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 9ff4ab66-c52e-3213-8bd1-4f12d9fb8522 | -10.475 | -43.4342 | 2025-10-18 03:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7fc2ff07-5a08-30d1-9166-8a8ad894dc9d | -11.6104 | -44.0913 | 2025-10-18 03:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c99b6a4a-163b-327e-b74a-c9d4705f2bb6 | -11.6109 | -44.0678 | 2025-10-18 03:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 43cdcd35-a41a-3b09-88aa-110f332db984 | -19.1114 | -57.5486 | 2025-10-18 03:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| e567f35d-e1aa-3497-8db9-d3d10962f317 | -11.204 | -47.8318 | 2025-10-18 03:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 76e9de6d-9c4f-3957-a113-dfff30a7aac1 | -10.4941 | -43.4315 | 2025-10-18 03:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| be0299d0-ef00-3e64-a3c8-dc8d341a9568 | 1.7664 | -55.9608 | 2025-10-18 03:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 36a6d12d-e9ad-3801-b1ac-b42cd726c861 | -4.4633 | -43.2152 | 2025-10-18 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 213fbc7f-e2ad-394e-9068-d96fca6480c7 | -10.4937 | -43.4552 | 2025-10-18 03:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7202ca9b-cad4-3e10-bc7f-d925814de07e | 1.7664 | -55.9805 | 2025-10-18 03:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 7189bf31-8e04-39c3-b0b7-3074d521d4c5 | -4.4445 | -43.2397 | 2025-10-18 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c42c3ba3-2ab9-3cad-a3d6-4a636b4efcf2 | -3.1431 | -50.2464 | 2025-10-18 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0e977e96-f2c2-3849-bf2b-1eb7674e2258 | -5.0027 | -46.0331 | 2025-10-18 03:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e46dc34d-9aad-3cee-8d3a-d2611d6707c4 | 1.01127 | -51.19583 | 2025-10-18 03:57:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fb15d2eb-8615-350f-8634-afe8851e62af | 1.7664 | -55.9805 | 2025-10-18 04:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 89613a98-d948-3136-b715-9df57ec0483d | -10.9755 | -45.4553 | 2025-10-18 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 8c4b57bc-24e4-31f4-a427-9fb71254053f | -10.475 | -43.4342 | 2025-10-18 04:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c25c78c2-7a20-3848-84ae-68207cb99b2b | -10.9564 | -45.4579 | 2025-10-18 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| d19b4703-65b6-3d3d-825c-cf84b03ff305 | -10.4941 | -43.4315 | 2025-10-18 04:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 6b0734dd-39b4-3fd8-b343-902c3dab8fe4 | -10.4937 | -43.4552 | 2025-10-18 04:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ac91d89f-6e28-3341-9453-0daa5223803e | -5.0214 | -46.032 | 2025-10-18 04:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3444a91a-af65-382a-88a3-478707096a3c | -3.1431 | -50.2464 | 2025-10-18 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 03cc9c92-9410-3826-adde-f2d8d573f567 | -4.4445 | -43.2397 | 2025-10-18 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ad344b3f-8823-3666-9c68-614e7fb8d612 | -11.204 | -47.8318 | 2025-10-18 04:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 20b5f4b4-9acb-3f35-98dc-fb5d214028d5 | -4.4446 | -43.2164 | 2025-10-18 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| fe5cdd7a-a2d6-3f6d-bc4d-5b86c6c98c90 | -4.4632 | -43.2386 | 2025-10-18 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3833e2cf-df05-3804-a644-fe3d021e8011 | -10.956 | -45.4808 | 2025-10-18 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3d1c25a6-9cdd-3fd7-8a92-93c87e7867b3 | -11.6104 | -44.0913 | 2025-10-18 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 45373e33-9a18-3b91-b001-b536395cf247 | -5.01693 | -46.02664 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2caab7bb-0f92-3424-97de-43c9107c7041 | -5.79529 | -41.89876 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e22152db-038c-3f52-9efd-90043d8057ef | -4.0001 | -45.50198 | 2025-10-18 04:00:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b070b3b7-2c8b-3b22-98d4-214fbe3fa163 | -5.84239 | -45.73084 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b636b02-e57d-393e-b1f1-abb12790ff29 | -4.84566 | -46.72141 | 2025-10-18 04:00:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ac19787-aadf-352e-ac04-12205e3d8174 | -5.92954 | -45.44016 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ecda697f-7f5c-39f1-bf14-49ded5ba65a6 | -2.73908 | -49.39181 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4225de92-1b08-3b26-96ec-ce5814f35e68 | -4.73239 | -46.1594 | 2025-10-18 04:00:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 27d3ee84-c0b7-320a-9230-466adaa97652 | -6.32051 | -40.30021 | 2025-10-18 04:00:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca531554-fe74-3d4d-97f8-ff5b45444d53 | -5.014 | -46.01683 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| dd225f11-3c8d-3a76-ba6e-3a96dd5fd982 | -2.86388 | -50.73545 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f794394e-0198-378e-a590-e820591b4da1 | -4.69378 | -48.62778 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5afa9589-9624-3489-9936-666ff6d4c174 | -4.91338 | -45.40975 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bba79930-98ff-31bc-a955-798d7dbdb8e0 | -6.14541 | -44.28872 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0eedd730-2af1-3500-a45f-27beefee1558 | -6.36388 | -45.7795 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43641a07-0afe-3407-a8a5-b6d07c58fe2d | -3.10353 | -39.78366 | 2025-10-18 04:00:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1bf878e-e20c-3942-b94a-cb6f33ff8884 | -4.96832 | -44.61058 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73fd0f1b-3d57-3ff8-8e18-fd508fa091bc | -6.74119 | -43.81011 | 2025-10-18 04:00:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a891f818-ba2e-3ffe-b34d-6aff9696eea1 | -3.24593 | -45.97001 | 2025-10-18 04:00:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9102d641-e7a8-3aef-8588-88380539d4c7 | -2.74549 | -49.38874 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cc8d4c1-6aff-3f33-a992-d183f7d086f0 | -4.9724 | -48.36232 | 2025-10-18 04:00:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f7efc49-1e1d-37fc-b68c-eeb67011067e | -5.25511 | -47.24135 | 2025-10-18 04:00:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23e4f153-e5d1-3f02-9f25-973daaffe27c | -6.41598 | -42.01525 | 2025-10-18 04:00:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b310f8b1-b449-3ef9-b28a-e498776d7855 | -3.1478 | -50.24651 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 95e2841a-5574-3123-9669-d99ca8d219a8 | -2.37059 | -48.29403 | 2025-10-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbfd3958-e579-323a-9fa4-3316e25fff5f | -5.1563 | -44.93963 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a2985c5-234d-3992-a67f-5d82ac64ce4a | -6.59856 | -42.08135 | 2025-10-18 04:00:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f8094900-714e-3115-9b49-5f75d620b799 | -5.65501 | -46.81594 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b427a54b-b38f-39ec-9e29-fca5ae7c6f03 | -5.85126 | -44.34127 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b273d017-fa67-3677-a71c-aea6421a26e6 | -3.15951 | -49.166 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 475ce639-9d31-3092-94b0-f9cd59e5be0c | -3.68032 | -45.63556 | 2025-10-18 04:00:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8edb1a9f-8bf0-38d4-833a-72b5a29fc95c | -5.29814 | -45.47427 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe1ce4b8-20de-3591-8220-3ea25c420f18 | -3.15039 | -50.24075 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2ad32fa5-4646-3084-bd67-8a9337c77d30 | -4.28134 | -44.61894 | 2025-10-18 04:00:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ed4ef6d-7697-3dc6-8f4c-52f9fcb5e83d | -2.80723 | -48.66128 | 2025-10-18 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bb09cb4-0d69-3180-b20c-3b5c6d0f43c4 | -4.49892 | -46.48601 | 2025-10-18 04:00:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 993239b3-0c7c-3f03-afb1-aa3d2d54043e | -2.36006 | -47.54387 | 2025-10-18 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e83aadb3-87bf-31da-94a9-4adab6f1f76b | -5.8336 | -40.81778 | 2025-10-18 04:00:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5f4b4b7-a608-316b-ba20-c2dda31c11c0 | -3.25045 | -45.97082 | 2025-10-18 04:00:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4861355b-eac7-3df4-81a1-c355af429c13 | -7.10815 | -40.3335 | 2025-10-18 04:00:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c5f2959-d4c1-35b2-bbc1-8b21c9fb4f62 | -4.96548 | -44.60285 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34bd35ce-1d8e-376e-881a-f0859436a9f9 | -6.36815 | -45.7801 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6661ce2-5866-3ae0-810c-e7d666c15434 | -6.21002 | -44.68121 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f1d33a3-16a9-36ce-ad36-4ecea4d1588a | -4.99601 | -43.85672 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5c632aa-d780-3dda-9c4c-79996bcd78f2 | -5.3091 | -44.84973 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e83e02ff-47cc-334e-89d3-68f9a656f724 | -5.85494 | -44.33937 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 956cfeb4-25d8-3630-a6fc-b790d7633406 | -6.72252 | -44.3765 | 2025-10-18 04:00:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61233890-3f4d-384e-bdeb-c4962d9a9c05 | -6.13842 | -44.28291 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebee4f38-e7a7-38cd-be04-89c46764e23e | -6.30494 | -44.71542 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0876d2de-7908-3a84-ab24-19aa11a28ce2 | -3.7636 | -41.73306 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e732e3c2-2378-37cb-ba79-b2245cccb8aa | -2.87556 | -50.74242 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc5ceaac-1119-3018-a1ca-6dfabc008ffd | -5.71627 | -43.82515 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9adff529-9e25-39a9-a0eb-fb805999f795 | -3.57244 | -49.44469 | 2025-10-18 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e8db42c-2646-3db5-bf3c-3f1d3b22762a | -6.48326 | -44.5619 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d92954e1-898b-364d-8244-ad891cbe2a95 | -4.24675 | -48.56514 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8933b2c7-c153-39ce-9074-0a937c6aa3dc | -4.30399 | -48.06591 | 2025-10-18 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 760b3b31-fb1e-3da4-b731-4c3d5e5ad3f3 | -5.91445 | -43.94181 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c9a06e4-706e-31a9-9a4b-70fc98faca7f | -3.80296 | -51.65062 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dc059e5-f504-3519-b0f2-0ff79625ea46 | -6.05788 | -43.39996 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 589a10fa-56d9-3291-97d5-d86e7f22376e | -4.53647 | -48.41436 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45abccd5-67af-3799-a5c7-b7288bd5f346 | -3.06327 | -43.22254 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README13.md)
