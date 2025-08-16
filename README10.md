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
| bb4de34b-5ed9-30e9-b63b-76a83435f353 | -7.4176 | -60.009998 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55d602e5-e071-353e-be8d-f3bc12afbb09 | -9.5171 | -60.513802 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6d3bf15-540b-3044-9031-c893fb56cb5f | -8.9715 | -61.654999 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83380974-6d45-3fa3-9ce9-101b0c975bfa | -7.5256 | -61.310799 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc36262d-207a-3ff0-b160-1240f82de031 | -6.9334 | -59.6292 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 670644c8-fce5-39db-8150-572d36e3f167 | -7.4598 | -59.921101 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc30bee3-52f4-346e-b2da-4e702d311129 | -9.1679 | -59.6535 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cead6037-e4e6-325a-8766-4fc9c4e57b1c | -11.3601 | -55.383099 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef81156b-a389-3302-a96e-9d0826fcffcb | -12.603 | -46.9282 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7f820bc-9a1a-3b1f-ba58-daaacc575673 | -8.9913 | -60.547501 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81276f48-0fc5-3bca-8166-04dda8db9e7c | -12.5893 | -46.954498 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 241db1c9-80ab-3af4-89a9-dd4fbbf0c563 | -7.825 | -61.320599 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3b8409e-9682-35e0-bb4d-fd75498918ca | -8.9886 | -60.4869 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2aef1d-7eee-3bc7-ab8e-dd7bb8d4a1ea | -7.9306 | -61.717602 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63590788-dc41-3a44-b3ce-f79c82e523bf | -13.4803 | -60.984402 | 2025-08-16 00:47:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db07f62c-ec9a-3aaa-bfd4-d1467436829e | -12.5879 | -46.909901 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd011e27-07ae-3be9-9b77-8a4a6d8a287f | -7.4406 | -60.021099 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3255e3d-63a0-3a55-8bf4-4bb4188cc9aa | -2.3687 | -47.6563 | 2025-08-16 00:47:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5eb17ab-086e-319a-ae86-c69cd07fbb42 | -8.9993 | -60.536999 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03643012-3db2-354a-9891-5a5f7e1c94fe | -12.5315 | -46.970299 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b952787-bc50-3805-9ea0-cb3c22d8553a | -7.4389 | -60.0135 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3ee2b82-eac1-36da-9636-230e864165b6 | -9.1792 | -59.610802 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b6769d7-a0bc-30ce-a99d-b0fe048b5998 | -12.5838 | -46.933498 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 187bfb6d-1331-3fce-bb64-a336c5144961 | -11.3585 | -55.421501 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdb5db36-4f4e-3570-8b06-5fd255635221 | -11.2493 | -50.461498 | 2025-08-16 00:47:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60647a99-ada4-39fe-9c90-4830807e452b | -14.9494 | -54.752701 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cfb0568-6253-34f5-b565-e3f7de948b50 | -9.1956 | -59.6394 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03c49781-ac1b-32e5-a849-72facdd0ec53 | -11.3519 | -55.392601 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 479a2749-2c43-3ccd-8f9f-3c0dfed5c6c0 | -12.5783 | -46.912601 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d775992-4678-333f-9b1c-d0393d97102f | -3.8221 | -47.732399 | 2025-08-16 00:47:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af036573-3122-3845-9f69-ff68c4be3318 | -9.5091 | -60.524399 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1755ee98-a4c3-35fc-87e7-1543fb3fe7aa | -7.9327 | -61.727001 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90e01467-00b7-3078-bc92-362221f1957e | -7.9208 | -61.719601 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6437b32a-6f13-3796-aef8-1f75d433b6fe | -9.1777 | -59.651299 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a40ce62-744b-3d65-ad4c-dd836c258dfb | -8.1214 | -61.174 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c49b592-294c-37db-9288-514350f5638c | -12.5989 | -46.951801 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3f0c7e4-1231-380c-bf27-365ae4368289 | -6.94 | -59.986698 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdaa4e94-8c4e-3345-90c5-34e3517744fd | -9.0055 | -60.5182 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d695fb15-4b9d-3d26-811d-31672d1f901e | -8.9859 | -60.5224 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8aaabb59-d6d3-35a6-b7ba-d902cc19f759 | -9.5189 | -60.522301 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2bd82c1-9609-3d16-8362-18b9f3dd24a9 | -11.3568 | -55.414299 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf34fc0-be7f-3a4e-a342-0110da726fcb | -11.3487 | -55.423801 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 183d0785-b658-3a7a-9129-523d020f5f35 | -7.9482 | -63.196499 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab04008-e69e-3c49-9cd0-798a6c828518 | -6.6358 | -60.0056 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca3f9d0-66f4-387e-9bd9-0e9b16099ad8 | -7.4517 | -59.930801 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25462001-d50b-3f36-909c-e1d705db49ca | -11.3601 | -55.428699 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f13db46-f2da-3380-acea-c7ba97546624 | -11.3683 | -55.4193 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f557f658-1b70-3329-a4c0-d26c9988f5d8 | -9.1696 | -59.661201 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed07150-e40c-3e51-9e48-1bb8d7c8b957 | -9.5055 | -60.5075 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 231c82e6-d4b4-3c02-bd17-e8c7b72a7f43 | -12.5164 | -46.952 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd2c8da-4aeb-31b4-8363-5b64efac2683 | -11.259 | -50.459099 | 2025-08-16 00:47:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf089266-39e7-36ac-bcd9-8f7fdf8ecb9e | -6.5638 | -43.0357 | 2025-08-16 00:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 286c009a-c42b-3f54-93bf-4d1ea1d29b95 | -9.1708 | -59.6568 | 2025-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 367529ce-5d30-3bd1-a98c-2423de575137 | -9.0346 | -67.427 | 2025-08-16 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 8a3993b3-1155-3663-bc89-79602a55f767 | -3.821 | -47.7227 | 2025-08-16 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9463c04b-4087-352b-b12a-473ab070870e | -11.3466 | -55.4326 | 2025-08-16 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 950dc72e-fee9-343b-96d7-b7d73fb3b931 | -9.4994 | -60.5278 | 2025-08-16 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| f83dcad9-c883-3de1-8e98-562da57fca85 | -14.9628 | -54.7351 | 2025-08-16 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 3ea87f2c-7c51-3b1f-bc4a-1451a5aa0f67 | -7.9148 | -61.7478 | 2025-08-16 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b09ce5fc-30ca-3a6a-8549-8ee6b911e532 | -14.9632 | -54.7143 | 2025-08-16 00:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 0ebc197e-2893-3782-8d8a-7a92eeae53b2 | -9.4992 | -60.547 | 2025-08-16 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 7faa689d-3496-3925-93a1-5c4d7efede1d | -4.9305 | -43.2558 | 2025-08-16 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| aeb370f9-fd4e-36ea-adb8-97c7740f8970 | -14.9435 | -54.7374 | 2025-08-16 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6c4c50ca-4265-399e-ab77-64ff661c3c16 | -13.1074 | -57.1511 | 2025-08-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1a0ee591-4e89-39fa-a9cd-df48bb3ad386 | -9.5179 | -60.5461 | 2025-08-16 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 3f2bf3c4-5589-3e88-b959-e403d16c25b6 | -9.1709 | -59.6374 | 2025-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 4f565ad7-bafd-380c-ac7c-4cde16fbc6d4 | -9.0531 | -67.4265 | 2025-08-16 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2f9cfb35-bcf0-354f-a7cb-ca877ea208d6 | -14.9438 | -54.7166 | 2025-08-16 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 207.9 |
| d7814ae2-5a6d-3130-ac9a-f0bd11419f66 | -8.9706 | -61.7224 | 2025-08-16 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d62c9551-6f3f-3a43-930e-5dba4f54be9e | -7.1325 | -59.6569 | 2025-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f48c31f7-d60a-3973-9fe7-f4de3248447b | -8.9708 | -61.7033 | 2025-08-16 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 48b7bd1b-ab01-3f3c-be0f-22ed637fc62f | -13.1267 | -57.1293 | 2025-08-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 2b9f4c4d-bbd9-3a25-a3f6-8bf3e9c775c6 | -7.8247 | -61.3327 | 2025-08-16 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7a9cc7b7-8b1a-37c1-91d0-b06f85c8f73b | -9.518 | -60.5268 | 2025-08-16 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8a67a5e9-a19e-3a98-860c-d2efd22e3b8f | -14.9245 | -54.7189 | 2025-08-16 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 42f0651a-d838-38ae-bc62-009e94786225 | -7.0404 | -59.6222 | 2025-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| e666df57-d7f1-34e9-a523-e6aed99ebc41 | -13.4294 | -43.6733 | 2025-08-16 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| da16e30d-1154-34f3-8a88-61d4d9d5e5c9 | -14.6023 | -47.9018 | 2025-08-16 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 0d62728e-6a5a-33a5-b49f-af5dafbd3d19 | -7.9149 | -61.7288 | 2025-08-16 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ebc03129-d5cc-36af-a364-2c3f866287a3 | -9.2082 | -59.6354 | 2025-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| edf315b8-222c-304f-b12a-aa62817200ed | -14.9441 | -54.6959 | 2025-08-16 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| fd39fdd4-4f73-3773-9233-0a18e9cd9971 | -6.9486 | -59.549 | 2025-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 23dca5f4-e95d-383c-ba4b-5fd946c3aa98 | -13.1265 | -57.1494 | 2025-08-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 41998a0a-2b25-3fb4-9854-0c88d05df576 | -9.1522 | -59.6578 | 2025-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| db352a17-85c6-39cd-9402-858f9ec5b31d | -8.9893 | -61.7024 | 2025-08-16 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4c3286df-e807-3352-a166-73e2c2103b17 | -14.5828 | -47.905 | 2025-08-16 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 54950613-e75a-3a14-8607-a5d13b13e233 | -8.971 | -61.6651 | 2025-08-16 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 09d2b8ed-3a8c-3ff9-bc69-1e783ebc40c6 | -8.9709 | -61.6842 | 2025-08-16 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 115.7 |
| af75a252-14d8-350d-9d87-e7c6373b5556 | -4.9118 | -43.257 | 2025-08-16 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| af9fb4a7-af1e-3b28-8655-baa839986510 | -3.8209 | -47.7444 | 2025-08-16 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 08be31a3-04a8-3c21-bae1-4f53e3a0d6b6 | -13.1077 | -57.131 | 2025-08-16 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| b4d666d2-96b1-38d0-bcc5-99e32455b224 | -9.1711 | -59.618 | 2025-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 944beb94-6a21-3119-9313-d53c59faec21 | -18.0467 | -47.7253 | 2025-08-16 00:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 3bcac6a6-3a1c-3c01-a8c0-c5f290fe4eac | -7.0796 | -59.2351 | 2025-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e280efa6-3100-3891-a63c-72543755aead | -11.3468 | -55.4124 | 2025-08-16 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4e48251c-c385-38b4-8ffb-4ba2e7dbce0f | -8.9523 | -61.685 | 2025-08-16 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 93f3d26c-469f-3fe3-8fde-e70615382d71 | -7.0612 | -59.2358 | 2025-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1ed3a020-5b7f-3d91-9037-ef1b52a60044 | -6.9302 | -59.5497 | 2025-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2fa5b787-d09d-36bf-81e3-8c8378a7e968 | -2.3763 | -47.6636 | 2025-08-16 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 526941f5-9d46-3227-ae7f-82afa0aeb7d7 | -9.1523 | -59.6384 | 2025-08-16 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |


[Clique aqui para ver as próximas entradas](README11.md)
