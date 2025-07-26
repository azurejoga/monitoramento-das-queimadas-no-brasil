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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 154db358-56e8-3628-a1af-871099052a3a | -2.97979 | -54.50068 | 2025-07-26 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7774878e-22fa-3883-ad4f-934ac89a0402 | -2.90413 | -48.24737 | 2025-07-26 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f5bb3733-29c5-3476-83a3-9ecbe9167ec8 | -4.30945 | -48.10253 | 2025-07-26 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ca483039-626f-3ae7-8e05-d3074bd78b65 | -3.75007 | -49.04982 | 2025-07-26 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1493ecd-d20e-321f-98cc-4f605da514c4 | -3.38513 | -47.49285 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d579bfdb-4456-3d28-9a30-3455b49f8c04 | -3.39248 | -47.48488 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e3672c1c-60b7-3fb1-bab2-c5ee0a5aef52 | -3.39908 | -47.49775 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 23b2f263-8c50-38ed-b3e6-e1bda8788066 | -2.9916 | -49.32074 | 2025-07-26 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe344e10-4642-3894-9cd5-9a1aab63a60a | -3.13057 | -47.01388 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26f0aedb-30f3-3468-b037-25c49b51b254 | -3.38767 | -47.49157 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ad2878d6-c71d-33f5-8618-9bdcc71fb250 | -2.99007 | -49.32283 | 2025-07-26 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f20e0f2-9784-31cc-b8ab-4aaba3779c13 | -3.39369 | -47.49247 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7b254f30-d4b0-3e05-87a1-e7c841cb108d | -3.66129 | -48.44808 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 067c5d7f-b8ed-3e9f-99c9-1984190600d1 | -3.39114 | -47.49379 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8961742e-a7d2-3d26-b75e-d37480a9afcb | -3.27653 | -48.81727 | 2025-07-26 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b4a79ed-f1bf-316c-91fc-67473aa9bdb1 | -2.90981 | -48.24829 | 2025-07-26 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4c7817e7-f92a-36ca-bb49-0f5574d379ca | -5.6669 | -51.36142 | 2025-07-26 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11a18ab5-065f-3b71-8ea0-8318f6d27249 | -6.01379 | -52.17442 | 2025-07-26 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35f64144-854c-3010-a8ef-b2228e9c4db4 | -3.05282 | -47.37912 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27770ec6-0911-3f38-81d3-daeda19ae904 | -5.67168 | -51.36227 | 2025-07-26 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d9c4d6b-252e-364b-a5f3-020a843d9cc5 | -3.66187 | -48.44396 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9147a212-6338-3178-a8ea-bb49f5fe1120 | -6.57134 | -49.50393 | 2025-07-26 05:16:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| becd0a89-9be8-372d-acce-db2c51761ea5 | -3.98949 | -47.88945 | 2025-07-26 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76ef0f1b-4c68-3c5b-bdfb-7e3951260b6d | -3.31478 | -48.71294 | 2025-07-26 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3ce1820-42a8-38e5-b2a5-5fa02636c9cc | -2.97907 | -54.50528 | 2025-07-26 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c54728ac-85eb-3bd2-802b-9adb37fda74f | -2.99584 | -49.32035 | 2025-07-26 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b640935-0c62-3ae4-8a72-0be4835224dc | -3.0509 | -47.38028 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f09a727b-9881-35ea-9dac-c512c7727254 | -4.30299 | -48.10585 | 2025-07-26 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7baf1443-e135-326d-b17f-1bf17b8fb500 | -3.38705 | -47.49594 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1c55af80-7a78-3d4b-97c4-bf7707819281 | -3.39181 | -47.48935 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aabbd6ce-f495-37b0-ba61-a6f213072cf1 | -2.90924 | -48.25216 | 2025-07-26 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 34a53397-002e-3b34-9b2d-36d462774d1a | -3.27704 | -48.81367 | 2025-07-26 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61549ec6-9fa2-33ed-bea5-c9a0dc0ece09 | -6.9901 | -47.0808 | 2025-07-26 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18dddec6-e9ae-3a0e-9dab-9476f08f4c10 | -6.98938 | -47.08627 | 2025-07-26 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4548725f-bfba-3c21-a31b-880d114dda03 | -6.01448 | -52.16975 | 2025-07-26 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea7b1d4b-8bbb-3e91-a8dd-0b35dc2a9a88 | -3.05693 | -47.38116 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7209bb0d-d34a-369c-8636-737eea249046 | -3.17574 | -49.45317 | 2025-07-26 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc0dd1f6-633e-39a3-8959-34ccf3b20329 | -4.30359 | -48.10167 | 2025-07-26 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e190d28e-eda4-3029-b10e-f6bd0d0550d4 | -3.98354 | -47.88882 | 2025-07-26 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1e89b57-9cc8-35ee-b090-d2678fc5ec3a | -3.04423 | -47.3837 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e1e2616-c72a-3218-9162-8fa96ec8b2b1 | -3.38579 | -47.48849 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cf7fca3d-0bf0-330f-b4ac-92d47735b1bf | -3.05221 | -47.3834 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 690eb7f9-b02b-3f9d-8fef-53f091c73dab | -3.75555 | -49.05055 | 2025-07-26 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 757e5aab-b6ca-3817-9e96-90c5683d98ed | -3.39433 | -47.48796 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5828e812-6034-3ed9-92fd-7a5d1c52683b | -4.30885 | -48.10671 | 2025-07-26 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 91e4d1e1-90c1-3f96-9f0c-56298ff43fac | -5.32326 | -55.94469 | 2025-07-26 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1752fa27-214a-328e-9ead-bab817fed5f4 | -2.99691 | -49.32151 | 2025-07-26 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3aa6908-f494-390b-972b-30d504c707af | -4.10464 | -48.2058 | 2025-07-26 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ec21fa5-e2df-3618-82d9-4b006590ee7f | -2.98124 | -54.4991 | 2025-07-26 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f36a025-23c8-3f9f-863c-9377d4629255 | -4.34968 | -47.69159 | 2025-07-26 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 910598f7-7c1b-3883-a725-46fb2aa243cd | -4.07362 | -46.90421 | 2025-07-26 05:16:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 145501cd-c141-326a-a906-100aaaa523b9 | -3.3883 | -47.48716 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 362c67e4-2088-3af1-904d-0c1d658bc823 | -2.98055 | -54.50374 | 2025-07-26 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5108ff2d-3758-3f99-9661-694295879e51 | -3.39973 | -47.49325 | 2025-07-26 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c33f684f-ed44-387e-a2d8-7ddfddbd8653 | -6.64328 | -58.85162 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65cedbe2-2bdb-35ba-99aa-a1d43cc1913e | -6.68881 | -58.84504 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18896f4c-7bf7-3596-a91d-fd6c37b8e6de | -6.6645 | -58.82706 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 6d59fd24-6864-30a8-ab11-2b3907c7960a | -8.07313 | -48.01073 | 2025-07-26 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c55b7965-6351-3f3a-9d24-22619a1f2394 | -6.6805 | -58.83311 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 80b146f4-25d7-34c3-b729-88ccfdc9eb3f | -6.66958 | -58.85977 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 857db3b8-13a6-3162-a3d3-c552b2cda6a7 | -6.67227 | -58.84246 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 3bdc8c99-b848-3d44-ae8e-bd4ad80ce153 | -6.62728 | -58.8456 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| fd0e3bd7-97d2-3864-b74d-7f85352b8b2d | -6.65867 | -58.83984 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a28793ff-e4da-38d1-93e5-d9a6872182c1 | -6.68489 | -58.82669 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4d13a63c-67e9-3a5b-9de0-f500944c9371 | -7.81522 | -61.3314 | 2025-07-26 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| accfb9e1-d9bf-3f5c-83d6-a0171a94389b | -10.04487 | -64.99243 | 2025-07-26 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b257c27d-856a-37d6-bcfc-68672a9d9b7b | -6.64658 | -58.85213 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 4d9e269b-6ea9-3442-9468-74440eabb971 | -6.64544 | -58.83778 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 55f81a70-ba8b-3046-ac9f-08f5afa48fec | -13.12837 | -47.3289 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89269474-795a-3e29-a86c-5b535afc7f10 | -7.90314 | -63.5307 | 2025-07-26 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fafa4e05-debb-3911-96a7-33e550aa3b9f | -6.78269 | -61.96478 | 2025-07-26 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f0c9668-ebd4-35b3-ab1c-75954064f4f4 | -6.66842 | -58.84541 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 12720d88-70b4-3a14-b14e-87e85a0cc25f | -10.67334 | -51.89217 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f5386eb2-943f-39d0-8d64-3e97cd55c469 | -6.65205 | -58.83881 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 35e30572-2e2a-3ac3-ac08-fce07b917535 | -6.66127 | -58.84784 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 9d24c509-bc4c-34a5-89dd-5c1fbe65b49e | -6.68104 | -58.82964 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fd3ea651-b4aa-3356-8156-6c52c4f12c96 | -6.53431 | -56.26422 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db96ba88-f244-35ba-aac1-32f7e73cdefd | -6.69266 | -58.84209 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5ab3898-4cfb-3a19-b3f2-028dc9348274 | -6.62781 | -58.84213 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 9da029eb-3b4a-3f23-b982-9e21f8316338 | -10.04802 | -59.10426 | 2025-07-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 409c8973-27da-31d6-8fa2-618b33ff92e5 | -6.68058 | -58.85439 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f0b5c6d8-53a1-3f68-be6e-bbdad1b58dca | -6.67442 | -58.82862 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8aca35c6-2410-329e-bcb4-9a46d9bbacc1 | -13.111 | -47.36138 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 932b4335-ba5c-3865-b2d4-7fda4dfb85e7 | -8.6103 | -64.06814 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24f20310-b0fd-307e-ada2-4691b70ea140 | -6.62997 | -58.82829 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2d35da7f-ecd8-3242-a5ad-bb9ba0d51cf6 | -6.61951 | -58.8302 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cf84c1c-b043-3453-a739-b4ac5b03be18 | -6.55576 | -56.24252 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b982487-d9a7-3ec9-837a-e8bbf554edf2 | -7.18342 | -59.44381 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c7babde-f267-3c41-962b-1b9e32f983ed | -6.65036 | -58.82791 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 239e44c7-c0b7-3798-ada4-e353d1107909 | -6.62505 | -58.83816 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c687e9e7-2e16-341b-b15a-10d95aabee59 | -6.67719 | -58.83259 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9593c808-88a8-3105-8865-c971e26ffcae | -9.20732 | -59.68132 | 2025-07-26 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a97457c1-a6a0-3d3f-9c47-f31c34c08922 | -7.66305 | -69.92786 | 2025-07-26 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9af55667-3a85-3cd7-bd0a-4982502ef1c5 | -10.67983 | -51.88702 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14f1a62a-ddc8-3fd8-81d8-fe79cf45abf7 | -6.62835 | -58.83867 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ceba2cb1-9571-3c81-894b-84ed68a8f141 | -6.68327 | -58.83709 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 821378af-591e-3c5e-9a44-e0a47301cead | -6.65259 | -58.83535 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6cc1b208-359a-3837-964d-bbac749acf85 | -6.67504 | -58.84643 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 03a9d68a-ecb0-3a2d-a579-3216d4bf52fe | -7.29188 | -60.18149 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef5fe11f-40ee-3d33-9819-5cf64bbc9296 | -10.79098 | -56.92041 | 2025-07-26 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README24.md)
