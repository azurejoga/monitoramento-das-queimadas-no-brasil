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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14b0d27b-52d5-3c69-b89a-01da51ca0e54 | -11.76894 | -45.00061 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ecbdec4-258c-3132-a3b7-e2f547c9cced | -11.77669 | -45.01074 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a43dc346-d3b7-317f-9407-0924c5d5787d | -16.13191 | -46.88148 | 2025-08-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1bf2f8db-678b-3023-ba46-9af16ec58c33 | -12.60303 | -44.8283 | 2025-08-01 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b688fd97-005f-30c9-b447-141b3b578bd7 | -11.77419 | -45.00916 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c88d138a-7662-3557-a628-ce71ea115bc0 | -16.12502 | -46.87991 | 2025-08-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e4d51c9-e158-306f-80ea-d60c3badd784 | -16.13342 | -46.87489 | 2025-08-01 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4a2c5148-532c-396e-8428-455c2844b311 | -10.60479 | -45.2739 | 2025-08-01 03:25:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0e304fa5-e32b-301b-9d54-365e2fec6913 | -12.43789 | -44.74981 | 2025-08-01 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23e1135d-54c8-3c5e-a39d-6d0ae49600a5 | -11.77001 | -45.00923 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0c2739e-acb9-38a8-8dfd-b63918b16f04 | -11.76608 | -44.99468 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bac6378-94cf-374d-8d1b-0c786e4854fa | -16.15659 | -40.19457 | 2025-08-01 03:25:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0621c487-ca2e-3c1f-a9a9-a6f6ca33cd51 | -12.43657 | -44.75098 | 2025-08-01 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00d7b2af-8288-3509-9a88-722d61b9be21 | -11.77261 | -45.01696 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 534c414b-5cb8-37f3-b2a4-8cd7ffccd7af | -11.77156 | -45.00185 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd5fd527-1ce5-3505-af45-53a72f587c5d | -11.76338 | -44.9936 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa68efa8-2c63-3bb9-952e-9de522698daf | -10.60433 | -45.27146 | 2025-08-01 03:25:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 948869ad-4c61-3094-a4c9-3d330155223a | -11.78078 | -45.01113 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4cf2e7d-559d-316a-ae3f-e1c304102d7b | -11.76748 | -45.0078 | 2025-08-01 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 687a3f92-edd0-3d95-b4b9-e4ac2848235d | -10.60602 | -45.26786 | 2025-08-01 03:25:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb20ff62-a682-3381-8178-03a4693db9fc | -20.44736 | -46.42349 | 2025-08-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68ffc9f9-530b-382f-b33c-5065956621d1 | -23.52205 | -47.83699 | 2025-08-01 03:28:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| 6c4a3ee2-a151-33b4-8145-93a126ce1434 | -20.47239 | -46.27923 | 2025-08-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30a25e87-c9db-3b4d-842a-d648a3c75fdc | -20.34733 | -45.99119 | 2025-08-01 03:28:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fde3d072-db53-3056-b8f1-81efc1868c5f | -23.52346 | -47.83128 | 2025-08-01 03:28:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| 1dfe43f9-6e79-3261-8112-1e966544a642 | -21.24311 | -48.5731 | 2025-08-01 03:28:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1e0daaa6-a275-3456-92c1-d6cfa624a1b5 | -19.53856 | -44.10092 | 2025-08-01 03:28:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b29ffaa-154c-3690-b6b7-dd2e65cd3697 | -23.51566 | -47.83568 | 2025-08-01 03:28:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| 9a069dbd-3c11-3226-8f22-2edb095cbfeb | -20.45193 | -46.42147 | 2025-08-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 082eca98-825c-3ba9-98fc-1f29f178f8b9 | -20.44019 | -46.42621 | 2025-08-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6a4799d-a222-33c6-9af0-f48b43038429 | -20.43625 | -46.43231 | 2025-08-01 03:28:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90d51248-fd3b-3b7d-8835-06083ee318c9 | -19.68033 | -43.92461 | 2025-08-01 03:28:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a8718cc-61f8-3fbf-b5b1-5e9f9e50e0b7 | -20.43901 | -46.43132 | 2025-08-01 03:28:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aea828b4-dd9d-35d8-a27f-65983cad6ade | -18.21687 | -44.71751 | 2025-08-01 03:28:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 800a885a-2391-3da9-b11c-60ced3f2b550 | -22.51424 | -47.21824 | 2025-08-01 03:28:00 | NOAA-21 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 735b6c19-4e82-3da5-ad49-a46aa19a5083 | -21.24428 | -48.56626 | 2025-08-01 03:28:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d14ef92-cdd8-3954-94c0-7be0d752080f | -22.95655 | -49.1242 | 2025-08-01 03:28:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bb589cf-c021-3ac7-b4e0-fe4ce185a738 | -23.51711 | -47.82981 | 2025-08-01 03:28:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| 429ad3ec-c87e-30b9-9232-13b2a2e6ea9c | -22.95733 | -49.12102 | 2025-08-01 03:28:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd78dcde-8ebb-3221-9787-9d7620efa1ce | -20.43748 | -46.42712 | 2025-08-01 03:28:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af065be9-db47-3d16-81d0-8f65a1ca1080 | -22.59372 | -42.10381 | 2025-08-01 03:28:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ac86fa5e-f05b-370b-b257-69f8f378a6f3 | -18.21088 | -44.71672 | 2025-08-01 03:28:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb95226b-363a-3dfe-a200-b3e5beeb8ae9 | -20.44349 | -46.42945 | 2025-08-01 03:28:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 562a77c1-9dc8-33d3-8806-748094e0c2ef | -20.44224 | -46.43475 | 2025-08-01 03:28:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0da7ba7-325a-3843-b49d-b3d303a29fb2 | -20.44501 | -46.43373 | 2025-08-01 03:28:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46cb365e-e8cf-318b-b54d-e04a38a84c42 | -18.21494 | -44.71597 | 2025-08-01 03:28:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e98b2a00-ed50-3df5-aab9-aa4c57b644eb | -22.11046 | -44.61205 | 2025-08-01 03:28:00 | NOAA-21 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7ffddb69-7163-358d-b69f-b0757fccf6c2 | -22.51727 | -47.21758 | 2025-08-01 03:28:00 | NOAA-21 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adb1ff09-f74e-360d-ba21-d19475226012 | -23.52941 | -47.0717 | 2025-08-01 03:28:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ea3f881-2404-32ed-bf20-aba043add6c9 | -22.5155 | -47.21311 | 2025-08-01 03:28:00 | NOAA-21 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5085efed-1df8-3f3c-86a7-f44883042887 | -21.24481 | -48.56617 | 2025-08-01 03:28:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e174b85f-26ba-3deb-acf5-a48d0072b34d | -20.45074 | -46.42649 | 2025-08-01 03:28:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a769b42-77e4-3c18-a450-6e340c0e5dc6 | -22.95556 | -49.12807 | 2025-08-01 03:28:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42766f74-3995-362f-a7ff-150577b101d8 | -22.51117 | -47.21549 | 2025-08-01 03:28:00 | NOAA-21 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 71a023c8-48e6-37fb-ad68-036463d4b323 | -23.5234 | -47.835 | 2025-08-01 03:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| 1dbc6c6c-7fb5-3c44-87e8-c60963378552 | -6.7295 | -59.153 | 2025-08-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 935777ac-5006-3f67-b4ab-6edef3cc6fb1 | -6.6328 | -59.9841 | 2025-08-01 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| faaf8194-2630-349f-b6cd-d349812a1d4b | -8.0321 | -43.1257 | 2025-08-01 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 175.5 |
| 054d9438-7aca-3dce-85ed-d0e4e473b703 | -8.051 | -43.1237 | 2025-08-01 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| b8c80f21-7d73-3822-9c12-a5a69c2403ea | -6.7477 | -59.1909 | 2025-08-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 40881a86-0a42-33c4-aaba-3a9a077f47f7 | -6.7478 | -59.1716 | 2025-08-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 6325701d-b2bb-3766-ba6a-9999e3e4686e | -8.0513 | -43.1001 | 2025-08-01 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 799643bd-5dac-31f8-a4c7-2e3ef0621d91 | -6.7293 | -59.1916 | 2025-08-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7105e454-3018-30d1-9f6b-5fbf96965213 | -6.748 | -59.1523 | 2025-08-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6daf7785-4630-398b-851b-416636bcebe2 | -6.7294 | -59.1723 | 2025-08-01 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 237.4 |
| 3c5d81b0-ef1d-345f-af5f-78428f870253 | -8.0324 | -43.1022 | 2025-08-01 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 607b1dc9-f9c1-3252-8968-948787d97604 | -28.64497 | -50.02294 | 2025-08-01 03:30:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c6bbf792-c3d0-366e-917e-61b1c0b88e3a | -6.7295 | -59.153 | 2025-08-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f25ad86d-42a8-35c4-b0ef-1ba9568a0e41 | -8.0324 | -43.1022 | 2025-08-01 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 8eb2435f-4408-3d81-899f-5cb66089c651 | -6.7293 | -59.1916 | 2025-08-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7e4f27a7-b16c-3f42-906a-8b4bce864b3e | -6.7478 | -59.1716 | 2025-08-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 206.6 |
| 55f41e66-6409-3525-8c70-ad2dbc8c2d92 | -6.7294 | -59.1723 | 2025-08-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 246.5 |
| 8bc45f4f-aed0-3f2b-8110-d35f09bd353b | -8.051 | -43.1237 | 2025-08-01 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 37b2381b-4796-346b-aef5-4fe90c9e03c8 | -6.7477 | -59.1909 | 2025-08-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e2f00cac-0b7f-3d4d-b584-5544be3ad39e | -6.748 | -59.1523 | 2025-08-01 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| c0683b2f-8c8a-37d9-8afb-5dbbc9ce614f | -8.0513 | -43.1001 | 2025-08-01 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 442431d8-37d1-30d8-b9d7-b5e4a92125cd | -6.6328 | -59.9841 | 2025-08-01 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7af790a0-0e0a-3c67-8cfe-27ac321e56fb | -8.0321 | -43.1257 | 2025-08-01 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| 01d37330-ab56-3a95-9d0c-5219cd6cb4dc | -3.82093 | -41.57216 | 2025-08-01 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 77526785-877c-3c5a-8b6c-05eba8878ab6 | -10.07672 | -37.67078 | 2025-08-01 03:49:00 | NPP-375D | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a385d8cf-5f56-35e4-9fe2-97f535d7fd3b | -8.33147 | -38.09268 | 2025-08-01 03:49:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c0757ae0-7869-3ced-8de1-5a9b4f8bec0b | -7.72211 | -45.09785 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcb89885-7de7-3d9c-9085-9e8720820af1 | -7.57601 | -44.8215 | 2025-08-01 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad7e6568-2043-3e6f-9a1d-b20692fdf36b | -7.72809 | -45.09304 | 2025-08-01 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cb4d0d2-00ae-3cb9-a6d1-e78400ba5a58 | -6.5726 | -41.53912 | 2025-08-01 03:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ae49fdc8-4734-3d8d-b2ac-9c6d6fb4df52 | -7.8779 | -45.54744 | 2025-08-01 03:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf363a7f-b2ce-384a-8beb-0793b0ab51eb | -8.51953 | -43.3109 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b86c3e09-7ac1-387e-8cc9-11d9140b62d2 | -8.04505 | -43.11716 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 7ba6ae28-a61f-3ef3-bd94-a630e9286820 | -4.22528 | -47.21998 | 2025-08-01 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4757cdfb-f311-3f91-abf6-c09b59f2c405 | -7.30128 | -46.14786 | 2025-08-01 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b04c8a03-8962-3aba-a112-e66d5b868969 | -6.94939 | -37.39182 | 2025-08-01 03:49:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3904d460-266d-3f95-8dcc-f8baf94a0dd5 | -7.88302 | -45.54826 | 2025-08-01 03:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64b8092f-6e66-32f3-a034-436c4dca5d57 | -6.57175 | -41.54429 | 2025-08-01 03:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 864d6b67-44f1-35cf-a5be-25a990c69409 | -7.87332 | -45.54363 | 2025-08-01 03:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10fa77d1-e94f-3428-bd79-5b23eb0401e6 | -8.51376 | -43.31845 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e78f08f9-af3b-329e-ac67-215e125cf88e | -4.30824 | -48.1098 | 2025-08-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6db5688d-d881-33df-9733-edb5f4873fa1 | -8.03497 | -43.12389 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 5efc55be-6e3d-3193-bd73-0c572859f61c | -9.16331 | -40.59819 | 2025-08-01 03:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.2 |
| ecd55118-f286-32a8-9a39-dd76db38900d | -4.31553 | -48.10577 | 2025-08-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2c295d62-ec8c-3dff-83c8-265ad6ca4f1d | -8.05152 | -43.10561 | 2025-08-01 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |


[Clique aqui para ver as próximas entradas](README10.md)
