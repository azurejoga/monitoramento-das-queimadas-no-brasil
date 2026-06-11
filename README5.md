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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c80ed62-ad7c-392f-83e3-47da019afdc9 | -9.32567 | -45.48896 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6ee39ff0-1dd2-34fc-ab38-2757c225a75d | -9.13847 | -47.98127 | 2026-06-11 04:12:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc69697d-1213-322a-b4da-41320c4793ef | -12.15004 | -48.45254 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b66c9cc-3580-369a-a94e-71bed1188d06 | -8.98617 | -48.09004 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a427f099-3bcb-3d5e-bade-5a4cff9796fc | -11.98164 | -47.38686 | 2026-06-11 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5792af07-8369-3c11-8d06-7f541ef33383 | -9.30462 | -45.46956 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24de2c71-0a59-3054-b7c3-6bc973f70dcd | -7.62529 | -50.04411 | 2026-06-11 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e044656-f815-32ec-a2db-3aaff164f542 | -8.31811 | -43.81441 | 2026-06-11 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d11daa03-02e1-3de9-bca6-62af05a9e0e7 | -8.51022 | -47.02103 | 2026-06-11 04:12:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8073d6f-ae93-39c1-b706-e52a582314c9 | -9.74876 | -47.88121 | 2026-06-11 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 858f3383-f485-3638-bea7-a6377a5f8737 | -12.36881 | -47.89016 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 99f340d8-ef58-34f5-86b2-6e4db28c187a | -13.36427 | -43.20468 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| aef171a3-0c68-39b0-9953-8e6191501653 | -7.91068 | -47.07268 | 2026-06-11 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c61d233-396b-317f-a8e4-7a509015763d | -9.11055 | -50.91728 | 2026-06-11 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69767278-0bd8-3ecb-b1e6-412a45ef0671 | -9.53103 | -47.75882 | 2026-06-11 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dfbb6fc-9e69-363c-81d9-a72264a0f045 | -12.15091 | -48.4478 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b3cf2d9-9916-30d1-8760-1057db74c4d7 | -10.98687 | -46.75298 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42871f18-b9ed-3068-9f5f-d69a7be09b6f | -12.05286 | -45.29671 | 2026-06-11 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f636c908-ce5b-368a-b898-002fcd488525 | -9.32259 | -45.48321 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e0b7cc5e-9449-36f8-9cc2-6228ec43d1cb | -9.21726 | -48.57855 | 2026-06-11 04:12:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 414919e2-1a57-313d-bda5-a10e70176bf9 | -11.57809 | -47.44705 | 2026-06-11 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa60779f-aecc-36f2-9ed3-944204dcd9e9 | -10.85016 | -46.78971 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 655d9a83-580b-33c5-bc6b-c49a0995ba18 | -12.03362 | -41.38354 | 2026-06-11 04:12:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96ff025f-70d9-3210-9f1b-2f54f4addad1 | -12.85559 | -44.37534 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9d038fc-6a15-3e85-ace3-4495c354fc25 | -12.85914 | -44.37596 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 247a4ed3-d9cd-30be-9941-b1b30dfddbb4 | -11.87255 | -47.10345 | 2026-06-11 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fde00251-6982-3a85-a9ca-08a09032271d | -12.14289 | -48.4659 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69da40f1-f93b-3d39-ac02-a34e4bdfc0f4 | -10.87985 | -49.54187 | 2026-06-11 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4736ac4-75f4-31ad-ae87-fb2d277ffbf6 | -11.58168 | -47.45196 | 2026-06-11 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d52247f5-f25c-3309-99ac-111d3a6d973d | -13.68252 | -44.29037 | 2026-06-11 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61b64821-3d4a-3d87-9e92-e8e1fc0ee827 | -11.80226 | -48.80061 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e610de2e-e030-3ae7-83a5-b7fc18a62f11 | -9.2081 | -47.91412 | 2026-06-11 04:12:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1988bd4-84ac-3cb9-8515-1925e320e558 | -9.32173 | -45.48826 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 964d899f-4a0f-390e-9fc0-85e747491e11 | -7.72476 | -44.16187 | 2026-06-11 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fab541f-8d95-36a8-88af-081cd941c729 | -13.36965 | -42.42246 | 2026-06-11 04:12:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| abe8db06-466b-3256-8170-bcf7131f70c1 | -12.04536 | -45.29541 | 2026-06-11 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 195fc7b9-e051-34de-9528-89eebef5f7c9 | -11.10873 | -49.09373 | 2026-06-11 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaa705e3-e245-3ccc-874e-1023c2a33cbb | -12.01412 | -49.27576 | 2026-06-11 04:12:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45ce9f5c-a53b-3d65-814c-6f74ffea4ebe | -7.881 | -47.10228 | 2026-06-11 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4772d657-7399-333f-a853-9e998ebdec47 | -9.30376 | -45.4746 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13f6e5fd-ef9f-3cf0-8f91-506e2d7b1209 | -10.38184 | -46.62424 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 382ec088-01d3-3aa1-a2aa-e76084cd8717 | -12.31076 | -47.91025 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c7d915c-5eec-32f6-9c80-b9abea2bef24 | -7.34672 | -47.01785 | 2026-06-11 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac0ee460-5c08-3073-86ae-29677f66e9d6 | -12.30121 | -47.91282 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efc894f3-5ffb-3f30-943b-d9402c108879 | -7.34965 | -49.85038 | 2026-06-11 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4c8793-48c0-31f8-811b-004ca7bd94a8 | -12.85628 | -44.37127 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5834dcd5-1318-3a78-9020-0e93179ae478 | -10.84664 | -46.78517 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aa14da9-c7d7-381e-be0d-98a547bf7c2d | -7.59925 | -46.45985 | 2026-06-11 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d02f1b0f-c8f9-325c-a532-7849b3f1cb7d | -9.13758 | -47.98621 | 2026-06-11 04:12:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c556f4-7fde-3d81-b998-df775ffe33e8 | -12.64059 | -43.43697 | 2026-06-11 04:12:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47fe14a8-68ca-3f60-b6d1-6b8b0d6bd17a | -8.66333 | -46.60554 | 2026-06-11 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a92b90f-8f0c-371b-871f-b99804a63b8a | -11.10772 | -49.09912 | 2026-06-11 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1be27be1-3289-3cdc-a117-31f65df51019 | -8.51463 | -47.02182 | 2026-06-11 04:12:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aaf5dc12-c092-3f66-8286-db7617a47372 | -11.78305 | -41.19445 | 2026-06-11 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 32a12b5c-7579-369b-a0b3-bb8c5a17b188 | -10.93362 | -44.67091 | 2026-06-11 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 590419ba-17e1-3440-9fbd-eaa4446ee5e8 | -11.01603 | -46.75803 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 587d462e-e874-3010-827a-38b15ec9914c | -9.21273 | -47.91499 | 2026-06-11 04:12:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70a4af9b-a81e-3449-b216-031547c70fe2 | -12.85845 | -44.38003 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fe80a04-aff9-30e5-bec9-a6fcd5135828 | -12.14462 | -48.45641 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c204bd7b-6e63-3985-8d5a-839e98a06ef1 | -12.85777 | -44.3841 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b4cf29b-7273-301c-8e5b-34fa183043a0 | -9.31865 | -45.48251 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 54f698f0-00ed-35b2-a27c-4d08d15e0646 | -9.21187 | -47.91986 | 2026-06-11 04:12:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e96446e-f317-35e7-af9c-c2503fa1e199 | -12.01146 | -49.27776 | 2026-06-11 04:12:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b235c88-f43c-332c-9013-b900e4ff6fd9 | -12.36367 | -47.89357 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 744a4949-7a2b-32c0-906a-beedd86e01de | -11.97738 | -47.38603 | 2026-06-11 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6c3b11b-a92f-3390-b719-cbaa73ee4de4 | -7.90619 | -47.072 | 2026-06-11 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c56a5290-19a1-3fd3-a643-5883ab1766db | -9.21143 | -48.58315 | 2026-06-11 04:12:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ae12e16-39cf-3175-97f2-df58b19940a4 | -7.8765 | -47.1016 | 2026-06-11 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4751b1f-8337-3599-95ab-8c672796e85a | -12.03306 | -41.38707 | 2026-06-11 04:12:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a1f94f15-6923-3ad7-8832-722eadca0ff0 | -10.84667 | -46.78824 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b154c19e-5ffc-3450-917e-884c30e206b2 | -7.72391 | -44.16319 | 2026-06-11 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 315dddf7-a138-3cf6-be09-1bea26ef4639 | -10.28542 | -47.61831 | 2026-06-11 04:12:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fd8ca432-ad36-345f-a48e-6efb612d2906 | -12.85205 | -44.37471 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08039e0e-81ab-375f-8596-0e970d671c90 | -13.36766 | -43.20527 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e4de403-39c7-37c4-a0e0-76d2e35031ba | -9.31471 | -45.48179 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5baec2fc-68eb-3e88-afaa-08defcea5346 | -9.31236 | -48.96603 | 2026-06-11 04:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe8c784a-47d4-3ed7-9d98-dd7b69543b06 | -10.84598 | -46.78896 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38284799-57a6-3334-b628-78ef04a09c62 | -12.01247 | -49.27249 | 2026-06-11 04:12:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 003a4eba-f52d-3fd2-a724-fcc693141083 | -10.85085 | -46.78899 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0eae64d2-8b44-3375-a434-48656ecb5e24 | -12.36804 | -47.89442 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6be7553d-1146-3adf-b1af-bf9172e66847 | -9.30855 | -45.47028 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6aadd85-d8c0-3609-a07b-5e0549b2dc7f | -12.8669 | -44.37315 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59277838-8e6f-322e-8a94-9cb41ab06bec | -12.05364 | -45.29215 | 2026-06-11 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13ad1066-107a-32b5-a1cd-72d78a31d679 | -9.32652 | -45.48391 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4ced5b32-d4b5-3133-bc91-70b9594431b4 | -9.10488 | -50.91623 | 2026-06-11 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e3d1313-0eb9-3260-b298-156196eb189f | -9.3195 | -45.47746 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7fe27f63-0334-3107-9c87-63b1be4dc16f | -9.30069 | -45.46885 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f45f8992-2a12-3b7b-9ca5-34ae6e3b1816 | -9.80571 | -46.7009 | 2026-06-11 04:12:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9400df4-601e-383a-a119-e26dbd1add69 | -10.37767 | -46.62354 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c30c9469-3868-33fb-8f1b-b63e1f4c76a8 | -12.05739 | -45.29282 | 2026-06-11 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25362983-0867-356e-9bc8-dcf776f9e476 | -9.32738 | -45.47887 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 650cca91-ba6e-3017-9ad2-b6a886e406cf | -7.87824 | -47.09935 | 2026-06-11 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3288fb8-6483-370d-b117-4e36f9a887a4 | -9.3113 | -48.97188 | 2026-06-11 04:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ab15636-7949-34b6-aed1-c644bcfe1b67 | -9.53185 | -47.75422 | 2026-06-11 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d22a0375-44c8-3513-b692-670e6050305b | -12.862 | -44.38065 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fec957c-40bb-3b26-bb53-65d6733929ac | -8.32175 | -43.81502 | 2026-06-11 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| afffb158-3eb4-367d-bca8-e7066a46def6 | -12.85273 | -44.37064 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d385dff0-2456-3dd2-8906-996d64e97b01 | -12.7471 | -49.89589 | 2026-06-11 04:12:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ff593db-10f5-3a87-9ae4-69a8806c003c | -10.28623 | -47.61386 | 2026-06-11 04:12:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e75c2bdf-98a4-3e04-907a-c6d684a69ef8 | -12.37241 | -47.89531 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README6.md)
