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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bca3ffc-a2a2-3c0c-b744-a891d6a3f860 | -8.8343 | -46.7694 | 2025-10-03 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 416dddb5-afe9-3667-b615-5c2801cc599b | -12.6131 | -46.9725 | 2025-10-03 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| c2f5eec2-50f7-3b0f-bd9a-029ac4798a4c | -9.9965 | -50.2034 | 2025-10-03 11:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| a7e2f176-7ba7-332e-80df-42e01195d3bf | -9.9962 | -50.2248 | 2025-10-03 11:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6f04ae40-28e8-36c3-8a03-d9332e900f0f | -9.9959 | -50.2462 | 2025-10-03 11:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| dd02eb2a-0c1e-328f-a3d8-6e06121409aa | -10.9673 | -51.0614 | 2025-10-03 11:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 2861118d-5dd7-31c4-8963-870b1b74a5b7 | -11.9155 | -46.3272 | 2025-10-03 11:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| ebb23fee-30c2-3eb8-943b-7b35a383aac8 | -12.5305 | -47.2988 | 2025-10-03 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 60f70b59-f140-3586-9c1a-85fba685c65f | -12.6131 | -46.9725 | 2025-10-03 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 075f8e7e-8b6c-35e5-84fc-22b5b8324321 | -9.9962 | -50.2248 | 2025-10-03 11:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ad969cd6-d85f-3dae-bd51-81c56dd8f943 | -11.9155 | -46.3272 | 2025-10-03 11:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 472b14b2-8a29-35aa-9a24-3276642a5039 | -12.5301 | -47.3213 | 2025-10-03 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5a29dff9-d399-3a60-99f2-1fe78359f291 | -12.6127 | -46.9951 | 2025-10-03 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e8c3cc22-d7fe-38d8-b664-9de09470aeed | -9.9182 | -43.7212 | 2025-10-03 11:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 6d28a77f-3a3e-3571-a5e8-4ca5994e5e8e | -10.0153 | -50.2016 | 2025-10-03 11:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8784895a-8ffb-3291-a8c6-d69342a7b707 | -11.9159 | -46.3044 | 2025-10-03 11:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c6f81838-2194-313e-9199-2517b3e335a1 | -8.8343 | -46.7694 | 2025-10-03 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 6b5c128b-540a-3b83-bfc4-a84c139c39e4 | -9.9965 | -50.2034 | 2025-10-03 11:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 170.7 |
| c2dbe323-e378-3831-8597-a778ebf5872e | -10.9673 | -51.0614 | 2025-10-03 11:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fe5e5e17-0335-3f11-b953-867b427e99de | -9.9959 | -50.2462 | 2025-10-03 11:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 07d99ef2-0025-3a45-81a4-a7b79aa0739a | -9.8991 | -43.7237 | 2025-10-03 11:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 38dfce28-0a51-3b9f-885e-7b3e40723563 | -12.6131 | -46.9725 | 2025-10-03 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 593cafd2-c030-3ac0-bf77-1f563e17a742 | -12.6127 | -46.9951 | 2025-10-03 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 418872ca-a492-3313-a3af-851c48399580 | -8.8343 | -46.7694 | 2025-10-03 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| aecb7be8-3b38-37e2-b0c4-bbb185019d36 | -9.9959 | -50.2462 | 2025-10-03 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 220ee52b-6d01-36bb-b533-7d1a42aa41db | -9.9182 | -43.7212 | 2025-10-03 11:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 928f4498-245e-37bd-81b4-a879fe9fb9a3 | -10.9673 | -51.0614 | 2025-10-03 11:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 7b53f6c6-0f5e-304c-b0ca-6c026237679a | -9.9965 | -50.2034 | 2025-10-03 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 6f503853-23f8-392b-a2af-9e24c2383762 | -9.9962 | -50.2248 | 2025-10-03 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 14210f89-95a3-38d0-8def-d854e9a67514 | -11.9155 | -46.3272 | 2025-10-03 11:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 162.6 |
| af4a583a-1f67-3c91-a3e2-00902e627130 | -8.9118 | -46.6052 | 2025-10-03 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 11186fb3-8b0b-3303-808d-1690d65b5fba | -9.9182 | -43.7212 | 2025-10-03 11:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| ae75d498-3d04-308b-97e0-838d9bf4f33d | -12.6131 | -46.9725 | 2025-10-03 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 2acd66b3-8f3b-3d52-860d-2ccfefc28fee | -12.6135 | -46.9499 | 2025-10-03 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5773b995-7b35-3b70-b143-751b8acc555d | -9.9965 | -50.2034 | 2025-10-03 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 96c7bddc-e9f3-3a95-abcd-52556e368c16 | -12.6323 | -46.9697 | 2025-10-03 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 77564b1d-6e2c-3cbe-93b2-138a130e08db | -8.8343 | -46.7694 | 2025-10-03 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| dc5197b4-5bbb-3cf7-bb46-279bde900f44 | -9.9962 | -50.2248 | 2025-10-03 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| ea62da4c-ec71-3e34-8713-ffbfa911d714 | -12.6127 | -46.9951 | 2025-10-03 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 960d21cd-77f9-3d97-a8d6-a98d819dd17c | -9.9959 | -50.2462 | 2025-10-03 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 148.3 |
| de81d0e1-b5dc-38d1-9807-684b43fd2e2e | -11.9155 | -46.3272 | 2025-10-03 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 91179e08-4763-301d-afd4-7d7ad2b3302c | -12.6516 | -46.9669 | 2025-10-03 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f6436e05-6f6c-3461-a002-19ee40167b08 | -4.95043 | -37.71436 | 2025-10-03 11:36:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f70f5d90-02a0-396b-978d-5c718c4e6ed8 | -5.15291 | -37.59095 | 2025-10-03 11:36:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7867e087-5cbe-3b5c-b789-19308b90c70a | -5.63456 | -43.91053 | 2025-10-03 11:36:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4cd41c9e-03b7-3ae4-8e88-5cec3b8f7984 | -5.77264 | -36.49133 | 2025-10-03 11:36:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 68c89ebc-d664-3cd2-8ff6-9b34aed75389 | -6.19946 | -37.43537 | 2025-10-03 11:36:00 | TERRA_M-M | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| bc764b52-e6b7-3b5a-94b0-7d649adade89 | -5.15162 | -37.59988 | 2025-10-03 11:36:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 70a92433-17e6-3560-b983-dfec7378731c | -3.59879 | -38.95464 | 2025-10-03 11:36:00 | TERRA_M-M | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e3f295b7-8426-395b-9115-b83950f1eba8 | -5.68894 | -42.70217 | 2025-10-03 11:36:00 | TERRA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| ae72411a-dc6b-38ed-8d07-be9ccb369d3e | -6.0534 | -41.23769 | 2025-10-03 11:36:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| a727d009-affd-3ba9-96c7-7ed4afeb7510 | -6.04983 | -41.23025 | 2025-10-03 11:36:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 07cb2905-7a52-3fbf-8e52-7359af106c8d | -6.07739 | -42.4919 | 2025-10-03 11:36:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| ee17ce3d-4372-3914-8c64-36ced1f51e51 | -4.63711 | -37.58124 | 2025-10-03 11:36:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| c6b5a267-e308-31e1-a790-54d1ccc727f2 | -5.79035 | -42.88557 | 2025-10-03 11:36:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| bd68ae0b-c1fe-3996-bd60-24a776d25250 | -5.39153 | -36.82779 | 2025-10-03 11:36:00 | TERRA_M-M | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| add99c88-b307-382b-aac7-364116104ec4 | -6.22154 | -36.57628 | 2025-10-03 11:36:00 | TERRA_M-M | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 8b18e4fd-d474-357f-a66d-af64cfed0936 | -6.55241 | -36.51366 | 2025-10-03 11:36:00 | TERRA_M-M | CARNAÚBA DOS DANTAS | RIO GRANDE DO NORTE | Brasil | 2402402 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 677beed7-03f6-3d0f-b731-b853f536564b | -8.59004 | -44.79537 | 2025-10-03 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| e13c74da-34af-3245-8c43-63f66e7ce709 | -9.91583 | -43.73063 | 2025-10-03 11:38:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 87ad2ff0-0aa5-338e-bac4-4f2bb835c88f | -7.91055 | -43.53154 | 2025-10-03 11:38:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b74a00b1-4f13-3e1c-85b1-0e0864d189cf | -9.03238 | -40.25466 | 2025-10-03 11:38:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| cb5b3843-f3a6-3f37-914e-ca72eb3b1ead | -10.17892 | -45.49303 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9f0574d2-7111-3dc8-86cc-bb8db1bb7505 | -11.92251 | -46.30978 | 2025-10-03 11:38:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 71c44f58-53ed-31a3-810c-60ec64483c65 | -10.17418 | -45.48484 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 710c58b8-838b-3682-b7af-c3531ccf0be1 | -11.14374 | -47.1875 | 2025-10-03 11:38:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| c9255ef9-a68e-36b1-9a00-8eeac58f3467 | -7.40128 | -37.47868 | 2025-10-03 11:38:00 | TERRA_M-M | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1f1d501e-7543-35b1-8381-1384de113fd7 | -11.14184 | -43.39204 | 2025-10-03 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| ea5e0cad-0d27-31b3-ad8c-41c9daa88ea8 | -7.74726 | -42.56495 | 2025-10-03 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 412.4 |
| b6962c17-d7cd-37c3-9e97-4ca47cc6d316 | -11.88585 | -43.27718 | 2025-10-03 11:38:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 86e97157-84a5-3e47-b139-6b9962ac8ee6 | -8.39211 | -38.09321 | 2025-10-03 11:38:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| be8950cf-e550-3dbb-bc69-2c952c431ce4 | -9.90365 | -43.72885 | 2025-10-03 11:38:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 35.8 |
| b7d9b5ff-ad6b-3961-8f8f-aa92352ef840 | -7.52626 | -37.43925 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e871dc5b-cbb1-35f7-9e6e-8ab9192a3c97 | -10.95868 | -41.74684 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 43b9cd22-46dc-384e-987b-167b87869d4a | -11.42649 | -43.49022 | 2025-10-03 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7af1a3bd-f13f-3df7-8c57-4bf68ff6a934 | -9.90649 | -43.71078 | 2025-10-03 11:38:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| dcc149e8-813c-3f35-b2f7-9b89fc20895b | -10.22767 | -48.24157 | 2025-10-03 11:38:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7e610a66-956a-3008-b9cf-d480d49226e6 | -11.46399 | -45.13573 | 2025-10-03 11:38:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| dbceb306-92d5-39c4-a997-c45d77e6d8ff | -7.75618 | -46.26029 | 2025-10-03 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| c1e79d14-fa15-34fd-8bea-08df42751156 | -7.74966 | -42.54949 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| bc683b7a-3226-33ec-80ad-a1b8ca2d85ea | -12.29575 | -45.36023 | 2025-10-03 11:38:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 5dad0132-6441-316c-8192-ebb223f1aa01 | -7.76597 | -42.52012 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 438.4 |
| 50b352e3-202a-38f1-802e-e2440c3fe3cb | -10.16177 | -40.23382 | 2025-10-03 11:38:00 | TERRA_M-M | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 608b4ca0-ab15-3d0d-af36-bdf3d9088cb2 | -7.75189 | -46.26529 | 2025-10-03 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| c81270d8-baa1-3614-b581-65ca77487377 | -8.18082 | -44.15892 | 2025-10-03 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1ec0c4ec-a8c9-364f-8275-3c85dddcdc29 | -7.77629 | -42.59162 | 2025-10-03 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 88f9f01e-298b-3c36-beb5-33075e4080c5 | -11.6574 | -41.46822 | 2025-10-03 11:38:00 | TERRA_M-M | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| b187d308-4d76-3b77-bda9-0a85ae663339 | -7.3072 | -45.25463 | 2025-10-03 11:38:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| d891f3f1-bed9-3cf1-8073-a8e0c5a50df8 | -9.91012 | -43.71844 | 2025-10-03 11:38:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 153.2 |
| 20507a77-b77c-3320-a389-25e814fd241e | -8.17833 | -44.16534 | 2025-10-03 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 00e91d35-83c5-3482-a008-413a3eda95d9 | -11.14443 | -43.37571 | 2025-10-03 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 10d5487e-1fc8-3f1f-bf91-5d513df78e7b | -11.8834 | -43.29248 | 2025-10-03 11:38:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 8b790054-ee49-3671-a763-c5cb2c2308b8 | -7.77942 | -42.58598 | 2025-10-03 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 7772eb97-8317-37c4-84af-8e9457466f42 | -7.76703 | -46.26968 | 2025-10-03 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4fa6ab7b-aada-35d3-8bb0-15a3d231caa4 | -7.76116 | -42.55127 | 2025-10-03 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 42683cd1-f71d-3678-b60f-be498618baf9 | -6.58472 | -43.44915 | 2025-10-03 11:38:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 41002664-04c2-3223-b664-d63c98cf27f1 | -11.45087 | -45.13306 | 2025-10-03 11:38:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 31350c03-a600-3b99-9727-1a5f72760641 | -7.75671 | -46.23667 | 2025-10-03 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0553f618-18c7-37a7-bb97-51a66835c00b | -9.91863 | -43.7127 | 2025-10-03 11:38:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 7aa20757-4c9c-3c42-a5d2-e67f89378413 | -10.94744 | -46.72629 | 2025-10-03 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |


[Clique aqui para ver as próximas entradas](README142.md)
