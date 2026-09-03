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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6e7cc1d-c95d-3a68-9327-bfbf609ab5a4 | -11.75462 | -50.4751 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 275aa69c-790d-3a9a-aa01-bec76ff3a7f8 | -10.99871 | -45.07759 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 40728ea4-8ad2-398d-8ef0-73c99e4a3296 | -18.76235 | -48.91091 | 2026-09-03 00:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ef13f24-e821-3269-81f0-aba6a7599cfd | -18.82557 | -47.60744 | 2026-09-03 00:05:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 8742d4f2-ac57-3a66-866a-9ac6b6aa694c | -12.09832 | -47.0715 | 2026-09-03 00:05:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 37288769-b468-36b8-84bc-06b523938f3e | -10.56853 | -47.7115 | 2026-09-03 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a825db69-b686-35bc-8a27-fae41163e35b | -18.84582 | -46.45456 | 2026-09-03 00:05:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b2fb0508-689c-35e4-9fcc-b0d9b9a3888f | -17.08204 | -56.84597 | 2026-09-03 00:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| c063aa03-b884-34ce-b5fd-728712c2ca38 | -12.41053 | -44.80709 | 2026-09-03 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| caac1b70-d859-3a99-872b-343e4458cbca | -10.22876 | -50.28807 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2a2c0f0f-27c4-36be-83b2-005ecb97a586 | -9.08931 | -47.819 | 2026-09-03 00:05:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f4c15020-2d9a-32fd-a869-a75db7f247a3 | -10.75654 | -48.97778 | 2026-09-03 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4ac15638-0459-339c-94dd-98e50859646c | -3.03598 | -48.41621 | 2026-09-03 00:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8043bdb8-8864-3fc7-833f-0b0bb593000d | -4.41516 | -55.7724 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b55dc4a6-148b-317e-b66d-f3db20fca670 | -6.25172 | -55.4315 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4e798c1f-edaa-35ab-a9be-a6ef79f3d7d0 | -4.97412 | -55.84098 | 2026-09-03 00:07:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c2be2bc5-96dd-31bc-acbe-e321e9c87306 | -8.26178 | -49.9269 | 2026-09-03 00:07:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 594a1396-099a-3f01-be88-cc04bd4d5b6c | -1.09213 | -48.05142 | 2026-09-03 00:07:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8a7d3e2f-79c7-30aa-864e-6a64644d6540 | -7.57373 | -57.70697 | 2026-09-03 00:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3d8c6106-6b92-3c26-9ad9-e33a52b64503 | -8.42844 | -54.69773 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 46cc7005-9ac4-3881-b948-e164313278c4 | -4.14004 | -51.07259 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f4f75bd0-88cb-38a1-9fa7-bbd5c30c6b77 | -6.26301 | -55.42985 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 3124339a-311c-3b9d-af5b-980e5b3e10c5 | -8.46896 | -54.66343 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| aacfa1e8-d3df-3de2-ada2-242bea9d3f44 | -4.91376 | -43.46737 | 2026-09-03 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 56bcf12c-9075-36b3-a263-d39c6942c370 | -7.83125 | -47.67923 | 2026-09-03 00:07:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 26a03860-027c-320a-b85b-d2e2f7d3552f | -3.24343 | -47.25797 | 2026-09-03 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f5a8b56d-352b-35e3-8dc7-0ac402ff90c5 | -8.43386 | -54.74114 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ac7c055d-4a65-3014-8ca6-1b60c258c4c4 | -4.14124 | -51.08135 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10e0554d-515f-367e-a057-53bb28607035 | -1.7942 | -47.95169 | 2026-09-03 00:07:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 32a981ab-79fc-36a8-be0a-0734aedbfcda | -6.07148 | -53.67092 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 052cadbe-6578-39f6-ac47-69c236221e81 | -6.36315 | -55.22464 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 16affe78-c38a-34e9-87fd-f48eca52f969 | -3.14055 | -60.63828 | 2026-09-03 00:07:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 6240f76f-2f19-3047-b5cf-d5f56db123ad | -6.07368 | -53.67565 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a62effd4-65a3-313a-b0c1-53b9b2b381fa | -5.95497 | -47.18881 | 2026-09-03 00:07:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c8707fbe-e409-3602-a8c4-986c92b27e24 | -5.58017 | -55.82034 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f7f553e4-a576-348e-a0af-c51eceb34960 | -8.45794 | -54.66487 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 5aa9e814-7174-3405-bc4d-655f296aa80d | -4.11646 | -51.0313 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 6b6ee2c5-06b0-3bb2-98dc-68c317032881 | -6.64261 | -52.95206 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1722e25e-3c58-3cb0-af14-960941df1df0 | -6.67214 | -58.75778 | 2026-09-03 00:07:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3d421045-17a4-3b63-b431-03ba4225343f | -6.62673 | -51.86283 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f9e6bb5f-2b0f-3e28-9d52-de6a09f2077b | -6.67565 | -58.78625 | 2026-09-03 00:07:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 7f9cafca-a38e-36dc-9da1-b7a0e50cdf21 | -6.36091 | -55.21592 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 22728e31-0998-3e50-9df5-ca70405ff583 | -6.36284 | -55.23041 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b8b38340-2b2d-318b-ba51-5ca3b6522e89 | -3.20641 | -61.22323 | 2026-09-03 00:07:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 474fe002-434d-3bd6-86b9-71f615ccaf3b | -3.38672 | -59.42803 | 2026-09-03 00:07:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 14782231-c968-3995-9887-c632d617e55c | -4.97634 | -55.84645 | 2026-09-03 00:07:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b9d4b82b-6149-308b-921d-c73c54cdb100 | -4.15003 | -51.08013 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| a8f0a225-07a8-3ffc-8770-e0f573db86fe | -8.43949 | -54.69629 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 29b532f1-04c9-3361-808d-6ef5a399d96b | -5.21318 | -60.05443 | 2026-09-03 00:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 90a8cc45-868b-3e70-9764-42973047183d | -3.63069 | -54.60037 | 2026-09-03 00:07:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| de84900a-c065-3ccd-8906-d14a2d3a7cf0 | -6.41354 | -58.28872 | 2026-09-03 00:07:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 1b8d3caa-5e64-3e7e-b747-a5adfa3572a7 | -4.97843 | -55.86192 | 2026-09-03 00:07:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c0a71941-fd1f-3228-83d4-ba7b6a45e973 | -1.09381 | -48.06337 | 2026-09-03 00:07:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| fa079592-070e-35b7-8d0c-13d4d2c15fd6 | -8.08001 | -49.62173 | 2026-09-03 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae30e470-9867-324d-ab54-e6d135e582de | -8.08875 | -50.96135 | 2026-09-03 00:07:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f8f1656e-c921-3d5d-907c-79f7ca5c9d3e | -8.43567 | -54.7556 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 5c5a9129-fa08-34a7-a987-bb29865fb90c | -6.14693 | -55.67705 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 945421ee-1495-3543-b275-50200c19e996 | -7.29392 | -49.80721 | 2026-09-03 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 586b9002-69f5-3eac-99a7-ec05d0bc772e | -6.67663 | -43.40263 | 2026-09-03 00:07:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6fb49746-06cc-3022-9de6-4fb6da250f7e | -5.95326 | -47.17705 | 2026-09-03 00:07:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f163739e-1845-3d48-9267-19993edadb45 | -3.21772 | -48.81483 | 2026-09-03 00:07:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2f56a35e-c589-35dd-9ef3-c1a85ed3c572 | -6.6186 | -55.25418 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 66d0ef81-b671-3c46-8a92-ec6de3411624 | -6.61665 | -55.2393 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 2c6a3145-833b-397f-8b6c-3b9659b3819e | -4.70616 | -56.06021 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1a19b6fd-b7f8-34f6-9ae9-d29f605e676d | -3.80475 | -49.11931 | 2026-09-03 00:07:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 88b931d2-70b7-3502-9c7a-c416cfcc1a55 | -1.53755 | -54.25846 | 2026-09-03 00:07:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f274fae3-3926-3b37-9aa8-dde899291bb3 | -1.1071 | -46.29291 | 2026-09-03 00:07:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| fbc16b11-1943-3f7f-a507-b7006600501b | -7.61232 | -57.62437 | 2026-09-03 00:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| e2b73486-0e06-3eee-b01f-33b1810accf4 | -4.90771 | -43.47367 | 2026-09-03 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 39c6c15c-4ee4-34da-9f4a-ffbe7261bfcc | -4.96487 | -55.84778 | 2026-09-03 00:07:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3a7059d0-15b8-3662-99b7-363949957190 | -6.43404 | -48.53453 | 2026-09-03 00:07:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ddbe5796-c209-357e-9879-5f0fb073842c | -3.64777 | -49.97015 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 673ee09f-fe41-3683-be2d-cb29d5cd30b6 | -6.08171 | -52.19376 | 2026-09-03 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2dc42a99-0dbb-3a93-a5ed-9966ba880888 | -4.96696 | -55.86335 | 2026-09-03 00:07:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8c2f690a-3858-38c6-ae29-5eebb70f3d25 | -5.86185 | -57.57073 | 2026-09-03 00:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 23d56c92-46eb-3f5f-a7dd-14160c394397 | -8.43207 | -54.72681 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 4ad42ccd-c146-3999-a490-085107486684 | -3.92572 | -49.05669 | 2026-09-03 00:07:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 1e259420-00b6-384b-b4bd-504911a4aa63 | -6.50414 | -53.61604 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7e9f8ac5-3455-39ab-bd2f-3b1678e29376 | -4.14882 | -51.07137 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| b7d07cc9-a0f6-3b78-96e7-630c340618ef | -3.82355 | -50.11363 | 2026-09-03 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 45427a9f-061f-30eb-9eed-bdf76d2a37f5 | -1.71464 | -47.08903 | 2026-09-03 00:07:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f5b4091f-e674-33e4-a3b4-ff70046c0759 | -3.93495 | -49.05531 | 2026-09-03 00:07:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b84d39a5-35ae-3f2e-81c2-48b67796cdbe | -8.08111 | -50.97158 | 2026-09-03 00:07:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3c8dcaa6-e7aa-3e48-a6e1-feb734dd3fba | -6.37055 | -58.29414 | 2026-09-03 00:07:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 82244bde-1aa5-3b39-b9ec-1ec2b5163bb4 | -5.93561 | -49.84124 | 2026-09-03 00:07:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b38b116d-776b-35ea-b316-2bdeeae0b838 | -1.84842 | -48.77332 | 2026-09-03 00:07:00 | TERRA_M-M | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb5744c9-1f79-38a9-bfc6-e5a137094610 | -5.76208 | -53.40094 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 36fc1d45-6c68-31ac-a46a-5f4063fa3757 | -6.15535 | -57.76014 | 2026-09-03 00:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 903962f0-8571-33e5-bf72-c21681879e99 | -7.41524 | -49.74138 | 2026-09-03 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f0b3750b-135d-3b74-8e17-bfe1f407f530 | -8.45974 | -54.67897 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 35575dc5-f73d-3a9d-bdd2-b4feefac0386 | -5.25389 | -60.18222 | 2026-09-03 00:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 0fbb1129-cde4-3f92-b2d7-eb7d8d16d0ac | -5.26329 | -60.18777 | 2026-09-03 00:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 7cbc2ac2-37ea-3bdf-93cc-3b12d4702a49 | -6.14426 | -55.67077 | 2026-09-03 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9617bc1b-6b5a-3ede-945b-7adfd5ce40ee | -8.12615 | -54.93933 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d4bdff2a-91dd-39d0-bb55-3acd523449f2 | -8.78102 | -54.58398 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 787f2631-1a93-3bc9-9d8d-607c18b2a3ac | -3.59358 | -55.38168 | 2026-09-03 00:07:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 13e3adfb-5d4f-3b91-9bda-7e1d3f1ea027 | -5.83119 | -47.04319 | 2026-09-03 00:07:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a3924113-0a45-35c5-b656-3e6081b8197d | -6.41979 | -58.30891 | 2026-09-03 00:07:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a1f50273-0cb4-350d-bd6d-e7a529db3b43 | -8.46713 | -54.64923 | 2026-09-03 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 97803df8-e6c2-3002-a8c0-5d32bc1218a9 | -4.97609 | -55.85648 | 2026-09-03 00:07:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |


[Clique aqui para ver as próximas entradas](README4.md)
