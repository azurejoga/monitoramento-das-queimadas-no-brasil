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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| deeb16da-214c-321f-8ca2-58717f89ca84 | -16.67142 | -57.11117 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 7be44a1a-8071-384b-b80d-123ca48d1cb7 | -16.67124 | -57.13357 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 26237936-c309-31aa-be2a-cbb126b6a4c8 | -16.67083 | -57.11481 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| beeca78a-348f-310c-a9f3-7b2bc3831a70 | -16.67042 | -57.09607 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1e1d0f21-1ef8-38e0-a346-98eba05a936a | -16.67024 | -57.11844 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8120c263-f6ab-3bf1-967f-afc98543a50d | -16.66983 | -57.09969 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| a85de0ad-37b3-3f4a-8f3c-b7ec52a547e6 | -16.66966 | -57.12207 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b8640a50-e6fc-3f92-ac07-f371675233b8 | -16.66925 | -57.10332 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| 3ba5bdd3-8736-3cc2-a816-665480337e35 | -16.66907 | -57.12571 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c617b16d-af04-314d-9b1f-6ceff2cb1d51 | -16.66866 | -57.10696 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| cfb1c89b-4976-35c2-b729-59e208e0e6ee | -16.66848 | -57.12935 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| cda702bf-1846-313c-890a-343b9c293280 | -16.66808 | -57.1106 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 82fca22f-43aa-3464-a654-0be9c18f7f1e | -16.6679 | -57.13298 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 8f25bff1-72ed-33d9-8cfb-dd2664f7b30b | -16.66767 | -57.09186 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1203013d-e311-3556-b0cb-7b9395c69e30 | -16.66749 | -57.11423 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| a3d9aaa6-457c-33a0-b24a-625e5ae60eaf | -16.66731 | -57.13663 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| d85ef589-6184-3ba3-a822-b7d9c37b7fbe | -16.66708 | -57.09549 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6642b78c-17a4-38bd-a6ee-6a2186c58f7c | -16.66691 | -57.11786 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 767a4431-75d4-3a04-bf03-4c4a95c1375e | -16.6665 | -57.09912 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| 6887adb1-ee89-3a28-899b-5dafab6815a6 | -16.66632 | -57.1215 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| e0c080db-d013-38cc-8b13-3c67ccebe51c | -16.66591 | -57.10275 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| da49c894-5206-39cc-8b29-ef598c03c118 | -16.66573 | -57.12514 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 2f4b51ed-1742-3a0b-b2de-93a4b8b71dd8 | -16.6655 | -57.0918 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2aa967db-8f13-383c-a849-fd2820009d02 | -16.66533 | -57.10638 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 1bc87297-ee28-3da4-a43c-90286cf08afa | -16.66515 | -57.12877 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 9b089d67-eeb7-3214-b1f0-b91cadb88b12 | -16.66492 | -57.09543 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d253fe8d-4a8b-3753-9e0d-35d47d7fd22e | -16.66474 | -57.11002 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 99da6f67-b4b7-3181-968b-a8ad71e7ada4 | -16.66456 | -57.13241 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| a0d76dd3-fd34-3bf3-bd9a-234578e7eb1a | -16.66434 | -57.09907 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 8fb447f3-0645-3c39-80da-c9e2e3fbaa49 | -16.66415 | -57.11365 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 92c66eca-b15f-3e60-bcca-4d1898758809 | -16.66397 | -57.13605 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 15803ab0-d541-3b21-857c-5c50044c6a38 | -16.66376 | -57.1027 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 90696576-6e63-35d1-b97e-a02eab2e9e6b | -16.66357 | -57.11729 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 9c4070cd-64f7-37c8-a4f1-0b9aa5749df9 | -16.66338 | -57.13969 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| ec736583-b9c3-3fa9-9156-3c6ac4b815d9 | -16.66318 | -57.10633 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6d2987d4-72c2-3cfd-a2d6-d968ad31c913 | -16.66298 | -57.12092 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| a2416d2f-acdc-3ce5-8a0d-ce76c0cc9bf8 | -16.66274 | -57.08759 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bf507b98-6c6b-3fbe-b4f6-8da230470035 | -16.6626 | -57.10997 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 29a5c35d-1502-32c7-bcd1-b806c057f738 | -16.66239 | -57.12456 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f6ac48ae-3204-3ac9-80f3-b161f5e7b851 | -16.66216 | -57.09122 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2353ca04-f956-39d9-910b-47252d73b583 | -16.6618 | -57.1282 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 9ea9fd37-e2be-34db-9d53-f1fe256d86b7 | -16.66122 | -57.13183 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 00706f46-745a-3ef3-be91-4bb69dd76ee4 | -16.661 | -57.09849 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| e988bca3-fd68-3ccf-9d7d-e48e3220be71 | -16.66063 | -57.13547 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| fa3815fb-eb42-3345-967d-85285cd19546 | -16.66027 | -57.12452 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 32b48a4d-af1c-370f-a844-d9479fea871e | -16.66004 | -57.13911 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 1d914304-4817-37dc-9c42-b0835f156751 | -16.65969 | -57.12815 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| 6076352c-b734-31e3-aa01-e1790d3279ed | -16.65911 | -57.13179 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| 3d3d3421-1349-37fd-84c5-0aa3e49bfd95 | -16.65852 | -57.13543 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| bcbf3b78-a534-345b-8b5d-a29fb69c5a56 | -16.65794 | -57.13906 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 02b3762e-3ef9-3ecd-b2f0-e3581bd27609 | -16.65693 | -57.12394 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8d76e4a8-4e0a-3069-a52f-eaebb539362f | -16.65635 | -57.12757 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| ebe075e5-9a97-3979-9a5c-7df69e0a88c2 | -16.65576 | -57.13121 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| 1d5f98da-9314-3215-9dbb-4e7f397c15db | -16.65518 | -57.13485 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| c441101d-fd4c-3b16-9cdc-ed44b3c4af5e | -16.6546 | -57.13848 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 1b1b7c1e-bce8-30a6-b654-3b02509d00d0 | -17.1821 | -56.94834 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c3b4b23e-d052-325a-a57f-688033d79696 | -17.17762 | -56.95502 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9f37e301-3ac5-35b7-aad2-b47453eb44ab | -17.14738 | -56.80098 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| fcef2369-de2f-3a8f-9fc8-e8a580665dea | -17.14623 | -56.80821 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8c9ec2bc-3049-3ee9-b233-23bcd844ee40 | -17.14566 | -56.81183 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8e4950e7-ea0d-3d7d-ac03-71fb961f5951 | -17.14508 | -56.81545 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e481ef6e-7d05-31ff-b8f9-ced575188103 | -17.1449 | -56.80096 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d74f2f59-990c-3174-945a-e6eaf91527f6 | -17.14375 | -56.8082 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1898764f-386b-32cd-a437-d78d9db5f8b8 | -17.14318 | -56.81181 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 366fdebb-f510-3740-9977-90a3842c489c | -17.14272 | -56.79315 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b6a9a528-cd3d-33ad-8104-106e33050909 | -17.14261 | -56.81543 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2f50dd6c-fa50-3406-9574-0b47cf19f0e6 | -17.14214 | -56.79677 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dbf950fa-0db2-391b-8284-2cd81d1e166a | -17.14203 | -56.81905 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 36f12b46-1a3a-3a85-a24a-6dcf65c97a35 | -17.14146 | -56.82267 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| bad1052a-08f1-3aec-befc-4cb339eb06b1 | -17.14089 | -56.82629 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| cd6b504d-8d33-39da-874e-1b8c9df5e621 | -17.13996 | -56.78896 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1ae7687d-71ad-363a-82f6-40038cd776f6 | -17.13939 | -56.79258 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 42295123-45b1-3f5b-9ab6-978f595d06a6 | -17.1387 | -56.81848 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 542d32e0-c2db-3e7b-bf96-622fa1083bc5 | -17.13813 | -56.8221 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1e9a3ba6-e36e-3b6d-b399-a89aa87ba1f3 | -17.13756 | -56.82572 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 779ef557-f60a-3198-a4b5-40c15874cb9e | -17.13698 | -56.82933 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 35c10f68-74fd-3846-a677-aadb7169996f | -17.13641 | -56.83295 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 812318a7-bbe9-3c62-83d2-4cb1acf42a77 | -17.13365 | -56.82877 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 296b03a6-2976-3288-8e9b-24c50f1764e3 | -17.13308 | -56.83238 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| adfdbdc7-6ae0-3252-9e43-c99788db3661 | -17.13251 | -56.836 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ff014c63-9cac-3df4-b8a9-ff9f47aeb22d | -17.13193 | -56.83962 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9a6a31ff-d247-3fce-9080-72d685ca16d7 | -17.13136 | -56.84324 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c65182b2-2f6d-3f37-96a3-ad73adf37d57 | -17.1286 | -56.83905 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8cb08892-6ed6-310f-865a-4906ed160a61 | -17.12803 | -56.84267 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 45d05e9a-fd75-3cea-9b2e-437b61d0582e | -17.1247 | -56.84209 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 6be0ff4f-7972-354d-8d01-cd312390a89c | -17.12413 | -56.84571 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 9b574eba-b6a9-3933-8282-8832c73e2e83 | -17.12137 | -56.84152 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| f4acfb22-b052-3b6f-934d-e5f127e5fa3c | -17.1208 | -56.84514 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 8da1dda0-3483-3035-bec5-235e7ad9d51c | -17.11746 | -56.84457 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| c39821c0-1324-399d-8f76-9af7dc30fe29 | -17.11414 | -56.844 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 76dc510e-0d3e-31af-860e-1bd4447d0e89 | -17.11081 | -56.84343 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ea7e61c6-4fe9-3e0c-a549-fd9079f7121e | -17.11023 | -56.84705 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ff5a93c2-45e0-3948-be47-8f4d1d189ba4 | -17.1069 | -56.84647 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 32c2a183-d75a-3c7d-9dbe-a3426d5b99c3 | -17.10415 | -56.84228 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7603b45b-eed4-3b25-a349-66f743497ca3 | -17.10357 | -56.8459 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 6e0d317a-6f2b-3988-9d0b-c7f23fcbd832 | -17.10139 | -56.83809 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3e418937-6936-3d47-8d4a-6c32b46414f8 | -17.10082 | -56.84171 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 774c69bc-fa51-3640-8e71-3988a89d6148 | -17.10024 | -56.84533 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 1438fa79-f5a8-3465-ab4b-43f032432aa4 | -17.09749 | -56.84113 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7b3a9cbe-9622-320e-869a-c6c2f9cb3ca0 | -17.09416 | -56.84056 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |


[Clique aqui para ver as próximas entradas](README104.md)
