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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 224c19d4-c65f-3a0e-84fd-b1ccc3513269 | -10.5232 | -37.0121 | 2024-12-24 00:04:00 | METOP-B | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 506a2859-eabe-348c-8346-204aa8d58a27 | -10.7202 | -37.230499 | 2024-12-24 00:04:00 | METOP-B | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbcba1af-e1b9-3ddb-a306-510ae7ed4493 | -2.3494 | -45.5825 | 2024-12-24 00:04:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 601d8f04-ffb2-3c92-87b8-e08e4b6e8449 | -6.1948 | -42.6213 | 2024-12-24 00:04:00 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 198403f6-cbf4-30e3-97fe-ede7ed702b28 | -1.4615 | -45.800701 | 2024-12-24 00:04:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95714aa3-4eb3-3b26-89c5-76d7f1254eb8 | -7.2368 | -37.4151 | 2024-12-24 00:04:00 | METOP-B | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 67f74718-a565-3bd9-a173-4bcae68142cc | -10.614 | -37.0462 | 2024-12-24 00:04:00 | METOP-B | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95df8e29-e01f-3dad-8348-54ce53b89ff8 | -6.6881 | -39.1105 | 2024-12-24 00:04:00 | METOP-B | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 051bd05a-e33a-343c-824f-a0b9bedf8da5 | -9.0224 | -39.924702 | 2024-12-24 00:04:00 | METOP-B | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f8a22e71-8d2c-3ddd-a7b5-7e7c5232a84b | -2.9933 | -40.374298 | 2024-12-24 00:04:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 77c0b956-f482-365c-b49a-0be8743e86e9 | -3.1358 | -45.417099 | 2024-12-24 00:04:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb01925e-e5bc-3884-98e5-e4ebd26cde4a | -3.1374 | -45.424301 | 2024-12-24 00:04:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ae2fd46-4d97-30ee-886d-e1666b43adf8 | -2.9992 | -39.996101 | 2024-12-24 00:04:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ecf2fc0a-486a-329d-811d-cd31868c9533 | -4.5098 | -42.052399 | 2024-12-24 00:04:00 | METOP-B | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44b4c573-0b29-3283-807d-a367d97629bf | -2.7561 | -45.698002 | 2024-12-24 00:04:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 275efecf-33d0-3fab-8edd-f73ff7ae1e82 | -2.1042 | -47.105999 | 2024-12-24 00:04:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f62ae12f-d268-3556-ae3f-91857990121a | -2.6474 | -46.085999 | 2024-12-24 00:04:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6d1ebc-fe12-33eb-831b-075f9d19f2e6 | -3.9065 | -46.1049 | 2024-12-24 00:04:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f361cc74-8758-3051-8db0-be244befe5f4 | -2.7735 | -45.0868 | 2024-12-24 00:04:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf3951c3-59e5-3ed1-996a-d0b51ee6be6c | -8.9892 | -36.046001 | 2024-12-24 00:04:00 | METOP-B | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b00a990-41b1-30c6-9f76-b310ba752be5 | -2.8306 | -40.293499 | 2024-12-24 00:04:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1e964688-e1a4-3c7e-8d72-399bb3fa5900 | -2.2152 | -45.993801 | 2024-12-24 00:04:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c63e1565-8b53-3374-ac25-432c2cd5e489 | -2.8665 | -46.743999 | 2024-12-24 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7de547a5-0f35-3b95-842d-213950b21e2b | -2.3462 | -45.568199 | 2024-12-24 00:04:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66742586-bf8d-3959-8b10-1ccd506cd6b5 | -23.23168 | -49.61263 | 2024-12-24 01:00:00 | TERRA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 405e7f66-ae93-3dbd-b101-69d535a54c7c | -23.23037 | -49.60237 | 2024-12-24 01:00:00 | TERRA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 16dfe003-21bd-3242-ae52-535d5f1e4ac6 | -1.5865 | -53.336498 | 2024-12-24 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00ca5911-62d9-3e03-b688-fbf0d8be6664 | -6.2325 | -55.623001 | 2024-12-24 01:01:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f9b18c-10d0-31a5-ae32-97c7b5a02b12 | -3.1319 | -52.1236 | 2024-12-24 01:01:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35e099ec-b95f-3689-a175-4ce00ac98ca0 | -3.1032 | -54.550598 | 2024-12-24 01:01:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae25056e-15d6-3fab-928d-9c7eee2449f0 | -3.0614 | -53.784302 | 2024-12-24 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab5876d-0a95-301e-969e-02637c18ecad | -3.0329 | -53.884602 | 2024-12-24 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00bf70cf-2e84-378c-ab82-b96fd7ec54ce | -2.3621 | -54.601601 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a333921c-ec4e-3b0e-a6d9-0c2859cdd8f1 | -2.375 | -54.612999 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 708995a2-4b80-3d0a-9393-ddd40b14ba6a | -6.98 | -43.541901 | 2024-12-24 01:01:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 529745ef-2cc8-34b8-a778-9d28ed7d3606 | -2.35 | -45.575001 | 2024-12-24 01:01:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf2b8004-2479-3ef5-b256-9b55bbc8f565 | -1.5232 | -54.946098 | 2024-12-24 01:01:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ceb47f-feb3-30a8-b839-a0f16225d4cb | -1.7156 | -54.481201 | 2024-12-24 01:01:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a1c0fb-ad67-3b1a-80ac-60a8431d9f4d | -9.9252 | -59.8964 | 2024-12-24 01:01:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b0a62c8-059d-3679-975d-598ad4752c82 | -2.4165 | -54.209801 | 2024-12-24 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27242ef2-8356-3a86-a5e9-5e915b1ebb30 | -3.8157 | -51.0289 | 2024-12-24 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a938055-398a-33cb-804e-5ff7f2993e56 | -2.3864 | -54.617599 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf3d0532-7f3c-3ff6-b748-0ac0aeaf6868 | -3.0714 | -54.636398 | 2024-12-24 01:01:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b192dbd-35c4-36e6-8291-c03db699e57f | -2.7797 | -45.1073 | 2024-12-24 01:01:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c627f652-1748-3d05-b8f6-29d316a06419 | -2.3548 | -45.594799 | 2024-12-24 01:01:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 224b8418-b009-3a7e-bc65-9ebb34bd36ee | -3.0361 | -53.8983 | 2024-12-24 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eae52d98-85bb-380b-8f23-5f2585811dfa | -1.7116 | -54.014301 | 2024-12-24 01:01:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed9c9104-4773-3e6a-9612-7988aea7941c | -1.5849 | -53.329399 | 2024-12-24 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55da31ce-a3d8-3423-8bb2-0008ac3e3896 | -3.1028 | -54.593601 | 2024-12-24 01:01:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40536cc-57e7-34d8-aff7-8b976b041513 | -3.4234 | -52.8484 | 2024-12-24 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0f5ba75-b004-3211-a59d-90430b09e5b4 | -2.9852 | -54.125599 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58c05a4c-8035-31f3-8de5-bd6a762a47f3 | -3.0646 | -53.7981 | 2024-12-24 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34343b24-1914-3ca9-86f6-e75a5155fc33 | -6.2308 | -55.6157 | 2024-12-24 01:01:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fdd01ce-e33b-3211-8cb7-ff62cbd9d50d | -2.7911 | -53.237499 | 2024-12-24 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e018f1ce-67f4-34c7-ba88-66ebe0b832f2 | -3.1573 | -55.011902 | 2024-12-24 01:01:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a80de31-20de-3316-9d3a-736321b98e43 | -3.0345 | -53.891499 | 2024-12-24 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82030baa-187d-3bca-a956-17c6cb11fee7 | -2.3645 | -45.592499 | 2024-12-24 01:01:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58948c6b-0d21-36c1-aa9b-7a1d1a303908 | -1.3622 | -53.705799 | 2024-12-24 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315e94d3-16cf-3971-a460-edf786be825a | -2.9754 | -54.1278 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d011aaab-403b-3693-8cb1-7c9d450d16a1 | -2.768 | -52.645699 | 2024-12-24 01:01:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b66124-14c4-339b-a723-b4f14a722276 | -3.0729 | -54.6432 | 2024-12-24 01:01:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac11382-7a82-3a5d-8d22-444192d9298a | -3.1016 | -54.543701 | 2024-12-24 01:01:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3fc6a1a-f689-3661-b568-ebab250291ee | -2.77 | -45.1096 | 2024-12-24 01:01:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94ebf8f5-dff7-30f0-8a5c-b3efbadca678 | -2.3636 | -54.608398 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de78576-f72a-3425-9350-87873f8b40f0 | -3.4217 | -52.841301 | 2024-12-24 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64cb5612-24a6-3157-ad0c-dd7434bca33f | -23.2341 | -49.603199 | 2024-12-24 01:01:00 | METOP-C | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a8ce560-b7f0-3e9b-ac89-29f738eaec62 | -2.3597 | -45.572701 | 2024-12-24 01:01:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24255d34-855c-3cd3-95c7-8bc04a415003 | -6.9703 | -43.5443 | 2024-12-24 01:01:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ccbf001-d8a8-314e-b3b0-5d6b7de4c4b3 | -3.063 | -53.791199 | 2024-12-24 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1187fc-0c47-3a68-a2c6-5f074a52ebf2 | -2.3652 | -54.6152 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a25c930a-be9d-3364-acf6-f3bb6ea7b3ed | -1.7172 | -54.487999 | 2024-12-24 01:01:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83fdf08-6f5c-302e-89a6-aa8778591709 | -2.3765 | -54.619801 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5794c8ed-0d20-32c8-b472-5483c44fa9b5 | -2.7649 | -45.088501 | 2024-12-24 01:01:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90945364-a2d2-3f6d-8e97-6db702d58dd6 | -2.7746 | -45.086201 | 2024-12-24 01:01:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0b40b0a-2010-3344-b0be-b9c035345392 | -3.0901 | -52.0769 | 2024-12-24 01:01:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f1b3d0-6775-3417-b7ab-45cf48438e7a | -2.7895 | -53.230499 | 2024-12-24 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a25db4-4d47-37c4-9306-637275c10899 | -2.9867 | -54.1325 | 2024-12-24 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0b4836-ca62-33f0-a6e4-61271f64f436 | -1.5247 | -54.9529 | 2024-12-24 01:01:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27eb2139-10a7-34da-9255-03163651933f | -12.70865 | -40.2051 | 2024-12-24 01:02:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 29fbc9b2-8933-3be2-b019-a393d7360ec8 | -6.98815 | -43.2694 | 2024-12-24 01:04:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| f9165c49-0869-3948-8968-adddca418757 | -9.22789 | -60.33733 | 2024-12-24 01:04:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 516150d1-fa53-3de7-afc3-9651c88388fc | -6.97196 | -43.54814 | 2024-12-24 01:04:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 318d4c68-74f1-3ba6-a4b1-0fa805d772e9 | -3.1338 | -52.12822 | 2024-12-24 01:04:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 856c8997-ea81-3fa6-9511-9db231215cdf | -3.2341 | -51.45257 | 2024-12-24 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d86e3713-4437-3905-b5e2-d87525ca70ec | -2.76566 | -45.11299 | 2024-12-24 01:04:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cceffdc4-4ac8-3a42-a410-e25d66b192ba | -3.98233 | -46.34613 | 2024-12-24 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 349d6e51-3da8-388f-81fb-222c18104c7a | -3.09102 | -52.08031 | 2024-12-24 01:04:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4ac2edb2-1aa7-3268-95ec-1cb601afaa94 | -3.03394 | -50.49274 | 2024-12-24 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ea7e2a14-4bf2-3770-9b40-15205ff05549 | -3.81101 | -51.03809 | 2024-12-24 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bfb1e078-8c84-3063-be3d-b8a2f6fda5e4 | -2.34715 | -45.57368 | 2024-12-24 01:04:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 105734ba-6c99-3931-80a0-b6280603afb8 | -3.15878 | -55.01718 | 2024-12-24 01:04:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 926de6ed-e284-3bf0-af46-8d7596204836 | -3.03786 | -53.8904 | 2024-12-24 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 556d7f88-f0af-362a-bf1d-f5c1479a7d0a | -2.765 | -52.64474 | 2024-12-24 01:04:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dc36a515-7ec1-37d4-973a-8eb111d9fb7c | -6.23283 | -55.61945 | 2024-12-24 01:04:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b72ad5db-7192-3880-ac0a-378f54401413 | -2.76812 | -45.08232 | 2024-12-24 01:04:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 3ead197e-75a9-3c7f-9694-489cb463a97f | -2.86102 | -46.75236 | 2024-12-24 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6aa165c5-67c6-3a13-abbd-7cb0138be9d6 | -2.77165 | -45.10548 | 2024-12-24 01:04:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 3f3109cf-8d84-3e67-b0a4-a1c967881556 | -3.06732 | -54.63789 | 2024-12-24 01:04:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8b880492-6567-3d84-920d-b40afd0750c6 | -3.03915 | -53.89981 | 2024-12-24 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5420d652-100c-3f14-a4db-d605c3dce856 | -5.12885 | -49.40873 | 2024-12-24 01:04:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README3.md)
