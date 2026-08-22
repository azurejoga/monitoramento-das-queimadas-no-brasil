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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c7464ba-6b19-3a09-ab1d-a5f92b8e3ec2 | -9.0348 | -60.4551 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 268.5 |
| 4a1a3e1e-deb1-3bf3-a619-16aad47d55b5 | -8.9041 | -60.5577 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7a7fe035-f791-3456-af41-c9fc96f8710d | -5.9997 | -57.8054 | 2026-08-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d2f04a70-32cc-35e7-909d-2e9a06ba6a81 | -14.4514 | -51.8149 | 2026-08-22 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2a7b824f-ff5c-384f-90aa-08d7baedb5a0 | -9.0534 | -60.4542 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 5ad6d6b0-fd1c-3596-bad3-dca9e42e4ca0 | -9.191 | -59.4425 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| b17cb122-8688-3b3e-bccd-638925a047ef | -8.3904 | -62.6774 | 2026-08-22 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 675d9262-0470-3132-a07a-5dee1250d168 | -14.4288 | -53.1516 | 2026-08-22 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 2eae46db-bdaf-3648-bd00-9f2e6eb8866b | -9.0536 | -60.435 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 18e40574-00fe-3c4e-8d21-375bd909f9c4 | -6.8756 | -59.4171 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4da0094f-526e-3795-b871-ab0bb290f9b8 | -8.4089 | -62.6767 | 2026-08-22 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f3413e90-8dcb-31b3-8bc4-ba7de40967ea | -6.8992 | -55.6977 | 2026-08-22 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 602c3f79-64b0-3344-bf19-e1f249526b3e | -6.97 | -59.0465 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 8f44fe39-7917-334c-b562-5b5eb326c6ad | -14.3361 | -52.9318 | 2026-08-22 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 8d85dc6e-3146-3be2-a2b2-d030d7cbbcb4 | -14.4126 | -52.9643 | 2026-08-22 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| ddc4ccfd-368d-35b9-91ab-bf42b33230be | -9.1724 | -59.4436 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 526f2c5d-6aa9-3304-9e86-2810ef09bb1f | -13.9364 | -53.8798 | 2026-08-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| f540b31f-7fa9-3918-a506-14ad10078517 | -6.6197 | -53.378 | 2026-08-22 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 25ba84c4-b4b1-310c-a370-2f82856de998 | -11.3667 | -46.0177 | 2026-08-22 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b27d1cf6-c21b-36db-9d01-c4ceabc4297c | -8.5221 | -54.8007 | 2026-08-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| ffe084cb-e6d1-36f4-99fc-1a033dc3eb0b | -15.4014 | -52.8352 | 2026-08-22 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a0ca8e1c-5da0-38b6-bb0b-bde35429b049 | -6.8568 | -59.4757 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.0 |
| d7725ac0-408b-3960-9f7d-927c775dd67f | -9.1909 | -59.4619 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 2c90b5a7-e240-3669-aef9-2c611736c20d | -9.1722 | -59.4629 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| bfb53bff-d018-35a7-9979-ff267c6a46e5 | -6.018 | -57.8242 | 2026-08-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b195d0db-3ea4-31ac-898c-00b4a7f91341 | -6.5302 | -58.5227 | 2026-08-22 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e4e38f8b-1eab-3f84-b467-3ac80e436a56 | -6.5441 | -56.2508 | 2026-08-22 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| dd2cbb7f-1e81-3a72-bcda-f5e2dc2b3f3a | -10.9435 | -51.4234 | 2026-08-22 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4b6b09be-20e3-35e3-9903-b1067b898b07 | -11.6059 | -46.551 | 2026-08-22 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 294953f5-db10-319f-bebc-61038aa6b8de | -13.1071 | -43.3496 | 2026-08-22 14:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e01a8d50-dc9e-3d83-9b72-012fb9d17336 | -11.6055 | -46.5736 | 2026-08-22 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| de9d9df9-1437-3d20-a588-873789183dc9 | -9.106 | -60.9127 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1cb1400d-ba23-36dc-8566-2b2a086b916c | -9.12 | -61.6011 | 2026-08-22 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b7fbf972-5da0-3e4b-84c7-189dd5325b85 | -13.997 | -53.6853 | 2026-08-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3d075db3-e27f-3e77-a67b-06e851c6837c | -6.0181 | -57.8047 | 2026-08-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bf724f84-caef-37d1-88ae-aa8d5a2eb9f7 | -13.0881 | -43.329 | 2026-08-22 14:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 160.5 |
| 86d2f747-75d2-3d25-bfc6-7faafe0813ff | -6.5626 | -56.25 | 2026-08-22 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1b8c7f41-e604-3fb3-95c1-6e8d96066ec4 | -8.3481 | -46.5058 | 2026-08-22 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 23f47f44-5239-3c10-91aa-862c32265ecf | -6.9314 | -59.3377 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ff2a873e-ff7a-3943-81cc-03271ea4b69e | -7.0191 | -48.0323 | 2026-08-22 14:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| cf572651-a21f-39fa-945b-3dfe65d5e924 | -6.3863 | -54.9451 | 2026-08-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7a886d16-ca19-3856-aa47-40251a702f3d | -8.5216 | -54.8612 | 2026-08-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 17a554a2-5439-3fbb-9031-e45634a46b5b | -9.1201 | -61.582 | 2026-08-22 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| bedfbf1a-5869-3e38-b321-b55cb251cd54 | -5.9996 | -57.8249 | 2026-08-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 37460afe-6eeb-371b-89ac-3fb813a6ca22 | -10.6749 | -50.3048 | 2026-08-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 1bd05904-f6a9-3d55-957c-0b649d367956 | -6.5439 | -56.2706 | 2026-08-22 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 0715ff73-521b-39f5-a40a-c974323c4358 | -9.4744 | -48.2917 | 2026-08-22 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2bf6bee5-6b2a-3d78-974a-654d54105604 | -14.4285 | -53.1727 | 2026-08-22 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d10a8036-f0e8-33fa-82b1-f1c95652e0ed | -8.4088 | -62.6956 | 2026-08-22 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 2f5f3f45-9fce-3336-809d-cf6c152fe6bb | -8.9936 | -50.7215 | 2026-08-22 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 8c3cd4ea-2f02-3ee2-a878-17f0d4ca39eb | -16.1279 | -43.6194 | 2026-08-22 14:40:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 18b699dd-4b46-3e3d-9d62-b2321bb9a947 | -13.8387 | -53.995 | 2026-08-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| dff0b2c0-22a6-3bfc-9c6e-b4d7f6ed550c | -8.9042 | -60.5385 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| aaf4c0b4-8b27-3d81-9bdd-6bb7d9efa220 | -10.9624 | -51.4214 | 2026-08-22 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 49cb046b-f18d-3467-bfdc-ec3692892450 | -8.5218 | -54.8411 | 2026-08-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| ec9325ea-642a-3e57-8eb2-f3c35caffb73 | -6.8042 | -58.9954 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 648d5de6-178e-35ed-97d7-172de0c8b5ac | -8.5408 | -54.7995 | 2026-08-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| e569a8f7-4b55-33e7-90b6-2041a6874397 | -15.1873 | -48.7671 | 2026-08-22 14:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6f77506f-ee0d-316a-8500-fb1279edf0e8 | -16.1273 | -43.6437 | 2026-08-22 14:40:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 1e63de4a-f83a-3db9-9f12-5ba1d0242970 | -6.8043 | -58.9761 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| c3f7fb04-1869-315c-9f7d-80bc0c9fc39d | -6.5829 | -58.9851 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 9d75ee3b-c071-347e-ad2c-c0862fe83f51 | -6.9315 | -59.3184 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 38e46e70-e824-3735-8543-f9060e4d891c | -6.4391 | -52.7343 | 2026-08-22 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 211b07ee-4af1-3783-b953-6bd13c64c29d | -7.0004 | -48.0338 | 2026-08-22 14:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| daafde93-ccfd-3c9a-974a-f6cf444ed824 | -9.035 | -60.4359 | 2026-08-22 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 730595ee-93a7-3547-9019-267a808cc156 | -6.1285 | -57.8393 | 2026-08-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 187.8 |
| 95d427a9-e746-3e2c-92b8-99786cefee0e | -6.9499 | -59.3177 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| c401cd24-9733-36e2-92f8-985f8aeea13e | -6.6195 | -53.3984 | 2026-08-22 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b9241b0f-e936-3f03-be6e-998163be5509 | -15.3415 | -52.928 | 2026-08-22 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d2fe56c7-2e03-319a-bba9-5b5056ba7b7d | -6.8226 | -58.9947 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1f314c3d-4da7-387a-8c04-9efd49eb5f4f | -8.522 | -54.8209 | 2026-08-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 9d5d67b4-f7cc-35df-abd0-381c590f113d | -6.857 | -59.4371 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| e4a07406-9659-3b8a-aa05-fba252c17596 | -6.8755 | -59.4364 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| fb249e41-73b7-3d16-8e7c-4bc6d98ca809 | -8.3903 | -62.6963 | 2026-08-22 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1a47d6b0-1429-352d-acb8-d2c61c3be575 | -14.4131 | -51.7987 | 2026-08-22 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ef11818f-ebf0-3c6e-aca2-b6207b27b1f2 | -11.625 | -46.5484 | 2026-08-22 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 50f8c86c-d93c-3c87-8d67-f11c516b8f8f | -6.8571 | -59.4179 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| ac5d8e2c-dddd-3447-b240-73770ef97ceb | -6.5487 | -58.522 | 2026-08-22 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f908b514-e756-3189-8242-6a9e792ca77c | -10.8842 | -50.2183 | 2026-08-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| cbd7a0ac-53d9-37b7-bb1d-3861345ff4ae | -10.7847 | -50.5706 | 2026-08-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| de00a685-63b1-3fa5-9567-d2eff6aa1558 | -6.3654 | -58.3354 | 2026-08-22 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 753e0ee5-b81f-3894-b34b-4c68553e5197 | -6.9699 | -59.0658 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7e02c186-6db8-321e-8d66-69bcd48d2ce5 | -6.8569 | -59.4564 | 2026-08-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.7 |


