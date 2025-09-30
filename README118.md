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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc424417-204e-3b4d-84b1-da0a8f70c5f6 | -14.7367 | -45.2255 | 2025-09-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 386.3 |
| 348308a4-1b10-3e02-ba33-e7861946a622 | -9.1248 | -47.6256 | 2025-09-30 13:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 6200f992-e557-39a4-8520-d45e8de46a43 | -18.2176 | -53.3177 | 2025-09-30 13:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 625e9edd-08a4-3e09-a535-44c2c0619d22 | -8.541 | -44.6515 | 2025-09-30 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 175.1 |
| c027934e-55e4-3fdc-ac44-9bf351ba3bbd | -12.1076 | -44.1785 | 2025-09-30 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 64630c97-9396-3401-8e22-700621e604b4 | -8.5407 | -44.6745 | 2025-09-30 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f95582d1-c22b-3888-aed3-3f94d12c4a36 | -7.835 | -46.9986 | 2025-09-30 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| a9fba736-527d-3997-853e-2430758cd4de | -5.2869 | -43.1613 | 2025-09-30 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b6bb7d79-0958-35f6-b6b5-6f800dc13d21 | -16.7575 | -51.3482 | 2025-09-30 13:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 918f13be-4f7a-33c5-a656-6b1eaebd733a | -12.3867 | -50.1731 | 2025-09-30 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 76188a28-55ec-357a-ad70-a3f22a4d1d1e | -7.819 | -46.7561 | 2025-09-30 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 1edc46ad-00ee-3d9f-9e89-eea6fff01350 | -13.7319 | -54.7307 | 2025-09-30 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| a9b84e66-a87f-3665-9409-bd3fd73ddf41 | -8.4368 | -46.9424 | 2025-09-30 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| bcfbae85-3c39-3b9d-841d-9f2f1fbe9018 | -11.1948 | -47.211 | 2025-09-30 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c7005feb-9247-30a2-8beb-4f77e7a68ef5 | -5.7599 | -42.6797 | 2025-09-30 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| c5875e77-811e-3658-b9c5-d1e051250ac1 | -12.2348 | -47.7863 | 2025-09-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d1628c5b-e15e-3110-b06b-5ed705b52edb | -13.2226 | -43.3768 | 2025-09-30 14:00:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 129.5 |
| a26ab3dc-e4a8-3c55-98d8-5eebfed172ec | -17.921 | -57.5952 | 2025-09-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 48c946e2-9146-3d40-9c22-bc486f2dc752 | -9.5703 | -54.5843 | 2025-09-30 14:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2dbd8962-5122-3656-80e5-d044bcc9a64f | -9.9585 | -43.5752 | 2025-09-30 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| ec4adb49-d4b4-3225-b8cd-d2aab029497a | -9.939 | -55.1632 | 2025-09-30 14:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 284e91fd-2411-3b87-8123-e250ddfc073a | -6.4131 | -43.0724 | 2025-09-30 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 07472062-9c9e-3f1b-b0d8-1dfbf766cde4 | -6.523 | -45.207 | 2025-09-30 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| d597ad9c-391d-34be-bbc2-a27f655a57e5 | -8.1616 | -46.3675 | 2025-09-30 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| cfcf8a93-10b8-3b85-bd71-4e7267c7b79b | -12.7022 | -45.2715 | 2025-09-30 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 86204ae9-1a18-3987-8166-594bcb8ecb25 | -8.244 | -45.7754 | 2025-09-30 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 25aca53c-ab35-3957-ac2d-d39063ed9f2c | -10.1855 | -44.8709 | 2025-09-30 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 8bfd4376-2bef-3218-9b24-45e920ba692b | -9.4007 | -54.6984 | 2025-09-30 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 70b78a79-6c38-39b1-97f2-a26b502590bc | -6.5042 | -45.2085 | 2025-09-30 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5aad98da-de6b-3c2b-8c48-c563bb8dc639 | -7.9191 | -44.6245 | 2025-09-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 242.9 |
| e24e3402-8837-37c7-b8cb-5761278c095a | -9.0425 | -46.7032 | 2025-09-30 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a1974bfb-7a52-3c32-aaa9-7383dd4635b1 | -10.6419 | -48.6021 | 2025-09-30 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 9f55e16f-107e-3e92-a7e3-25185e19707a | -7.8696 | -47.2606 | 2025-09-30 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 166.9 |
| a3c2f01d-fade-3888-8a4e-e8077a3c43db | -14.6603 | -46.9663 | 2025-09-30 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 6c481679-b261-38fa-975c-211ba557bae6 | -14.5517 | -48.4907 | 2025-09-30 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b95a96c5-34fb-3a06-9080-09fb514f3d2e | -15.9268 | -46.2334 | 2025-09-30 14:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 248.6 |
| 471b6bfd-13ab-33ee-adcf-231bdb959069 | -7.8378 | -46.7544 | 2025-09-30 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 93dd33d6-2e17-3e9f-88de-6abbac4f4a85 | -11.1548 | -54.1054 | 2025-09-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 41fe176e-0059-3028-97a0-bffd6147aca1 | -5.8445 | -45.7545 | 2025-09-30 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 56ff3d0f-96ca-355a-95af-51ba429838d9 | -12.2153 | -47.8112 | 2025-09-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d82e8408-ae2d-3219-acc1-b51f44b681c3 | -5.4565 | -43.0554 | 2025-09-30 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 1638d60c-7146-3055-87c7-aa81e7a38016 | -12.3867 | -50.1731 | 2025-09-30 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 1cabeda8-50e0-3e51-995e-760e531f0d3d | -12.4058 | -50.1708 | 2025-09-30 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 93ee3fc0-ea44-3815-88ae-fa1dfb40ca02 | -18.1981 | -53.2993 | 2025-09-30 14:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7c56d547-d7fe-3ff6-b01c-c936e4cf3b99 | -12.952 | -48.4185 | 2025-09-30 14:00:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 199fb2a2-8842-3efb-aeee-3bf2b67b2b80 | -13.2741 | -50.8997 | 2025-09-30 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 25f87727-203a-35ad-9f08-f1e2203dd6cd | -15.7917 | -43.6672 | 2025-09-30 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 497.6 |
| 1a0c2a2d-497b-37a6-be81-1e6bbb9edec5 | -6.153 | -42.789 | 2025-09-30 14:00:00 | GOES-19 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 6fdb0b89-ea32-38c5-a37d-3ac21c0e583d | -5.2867 | -43.1846 | 2025-09-30 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| c67e35f3-cd55-344d-8847-2b5c6131fac9 | -8.541 | -44.6515 | 2025-09-30 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 0212876e-c28d-3c12-bd2e-3846553dd51f | -5.7411 | -42.6812 | 2025-09-30 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 370.1 |
| 3474fed2-c2b4-3091-979a-c57bb1a3a7d6 | -18.2176 | -53.3177 | 2025-09-30 14:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 228.8 |
| 2235b455-7816-37f7-b2b4-63d4b3f56516 | -22.5205 | -44.597 | 2025-09-30 14:00:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 135.9 |
| 324f20d0-cf18-39ec-9e1a-122c722749a8 | -9.8845 | -45.9576 | 2025-09-30 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 7ae142a7-5feb-3cda-8d43-0c7b8374d7ef | -13.2006 | -47.4251 | 2025-09-30 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 0cf32503-968a-353a-a664-aa2a4318d5db | -7.2999 | -42.8486 | 2025-09-30 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| b8ef2f2d-ea66-3c48-9386-07cabcd80f46 | -8.9182 | -46.1115 | 2025-09-30 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 939f7dec-f2be-3a83-a915-14b6b20efab9 | -7.8188 | -46.7783 | 2025-09-30 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 8093dd0f-5ef6-380d-82ed-d8154fa56648 | -6.2759 | -43.6442 | 2025-09-30 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| eeae434f-963e-3e5d-be71-cdb41e378a80 | -5.7225 | -42.659 | 2025-09-30 14:00:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 5991c11b-1a74-322e-8d58-d92277a01822 | -17.9411 | -57.5722 | 2025-09-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.1 |
| b106fc3a-444d-35af-87d3-64f1641cdc90 | -5.8612 | -43.8858 | 2025-09-30 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 5cdf097c-d393-3917-ac9f-580fd82c9728 | -14.3847 | -47.1486 | 2025-09-30 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 227.7 |
| dc636e28-13a9-3c84-a463-f1ed4813c9bf | -11.1753 | -47.2358 | 2025-09-30 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 69ea31f2-6e53-3805-b9c8-19e7c6bed24f | -11.1944 | -47.2334 | 2025-09-30 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 21ccc2e3-b56b-33fe-bc8a-c200f2abd640 | -9.4206 | -54.5753 | 2025-09-30 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 249.4 |
| d67c277f-cd24-36be-ba56-f8ec9ed9639c | -5.826 | -45.7334 | 2025-09-30 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 96d7b816-4f8a-3c49-9cba-aeef2440d81f | -17.9408 | -57.5928 | 2025-09-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 56a0fffd-70ed-39a9-b431-e578d3687597 | -14.4041 | -47.1454 | 2025-09-30 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 114ace3d-15b0-3c41-9585-bb9a6eea28b2 | -5.9192 | -43.6961 | 2025-09-30 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b6744ceb-2db9-3aad-8717-4e2df8149a92 | -5.2869 | -43.1613 | 2025-09-30 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 47c12a6c-5239-3458-8ea6-a1efcf41047a | -7.0481 | -45.1856 | 2025-09-30 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5265982e-12f2-3ee2-9b6c-eaefb5ebea73 | -7.819 | -46.7561 | 2025-09-30 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| a5107051-a87b-36e5-86c7-ac305cc159b6 | -9.8198 | -47.8606 | 2025-09-30 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4323ccac-6952-37b3-801c-29f9c1f40be1 | -9.1248 | -47.6256 | 2025-09-30 14:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| aa3b97dd-5fa6-3c86-8ad8-c83caba07e0c | -11.1546 | -54.126 | 2025-09-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| ce68f3c8-6d5c-3cbd-8491-5f2b2681cad1 | -5.4752 | -43.054 | 2025-09-30 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d77831ba-5cc9-3563-a1c3-240251a1f17f | -7.835 | -46.9986 | 2025-09-30 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 740cdda0-4fb6-3304-a131-a5d376dc605e | -14.7166 | -45.2525 | 2025-09-30 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 654.1 |
| d18671eb-d031-321b-971f-1ea7af2acd28 | -10.1045 | -47.7851 | 2025-09-30 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 20a2223f-b530-305c-b9a4-174b11171044 | -9.7684 | -46.1293 | 2025-09-30 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 1dd706a2-7f0d-3ede-9f6e-087d0e4a40c6 | -7.8375 | -46.7766 | 2025-09-30 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 173.4 |
| da9248f4-e5c8-3784-8a09-66b39159fb1f | -7.5146 | -45.4385 | 2025-09-30 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 1bafbe14-2e05-36a2-8579-351cb215a46e | -12.2344 | -47.8086 | 2025-09-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| e485b2ce-9f9a-3d8d-ba80-c50f2f457d7a | -7.2996 | -42.8722 | 2025-09-30 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| acc7947d-6de2-38fb-a93f-20a0c9b6fbbc | -12.7872 | -46.9018 | 2025-09-30 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3cfc0e53-2718-3659-8603-eefc3f475814 | -7.115 | -47.785 | 2025-09-30 14:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3effa9a6-97b7-3f74-a2d4-638d29b0aa7e | -7.281 | -42.8505 | 2025-09-30 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| eac3e5ce-7d0d-3fd7-992d-3939351f0f90 | -18.4862 | -44.0191 | 2025-09-30 14:00:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 129.3 |
| f5b26ad4-cc50-3353-b2b4-69a7dd3ab7d8 | -13.8264 | -47.9794 | 2025-09-30 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a9e8e2e6-00b1-36e2-94d7-f0534960f6dd | -6.5227 | -45.2297 | 2025-09-30 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 47454f2f-f2cc-3d58-ba89-a1aba6fedf3b | -17.9016 | -57.577 | 2025-09-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 3b9196e3-8ca0-3f68-a7fc-1f3b4ff9091b | -17.9214 | -57.5746 | 2025-09-30 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 192.9 |
| e5e7da15-c18d-367b-9162-5539e729e51c | -12.7018 | -45.2947 | 2025-09-30 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 05874f31-ec01-3e48-99a3-18d6e2d75eef | -5.7601 | -42.6561 | 2025-09-30 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| c1e9a0d1-de89-3ebb-85c0-7419924b4b80 | -8.672 | -47.7144 | 2025-09-30 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 46192c18-be49-329f-87ec-9c3c3ebb6315 | -15.2746 | -49.263 | 2025-09-30 14:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 7866d728-6bbd-3232-9393-e731f7d63fa2 | -9.9581 | -43.5987 | 2025-09-30 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3b6e5ce4-a02a-34c2-b760-0d4f84d0af6a | -9.1434 | -47.6457 | 2025-09-30 14:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 95333fbb-5b98-360c-9044-c33eddb02bab | -10.6423 | -48.5802 | 2025-09-30 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |


[Clique aqui para ver as próximas entradas](README119.md)
