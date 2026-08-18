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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27c41ee7-cf24-38ee-89ad-4cf06cc01d6c | -7.6059 | -60.8264 | 2026-08-18 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 26282eab-fbe2-36ce-9e49-cfdcd859876d | -9.4254 | -60.4545 | 2026-08-18 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1a871ec0-a980-3e73-b7d5-cd528eeb04d5 | -6.8596 | -58.9931 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 7b79c5d6-958f-30a1-a393-37b0a60e2f68 | -14.1824 | -52.9089 | 2026-08-18 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| b6e12803-1ca5-3159-b7f7-d4a9056312cc | -14.1821 | -52.93 | 2026-08-18 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2974dd6f-e43d-30ec-894c-cc9e6a64f9a1 | -14.2759 | -51.9234 | 2026-08-18 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c8ca5529-5f1b-375b-8507-425288e3b73f | -9.4256 | -60.4353 | 2026-08-18 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| cc175f0e-9dca-3f93-aadd-411760ecc204 | -17.1016 | -46.5808 | 2026-08-18 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ae1a915b-12fc-318c-a7ff-2aa878b38431 | -6.9516 | -59.028 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| af3c1b4a-6f2d-36d8-8d7d-8023995e8ff9 | -7.9149 | -61.7288 | 2026-08-18 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f34ac7c5-b0fe-392d-ac7e-050bbb894163 | -6.7123 | -58.9412 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0bf2f6d5-7e33-317b-82e5-fe00ead3375c | -6.8594 | -59.0125 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 2a4391a3-9d3c-3633-9774-a743bcc9a420 | -17.4667 | -47.864 | 2026-08-18 00:00:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 1dbed604-bd5b-3580-a791-374b064bb2a4 | -8.5549 | -55.3015 | 2026-08-18 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 28330519-2547-3732-954d-1a65f0ff678d | -14.1628 | -52.9323 | 2026-08-18 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 9fe0107f-60ce-3c52-b4ee-6d99577c1206 | -7.6051 | -60.9601 | 2026-08-18 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 40bffa14-e497-37d6-9239-4fa0746ee809 | -9.4257 | -60.416 | 2026-08-18 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 82fdffd0-c885-3e15-ba94-ff5b7f2350da | -14.1635 | -52.8902 | 2026-08-18 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0d2ac3c0-f939-300c-8875-1f75484c826c | -6.8593 | -59.0318 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 2ba1ab92-a7e6-3c7d-9cc3-c112d5ada142 | -8.604 | -50.3527 | 2026-08-18 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| f3c92bd6-5541-3812-83ec-38732b68135a | -6.8411 | -58.9939 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 5d814ed6-db86-31c7-8cc9-1d1897303cf0 | -8.2222 | -55.0216 | 2026-08-18 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a5c7c6f8-7096-36f5-b2c0-16f4cc8cd780 | -6.8409 | -59.0326 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ae52ef99-8b35-3bf7-8538-7a9014329740 | -6.841 | -59.0132 | 2026-08-18 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 204.3 |
| 50d63a0b-9bdd-3c90-aaf5-692912ffaf8a | -8.2036 | -55.0228 | 2026-08-18 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| cb8e2e4e-f490-39cd-a6e0-28683ab68e0c | -14.2755 | -51.9447 | 2026-08-18 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9f89d461-1597-3514-9d89-eeb77d425d41 | -8.0834 | -61.3603 | 2026-08-18 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 01b662b6-7dc6-39bf-b6d7-d54a60a6f7e4 | -14.1631 | -52.9113 | 2026-08-18 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 61bb8a4f-c041-3fc9-84ba-192b8099dfb0 | -6.4048 | -54.9441 | 2026-08-18 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 32e9abc1-4e21-3dae-89d6-ff34e221e2c9 | -14.1824 | -52.9089 | 2026-08-18 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f640695f-1a29-3cc0-8b0b-2bb7ca294603 | -7.6059 | -60.8264 | 2026-08-18 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 604b577a-8ebb-3c15-b12e-6e3ecb2e3f75 | -6.8596 | -58.9931 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 73c38ae8-147d-368d-a422-d5c2e48f268f | -9.4254 | -60.4545 | 2026-08-18 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a93c07d3-f27e-31c6-bba5-d7a88ca3cea1 | -8.2036 | -55.0228 | 2026-08-18 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 655c5864-6b0b-3ce2-8e8a-d13cb93b6228 | -6.7663 | -59.1708 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 96e4cbd5-28de-3c61-88f9-3b1988280624 | -6.7478 | -59.1716 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 303.1 |
| 6fa6382e-7686-3560-8aa4-f06af2b86480 | -14.1635 | -52.8902 | 2026-08-18 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 1c4ac2f4-6d12-3201-b9ac-750943280b0b | -9.4257 | -60.416 | 2026-08-18 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 088afc0b-844b-31ea-bdeb-1391f7e24efc | -6.748 | -59.1523 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 5f743e6c-668b-3948-a9aa-43cbeca17b06 | -9.226 | -50.1065 | 2026-08-18 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6e2238dc-5554-3e8a-b882-2a2a176ea368 | -6.4233 | -54.9432 | 2026-08-18 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| abf5f064-3a14-3221-9476-89622f1309be | -6.8594 | -59.0125 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.4 |
| aed9979d-d460-3358-95e9-c505f5f7eff0 | -6.4048 | -54.9441 | 2026-08-18 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3c880565-c22b-33b9-81fd-bfbcf30981d2 | -8.2034 | -55.0429 | 2026-08-18 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a9008c10-42a1-3fb8-a0a2-7fbb9201731b | -6.7664 | -59.1515 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 030378db-80e3-3888-9d9f-7c50db963b84 | -17.1016 | -46.5808 | 2026-08-18 00:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9d175c4b-cef2-3a0b-b501-d2a250d7d891 | -14.1821 | -52.93 | 2026-08-18 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| f7ae24d0-5669-3e74-a6ed-9d70084f8cc0 | -6.9516 | -59.028 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 9512d6b2-6c78-3c1e-a6d9-146098bdcf6f | -7.0199 | -34.9942 | 2026-08-18 00:10:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 42928698-bb8b-3b47-b960-4c7d32462038 | -23.0986 | -50.0526 | 2026-08-18 00:10:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| ee83561c-f721-3b90-8eae-114f274dc01e | -6.7477 | -59.1909 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| fc53cdb1-a2ad-3815-b33d-0cf9ae01855b | -6.841 | -59.0132 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 194.5 |
| 409ea0f9-5768-3e2c-bda7-2ddd870b1e22 | -14.1628 | -52.9323 | 2026-08-18 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| e3141044-1877-31b3-b27d-5d1dcce3f74e | -8.222 | -55.0418 | 2026-08-18 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f92b1ac8-4c66-3d9c-920e-7160d68b7f5f | -6.8593 | -59.0318 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ed300e22-2c55-3044-9bfc-a7b4145c4a58 | -8.2222 | -55.0216 | 2026-08-18 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 18279f6b-088a-317e-97f9-5a2ec98b592c | -8.604 | -50.3527 | 2026-08-18 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6d3a718a-1c2a-35ab-a4c0-114796d7f133 | -6.8409 | -59.0326 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0af1ab56-ab19-3ff4-b995-eaab1a36e55f | -6.8411 | -58.9939 | 2026-08-18 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| b2185eca-ed3b-31db-ac25-f36396bc89ed | -9.4256 | -60.4353 | 2026-08-18 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 006b3495-6cd6-3982-834e-474c9b99c660 | -14.1631 | -52.9113 | 2026-08-18 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 2fb58f5e-b4a5-3a02-a442-73b63c35c230 | -8.58 | -54.79 | 2026-08-18 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f71905-a938-3934-a803-57459999af52 | -8.6 | -54.74 | 2026-08-18 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6bd9445-5ef0-39c3-becf-bb60dea1164b | -8.54 | -54.72 | 2026-08-18 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d8a2874-fe77-3af2-8eba-6339277d3291 | -8.57 | -54.73 | 2026-08-18 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 677f595d-29b1-38c1-9178-c327a0599cb3 | -8.57 | -54.66 | 2026-08-18 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88b62462-fe7f-3c8b-a732-95c2fed8204f | -17.1016 | -46.5808 | 2026-08-18 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 5a1eae1d-b6e0-338e-a7bf-76b4ef636fd6 | -6.7477 | -59.1909 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 4383a042-5c6e-33f5-8f95-fc7be5051e5d | -14.1821 | -52.93 | 2026-08-18 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 499f31b9-3899-35f4-9c51-2d211196dac0 | -9.7601 | -46.7141 | 2026-08-18 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 708c72ea-86d0-3b1f-8609-9c71862605dd | -14.1631 | -52.9113 | 2026-08-18 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 86cb245a-de97-35f2-a662-aee5e9f65ec4 | -14.1824 | -52.9089 | 2026-08-18 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 219c2d98-1e60-3afc-87dd-e4bd06d00c67 | -6.8409 | -59.0326 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2352fc68-bb1a-3599-a988-3b9f1e81beeb | -6.4233 | -54.9432 | 2026-08-18 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 5461ca55-01ff-368e-b16c-d74907322e5a | -6.8411 | -58.9939 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| bee9f482-a0f6-3fa9-9a86-cba0d6929272 | -8.604 | -50.3527 | 2026-08-18 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| e1ce8308-0cc8-317b-91d8-34ec9b410270 | -6.841 | -59.0132 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 30cbd35a-605c-3500-a14c-3e8b8afe9f7c | -6.7478 | -59.1716 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 287.2 |
| f924294f-c43b-30a8-bd00-494966036eb5 | -6.7663 | -59.1708 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c7bf8028-c219-365e-bc13-66934d292cd9 | -6.4048 | -54.9441 | 2026-08-18 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e1cdff8a-3552-319e-acda-ae0adea5ff60 | -6.748 | -59.1523 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 582a7ff2-6b96-345a-8431-b05ccc6c2760 | -6.8594 | -59.0125 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 31eedabe-15a5-3e4b-ab58-b88fc43e7edc | -9.4254 | -60.4545 | 2026-08-18 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| bfb59efa-e2be-3cfb-8b7f-64026584f770 | -8.2034 | -55.0429 | 2026-08-18 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1e8bd05f-ea13-34ca-8a9f-76a5b3e62580 | -9.4257 | -60.416 | 2026-08-18 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0bb6d033-a69b-36c5-a967-5e184c6bb7a4 | -6.9516 | -59.028 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a389d933-f0e9-3a98-821b-2ed9c327c51a | -14.1635 | -52.8902 | 2026-08-18 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c3332f6b-c36d-3d7c-87db-01b15ab5a4ec | -8.2036 | -55.0228 | 2026-08-18 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 7fc8d9b1-ec08-35f8-8eb1-a332edd02a05 | -9.4256 | -60.4353 | 2026-08-18 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| d5a45377-ccb6-3279-b97b-f309fe3cce78 | -8.2222 | -55.0216 | 2026-08-18 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 986dfa31-8cab-3f52-b7fb-a037f480b5cd | -17.101 | -46.604 | 2026-08-18 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 594052fb-7c7e-3305-b176-0e31775a5225 | -8.222 | -55.0418 | 2026-08-18 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f6cd3183-7d6e-380f-a333-46b2af12e4e7 | -6.7664 | -59.1515 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| bfde493e-5477-33fa-89e2-fe3e0d12e7ed | -14.1828 | -52.8878 | 2026-08-18 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| df67ecbf-4d37-3361-91f8-7dc41d4c6c2e | -14.1628 | -52.9323 | 2026-08-18 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| bea4ed8d-fdae-3e12-bc71-118ec1cc1784 | -6.8596 | -58.9931 | 2026-08-18 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e5f98178-643d-3986-88a3-f296aef69aab | -6.748 | -59.1523 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| e03352d5-6dcc-3e02-a8f0-de62de3ca239 | -8.2036 | -55.0228 | 2026-08-18 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| ffbb299e-5240-3a83-b631-65feb833e8a3 | -14.1821 | -52.93 | 2026-08-18 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 88df5477-38c8-351a-bbcc-dfd36ec48e52 | -14.1824 | -52.9089 | 2026-08-18 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |


[Clique aqui para ver as próximas entradas](README2.md)
