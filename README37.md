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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3284532-472f-3dd0-bf46-07250253db3f | -11.11148 | -62.66145 | 2025-10-23 05:50:00 | NOAA-21 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22b3f6a1-dcb4-3ff4-b949-e67c0e6502a6 | -9.78771 | -67.95015 | 2025-10-23 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfbb3a03-7f0f-3689-9dcf-b4a276454b05 | -9.975 | -65.11485 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 512df5dd-8766-35e1-aa6d-b6e70e5307bd | -9.12243 | -65.93715 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f470200-38b9-3f1e-a832-1a8efa36c978 | -9.8547 | -65.1932 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b9f3797-a699-3239-a7e3-db966a92fd63 | -9.91058 | -67.3173 | 2025-10-23 05:50:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ff41c48-7b04-32aa-9fa8-5e5094300b7c | -12.13363 | -63.21031 | 2025-10-23 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9855c2e3-9054-3a3d-bb6b-b52f6dc68489 | -12.13216 | -62.971 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3cfd2ad0-1345-37cb-b576-0e22ff7599ef | -10.81638 | -68.35357 | 2025-10-23 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6be76ef6-58c4-3171-9ef0-8de2b448999d | -12.58276 | -62.9584 | 2025-10-23 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8a4e760-d3e5-39df-9734-07ca0a3054d0 | -3.01833 | -49.482 | 2025-10-23 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 47a19219-51bb-3f80-bcf2-1281daa5fa23 | -3.0126 | -49.4477 | 2025-10-23 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| aee5e45a-a162-3a4b-91dd-be9e9abceb66 | -2.87019 | -50.71223 | 2025-10-23 06:16:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 536f4668-efe0-350f-82d3-efde1b9780ef | -3.01967 | -49.47293 | 2025-10-23 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c0aea1b3-093e-3807-b8c6-d0c9781c65b2 | -2.56294 | -49.49548 | 2025-10-23 06:16:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b5c731d2-633b-35da-abeb-124e31b4bf7a | -3.04106 | -49.51297 | 2025-10-23 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa04a03e-22d1-3d6e-9ba1-678f1a3d83f7 | -3.04842 | -48.71112 | 2025-10-23 06:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 70c40ff3-ee8d-3c52-b341-b410cc978320 | -2.80106 | -51.34934 | 2025-10-23 06:16:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90ce74bf-c2cf-365f-ba53-ca9aedbef252 | -2.73135 | -48.29018 | 2025-10-23 06:16:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 705fd6b1-f1e9-3a1a-bfd9-70398ac1f279 | -3.02725 | -49.4833 | 2025-10-23 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ca478e22-922c-355a-9702-e0582c341abc | -2.85746 | -50.73714 | 2025-10-23 06:16:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9914fd96-d095-3714-9fa0-ceb96741fb80 | -2.92414 | -48.29974 | 2025-10-23 06:16:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 94f3001e-bc07-35cb-bf73-5792e8d71fc1 | -12.12991 | -62.96234 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 755341d4-98e1-3d67-96aa-85ab301ca18a | -6.85822 | -46.2867 | 2025-10-23 06:18:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bc477cdd-8270-3cd0-8597-f690f989a845 | -9.81081 | -68.80634 | 2025-10-23 06:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 291ad612-6b6d-34d4-a65a-8bd1376f1f43 | -6.59598 | -44.2117 | 2025-10-23 06:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| e2c1b52c-f606-367d-a566-411a86ad495b | -3.39758 | -51.49944 | 2025-10-23 06:18:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8e2778d9-5fa1-3619-93c8-8297ee0fb96c | -10.45998 | -68.46361 | 2025-10-23 06:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cba8afdf-cc2a-3263-9d8f-4346d075d00f | -12.37514 | -63.87068 | 2025-10-23 06:18:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57e31bdf-0519-30a5-81cc-92736c416600 | -7.07561 | -46.19054 | 2025-10-23 06:18:00 | AQUA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 26ba511c-3ce9-35c3-8816-fdc5bbd12167 | -3.69842 | -49.55989 | 2025-10-23 06:18:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c61cae1b-7c05-32f1-8526-098094a3f745 | -12.37514 | -63.87067 | 2025-10-23 06:18:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e31088ea-b177-3b78-a525-4305aa51a89d | -12.1271 | -62.96796 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19390f12-8034-3c5f-8fb8-efc895383370 | -12.13392 | -62.96383 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd85009e-fd26-3a6b-9c42-4a10189ad02a | -6.60294 | -44.21909 | 2025-10-23 06:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 891de770-7f2a-3a92-8b8e-4943569f7e8e | -12.10029 | -63.62367 | 2025-10-23 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bec8428-0538-3e9d-9a00-1073be472597 | -11.97055 | -63.91938 | 2025-10-23 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93369fa8-04d2-3fcf-b3cb-d44528f1a5b6 | -3.2202 | -49.36602 | 2025-10-23 06:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3ba5407c-4d15-3056-872a-ebb87d0a37a8 | -12.09429 | -63.62297 | 2025-10-23 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34c0bb0b-b36b-34dd-b10a-6d7367ec0399 | -12.12871 | -62.97219 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 913cb76e-c843-378c-80ae-079af2468cf4 | -12.1328 | -62.97367 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e087395-21e3-3a73-830e-60d122b5ce8b | -3.67736 | -47.63146 | 2025-10-23 06:18:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 02256d81-6de4-373e-ac7a-5f4f1230f4e6 | -4.45853 | -43.23621 | 2025-10-23 06:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c50579c4-a51c-3337-b906-acd2e62ed446 | -11.97643 | -63.92017 | 2025-10-23 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82b63041-73a6-36bc-9eea-e252300368ab | -9.11773 | -48.89388 | 2025-10-23 06:18:00 | AQUA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 939f6f90-291e-30e0-bc02-3354a5b0ed01 | -2.80412 | -54.37683 | 2025-10-23 06:18:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ddaa751e-4cdd-38b9-b57c-39694d5dde62 | -12.37462 | -63.87502 | 2025-10-23 06:18:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abbe2522-347f-3a39-87b0-4d0a30b979f8 | -12.12766 | -62.96302 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57f395fe-d5d8-3dc6-be91-939d3ff29fc1 | -10.73303 | -69.35485 | 2025-10-23 06:18:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adaad4d9-3882-3678-8e22-cde8e7b72c69 | -3.47444 | -50.06287 | 2025-10-23 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a56803f4-874c-32a6-846c-64258b64f716 | -12.1003 | -63.62367 | 2025-10-23 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e55289e-acc5-377d-b1f1-5790b748fbab | -10.45664 | -68.46451 | 2025-10-23 06:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0a24649-aa1c-3420-b4c6-7e5b16ac22c5 | -3.47311 | -50.07168 | 2025-10-23 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 78662055-b4cb-3477-8aec-a5f95f4c7a43 | -10.45998 | -68.46362 | 2025-10-23 06:18:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7128aaa-8675-32fa-abb4-4135965771bd | -3.47178 | -50.08051 | 2025-10-23 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2d36069a-b545-3b42-9377-84709ecbc59f | -12.13279 | -62.97367 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7d1c9be-c897-366d-b668-b4db09525379 | -3.22155 | -49.35688 | 2025-10-23 06:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9c15dbf8-574c-3903-a1d0-7c1f10b5f0a7 | -12.13336 | -62.96877 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9d4fefb-2be9-3879-894a-751cac689ef3 | -12.12931 | -62.96727 | 2025-10-23 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d880d3f0-d810-319c-ac7b-5e8d7035c26c | -10.4711 | -49.09641 | 2025-10-23 06:20:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cd8d426a-4f4c-3a4a-b332-1e3403928d41 | -11.99492 | -46.78434 | 2025-10-23 06:20:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 882406e0-178f-34b1-a8a6-8ac1058f7281 | -10.46955 | -49.10758 | 2025-10-23 06:20:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2ff52f63-223c-32fb-86ba-cb0b3552a0fb | -11.35291 | -49.79586 | 2025-10-23 06:20:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| b744e3fb-4892-3b31-ad79-b09381213e56 | -9.99327 | -49.14691 | 2025-10-23 06:20:00 | AQUA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ae9eb9b-26dd-3856-a4cf-8b9447a7be14 | -10.47266 | -49.08511 | 2025-10-23 06:20:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5b197935-3b2e-3a0a-9c17-88b9755b7a51 | -11.99718 | -46.76672 | 2025-10-23 06:20:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c78f771c-ce59-34bb-b668-b02d77b33770 | -10.46125 | -49.0949 | 2025-10-23 06:20:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8e81f22-d988-3b8b-95de-d9d8dda18855 | -11.35443 | -49.78524 | 2025-10-23 06:20:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 53d7b1f9-5c57-3d7a-93b5-054997f3687a | -10.45969 | -49.10617 | 2025-10-23 06:20:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6e0b28f1-e904-3514-8cb6-216e3a2481d5 | -10.90944 | -48.05911 | 2025-10-23 06:20:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 55284471-4020-3eb1-898f-3e93eee097dd | -10.90764 | -48.07234 | 2025-10-23 06:20:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 964258c3-d940-394b-bf01-cecba158dee7 | -10.89873 | -48.05772 | 2025-10-23 06:20:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eef56000-f12c-3412-b046-040929644ac3 | -17.59951 | -46.60671 | 2025-10-23 06:22:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 420b701c-6b5a-31b0-ab79-de120be11815 | -17.61291 | -46.6082 | 2025-10-23 06:22:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 88fce09d-585f-348a-8b23-064d681c7595 | -19.26079 | -49.35193 | 2025-10-23 06:22:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 6c763d63-ce7f-328b-8acc-6abbc737e211 | -10.45799 | -68.46848 | 2025-10-23 06:40:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4a36ced-e009-3c37-8157-dc5779d30f0a | -9.1174 | -65.359 | 2025-10-23 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 3c7d5888-3c4a-395d-a509-16dcd182e773 | -17.6167 | -46.614 | 2025-10-23 09:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 4bcd2358-429b-3171-bffc-195a797f3dcc | -17.5967 | -46.6182 | 2025-10-23 09:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 88ef4d2d-f781-34de-b3f1-e841276acba1 | -17.6167 | -46.614 | 2025-10-23 09:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 9c42a387-541a-3e02-af6d-0b10fcfc91f2 | -17.6167 | -46.614 | 2025-10-23 10:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 654a017d-07b2-34b4-b221-7ae6dccaa9c7 | -17.6167 | -46.614 | 2025-10-23 10:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 961df756-fba6-3c80-83c7-f308eb0543cb | -17.6167 | -46.614 | 2025-10-23 10:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 42e74d8d-153d-35cb-bc35-c886646b2147 | -17.6167 | -46.614 | 2025-10-23 10:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 142.3 |
| a80b2dc1-9046-3ae3-8e0d-81a14a1dec18 | -17.6161 | -46.6373 | 2025-10-23 10:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d07dcc22-acea-3093-9f71-371deba28f7e | -17.6167 | -46.614 | 2025-10-23 10:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 174.4 |
| bc518094-a19f-3fa3-aa33-1ca0041c424a | -17.6167 | -46.614 | 2025-10-23 10:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 3c590fc6-b8ab-3f62-acb5-7f0dfc5f5bab | -17.6167 | -46.614 | 2025-10-23 11:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 7de999b3-1f4f-3b86-96e7-203ca5c3da95 | -17.6555 | -46.6523 | 2025-10-23 11:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 8a44b3ab-7cdd-3eaa-a39f-ba12746eb4d1 | -17.6161 | -46.6373 | 2025-10-23 11:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 452d157a-75c1-3228-b2ca-f82dcf58b261 | -17.5967 | -46.6182 | 2025-10-23 11:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 09ad8c6a-fdb3-3330-b602-2cf27cd1174d | -17.6173 | -46.5906 | 2025-10-23 11:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 471032e7-1510-3fd5-b1fe-2794b42d7a2c | -17.6173 | -46.5906 | 2025-10-23 11:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c11c15f1-be73-3d51-a4f9-a5c9d7d46f4a | -17.6167 | -46.614 | 2025-10-23 11:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 193.5 |
| e21298fe-e400-3421-9ee6-8e3d098d4ce8 | -17.5967 | -46.6182 | 2025-10-23 11:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1eed2b89-be4b-3300-ba99-c621bcf36688 | -17.6167 | -46.614 | 2025-10-23 11:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 196.1 |
| a9b98dca-9a59-32b8-9e5f-9d3dcfc50b8b | -17.6555 | -46.6523 | 2025-10-23 11:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 689c0f64-060a-364b-b45b-969e4dbb0c88 | -17.5967 | -46.6182 | 2025-10-23 11:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 322f665f-a9f0-32be-8a1a-3255b5a316a3 | -17.6173 | -46.5906 | 2025-10-23 11:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 6c94aefe-bb2b-3a34-bfb3-16f2d338e710 | -17.5973 | -46.5948 | 2025-10-23 11:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 105.7 |


[Clique aqui para ver as próximas entradas](README38.md)
