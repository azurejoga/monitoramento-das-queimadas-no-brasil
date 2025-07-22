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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed27ad99-3f1b-33e9-aa03-8af0a1f3e618 | -7.14499 | -46.10053 | 2025-07-22 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04329bc2-67d8-3c45-a2de-062a5ce3d42c | -6.88348 | -42.76195 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e318b4b-d9f5-3f85-b164-65f0e562f726 | -3.65179 | -48.32394 | 2025-07-22 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c23ddab7-93f2-37af-847c-cb62e50eb67c | -6.19528 | -44.39133 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ed3beb7-ae91-35ff-a14a-80447caadf1d | -7.16155 | -40.21276 | 2025-07-22 04:00:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6f734703-329e-3ee8-b8a4-a2ae514846df | -6.6359 | -49.76008 | 2025-07-22 04:00:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e66c9f91-4ec9-395d-b365-d1ef124a9613 | -3.82678 | -47.74147 | 2025-07-22 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c723a00b-2778-3a26-858b-d22c46d91dce | -6.64137 | -49.7611 | 2025-07-22 04:00:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 148fcbc4-ce2e-34ac-b4f8-e36cad566b43 | -6.84169 | -42.73129 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f6a5a85-3dc0-3fd0-bfec-1da95c92e16e | -5.68091 | -43.67397 | 2025-07-22 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef957e81-156e-3cfe-b708-410e32b23e84 | -3.50741 | -43.2482 | 2025-07-22 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 786db63b-ffe0-3e42-bf0b-09da0abad7e4 | -6.63222 | -44.57529 | 2025-07-22 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05129704-b8c0-3747-934d-29cfdf0670fa | -6.97805 | -42.80432 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 245ff876-2ea9-3b07-8a91-2c0c8758ebd7 | -7.20555 | -45.33065 | 2025-07-22 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceca2711-4235-3ee2-9e93-07269e2ffad6 | -6.62589 | -42.33673 | 2025-07-22 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7d95c102-da4f-3bba-845f-48ac2c57b94a | -7.1783 | -44.14393 | 2025-07-22 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44f27382-1d29-3933-ba22-6897e08c7308 | -7.14634 | -46.09271 | 2025-07-22 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9bb47ea-aa88-3aac-bdbf-2e8057e13f1a | -5.88162 | -45.20854 | 2025-07-22 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aad02eaf-f6b2-34fb-8343-3bf9ddb47ebd | -3.39195 | -47.483 | 2025-07-22 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba8493e3-acaf-35b0-b9d3-c25f6a994d39 | -3.82649 | -41.57698 | 2025-07-22 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2fecb5a6-a26a-3d19-9d80-f82c930c71c1 | -3.35448 | -42.87438 | 2025-07-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8aa60e0c-3398-3fb4-b1b2-ae458f10b188 | -6.1945 | -44.39615 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a25af41-18d3-3803-bc07-ccccc6aca22e | -6.84457 | -42.73572 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4c59e00f-9a03-3496-b60f-af688dbb04d8 | -6.61899 | -42.33556 | 2025-07-22 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ffe1997-b3cc-3df9-86db-0732d602c9ce | -2.54033 | -47.69203 | 2025-07-22 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54e98e9f-2f13-35ef-b176-051fe51e39b0 | -5.51262 | -35.58245 | 2025-07-22 04:00:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 229c0bb2-e8bb-3b35-a788-4f11b62aebcc | -3.39289 | -47.47733 | 2025-07-22 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad412080-4145-3a2a-85b4-301209b9d39f | -7.15547 | -46.09042 | 2025-07-22 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2656aa81-23cd-3d99-86ac-1b6324f6154c | -8.04314 | -42.16326 | 2025-07-22 04:00:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4fb2ebae-8975-345d-a5ee-04ebbfe2bf82 | -6.63042 | -49.75905 | 2025-07-22 04:00:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d632bc8e-b087-32a2-957f-f2dabd0ebd7d | -8.11879 | -42.94692 | 2025-07-22 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4570c56-b3bb-3ade-8347-6b0f762dec6c | -6.46889 | -43.19364 | 2025-07-22 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89b6ef17-3c16-3e66-aade-e92072804bf4 | -4.38233 | -43.28224 | 2025-07-22 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 67d5db61-de14-33cc-8d17-bb5e3dcbefe2 | -6.21018 | -44.30003 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 243609a2-ee70-304a-bee7-60c1fc64b210 | -5.56249 | -45.22033 | 2025-07-22 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa65ac81-7faf-34bc-b86c-ffc90a159d18 | -5.91918 | -43.46321 | 2025-07-22 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca0b3bd5-8027-30c6-99f5-ada1d03b4cda | -6.88411 | -42.75811 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e069363-38b9-39bf-a04f-a8b9c95f3320 | -6.85119 | -42.80542 | 2025-07-22 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 395bc3d9-0b33-389f-83b4-a64451380aae | -3.82728 | -47.73853 | 2025-07-22 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5df4d21-7003-322b-bc46-b24010255c76 | -5.84383 | -48.15503 | 2025-07-22 04:00:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8ce11be-ac98-32a3-846b-591dd348ddad | -6.96349 | -44.38872 | 2025-07-22 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b31fc59f-5ac6-3371-8f42-7a79b4660cfe | -7.78198 | -42.9662 | 2025-07-22 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 561cdaf7-218d-363e-9405-24346c85b75e | -6.6196 | -42.33175 | 2025-07-22 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 687294f1-8db2-3d32-bebc-1e670e5db850 | -7.08708 | -49.16661 | 2025-07-22 04:00:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f7cac86-2364-38f4-bc3f-c06678c75d11 | -5.67605 | -43.67152 | 2025-07-22 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99ebcde9-3031-3fbd-98e4-488e1631038d | -3.50367 | -43.24759 | 2025-07-22 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61f52613-ecd9-370d-8d01-04ae77362299 | -5.83832 | -48.15714 | 2025-07-22 04:00:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47bd9852-5dbd-3e56-af3a-ace409affeb1 | -7.18205 | -44.14459 | 2025-07-22 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02f10b03-a7fa-3b36-a32d-352062c7be45 | -5.56311 | -45.21665 | 2025-07-22 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 98ab1bc9-5d28-3d1f-8df9-5bd43a005984 | -6.97167 | -42.79925 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e61573e8-e713-3cee-ae5a-cfe6370013f7 | -8.11942 | -42.94305 | 2025-07-22 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2b6a0de-0090-3d80-ab22-32a2b8ec0537 | -7.19032 | -44.14112 | 2025-07-22 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9df52316-315c-3be8-8871-2404612474a9 | -7.62507 | -39.24646 | 2025-07-22 04:00:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1e4c997f-ca6d-3925-a454-4ee787a058e9 | -3.42333 | -43.16714 | 2025-07-22 04:00:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5553a6-fbf9-31b9-b228-7fb0f3fc2463 | -7.12424 | -43.33264 | 2025-07-22 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cfde8e0f-03ca-3c2a-bb80-040f569cf928 | -5.56373 | -45.21298 | 2025-07-22 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b421fb4-624e-3d0d-b079-41c482c319b9 | -7.28651 | -44.35852 | 2025-07-22 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f306bf4-248f-34f0-811a-22cbf5cbd4b1 | -6.1999 | -44.3873 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e3d8e20-8a66-3e45-bc3d-309fa14db832 | -8.01253 | -43.33005 | 2025-07-22 04:00:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 09dd1504-608a-365e-8b2b-c3c444e4d29d | -6.18909 | -44.40496 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 265741e2-f7c2-35a7-bc6b-f0272b9f4ce6 | -4.54722 | -48.00815 | 2025-07-22 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72208fbb-fa9d-391b-bc0f-39dfdcfc3d89 | -6.90008 | -42.79301 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8edeb74-7563-344e-b41a-e0cf7ac49a9a | -7.09059 | -49.17733 | 2025-07-22 04:00:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e240a6a-6967-3dfa-a7a2-62191ba243d5 | -3.97818 | -47.88256 | 2025-07-22 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47e8648b-9937-34ab-abb9-7abbb22cdb8e | -3.35517 | -42.87006 | 2025-07-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c0e3268-4f30-3ab1-81b0-350be5959aa6 | -7.0865 | -49.16988 | 2025-07-22 04:00:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8494abc-0d5c-3bfb-9528-2910eb756fd8 | -2.91683 | -48.24323 | 2025-07-22 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac6ad201-0873-3854-a9b6-4821a3bdb8cf | -4.77841 | -45.34092 | 2025-07-22 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0a635e8-2ab7-31ae-846e-8027e5928006 | -6.89656 | -42.7925 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2b9f919-aa54-3adf-96f5-54ca53f7a12b | -4.3846 | -43.2917 | 2025-07-22 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3f7eb3e-ced1-3c7c-990b-76abdbf92738 | -6.97518 | -42.79982 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 216c528f-47e7-3339-8d63-bbaaf970fd8a | -5.67978 | -43.67209 | 2025-07-22 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bd35949-ef27-31b9-b8c3-e3a803c1a782 | -6.20374 | -44.38807 | 2025-07-22 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86814a8b-b7f2-3c81-ad56-3a3a22e58e82 | -6.32278 | -44.06069 | 2025-07-22 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7fc00d2-0a0a-39cc-962a-05ca4597d8c4 | -6.83819 | -42.73073 | 2025-07-22 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3546af11-d697-38f7-8b98-bd60d649ff20 | -5.67718 | -43.67339 | 2025-07-22 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7d25012-8fa9-37ae-be4a-9d42254a5dd5 | -2.54082 | -47.68911 | 2025-07-22 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a43272d4-ba54-332b-91b9-ef674bd2b8cd | -7.12065 | -43.33203 | 2025-07-22 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e8d7e81-df29-34c4-8dfc-8de933e18f6a | -6.1634 | -43.75524 | 2025-07-22 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c902d447-d76b-3aec-95aa-345c8b36d101 | -7.25637 | -44.30543 | 2025-07-22 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08f90675-83d6-30a1-a147-3a1d07ff83ac | -6.71503 | -38.96377 | 2025-07-22 04:00:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59961beb-07d5-3af7-a867-19199a3fa610 | -6.62244 | -42.33613 | 2025-07-22 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c44aedd9-dd03-3adb-8ced-6dc799ab0e2a | -6.73246 | -44.32962 | 2025-07-22 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 409672c4-7468-3b3d-bb04-54b534073db1 | -3.29232 | -42.53967 | 2025-07-22 04:00:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b864564-1c69-35e5-b280-e47684df6610 | -5.84332 | -48.15796 | 2025-07-22 04:00:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 810419df-d81d-3664-9843-8bef11774c8b | -6.87778 | -43.76107 | 2025-07-22 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4413c1fc-9e6e-3f2e-b818-06a3bc1421d9 | -7.94469 | -43.97483 | 2025-07-22 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2884998c-9e26-3a0c-a6ad-54b262881ade | -8.92374 | -44.45204 | 2025-07-22 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0713f618-9a40-3dc3-ac1b-0b58ac0f0ab6 | -15.15263 | -43.67675 | 2025-07-22 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.3 |
| eed64a74-546f-3762-8565-7d6eddbd28ad | -15.92046 | -42.61458 | 2025-07-22 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 90a4575b-fe56-3a5b-8eee-1229282a311e | -11.71809 | -47.77212 | 2025-07-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35fbd118-aee0-3323-b8aa-cc0c8200a4ef | -13.65702 | -45.72736 | 2025-07-22 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 938f0f75-b065-3f5a-a472-4f50c2095dff | -14.3896 | -47.75477 | 2025-07-22 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c138ccda-1e90-312e-a1a6-bf8afa4c53db | -9.59717 | -43.85018 | 2025-07-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 142ce53e-6bfd-37da-aabf-4dd92e83ee66 | -10.62626 | -45.23138 | 2025-07-22 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08290ac4-59bb-36d4-b8ba-025c000f9d55 | -8.46969 | -49.61594 | 2025-07-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b95ac15-fad1-3491-a467-deaf2ece5198 | -12.04871 | -44.26567 | 2025-07-22 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5ade4d7-69fa-305a-844f-c8612f6678e3 | -9.67757 | -49.89807 | 2025-07-22 04:02:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c7cedc0-6d49-32d4-b294-91ef18c5ad16 | -7.51325 | -49.44466 | 2025-07-22 04:02:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae8d1561-642b-3a97-9937-653fba982d52 | -14.76012 | -47.11443 | 2025-07-22 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
