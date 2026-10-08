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

## Dados Diários - Página 408

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61ecb675-f6cf-31d7-9de0-6fee543f6e89 | -5.9835 | -40.9367 | 2026-10-08 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 175.0 |
| 3f41883e-6800-3736-9a75-e37d088bc3c3 | -6.2162 | -52.7876 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| f714bc13-3c17-3c51-b267-6874e4a8d23c | -3.86 | -44.1274 | 2026-10-08 19:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| aadebcb0-d9f4-3577-bf67-69b01ba2f1b6 | -3.9483 | -56.0138 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 53e21ee5-bdf0-3803-9fd7-b38467d91d73 | -8.3045 | -45.4525 | 2026-10-08 19:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e0c8fef9-10bf-3e58-b69a-3582ed2c89fe | -3.2085 | -57.87 | 2026-10-08 19:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| cbff4406-d8d1-3e92-994d-0606e9f270dd | -2.8712 | -54.1719 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 854f1781-6a8c-3827-9705-113d8c78b5be | -2.853 | -54.1322 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6200827c-594e-37a7-b606-e4514524b91b | -9.0359 | -44.3885 | 2026-10-08 19:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 440e38be-c969-3b87-a503-29c933f571c3 | -2.5491 | -58.0566 | 2026-10-08 19:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3f29f7d9-2db2-37eb-b0a8-63b54c1d7a23 | -3.095 | -59.1832 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 051ea2b2-cc60-3d1a-a1fa-0d2198530606 | -14.4345 | -43.9157 | 2026-10-08 19:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 2559e4d1-b49d-3354-b7a4-e2b5b726338a | -4.1023 | -44.1379 | 2026-10-08 19:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3d096710-2e1c-3a94-a04a-639ac154e4f2 | -9.9007 | -44.8608 | 2026-10-08 19:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 346.3 |
| fce5950e-d783-3d91-a9e1-141ae389ebd0 | -6.2527 | -52.8675 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| b4e387b7-50a4-3ee0-8390-3de2aac4fbff | 1.5284 | -55.9636 | 2026-10-08 19:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 17e183a6-f935-3ce1-aa54-1e0db4e425e6 | -14.4585 | -41.2104 | 2026-10-08 19:30:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 117.7 |
| 180feaff-6d82-3cfb-939f-a10fcc320068 | -5.0631 | -45.4466 | 2026-10-08 19:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 0efc639a-2a7c-3f3f-8042-50081b2874fb | -6.1227 | -55.6955 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 53c0df8e-d9b0-3247-ac3f-50d8d6575866 | -6.8907 | -45.8988 | 2026-10-08 19:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 1a7187df-5e05-370d-8dbc-c48c96fc2605 | -3.0163 | -54.7488 | 2026-10-08 19:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3f88750b-ee36-3cf4-a1c5-2eebd29567e9 | -6.2155 | -52.8899 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 608d1991-19d6-3169-8d7e-ef3c3c41ba40 | -2.5171 | -56.1459 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| ed55aa92-02af-36ca-ac63-7a16b7c9c5e0 | -5.3716 | -44.2211 | 2026-10-08 19:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 307e1ffd-f62c-34d7-87a7-36dc3d285840 | -3.9483 | -56.0335 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c85ac48b-92b3-3ff1-8b93-46cda90c34aa | -8.2176 | -46.4068 | 2026-10-08 19:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d3d82422-b337-392a-bdb7-6eeb728a0bd3 | -11.8696 | -43.5568 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 1e816a45-99b1-3e69-9aa8-f29c102d8174 | -8.5722 | -67.4569 | 2026-10-08 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| ec1e54b3-6a56-3ee1-a3da-53b978d7fb4a | -6.2355 | -52.6841 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| fc6b3bf6-b7bd-3704-a450-3bfb97b6beeb | -3.4095 | -58.0013 | 2026-10-08 19:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 26fbeae5-4276-3991-a724-33d17c6a1d8e | -5.0946 | -46.206 | 2026-10-08 19:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 0bb6191b-da62-3a0d-bbeb-fbdfeafb3ced | -6.1415 | -52.8734 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b825ccda-4a10-3fdf-ad19-2bb87f1bc550 | -3.1697 | -58.6437 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 5412bda4-7d3b-30bd-b0d9-bfeb80b8e2c0 | -2.9979 | -54.7692 | 2026-10-08 19:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4a9a6baa-abdc-3fb6-803a-4f9155c0a4be | -7.0706 | -52.6764 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 517d074f-db66-3f3e-80fd-59efa081baa5 | -2.4988 | -56.1266 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 9ec72489-dead-3253-ab1a-9fb547131d61 | -5.4956 | -42.8648 | 2026-10-08 19:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 6ebe74e8-79fa-3d20-a742-82740b00612b | -3.1879 | -58.6626 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5c1d80d9-43ca-321c-a010-22556bc069b3 | -6.4031 | -55.2042 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 2b8cdcaa-6c4b-3a23-958d-20f288e63d40 | -6.3098 | -55.3285 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| b5959c3c-cba9-3740-9e32-e6157a9d9226 | -3.314 | -53.6979 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 2dc4aad5-faf2-3ace-802a-b2f407af11f6 | -3.2137 | -42.953 | 2026-10-08 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 819931ae-c33e-312a-9001-ab4dfb8eb328 | -6.4411 | -55.0424 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 457.2 |
| f2110a16-6996-30be-a99b-ccfdfbb5004f | -8.0764 | -45.6339 | 2026-10-08 19:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 803a2824-8cf5-3844-8522-92b67e362eee | -6.1226 | -55.7154 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| c031f1d4-6f29-304b-90d9-cdcce2f96bef | -9.2778 | -47.4554 | 2026-10-08 19:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b52afbe1-dc0c-3690-bab7-c5b7e28306df | -3.1874 | -58.8358 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| bed85f12-f807-32e8-b9cf-3becb201bbe4 | -9.8817 | -44.8632 | 2026-10-08 19:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ba8b20c8-5cd0-3f0b-a694-b25c5b18f541 | -3.7057 | -57.0998 | 2026-10-08 19:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3ea063c2-846b-3e27-8b1d-0adbbbf8ac74 | -3.1879 | -58.6433 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 132fec67-b1de-38d6-ab07-38de36147714 | -3.2081 | -58.0057 | 2026-10-08 19:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 476.9 |
| 15b3005a-cc4e-305d-b3a9-b72849a26c72 | -2.4806 | -56.0678 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| e5867d97-b47f-384d-8ee6-88cf614fc622 | -2.5675 | -58.037 | 2026-10-08 19:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 7a24f4c9-3959-3c28-9167-fc368d86b416 | -3.0256 | -57.7768 | 2026-10-08 19:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 81fe1ff9-c868-3df4-9e8d-1b25bd305e03 | -1.3111 | -54.1982 | 2026-10-08 19:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| c64c8996-6621-3771-902d-243b4d4759ef | -4.7404 | -55.6522 | 2026-10-08 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| d2855aab-2e87-3fbf-bebe-80f2432a5963 | -5.9833 | -40.961 | 2026-10-08 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 415.3 |
| c4e2646f-0f7e-306e-8843-281fc2bdf13e | -15.1051 | -43.6409 | 2026-10-08 19:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 152.9 |
| 90a3900d-2f95-3faf-adb8-53c693e77833 | -2.517 | -56.1656 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 79f2b574-bc37-3be3-8c33-b8fc0798f1b8 | -11.2271 | -45.2374 | 2026-10-08 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 8a566dfb-75c5-3aa2-998b-5551c917c3d8 | -9.9011 | -44.8378 | 2026-10-08 19:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 16c0b9a4-7fcc-35e4-9ecb-213042a5254c | -2.9451 | -54.0497 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6a9fc671-5baa-3daa-927d-49ef8df73ae1 | -2.8347 | -54.1125 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1b357c01-8dd7-3585-81ce-a178887cbb14 | -5.68 | -45.3383 | 2026-10-08 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| fa8c7f25-eb9e-3795-a410-dfc0745ef80e | -2.7428 | -54.1347 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| b629903d-aaa1-3207-a62c-0c9c668d403d | -7.4097 | -44.7427 | 2026-10-08 19:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 72e018f4-7b9c-33a7-9985-404ab7bdcaee | -6.0447 | -53.49 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 4c074c56-2ff1-35b1-8a8a-9d88507c29f6 | -8.0575 | -45.6357 | 2026-10-08 19:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 40fe9d11-a961-388d-93a1-5cd7e9926cc6 | -8.9775 | -45.9023 | 2026-10-08 19:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8dbb04c1-0c5a-3bb1-9da4-233e97986a7d | -5.9891 | -53.4928 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 89f0e470-9246-39a9-9bc5-3651a125b796 | -4.6362 | -50.9646 | 2026-10-08 19:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 706.1 |
| 931a3a3e-a761-3dfb-a279-a5fd844a5168 | 1.6938 | -55.6066 | 2026-10-08 19:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 4757495c-944a-3277-a228-662878f28498 | -9.479 | -67.4897 | 2026-10-08 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| b8d7f60d-4756-3803-b212-2ea7c91ff8f4 | -11.0758 | -44.0299 | 2026-10-08 19:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| cebadb3d-1120-3a75-9bec-9d979dcc98b8 | -4.2338 | -46.9387 | 2026-10-08 19:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 03ebcac7-159a-32ed-b945-255140e90123 | -4.4216 | -49.6707 | 2026-10-08 19:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 640f5cc5-0733-3560-abab-d2d206cb0bdb | -9.9801 | -45.9009 | 2026-10-08 19:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 40b91d41-bbef-3098-a8f0-8a211cc493fd | -6.4032 | -55.1842 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 5392044a-0650-33ef-a1cb-892c77370844 | -3.8413 | -44.1283 | 2026-10-08 19:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| fe89d54b-9e4f-3b4e-ad87-586a8f08fdfa | -6.509 | -55.9554 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 2b7829c3-0f0b-313d-890d-27a47b9e4253 | -11.619 | -43.6196 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 83076044-defd-38fe-bda5-feb200ccb6d5 | -5.5863 | -43.2095 | 2026-10-08 19:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b2de08d8-09b5-3377-92e8-961925815f74 | -12.1549 | -44.7314 | 2026-10-08 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| c1feaa57-7cd7-3c5c-8696-f2bf5c0cfcd8 | -6.3134 | -54.7884 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 63a29eed-251c-30a5-9508-6452c17206c7 | -6.8904 | -45.9212 | 2026-10-08 19:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9f2d4cf3-c67a-364e-9f24-2eeed9adb8b6 | -6.2342 | -52.8685 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 044943f8-7d5e-3cf0-a341-a9df129e4454 | -6.1501 | -51.6992 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 825297fe-a206-326e-bb7e-91648d1d6616 | -2.7429 | -54.0945 | 2026-10-08 19:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| aa06b8b4-6929-3b38-9f46-1bd431a195fb | -5.7117 | -53.4862 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 272.7 |
| fa979c2b-f286-3306-bc37-3cfb54241ba8 | -2.499 | -56.0675 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 71e67ace-207f-3fd2-9943-90bfd842144b | -5.3718 | -44.1981 | 2026-10-08 19:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ec6416ba-598c-3512-a761-ab2b52582d87 | -6.104 | -55.7361 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| b4dcc501-29f1-34aa-8dc2-adeaf01c95fe | -5.3905 | -44.1968 | 2026-10-08 19:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| a81ad6d0-4d5e-3cb9-af53-3fcc79289b70 | -1.7681 | -55.0309 | 2026-10-08 19:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e1fc554c-fc8f-3808-9678-1c38460d3af4 | -3.9299 | -56.034 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 6ecd53c2-0722-32c0-a5ee-a10961f08127 | -3.2031 | -53.8621 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 33540d41-be13-3f3a-b7fe-0b264f112a31 | -6.0609 | -42.608 | 2026-10-08 19:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| aeb15218-9782-3665-b221-6db81a589c16 | -13.3666 | -43.8979 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 3c7e77fc-35bc-348d-9d43-de88189d4b85 | -5.5144 | -42.8634 | 2026-10-08 19:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 2c30ae14-8581-3d4e-96a9-dfa077128376 | -7.5882 | -42.3925 | 2026-10-08 19:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |


[Clique aqui para ver as próximas entradas](README409.md)
