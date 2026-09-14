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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c61e339e-10e5-3af3-bd28-2236e54d0bb8 | -11.78393 | -46.39528 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d7f416b1-3318-3344-a7e0-6722b6a94a94 | -6.04439 | -52.2053 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e7fb00e-2056-3cf6-a672-147832e68b28 | -9.44013 | -47.8555 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f37a68-c858-3a3b-8613-1e9cb11d79d2 | -10.69237 | -54.15659 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 325a22e6-3de0-3717-85e4-823a378bfa61 | -6.2768 | -59.93796 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58f47e4e-24e5-34cf-9ad8-a0e70ddcfc63 | -10.54056 | -46.2859 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd01988f-12f8-39df-bbc4-e0b5ba3250a2 | -5.4228 | -51.33015 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d809ced8-5ed3-34f8-bf5e-de8519bc36e3 | -6.43111 | -56.06004 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c433f7a6-9101-37a5-abc3-3b826a7709be | -10.03915 | -52.12327 | 2026-09-14 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93b8ea80-82b4-35a6-8cb4-62e72afd7183 | -10.68272 | -54.15112 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5209fcbc-6c3b-30f6-99aa-41ccaee8a9f4 | -10.67806 | -54.15806 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 86288c73-072d-388b-8ff4-16ea1f628db4 | -10.56688 | -51.33406 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cc28755-4268-368b-9ab0-b90dd4c34276 | -10.58354 | -51.33671 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e870530-dab6-3d4a-b84f-1dcd94b1bd16 | -7.67809 | -55.11733 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c70ce7-c248-309b-9b9e-54fd30086766 | -7.47474 | -49.78382 | 2026-09-14 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd1bfceb-f36d-33e7-96d5-92dbc9551950 | -10.67433 | -54.13813 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e667cde-de80-390c-8b45-e13d1787108c | -11.24705 | -54.15575 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a0b215a-1511-33d4-9875-3cbe14b0172e | -10.47691 | -51.3235 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f270e9-bb0a-3dd8-8dc5-25ee04989c73 | -10.56409 | -51.32998 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56fc414f-e2a0-311d-8f37-816ae79b4ba4 | -3.59408 | -59.07182 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fca759bd-ee93-38af-8a3a-b46390f800cb | -10.80845 | -58.58029 | 2026-09-14 04:53:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5da7e055-41ac-3f96-8a30-5185dd1ecac0 | -8.54087 | -54.71223 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c65249e-22a1-3091-b6f6-22b26dce54fb | -6.29303 | -55.27363 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92163808-64e5-3de4-b6bf-ba4ea700d8f8 | -3.81228 | -58.90266 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e4fd1ae-ced6-36c7-8e29-19a1af680b1b | -10.24323 | -50.90636 | 2026-09-14 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e0d62dd-4886-3cf5-9b63-470c0f8cc541 | -9.40221 | -50.18093 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43d8c977-7a77-3adb-adb6-30ac14aa9cee | -7.09162 | -41.81215 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5b7edbc4-fb30-3772-858b-1e2b0a565496 | -10.37645 | -46.65409 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec96a886-76a9-3d74-8694-f4c94fcd8dbe | -6.1358 | -57.69473 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc9db4d1-8322-3a32-b8bb-4841fdf84058 | -4.38644 | -55.2029 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2cbd4f2-f064-3119-b713-7ba97bcee59b | -10.0386 | -52.12677 | 2026-09-14 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48492a61-aa03-39c9-bf92-9077f0397e33 | -4.97854 | -56.1312 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fda70129-58ad-347c-8c09-5b428eff635b | -11.77907 | -46.39866 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 343f8593-94f8-3957-8e28-023ec542d7ca | -11.22471 | -46.41927 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 503b0449-84db-3303-9320-3f37c67f9243 | -12.15737 | -48.95786 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57ed681d-34b4-31b7-bb56-28929bec96d2 | -10.55133 | -51.3279 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e75234d5-5426-36b9-97a6-2112d3b4310e | -5.42611 | -51.33068 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ebaf0609-26a0-3141-b9ef-aa57d91309f4 | -9.4426 | -50.12274 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 7e57f60a-ab72-370d-ab20-1bd967d83a4d | -7.22772 | -47.55642 | 2026-09-14 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 388f1137-c5dd-31fd-8b49-d8e88ce6d92f | -10.66562 | -54.14821 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 3148d4ef-1667-3c4d-a02e-d15808936cbc | -6.23299 | -51.68332 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c3c80bf-b0af-34a3-ba2e-6f3d7da51825 | -9.71297 | -50.84626 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a569e192-c218-3da2-b856-af35e8e8f684 | -9.69538 | -58.17439 | 2026-09-14 04:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acd19dce-6052-3723-9361-19f0f5f8491e | -10.68584 | -54.17484 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fb973ed-be0a-3131-a54f-711e7e111345 | -6.58304 | -58.87279 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76f9fefb-79e5-3d8e-a4c9-80bcf4e88b86 | -11.25074 | -54.13332 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3800c671-9705-3d2a-aa72-23064f4f0f51 | -8.3905 | -46.2955 | 2026-09-14 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ff540bd-53d8-3ce5-8534-3dcf4121df80 | -8.54359 | -54.69588 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7b643e3-6591-37ba-bc25-dfec790d6a1f | -10.5802 | -51.33622 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 271d896d-492c-3ac7-ba9d-99b8d1b42a6c | -5.12264 | -55.96406 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb77f038-da88-30b2-8a72-081012376f67 | -6.32003 | -59.97301 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 182831fd-2941-32c5-ad2d-5890b6b6e856 | -3.17921 | -61.11659 | 2026-09-14 04:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0977de7-9d26-35bf-b1d0-ccee818a8848 | -9.53601 | -45.43375 | 2026-09-14 04:53:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7eb3623-d513-3fe7-8edd-381b641b9090 | -10.64424 | -50.5737 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c408609-6530-3717-a913-863b789edcab | -9.44391 | -47.85614 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d947e119-40af-3fe4-adf9-ad380b1a1c9f | -7.55795 | -57.67236 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1eacf4b-00ad-3451-8735-7f13a9da846f | -9.57946 | -55.13877 | 2026-09-14 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ece6c99-3126-3e3e-8d5c-2c0c5c3ee37f | -6.32236 | -44.18058 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3faba7d-7b89-396e-b46f-ce3864c8d2d3 | -10.53578 | -51.29631 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7fa2e97-54c2-3626-be5f-3b3648f1a4be | -6.32186 | -59.99283 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90b2dc5e-eb41-3db1-8b5c-76717f85f599 | -9.33142 | -44.3702 | 2026-09-14 04:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d1d87e7d-7840-3675-b65a-4ec85510ad40 | -10.65878 | -54.14704 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 61ddc027-c628-3060-a904-93486875aee8 | -6.58616 | -58.85347 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d8ba7a0-3414-332d-8004-84f23685bff6 | -7.0919 | -41.8088 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 311286f9-6c27-3775-9a93-27756dbb1937 | -10.25691 | -57.69447 | 2026-09-14 04:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7943889-2dce-3774-aef3-23e27b704cb2 | -4.38563 | -55.20792 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c37f4c9a-9606-3924-9956-7c19cc3ec896 | -6.27321 | -59.92794 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd72c1ee-0c68-3ed0-93ca-780a35ca996a | -10.53967 | -51.31514 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5bcbe5d-38ee-305d-814f-a739b9c80453 | -9.71522 | -50.85394 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29d7cdfd-e742-3fd6-9bff-b4e3e381bbdd | -6.27374 | -59.92488 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c07f6a60-8f33-3c7f-a881-2c613ebaf782 | -10.69785 | -47.5249 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de576df2-a8fa-3273-9e8c-c6d90be635a8 | -11.26497 | -54.13194 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a419ed05-f566-388f-bee8-d7e8abe9aaf3 | -7.09309 | -41.8012 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a796aeee-4e0c-31e9-8e24-0c1a631d7a91 | -6.32173 | -44.17788 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7f135f5-13a0-3b87-853a-6c89289b5684 | -10.68957 | -54.15226 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3e14363-dce3-35aa-aa10-dedf6b844bc1 | -6.29179 | -59.94368 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8963c71d-5c33-3c16-aca4-45571f87e9d5 | -7.9641 | -43.9883 | 2026-09-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6ce1218-f22a-3581-bc3a-6be6287fef20 | -8.12033 | -44.05814 | 2026-09-14 04:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fac447f6-68a5-3ce8-ad15-32bedd3dccb0 | -9.61242 | -55.11885 | 2026-09-14 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcab6588-f80a-34b4-9c4f-9b3605490723 | -5.11916 | -55.96003 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b69e2bd-ddb2-3d50-862c-5a6f8a7dc0bd | -9.37439 | -50.11217 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 188ebcb4-fe6b-347b-bb3e-14b38a2023be | -10.68553 | -54.15543 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fcc3c1b-b19e-35f0-8bd7-571a01e600d8 | -6.25194 | -44.79881 | 2026-09-14 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dd09c4f-a693-38a6-911e-be160c6cdd8a | -5.13586 | -55.95902 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5931a271-223c-3707-93c0-13d16d213f7f | -5.08314 | -56.25797 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 017cebe4-e1ea-365a-b373-a4676dabe807 | -10.67402 | -54.16124 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 938a1a4d-f845-3201-8ab3-54e55c152d24 | -6.58871 | -58.86842 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27aea1c5-a6b7-3de1-bfa7-daa0b91747e3 | -10.68989 | -54.17165 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f59fa141-994a-3d49-bf10-baead27187c3 | -8.99981 | -50.83017 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2482b6a-1eab-337a-b430-4cfde648a85f | -10.55078 | -51.30962 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad77165-e367-3852-b8d1-af401639398e | -10.67619 | -54.16935 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a5e501bd-8a0d-3593-b0d8-f588b677dba1 | -5.12433 | -55.95364 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 741c1982-5dc7-3475-9adc-a567f2d64573 | -7.0758 | -41.80367 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c8b1ede2-74ba-34c8-9d52-aef6f21c4527 | -6.74534 | -59.43052 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7d6b199-02ed-3ad8-8e6e-81b5daf7b470 | -10.4697 | -51.32594 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6458090-0380-30fe-8041-e70f74a0b5bc | -5.82699 | -52.09782 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1e70f8-2f26-3b05-99a8-c0dd20ee6721 | -7.09064 | -41.81937 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b6c46d1-d207-3849-b31f-9b424fd0ea4c | -6.84855 | -55.56892 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 923b220a-2075-3f2e-9e01-58e991fd9ed2 | -6.01797 | -59.93995 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50387d92-ee24-38f2-8eee-b57649b47f1a | -4.12438 | -60.68463 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |


[Clique aqui para ver as próximas entradas](README43.md)
