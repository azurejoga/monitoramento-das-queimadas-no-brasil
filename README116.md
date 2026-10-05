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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf31840b-2091-3980-955b-a177b2b0f22e | -3.57213 | -55.41977 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d424a63-9e2c-380b-8801-9b1624936665 | -2.88822 | -42.36664 | 2026-10-05 17:15:00 | NPP-375 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58e0458a-58e6-331a-89a5-39bddc336630 | -4.44792 | -54.96973 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c80658ca-1488-3961-b176-40db79372f39 | -3.62333 | -55.28181 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 72b0f397-2516-311f-a102-f6c318cd7a7a | -3.09665 | -53.72031 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| c57c9db7-987a-36b9-b197-7c4c3daea42b | -3.04036 | -54.25367 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2b5eca65-ac34-3054-bef4-3432b23380c2 | -5.52133 | -41.01957 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 05eabe10-c6e6-3a96-92ba-14a152627e09 | -6.49817 | -44.16502 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff8f23bd-dbde-3aff-b1d5-51a99fc5bd6a | -3.5372 | -55.53823 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b417206d-d54f-36e1-9795-4223e47a434f | -9.05339 | -65.43357 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 65a6f406-238f-30f6-9d3b-e25de8effe03 | -8.87664 | -66.64165 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ffa45737-92dc-3ea9-8161-cd48591f9712 | -8.73576 | -47.07037 | 2026-10-05 17:15:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc8ee77b-c298-3972-b2ab-a9ec05966619 | -9.07718 | -66.09599 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a8e43935-8af4-3ae5-ad0d-730b3c9f875e | -5.8177 | -53.84266 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| c5e7561f-ddc0-32a7-8a8f-d94e6e4e4585 | -3.09719 | -53.72379 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| de5cefa0-53a5-3bcb-a83f-7da207f4f08a | -2.99387 | -54.10537 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 751564eb-d467-3871-893e-9e14c3d4a581 | -8.60184 | -66.81619 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1c3b5336-2a49-3e14-a9fb-c069dbeaaa6b | -3.46773 | -54.59584 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 41e8749b-ee96-37af-9e08-fca857ac2055 | -5.18833 | -42.81517 | 2026-10-05 17:15:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 112f0e75-82fa-3d21-bec5-1995f1402eb8 | -8.81954 | -47.17293 | 2026-10-05 17:15:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5de581f8-d593-3a6c-89a8-4a37511dc269 | -3.06939 | -54.15681 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| f39c7403-1920-3479-a067-33f6d690f66c | -3.68222 | -55.94429 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| db7617ef-e7fd-380f-828d-8bd1ec93b340 | -3.14155 | -53.72416 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| bb0ba19c-0584-373e-b95b-7106d7f8b835 | -3.06434 | -54.16817 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 82cfc14a-9a77-3326-9be7-c31f83211b8c | -4.21112 | -53.4658 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 707907b1-363a-3743-8ff1-b7eca6245085 | -3.66912 | -55.95001 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 690247ff-3ae2-31e8-a8f1-7af216f078cc | -4.20672 | -53.45935 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5007fc83-f8f1-3570-8fc8-01a60704fff7 | -3.06155 | -54.17213 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5fa721f2-e8bb-30cd-bc26-f9aeaa3c4d59 | -4.06547 | -47.0671 | 2026-10-05 17:15:00 | NPP-375 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4daeeb72-89f8-3032-b5f4-8e4c010e3578 | -11.02078 | -61.40037 | 2026-10-05 17:15:00 | NPP-375 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b84272c-5538-3e56-a174-af42ef3512a6 | -9.96394 | -65.12431 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| faab0f97-d56e-3684-ad85-ca5a61a6ad34 | -4.72169 | -45.21168 | 2026-10-05 17:15:00 | NPP-375 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f4fa53d5-be86-356e-af25-a85142cc526d | -2.8209 | -50.50364 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ab2c4816-d523-3c9b-9f56-d0d37e88e216 | -6.60985 | -41.57122 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 7f7aa28f-4d1b-391a-a5ec-93b0242aa0bd | -3.06872 | -54.17457 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f7d026e1-b36c-3b09-80a8-a69eecf2673c | -3.1004 | -53.74463 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 665e1311-14bc-3b89-8d64-6e53eefd1b3e | -2.74665 | -49.53082 | 2026-10-05 17:15:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 482ae3f8-5fce-3ff1-bf66-bfc44e343549 | -6.51686 | -55.38763 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a6f0bbc2-7a9f-3b1a-92c6-ea4d39f6b9f9 | -4.8409 | -41.81368 | 2026-10-05 17:15:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 817a2b41-6122-3f00-881a-1f1114d270d1 | -9.29293 | -65.64259 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8d198b40-1316-3b37-8e09-ccbb1bc7ff1a | -8.66027 | -54.54484 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a207137f-f8fd-3028-960d-d7c1b1c300ae | -6.72986 | -44.92488 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 772de44c-c10a-3915-8efb-fcb0493d974b | -3.08094 | -54.16566 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f8421712-25c7-3e9b-898c-5e754dc911c0 | -3.07324 | -54.15976 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d1f7d736-71d4-3db2-9236-a8658b26b55b | -3.27515 | -50.39732 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 84c59487-6519-3899-92f5-6e1d72a14beb | -8.66799 | -54.57343 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 176269a6-8b14-3eb9-9f35-f966d12a752e | -9.29504 | -65.63996 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 159efa92-6268-3bf2-ab8c-54e0fea20250 | -3.46003 | -54.58993 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b57d1700-f00b-3827-b8f7-a3da9d4cb186 | -8.65919 | -54.53757 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 299a3e36-75d7-3590-9717-41ec2eac1d11 | -7.4784 | -42.80359 | 2026-10-05 17:15:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| fb171d81-c8dd-3963-92cc-2ca1d061cb36 | -3.06886 | -54.15337 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9592a7dd-ebfc-3945-ac1b-10f54d4ba492 | -3.47062 | -50.09377 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 287321b3-55f6-3810-a28f-d63aceb1b235 | -9.0833 | -66.08897 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76cff264-7cf3-3b00-b19d-79de62e57585 | -9.04928 | -65.4336 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4ee0534e-1dd5-3d81-b1ea-1b34cbeade9d | -4.11216 | -54.40927 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7290b25e-d641-3ffc-9ae1-df8fd0469a0f | -5.18857 | -42.8183 | 2026-10-05 17:15:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| decc953c-a96a-3df5-820f-51a038df468b | -2.68642 | -49.03703 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 58853836-c3b0-3237-954b-fc7ebdf0f1d5 | -6.45572 | -55.00129 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9a3b4ce7-a804-369e-937f-8e560db4fd6f | -7.2407 | -44.01632 | 2026-10-05 17:15:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 195e896b-b964-3f42-8d47-5d89f22714be | -3.84156 | -50.31664 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4da591c0-3f13-3f9c-8b98-fd3b1fbeb6ab | -3.05114 | -54.21322 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 7a7747ef-9eae-3989-a769-b4368f453763 | -6.90692 | -43.66835 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 926af8bf-26c2-30e1-a9b7-70b20c33fd4f | -8.86434 | -66.78272 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| dcec998f-d34a-35c3-b0d1-1dfc7176834d | -6.87968 | -43.67682 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| e4099eaa-6360-32ed-9960-d391893632d3 | -6.90203 | -43.67321 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0897b95c-8d79-30ef-bf08-42a5d3251db1 | -8.52992 | -54.5798 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 56b6c68e-ee6c-3858-811c-22e82d4c2aea | -7.65413 | -44.3688 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70780080-47d5-3a05-aff2-6c8a21ab89cf | -2.63245 | -49.30883 | 2026-10-05 17:15:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4354020-7a9c-324e-8d17-06f8d9cc7e52 | -6.04662 | -43.68903 | 2026-10-05 17:15:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f40b7867-d6a5-3768-abd0-c99e573169ca | -6.59062 | -41.5743 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 40.9 |
| 69a8fea8-3420-314e-8efc-ed9785266b74 | -4.27763 | -55.13661 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6098e2a6-7fd3-37e0-a17e-391f87576e15 | -5.95662 | -41.35094 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 175.7 |
| a72c7bf0-c573-3b9a-a09a-9a129c1278f8 | -7.22881 | -55.18558 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1e5d85a-158f-3141-bd13-388602b98d63 | -7.23386 | -55.19608 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 623cced7-cef9-3cad-991c-c93648d143d7 | -8.28118 | -45.92017 | 2026-10-05 17:15:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cb257c0e-2957-3b73-a56b-609fcc209329 | -3.95683 | -56.05304 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 36a5c9c8-cfff-3cf7-ab36-21c5c767592d | -6.91396 | -59.26408 | 2026-10-05 17:15:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82bdca03-09e7-3c8f-bd5e-359d337cf111 | -3.2387 | -53.87207 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 592715cf-01f9-36e6-88b9-bc4e346d965b | -3.28709 | -53.83282 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72dd36ea-0066-3c11-8a8c-dfb8766b7802 | -5.57127 | -54.314 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d0c53df0-538e-3b68-9b8d-4bc4a11d04d8 | -5.80665 | -45.24525 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 364cfc54-ba8d-374c-8181-36ad7f8368b4 | -3.68332 | -55.95161 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| fbbaf166-3817-3f60-89ce-fb7cbe97735a | -4.4359 | -43.42901 | 2026-10-05 17:15:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8d717847-14f7-3b71-b2d1-92d7c8d2be0e | -3.04435 | -54.23543 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ec933847-263c-3299-9e32-e17f5139a1c3 | -4.42761 | -55.63709 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| deb07a07-4737-3e91-8aa5-5fbebea1bb0a | -4.11653 | -54.41567 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1fb8d53f-b7cf-3d29-8e15-a8af0facc39a | -6.3533 | -42.53987 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 968bd5d0-1e9c-3c0f-9f9c-6219302101a9 | -3.28825 | -42.25356 | 2026-10-05 17:15:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 66c0469d-2140-3a85-b1bb-44df44a050f7 | -3.61101 | -54.60171 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d0888263-627d-35eb-b5ce-2c8284b19b0a | -8.7732 | -66.5709 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 71f45193-8386-3d3a-9164-9c502a8945e7 | -4.43851 | -43.4291 | 2026-10-05 17:15:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 06e10a47-fde7-3afb-91c7-6c4587090e4c | -4.45729 | -54.89666 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 73d24b28-8e85-3e39-b8c9-5c11ceb770c6 | -9.34044 | -64.714 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ecb8b6e1-7686-3bf6-8ffc-40f29556e3d1 | -4.96336 | -40.56108 | 2026-10-05 17:15:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 508be1e4-951a-3a8b-88b5-70a9c4b29d83 | -6.8958 | -43.67048 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dee465b1-2cab-3111-bb37-449e2963304a | -8.53204 | -50.43939 | 2026-10-05 17:15:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 249fe9d8-6556-3c42-a999-674120b49b0a | -6.25538 | -52.84276 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5c1080c0-73e0-33be-92bd-50e96a3921c1 | -6.41915 | -43.46881 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ae3e873c-99c3-3c72-a47a-5a523a4d60cc | -8.4235 | -54.99047 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 62495c8f-ae8c-39b9-ab03-c4262f19e72c | -6.33499 | -43.74683 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README117.md)
