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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a638e95a-36a4-3ac8-aef3-628ea3b57ae8 | -6.6816 | -55.0502 | 2026-09-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d90e4ac2-6bc5-3d52-9f24-632602fe71da | -6.3295 | -43.9179 | 2026-09-23 00:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 35aa3eb4-12f0-3a5a-bc65-684cac638778 | -6.6127 | -43.7549 | 2026-09-23 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 287.2 |
| 200ae4ad-8070-3b74-ad14-f286960321b1 | -8.4983 | -57.6271 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 806d148b-879d-3198-8f94-8a8e63a5c13e | -6.6148 | -59.908 | 2026-09-23 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 7b00cd54-9ff1-353c-8b01-180bb57777f3 | -3.2128 | -46.9602 | 2026-09-23 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0accc66e-6e41-3004-b6a5-d00f3a4f9660 | -7.0349 | -44.6625 | 2026-09-23 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| ef1186b2-7423-3ec7-be02-572f1a08aaa7 | -3.2313 | -46.9596 | 2026-09-23 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| b4f6354a-c3d4-3276-af36-f3acef32cf44 | -6.6776 | -58.5554 | 2026-09-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 96fdeae2-1603-32a0-94e1-b22ffca9d445 | -6.6315 | -43.7533 | 2026-09-23 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 87dbe16a-d7af-3a98-8148-f4ed84d4da1e | -3.6764 | -60.5649 | 2026-09-23 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a8213d8e-9d6f-34f7-b4f0-8c6f446f2515 | -11.7082 | -50.9598 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ec1ab5ff-e7e2-3ced-8033-6c837f59b9bb | -15.6376 | -43.5312 | 2026-09-23 00:30:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7663fd0f-d636-3f7b-89e9-a90326177bdc | -6.7211 | -44.1618 | 2026-09-23 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cfa43242-19ad-324f-989a-2e1dcb6d8d8d | -9.1024 | -61.4491 | 2026-09-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ee611e8f-e720-3a85-9929-0cb8951752df | -8.8108 | -44.2525 | 2026-09-23 00:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 525c6196-d976-37b8-8d6b-852e9ff02769 | -3.478 | -59.5779 | 2026-09-23 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9cc68741-9de6-3935-a526-8a554f7843c1 | -8.1876 | -54.7219 | 2026-09-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3cfe1ae5-5647-3160-8585-77b13ab9d538 | -11.7297 | -50.7869 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c97b451d-f9e0-3cb3-a975-84871289552d | -11.7278 | -50.915 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b9514c4d-d722-3fa8-8722-696692cc9322 | -9.1025 | -61.4299 | 2026-09-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a77d843c-38df-35a7-b563-21790e35d6b8 | -5.3453 | -45.1576 | 2026-09-23 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7162b40e-aabb-3957-832c-b71809196e2a | -6.6815 | -55.0703 | 2026-09-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| fdc00a40-9ccb-3014-86e7-42473f365607 | -6.1289 | -57.7613 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| da59f747-0d23-3098-96fe-753cbe8e4201 | -3.4781 | -59.5588 | 2026-09-23 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 65807646-0659-3d52-ae26-cdc650288ceb | -3.6763 | -60.5839 | 2026-09-23 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a6b87006-c5a5-3a86-8c73-2dcf39d3970a | -6.6331 | -59.9265 | 2026-09-23 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| cc24710f-9184-360b-b9ab-4161ec6abe66 | -6.7213 | -44.1387 | 2026-09-23 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| de6b738e-3610-394a-ae7f-2f0ca1e2106f | -8.8105 | -44.2757 | 2026-09-23 00:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 262fa912-c5e2-3c19-ba47-3127cc806f8e | -3.6947 | -60.5645 | 2026-09-23 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fd8fdb3b-6da1-3979-9db9-5aa79e9dafce | -3.2314 | -46.9376 | 2026-09-23 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 167.7 |
| 538f3a4d-7424-3aba-b37e-b7d9ff979f59 | -8.2062 | -54.7207 | 2026-09-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5cf7ddcd-95cc-3b99-9377-196399f93a10 | -11.304 | -51.3646 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 53bcfcd1-5882-3b85-ac97-037aa8434bb2 | -12.4216 | -46.9551 | 2026-09-23 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ecfef06b-fdca-3bc2-b591-bf78035f9ac1 | -6.6332 | -59.9073 | 2026-09-23 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 4c742437-0135-3a79-aa84-7894a4f076bc | -6.5941 | -43.7333 | 2026-09-23 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 886c7c80-4f9d-3f9b-a7b8-f4789aa50ae0 | -8.9164 | -61.4958 | 2026-09-23 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 81dd8ad6-9ce3-3f36-ba42-0468ef73bd83 | -7.8811 | -61.1779 | 2026-09-23 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 006b8c3e-1b14-3a34-a6bc-8317dec7747f | -6.1109 | -57.684 | 2026-09-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a5fe6d29-efc5-302e-956f-70f03529757f | -6.6129 | -43.7317 | 2026-09-23 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 247.9 |
| 97b02c62-a41d-30fb-b4ec-10e51998307c | -10.6094 | -53.9902 | 2026-09-23 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 21cff893-3df0-3a8e-a94b-9422cabf82a9 | -5.2475 | -48.1941 | 2026-09-23 00:30:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a53fa60e-245a-3945-803d-911646f01257 | -5.7565 | -45.1293 | 2026-09-23 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 95c53e72-f830-304f-bef5-d347e3a38558 | -11.7107 | -50.7891 | 2026-09-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e1b886b8-fd90-3680-8521-0295a9c31d43 | -12.79 | -50.91 | 2026-09-23 00:30:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 218110a4-a2ff-366c-a276-afa386c5e50c | -12.79 | -50.85 | 2026-09-23 00:30:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28d45fa7-21e6-30a6-8163-4c7262c34fd2 | -12.82 | -50.92 | 2026-09-23 00:30:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b642a7e-cfae-3650-bab6-fda513d560a0 | -12.76 | -50.9 | 2026-09-23 00:30:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c5959e8-1f7b-30be-a3fd-20cea5722506 | -6.6687 | -55.07 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca2dcea0-c48b-3659-9798-c72f249e3b7f | -6.8935 | -55.332298 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d3fa65-39c4-3ba0-8ac1-104c44ad7fc1 | -5.602 | -60.195 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8b0d49-3ded-3fb9-acda-19f223ed19b2 | -3.3943 | -59.511902 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8754e712-cff6-3d40-9138-9752701e0ce6 | -6.1942 | -57.7616 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72b9876f-d4c1-3146-a05e-8997f8e10398 | -10.0348 | -52.098202 | 2026-09-23 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef391ee4-d104-3704-a18c-e97b95a77568 | -11.3076 | -51.368599 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9932a8e-ca3d-306f-827a-ff943c5efaf3 | -6.102 | -57.6716 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9da97cb1-e9ed-3c12-9411-bdb625bc1fd0 | -6.6315 | -59.927399 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87c4c98b-ed9d-39af-9c80-092c734ef204 | -3.0706 | -61.195 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f25e89c7-ffb2-3bd7-b150-9cff5c50c713 | -7.3341 | -55.592499 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3d3e12-d6d1-3bec-9ae0-2cbfb7ccb437 | -3.5469 | -58.5387 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 819a59ba-d366-31cf-9b25-caa05ac419e0 | -2.8575 | -60.240002 | 2026-09-23 00:36:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5561e7ac-83c2-380d-90a6-94cc4e7a4eba | -10.4469 | -51.267799 | 2026-09-23 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2d3b2a5-85e5-309a-9364-5cab516c015d | -10.2452 | -49.959999 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b22cfb8-bc19-3bc4-8cb7-5a11b33e9eb2 | -4.4224 | -55.0765 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5906d3f8-b7f4-3a38-a1f0-26abc5b47506 | -3.8559 | -58.814999 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46d68ba8-4f8a-39f2-9fb2-c97123061311 | -4.2761 | -48.605301 | 2026-09-23 00:36:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ade025ef-9f60-37b2-8643-a698335bde22 | -3.0672 | -58.009201 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd45fbc8-1399-332f-89e3-862ba0f3b6af | -8.7935 | -60.7822 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edcf1e65-d2f1-3771-9d02-4997e8030fad | -8.6173 | -54.616798 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12722833-8c11-3c8c-8000-4145ef4e474e | -2.5809 | -57.406898 | 2026-09-23 00:36:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0f2fdd6-3aa0-310c-a03c-9f942cb3ec70 | -3.0824 | -61.2019 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 541a8596-158f-3645-a0f8-b640697ebaaf | -8.1797 | -54.8228 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6ab223-9fc5-3f31-b795-2462c64d2413 | -3.6832 | -60.576801 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8025f975-dbc4-3f07-8416-4071a7c93bac | 1.9067 | -60.574402 | 2026-09-23 00:36:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4e109364-bbe2-3ea7-be52-9c0a91bf7ecc | -1.9159 | -58.249802 | 2026-09-23 00:36:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77cbbd9d-005d-3197-ba9f-f64f5115e37b | -6.6082 | -59.914501 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57338791-af4c-37b5-81f0-d123b239dd84 | -12.474 | -46.9757 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e87301d-8bf8-3d79-9b5f-2202bda47c61 | -3.1819 | -56.828999 | 2026-09-23 00:36:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f93fa92e-8bc5-3f0a-b7a0-747b0ef26543 | -6.3007 | -59.963402 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 764b8af3-680c-34b8-8a6f-fc7ea3c11540 | -7.5397 | -61.473701 | 2026-09-23 00:36:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9566f72-9ce5-3b31-b615-158f71a54739 | -6.1291 | -59.929901 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50a1a656-2782-3d0f-a93f-8b929248f6d4 | -9.8495 | -48.311298 | 2026-09-23 00:36:00 | METOP-B | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce83ab2-5898-3b86-9f75-9517d8dca5e8 | -3.4582 | -59.521702 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ab26e35-7286-3de5-98fb-9fb3a0799c9d | -5.2305 | -48.183399 | 2026-09-23 00:36:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8c108a-8494-390c-bacb-0783cc64d54c | -6.6235 | -57.979099 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf870624-2162-3398-96a4-6c8fb742c6dc | -12.7855 | -50.8941 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e814ed95-de97-3bd8-8ffe-09e24e6dbd2c | -4.5214 | -54.968601 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f9b058-40de-3cfd-9b9f-4471723e5076 | -11.2987 | -51.331299 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 697f8f99-4371-3699-81c7-fbb1f39da63a | -4.0642 | -56.219601 | 2026-09-23 00:36:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4f4a78-ef1d-31f2-9765-f126462e5c71 | -3.2859 | -59.4412 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7a9098c-9fc0-338d-a9b2-6e66cc6f53be | -3.8198 | -58.883701 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d526867-55db-3525-b310-e99c6759eb52 | -3.0192 | -57.933201 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b32465d3-b96a-343e-8b08-cbc7cded8f54 | -6.3507 | -57.771198 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8e0411-f4d4-3bcd-83b5-429da01f821a | -6.5192 | -58.297199 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b9b083f-0b48-301d-b748-52fdb922ad1c | 1.6542 | -60.3703 | 2026-09-23 00:36:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 173fb66d-0924-3f37-8af7-1dd3c302484a | -5.895 | -52.0863 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bbdeccb-7e8c-3e81-9443-33f3f3a9835b | 2.7816 | -60.217701 | 2026-09-23 00:36:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 10043518-cce0-3f53-951f-24097cffb7e3 | -6.3745 | -55.271702 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 955ca1c8-a541-3092-a769-0a2e864b9eb9 | -4.8651 | -55.842201 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4656a35a-2777-31fc-beaa-7ec41146da13 | -5.9804 | -57.771999 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
