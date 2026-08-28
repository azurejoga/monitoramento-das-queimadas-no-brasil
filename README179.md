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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8a47990-e8e8-3b37-85fd-a5167dc65e08 | -9.2477 | -57.0697 | 2026-08-28 20:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 223feb4c-d507-3e1e-af4a-a85ec200abd0 | -14.3376 | -51.702 | 2026-08-28 20:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3e7530e3-b056-3de3-90a8-da29b4b14e86 | -10.7407 | -54.0401 | 2026-08-28 20:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1e1430ca-c193-3c64-b590-2a77edc3110c | -14.3762 | -51.6969 | 2026-08-28 20:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ef67ef2b-8e7d-3712-b5af-0e979306ee36 | -14.1788 | -48.7481 | 2026-08-28 20:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2ba3da61-dfeb-3b3e-9289-e675f8d245d7 | -4.1696 | -42.4346 | 2026-08-28 20:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 7da040db-8680-316f-a957-cb2c166ef203 | -6.425 | -43.7478 | 2026-08-28 20:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a7ac32f3-65b1-38e8-aac2-483e54313b3d | -21.5147 | -55.42 | 2026-08-28 20:10:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 119.2 |
| d5832704-4330-3f2f-9899-5ba9fbde03d4 | -9.9288 | -60.4277 | 2026-08-28 20:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d19e40c3-d8b4-3bd4-a7ec-eb7e37d96b0d | -9.1239 | -61.0078 | 2026-08-28 20:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 69d51ae7-00fc-3364-b3d4-a2619cea4652 | -9.1525 | -49.9639 | 2026-08-28 20:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6b9fb587-0e9c-302a-948d-b28ff6f4be1f | -11.0445 | -57.2023 | 2026-08-28 20:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 334.5 |
| 7028ad61-40dc-3277-ae6a-a0bea17e161b | -14.2027 | -52.8432 | 2026-08-28 20:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b05205e0-d28f-3870-9eb6-8f2de3600240 | -8.0301 | -48.0145 | 2026-08-28 20:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d51c4338-2bc8-396b-9cc9-420af66bd1d1 | -2.7304 | -47.0424 | 2026-08-28 20:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| f932f59b-4382-3baa-acba-840d5d2f50a8 | -9.7264 | -47.7827 | 2026-08-28 20:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| fddef63b-b9e9-39b7-9002-64a4d58b75c8 | -8.5968 | -54.7957 | 2026-08-28 20:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 0651a873-6fa5-3176-96e9-0893f69382fc | -14.9386 | -56.3216 | 2026-08-28 20:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| ecd1f670-97d8-3958-97dd-84e82ef23b65 | 0.1549 | -60.412 | 2026-08-28 20:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a56bd7a5-8e59-3df3-a569-6e01d5dc76ea | -9.5102 | -56.9338 | 2026-08-28 20:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d2c60859-b3f6-3b39-80a3-cea946f58a26 | -3.6034 | -60.5284 | 2026-08-28 20:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| ffd63e98-5dc8-3644-b4f7-f1ceaf779a1e | -2.533 | -45.3168 | 2026-08-28 20:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 19d347d7-2d77-3825-abf9-af688906af79 | -9.1238 | -61.0269 | 2026-08-28 20:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 38d60ec1-f242-34fc-bf8b-6d3691d95d58 | -10.7791 | -53.9752 | 2026-08-28 20:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9a224887-c39d-3152-a110-65d304bc93dd | -6.9521 | -58.9506 | 2026-08-28 20:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 20223141-6a6f-3136-b706-ef56187e8753 | -9.1424 | -61.026 | 2026-08-28 20:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 84e14cab-1211-3c66-90d2-152eca4b2002 | -11.4972 | -45.084 | 2026-08-28 20:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 32e5a34f-6f4e-37fb-8b53-9a992e7138d3 | -6.7248 | -59.9998 | 2026-08-28 20:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| feae4c0a-7142-35b8-8a3a-6ed5352a1631 | -7.5289 | -61.3825 | 2026-08-28 20:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| db560d1e-3ba4-31f6-b0d3-2426b546b15b | -14.3569 | -51.6995 | 2026-08-28 20:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 277.9 |
| 5d2e315a-e52f-30c8-9ffa-be97c242d14e | -8.5971 | -54.7553 | 2026-08-28 20:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 85a566d8-defc-3f4a-90bd-2ecff788a97d | -14.9015 | -52.6055 | 2026-08-28 20:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2036b19a-2377-3391-ab85-9cfd20a2040c | -13.5991 | -45.772 | 2026-08-28 20:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 82c1a90b-a0f9-39c1-b7d7-7a3dcb675e61 | -11.7167 | -54.5244 | 2026-08-28 20:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 18e77553-dd12-3fa4-9d5e-c45c4a259828 | -5.2709 | -45.1173 | 2026-08-28 20:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 294.0 |
| c10e7082-85e0-3377-9c65-82c96847b6a6 | -6.1657 | -57.7793 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 43fcd7d8-196f-3304-ae0a-ad6c3b7aefd2 | -12.3608 | -50.6061 | 2026-08-28 20:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 200.3 |
| e52e7ff3-0dbd-3ce8-992d-447014a1380b | -4.9779 | -49.6017 | 2026-08-28 20:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| bfcb9683-57b1-3d4f-b9ba-d2af670b2d43 | -9.8028 | -46.373 | 2026-08-28 20:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.2 |
| bd162f04-b286-377c-af20-0566288eedc8 | -12.7603 | -44.2608 | 2026-08-28 20:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 273.7 |
| 135c37d5-35fe-3f61-91e9-01e95021951c | -9.971 | -53.9214 | 2026-08-28 20:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5a50c163-dccc-32be-be6e-2ac9f4d048b5 | -11.7165 | -54.5449 | 2026-08-28 20:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 470be028-e3e9-3316-b0b9-04f10c128ba7 | -17.9676 | -50.1985 | 2026-08-28 20:10:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 223.6 |
| 2f50d10d-7f4c-3208-a96e-7317066bfdde | -9.02 | -57.5377 | 2026-08-28 20:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 8aa0e3df-e787-3c44-a851-497a75e801f0 | -5.9819 | -57.6892 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e4d667ce-7916-3131-b816-9aaddb60d627 | -21.4947 | -55.4019 | 2026-08-28 20:10:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8d804787-d309-30cb-8280-c002efe1f6f8 | -8.6156 | -54.7743 | 2026-08-28 20:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7728587b-8112-3068-822f-0f5a0e959fc6 | -5.982 | -57.6697 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d1a1b7cb-ee81-3ead-95ad-452cf54fa4bb | -5.399 | -43.1999 | 2026-08-28 20:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 280.3 |
| 9acf42e8-fef5-3bde-801d-01c43a28abcb | -4.9778 | -49.623 | 2026-08-28 20:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 6a3e7f50-2efa-3a1f-9b35-c27302c40a2e | -12.3615 | -50.5632 | 2026-08-28 20:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| cddf4a0f-bad4-31ee-80cc-6dbcb92d56a9 | -11.26 | -54.02 | 2026-08-28 20:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73616414-687d-3ed9-baff-230a72187c9b | -12.36 | -50.59 | 2026-08-28 20:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce9fce9-625e-38dd-aaea-2569a14e9b2c | -17.1068 | -47.1795 | 2026-08-28 20:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ba4195ee-daf2-3fdf-b21a-7c90e5ad40c5 | -9.8739 | -60.2955 | 2026-08-28 20:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 214.9 |
| f70189e7-8619-3693-bfbe-24c72fc4130a | -14.1978 | -48.7673 | 2026-08-28 20:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 9da4d355-b2ae-388d-93a9-986e3bde6a5d | -2.7119 | -47.043 | 2026-08-28 20:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0c15ee4d-3d28-3e04-815a-a2ffec62f1c1 | -8.6197 | -70.2189 | 2026-08-28 20:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 93.9 |
| fbb02927-4776-35c5-9e93-6ee9920a9e3b | -8.5971 | -54.7553 | 2026-08-28 20:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| fe0cd5bc-f9f0-319a-91dc-f0fb0f53f89a | -6.7504 | -58.7268 | 2026-08-28 20:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 538313e9-febe-34d5-84b0-b6bdda86a3f3 | -11.6978 | -54.5262 | 2026-08-28 20:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 83d82468-70ea-3161-9280-773c568e4139 | -6.9521 | -58.9506 | 2026-08-28 20:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 8d9da39a-14fa-3370-b2f8-9461aeb2decb | -11.2128 | -53.9976 | 2026-08-28 20:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| f4f16105-e62f-3967-8e7b-1308a18643bd | -14.603 | -50.8928 | 2026-08-28 20:20:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f9b98905-88f9-3d3b-ba82-350633e15aea | -10.5711 | -59.6149 | 2026-08-28 20:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 41dde430-6d0c-3761-960f-ddc809068396 | 2.2375 | -50.7723 | 2026-08-28 20:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7a9e032c-0b5c-3d0a-8600-6a1b8fd9ba12 | -6.1473 | -57.78 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5fb8b331-63fd-3f3f-8711-03bc950e891a | -6.4908 | -53.2629 | 2026-08-28 20:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 655ce5c9-8510-3b0d-bcef-a6b7b0c45bb3 | -12.7603 | -44.2608 | 2026-08-28 20:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 43fad3de-618e-3d48-8aca-4b28256f3d77 | -12.3803 | -50.5823 | 2026-08-28 20:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 74b26949-840f-39ab-af3f-46be5ee48df4 | -11.0443 | -57.2222 | 2026-08-28 20:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 441.8 |
| c392bcdd-8eb1-3fb6-9628-45b9645483bb | -9.8803 | -65.0327 | 2026-08-28 20:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 25ec6d40-ca8e-3486-acb7-1fb9692baa10 | 0.1367 | -60.412 | 2026-08-28 20:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 117.7 |
| e9d0b5ec-312d-38f5-a543-42fa7b548bc7 | -11.7165 | -54.5449 | 2026-08-28 20:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 171.1 |
| b4ecea25-2719-38cf-b0de-8a92c5d14cca | -14.2027 | -52.8432 | 2026-08-28 20:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| addebb77-a150-3f1b-8193-929fb99ed5cd | -9.0198 | -57.5574 | 2026-08-28 20:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3357ba6c-f242-3ebe-a53e-d8d26748c105 | -11.4968 | -45.1071 | 2026-08-28 20:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f3d5f927-a0f4-3429-9d88-e241c25293ca | -9.9708 | -53.9419 | 2026-08-28 20:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 6326217d-28a6-3b8b-9316-cd350f57f545 | -11.0441 | -57.2421 | 2026-08-28 20:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 7ed08f5f-3fe0-302f-b286-37c3e74549e0 | -7.5478 | -61.3056 | 2026-08-28 20:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 289.4 |
| 448879b0-dbe2-3e51-8f52-01b4541bc0a4 | -3.6033 | -60.5474 | 2026-08-28 20:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 8b5152ea-f1f7-3289-a59e-66093ea19344 | -13.8752 | -54.1153 | 2026-08-28 20:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e6027cc0-05cf-3235-81ef-342f0b4a2822 | 0.1549 | -60.393 | 2026-08-28 20:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 41d2611a-c9ce-3f3a-bd97-76178ae242a5 | -10.7596 | -54.0384 | 2026-08-28 20:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| f652d4d3-0b29-3a13-bf62-102c88cdbce5 | -9.8737 | -60.3149 | 2026-08-28 20:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 62838659-a731-36c0-80bc-dd4364a64547 | -6.949 | -59.4719 | 2026-08-28 20:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| b90e86b3-20fd-3362-822e-128d8b63bb6a | -9.8617 | -65.0334 | 2026-08-28 20:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 155.9 |
| d9c674e3-8c87-3a01-9311-1626e32826f3 | -9.1739 | -56.9754 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c2b9c5b1-86eb-318a-b2b8-4718e509756f | -6.1656 | -57.7988 | 2026-08-28 20:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b594e432-01b5-37d0-9dba-f6496fae5ec7 | -14.9193 | -56.3237 | 2026-08-28 20:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 37fd4ec8-a296-327e-a594-fd40947c2422 | -5.2711 | -45.0946 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e21ea89c-d3ee-3156-a2d4-95853943d572 | -9.1978 | -61.0809 | 2026-08-28 20:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f363bd76-d70c-3661-8742-eff089c92fea | -13.5991 | -45.772 | 2026-08-28 20:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 56bd5de4-fee2-34cf-ade2-d99e197dff63 | -6.7247 | -60.0189 | 2026-08-28 20:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| b990b652-959c-371f-a318-049c7f2bb9a8 | -8.7757 | -50.083 | 2026-08-28 20:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e4ec8742-6698-3bb8-8012-b0378774e10f | -14.3565 | -51.7208 | 2026-08-28 20:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 4e750654-5eeb-31f8-b09f-3b272df4d094 | -10.7598 | -54.0179 | 2026-08-28 20:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ea3af933-5ebc-32b8-8de8-e789c603fb4b | -8.6012 | -70.2192 | 2026-08-28 20:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 6daa97a6-94bf-3eea-9acf-72f8e64cf017 | -5.2522 | -45.1185 | 2026-08-28 20:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 013cef25-e0f4-3b94-b617-f082fdc95a71 | -14.9011 | -52.6267 | 2026-08-28 20:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |


[Clique aqui para ver as próximas entradas](README180.md)
