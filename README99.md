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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22ef92a1-9f54-3da5-bece-17a1284ee503 | -9.4079 | -60.3013 | 2026-09-17 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 59458bb4-3fd2-3b97-ae09-33069b83c7c4 | -6.0256 | -59.9293 | 2026-09-17 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 22861376-387b-3f14-a6a0-acf15c60bbb8 | -9.3567 | -50.1796 | 2026-09-17 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 11bbe88c-1139-31a6-b3cd-631f3cc045f8 | -7.8227 | -44.8175 | 2026-09-17 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 355.9 |
| d5e62e0c-a6e8-3544-87eb-c93fd20ba3df | -9.3572 | -50.137 | 2026-09-17 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 736793ff-6dd9-3fe0-a02c-2363cfef7751 | -12.6628 | -50.8264 | 2026-09-17 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 59a46791-bc1e-3559-91c6-2ea84a1a7ce7 | -9.7497 | -46.1089 | 2026-09-17 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 6856c6a4-a059-35e3-a473-42f53dd0957e | -14.8376 | -59.5515 | 2026-09-17 15:50:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 79825a10-4845-3ac6-b4b2-00343144365b | -9.3758 | -50.1565 | 2026-09-17 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 5337e403-61f2-3c5a-861c-b004b79dcfe0 | -8.4983 | -57.6271 | 2026-09-17 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 212.3 |
| 7c64a15f-e8ac-3007-a88f-e526f586bd97 | -8.411 | -54.7274 | 2026-09-17 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 497f52c9-f8df-39f5-9f30-fc55be334ebc | -9.3763 | -50.1139 | 2026-09-17 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 06fdcabe-11a6-3b61-9db5-2af58f398100 | -9.7979 | -60.4734 | 2026-09-17 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f4a93a16-e076-3c4b-8aee-6165a6654080 | -14.8183 | -59.5532 | 2026-09-17 15:50:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 93cf6f40-befb-33b8-8975-f599dcacec54 | -8.4797 | -57.6282 | 2026-09-17 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 191.7 |
| a65810c7-47e7-307e-894f-13e8d2fdebb2 | -9.8322 | -48.3417 | 2026-09-17 15:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e1543941-9867-3250-a85c-21c3507eebcd | -10.7923 | -46.1845 | 2026-09-17 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| c7187d98-3795-3d9a-8ba1-a7da92cf9500 | -9.3765 | -50.0925 | 2026-09-17 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 5f7ded6a-0aa7-3348-beb6-365c0e55bdaf | -9.5512 | -45.4296 | 2026-09-17 15:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 177.3 |
| edbd21d3-c31d-3baa-a5af-8c4ab53db74c | -8.4296 | -54.7262 | 2026-09-17 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8ae0a7c0-fcde-39d3-819c-189ad9da502f | -7.1389 | -42.1051 | 2026-09-17 15:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| d4a2a386-fc1e-3aed-8a90-3ced82d65b39 | -6.1108 | -57.7035 | 2026-09-17 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| a42c979b-7475-310b-9e3c-320a5faecc58 | -11.738 | -50.2295 | 2026-09-17 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| d73c49f6-17f1-380d-9579-9ff7be9fa875 | -12.0464 | -49.9776 | 2026-09-17 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| fb37a995-5c7e-30c0-975e-00d181bd8e37 | -9.9512 | -45.2902 | 2026-09-17 15:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 826eaafa-983e-33f7-81ca-db8fd2459c0c | -6.4484 | -60.0101 | 2026-09-17 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| b14e7bd7-0335-346e-80fd-143dc74bd06d | -8.396 | -47.2121 | 2026-09-17 15:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 9d139a22-cece-3246-a0f7-ba01f2a4ac80 | -8.4669 | -44.5445 | 2026-09-17 16:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 16b8ad79-d463-38d1-9911-60a241d3beac | -9.5512 | -45.4296 | 2026-09-17 16:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| b0dca9a8-eb0f-3894-b56b-1994bbb61425 | -7.8033 | -44.8651 | 2026-09-17 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 186.2 |
| b968bfa2-c16d-31b3-aee5-4448899a5097 | -14.8376 | -59.5515 | 2026-09-17 16:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ede936a4-5c5a-36b9-9313-8a63a05c342d | -9.3765 | -50.0925 | 2026-09-17 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 2ae78f85-5644-3541-9c3d-9ea29bc233ef | -9.3572 | -50.137 | 2026-09-17 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d30a5045-0aea-3fe9-85f8-eb7152aa3137 | -15.5397 | -53.8081 | 2026-09-17 16:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 398a3b02-ce79-3620-a1d5-ddbc0fb75fe3 | -6.6767 | -58.7105 | 2026-09-17 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 9b8dde48-46f5-390b-9d2f-27eab4f65b0d | -7.8221 | -44.8632 | 2026-09-17 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 8e6873be-ea82-3986-a66f-79c3de3628a6 | -9.376 | -50.1352 | 2026-09-17 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| ac38206b-c701-39f1-93b3-6ba716286232 | -12.3578 | -50.7991 | 2026-09-17 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e01c5bdf-75aa-3df4-a6f6-63131c7f1e3a | -12.493 | -50.6972 | 2026-09-17 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 1eaef608-007c-30dc-b105-bd421e664aa1 | 1.261 | -50.872 | 2026-09-17 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ddae1ec5-eb20-3874-92cd-97b8274cc495 | -6.6952 | -58.7097 | 2026-09-17 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1301470d-ba4f-3914-85d1-2396591e37bf | -9.3948 | -50.1334 | 2026-09-17 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| bfcef05b-6133-39cf-8dd1-d9fd79925078 | -14.8183 | -59.5532 | 2026-09-17 16:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0a6754ef-d5e5-33d5-9909-e756decc9188 | -12.4722 | -50.8068 | 2026-09-17 16:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7e5b087f-594a-398c-b6a5-11ae8c027a63 | -9.3763 | -50.1139 | 2026-09-17 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 2fc3495f-f396-3d67-92f2-1b2e290b050f | -8.5431 | -44.4902 | 2026-09-17 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 162.9 |
| e86aed0d-6e43-3655-b57b-e0297f511f08 | -6.1108 | -57.7035 | 2026-09-17 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 001f6d7d-819c-3b46-956c-26d90a61d6ce | -9.5512 | -45.4296 | 2026-09-17 16:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 223.3 |
| a733c3b6-2f57-35a2-bcc4-71e069d63869 | -15.4817 | -53.7947 | 2026-09-17 16:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 426d8b5b-a71a-3f5f-8865-c59b77f31e98 | -7.8224 | -44.8404 | 2026-09-17 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.2 |
| ceb737f1-bfa4-3885-8143-292d3c7c30c0 | -9.3567 | -50.1796 | 2026-09-17 16:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| ba82c8e5-4925-3bef-b6a2-90e888d3b86c | -9.8322 | -48.3417 | 2026-09-17 16:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1665e83b-a16a-3857-812e-e7aab8877d3c | -12.3578 | -50.7991 | 2026-09-17 16:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8070e33d-7440-38bc-953b-8715fe3744fa | -14.8376 | -59.5515 | 2026-09-17 16:10:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a699bb0c-7ef4-392e-bf6a-5445f9ccf538 | -7.8221 | -44.8632 | 2026-09-17 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 2454331f-bff9-3fc0-b336-dea59f1ecb3c | 1.9241 | -50.8202 | 2026-09-17 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c1307b71-76be-3cb8-a7b6-41c47a2cf718 | -7.8033 | -44.8651 | 2026-09-17 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 339.6 |
| bdb9a7fa-8da3-3e70-8d97-ff7761f52d9e | -9.8884 | -48.3794 | 2026-09-17 16:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 4d285793-6dd0-3762-819b-2f0f88a2c01e | -12.0273 | -49.9799 | 2026-09-17 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 28f570c2-14cb-3631-a7bb-5e6151871e8e | -12.6826 | -54.6763 | 2026-09-17 16:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| f9c4079d-9991-3f26-8ba9-1ad85b850c2f | -9.3763 | -50.1139 | 2026-09-17 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 4f60f33c-355e-3472-9523-013dc66d8d69 | -12.1501 | -64.1414 | 2026-09-17 16:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| bc6f97b5-d5e7-3ae1-99c2-468f6f6d376b | -7.8224 | -44.8404 | 2026-09-17 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 49d2efb4-e5b2-3674-9b17-1ba08c2f79fa | -8.5797 | -44.5783 | 2026-09-17 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 500.3 |
| 303c6c43-bfee-35a7-98a2-b4d52edc19a7 | -9.5512 | -45.4296 | 2026-09-17 16:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 304.7 |
| bb9810a2-f310-3f55-ac05-5a31ddb4f57b | -9.7687 | -46.1067 | 2026-09-17 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 4010aad5-3509-36b0-94a5-eedaf660cf05 | -9.7497 | -46.1089 | 2026-09-17 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 95cd18db-ce91-3414-a1c7-3b270088e6da | -8.7949 | -46.9069 | 2026-09-17 16:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| a927f52c-75cd-350a-bdd5-ae60ad9d2b69 | -10.7923 | -46.1845 | 2026-09-17 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| f57812b0-8d8f-3c9b-9581-c29c182581c4 | -7.8221 | -44.8632 | 2026-09-17 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 199.1 |
| c27c05a0-3380-393b-a74a-8c8aff0869cf | -9.7877 | -46.1045 | 2026-09-17 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 2edccc99-19d9-3f90-bde7-760b227988d8 | -7.8224 | -44.8404 | 2026-09-17 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 224.7 |
| fb26465b-056a-3bd4-9a5f-52bd23b0e388 | -12.3568 | -50.8634 | 2026-09-17 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d1deabe6-4aa3-3310-91b8-ffd1f6729c82 | -12.3571 | -50.842 | 2026-09-17 16:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4bae9940-ca36-3360-9b64-ac7f93631e46 | -12.6826 | -54.6763 | 2026-09-17 16:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| e0b7d899-eecf-3b0b-98da-3fc752629a21 | -7.8033 | -44.8651 | 2026-09-17 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 293.1 |
| ea20166e-8a0d-322a-8174-c2c1fc42e0d3 | -9.3758 | -50.1565 | 2026-09-17 16:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 88a37fa9-f986-3a01-876d-82e265dd4e74 | -8.8644 | -45.8919 | 2026-09-17 16:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.6 |
| cd96612f-4fe6-38c0-a80f-c5524d048aac | -9.8322 | -48.3417 | 2026-09-17 16:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 685232d9-8cb5-352c-95ef-2d3977ec7adc | -9.3572 | -50.137 | 2026-09-17 16:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d2c64d25-d5fc-3b8c-9ad1-c0bd173945b2 | -11.6972 | -54.5672 | 2026-09-17 16:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e4f3fd4d-7a0d-3700-a276-16f26584b0f3 | -8.7949 | -46.9069 | 2026-09-17 16:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 87ddc828-e07c-3ec4-92a3-41ba7dd06fb5 | -9.3569 | -50.1583 | 2026-09-17 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| db44627e-67e4-321a-a341-6a0ce6279c12 | -9.3758 | -50.1565 | 2026-09-17 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 2a70b7a7-67a6-3a23-97e9-4194632ff5ec | -12.6826 | -54.6763 | 2026-09-17 16:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 55a186ca-a117-3222-ad8a-6972b381f41e | -9.3943 | -50.1761 | 2026-09-17 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| a81caf0b-2b34-3b1f-81a9-ef9e4b0051c6 | -8.5797 | -44.5783 | 2026-09-17 16:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 5088a32e-abf7-3180-bcdd-0bb7e915d57e | -9.3755 | -50.1779 | 2026-09-17 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 1b2cdf2e-566a-3e71-a84f-824abfc7aa55 | -9.3753 | -50.1992 | 2026-09-17 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 95452182-3fb3-37f2-94fd-d8598ecc0019 | -8.8644 | -45.8919 | 2026-09-17 16:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 178.4 |
| fdb5f15a-44da-3225-b79c-8c6b88443b30 | -9.3567 | -50.1796 | 2026-09-17 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| fdd5899c-9bdd-3214-9c8f-5132a8d870f5 | -12.6826 | -54.6763 | 2026-09-17 16:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| fcbcc1ae-6636-3f80-a78a-ab353077fffe | -8.396 | -47.2121 | 2026-09-17 16:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ce274370-62ad-3aea-a95c-6475e87c5edc | -6.1478 | -57.6825 | 2026-09-17 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 20f0a68d-7e3b-3534-ab12-d854d3253248 | -9.8322 | -48.3417 | 2026-09-17 17:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a17dd4ef-7d19-33e3-80c9-24c5555e7b5d | -9.3765 | -50.0925 | 2026-09-17 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b1139365-8412-326f-a286-f9765f6f2e31 | -9.8884 | -48.3794 | 2026-09-17 17:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 71b36b1b-5d25-3cff-a95c-aa5563f374d7 | -6.7684 | -58.8035 | 2026-09-17 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| eaf3a242-8d06-32b9-a43b-b8893db96ce0 | -6.1478 | -57.6825 | 2026-09-17 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 19b05920-0100-30fd-8a6b-efdddcbf96fe | -9.3943 | -50.1761 | 2026-09-17 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |


[Clique aqui para ver as próximas entradas](README100.md)
