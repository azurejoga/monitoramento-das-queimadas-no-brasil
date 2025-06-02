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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c7cf603-07a9-3074-af49-f084a4034ff7 | -9.33993 | -47.08318 | 2025-06-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0188a4f2-2314-314e-be73-2c2720b242dc | -11.14503 | -53.94318 | 2025-06-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5cfcfad-6a6e-3546-b4a4-927bad86745e | -11.29854 | -46.45911 | 2025-06-02 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 908d7312-f5ec-37a8-b5ae-ef7de279e682 | -13.10363 | -45.2661 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf30c8bc-5fb3-3a20-8135-342550a43370 | -9.52522 | -46.76668 | 2025-06-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 796ae71b-18e0-3e0e-8104-5376d5f99999 | -8.77462 | -47.24008 | 2025-06-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f73fc35-5632-36ab-811a-d333246beab0 | -9.11906 | -47.64301 | 2025-06-02 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87c0f059-688e-350c-b07c-d60c0204979b | -9.37602 | -48.41791 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa0bf36d-a10d-3f3a-be4c-ef1f6ff142a5 | -7.95514 | -45.41714 | 2025-06-02 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d25e2e66-a463-396f-a89b-4380561b03b5 | -5.92409 | -45.5294 | 2025-06-02 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95dc93dd-a267-388e-a7ff-1089a3234dcc | -11.44359 | -55.00939 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c480ce03-717b-36d1-a380-6a6ab02b56ff | -7.08063 | -46.55898 | 2025-06-02 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b69569b-4855-3976-8002-47d568aba521 | -13.0827 | -45.26315 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ddc7811-9f35-3820-8bef-568a52394afd | -9.3947 | -48.40949 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 044fd059-113b-3826-91ca-fef7abd461f2 | -11.44745 | -55.01006 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a64e065-6852-3e28-916c-edd6f2994f52 | -7.0058 | -44.6036 | 2025-06-02 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 542280f6-cd84-3677-979a-0f369b5c5589 | -9.52586 | -46.76239 | 2025-06-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dcc5f64-c593-3bc8-85e4-ff2768250684 | -7.01134 | -44.5938 | 2025-06-02 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc1ebf06-e566-38a1-828e-c4fa06705338 | -9.37941 | -48.41844 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23afc6a1-e1d8-3bdc-a07a-702cdb881353 | -13.09107 | -45.26434 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f246ab0-8f88-35a5-adf8-11178927ed2d | -13.10476 | -45.26581 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c95c5adf-f289-3c65-98e2-786d34b01984 | -9.40123 | -48.44058 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5a92ce8-00dd-3b93-8db3-bdd63d9865fb | -13.08216 | -45.26707 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdf179e4-dc1b-3125-a2a0-c68d787a9076 | -5.9234 | -45.53393 | 2025-06-02 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a660bc04-f58e-345a-aa2b-9cac8c35a738 | -7.08482 | -46.55544 | 2025-06-02 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e92ac86-7dcd-3d98-82fa-d51f261ae9c9 | -6.72873 | -44.36773 | 2025-06-02 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd65c2ed-cc0c-365e-88cc-e6ac18da66c1 | -10.81172 | -56.93845 | 2025-06-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f118a93d-5966-367b-a36d-20873fc5a103 | -8.77875 | -47.23667 | 2025-06-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f44f4493-0843-394a-aca2-153977c91069 | -11.19519 | -55.02666 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3efb6ef3-d17e-34c8-aba4-59c667e7b10c | -10.46512 | -47.94549 | 2025-06-02 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d10efe70-d6ca-3a31-b612-668f57daa122 | -9.40261 | -48.42583 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3577bb29-6618-312d-ab16-9d64febd1abc | -11.44443 | -55.00451 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bff2eff-3bb3-30b1-b51f-a55895f06bdc | -5.92104 | -45.52435 | 2025-06-02 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e8f382b-9662-31a9-9cd6-d1543842f435 | -9.39413 | -48.43579 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 158a4e9b-ec40-383c-a817-8cd8096f085b | -10.81932 | -56.94316 | 2025-06-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cefe4e5a-9e30-3ead-8a78-ed892247161b | -13.09526 | -45.26493 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08b8ec18-dcfd-3338-a866-a49162b9b23a | -7.88392 | -46.22966 | 2025-06-02 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93ff3600-c8f1-39c3-88b5-67e2737de910 | -10.67988 | -47.19424 | 2025-06-02 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be34de03-61ef-37c6-8d6a-4817e90f681c | -9.32742 | -48.94824 | 2025-06-02 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bd1c347-2151-3678-982e-c8cce759908b | -9.39922 | -48.4253 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ccf892c-5dba-3c98-9fb8-7f14a91d60f8 | -6.7341 | -42.89527 | 2025-06-02 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 42a48910-2ba6-315f-b1d8-062e434258a4 | -11.44057 | -55.00383 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f82717d-b588-365f-b71e-fb6ac1ceb005 | -13.08634 | -45.26766 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b970f664-3ded-366d-b3a1-b3597a98a939 | -13.10057 | -45.26524 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd6cf911-b38a-3990-b565-aafc6f2ce552 | -9.40179 | -48.4369 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a93646cd-e7c0-39e4-8247-22c43120d0fa | -9.11499 | -47.64638 | 2025-06-02 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33c50d47-fcec-33fc-823b-5b09c656b092 | -5.4172 | -47.5689 | 2025-06-02 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df580947-d993-3943-b7cc-be188d8061cc | -9.40035 | -48.44052 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d70d79a-ac42-365a-b5b7-02b55a08eb4e | -8.33026 | -47.09515 | 2025-06-02 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbb0f20e-51bc-37c8-9cc9-8ce01395c370 | -10.4686 | -47.94604 | 2025-06-02 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8cfff72-fe2a-394c-a986-31d11c13b3fa | -9.37658 | -48.41423 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 572a05ec-074b-3521-87e7-fd7e23eb2d57 | -11.44829 | -55.00518 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ba29693-1dde-30b8-a916-2f9fe1e5fd7c | -9.39979 | -48.42163 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f75aecfc-ead5-3c9f-9c61-732652a23c1b | -9.11557 | -47.64248 | 2025-06-02 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aec492c8-e9d1-3a9a-90a2-5ccbe6debf99 | -7.88458 | -46.22533 | 2025-06-02 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f8833eb-af9a-3f4a-b818-166e85ca148a | -7.08256 | -46.55601 | 2025-06-02 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b171119e-df97-3bc6-9578-1e5d40c4fb77 | -13.10783 | -45.26664 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0911bd08-6e52-379c-ad52-a7a0485e0735 | -11.14577 | -53.93885 | 2025-06-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25d3fe29-a375-327f-be7e-6e2a876c0264 | -11.45215 | -55.00586 | 2025-06-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e3e6ca2-a2d5-3ace-863a-6dc148b818b9 | -8.33086 | -47.09109 | 2025-06-02 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdd498ae-a017-38a3-8712-6b3672b96191 | -9.06849 | -47.15716 | 2025-06-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5906454c-1ee0-37cf-b479-65210545b343 | -9.40375 | -48.41846 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3948a294-7e8c-3130-b633-2a23a498ad7b | -9.52158 | -46.76611 | 2025-06-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b14f7fb2-006e-3cec-a3e7-ab46f7535711 | -9.39582 | -48.42477 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af3adb4d-a7a2-3e61-bfa5-17dd2b97a76e | -9.40318 | -48.42215 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0c6db0d-8a08-31f8-9c4b-ace9df4a4e69 | -9.39996 | -48.945 | 2025-06-02 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cd631da-4179-3c3d-a1ed-59a48f9534a7 | -6.73665 | -42.90908 | 2025-06-02 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e06f77e6-7be2-3dc5-aa2f-74f7bc834043 | -9.11847 | -47.64691 | 2025-06-02 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea94656-eefb-35c4-8ee2-d0e7f4ea48f0 | -7.08288 | -46.03767 | 2025-06-02 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86aef324-f88a-366a-88fc-4afe9fc41bf8 | -10.82417 | -56.94541 | 2025-06-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5dbcc10-134e-3cd9-9a70-e33aa15c8a85 | -8.77522 | -47.23611 | 2025-06-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bee2649-984b-3ab4-a410-45116e208172 | -10.98196 | -44.62597 | 2025-06-02 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e4fa72c-c4cb-3e27-87b4-683a261effa2 | -13.09053 | -45.26825 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39a14d5f-1895-3c18-b1a3-9af5a1a8533e | -7.00927 | -44.60785 | 2025-06-02 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9772b87-cbee-308a-95e7-5037cf57b7b2 | -10.81975 | -56.94461 | 2025-06-02 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eb8a331a-e958-37b2-a9aa-9c6d06ff0dca | -8.32613 | -47.09854 | 2025-06-02 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23b416b2-0690-39ed-a3f7-a014ca32712f | -9.40401 | -48.42219 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b597753-22f8-3f93-9bab-5c3f447f0294 | -7.8809 | -46.22478 | 2025-06-02 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c37aa00-764d-3019-aafe-c4d27f791c47 | -13.09944 | -45.26552 | 2025-06-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2f98e3e-95d4-3e79-9cf4-c1d7f20adbad | -9.40345 | -48.42588 | 2025-06-02 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33e3b4a5-c121-3b27-a6ac-70b37c6bcc6b | -9.56747 | -40.77494 | 2025-06-02 04:38:00 | NOAA-20 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b462b727-df15-31d4-ade3-af5f28255738 | -6.72925 | -44.36424 | 2025-06-02 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72095200-ecca-32e5-b8b4-e1b28fa3f62a | -6.73217 | -42.90848 | 2025-06-02 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83a17874-5d3f-3ee1-acf2-2aeab111f7ea | -8.12837 | -49.58725 | 2025-06-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79a63853-1d3d-3a4c-ae56-2f1e294d9616 | -5.18639 | -48.07918 | 2025-06-02 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a2dea50-501b-3e4a-8fe7-3b97cddd7651 | -7.01188 | -44.59018 | 2025-06-02 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a178f845-d149-3fbc-8435-bea469f90978 | -7.00978 | -44.60439 | 2025-06-02 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9e4efa7-6149-3d75-aa1f-0bdc415e08e8 | -18.2234 | -49.21526 | 2025-06-02 04:40:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b371c59d-249b-3339-a16f-f9da635e5579 | -14.03391 | -55.12818 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fda0869-f57d-348e-a18f-6091bd70c766 | -17.28391 | -42.65583 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc6af2ea-b5e6-3bdf-8216-e1e4296f82de | -17.62131 | -50.91484 | 2025-06-02 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 743a302d-d9c4-370a-b065-97b8892ad671 | -17.28354 | -42.65312 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0996acdf-ce62-3777-9673-c9939e1a8993 | -17.28998 | -42.64964 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db316638-7b79-3f38-a9b4-07c0ce8e15d4 | -19.28891 | -55.15548 | 2025-06-02 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07f6dae5-fd69-3da8-936c-d6db047a7fb2 | -11.90946 | -54.82986 | 2025-06-02 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 953e0e23-cf47-363e-8aa4-f1ea05a64dc5 | -14.02563 | -55.13141 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1fd9af0-0cf0-3735-b687-47e3d446e447 | -17.29123 | -42.63885 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 779a6930-8c91-35bb-b50d-742bcb54c491 | -14.01894 | -55.12548 | 2025-06-02 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7ae8044c-3dba-3178-835d-a43489de1417 | -17.29484 | -42.64775 | 2025-06-02 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aa54c84-8404-38ab-9adb-cd4d601f4a01 | -12.66111 | -58.21748 | 2025-06-02 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README7.md)
