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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4625ff4a-ef55-3c73-8051-c889d25c1935 | -2.76761 | -57.67288 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 8c5a114d-e053-3501-ad8c-64e939c06ed4 | -2.03699 | -54.30498 | 2026-10-05 17:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4e78f8be-61cf-33b8-895a-b84b0f02cffd | -9.14428 | -67.93255 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f231b2d7-92e9-3649-923e-2eccd62664e0 | -8.85725 | -66.77532 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 25721bc3-6900-36cf-a4a2-46f15ff3554c | -2.3226 | -56.84807 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 980a1b8b-86d6-3ab1-8e0f-f7b04762ccfa | -9.2059 | -66.08222 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc29e2df-a077-36b4-863b-01df79d25a84 | 1.81611 | -55.55739 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 162d3b00-4889-391f-be32-28d6fbc56b22 | -7.86725 | -54.69361 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3937f194-6a44-3a27-9d00-a73ca37bcd2b | -10.42027 | -67.97545 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 0ff49b02-d545-3b0d-bef6-5b23dec17679 | -8.87055 | -67.00188 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 315ad1ce-a5df-30f2-9a69-2f597646eeee | -9.23664 | -65.57924 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| fccbcccd-c267-3ae0-a384-24aeca26f851 | -8.54385 | -67.07346 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 65778ecb-fb5a-363d-9b3f-7515b3981fba | -9.23335 | -67.87189 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 271a1cfc-15cb-3ac6-bcc4-fa2295c3f1e6 | -8.8653 | -66.79107 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fe57233c-f862-35bb-ab99-e9334b40a041 | 1.46015 | -55.65369 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e8f50dbf-f8ff-339d-9771-22caea6355ba | -9.48565 | -68.94792 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 784fca93-4369-31b5-be1d-a33dd93269ce | -2.38587 | -56.12365 | 2026-10-05 17:37:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35e01de1-aa9a-34b1-8f20-668584c139de | -9.10311 | -67.69271 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 60eec972-f66b-392a-a34e-b1a33c98930a | -8.55435 | -54.58272 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e9b53a1a-cff6-39ef-b95a-71327385a6ac | -9.04575 | -66.09429 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a4cf3b74-701d-39ac-ae71-5554888f7e27 | -8.89147 | -66.64344 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a79cbb95-12eb-3487-9a09-a51a6af477f3 | 1.79689 | -55.5451 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ea3eeaae-d988-31d2-9582-99045ac79a4a | -8.86132 | -66.79654 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 142ef837-4bf5-341e-82ea-785748b1ea64 | -8.9525 | -69.12129 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3122feae-d76a-31ee-a828-3896fa3dfce0 | -8.66613 | -70.03954 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6072b29e-1447-371c-a660-cf18167c5d7d | -9.09234 | -65.46152 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f40b04a1-f37f-368b-b7f9-84b716198230 | -8.62377 | -69.70401 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbc44048-5f14-3199-843d-d1fc1e89b43c | -9.32321 | -66.58852 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ac11f446-8f6d-3b76-ab83-a778d9eac82e | -7.21011 | -55.18923 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 22868c53-806b-39a6-b0bf-390fe0099027 | -9.83313 | -65.01788 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5be139ec-1caf-3f4d-af41-48ecb9622948 | -8.52511 | -54.61 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| f94bd43d-377b-3e6f-b83b-98de2ba38cd4 | -9.07958 | -70.04169 | 2026-10-05 17:37:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 30.9 |
| e577d3b4-4590-3250-87f6-725070b6d00f | -9.35701 | -67.31303 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 21ed7ee6-bdc1-35b5-8a48-fb9f21e5af58 | -9.10497 | -67.82527 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ca828f1d-8c8c-3637-b465-92fb378fe2d3 | -2.01522 | -66.31597 | 2026-10-05 17:37:00 | NOAA-20 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2776e49c-1c25-38fc-b439-910511ce6355 | -2.36937 | -55.27189 | 2026-10-05 17:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ee5822f3-1904-389f-99ba-050de6ef1720 | -8.93643 | -67.34058 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| adb137bf-ad90-3c3a-b8be-4d25c4078a25 | -8.85039 | -68.80297 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c0a49f4c-1a61-30e4-bdef-e6010d20aa54 | -1.63438 | -56.00729 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2e03ca19-edf0-3a63-8cf5-a83446b1bbea | 0.65511 | -59.56874 | 2026-10-05 17:37:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 96d2c93d-e231-30bd-9380-b82f247ad432 | -10.17995 | -69.3347 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5531e8c0-162c-380d-b741-16d76175d739 | -9.41406 | -67.77232 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e53b301-e4f6-38cf-b681-79826589ef7b | -10.40795 | -69.70245 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6a453e08-8ce2-3311-b78c-6d20de2c3457 | 2.08749 | -50.90545 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ff68668e-72b6-3c18-89c7-e973902ecb22 | 3.58447 | -61.33694 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78795d56-1ab3-30d5-92c4-d9a149c88400 | -3.17776 | -60.05621 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e84927fd-90e4-3fc7-878a-32fa6f30ea0a | -8.8518 | -70.59879 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 18.1 |
| cc08ff5c-89d9-3ada-8f75-386e0f0943cf | -10.68203 | -69.08764 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 619b3bf8-61b4-3632-9e82-d34954ded5f4 | -10.02714 | -68.39985 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ad32c7d-6a5f-30a4-b236-a1d8723f0936 | -2.8321 | -67.70735 | 2026-10-05 17:37:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 458640d4-4d69-37f2-8035-8e542fa3caf9 | 1.57588 | -55.98766 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 58b8923a-2335-34e6-a1b3-365029f5a526 | -6.71668 | -55.07758 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a03a85e1-ffac-3788-bd35-059697da6f8f | -2.55166 | -65.87387 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 74347e31-ccf3-356a-9736-385bff8c63d0 | -9.65478 | -64.61926 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6973d21f-153a-352f-abbc-1ba5fa350bcf | -2.95505 | -59.15702 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b6b33135-a067-30c5-b903-2740b2dfe8d9 | -8.8593 | -66.78196 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8958879a-201e-3506-b99e-4b22d48cd3a3 | 1.81743 | -55.54852 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5e3df2df-4473-3941-a072-6bcd217d0805 | -1.8449 | -64.14189 | 2026-10-05 17:37:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 290.5 |
| 5a4c2861-b9ca-3bae-90d4-9acc170ca0f9 | -10.72057 | -69.4063 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 440eda2d-8a0f-328b-a2af-fcd62f692eef | -9.98707 | -67.89745 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b9e4efc2-e840-3cfc-9941-08253cc050c6 | 3.07454 | -60.58583 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8b3a4d44-8980-3dca-93f6-5f3b8d75f83a | -3.1755 | -60.0637 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 642784d2-20c9-39c5-bce7-e5230cf5167d | -7.4431 | -55.67557 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4f7e713f-b97a-3d33-b0d0-0779153b6714 | 1.61503 | -55.78922 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| ac29f437-7eeb-3e4f-a11e-f12fb1db1c4b | -9.89075 | -64.17595 | 2026-10-05 17:37:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c5bb1c3b-3dd9-34fc-855e-1cb07eee61bf | -1.70978 | -55.01754 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| d5316ef1-8c09-3dea-a35b-01c05012ccec | -8.94127 | -67.33996 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| fcde625c-a1c1-3af3-ac23-efd791e8ce03 | -6.46231 | -55.46018 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 59e3291c-4c69-3d8e-b408-084deb165a4f | -1.74411 | -57.18189 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 1decfdf9-d05c-3b7b-b3af-7a3e699f94c8 | -9.38714 | -68.32355 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7493c1f6-d166-3ea8-a053-dc05d08c9f04 | -1.62445 | -55.13296 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6d44d280-4669-322e-82ef-56840164ffca | -8.55901 | -54.58565 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ed148ec6-491b-3435-9885-76c6010f6b82 | -6.6793 | -55.10167 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 644339a9-9b6f-3976-bc6e-a94af47e1dc8 | 1.87205 | -55.75657 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4703f760-6b14-38f8-80b9-4b2d60eb4b95 | 3.57056 | -61.33847 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a53d2db-01e0-38cd-97db-99d6daf3cdae | 2.08927 | -50.73133 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fbf03a25-58a0-3561-ab63-7b010b567117 | -1.73296 | -56.07454 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 16e1e0fb-dbf3-3936-8c2e-7a0462153892 | -9.87335 | -65.03186 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 96673c52-998f-3637-8fe2-62a2440990b1 | -6.81177 | -55.2928 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1d908f01-1d08-32cc-873c-571ad3aac172 | 3.11704 | -60.56287 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 106b8571-6dd5-39e2-8975-b05e5167325f | -9.236 | -67.89255 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fef445d2-7f89-3b05-9390-de51ccf62eaa | -9.42231 | -68.84281 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| db4aa9d3-4483-361f-be64-cbddebdf95bd | -9.33963 | -64.71157 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76f27e48-2923-398d-ba7d-eff108c292ec | -8.85668 | -66.7972 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| ac7f1b69-9cf6-3fa9-ad8b-547327c111e3 | -0.33839 | -52.02415 | 2026-10-05 17:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 428a249e-7c8d-3471-a90e-d82a520c0b1b | -9.90319 | -68.73172 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbcb36f0-7f87-3808-90c5-66eae92e5600 | -1.73705 | -56.07396 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3faf2aba-abf7-3e84-b6cd-ee72b7f38ee2 | -2.49434 | -56.82397 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a1c8d2a1-22a9-3ba8-babc-2f8d57f3a7ff | -7.37923 | -47.43224 | 2026-10-05 17:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7a8ad2f3-e52d-3b83-8deb-9fa6ff12b43b | -10.6705 | -69.5358 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 96f6d66e-2924-3055-b232-d0250ab9fa0e | -7.11505 | -55.72126 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e77e8f88-fb24-3c45-942a-7efa0becca75 | -2.77722 | -57.66269 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 136.4 |
| a49878b8-ac59-34cd-a0f5-f4820da2cef4 | -8.90906 | -68.63747 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 6bd3a73d-6b1d-3e67-9e38-4ee54cea9cf3 | -8.97692 | -69.30497 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 47b44e59-d4bd-310c-a67e-d55ae8e2047a | 1.45574 | -55.65306 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fb7b4baf-7de1-3082-920c-05904b81945b | -2.5395 | -58.03486 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6e9ce5f-9f78-31da-83ed-e878b7c1c7eb | -6.67854 | -55.10315 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8bb2a625-8b21-3534-98a2-d553a9f437ba | -8.63391 | -66.98236 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3f74497d-037e-38c0-bf82-348134c2016d | -3.0152 | -59.20417 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7360224b-ac1f-3451-9b06-4ac56211113e | -8.58738 | -67.14479 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README146.md)
