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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14e5853c-f3ef-3bcf-b916-e99cb8732cc5 | -9.5179 | -60.5461 | 2025-08-17 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d9de5b3e-7d6b-3555-b8bf-15ce040ee4e5 | -8.9788 | -60.4964 | 2025-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d869c23e-1075-3037-9933-63f7c476c293 | -9.1894 | -59.6558 | 2025-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c08f1088-04e8-323b-b91e-3b353b9c3f15 | -9.2082 | -59.6354 | 2025-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6c52daac-2325-320c-a8f0-cd98a7b6d003 | -6.545 | -43.0373 | 2025-08-17 01:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f6f39fcc-b2a2-39fb-a96d-ff193f0ce7b4 | -13.0128 | -42.3077 | 2025-08-17 01:50:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 53206984-39ba-3702-ae12-a12068947355 | -9.4992 | -60.547 | 2025-08-17 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6a55be28-b699-35cc-b334-9b31de43ad33 | -8.9974 | -60.4955 | 2025-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d4909c29-f809-31c1-8564-caa37d438259 | -14.9248 | -54.6982 | 2025-08-17 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 68247384-854c-3256-b857-02197890e69d | -9.1895 | -59.6364 | 2025-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d82034dd-9a74-3f80-99a5-17be2ef1677c | -9.518 | -60.5268 | 2025-08-17 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7b30817b-2ba2-3f46-8fd3-5087d86db965 | -13.0122 | -42.3321 | 2025-08-17 01:50:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 277b930f-9853-3a43-88f1-91a7eb0a5fd6 | -14.9445 | -54.6751 | 2025-08-17 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7c237c3c-139f-358a-ad70-4626b46a84f3 | -9.1709 | -59.6374 | 2025-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 2d95a5fc-d9f5-381a-b5c4-244799821497 | -8.9787 | -60.5156 | 2025-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| bc207a3a-cc0c-3520-9a89-6a2a5c58e6ae | -9.4994 | -60.5278 | 2025-08-17 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fda79192-8ffb-3ddf-bb53-6e01cccb1050 | -13.0317 | -42.3285 | 2025-08-17 01:50:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 1908247b-c038-32ca-8941-e377c460f904 | -14.9251 | -54.6774 | 2025-08-17 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ac443a37-f880-3049-a58e-8853e22e1cfd | -10.8444 | -45.3126 | 2025-08-17 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8c568bc6-b601-349b-9743-e65f47e7f88e | -8.9893 | -61.7024 | 2025-08-17 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5aad1ab0-db06-3fee-8e88-bbf618b5e5c4 | -10.8444 | -45.3126 | 2025-08-17 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5c1a6e7b-f9df-36ee-8d44-a79b23b28cee | -9.518 | -60.5268 | 2025-08-17 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| f6b50fc6-437e-391b-ab88-0bb9c2d3199f | -13.0122 | -42.3321 | 2025-08-17 02:00:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 181.2 |
| a06c05fc-3a9f-322e-9ddd-fe048b8f8ee5 | -9.1894 | -59.6558 | 2025-08-17 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a3924bb9-3516-3be7-884a-ce8b9ba9f484 | -12.898 | -46.1135 | 2025-08-17 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 386b7408-7dda-3913-b97d-a7d9bc56b1ee | -7.9253 | -63.242 | 2025-08-17 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| cc2946c4-5de8-33ba-b8cf-5d4de3229304 | -8.9974 | -60.4955 | 2025-08-17 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 654c95ce-e295-3877-99ac-a8ebd9973983 | -9.5179 | -60.5461 | 2025-08-17 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| a7b9bd23-af43-35d4-be37-6c970dfe8332 | -8.9788 | -60.4964 | 2025-08-17 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| a60a929b-3daf-3547-9578-47da0a386299 | -9.1895 | -59.6364 | 2025-08-17 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ccef33bf-6874-3496-acf1-dba936d4058b | -14.9251 | -54.6774 | 2025-08-17 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4aa523ae-9d53-32c6-ad0c-73cff46e921c | -8.9787 | -60.5156 | 2025-08-17 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| cdd25f52-0ef2-33b5-bf00-7f04bbfde9e2 | -13.0128 | -42.3077 | 2025-08-17 02:00:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 113.9 |
| f52fd52a-8b78-3e9f-a09b-5924d3cc221e | -14.9445 | -54.6751 | 2025-08-17 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b8d35cb5-f717-3e14-a3ff-b0e1248479b3 | -10.8253 | -45.3152 | 2025-08-17 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a62e6f3e-f2d5-3385-820c-d476bf4cd6fa | -6.545 | -43.0373 | 2025-08-17 02:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8598ab28-e181-3bc8-82de-f56d99151dba | -13.0128 | -42.3077 | 2025-08-17 02:10:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 70.6 |
| d8cff146-a46b-38c6-a5c3-c98c89810ff7 | -7.9253 | -63.242 | 2025-08-17 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| ba56bc11-2edc-30e1-948f-b4448134a6bf | -10.8253 | -45.3152 | 2025-08-17 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f7cfed36-40e9-35ef-82e6-f666cfe07a58 | -4.9118 | -43.257 | 2025-08-17 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f8909503-cebd-38ce-b7c0-22cd0d25e87d | -13.0317 | -42.3285 | 2025-08-17 02:10:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 9a736c7d-74cf-3bdc-83bd-4107a3a6a8b6 | -9.5179 | -60.5461 | 2025-08-17 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 12b9bcd5-d050-3b9d-832d-14410a9dac08 | -7.9068 | -63.2615 | 2025-08-17 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7c8ddaf7-0dfe-3563-9d22-d772913803b6 | -7.9437 | -63.2602 | 2025-08-17 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9db2a01e-013d-3c36-b067-6d7479c22124 | -8.9787 | -60.5156 | 2025-08-17 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 75cd2fe7-9f4c-3fd1-9e39-47de38137704 | -12.898 | -46.1135 | 2025-08-17 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| a653fdd6-674e-3390-a12f-ae104a95bdaa | -9.518 | -60.5268 | 2025-08-17 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 532bec14-cf26-3221-9d7e-4e89cebb9a58 | -10.844 | -45.3356 | 2025-08-17 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f95cd023-8b2e-3d2d-bb2b-39227b8ca78e | -9.4994 | -60.5278 | 2025-08-17 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 349ada77-e99c-33db-bd99-922abf7c2bf0 | -13.0122 | -42.3321 | 2025-08-17 02:10:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 27d3234e-3e66-38c2-89da-6e9856f65ea7 | -6.545 | -43.0373 | 2025-08-17 02:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 91410272-973e-3f67-adeb-8ebf710d5b2f | -14.9248 | -54.6982 | 2025-08-17 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b186903c-2126-3032-a775-fbba542af93b | -7.9252 | -63.2608 | 2025-08-17 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 179.1 |
| c3d6f434-285c-3444-ba2d-9611497f4784 | -10.8249 | -45.3382 | 2025-08-17 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 63df1286-5376-37ed-987e-b4cbb684b79a | -4.9305 | -43.2558 | 2025-08-17 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| b6f50674-62be-3a5d-bdae-61d0d7fd0b88 | -8.9788 | -60.4964 | 2025-08-17 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 11f745b5-08b5-33e3-81aa-b2ee235645d5 | -8.9974 | -60.4955 | 2025-08-17 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a374cda0-bb9f-3fa3-9d80-f73b1202c216 | -14.9445 | -54.6751 | 2025-08-17 02:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 9c950c9f-0d02-367d-a33f-7b8a4b6e8246 | -14.9251 | -54.6774 | 2025-08-17 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 5ea1adc8-78e5-3e02-806c-a578e1575667 | -7.9069 | -63.2426 | 2025-08-17 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5f009d37-5577-349c-b87f-af7c01b5d1e0 | -14.9308 | -47.0564 | 2025-08-17 02:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| febc5214-0ef9-35c2-b186-99661e3953c1 | -9.4992 | -60.547 | 2025-08-17 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 05fb7386-7196-386e-aec1-740f8f88b0c6 | -8.8682 | -68.506104 | 2025-08-17 02:11:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55b32986-ff29-3366-8c5c-b47794394c78 | -8.9788 | -60.4964 | 2025-08-17 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 30206c3b-50f1-381b-bbca-14d437f91297 | -9.4994 | -60.5278 | 2025-08-17 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 05b04499-515d-3c57-a53c-08c69f44ca83 | -9.5179 | -60.5461 | 2025-08-17 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 301353dc-8a35-34d9-8f34-f5a01e2d73e7 | -4.9305 | -43.2558 | 2025-08-17 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 4fc25226-cb35-3c6b-97f0-5fe8e7a3bda7 | -8.9893 | -61.7024 | 2025-08-17 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| bf09ea66-100e-3fb4-a2d3-2038c6755c0f | -7.9437 | -63.2602 | 2025-08-17 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 7df6dde9-2033-3124-8fab-28a24bf4a1d1 | -14.9251 | -54.6774 | 2025-08-17 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 156268bb-3e95-38da-9a7a-12beb6f420af | -8.9974 | -60.4955 | 2025-08-17 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| bff243a1-5166-3362-ba6c-f46a9c55abe8 | -13.0122 | -42.3321 | 2025-08-17 02:20:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 34fe67cc-1a64-3f71-9705-761e95cb706a | -6.5453 | -43.0138 | 2025-08-17 02:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e813c750-5458-38b8-aff8-1ecddb90c669 | -7.9251 | -63.2796 | 2025-08-17 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 2b459202-8a9f-3305-91ae-70b33cb4bc3a | -7.9436 | -63.279 | 2025-08-17 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| af176400-7a9d-3cbb-9581-6f5e35c44286 | -6.545 | -43.0373 | 2025-08-17 02:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| fb4f806d-db27-3603-8a6a-66e1149677ff | -13.0317 | -42.3285 | 2025-08-17 02:20:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 72.2 |
| c0052388-75a8-3303-83b7-a5056e30221d | -9.4992 | -60.547 | 2025-08-17 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 56f16c4c-92e4-3868-9e8c-2c8a55c1db0d | -8.9709 | -61.6842 | 2025-08-17 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| aeac78bb-ea47-3f5f-8953-6622c5bb7535 | -9.518 | -60.5268 | 2025-08-17 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 36a3f12c-3f15-3ffb-81a6-c9fcd934ec31 | -7.9252 | -63.2608 | 2025-08-17 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| d7bf0823-10c9-333e-9862-9611e602e6eb | -4.9118 | -43.257 | 2025-08-17 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 335f709d-5d74-34f7-a41a-e4825c8637d5 | -13.0128 | -42.3077 | 2025-08-17 02:20:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 67.5 |
| a5da3377-fc1c-3e0b-9b6f-e3d19b6d0cc8 | -9.4994 | -60.5278 | 2025-08-17 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8c2d2951-8891-3f2b-9611-f4252496fa0d | -9.5179 | -60.5461 | 2025-08-17 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d1ac13ff-16e6-3d26-9f29-695ebc3df8e4 | -13.0122 | -42.3321 | 2025-08-17 02:30:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 1aac7722-6588-34bd-a81f-e61c6137256f | -9.4992 | -60.547 | 2025-08-17 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4d9bad41-2e5d-3f3f-a72e-db04c567b916 | -14.9251 | -54.6774 | 2025-08-17 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 043aba2e-222b-3cd1-8ddc-a060fa6f0301 | -9.518 | -60.5268 | 2025-08-17 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 816c922a-44c6-3e6e-866a-2b24ea481256 | -10.8253 | -45.3152 | 2025-08-17 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 81f51341-8a3b-356b-bf59-ff791cd5344c | -6.545 | -43.0373 | 2025-08-17 02:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5bce4bfb-1bdf-3a67-bd9e-cf6f87f00baa | -8.9788 | -60.4964 | 2025-08-17 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 8fc69a45-6577-3373-9a22-a2ff87947d74 | -8.9787 | -60.5156 | 2025-08-17 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b539cc37-9ade-388d-b3c0-21b74d90820f | -13.0317 | -42.3285 | 2025-08-17 02:30:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 67.7 |
| d6740f8c-c35b-310f-a3ac-4aa7c3884426 | -10.844 | -45.3356 | 2025-08-17 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1bc35b89-7e5b-3292-a6af-fd66cee08c1e | -10.8249 | -45.3382 | 2025-08-17 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 64632134-0315-3042-94c5-d0deb507bdb6 | -4.9118 | -43.257 | 2025-08-17 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4fc36216-f5ad-3656-aabd-ffa7eafa2512 | -8.9974 | -60.4955 | 2025-08-17 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| ddda37da-33d5-369e-8ed4-92215de472dc | -4.9305 | -43.2558 | 2025-08-17 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2f8bbc1f-aafd-3bd2-a092-5ec3f3c75798 | -14.9251 | -54.6774 | 2025-08-17 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |


[Clique aqui para ver as próximas entradas](README8.md)
