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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a9c0933-08a0-30ad-b774-81d39705bf8f | -7.2603 | -44.665 | 2025-08-08 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 6c2a62ba-4c11-3014-910d-11634932ff02 | -7.0801 | -59.1578 | 2025-08-08 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 223.1 |
| 769dc3f8-408a-32c1-93cd-ef564e148778 | -7.0801 | -59.1578 | 2025-08-08 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 207.1 |
| 70d93021-fedd-3e2b-8cf5-a981714d7b61 | -7.2603 | -44.665 | 2025-08-08 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 26cda8d3-11b6-39da-b971-c6d55ce53f0b | -7.0616 | -59.1586 | 2025-08-08 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 360.9 |
| 5a811098-c155-3949-9fec-85ef39686916 | -7.0614 | -59.1972 | 2025-08-08 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 358.7 |
| ecba8d2c-c741-3b4a-9772-edb326d34545 | -7.2415 | -44.6667 | 2025-08-08 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 5144ff74-710c-3b9b-ad72-ff5d9189f5d1 | -7.0801 | -59.1578 | 2025-08-08 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 220.4 |
| 8b52e8f7-3ce1-30cd-b466-42089dab9a29 | -7.0614 | -59.1972 | 2025-08-08 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 263.2 |
| d5cb156f-b5de-39b8-8e0d-36945dc87290 | -7.0616 | -59.1586 | 2025-08-08 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 357.1 |
| 1ffcf8ae-f3d2-347f-932d-1c5938371ba6 | -7.0614 | -59.1972 | 2025-08-08 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 407.0 |
| e456794b-7eba-32a4-956f-9071f63b1160 | -7.2603 | -44.665 | 2025-08-08 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| bd16728e-4fa0-3199-adb4-b35ae8d387ed | -7.0616 | -59.1586 | 2025-08-08 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 358.8 |
| b2dd7a4e-0a8c-3ec1-a1c7-cdd2143ed2f5 | -7.0801 | -59.1578 | 2025-08-08 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 241.6 |
| e3af0892-ca67-3534-a935-4662aa014a67 | -7.0432 | -59.1594 | 2025-08-08 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ecdd495f-c2c1-375d-9370-3959e8a0a8b5 | -7.0801 | -59.1578 | 2025-08-08 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 224.1 |
| c5e7563e-95d3-3556-a08b-cdfd8180e7f9 | -7.2603 | -44.665 | 2025-08-08 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| eb5cdfd6-5082-3c6e-82eb-27bfb108cbda | -7.0614 | -59.1972 | 2025-08-08 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 401.9 |
| 52286e35-98be-386d-bc09-b3e44a11d6b2 | -12.571 | -47.1809 | 2025-08-08 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f2dd1dff-d5f4-375e-9ee2-3935cce7e297 | -12.5706 | -47.2034 | 2025-08-08 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| de9cd463-bf28-3439-9c94-4a5b60de582b | -7.0616 | -59.1586 | 2025-08-08 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 384.7 |
| 77b8568f-f99f-3295-b1ea-dc924e8789ce | -7.2415 | -44.6667 | 2025-08-08 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| ef2dabde-ec31-30c3-9420-1986c86dfdfb | -7.043 | -59.1787 | 2025-08-08 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 412.0 |
| ecd91af7-7060-3a4d-b842-09672bed0369 | -12.571 | -47.1809 | 2025-08-08 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 6109937b-8064-35a3-a8fe-14882698680a | -7.0429 | -59.198 | 2025-08-08 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 306.1 |
| 7580f0b5-9f68-35e5-85d3-d5d61955c256 | -7.0801 | -59.1578 | 2025-08-08 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 267.8 |
| aa238d02-a91b-3626-b90f-58f913f6c9c5 | -12.5902 | -47.1781 | 2025-08-08 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 83c2d3c0-89a9-3991-90e7-c1163944c75b | -7.2603 | -44.665 | 2025-08-08 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| d92c015f-952a-3834-801f-b939c9f5cf85 | -7.0614 | -59.1972 | 2025-08-08 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 450.1 |
| f4b32d16-65a5-3550-a8d2-c809b965c8f8 | -7.2415 | -44.6667 | 2025-08-08 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e23c374e-f36f-3813-8047-3362753c0b13 | -7.0616 | -59.1586 | 2025-08-08 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 362.9 |
| b7579e2d-c1b4-39c0-8fe3-b2a3aace5011 | -7.2603 | -44.665 | 2025-08-08 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6cacf17b-cb06-3168-b9c4-2f2b0450729f | -12.5706 | -47.2034 | 2025-08-08 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 77ed496d-7fa8-3989-a989-8dfa7d161722 | -12.571 | -47.1809 | 2025-08-08 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2978ff7f-62c7-3385-87ca-a95dc5452683 | -7.0614 | -59.1972 | 2025-08-08 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 426.0 |
| 0ad08b99-cfca-38ec-ac5d-4be9218b0225 | -7.0429 | -59.198 | 2025-08-08 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 255.2 |
| 6c7bc051-ad7b-3896-8a0b-2a17d5c2b1e1 | -7.0429 | -59.198 | 2025-08-08 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 276.3 |
| 69459533-a941-3779-a0a7-9ead0e7a2609 | -7.2415 | -44.6667 | 2025-08-08 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 9a6d39b8-5bc4-3495-a549-9b0cbe6eadf8 | -7.2417 | -44.6438 | 2025-08-08 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f76d5fe5-ae86-3288-9a60-93ec997b3926 | -7.2603 | -44.665 | 2025-08-08 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 9b5f59aa-3cc1-32b7-8dea-316a9fb3be39 | -7.2229 | -44.6455 | 2025-08-08 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 8ce78df4-bee8-3dd0-a86a-04ab3f53f14b | -18.8445 | -47.0483 | 2025-08-08 12:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 467e1335-2a5a-3158-988e-6c808622e410 | -12.5337 | -47.1189 | 2025-08-08 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| cce8c9eb-9f3a-3e9b-b67f-8ddd2ae3efe8 | -7.9106 | -45.3329 | 2025-08-08 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 180.9 |
| bb47be40-9f06-3ddb-ba87-82a0160adb40 | -18.8445 | -47.0483 | 2025-08-08 12:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 02516c95-c7e2-3312-a7d0-a179ffd54b38 | -7.8915 | -45.3575 | 2025-08-08 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 215.4 |
| c214e7fe-0802-3cfd-bd13-9eed452cd7e2 | -7.2603 | -44.665 | 2025-08-08 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 80a24d9b-d1ce-3632-88b1-5d2fd30285e8 | -7.8918 | -45.3348 | 2025-08-08 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 299.4 |
| f644819a-77d8-3c43-b09c-aeae1b28aec5 | -7.0429 | -59.198 | 2025-08-08 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 255.5 |
| 748b4a4f-6144-356b-936e-e0fd82ac8802 | -7.0615 | -59.1779 | 2025-08-08 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 791.3 |
| 2b3a0a2a-1d9f-35eb-881c-67bd284d60e5 | -7.9104 | -45.3557 | 2025-08-08 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 93c22530-a50a-305a-9c38-329c9ddaf2be | -7.0614 | -59.1972 | 2025-08-08 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 441.9 |
| 0a7da6c3-52b4-313c-acda-200c4206717e | -12.5337 | -47.1189 | 2025-08-08 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 65d44422-2def-341b-9978-50491d45b831 | -7.8918 | -45.3348 | 2025-08-08 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 245.1 |
| c6aa1783-02a0-3d9b-b8ed-9b08abd0f18d | -12.5714 | -47.1584 | 2025-08-08 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| fa25ee3b-880f-333c-99c5-841144ec7bce | -12.5718 | -47.1359 | 2025-08-08 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 204d75a3-6ecf-301f-9572-567c48f90006 | -7.8915 | -45.3575 | 2025-08-08 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 2304cc1b-9fee-316a-b19b-74af11e21e3a | -18.8445 | -47.0483 | 2025-08-08 12:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 3589dbbf-c5e5-3360-ba92-f86c9ad2a009 | -7.0614 | -59.1972 | 2025-08-08 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 289.7 |
| 57c6ab1d-4289-30e1-a0c0-4cf36af0ecfa | -12.5341 | -47.0964 | 2025-08-08 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5c2e6ada-4ddc-3ee4-a031-f9749acabb49 | -7.2603 | -44.665 | 2025-08-08 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| acfd5ea2-c5d6-364a-8056-6497ce01c793 | -12.5526 | -47.1387 | 2025-08-08 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| c37a094a-5f28-3f20-902a-45f62dc5bfa3 | -12.5718 | -47.1359 | 2025-08-08 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 0e2a2f7e-1893-38af-bfa0-535452b15c46 | -7.9104 | -45.3557 | 2025-08-08 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b1555c83-9512-3612-9b74-422be20d4ee5 | -7.8918 | -45.3348 | 2025-08-08 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 75e954f1-6d2d-368c-bf0d-bba42a7e6435 | -12.5337 | -47.1189 | 2025-08-08 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| de1913dc-01a7-371b-a547-f805ca65f7a7 | -7.0614 | -59.1972 | 2025-08-08 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 437.5 |
| cc1944da-023c-3430-b0d2-609f71909641 | -7.9106 | -45.3329 | 2025-08-08 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 172.4 |
| fd72234e-bf9e-3769-a3b6-b8dae4941226 | -7.2603 | -44.665 | 2025-08-08 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 62ca789c-b1cc-39b1-ad91-66523914a27e | -18.8445 | -47.0483 | 2025-08-08 12:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 908c2475-381b-3a41-a8f3-e3d6bb94b420 | -6.56709 | -42.81086 | 2025-08-08 12:32:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 4e8c4203-f769-3a39-abd6-d429778f1601 | -6.13057 | -42.94388 | 2025-08-08 12:32:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 0c5c68ca-61e0-3eb8-a2a5-495b05fa684d | -8.49818 | -45.70105 | 2025-08-08 12:32:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1fece164-a206-396c-8a08-a06e6d76d3c1 | -6.96239 | -42.87038 | 2025-08-08 12:32:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 1dbb102a-c6ee-3a06-9f6d-b47d18dd46a9 | -6.12983 | -42.95907 | 2025-08-08 12:32:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 4334bbcb-9ac9-3225-8484-fb954589b24d | -7.36743 | -44.64407 | 2025-08-08 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 426dffa3-f492-3471-b832-4117c284ba4c | -7.37589 | -44.65097 | 2025-08-08 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7ed1a5ef-0e20-3fe6-851d-df4c9f8a20d7 | -7.90714 | -45.33067 | 2025-08-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a860df20-5c57-3081-a66b-fc304879f99a | -3.30734 | -42.54502 | 2025-08-08 12:32:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c9fbc5a4-33e6-3e8e-b900-1c60da8fee2f | -6.90271 | -44.151 | 2025-08-08 12:32:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9b1301b2-6ca8-3387-9ec8-9983e192e298 | -6.90491 | -44.13411 | 2025-08-08 12:32:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2ba5c9c8-16b9-3b69-b4b7-2beeb1832445 | -6.27185 | -45.28909 | 2025-08-08 12:32:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2059ddd0-3b08-3e24-a37e-7a4d2013ee25 | -3.31009 | -42.52514 | 2025-08-08 12:32:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| dc6c2f46-25c8-37c5-bbb1-d1ad95e9f46a | -6.09188 | -44.99177 | 2025-08-08 12:32:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f102254f-b2ea-3977-b174-70c7f74b77ff | -7.57626 | -44.4247 | 2025-08-08 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6a6f06dc-5ba0-35fe-91ab-6cf47bd381de | -7.9053 | -45.34501 | 2025-08-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 08f9b3bb-58eb-31da-9561-430c75b7c02e | -6.19865 | -42.51801 | 2025-08-08 12:32:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 9fa7f5e2-c846-3efb-94ca-ce4252677665 | -9.21001 | -44.53538 | 2025-08-08 12:32:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a6a30dc4-7548-3b34-8348-9f0a978dc29d | -7.25726 | -44.67756 | 2025-08-08 12:32:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6c1fe533-6be2-3937-95c6-959797387567 | -7.22783 | -44.65044 | 2025-08-08 12:32:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| fe0d05bb-2da5-3361-9418-3057ee8e92e2 | -7.72106 | -45.5224 | 2025-08-08 12:32:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 95bc119f-9408-39cc-8282-de72254c1822 | -7.57834 | -44.40834 | 2025-08-08 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 2a71ad3a-31ed-398c-8632-361220cb25b0 | -3.56639 | -44.23182 | 2025-08-08 12:32:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9c458fe7-4381-357d-883c-f839e9239bb8 | -6.96643 | -42.86401 | 2025-08-08 12:32:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| af12aeed-a520-34ed-8d72-75e0705725b0 | -7.2257 | -44.66654 | 2025-08-08 12:32:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f2721bae-93a6-39be-88f5-04c0775ad272 | -7.90436 | -45.33849 | 2025-08-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 072ffb17-cd53-3a6a-b4b3-2c42ec9d9afd | -6.46777 | -44.58387 | 2025-08-08 12:32:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| cf9b56fd-3167-3b17-81bf-03d349921fb3 | -7.56956 | -44.41837 | 2025-08-08 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 315bf648-e424-3f59-8f58-2061d508abbf | -3.54428 | -43.21269 | 2025-08-08 12:32:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 1930a983-3b81-31fd-a715-fb32868f13ee | -6.96352 | -42.88575 | 2025-08-08 12:32:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |


[Clique aqui para ver as próximas entradas](README28.md)
