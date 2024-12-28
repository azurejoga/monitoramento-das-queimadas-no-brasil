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
| 4f8cdf4c-1a61-385f-bdef-854cb0273af5 | -3.91165 | -46.8871 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72eb12b9-b9ee-306d-a7f2-8ee696764caf | -3.84245 | -46.6875 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8002eb1f-4548-33d1-aa1b-842c2caa3e65 | -3.91087 | -46.98197 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bd44698-a802-3938-9dcd-1c68db0b0796 | -5.24805 | -41.4185 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20be87f1-1ba7-3d25-8f9c-77ea25bf0049 | -6.39667 | -38.91113 | 2024-12-28 04:14:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a1dac26f-0900-371e-b4da-b1ff3a47d948 | -5.83673 | -44.02137 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b570e64-a598-3b3e-9b74-dfdffec25b87 | -3.97112 | -46.58455 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a1f9835-dbf6-373b-a5cf-8fdf1dba2014 | -3.71658 | -41.69701 | 2024-12-28 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 927e3fef-21ba-3910-9142-1e72d6bc77af | -5.24239 | -41.41025 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 509c0ae3-a8e9-3198-a202-db02ac866465 | -2.52104 | -51.85999 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79e14bea-41c3-31c0-9dcf-bada4aa92e00 | -2.4802 | -54.16482 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3096d556-b5fb-3ed1-8ccd-c2cc55b5f20d | -2.90774 | -54.49055 | 2024-12-28 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52ad0604-4957-3577-9778-cfbb4624cc65 | -4.57144 | -41.29414 | 2024-12-28 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 38c90e53-82eb-31e7-be7a-54267fd4c4ee | -3.89977 | -46.98681 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fbd17db7-76f4-3228-bcbf-174a5e230a9c | -3.19102 | -45.9928 | 2024-12-28 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04c91e7a-94b8-3418-b864-a3891cd3c17a | -5.86586 | -41.80286 | 2024-12-28 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| def240f0-516b-362d-a40f-a6750eec46e9 | -3.94326 | -46.76148 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| faf8f94d-01b3-3db8-9b92-6f3373126341 | -4.1113 | -46.68268 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d373fc4c-e85a-3790-9b9d-c992f109989c | -2.28971 | -45.57221 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceabc7f5-e6ee-328d-98fb-015ac2c6223d | -3.95747 | -46.67109 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8322d40f-612c-3b8c-96d0-6b984897ccbe | -3.99381 | -46.68918 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f61cd339-54b6-374f-a032-1548c373fc20 | -3.99685 | -46.6943 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7b115914-0a0d-37db-b429-b922341d504e | -3.87703 | -46.69077 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 23f103e2-447e-3cb6-93ff-7ac2c7a7e36d | -4.0547 | -47.03214 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ced238b-2fed-3c92-a42d-23aff44b05d0 | -3.75908 | -47.21836 | 2024-12-28 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cc06766-6168-3280-b0cc-a8e2cab6e6ac | -4.00823 | -46.71958 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 768a0613-35a2-357f-9942-054da5f57430 | -5.57501 | -46.12894 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 37956ea8-b4fd-303b-a77b-b5fe3280d5df | -3.20336 | -53.94457 | 2024-12-28 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 381d1a31-d2d1-3eb1-87b2-130362f3d814 | -3.81762 | -46.6976 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddd05636-9010-3bbb-8dc3-47dbc00cf0e7 | -4.04471 | -47.0451 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fddc2df9-a32a-3ce2-a6ca-6de8debaa261 | -6.50483 | -39.54836 | 2024-12-28 04:14:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e8d3102e-87e6-3207-abad-6c18a433e334 | -4.03645 | -46.78549 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 193bd91e-f2d0-32de-ad33-7466b6c1febb | -3.98396 | -46.67847 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd974a2a-1d45-3f18-833a-63d9a0a9bbae | -5.40198 | -42.95256 | 2024-12-28 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8f4a83e5-8494-3ac1-a602-afa55758f831 | -3.97221 | -46.89464 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38adc48f-e95f-3137-ab71-20f9f821119d | -2.48933 | -54.16823 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5dffb97f-8c17-3e9b-bed4-beaa9169cfaa | -4.05781 | -47.01301 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea6c0e68-325a-3919-880a-e03344167c23 | -3.83795 | -46.69144 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dcb06e1b-76e2-3817-8b8e-02e528b37c63 | -3.9674 | -46.68525 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7cd80491-257f-3bea-805e-919237b70012 | -3.90493 | -46.92947 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd21f558-55f2-3ad6-9c0f-0bb0eb99c510 | -5.31324 | -46.06905 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb4df8ad-fe77-313b-80e2-88d08d528325 | -5.90771 | -43.4845 | 2024-12-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b940705d-da1b-3ceb-b147-0bee4e351bc3 | -3.92946 | -46.62898 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faf75067-03ba-3028-88fa-fea828f18b56 | -5.64234 | -43.72253 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2b2c0bd-1b84-3fe1-96f0-e9eb58ed63b9 | -4.00897 | -46.71501 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f588cc4c-7ecb-3b32-94ca-2d1c12d60abe | -3.98932 | -46.69308 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8038c9a-c2ff-3671-8139-d0a180ac0078 | -6.76131 | -39.40784 | 2024-12-28 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1e2f5d4c-efc4-3020-9b0e-363cd6dd0a60 | -3.15293 | -39.77993 | 2024-12-28 04:14:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42c16358-52f7-334c-8c79-5cc44dddb35e | -1.71759 | -46.21038 | 2024-12-28 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a68c79ff-a254-3fea-82d0-1b7ddcb0a7cc | -3.96439 | -46.68003 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37ad6adc-5df9-3c31-a28d-5594dd4f697c | -6.40084 | -35.22425 | 2024-12-28 04:14:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fa3d25ae-7f90-3d84-b918-a77191e72158 | -3.84275 | -47.04724 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bb863c3-a3c1-35a3-be87-88b57389aed1 | -3.84173 | -46.69205 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a3bc2b0-7fac-3f5b-b743-198193fec096 | -3.81932 | -46.73568 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0708a12-9671-3ccd-8c23-0a3ea9188959 | -5.71123 | -43.26245 | 2024-12-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 871d00b5-cfc0-3874-9779-46ef191d304d | -3.90053 | -46.98199 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b77e402-499f-3947-b15b-639094787ff3 | -2.90553 | -54.49395 | 2024-12-28 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fa04ff42-c061-362c-b8a1-e3ce45848d79 | -5.53576 | -41.75989 | 2024-12-28 04:14:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d9e6c52-e145-3072-8def-fa7ec9912f60 | -5.2113 | -41.24221 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 37e01b23-2600-39b9-9225-45e9b306ed03 | -3.9308 | -46.98043 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a73ad14-dffe-39e8-916e-0ddd42d3f0b2 | -3.96359 | -46.68128 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12998471-e12f-3e63-9dd6-962bb30c6f8a | -5.21921 | -41.23595 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e454cb9d-0b59-3dcd-8434-d2b869073452 | -3.99611 | -46.69885 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e0d7159-33b6-3fd9-b90c-b2d765fb1441 | -3.96126 | -46.67156 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21ae384d-6849-3c1c-ab82-aa49ce69dc9e | -6.49406 | -41.78144 | 2024-12-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73ba1017-8427-311f-9c24-764d82481359 | -2.28404 | -45.59154 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6acd66a3-ecb0-34eb-9fcc-94f50958697e | -4.01504 | -46.55812 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24bb85f-f0a9-3062-aa24-692343c09c24 | -5.98009 | -41.69923 | 2024-12-28 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d03563d2-634c-3f34-a45d-1111f37afa04 | -5.4068 | -43.89973 | 2024-12-28 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c48bef3-65f3-3770-981d-5728d447f12e | -4.34069 | -46.49165 | 2024-12-28 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4296cf56-065a-3264-a935-115f983ac7a2 | -5.42664 | -44.83219 | 2024-12-28 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 79b5032c-a502-3846-a2e5-f600e7c8e091 | -4.07934 | -47.09974 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ae5533a-1c31-3a2b-a9b4-dc27b4d8ab22 | -4.53202 | -41.54846 | 2024-12-28 04:14:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 028f0974-8e21-3e78-a1f5-c9e8c5215361 | -7.26957 | -45.36803 | 2024-12-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c230eb22-80ee-332e-9061-eaf7824ce21a | -4.74023 | -44.64611 | 2024-12-28 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1ef4129-75fe-3406-a182-65968c9a0c5b | -3.99691 | -46.7178 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cab919ac-c137-3438-acf5-ca8ae7efedf0 | -2.52161 | -51.85653 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fc5ddd0-83bc-3ff4-83e3-54a7b1c721c4 | -3.86667 | -47.02141 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 925503dc-b19d-34cc-8520-c51e1edb4656 | -5.90381 | -40.77011 | 2024-12-28 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b7807db-4476-3a85-a0ca-397b10f31464 | -3.96363 | -46.6847 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86c72db8-11dc-3987-896b-1c90d6ec459e | -3.99308 | -46.69369 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| edc3332a-74c1-3bd6-b363-7cf19363cb9b | -5.57791 | -46.1337 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 78e7da45-84b4-3081-8d46-70869009051c | -3.96817 | -46.68058 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c66b0b53-f9c9-37eb-b040-5824cd9d99e0 | -1.36917 | -46.61561 | 2024-12-28 04:14:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73c9902b-0920-36a2-a59f-ba341281bba4 | -3.88508 | -46.9555 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea92e32e-c76d-38ba-abd7-2123afbe5a76 | -5.53241 | -41.75937 | 2024-12-28 04:14:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 361a4dab-3726-316d-9160-2c09a2f465e9 | -5.97727 | -41.69511 | 2024-12-28 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26cc46f8-3a7c-318e-828a-87c59f799306 | -2.72546 | -45.62237 | 2024-12-28 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fd21a64-7513-3352-8e2d-87df62ec8f43 | -3.56254 | -40.85172 | 2024-12-28 04:14:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f7b0d78-f042-3797-b2f9-22ee47244823 | -2.28647 | -45.59311 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c7e14a3a-4d01-32d1-b60e-2ad43ed88f5b | -3.84607 | -46.69073 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0b1dacb-49d0-367b-ae63-c2d9c51954d4 | -2.90688 | -54.49559 | 2024-12-28 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad469bd5-f74f-35a9-85c8-a9b5d7e488cf | -3.97118 | -46.68581 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25f1595a-8275-3846-a4fc-6ce779c76701 | -6.11714 | -43.94775 | 2024-12-28 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f225265f-39c6-30a7-9a0a-6a95a8ac9cfd | -4.01274 | -46.7156 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3398b831-dbda-3df4-8d51-c837a1118501 | -4.06844 | -46.73235 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 94031771-131e-34aa-9760-a1c6ac82ea23 | -3.9057 | -46.92464 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0f522db-9448-33cf-9c5f-4bf70a8d53c5 | -5.74111 | -44.42954 | 2024-12-28 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f1e606e-1997-3c8b-8b02-8bcade867597 | -4.74133 | -40.78527 | 2024-12-28 04:14:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c03c9e7b-7b2e-3f46-92a9-8d26d959005b | -3.95227 | -49.44707 | 2024-12-28 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README9.md)
