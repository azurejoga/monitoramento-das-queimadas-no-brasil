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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1af911dc-c7d8-3ac9-b1c1-e1f5dfaba4ea | -5.89756 | -45.53202 | 2026-09-28 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ef71a41-ff97-3a17-840d-9e90f7a9e210 | -3.10438 | -50.32276 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 339449b8-80d7-35ee-a9e1-685fef7f07cb | -2.05209 | -56.86933 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03a9b50d-6252-3000-ae04-d9a9f04bb928 | 1.67636 | -55.95417 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05a43a65-4acd-3f5d-9786-dabb22f87cd2 | -3.9737 | -48.00657 | 2026-09-28 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09618d67-392f-3312-88a9-cd2e2e71dd4f | -4.01282 | -43.23141 | 2026-09-28 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 220df9c7-237f-3d02-b689-b14c15802b34 | 2.38356 | -51.02117 | 2026-09-28 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29a66655-46dd-32ff-9997-0b845d395918 | -3.14554 | -54.08333 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24554cfd-d879-3a0f-9f56-0e3f410a3f4c | -2.05762 | -56.87043 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ba30283-84c6-370f-a0d6-c47a79adc6ed | -2.27228 | -52.01598 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26f9c8c6-a5fa-3ce0-8048-9395bd0a3bc9 | -2.98604 | -51.05471 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7149b947-c769-371b-abbe-96553a1e9dd7 | -3.82442 | -44.09176 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bca94cb4-7c99-330a-a3d4-54cb7bfd0b3d | 0.46698 | -50.97446 | 2026-09-28 04:32:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37d80d6f-6544-3367-b80b-4dfd6928a194 | -3.3606 | -50.46491 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1aa0d9ea-879f-3095-a52a-5235ad1e6bd8 | -3.01609 | -54.21674 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7d74f1c-a026-3b9c-b5e0-12dd8027e7cf | -4.18326 | -50.40021 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2c3c43f-074f-3e12-9dc5-daff41ea57c0 | 1.67269 | -55.93253 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d48abaf2-25a3-34ea-bb38-a7d57fabcb13 | -2.14641 | -46.17566 | 2026-09-28 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b7dc1261-4a4f-3202-a73b-ae75dfb05f91 | -2.77465 | -49.48948 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec359525-e682-3e7d-b11f-be830be73fad | -3.41953 | -50.43171 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47576561-845a-38c8-9abe-3e959f4c8c35 | -2.12391 | -56.88445 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84cd7efb-7a87-3924-8e69-b99ff90d60ac | -2.93033 | -48.75232 | 2026-09-28 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a75645d6-02eb-3258-b8d7-de7b1fbdeaf6 | -2.99919 | -54.75445 | 2026-09-28 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66025335-9b91-334f-8f46-867ae1373f75 | -3.20697 | -51.03197 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3ffcfa0-b3c9-3c8b-b5d3-91e93d5b28ff | -3.20998 | -51.03701 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d8afa4c2-f980-3316-a67b-84dc10d2983b | -2.67557 | -56.46228 | 2026-09-28 04:32:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a307af01-d3f3-39ae-9793-85232a839269 | -5.39028 | -46.5754 | 2026-09-28 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43a9f0a9-8ad8-347e-a064-8ef810c2eba9 | 2.38409 | -51.02464 | 2026-09-28 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42f6cd23-234d-3270-a124-d062a4d34dd8 | -4.91392 | -37.36816 | 2026-09-28 04:32:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 55422e35-1614-3ebe-84f6-430f0930054d | -7.67979 | -54.74403 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a01e80c-f189-3354-940c-9c45a11a0250 | -11.68299 | -44.54455 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb70d07d-7dd3-3336-953d-c3368a284bb2 | -8.66553 | -48.965 | 2026-09-28 04:34:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5930138-43a6-3b66-bbf6-8fb59924dfc3 | -10.20056 | -49.99492 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d43e99c2-6dd5-37cc-b8bf-512d9607a95f | -6.30821 | -56.03473 | 2026-09-28 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2535b96-512e-3e90-967b-d1da0648cc0c | -6.74789 | -55.09272 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82d9f353-6742-3120-a9fa-ba02faaf0a8e | -9.55059 | -47.97475 | 2026-09-28 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc93c85e-6c80-31df-89c0-747b28493005 | -11.11097 | -47.1033 | 2026-09-28 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afb14c25-c64d-3ae0-9781-155a299b1e3f | -11.45013 | -44.92727 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a01b0b6-e40c-3b72-8dc6-099b707f3937 | -7.52192 | -46.61159 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b148184-3b5d-33e9-bf70-1ba90d3bc4bf | -13.10265 | -47.4213 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| defc06e2-fae1-35bf-be8e-8afe8964df52 | -9.99887 | -50.13078 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fec57eff-542e-3eaf-8f68-01e231410221 | -8.76825 | -45.82745 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17e0b16a-dbb2-30a1-b198-a773e05e78b7 | -10.72426 | -49.02796 | 2026-09-28 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fab5fd7-d00c-382d-b09f-4dd7e98f076f | -10.92256 | -50.66831 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 108fa915-e1ad-38d6-8a6e-a59a0426d477 | -9.97353 | -45.34029 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94c89c63-c523-3f76-9b8f-a9238b07a044 | -10.17106 | -63.05967 | 2026-09-28 04:34:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 693af2d9-a772-39f6-937e-ba64e781e415 | -9.27015 | -47.72129 | 2026-09-28 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1529b3c7-cf27-38fe-b87c-d175ac4f4994 | -9.94537 | -48.69922 | 2026-09-28 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7035c969-534f-3f1a-a2dd-eca21983029a | -6.99169 | -42.69513 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e57262bc-3151-3725-bef8-513817174fab | -7.26997 | -45.34012 | 2026-09-28 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e02f4ea9-7b8e-3e93-b125-47844a0a9b6b | -6.18513 | -44.12152 | 2026-09-28 04:34:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 354ba235-2d23-3de4-b9eb-138c46458a3b | -6.66464 | -55.11077 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 84bae945-bb5d-36e5-a84b-5f8c0084855d | -11.14283 | -50.06118 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d78ad83-b1ee-3bfa-8128-1e8f0b3b4ce8 | -6.94978 | -41.60371 | 2026-09-28 04:34:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ff9212ec-8516-3026-8e50-66a208231db7 | -10.71295 | -44.43415 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03a904b3-c59e-343c-899a-966bbe17532e | -8.4188 | -44.87211 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc2a6630-8a51-330e-81d8-8ba36f27f2ff | -6.99301 | -42.70034 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 839ec836-b080-3a2f-94e3-679dee6f450d | -11.69602 | -50.60116 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69fe0837-c45b-398b-a0df-4301a050d8a5 | -10.65071 | -50.71461 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc44b76b-f21b-38f2-bc90-2138bde33035 | -6.59814 | -47.16602 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 976913ad-dff3-35ed-93d7-6edbec914ff7 | -11.19051 | -44.79929 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 1816ed1d-0cd6-353f-a48d-ec9f399c9cbc | -7.57391 | -46.63451 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97bc0599-fa4f-3633-a2c5-83e22af86404 | -11.33517 | -54.10963 | 2026-09-28 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3c061c7-1f2d-3ae6-a3d8-f61a137d4b6f | -10.8231 | -61.41278 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d3ea482-5341-3942-b57c-6a9b06955548 | -11.27014 | -43.54061 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f76033ac-44ba-3021-82ac-96cf2654a9ce | -9.98147 | -50.15378 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a12e41b3-23a7-3208-8fb3-c2eb94d1fb40 | -12.63489 | -47.26568 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c86fd56a-de7b-3f8f-9c51-cb8b1f6a1df4 | -11.51945 | -50.6876 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c25c1d6a-5f09-3ee3-ac7b-db0f916ece58 | -6.07575 | -57.81302 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80401b48-ba7c-3b68-b4be-83dfedcb20fa | -11.43937 | -44.92872 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a7b4dc2-7a98-3528-90fd-df2336132ef4 | -9.79081 | -44.82412 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32f87bf7-a4be-3414-948c-14e6138dd6da | -7.82193 | -55.12965 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0670f49-d561-32ed-93e2-0fae1034ef91 | -10.21781 | -49.99405 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf2f11b8-f119-3676-9002-d9d8025bc72b | -13.45764 | -46.32208 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be928aed-1a54-3031-b519-eef6ac38bc6f | -7.33672 | -42.08306 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5980d778-e768-33ba-afef-a42802f9f999 | -6.07319 | -57.82777 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eb1bbc5-841e-3d59-8b18-49824116cdd9 | -13.10723 | -47.4142 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b6e501e-9cd4-392e-8dd0-5bf38716b9c5 | -10.42612 | -53.841 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4cdbbff-587a-3c91-8348-4c99a0885c49 | -11.33709 | -44.96289 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e2593da-a96a-3712-9294-3b1d9ef5e406 | -9.74555 | -48.95274 | 2026-09-28 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7029fa2-7a4a-3efe-a6b6-8ddf4c93b9dd | -10.22171 | -49.99102 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5651ee29-74b2-3e5f-b7c0-427438aaeb69 | -6.69741 | -42.14722 | 2026-09-28 04:34:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d2155bca-d001-34c6-9290-c8ea649fef4b | -8.02538 | -54.89164 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d64a7d3b-d2a8-3908-96f3-180d854ed9ee | -10.82286 | -60.75064 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| a1e31af4-b021-312b-877b-28292e48e83a | -8.03269 | -54.90182 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30841dbc-e42b-3186-b902-8137502dbb3d | -9.26694 | -48.66624 | 2026-09-28 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2dd6acc-cf23-3488-8e64-b48e90efae30 | -9.079 | -49.87568 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e302ba82-754d-3b41-9650-af2e8ca50208 | -12.59111 | -51.96283 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79b8d852-57dd-3d59-82fa-343f3fcef49a | -11.54622 | -50.5205 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 87b75164-606b-3d90-8237-017379f04cd0 | -11.33545 | -47.75082 | 2026-09-28 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0429143d-caee-30de-99eb-f3e8449607c7 | -11.68228 | -44.54963 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7a15b28-8e11-35e6-a920-32690fa30cfa | -7.72021 | -54.77169 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daffd47c-dc78-3820-86f6-73adaa73c96d | -9.8282 | -44.94462 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f4c6361-cf62-3b14-8c80-88031c7baef8 | -11.47804 | -46.85245 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0179f7e2-7129-313d-97e9-1a5ccc8e5ce3 | -11.83373 | -44.98106 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fd260c9-cb5d-3b8f-92f8-f3cfdc3a661d | -12.73267 | -47.29165 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d743c98-aa0f-3808-8b12-2e43b98023de | -7.05714 | -42.82759 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edf6dc30-5a4f-3f14-a8b3-252f6158df72 | -9.78704 | -44.82357 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72a9aef4-9ed0-3ab2-9b23-a63c7050aea4 | -10.92872 | -50.67308 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce3c02a1-7e78-3c0e-b94b-de46e524146b | -9.77442 | -44.83099 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README30.md)
