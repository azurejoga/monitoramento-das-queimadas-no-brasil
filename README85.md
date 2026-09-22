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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e8b8736-3869-3b92-8a71-1efae492144a | -6.67107 | -47.37325 | 2026-09-22 05:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3535ba3c-a004-3e06-9e2d-e09e1d9bc342 | -3.65445 | -58.86768 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0808088e-faa5-38af-9f85-1961be5a3661 | -6.78269 | -48.66886 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d080e3c-25e4-3092-98e3-2c51f792e353 | -5.87905 | -52.04831 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74dd47e2-a71b-34b0-ad78-3d9ad87e02f9 | -1.33364 | -54.66154 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b8718bd-c349-3b15-b361-060099a26076 | -2.54776 | -58.01468 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e395fbbe-f364-37c2-b498-81d0a25d0272 | -12.92737 | -51.01731 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2276b247-5842-3c1c-88db-760c4584b58a | -2.28341 | -58.09642 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 375674fa-eadb-31f6-8f25-bbaad684487c | -12.35451 | -50.22659 | 2026-09-22 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a89f5c6-8099-34ff-9960-fe8a06dfc002 | -7.57592 | -57.67783 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05478420-0f51-3682-8029-d187f5454cf9 | -3.90229 | -55.88533 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f5f88a1-e9b0-396f-b7e1-d86fecbcacc3 | -6.34586 | -59.96053 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8864cca-30c0-31da-9d26-011af65033fa | -5.8483 | -53.54199 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa9d9715-6a4c-367e-806f-d26205dba78f | -3.34354 | -59.87255 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 464ac5e8-a0c2-302b-819e-9adf6d6e4a56 | -4.34121 | -55.64856 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 214f5fb4-3246-3344-804b-599a8d77ad6d | -4.18484 | -49.40995 | 2026-09-22 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee6d6ceb-adbf-3246-b891-573f0500ea61 | -8.18471 | -54.78165 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80948a8c-fa81-3a5b-9739-f5c91f2e50e0 | -3.3998 | -59.52741 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ff9aada-2d18-3e3c-ab00-88b44a64271b | -6.13975 | -59.94115 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6bc74d0-6308-3e6a-8cdb-31452b5aa9e5 | -6.75453 | -59.06828 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c318450-674b-3f07-bdab-399036441bc3 | -6.40932 | -51.2432 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81c98974-fa16-3ebf-a36c-962f2b941b2a | -6.16095 | -59.94473 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cc2aa9b-64bc-3183-85bc-8f7979ff9725 | -6.00944 | -47.89942 | 2026-09-22 05:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43491b4a-4648-3361-896a-c50b8b6a0134 | -9.61992 | -43.94652 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f3807563-4426-3682-a894-5a5227ccc019 | -3.20626 | -53.95068 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e39e9652-b8cf-3715-aa62-4323a3198bdb | -6.70558 | -59.00403 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc42ef17-6684-3ef1-91d9-d1bcbb1cadd1 | -10.54192 | -57.4396 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fcb87ee-cae2-3299-9fac-e93be4ada8c9 | -3.39529 | -50.43955 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b70eb9c-6d97-3b96-9b4a-3a2963a7a580 | -11.03376 | -54.14798 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b1e751b-8036-3041-bbed-b4f8249d53e1 | -7.40433 | -55.2222 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b1790e-402e-3ea4-87b6-b8dc1669b7ab | -6.66675 | -50.94401 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2635fa88-9d01-37b4-885f-16fb4272c308 | -6.73312 | -55.09168 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc808c2e-3c28-31c8-bf43-4d540f18b8bd | -3.75122 | -58.32896 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68aacd5b-c956-3561-893a-8968568f3ad7 | -7.54436 | -47.327 | 2026-09-22 05:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c66d4f7-1895-3412-97e7-500c5e8a48cb | -6.74771 | -59.06718 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db420b69-c953-3e19-912f-bb028302082c | -5.21138 | -56.10266 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50823d31-2682-3c1e-9f2b-5680f34f0de6 | -3.0451 | -61.25705 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94d75288-237d-38e1-a741-119795ffe3c2 | -3.1709 | -51.36111 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f4ee85e-0d67-3367-afc7-60b11bf82b31 | -6.61986 | -59.91894 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 5b2d8ecf-d2a9-3760-a1d1-5f41ba511cd9 | -9.1313 | -67.94783 | 2026-09-22 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 353194f6-bb7d-3e0d-9ede-c4c2ada4746f | -5.80516 | -57.73447 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc0c0091-8657-3940-9972-575f894fe210 | -3.71411 | -60.55792 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74b4fb37-dbb7-3a76-808d-69336eb6b93f | -7.40024 | -55.22545 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 680907de-e8fc-3ee3-bec2-25c24b9cbbe4 | -4.41664 | -55.49867 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c84f8770-0c91-3cd2-bbb9-33a6459fa11a | -3.03569 | -51.33338 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65022c2b-83c5-3ed3-9ce9-46a8fb9891ee | -6.71298 | -59.00148 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61d72b7b-61d4-367e-afd9-1d39736937b4 | -3.19447 | -61.12474 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2dcba22-0b11-3888-a241-d23c50a5b651 | -6.8432 | -59.0186 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4675938-6ea5-3500-b394-516046e759f0 | -6.98191 | -59.78038 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d43b491-5cf6-3a10-b7e5-3574a7ffe084 | -3.45437 | -50.61008 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdd46b72-95f7-346b-9337-56565cdfbbcb | -6.10387 | -57.68227 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 74d630f2-170a-3db7-81ef-7e62dcb0339f | -6.15978 | -57.71252 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0586d7b8-1b28-3ae6-a0c1-6c7446449169 | -3.45001 | -50.60946 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d07300e-420e-3c6f-a055-042f9b477d4a | -11.70833 | -50.98943 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| a08af0af-4722-32de-bcef-5aae16e72a70 | -3.01335 | -54.17127 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82155b41-31b4-3fe2-8129-44711fad6f6a | -7.24969 | -55.58076 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad5f40df-1ef1-3039-88e5-948ad8db7482 | -6.07279 | -57.72729 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d57823bd-9a92-369b-96bc-78f7136a7a86 | -3.6701 | -57.09358 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d6d125-7203-3b83-8e36-79f4b3f8223b | -10.9569 | -54.36781 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19adbe6a-7585-39ce-94cb-f70e39b294f5 | -6.19584 | -57.78611 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4595e50e-5277-33a3-bad8-35b169afdec3 | -3.48314 | -59.56866 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a0f2965-073e-33ab-ae8d-1d1f8a533627 | -3.62383 | -54.5287 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd4fb859-7117-3ff8-b52a-ae437ab34d46 | -10.9087 | -53.9615 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7dabd2d3-8443-3c33-97de-14357b2589a1 | -6.12297 | -59.9547 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5242a92-6a19-3f1b-b4b7-c34b05a2d70c | -7.2451 | -55.61092 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c504f6f-9492-3773-8311-57728a58aaca | -15.35583 | -48.10841 | 2026-09-22 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b83171b2-f9ae-3dce-bb2c-909fa99674e5 | -5.83471 | -52.12262 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 891bc2e7-80b9-303b-96f1-8a5614f20579 | -7.90324 | -49.01152 | 2026-09-22 05:23:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dcd5160-c74e-356d-81ba-27fe432ae669 | -5.13168 | -60.28074 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e06182f-519b-30b8-8a52-aab2caea7bd3 | -2.73935 | -51.36726 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2de28dba-9437-36a8-abb6-fdd5a55ee9c4 | -4.63624 | -55.77 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d747cd90-6732-3714-bb31-e4784e086741 | -2.96166 | -57.71974 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b041be4-e8f2-33e8-aa0a-8ba578dd704a | -3.07384 | -61.17951 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aee1604a-aee4-36eb-9642-68c0dc8840f5 | -5.6692 | -60.23364 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48893c46-b285-38ad-acb5-604d30fc3b53 | -5.83893 | -53.47636 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b02f361-be90-3969-a9a0-92c168967e9c | -7.57979 | -57.67488 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9134b73-9ae8-308d-a888-bc6f61310030 | -6.77285 | -55.46782 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12c89fb5-52bd-3849-9a95-d57490c5a4bc | -9.76316 | -65.05664 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ad1c3d8-b569-3728-98d4-d4d0be6f9710 | -6.97816 | -47.49677 | 2026-09-22 05:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a695283-0d5a-3719-afab-7c41fee9c897 | -4.10404 | -55.5092 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a68aadc-b2c0-3683-ae3a-7bfd219458bf | -5.78541 | -43.7676 | 2026-09-22 05:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b680b172-75a6-362d-b2e4-036cf7e0a521 | -6.80048 | -59.43259 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 290d1c4a-5d8c-3309-a57b-254469adcf22 | -5.75793 | -45.07772 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c96ca786-97c2-3526-af2f-a95538e4fc85 | -7.57535 | -57.6599 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6a1471-04d5-3881-9197-16e74b3d6e33 | -5.86473 | -52.03175 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8734ef0f-5b6f-3751-b152-a7c5c9af05a8 | -6.35521 | -55.75299 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09362398-7bcd-305b-893c-db571db41b33 | -13.86867 | -48.57482 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cadf615f-47c5-3839-bcdf-b3159301b706 | -3.48924 | -59.59875 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24172b1b-32ae-32b4-a0fc-923a6081a5b3 | -6.15603 | -57.69771 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 546a6940-c38f-30d8-9447-22fc270c0504 | -4.53153 | -54.96917 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bc9d7ae-7c13-3c1b-b22d-7510365ba548 | -4.14021 | -51.10304 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59129805-02ed-356c-adfb-a4f952166013 | -5.98012 | -57.7805 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d3ca2d9-36b0-3e79-97f2-bf3537f940e8 | -3.44005 | -50.61631 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 118acb06-57ae-3c12-8e61-bc945b1ac8f7 | -6.69229 | -60.00701 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9912cd-192c-3fcd-a62b-f69fa5a94389 | -6.30886 | -59.94764 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab24174b-1962-304c-9876-85c8bf814e70 | -4.28355 | -48.62446 | 2026-09-22 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 065d22d9-7701-399c-9b4e-088cd0a46b17 | -3.05175 | -54.41178 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb77ba0-3711-381d-97e3-fe7679a3df27 | -3.14285 | -61.39436 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9281194-8a49-35d6-832b-d14eb79d6d99 | -14.58721 | -52.17449 | 2026-09-22 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa999b2-6abf-3bf9-9ee2-ec72b32399c2 | -4.07813 | -55.32052 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README86.md)
