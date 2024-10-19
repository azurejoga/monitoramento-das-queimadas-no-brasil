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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6c84b79-6190-3d46-b6d3-ea0bad1632f5 | -2.9517 | -47.9893 | 2024-10-19 00:36:02 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e912df92-e440-3f15-858a-61d7d5dec0e8 | -2.9535 | -47.996799 | 2024-10-19 00:36:02 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07776d68-93a6-3945-87b4-0143aa49aa44 | -2.9419 | -47.991501 | 2024-10-19 00:36:02 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5ce44d-d4a1-33a7-9bd9-d37ec320e351 | -2.9437 | -47.999001 | 2024-10-19 00:36:02 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1c0dea-ec4f-3cf9-b4ba-bcb2eb9b126e | -3.4555 | -50.3536 | 2024-10-19 00:36:03 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78811c81-0153-34f6-9f82-92e7aed06ce4 | -3.4577 | -50.363602 | 2024-10-19 00:36:03 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aba0db6-eaa8-3a54-b6a8-4b4d44d6884c | -3.3704 | -50.340801 | 2024-10-19 00:36:04 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f825f18c-9c28-3da7-ac81-e3684d246374 | -3.3727 | -50.3507 | 2024-10-19 00:36:04 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541cf56b-8a95-3e7a-aacf-f1af451c88e3 | -2.8644 | -48.239601 | 2024-10-19 00:36:05 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e7cdc77-7a6f-3582-95a9-aa3e2e32c175 | -2.8662 | -48.2472 | 2024-10-19 00:36:05 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d674fd82-3c29-382f-9245-3da23459dde7 | -2.8546 | -48.241699 | 2024-10-19 00:36:05 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d1ceaf6-285f-3158-b239-e0fa5d4a9ebf | -2.8564 | -48.249298 | 2024-10-19 00:36:05 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0306f724-136a-3257-a7e4-c5edef3918fd | -2.8581 | -48.257 | 2024-10-19 00:36:05 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c523f14-c97f-336b-876a-e5070e1ff2fb | -2.5544 | -47.059898 | 2024-10-19 00:36:05 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b23c21-f6b9-383e-9c84-452389d60baf | -2.556 | -47.066898 | 2024-10-19 00:36:05 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86cb77cb-7c33-310c-8a6c-4416548bd6b4 | -2.5576 | -47.073898 | 2024-10-19 00:36:05 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aed18c2-4de6-3984-8a33-b19dd067d1f7 | -2.3122 | -46.137001 | 2024-10-19 00:36:06 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3727e2be-7c95-32f5-a7cf-01a27e1087cc | -2.3138 | -46.143799 | 2024-10-19 00:36:06 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad1d9038-61d2-3fd7-98ec-32917b52226b | -3.0366 | -49.407501 | 2024-10-19 00:36:06 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 998a2a9a-c84d-3aa2-aebc-865ca73f9ed8 | -3.0386 | -49.416199 | 2024-10-19 00:36:06 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ea4e27-30dc-3e8b-8b98-60d8aea95f8b | -2.5195 | -47.2229 | 2024-10-19 00:36:06 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1785929d-ab97-398b-9c9f-3675aa730e05 | -2.5211 | -47.2299 | 2024-10-19 00:36:06 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4877a3-8161-373f-aa33-48c746877e9e | -2.7746 | -48.5695 | 2024-10-19 00:36:07 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ae06ea-3e0d-3d7e-aa94-6334fb682c41 | -2.7764 | -48.5774 | 2024-10-19 00:36:07 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c023e6d6-4896-315d-af2f-f46fc606955e | -2.3398 | -46.4823 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ec26c2-ec01-3c0d-91f2-72c3c52a56d8 | -2.3414 | -46.489201 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b84cf5a7-40ef-300f-8b96-01fac1d10082 | -2.3429 | -46.496101 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ef5944-425a-3e37-8f80-5facf0010d67 | -2.3524 | -46.537201 | 2024-10-19 00:36:07 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8355d5-4277-34ed-9836-662c18de699a | -2.3539 | -46.544102 | 2024-10-19 00:36:07 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 070ce146-850c-3fb3-9d25-0f3c7bf6730d | -2.3933 | -46.716 | 2024-10-19 00:36:07 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac389644-8a27-3087-81bd-d84ac78b6183 | -2.33 | -46.484501 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 339b5d00-d5ff-3efd-a34b-6de4f1dee416 | -2.3316 | -46.491402 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 991a6078-2547-3d58-baaa-beae27f59d25 | -2.3331 | -46.498299 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07210784-0cb6-33fd-8312-f2ba8e63783c | -2.3347 | -46.5051 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af6f521-b2dd-3bad-9755-c6446a97a835 | -2.3834 | -46.718201 | 2024-10-19 00:36:07 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd023349-1b27-3721-9a0b-305e516adba5 | -2.3139 | -46.4594 | 2024-10-19 00:36:07 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e09ac910-8667-353c-9892-fce4044188d8 | -2.3507 | -46.9804 | 2024-10-19 00:36:08 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 428ac27b-392b-3f27-b705-872d4d4beac1 | -3.3061 | -51.058701 | 2024-10-19 00:36:08 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88524fc3-c7d0-3b42-90cc-7076035ba1da | -2.3605 | -46.978298 | 2024-10-19 00:36:08 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 553f3ff7-aeaa-3168-8fa8-d0960e710bef | -2.8857 | -49.376801 | 2024-10-19 00:36:08 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0f6ce6-c8e8-3dea-bfb4-a6f6b0350e8a | -2.2446 | -46.741901 | 2024-10-19 00:36:09 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67655d9b-b0c1-3741-915b-b59a5b88e2e6 | -2.2461 | -46.748798 | 2024-10-19 00:36:09 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e12af7-d385-36c6-86ee-476ce232b40c | -2.6436 | -48.491299 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b386b5a-59d2-3b1e-b18a-b6af46fcfd40 | -2.6454 | -48.4991 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca64da4a-12e7-374f-a21b-b79d069adfdd | -2.6338 | -48.4935 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec0911b-4868-360c-9e3c-641c114158e5 | -2.6356 | -48.501301 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5919bea2-775d-34c0-a641-5b0664421c3e | -2.7097 | -48.827202 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0084163e-848b-3c05-8d13-8c13192485ff | -2.7115 | -48.835201 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72203fc3-a8c6-37a0-ba99-353f25e9de09 | -3.0559 | -50.357399 | 2024-10-19 00:36:09 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dea40dce-3593-38ac-86d3-5ee7a5e50486 | -3.0582 | -50.367298 | 2024-10-19 00:36:09 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 228f533a-6b81-3be6-9066-984181489ea5 | -2.2171 | -46.7118 | 2024-10-19 00:36:09 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4b7da4e-06c5-318d-924a-1122fa141da7 | -2.2297 | -46.766899 | 2024-10-19 00:36:09 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc864aa-d0d8-366d-ba5c-dc999f470665 | -2.2313 | -46.7738 | 2024-10-19 00:36:09 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 019af370-a4ee-39a4-b64a-0b781af71102 | -2.6999 | -48.829399 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccfbfd7b-838c-33da-8ad8-2bc9bc300a5a | -2.7017 | -48.837399 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b37056af-d475-3e04-b7c3-5eb7eb9bf78d | -2.7036 | -48.8456 | 2024-10-19 00:36:09 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e82b42eb-b01c-32f4-a730-f5d36d520b79 | -3.0461 | -50.359501 | 2024-10-19 00:36:09 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 447e6990-f927-39fd-8068-77cd91c54744 | -2.1369 | -46.542 | 2024-10-19 00:36:10 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94910b30-e685-346e-9578-b77b3fe5da8b | -2.1385 | -46.548901 | 2024-10-19 00:36:10 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009a3f9c-4b74-3da7-b348-e91ef9584860 | -2.5601 | -48.395599 | 2024-10-19 00:36:10 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 591908a9-d2a8-38bd-8f4e-d01f93f6e48f | -2.5619 | -48.403301 | 2024-10-19 00:36:10 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d2ee76-9a21-3ed1-912a-b67d780537c6 | -2.7042 | -49.166 | 2024-10-19 00:36:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15b41fe0-edb8-3e88-853e-929db6e19a09 | -2.7466 | -49.353001 | 2024-10-19 00:36:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5098cb23-b9d5-389c-9c57-e20172bca1f8 | -2.7486 | -49.361599 | 2024-10-19 00:36:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9c0ab62-37f9-32f5-ab05-bc6e598fa0b0 | -2.7505 | -49.370201 | 2024-10-19 00:36:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e632df42-bba7-356b-b1c2-a0ce0e08977b | -2.3393 | -47.607601 | 2024-10-19 00:36:11 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7676c6e-066b-3755-b789-dc5d724b95b0 | -2.341 | -47.614899 | 2024-10-19 00:36:11 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd0fdfa-f7e8-3610-acc8-083d09f5b8f9 | -2.6925 | -49.159801 | 2024-10-19 00:36:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da096175-41a2-39bc-b3e7-b425d5bc8f16 | -2.6944 | -49.168201 | 2024-10-19 00:36:11 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba7ba78d-0061-3be5-b51e-e95dcd9e30cb | -2.1699 | -46.911098 | 2024-10-19 00:36:11 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bea92ed0-d6d1-3550-8f83-4dce71f855f2 | -3.1363 | -51.3074 | 2024-10-19 00:36:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb8b72c-49e9-3fc0-9751-be2444e10a62 | -2.133 | -47.065399 | 2024-10-19 00:36:12 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40ba1a56-629f-3c32-b60d-77255d9dfcad | -2.6091 | -49.064301 | 2024-10-19 00:36:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a02413eb-9acb-30c9-b986-755a902390d2 | -2.611 | -49.072601 | 2024-10-19 00:36:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d891c71-2e74-306e-a38a-e1b7aa579f64 | -2.6106 | -49.116299 | 2024-10-19 00:36:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84e6f754-5b7c-3500-ae10-af782f303dc0 | -3.0719 | -51.202999 | 2024-10-19 00:36:12 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7de66571-5675-3f29-b8ec-a9406c8d2f16 | -3.0744 | -51.214199 | 2024-10-19 00:36:12 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b48c0a9d-ed15-3245-a655-753c4788e66c | -3.0769 | -51.225399 | 2024-10-19 00:36:12 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5b579a3-745f-30bb-8e20-1a3e734dec95 | -2.5517 | -48.947399 | 2024-10-19 00:36:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eca39385-e7a8-3c4d-aae9-0fb0b9d58195 | -2.5891 | -49.112301 | 2024-10-19 00:36:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70cd310e-a490-38cf-b5a8-c9d90936fec8 | -3.0621 | -51.205101 | 2024-10-19 00:36:12 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd847cd-2eb7-3e80-91b6-60a7e54265b1 | -3.0646 | -51.216301 | 2024-10-19 00:36:12 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f421a3fb-5d35-3f5f-926b-28f367129dac | -2.3504 | -48.289101 | 2024-10-19 00:36:13 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4440a019-489f-3a92-9b60-17c92a6cd7e0 | -2.3522 | -48.2967 | 2024-10-19 00:36:13 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f409ca57-194b-3d10-a500-688afd4d3c26 | -2.4012 | -48.5121 | 2024-10-19 00:36:13 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 912d9169-5609-3a27-a35d-e1931cf90d83 | -2.971 | -51.0284 | 2024-10-19 00:36:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4035566-7a70-3db2-86f0-67644e942fb3 | -2.9734 | -51.0392 | 2024-10-19 00:36:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d439f13-aae3-37e2-8e0c-a06fa7605c92 | -3.297 | -52.846901 | 2024-10-19 00:36:14 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b762908-02dd-3f5d-852f-7de764ec0b06 | -3.3002 | -52.8615 | 2024-10-19 00:36:14 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 871d989a-47ec-317d-b80f-6fe02822c5e4 | -12.0041 | -63.5008 | 2024-10-19 00:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3b30d9eb-ac91-39db-afdc-f3c07697d44e | -3.2872 | -52.848999 | 2024-10-19 00:36:15 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0299088-a8bc-3342-adcf-6937e06d12b1 | -3.2905 | -52.863602 | 2024-10-19 00:36:15 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007555cd-58b6-369e-ac9e-d9f61825e63b | -2.3954 | -48.939098 | 2024-10-19 00:36:15 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03159763-0174-3610-9d83-664167c26195 | -2.3972 | -48.947201 | 2024-10-19 00:36:15 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98549c87-1ceb-3e61-af5c-0488e2f705cc | -2.4586 | -49.398399 | 2024-10-19 00:36:15 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73388709-80ae-3204-8ba7-bf2e0ad2c8d9 | -2.3189 | -48.8288 | 2024-10-19 00:36:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 453b194d-f8e4-3ac9-90f1-a2b5220c53cd | -2.8278 | -51.303398 | 2024-10-19 00:36:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc7448c-b5e4-3075-8cdf-bece1b92d065 | -12.4958 | -63.3024 | 2024-10-19 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5b4eea58-4980-3db4-a4a0-a07c99fb716f | -12.496 | -63.2832 | 2024-10-19 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c51a808c-6c2d-3172-b521-ad89280e78da | -12.5147 | -63.3014 | 2024-10-19 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.3 |


[Clique aqui para ver as próximas entradas](README5.md)
