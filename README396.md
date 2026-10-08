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

## Dados Diários - Página 396

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad4225af-52b4-3b1f-9093-953e6a0037ae | -7.7025 | -45.4436 | 2026-10-08 18:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 4e836744-3282-3216-bbd5-8fd5b4b3b93f | -7.4886 | -42.8295 | 2026-10-08 18:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 1faa1ee2-fdae-3532-b7f8-b1cc4479ce96 | -1.091 | -54.1803 | 2026-10-08 18:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4288c816-7859-3fdb-959c-b5c30070b73a | -5.4956 | -42.8648 | 2026-10-08 18:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 31b662b3-0e07-33f7-b45e-5f72fe2cb9d3 | -11.755 | -43.5275 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 34aadf61-6de8-3631-800c-00bdc6a332c9 | -3.4095 | -58.0013 | 2026-10-08 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 39ea08fd-ab4a-375a-b425-489573f308d4 | -8.9772 | -45.9249 | 2026-10-08 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 9a11ecd8-6934-3e6c-b609-1a562aba1237 | -9.9398 | -43.5542 | 2026-10-08 18:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c75649a2-7667-3c99-b55c-df61ae8da448 | -3.1298 | -53.7834 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7ebc7ec3-b354-3478-8237-fa171374e7c1 | -5.3763 | -45.943 | 2026-10-08 18:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e5635f19-a6d9-3c44-9b31-8a6e82a03db5 | -5.4958 | -42.8413 | 2026-10-08 18:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| 5128d814-0779-3b63-a007-babdce24d117 | -5.6932 | -53.487 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 198.5 |
| a6bbe947-de2e-3514-bb2f-5d6ec694e2cb | -5.3905 | -44.1968 | 2026-10-08 18:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 88983766-28e1-3061-b0dc-3a50e8af4e0e | -2.9267 | -54.0501 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3f9d3300-100e-352d-bec3-bc17e46fcf68 | -6.1496 | -51.7614 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fa936c74-3d0d-3545-92a5-1c78b4eb1df8 | -2.9265 | -54.1104 | 2026-10-08 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 2d503ba0-5d76-333d-a26c-fce48560da58 | -4.084 | -44.0929 | 2026-10-08 18:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 996c5486-7a5c-3a2c-b911-55f8d4f9ae64 | -2.9005 | -56.6685 | 2026-10-08 18:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0f72792f-e4ad-334c-88ca-3f9312428328 | -2.572 | -56.1842 | 2026-10-08 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 243.2 |
| dc878a6b-fd1a-3c91-b753-fc085ebdbb0b | -3.8383 | -55.9774 | 2026-10-08 18:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 779177f0-0837-35f4-abec-094c5ec9b094 | -4.0838 | -44.1159 | 2026-10-08 18:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 253.1 |
| b3cf0b4e-3c71-3d7a-898e-ad9b384ba4cf | -8.2176 | -46.4068 | 2026-10-08 18:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 82e0beff-f4e7-3652-95d1-ed817b7c4b64 | -3.8749 | -55.9961 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0d0c974f-daf7-3191-9d4d-fba508932411 | -8.5367 | -67.032 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| e811964a-5fc7-3c23-85a6-4c5cf1b46c5e | -1.2911 | -55.4133 | 2026-10-08 18:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 98e377d6-b03d-319b-9aca-aff95141091a | -5.6934 | -53.4667 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 431.0 |
| 2572c637-4540-3d67-af43-13e7d73fecff | -9.3395 | -65.4451 | 2026-10-08 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| dc449044-a91d-3fc7-89f9-26746b605e58 | -8.9964 | -45.9002 | 2026-10-08 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 98dece0d-c2b0-3fd1-83f2-75f7bd2f6d55 | -3.1115 | -53.7637 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| a4a11182-8701-3081-bb7d-cbcb78c29db5 | -13.3671 | -43.8742 | 2026-10-08 18:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 53fa2918-d545-307a-9946-bbe2fac45444 | -8.5313 | -46.911 | 2026-10-08 18:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 34cf2231-9552-34b9-81e9-09528edf1e91 | -5.9835 | -40.9367 | 2026-10-08 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 427.5 |
| efb0756d-b0f6-37c1-a577-cc680445b839 | 1.6938 | -55.6066 | 2026-10-08 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 35344834-9993-3e9f-9059-a774286ba1ad | -15.1248 | -43.6369 | 2026-10-08 18:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 170.5 |
| 0c53b633-f1ca-3c9a-a4a0-0ff7cd72f6ae | -5.9833 | -40.961 | 2026-10-08 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 648.4 |
| c0dae0fa-2c3d-378a-8260-2d9cad987bb1 | -6.4567 | -55.4809 | 2026-10-08 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| ce95039c-8e5b-3152-8522-3e3829460d4a | -14.0873 | -43.7671 | 2026-10-08 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 617d5995-379e-317e-884d-855edddc6497 | -4.1023 | -44.1379 | 2026-10-08 18:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 5481da9c-48ac-34d8-a585-f9e8233e0921 | 1.7488 | -55.5663 | 2026-10-08 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 317b34b3-b8dc-380b-9079-6926a3b40d13 | -5.977 | -55.3639 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f775117f-9485-3945-a2da-ee64d77f5307 | -4.6641 | -56.2281 | 2026-10-08 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 0002fd40-0407-3673-af02-6196d5e45f3a | -6.1298 | -51.9281 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c92c8abe-01ff-311e-b679-2d0d7e506b29 | -4.7589 | -55.6516 | 2026-10-08 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a8198cbc-6a8e-3247-90ad-f591c25dab89 | -3.8598 | -44.1504 | 2026-10-08 18:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 88a3cf76-6f59-3b45-8ccb-889bca4f1c5a | -6.0609 | -42.608 | 2026-10-08 18:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| a4a5c7cb-ef71-38c9-a16b-b10791ee36ed | -6.3844 | -55.2251 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 6ae43850-1b3d-3786-ac1f-b8152c30416d | -2.9633 | -54.1095 | 2026-10-08 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 58c77bcd-ff14-34d1-8bd6-50190244a9d2 | -5.9772 | -55.344 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| e4e4e711-6ad6-3eaa-aeb8-6f04cbd50e25 | -11.1145 | -44.0009 | 2026-10-08 18:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 362adc89-d44f-371a-bd33-ee37a83c5759 | -3.2136 | -42.9764 | 2026-10-08 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 208.5 |
| b67cd687-111c-3360-b05e-5c757050f111 | -14.0667 | -43.8185 | 2026-10-08 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| ec7b54b6-5c0a-363e-8ac0-8aeffb587fe8 | -11.8503 | -43.5598 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 24a3d5ca-3590-3900-9a77-9165eb47e138 | -3.3912 | -58.0017 | 2026-10-08 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6882252f-0a38-3ca3-a1e7-edce204397e3 | -3.4312 | -56.9307 | 2026-10-08 18:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| fca970e8-37bb-32d9-94bd-98d1e7fcfc51 | -1.091 | -54.1603 | 2026-10-08 18:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 40ca0e10-fcd1-362e-83eb-820aaa363ef5 | -3.724 | -57.0993 | 2026-10-08 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 67e308b7-1528-38c1-8b76-21858d9d3939 | -6.8907 | -45.8988 | 2026-10-08 18:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 919598e4-99e8-328c-943c-48b1b24d2b03 | -6.1747 | -53.4224 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| e6b842f0-e9d3-3661-bad1-a031aea968ec | -5.2729 | -55.9494 | 2026-10-08 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f4da43c7-c400-32f8-b27b-6b079ca27572 | -6.1501 | -51.6992 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e1a1eb25-8bee-3ce0-b71a-5f3d0fb7a87a | -3.8037 | -47.4839 | 2026-10-08 18:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cc9fbe60-fc95-3300-a552-50c4c02648ab | -6.6027 | -37.8944 | 2026-10-08 18:40:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 8d03c583-7bcf-3dbb-a592-52d4e72e9a95 | -5.2853 | -48.1053 | 2026-10-08 18:40:00 | GOES-19 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1cbc1a5d-6d2d-3014-bda0-613d7e4384ba | -3.1602 | -50.5812 | 2026-10-08 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e415cbfc-ca7d-318e-ab7a-8ee848aa41fe | -7.591 | -47.0201 | 2026-10-08 18:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 2397bea8-0147-339a-a237-97258910f338 | -3.2577 | -54.0016 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 9e32c0be-5c94-3411-9c00-97574f976cfb | -4.1025 | -44.1149 | 2026-10-08 18:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| f703b72e-4f04-371f-926f-76bbf698d7b7 | -8.5184 | -66.9954 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 5a3aa24f-1224-342a-848c-862e09272606 | -2.9819 | -54.0488 | 2026-10-08 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 21466cac-8222-3392-8f10-f2c6e82c0b63 | -3.4312 | -56.9502 | 2026-10-08 18:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 66d27c8a-80e6-392b-8d34-78830b78f1f0 | -6.895 | -43.7066 | 2026-10-08 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 1781f994-be90-3b01-8340-d9ee5ea10859 | -8.5369 | -66.9949 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 6164f267-f6aa-3d57-b442-69eb603f4823 | -11.7764 | -45.5265 | 2026-10-08 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c209eb83-4215-36e6-8892-67f70336956e | -9.8821 | -44.8402 | 2026-10-08 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| afeaaf0b-1408-3a4f-9796-052e2d184f71 | -3.0992 | -57.6589 | 2026-10-08 18:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 22c4ce8d-c1c9-3529-9729-2b0223ff1ee3 | -3.1697 | -58.6437 | 2026-10-08 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 138.2 |
| cfd0d1ee-384e-3e08-a1e3-57e9d8c37a36 | -6.0075 | -53.5122 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| dea2b194-9a83-39c1-adb3-c2fb97e1b102 | -8.5183 | -67.0139 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 390d9a1b-8460-33aa-ace9-020fd4443940 | -6.4568 | -55.4609 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 31eb5c23-d04b-33dc-88bf-252e6ba10da7 | -5.9647 | -40.9383 | 2026-10-08 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 3b8efe5d-aa78-3dbe-8a44-0a1dbb170829 | -2.3115 | -57.9829 | 2026-10-08 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7c8b346f-5eb0-311f-b507-5b258e6b600b | -9.0362 | -44.3654 | 2026-10-08 18:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 0c6eda44-cbfb-35ab-b93b-aaed4a42f54f | -6.0386 | -51.7261 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| be464ac1-50d0-30cd-aed5-c92404fdcad2 | -5.6935 | -53.4464 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| edea3c7c-3c85-3461-9446-76c7a9334d3d | -6.3625 | -42.5112 | 2026-10-08 18:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| dcf43321-a689-3a2a-85ec-8c3ff6e74fe4 | -6.9331 | -43.6566 | 2026-10-08 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 8d0239b5-8001-3815-8913-462cc130a5b2 | -5.9887 | -53.5538 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| bd7a14ff-82df-3011-b1e6-3f070380733c | 1.6937 | -55.6263 | 2026-10-08 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 704a1d58-29c1-3d64-b2b9-7b4a8cec5876 | -3.4277 | -58.0397 | 2026-10-08 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 346086f9-bf63-39fd-be16-7a4b4de8fd07 | -2.77 | -57.5293 | 2026-10-08 18:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 181.0 |
| c79d3854-8ecc-3c4c-b616-f02c85ddba59 | -2.9707 | -57.7779 | 2026-10-08 18:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 44912e01-2899-3fd1-b155-bb0f230570c4 | -3.188 | -58.6241 | 2026-10-08 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| da33f63d-5082-37ea-9356-a090f4fdd1e1 | -3.0163 | -54.7687 | 2026-10-08 18:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 52b6fb34-7688-3ead-91c5-87fc8d430e85 | -6.1977 | -52.7886 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 942d7bf3-6076-34b3-923d-8fe06bc7ac23 | -9.1072 | -67.8326 | 2026-10-08 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 0bf24277-5566-3cf5-8e7d-f68ecf2f4c98 | -6.3134 | -54.7884 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| fac286e2-c07c-34e0-a16e-2b0985e64480 | -11.6181 | -43.6669 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3bc0e4dc-f7bf-322b-869a-39efd935f17a | 1.7672 | -55.5463 | 2026-10-08 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c8d3b85d-6bed-3cbc-996f-bd788320718f | -8.6981 | -47.1163 | 2026-10-08 18:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 29d419ea-fe41-3d51-b8b0-f7001341ed16 | -7.4694 | -42.8551 | 2026-10-08 18:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |


[Clique aqui para ver as próximas entradas](README397.md)
