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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5f97e71-92ce-3498-8858-f65bdf78f4ae | -6.6504 | -59.9594 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9f6ea9-93ef-3a4d-bb7d-7bc04b711d8f | -10.4111 | -50.2469 | 2026-09-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c1001cab-18c1-3c7e-8a68-bf5e493ae5d8 | -7.5703 | -57.6962 | 2026-09-21 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 69c1b2ce-abdf-3b78-be7c-3c6ed2c90ef7 | -9.4567 | -45.4178 | 2026-09-21 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| b14a8877-3002-35fe-834b-d9db60a95383 | -9.4757 | -45.4156 | 2026-09-21 01:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 925581a3-c68e-3ed7-96a5-d703bf5f9a37 | -11.8017 | -49.7913 | 2026-09-21 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 14f34609-9123-3307-9620-66aaed49a259 | -7.5704 | -57.6766 | 2026-09-21 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 4c65bcd1-9f2e-3a39-9e7b-cce5b4bb58ac | -4.3357 | -55.6659 | 2026-09-21 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3da75cd5-619b-3b76-87d8-a15790ae8a1b | -7.5888 | -57.6953 | 2026-09-21 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0e559daf-b169-3b92-8f04-bdb70b9221bb | -10.0712 | -50.26 | 2026-09-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| c7080395-643b-3df4-a074-2bfa73bdc41b | -9.457 | -45.395 | 2026-09-21 01:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 08551c9a-33a6-3208-977f-e09dc87dc3c6 | -6.4486 | -59.9717 | 2026-09-21 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| faa9d6b9-bdc2-35da-959c-1ffd2fd94b10 | -6.2026 | -57.7778 | 2026-09-21 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 61f22797-7bed-3170-9e9b-cb476f6effcb | -10.3921 | -50.2488 | 2026-09-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 26089e5f-3768-3678-81f7-8b8acaa6109b | -9.476 | -45.3928 | 2026-09-21 01:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 2076afa3-cde3-3a4c-94b8-0161904a0584 | -4.3541 | -55.6653 | 2026-09-21 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fbd19616-5891-367d-ae9c-0f01a27e7af3 | -10.09 | -50.2581 | 2026-09-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| d2d26ff9-719a-3dbe-8e95-a4468c5d7b7b | -3.4241 | -59.2535 | 2026-09-21 01:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e99a6960-917c-3ca8-9e17-328b9ce5e926 | -7.5889 | -57.6757 | 2026-09-21 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 93705510-6ecf-355a-bec0-efae52f71fb2 | -3.0534 | -61.2767 | 2026-09-21 01:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b46771e2-4f15-3ce0-8f4c-2c6e078dd876 | -3.0717 | -61.2764 | 2026-09-21 01:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 88f8640b-b720-36e3-8b40-2a50d4836711 | -11.8014 | -49.8129 | 2026-09-21 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 7a02372d-3542-3082-9ee7-1812e2d7c483 | -10.0714 | -50.2387 | 2026-09-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| ba41a25b-1bbc-3c79-b28f-3094a68af06a | -10.4483 | -50.2858 | 2026-09-21 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c78a96a4-2675-353b-a3b9-5bbb04ced3b4 | -10.7451 | -50.7025 | 2026-09-21 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5a75621f-9717-3393-8723-6fb085dc123f | -9.4757 | -45.4156 | 2026-09-21 02:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0af44917-10b2-31c3-b513-46a65ecaf0f4 | -7.5703 | -57.6962 | 2026-09-21 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| af5d5097-3b54-321c-b6e1-7419140eb28e | -11.8204 | -49.8106 | 2026-09-21 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c28f93ee-a3f4-38ac-88f4-dcf22fbbe535 | -9.4567 | -45.4178 | 2026-09-21 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d3b34ec7-959e-3fc6-9bbe-321e36043268 | -3.4241 | -59.2535 | 2026-09-21 02:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 7f258695-3812-3997-9a88-b20efbeed8c8 | -10.4297 | -50.2663 | 2026-09-21 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| dbfb87d6-af69-3439-ba2f-8010bda75786 | -10.0714 | -50.2387 | 2026-09-21 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 97eed1bb-7071-352f-aaad-f00036cb98bc | -11.0997 | -51.0687 | 2026-09-21 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e8847bcb-2097-330f-b91b-511a4de4d8b9 | -7.5888 | -57.6953 | 2026-09-21 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| dc644fd1-4448-30a7-8285-7ed22fd563f9 | -11.8014 | -49.8129 | 2026-09-21 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 74e11dbe-f025-376f-801e-922c4acc6065 | -10.0712 | -50.26 | 2026-09-21 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| a132f702-cf5a-3b72-920c-fb28678c4462 | -7.5704 | -57.6766 | 2026-09-21 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| acdd528f-870e-3c5b-82fe-065cf0c64dbb | -6.2026 | -57.7778 | 2026-09-21 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8ea39ea0-b5b3-38f0-9a9a-934ce534337e | -11.8017 | -49.7913 | 2026-09-21 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4da4c2ea-84f0-3fd3-ab97-6f6bc0db01a6 | -4.3541 | -55.6653 | 2026-09-21 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 6e6e2142-fbcf-3299-8554-c0b07be0a015 | -3.424 | -59.2726 | 2026-09-21 02:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3ab8c05d-1916-3535-9e7f-446ce032332d | -6.4486 | -59.9717 | 2026-09-21 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 65fb3589-1a37-3cbc-a794-098259805a79 | -9.457 | -45.395 | 2026-09-21 02:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c476b0d7-a590-3e4f-aefd-19243f9f9f05 | -6.467 | -59.9902 | 2026-09-21 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ddb5f383-d35c-313b-8ec6-bd9c8dae720a | -10.09 | -50.2581 | 2026-09-21 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 21c5c4a9-0dfb-34a0-b02c-73045e7f671e | -3.0534 | -61.2767 | 2026-09-21 02:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 36096799-ff8b-3a51-bb36-63c98c674c2e | -7.5889 | -57.6757 | 2026-09-21 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 90e67827-6c76-3a32-b563-d9d3302ef051 | -3.0717 | -61.2764 | 2026-09-21 02:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c6330d59-76fe-395f-81c2-9f94e4370775 | -9.476 | -45.3928 | 2026-09-21 02:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 044ad1ea-47c5-3fab-a5fe-d51d2d64c042 | -10.4111 | -50.2469 | 2026-09-21 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6fe156ef-8099-30c0-82e3-66df51cd9ae7 | -10.0712 | -50.26 | 2026-09-21 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 75069022-19a2-3c8d-996f-41f3f43bd4b7 | -3.424 | -59.2726 | 2026-09-21 02:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0458cbdc-15f0-32f3-8b04-4c316cf07905 | -7.5704 | -57.6766 | 2026-09-21 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| cf46effe-f318-341f-a1a9-907c37d5024f | -7.5888 | -57.6953 | 2026-09-21 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 847314ad-2cac-33c5-ba95-4cef6858d912 | -6.467 | -59.9902 | 2026-09-21 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0a664321-bc71-32f3-a79e-cfc39f9fae53 | -7.5889 | -57.6757 | 2026-09-21 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 13afdc5c-8faf-330c-82a1-b9589865975d | -10.09 | -50.2581 | 2026-09-21 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c72f2910-05f6-3ca1-ac15-565abe07f0fe | -3.4241 | -59.2535 | 2026-09-21 02:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 35515e95-0922-30ce-94d0-ffb4ce0a8c2e | -7.5703 | -57.6962 | 2026-09-21 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 63dd686d-f782-38d7-81a1-e62c3d5d9069 | -3.0717 | -61.2764 | 2026-09-21 02:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 763584df-9ed8-3cca-aed1-80d89868fd1b | -11.8014 | -49.8129 | 2026-09-21 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| fe5d8ffd-1296-3fea-b671-98eb17e107d2 | -11.0997 | -51.0687 | 2026-09-21 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f4b9cd36-d9ef-369e-a9e7-53f6d54f5981 | -6.2026 | -57.7778 | 2026-09-21 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 12ff35ee-22f1-3833-af9e-a05f98b49214 | -3.0534 | -61.2767 | 2026-09-21 02:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| cc10d967-a54d-3340-af56-d1b76b004ea8 | -6.4486 | -59.9717 | 2026-09-21 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b6a0a9ca-51a5-3765-9016-367f31de4fee | -10.0714 | -50.2387 | 2026-09-21 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 28c2ce42-c8b8-3b01-b098-78c38431c186 | -4.3541 | -55.6653 | 2026-09-21 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a60e9867-d8ea-3e0f-9c4b-c2189276fa4d | -10.0903 | -50.2368 | 2026-09-21 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8577dd27-4dc4-3fe9-901a-4676289f0dcb | -7.5704 | -57.6766 | 2026-09-21 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 700e15ff-42d4-3fcd-af17-c3c0615d2be0 | -11.3422 | -51.3394 | 2026-09-21 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 2ba8e464-2d1e-3c53-abb7-0029b2b54b91 | -10.0714 | -50.2387 | 2026-09-21 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d08c3181-a05d-39bf-854c-ba4bac1d6f68 | -3.0534 | -61.2767 | 2026-09-21 02:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 272b01e2-af5a-3e8b-aff8-33ae278023d4 | -7.5888 | -57.6953 | 2026-09-21 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 581e40a0-2d5b-3e51-9ef6-c5414af1aeb1 | -10.09 | -50.2581 | 2026-09-21 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 5c61dd9f-9a5e-3ff7-9f95-1271c64cb570 | -6.1855 | -47.3284 | 2026-09-21 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b6e7ed72-dd4f-35d8-93ce-57bfb0b2f5f6 | -6.7464 | -59.4223 | 2026-09-21 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 7e02209d-7096-3910-849d-a03a67ee0f7f | -7.5703 | -57.6962 | 2026-09-21 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 42f2dd59-90a2-32f2-a0d9-c4e81b369098 | -3.424 | -59.2726 | 2026-09-21 02:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e7ad4771-4bf9-3e7c-b584-212e54314a68 | -6.4486 | -59.9717 | 2026-09-21 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 340f9f83-aae7-3e1a-a3e4-489ae4318296 | -11.8014 | -49.8129 | 2026-09-21 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2c450473-e245-3204-9605-3db2844721bb | -6.1857 | -47.3065 | 2026-09-21 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7eddafe3-d192-31a5-a436-037ece83ea41 | -6.2026 | -57.7778 | 2026-09-21 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a1689330-909e-3823-ad90-f22882071e83 | -8.7726 | -44.28 | 2026-09-21 02:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e1f21a54-114f-3d6d-974d-25a3e2eff382 | -3.4241 | -59.2535 | 2026-09-21 02:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| fb9ee951-143a-316b-9764-c225f1ef8649 | -6.4485 | -59.9909 | 2026-09-21 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| b96f7743-b7ad-3fc5-885b-5787b7d23d27 | -3.0717 | -61.2764 | 2026-09-21 02:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 5ef9c32f-8152-35f5-98d6-3ccb5b585529 | -10.0712 | -50.26 | 2026-09-21 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 3b00a5d7-b3d8-3c09-9dea-4813b6862917 | -7.5889 | -57.6757 | 2026-09-21 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 479e933c-f8d0-3628-81b4-637ab97d189b | -10.7448 | -50.7238 | 2026-09-21 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d79af3cf-6056-38d7-bec7-37b2e55fc6aa | -10.7259 | -50.7257 | 2026-09-21 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 11f11514-f0f4-39ca-af0c-bf796d345141 | -10.0712 | -50.26 | 2026-09-21 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 21e0cf17-143c-3ecf-be86-4238167ad132 | -6.4486 | -59.9717 | 2026-09-21 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9151460a-0e94-3e6a-aed7-cd5b259c4cd0 | -7.5703 | -57.6962 | 2026-09-21 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7e3ac9d3-3a9d-3cc2-b2b1-3f9b982836e1 | -7.5888 | -57.6953 | 2026-09-21 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| bb66bd0c-ecc3-336b-8135-67276243b7cb | -7.5704 | -57.6766 | 2026-09-21 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 28fc5aee-148f-3f73-ae3f-443d886669a1 | -3.424 | -59.2726 | 2026-09-21 02:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1b614595-0c4d-3be2-a206-252c565eded3 | -10.0714 | -50.2387 | 2026-09-21 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a8db0503-d6a2-3354-a0f6-8af4ee150c77 | -15.0738 | -49.5813 | 2026-09-21 02:30:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f33795e1-e8d1-3892-bd26-581cc0373598 | -10.7451 | -50.7025 | 2026-09-21 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 105e8875-724f-3e9d-b3e6-f6a6ed7f5f92 | -3.4241 | -59.2535 | 2026-09-21 02:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |


[Clique aqui para ver as próximas entradas](README17.md)
