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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2af98a97-c016-3825-b141-907b204317cd | -10.4525 | -57.94826 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5116745c-4e86-3baa-85a3-389168ddb10b | -8.95841 | -65.9638 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1048303f-f6b9-30d0-a072-b994ba93d178 | -9.58361 | -54.46741 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 518954d8-64bb-3ee7-af0a-07086b206179 | -8.34053 | -62.93581 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66d927f7-66ac-3d36-b250-814cd7d6b2e3 | -9.45155 | -60.54809 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| daf07552-3821-38e0-8509-b4433a29c0e5 | -8.69964 | -64.21039 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acac9ebe-23c5-3f99-8e5e-551643869a36 | -11.83701 | -46.45342 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a4432eea-8dfb-3230-9f7e-2b0d7a1739a8 | -10.37573 | -57.83181 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8ff97e5-1e5b-3b53-8d89-041cbdfc397c | -9.43739 | -62.3288 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b291793b-e700-3f1b-8fd1-e738d7bc8543 | -10.98741 | -46.84589 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a880c5b-84b7-32e6-81b6-bfac2c0f2fac | -5.81931 | -46.36577 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 89f1c3bd-1e51-38d3-9899-93da50bdb8c0 | -6.59675 | -43.64336 | 2025-08-30 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5059181f-98bf-30f0-bb07-c1a03a6a8d84 | -9.108 | -65.76486 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 76cdd9aa-fc8b-3050-9dfc-ff41c2c0d608 | -8.34174 | -62.9287 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b140712b-3c47-3a4d-902a-a0dcec46b7aa | -8.90526 | -62.09909 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 642a5008-3afc-3ba4-9a6f-fce9cc5cd368 | -11.22091 | -55.0592 | 2025-08-30 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93dfe8c1-fda6-3d9c-9eb1-85bb9824f4bb | -9.46554 | -62.34832 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a8ffed-19d5-317b-b1bd-8769aa0908af | -11.86416 | -46.44544 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2d40dca1-153a-3391-8113-47bdff4d4c47 | -7.72308 | -50.2711 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f1cb0cc8-3a84-3cdd-9d47-4426f5437e38 | -9.44645 | -62.34497 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e962407a-7767-3f80-aee1-01a3a6a14e79 | -11.88346 | -46.39746 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ef83d53e-4876-34ad-a0e4-f84f3fda88be | -9.44344 | -62.33953 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a4e02da2-f7f4-32cb-ba27-84f6a9ea3e31 | -9.19856 | -59.6982 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cb57884-3f5d-3bfe-9bf4-3714a004d5ad | -7.14529 | -44.91323 | 2025-08-30 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7336ce4-29f6-3fd0-b88c-b1b4c9ac7b18 | -9.44885 | -62.3307 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 94fa2538-9fc4-3924-a7bb-fa69e5f6b384 | -9.17236 | -59.57379 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dc97748-6422-3cd1-b2c9-c03f49e55be4 | -9.44378 | -60.54328 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 782dd65f-bc7a-326f-b0a2-7c8982a7df23 | -9.4481 | -47.63883 | 2025-08-30 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e03abbde-34ae-3010-9305-0ab89993b3b6 | -9.50967 | -54.43994 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80a47eca-bb09-38da-843c-ed05e6d63177 | -6.37613 | -44.34503 | 2025-08-30 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2091aa5-3c16-3cad-b306-417ace88aee9 | -8.5156 | -54.71699 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15de4d4a-4f6d-3955-8ffc-52fb3170a479 | -8.17798 | -61.36478 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79e375b8-7937-3f0a-8fa8-553f73e1d39b | -11.84574 | -46.43484 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 518e2694-708e-37db-bf2d-85c77882b1f9 | -10.54198 | -56.38609 | 2025-08-30 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df817249-f20f-36db-a096-ed43bdda6412 | -7.09036 | -44.31338 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48f92d0e-e2bc-35f4-900f-0e5a3500ac1e | -11.58316 | -46.37058 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 200b11dc-ff6a-3b4b-bbe6-3e8514b35a55 | -11.58298 | -46.3695 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 45a09ed2-5aee-3361-807e-4cea7871bd81 | -11.91362 | -46.70224 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfe5e2d8-9c07-3b36-b0ca-d3ce7c974cca | -8.56104 | -63.01369 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4e7d7bd-62e6-35d8-babf-ffd54b8b96a5 | -8.89766 | -62.09785 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f44f2d3a-2f13-3682-b750-3a23bdbf9d34 | -8.54834 | -63.01513 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a5223e9-393f-35fe-95ae-c4c68d963ab3 | -7.73401 | -50.26244 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bc88c5e1-c876-3b2b-9d3a-c59e282e52db | -8.62468 | -67.2437 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd78cab2-c4db-39b6-bcbc-a411fe01f23f | -10.3697 | -59.20086 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb575934-00c0-370a-9a4c-0d03f870b7f8 | -11.85061 | -46.39324 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00b2c34b-700b-3cab-aa7a-f48765c61a98 | -11.9177 | -44.86261 | 2025-08-30 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bc75166-9f2e-3755-b65c-744e512fd214 | -8.28485 | -61.42183 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43930dfa-a3c9-3003-820b-63062e9ad5a2 | -8.25693 | -61.45298 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bd41c93-9ac2-37cd-b1b3-8a958b6f3606 | -8.63881 | -67.25697 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad59780a-ad86-30d1-93ad-e44331798310 | -11.87203 | -46.37892 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04ade522-4736-3403-8c8e-d90ffe159d8e | -8.71487 | -50.37199 | 2025-08-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c5f640b-8ced-3ba2-b43d-3602ce07e475 | -9.58773 | -54.49089 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d061d369-441f-3eaa-8f30-b587718bdbf8 | -8.28925 | -61.4181 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e721d461-f9c7-324c-b6c6-eb6e02977c68 | -8.42973 | -62.2928 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f28eba9-817e-32eb-b82e-18a5f25013db | -9.59827 | -55.39135 | 2025-08-30 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4dfb407-9dca-3604-8895-d55191d79930 | -9.44325 | -62.36405 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d440409-eb10-351e-9103-0ceb63141185 | -11.9369 | -46.6857 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0189250-eda0-332e-9b97-52f44f46cf1f | -9.63093 | -48.2997 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d83b9ec-4d3d-364d-bb1d-8063dcd66bb1 | -9.16502 | -59.57629 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a2e4c3-168e-381b-88a3-2d86ac205e4c | -6.78251 | -43.7742 | 2025-08-30 05:10:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2e887653-1509-3584-b011-ee9231e5e85e | -11.83117 | -46.85963 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f85a051f-a95a-31af-9613-716c60123c04 | -9.4358 | -62.33824 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 483785d2-ffa8-3783-b7b9-5fc9512a1337 | -11.83394 | -46.8597 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b53399b-8ffe-3342-9743-ac7aae335d73 | -10.36637 | -59.20031 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02fd0a68-4df1-3a12-b8d2-819c158b390f | -9.45439 | -60.55254 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91c9f462-0dd6-3c5e-8ea1-29d85b8de342 | -7.11613 | -44.60678 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d20d5408-9bd7-331d-b35a-bff31a636267 | -9.16735 | -59.56175 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d0740fd-2c6b-34e8-9f9d-64d1f64214ac | -8.17285 | -61.37287 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2580b4c6-c3a7-363a-8087-62b458a7d323 | -10.03304 | -46.03846 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dd5d11d-06a8-32f4-869e-a6cc66e3ad2b | -4.87303 | -46.8523 | 2025-08-30 05:10:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1891d9dc-00fa-31ff-a2b5-f87ef36499fd | -5.99425 | -44.72771 | 2025-08-30 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c212728a-4cde-3f05-ad3f-b71aaf8a9836 | -9.24834 | -56.89781 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f47ea149-3105-3bff-b163-5d29a8f2dc55 | -9.44696 | -60.56789 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b7287bdc-cd56-3361-a44c-6114fa13844b | -11.83272 | -46.86977 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 21cd6c3d-d28f-3844-bb5e-835a2ab6a3bc | -9.17625 | -65.79933 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d39a42ea-b47b-3b65-b772-faa6ab7e4525 | -11.92356 | -46.68934 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd8e3a41-194c-358f-ba6a-8cd8171eec24 | -10.33641 | -59.19527 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff63f62d-a958-305b-8193-835d0752f29e | -9.45592 | -60.5649 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83fb4241-762d-3129-bcec-dd3c49b850e8 | -7.72379 | -50.26614 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3d57b822-ecd8-31d6-abea-d7097785b16d | -9.14987 | -59.56267 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7b8a46b2-9aad-315d-bbf7-74a45aced5fd | -8.05706 | -45.42081 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c02cec2-d888-325a-9f36-86603197793c | -8.66715 | -62.43316 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1cef271-e81c-33b7-a32e-f82ba4647b5b | -8.17725 | -61.36913 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2634d4e4-ed81-345d-8c7b-fcc658092749 | -9.43776 | -60.55831 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1dabe310-40f7-3fed-85b8-1eb477fb9ced | -9.13399 | -65.81336 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a28a20f8-a57e-3eaf-8f84-44f97c5f07a5 | -9.58338 | -54.49472 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9d8fb64-4480-32f5-957f-b63f4206dc36 | -10.37351 | -57.82426 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cebcc7e-fde7-3244-ab79-2bd5f8bfc037 | -7.61653 | -62.72376 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b63fd843-5f95-36a0-b33a-4b0081d7cca1 | -9.22016 | -60.87 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a50a49b-53b2-3e77-85b3-3d79d0126c4f | -11.07382 | -52.03783 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c406594f-09d9-3b2c-b650-1c7a76f32898 | -9.15649 | -59.58619 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbd5f40c-6c0e-3a81-afd7-f19ca96a8b55 | -11.14417 | -47.15154 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 285e76e8-92ff-3cb4-a10d-eb61922f28e8 | -9.45875 | -60.56941 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ad55169-f3d6-3f34-aa04-00c431993ce4 | -7.40419 | -49.52443 | 2025-08-30 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 467e7b8a-a946-33bf-8bfb-492fd8658b68 | -9.24497 | -59.77755 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af99c6d9-f6a4-3e50-a448-fecf06b00769 | -9.60069 | -55.37537 | 2025-08-30 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61c97fc9-7e9d-3c80-bc67-c114799abbfe | -8.52607 | -64.00961 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 110cd049-544a-3d8b-a7fd-f3189dcee7da | -9.44229 | -47.63797 | 2025-08-30 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e407503-d882-37ee-a775-aa552fcf1f9b | -7.40827 | -44.29607 | 2025-08-30 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 467067c3-eca8-342b-aee2-2400a2ef590c | -9.46014 | -62.35711 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README68.md)
