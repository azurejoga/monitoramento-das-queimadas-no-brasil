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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98e76dce-d7ea-35ad-84b7-498354236d3a | -5.68012 | -43.68102 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9726751-2718-3e2e-91a3-4057f0a1c9f4 | -7.10277 | -44.38024 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bd05d50-38b6-38ef-8576-d182b5c9dd30 | -6.37618 | -53.33026 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c221614e-a4e9-31c3-8584-59c575741bd4 | -2.4464 | -47.3299 | 2025-07-30 04:49:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a6ef9cb-1613-351d-9b6a-86b44b97bd67 | -6.39442 | -53.36525 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec13e6b4-125e-37f3-ba42-b0b7d3462d39 | -3.58837 | -52.54467 | 2025-07-30 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 697a2e78-8b99-3b14-8ca0-b9c3f0db363b | -6.41926 | -53.31571 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dacb103-89ef-3f9b-9bcd-4e987a1523fb | -6.45674 | -53.35733 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6075d385-36a4-30fb-829d-10232c6fa03e | -3.58532 | -47.51609 | 2025-07-30 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2603964e-449e-308b-b99e-472dbfcb8083 | -5.98668 | -45.51915 | 2025-07-30 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c923206-1cbd-37c6-b696-6d5f3bb64029 | -6.70128 | -42.04868 | 2025-07-30 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5cb94a5e-33c8-37ab-9f48-93ed5b238077 | -2.90511 | -48.25226 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| c3050c1b-10c7-3b79-b847-bc716b6f1c37 | -6.03459 | -47.54953 | 2025-07-30 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 717506ea-1e3e-3ee7-ad03-7443d38ee54a | -4.05493 | -48.83021 | 2025-07-30 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05cf4792-0d35-33f1-aa16-9af4b773d774 | -6.25626 | -46.1198 | 2025-07-30 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77495dbb-2a2d-312b-a62a-81ebd7786216 | -6.71358 | -44.35643 | 2025-07-30 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95ed02ea-f79f-3ca8-9c15-3fe3f9e61147 | -4.58519 | -48.01321 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3982d663-57de-3d3e-a2e2-4329664db544 | -7.21204 | -43.1048 | 2025-07-30 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ef4e14e-ea27-3c69-841e-0260fe9edc85 | -6.03826 | -47.55033 | 2025-07-30 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 003e629b-b437-3764-b7a7-3471bb2a787d | -6.16724 | -44.42122 | 2025-07-30 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56a9c4f4-0ee5-35fc-8464-de795b94d18b | -3.31998 | -48.72003 | 2025-07-30 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fc219cf-7892-3f98-9e16-3e2aeeed8919 | -6.25693 | -46.11507 | 2025-07-30 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2490d88a-6773-3d1a-aab7-1be49ead8b70 | -2.90509 | -52.54651 | 2025-07-30 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe22a5a9-2a59-39d0-8658-83f70add6bc2 | -4.25573 | -48.54849 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26c966b9-a283-3828-887c-c5703c452007 | -7.30939 | -44.6877 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3457a6a3-e189-3d4d-b0d1-43f9b4ffc9e0 | -6.45232 | -53.36375 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc862524-ab90-3f63-a54e-64a2922233c6 | -6.42038 | -53.35153 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2371cb1f-6b91-39fc-b129-47d1d039a582 | -6.38944 | -53.35375 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5729441-5724-31d4-b5fa-aebece1e29e8 | -3.66148 | -51.23803 | 2025-07-30 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 984e8b8a-13eb-364f-a300-431f63101c9b | -2.90882 | -48.25284 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7350759c-e217-37e7-9284-766730f42e9e | -1.50262 | -47.4721 | 2025-07-30 04:49:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc375c6a-ff72-3d79-8e99-17dca3a55b74 | -6.71317 | -44.35922 | 2025-07-30 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28722f74-93c6-31e8-a04e-5aedad20b36d | -6.38668 | -53.32837 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e55b16d8-41ea-3565-a085-1bc05c6ecad7 | -4.59026 | -47.97929 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34f480dd-9762-3f6c-b831-c6000415ca3e | -6.38889 | -53.35723 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 250bc04b-490b-3253-9632-dc98b3d0f89e | -2.91857 | -48.67764 | 2025-07-30 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9260b506-c9fe-3a81-af30-dfe0aaf6bdfd | -2.91016 | -48.24401 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abd14b94-9c0a-34d6-a525-b375a88a3368 | -7.05572 | -44.9611 | 2025-07-30 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6169336e-d9c9-3965-a4a1-e42241744ada | -3.29748 | -49.19167 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55dcb0ee-76b6-3580-8960-e704c29d940e | -3.03662 | -49.42579 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23361aa5-c1ec-3f36-81d6-86fad8c03a69 | -3.04013 | -49.42633 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92e33a32-a7af-3fb4-a372-8bf371a710d9 | -6.88977 | -44.73225 | 2025-07-30 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d18fa07f-dcec-3230-bb7c-a1c6908a9cbb | -5.67443 | -43.68337 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa9117b1-f1f8-3483-8327-6f34031193a2 | -2.90281 | -48.29254 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44952a4c-9d8a-3e52-bbab-be61de30103b | -2.90367 | -48.24943 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 2b069148-022a-3fa8-9c29-9e581260ba75 | -2.90206 | -48.24728 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4a3057e7-b047-34e8-a009-b9fec601bd69 | -4.10053 | -48.20144 | 2025-07-30 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf44389a-554d-395f-9c7d-4bf347e7dcf7 | -5.06236 | -43.72566 | 2025-07-30 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fc21a23-d37e-3d97-8ea1-61631e44b441 | -3.60244 | -51.48524 | 2025-07-30 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 365f6085-e15c-305e-a2a4-6ef106b088bc | -7.14817 | -47.42908 | 2025-07-30 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44ad10ab-8cc6-330c-905f-40ea9c203d0a | -3.18309 | -48.80864 | 2025-07-30 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 070f11fb-106f-364c-b396-5b20282e4b7c | -5.39845 | -43.24732 | 2025-07-30 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f4f713c-782a-39f1-be2d-4bf0ef053c8b | -3.82107 | -41.57168 | 2025-07-30 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0d04c15-fdd2-337b-a588-d40db1bb5943 | -5.40547 | -49.1185 | 2025-07-30 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4ff2b5f-c301-35c2-ae30-3950b7f65982 | -3.58175 | -52.54363 | 2025-07-30 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44eb4946-b7d5-30a7-87d7-d8af59b0ea5f | -4.85965 | -43.23506 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12c716c9-85f0-3aa6-a3d7-01a60533dd0d | -1.94877 | -52.08175 | 2025-07-30 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b044a18-10d0-3b83-8ca5-8bce4bea67fa | -6.41264 | -53.31466 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b43ee2e0-d25f-34f1-9587-0208246dbb52 | -4.25797 | -48.54723 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84232667-6252-322e-afd6-e79191b253fb | -6.44901 | -53.36322 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac913091-1ccb-36ce-9d5b-80b744835e89 | -5.88465 | -50.5938 | 2025-07-30 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6554e97c-888b-386b-bffc-8753b0e8a3a0 | -6.03864 | -47.55014 | 2025-07-30 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab656aa8-20b0-3d32-9098-585a290b93ba | -4.64981 | -43.12819 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d21a0293-c2f6-38bc-956c-31f53eb03000 | -6.89577 | -45.25314 | 2025-07-30 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 937bba25-1b6c-3820-856e-c90b57327a23 | -7.21762 | -43.10563 | 2025-07-30 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 448a27c0-d040-3f79-aa71-8f4606d3ebc5 | -6.37121 | -53.34016 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c75c96d-1df2-3330-adf0-6cb52656ad40 | -4.65615 | -43.12219 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9af10d3c-36f6-31fd-a2e9-334148e0e3a1 | -6.39773 | -53.36577 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd66713e-0973-36b3-9a6d-642f5a2e9a04 | -6.4237 | -53.35206 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12c70307-c50c-31cc-b295-087513f864ac | -6.16771 | -44.41801 | 2025-07-30 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d636a45d-9566-36e9-a21e-8d3f42dc9da4 | -4.64769 | -43.12183 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9ea3762-c2aa-3bfc-87cc-086e3e449db8 | -7.309 | -44.69053 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf113e2d-7a4e-33b2-932a-146107a78a87 | -3.58451 | -52.5476 | 2025-07-30 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1373bb95-79b3-3061-a6f5-7950577d37b3 | -3.8331 | -48.95874 | 2025-07-30 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| a6898601-aacd-356b-a463-2e09a0f02972 | -6.72173 | -47.20662 | 2025-07-30 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 874f66da-b3b3-3a6f-b60f-25439af50ad4 | -2.90214 | -48.29695 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f85d3bb-51b8-300f-b932-090c37e2e5cd | -7.58749 | -44.81872 | 2025-07-30 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3f12423-728c-3604-bac1-eb342e7053a2 | -4.6482 | -43.11843 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b97559e-4a2f-3c01-b6fc-0bcae5bdcbb6 | -4.3786 | -49.03447 | 2025-07-30 04:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df21800d-3368-30bd-bdb7-2aef0c4409ea | -3.94758 | -49.3875 | 2025-07-30 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71c22fbd-0a98-38cb-bcc4-2b214ac105ce | -6.25421 | -46.117 | 2025-07-30 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70956b38-8047-36e5-8f60-c5eb27bbe080 | -3.07984 | -52.92334 | 2025-07-30 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fd26fa9-6618-37c3-b949-ddece9402cd1 | -5.40382 | -43.24824 | 2025-07-30 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccb30b9b-21ba-3f84-8c38-92da623d7392 | -4.302 | -48.09943 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca262225-8a50-3054-8e96-dde4d1307b08 | -4.37498 | -49.03391 | 2025-07-30 04:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a12f7b9b-7796-361b-bb16-d38012bbb80b | -3.29687 | -49.19568 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 016acc98-0e93-329f-919b-3e64a7fad61c | -3.03189 | -49.43305 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2883a93b-4ee7-3e8c-bb2b-33337a6803fe | -6.40713 | -53.37083 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 850262fe-d4c8-3361-b03e-60ee45eb636b | -7.36611 | -44.72182 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e90f859e-9a94-32c6-8e47-e40b8e80751d | -6.45288 | -53.36027 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54aa4f7-7a10-399a-be40-e30c297869be | -7.36651 | -44.71893 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5995e246-b37e-36f4-933a-0071877f721b | -6.40788 | -47.66663 | 2025-07-30 04:49:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6ae7d91-5d2e-378b-957d-ea1822669a5d | -6.40381 | -53.37031 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66380c5f-0a0c-3884-816d-6974867b6dff | -10.6172 | -45.2282 | 2025-07-30 04:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 9a1a7630-bb9b-3c95-b99c-6ee32807da5d | -8.5211 | -43.3063 | 2025-07-30 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e86bf061-db01-337e-83a2-15956a9287cd | -6.49445 | -56.20545 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f9f326-f031-3d89-b7f4-fb26bf4626af | -6.56965 | -56.18149 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 490d5287-f4c5-3e77-844b-aba46eb13acb | -14.91431 | -45.1447 | 2025-07-30 04:51:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 019df33b-c501-3c4c-9ee4-38e8fccbdb03 | -6.53014 | -56.19371 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dd84830f-5709-35aa-b317-b264c45bcf3c | -10.52604 | -53.62096 | 2025-07-30 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
