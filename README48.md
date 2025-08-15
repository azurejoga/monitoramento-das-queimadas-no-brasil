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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff108f98-f7c1-3ab5-9941-7ed4cf8ed552 | -6.68876 | -58.82852 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a33605f-6cc8-3101-b025-39d78e1f0616 | -9.15774 | -59.65632 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15262bee-a5bd-3786-9ff1-701e3254ed02 | -9.15262 | -59.65981 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03c1d150-dcda-3e02-9ead-65039715ef5f | -6.94065 | -60.12538 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 90a924dd-f831-3713-820e-6831e3eefc3a | -7.32653 | -60.62007 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9019a448-8f06-3728-8726-1e437a9780a1 | -6.91049 | -59.14074 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea73618-3d95-3f70-9f56-9e25251f56ee | -7.87775 | -61.8179 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1791cdd3-3592-342e-b157-9b32d73a1903 | -7.24248 | -57.65931 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3358de20-bb95-33bc-b20b-bc755b5ffd59 | -7.41744 | -60.03694 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50ceb702-f5bd-3ffa-b439-b875814bce9b | -6.89881 | -59.12988 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12cfab02-0e1d-3471-9296-5370c6ad2e0e | -8.11022 | -61.19085 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 69f995b7-dcff-31ff-b6dd-27eb6f670477 | -9.18894 | -59.68398 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c5c78ae-907b-364e-8793-1f66023e5fa7 | -13.04522 | -56.84084 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab06a954-af48-36c0-aa0b-02a9fdd424fb | -7.95676 | -63.46022 | 2025-08-15 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49fc6c8a-dad3-3c8d-94ca-9ec541f4890d | -9.49864 | -60.55346 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fce02c8f-d94f-321d-bec1-20677f05528e | -6.99661 | -59.98526 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34ac2356-07cd-36f2-a1f2-b97d9938eb18 | -14.79325 | -42.72776 | 2025-08-15 04:51:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c83e938a-87a5-3174-a755-ea2ff943a24f | -6.69813 | -58.85141 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30f59bcd-19cd-3883-8aa7-20d9eccb18d8 | -7.87436 | -61.82876 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 732bd896-e874-3771-9958-173ce9e34ea2 | -14.78961 | -42.72731 | 2025-08-15 04:51:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 405a4411-fc3d-3d8a-8d2d-fe976dd9095b | -13.12064 | -57.14951 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33b76997-06ad-3433-8f86-51752a5efab0 | -8.10532 | -61.18301 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e280a549-ea05-31ce-9641-6228358fd350 | -7.87819 | -61.80691 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 123a4204-2205-31b9-a3ae-52f07e063876 | -7.32268 | -60.61921 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 966b1dd3-14b3-33be-b2c9-0176c283b2ed | -7.24298 | -57.68061 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e6023e4-7224-38ad-b8d8-b86fcd2dd11e | -8.10427 | -61.19557 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b591eace-3c63-310e-9d69-8ba35e93eec4 | -7.31601 | -60.6292 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21cb4885-0c64-30a7-8450-d09e565475c2 | -6.65684 | -58.82064 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3b94c5e4-ca15-3b11-85d9-ad399a1deb5a | -6.91912 | -59.53804 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d80ef74b-39f1-3d68-9524-1d547122680a | -7.94618 | -61.76311 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 233390f4-e07a-35d6-8971-da8d4947a139 | -7.53626 | -61.34516 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91039197-c53d-3022-a76f-a1adc4247fbf | -9.18982 | -59.65306 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd486528-1628-361e-92e9-c9cbd7b50f7a | -12.75343 | -44.41698 | 2025-08-15 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae46b7d7-7bdd-33e6-9bcb-a84f7e7c36bf | -8.91056 | -60.7361 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba5a3531-193c-3e08-b487-a48e15cce92c | -8.31636 | -45.02403 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53179a2c-8ccf-3ec6-b3a5-0c24f86527a4 | -9.79143 | -61.50309 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8258a621-c5f1-3d7f-bc1e-9c31ff90a26e | -6.48324 | -62.94161 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a43aed43-ce74-3e23-a55b-6e6495feeb7a | -7.60122 | -63.50771 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c071f016-ab56-3594-a069-e7aa3861abfd | -12.78747 | -45.96154 | 2025-08-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d07f7b4-fba7-341c-8d2c-166dcbc7da11 | -13.12202 | -57.14122 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7d2f68d-eace-3f28-9fb5-90788c60e544 | -6.9273 | -59.14796 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d952761e-81b8-370e-923b-4f02a3a2cfb4 | -7.9394 | -46.85006 | 2025-08-15 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 371ff6e8-10e0-393c-b2c7-24226f985086 | -6.94828 | -60.13711 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 074f22fc-d865-3c0c-8de3-46b5f88a7532 | -13.32805 | -45.21912 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 326f342a-9796-3764-84c8-822321fb75fc | -11.55137 | -47.32175 | 2025-08-15 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49007d2d-dcff-39c4-b44e-724c6b4344ea | -7.32176 | -60.6246 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5a16601-133d-3054-8cf9-b42741ac9fb3 | -8.09941 | -61.18773 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 02936cdd-8094-3b13-a38e-50cd5c59241e | -7.94437 | -46.84641 | 2025-08-15 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec844379-0c02-3090-a842-150fea45c893 | -7.43838 | -60.02548 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 350657ce-f4a8-3c54-a93f-4b6c19e68259 | -8.30798 | -45.01128 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ff95474-0cf7-3ff4-acb7-6dc521b6d5d5 | -6.70025 | -58.83899 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83b67a90-9cba-328b-bcb1-4e17d591ee2d | -7.32557 | -60.62544 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86becb38-1b60-3b9b-b833-344164c238b9 | -7.87764 | -61.81004 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e29cbe12-cbd8-3465-a3ba-803785021bea | -6.48255 | -62.94556 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 90405ac9-8316-32ef-98bc-64aded2cd542 | -6.93978 | -60.13042 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d2b9f15-69d2-3d30-86d1-2c0f5eb68037 | -7.43177 | -60.03022 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 424a18eb-ccdd-34a2-9a41-194bd582c386 | -8.52144 | -43.29858 | 2025-08-15 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f7655aa-5836-3e16-a587-158b53f5a745 | -8.10326 | -61.20116 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c6c7ebc-e20d-3fff-be32-05dcb9e6d3ad | -11.31443 | -55.20576 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6034139a-ebf1-34ac-a206-47c9634208f3 | -7.07359 | -59.2174 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81346c76-456a-3ae4-8d45-70804bdfaabc | -8.32295 | -45.01303 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f357893d-9408-3388-a8e8-4b4278c4ba1c | -7.93534 | -61.76437 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 89e8dfae-fc8d-3c8b-aa35-da466b059414 | -7.43378 | -60.02465 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 720771d4-23c2-36b3-949d-4fe364dc0bfa | -7.57227 | -47.06451 | 2025-08-15 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ba2bc7e-ac66-373f-be11-ff3c16fb8394 | -9.16407 | -59.69719 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fa597da-bd00-3a92-9fc5-5880db2979ba | -6.54073 | -56.2007 | 2025-08-15 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c15bf94f-8ee1-3d5f-81a6-8f5647c0132f | -7.43 | -60.01895 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b743ee99-ab6e-3771-a987-f367758c1a1b | -7.95187 | -61.76093 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8e9d145-54de-3d3d-bc3b-d43362bdf980 | -9.50035 | -60.54371 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9080c423-7667-3dd8-ae78-fb8e43ee42c0 | -6.8937 | -59.13343 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7138ef17-8985-3a8e-a9b2-17563f0c43c7 | -7.08676 | -59.21967 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e29c0150-f0b7-354c-bf51-0d5f50ca6152 | -7.41617 | -60.01653 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 419958cc-108e-36ab-9502-94831709cdca | -7.07652 | -59.22666 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea64644e-7bed-3195-8dbd-4af96b9d05ac | -7.94103 | -61.7622 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35afeb06-925f-37f8-be2e-d7e5b724413f | -7.43294 | -60.02959 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e91b7d01-ca91-3a4e-9832-0176077ab1e6 | -14.06299 | -46.30457 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9317690-b4bf-3317-9685-66e308cbe751 | -9.15205 | -59.42424 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f95dcda-2559-36ac-a750-e3baacfa626d | -7.94893 | -61.7477 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d134423c-5027-3192-9bb1-ca49cfcb87bc | -11.34465 | -55.42495 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37676f37-41e7-3ac7-95fe-e7339a19bd2e | -9.50081 | -60.51391 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d9c0b3bd-9c45-3860-952e-f692608ac2c5 | -7.28643 | -57.6581 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fc051a1-54c5-3bce-8fa2-22a018661a32 | -6.87695 | -59.15234 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ceef9e4-9550-35c4-89ac-01cdb2a9ba80 | -14.90786 | -45.19012 | 2025-08-15 04:51:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1d6e4f1-8b3d-32a4-b86e-43bc109ea7a1 | -6.87265 | -59.83541 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1506a98c-0ee7-3d72-9dd3-a6dd9229fa2b | -9.17945 | -59.68667 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bc0d982-3141-30f6-b526-2b34684caff0 | -7.27975 | -64.69329 | 2025-08-15 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 733fc351-7041-34d3-9f4a-83001ed21625 | -9.20715 | -49.67433 | 2025-08-15 04:51:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e2ab17-3b7d-3b37-89c9-a66658d96c2d | -9.15395 | -59.6778 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f547bb3-f7f5-31a2-9622-c859d810c346 | -7.15086 | -59.63971 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09f7945c-cf5a-3462-bdb4-03f18f0e057b | -7.9438 | -61.74671 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7e1c5a0-2fa2-3154-ad8d-4c9a541a40dc | -6.69375 | -58.82522 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c98966d3-38f4-3d7e-9f9d-049836b9ed4b | -7.82255 | -61.32989 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddc07229-22c1-3b5c-9bcb-546488e671cc | -7.1242 | -60.12128 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b024367-59b1-350a-bf6f-091a4b1d6930 | -10.1852 | -49.50468 | 2025-08-15 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a8e4b0d-eca8-3a2e-a255-dc431608495e | -9.50198 | -60.55492 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 17949fab-4d34-3ca2-b765-bf3096e1c7fd | -11.02902 | -45.06961 | 2025-08-15 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8b43409-a886-3d8e-9717-4e1f305ecf6b | -7.60977 | -63.52637 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc070f5-d6aa-355f-a3fd-aa0bb220d45c | -13.12211 | -57.16256 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0c0b59b-cffb-3487-b392-a9a4a2881a1f | -8.303 | -45.0106 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27272a7c-1170-3574-8861-c5d24cab745a | -10.35576 | -50.81072 | 2025-08-15 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README49.md)
