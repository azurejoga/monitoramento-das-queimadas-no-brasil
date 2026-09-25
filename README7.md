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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 508b28d8-c21a-3666-b612-79ec01ad3f1b | -9.16663 | -60.76686 | 2026-09-25 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1b56b4f7-2c1c-3eae-bf66-06d322a09bee | -8.27073 | -70.80972 | 2026-09-25 01:20:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c643d055-cb07-3bc6-9527-857391004e86 | -8.03501 | -71.25761 | 2026-09-25 01:20:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d9f10e75-6354-3ce9-a703-56ad58249239 | -9.06386 | -65.69743 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| f2188f54-2711-32a9-ac85-d270b9852ead | -7.51479 | -70.39 | 2026-09-25 01:20:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 33597c73-9f83-33b8-b0eb-0527482dcf4e | -9.12524 | -65.76122 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b49eceff-6c3b-3797-ad38-27996051ca49 | -9.47165 | -67.07526 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 44a0d3ee-24b6-3a57-ab21-4aa25b05e018 | -8.78512 | -66.59373 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83515a8c-e9e3-3634-9573-9685a07b770b | -8.03635 | -71.26782 | 2026-09-25 01:20:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4c7e7aac-4857-3603-a815-ee64908c67fa | -9.37947 | -66.50338 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7be52afb-fc53-3343-b30b-9af3bafb07c2 | -9.38094 | -66.5134 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e92ef6ac-f353-38b8-8717-3df400dc50a5 | -9.07367 | -65.69601 | 2026-09-25 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 31b55fe7-7339-32db-807a-25032b17dbae | -9.54595 | -65.98254 | 2026-09-25 01:20:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e6c7a575-b53b-3c61-881d-549cf75602c3 | -7.39843 | -64.36751 | 2026-09-25 01:20:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a9fe5557-044c-3a45-b466-a5e140cd6558 | -7.4037 | -64.3843 | 2026-09-25 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ff9f2bd3-fc00-36d4-8bb3-6e6e9d53933c | -12.1685 | -50.7147 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9f1bb2c0-3630-360a-af2b-c15da8518e46 | -3.25 | -46.9369 | 2026-09-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| dec20ff1-1bd7-3e76-b65a-641f9c4b2d3a | -12.0727 | -50.7474 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9ee8ab56-f342-368f-a3b5-fe7c49983ed0 | -12.0731 | -50.726 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e7c8ec8d-6a43-326f-a003-da923f41d1dd | -12.1872 | -50.7339 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 0fd02b64-8373-3f29-9d78-5e69fa3c8514 | -8.34 | -44.1427 | 2026-09-25 01:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| f8b7f0a9-7e2f-3354-a11e-3d107353eb27 | -3.2315 | -46.9156 | 2026-09-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 2d7735e4-0faf-3feb-a8a0-35abf6c3092b | -11.7849 | -50.9086 | 2026-09-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 87fb5fe9-f062-3a82-9a0f-2cef525846c6 | -11.959 | -50.7179 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 152.4 |
| ac82181e-a29c-3d9c-a3a9-1d6cd7f63c63 | -11.7846 | -50.9299 | 2026-09-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 2dfe9cee-c8b6-3037-9fb6-90ef3f20a450 | -6.9863 | -62.9908 | 2026-09-25 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e2aac639-52b0-3efe-afc3-25f77b7e409b | -9.1535 | -59.4834 | 2026-09-25 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| eadbbab2-245f-354b-b154-f52cfe3f61a1 | -12.1678 | -50.7576 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 92be07b3-c2f5-3bf9-938a-7d66172fb979 | -9.1536 | -59.464 | 2026-09-25 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8caa8412-0ed1-383d-80bd-4c80d13f1a3d | -11.9399 | -50.7201 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 179.6 |
| fc6880d8-8ddf-343b-a8c8-8fa6ae2037ff | -11.804 | -50.9064 | 2026-09-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 215.6 |
| f7dd01c1-ef9d-3f89-9101-d18d1cb17e76 | -11.9402 | -50.6987 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b0e0aff2-c179-343b-9ff6-b0bae0c6ee3d | -12.1675 | -50.779 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| bfdbbdcb-b12f-3c82-8e79-15bc7fc6d6de | -9.1722 | -59.4629 | 2026-09-25 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1314b6ab-f1b9-3b50-b50d-319032524839 | -12.1681 | -50.7362 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 4b20f71c-5983-3b3d-8cd6-005e465edb72 | -11.8037 | -50.9277 | 2026-09-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 150.4 |
| e1d82464-0be6-3662-86db-4fb5f1bea7a0 | -1.1461 | -54.0996 | 2026-09-25 01:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f424cbe2-93a3-32e6-bb50-a43aa5e3df17 | -7.4038 | -64.3656 | 2026-09-25 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| cc9fb038-1722-3452-8942-bc8daa14b096 | -12.0609 | -50.2773 | 2026-09-25 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 25220556-8c67-3045-826a-51aa4928a39e | -11.8227 | -50.9256 | 2026-09-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| a98d5306-ca70-3e56-ac80-09b92ddaca76 | -12.1491 | -50.7384 | 2026-09-25 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| eb6dc963-8d59-314f-a11b-799820c98198 | -12.0799 | -50.275 | 2026-09-25 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4e09bb43-9020-3344-b12c-5bf5eeee52cb | -6.9862 | -63.0096 | 2026-09-25 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8764693d-9c02-3f8d-ba86-33b0bca86fce | -8.3211 | -44.1447 | 2026-09-25 01:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 89926928-b6f2-3d40-8a60-f681aa88fcf7 | -11.823 | -50.9042 | 2026-09-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| a3e4881a-b40d-318e-89bf-92998f5186df | -7.3854 | -64.3662 | 2026-09-25 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| de9cb1b5-fd75-3240-b52f-dac22567fd61 | -3.2314 | -46.9376 | 2026-09-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 535a7148-5c17-3e1f-ba83-b93b6c17d007 | -12.05 | -50.26 | 2026-09-25 01:30:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38c27c26-a285-3ad5-ab67-99a0fcfe3428 | -5.3891 | -49.1752 | 2026-09-25 01:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b2756bde-1075-3a09-ad00-b44ee0cf3063 | -3.2315 | -46.9156 | 2026-09-25 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 4d0e77e7-5cb8-3869-b305-dbc311d7a7f3 | -12.0609 | -50.2773 | 2026-09-25 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 25d19043-368a-3cb6-96a2-2240a4b96199 | -9.1535 | -59.4834 | 2026-09-25 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 51cf0138-03c6-37b8-af05-81b4d3022ec4 | -8.5891 | -48.3564 | 2026-09-25 01:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 5d9dca9f-797e-332b-9730-c7c2c8fdaa32 | -8.6077 | -48.3764 | 2026-09-25 01:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5aace179-91e0-3e7e-a559-090146ba8e2a | -9.1721 | -59.4823 | 2026-09-25 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 789a9958-9989-34f5-9390-2f191165ae1a | -11.8037 | -50.9277 | 2026-09-25 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5f093d02-eaa2-308b-b0d1-4eda99013807 | -11.9402 | -50.6987 | 2026-09-25 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 0c75785a-fa1a-38d0-978e-6170299c55f0 | -11.9399 | -50.7201 | 2026-09-25 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 215.4 |
| f4a07ab9-3f85-3d4d-9d9c-df2634c3305a | -14.7344 | -46.2219 | 2026-09-25 01:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 89dbe46b-1339-33af-9def-1d8f53b0733e | -8.34 | -44.1427 | 2026-09-25 01:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 3e890f57-a7bc-3122-be8b-9f8ce4b74b25 | -8.5889 | -48.3781 | 2026-09-25 01:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b7a09bc5-f0c7-347d-8db9-a48140b036ad | -3.25 | -46.9369 | 2026-09-25 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 75af040a-4281-3fdf-aa88-83b5b3e862d8 | -6.9863 | -62.9908 | 2026-09-25 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4aa5ed29-255b-3f9f-8313-7ea32824d8c0 | -9.1536 | -59.464 | 2026-09-25 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 53e20f1f-b1cb-3e0f-81ca-7ecf9531ef89 | -11.2859 | -51.3031 | 2026-09-25 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f025b472-fdf8-3b0b-939c-5c7ff4f9d9e7 | -11.823 | -50.9042 | 2026-09-25 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2efafb2f-2397-33fe-bca7-2795ef612a6b | -11.8227 | -50.9256 | 2026-09-25 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| f92b962f-a5d9-31f4-bd52-c16b3550265a | -7.3854 | -64.3662 | 2026-09-25 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4c42ae82-a787-328d-a320-ac93d9f550f7 | -6.9862 | -63.0096 | 2026-09-25 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0c6b09b3-3b77-3e48-8722-ff18bcca1c90 | -1.1461 | -54.0996 | 2026-09-25 01:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| fc08d99c-db13-354f-85dc-792677ba9a76 | -11.804 | -50.9064 | 2026-09-25 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 7e80d90f-2040-3dff-8fab-f37f6b6f5d5b | -11.9593 | -50.6965 | 2026-09-25 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 5ef6d562-e45c-3b3a-8fd5-4927f3f94d2f | -12.0799 | -50.275 | 2026-09-25 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 3057f016-977e-32f6-a88b-8a95228f6781 | -8.608 | -48.3546 | 2026-09-25 01:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5a3238e4-b7f3-3e74-9674-8680aab4c6e0 | -3.2314 | -46.9376 | 2026-09-25 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 034c70fd-aeca-38d9-a332-3c777bc8ac74 | -11.959 | -50.7179 | 2026-09-25 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 9c4394ca-879a-38e5-8793-a32333c95382 | -11.9586 | -50.7393 | 2026-09-25 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 9837a5f8-97ab-389f-8db8-70012bf77bb1 | -7.4038 | -64.3656 | 2026-09-25 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7614a97d-67cf-378c-9940-f7fcd6713f55 | -7.4037 | -64.3843 | 2026-09-25 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 41665b47-611d-37b3-9121-4b540ae8f699 | -3.25 | -46.9369 | 2026-09-25 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| d42a62cd-621d-37f1-a060-575b7be19f74 | -1.1461 | -54.0996 | 2026-09-25 01:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 8e94683f-1126-3f71-8672-4e6a56330ebf | -11.2859 | -51.3031 | 2026-09-25 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8aa3efa4-e101-366c-b2d0-28c7594281ee | -11.9402 | -50.6987 | 2026-09-25 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| ebbe76d1-ab35-340c-b504-8cb6d0c81500 | -11.8037 | -50.9277 | 2026-09-25 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9d4f9699-2be3-3b8d-a2e5-c5d093838d4a | -9.1536 | -59.464 | 2026-09-25 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 1119a3ec-7fa3-3b81-ae15-50bf57f120b6 | -11.9399 | -50.7201 | 2026-09-25 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 188.2 |
| f7c07de1-d926-39c7-af4c-eaa302e8ee35 | -7.4038 | -64.3656 | 2026-09-25 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 7372a47e-e5a5-3b18-beed-7e8f4194faf9 | -3.2314 | -46.9376 | 2026-09-25 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| dc7cb3c8-b2fe-365c-8b7e-968fb65bb1fd | -3.2315 | -46.9156 | 2026-09-25 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 894c0c76-7eb3-3cd1-a703-a9ffc016bd37 | -11.804 | -50.9064 | 2026-09-25 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 37848772-21d6-3b0c-9bfc-d567b151a917 | -7.3853 | -64.3849 | 2026-09-25 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5c3b9a9f-5cce-3775-b4f2-95d6e253b141 | -11.9593 | -50.6965 | 2026-09-25 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 8d9c7e16-b8ae-395a-8737-bbb5c96af26e | -9.1535 | -59.4834 | 2026-09-25 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7d75bf9f-bf68-366c-bc12-dbef3856cc6c | -11.959 | -50.7179 | 2026-09-25 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 216.3 |
| eae31504-6aa5-33e1-94ff-989c48b83fdd | -11.978 | -50.7157 | 2026-09-25 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| fce57600-7ad3-36c7-b60c-dc5ad0dc6196 | -5.7754 | -45.1053 | 2026-09-25 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 40d230c4-18fb-345a-aa98-fdf92bcd889f | -7.3854 | -64.3662 | 2026-09-25 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 81bf2416-b7a4-3b7e-9e07-4ca199aeb9c5 | -11.8227 | -50.9256 | 2026-09-25 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b964a90c-84cf-3c93-90ad-d67dbfdcf123 | -14.7344 | -46.2219 | 2026-09-25 01:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9d2c6e16-c0f2-3d13-9108-735dc064249a | -3.2047 | -53.4179 | 2026-09-25 01:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |


[Clique aqui para ver as próximas entradas](README8.md)
