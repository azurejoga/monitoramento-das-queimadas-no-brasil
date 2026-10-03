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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 840b632e-072f-3d7a-a77c-bac1c447e78e | -9.0046 | -65.6988 | 2026-10-03 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 211e1e34-e34e-36a8-b824-5ec7102d4d16 | -1.1901 | -49.084 | 2026-10-03 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 72251250-9c47-3dd5-9dd9-bedd7f9f7440 | -9.0045 | -65.7174 | 2026-10-03 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3234d738-dc5e-355e-aeea-285bdd709f71 | -9.4819 | -66.7836 | 2026-10-03 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3c407aad-8696-33d3-b6e6-175b0975d90b | -1.2085 | -49.0838 | 2026-10-03 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 8fbcd9b9-0ae8-32fa-b845-0397d51fa95e | -1.1897 | -49.2966 | 2026-10-03 17:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| ec4392f6-6a60-3492-b89b-f30a44756359 | -9.1147 | -65.9379 | 2026-10-03 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| ce6f9d45-d066-3226-b10e-70ee97cce497 | -1.1533 | -48.978 | 2026-10-03 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c1b0db34-b16a-3de4-bf83-7181c51a6bf9 | -1.2085 | -49.0838 | 2026-10-03 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| d0b77bcd-49a4-3a3f-8e4e-a88f292db845 | -1.1901 | -49.084 | 2026-10-03 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| edb873d8-819b-3ddd-b530-61d8fc133b6d | -9.2745 | -67.6433 | 2026-10-03 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3fb91d05-5f1f-37ce-8e98-4b822ce67226 | -1.4672 | -48.9097 | 2026-10-03 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4d4b7f25-39ee-3ec7-b07b-c0d03bd6f046 | -1.1897 | -49.2966 | 2026-10-03 17:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1a0dfbf8-4e1d-3e9e-b637-98116ab3fd18 | -1.4303 | -48.9316 | 2026-10-03 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| fb7e3144-4989-39a4-9c8d-07c757d523dc | -1.4487 | -48.9313 | 2026-10-03 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 63f52a8b-504c-3438-abe5-161737983a18 | -9.4819 | -66.7836 | 2026-10-03 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 338be84e-b9cb-3908-a92b-7edc5e8becee | -3.08 | -49.5 | 2026-10-03 17:15:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1b0d770-7ab0-3ed7-b10b-eff01760bb06 | -3.46 | -50.12 | 2026-10-03 17:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a5896c-2c80-377b-9fdd-2602dab6fa3d | -2.82 | -54.09 | 2026-10-03 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9903869-1458-38e1-a87c-a1a7dcb4ecc8 | -3.46 | -50.07 | 2026-10-03 17:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 928a23ab-2f10-3d85-b7b9-31e969013471 | -3.08 | -49.56 | 2026-10-03 17:15:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5600d5-0f0e-32e5-bb8a-b551980fc31d | -2.82 | -54.15 | 2026-10-03 17:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06286e60-595b-3640-acc2-5fb334c333fd | -3.49 | -50.07 | 2026-10-03 17:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a010e677-d9b1-3313-8bc7-094f15f39a4b | -2.85 | -54.09 | 2026-10-03 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054e82b7-d23c-3bee-866b-9dbf509dd9f2 | -3.49 | -50.13 | 2026-10-03 17:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4920f68-274d-359a-afb1-4cc01e4bb549 | 1.4268 | -50.7866 | 2026-10-03 17:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e8703fe0-2bac-3e9d-88dd-64057b2d4e6d | -1.4303 | -48.9316 | 2026-10-03 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a75579ae-f706-350d-821b-1a9870c69b40 | -9.4819 | -66.7836 | 2026-10-03 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 8a57972f-2c74-3df0-a107-29580023f7c1 | -1.1897 | -49.2966 | 2026-10-03 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 16b63caa-879b-36f3-b3b0-e47703b013f1 | -9.1147 | -65.9379 | 2026-10-03 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 7f8c7a12-f47d-3c4e-b9f7-36ba97529dd9 | -1.2085 | -49.0838 | 2026-10-03 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 6989835d-a013-3912-9fb6-4fa6e01f178e | 1.9608 | -50.8612 | 2026-10-03 17:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 29d6b45e-6487-375c-a5f6-bfcf2fbc2a7d | -9.0046 | -65.6988 | 2026-10-03 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 428ed098-7dce-39e0-829e-07de39d51d48 | -1.245 | -49.3172 | 2026-10-03 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| ff0ba1ba-80f5-31cb-8e95-fd078c09397f | -9.1076 | -67.7215 | 2026-10-03 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 1787add3-397d-3e2e-ba2e-3fe57aef9455 | -9.0046 | -65.6988 | 2026-10-03 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 90cc49dd-57f9-39ce-b06a-d25ef0b31f8e | 1.9793 | -50.8609 | 2026-10-03 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e6e2f72f-286f-3cd2-b01d-4172b5e913cd | -1.1715 | -49.1268 | 2026-10-03 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 5190078e-499e-3ae9-b51c-708521542778 | -9.0045 | -65.7174 | 2026-10-03 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 87433bdc-c29e-38f9-b402-49a9e8463300 | -1.4303 | -48.9316 | 2026-10-03 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a6ef6821-f076-3405-9ba8-dd87cae07d01 | -1.1897 | -49.2966 | 2026-10-03 17:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f0d79cad-ba06-3a6d-a219-a5bc16543a4e | 1.9977 | -50.8397 | 2026-10-03 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a6fd5395-081c-365b-8473-c41b73b7de51 | -1.0244 | -48.8087 | 2026-10-03 17:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 40033576-3bf3-3197-8d7e-61eeb765ddbe | -9.7126 | -65.0951 | 2026-10-03 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9be0937b-3670-32d6-a1d3-745bce2e6775 | 1.9608 | -50.882 | 2026-10-03 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 04126542-9e82-3ae7-ab5e-af5f559bb0fd | -1.4487 | -48.9313 | 2026-10-03 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 86df5ff4-f1a7-3802-bc20-7691ff0f677f | -9.7319 | -64.9631 | 2026-10-03 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| b29088e1-3548-3721-9659-7fb2f118efa8 | 1.7041 | -60.8399 | 2026-10-03 17:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5171162a-52f5-36bb-b357-dfc90e70e918 | 1.9608 | -50.8612 | 2026-10-03 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1bf1f66e-fe77-3980-89b1-7c25b00f707e | -9.1427 | -68.2572 | 2026-10-03 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 5e7165fe-e4d5-303c-b2f1-b617bc5d2c02 | -9.9174 | -65.0501 | 2026-10-03 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 422.6 |
| d82cb1bb-6f80-3ee2-806b-6d190705856b | -9.1777 | -68.9027 | 2026-10-03 17:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a2d4239d-f86a-3e7d-b5d8-ca64b97216fc | -1.4487 | -48.9313 | 2026-10-03 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a2028e15-927c-3f3b-a35f-cd1a45a1fc47 | -9.5151 | -67.7484 | 2026-10-03 17:40:00 | GOES-19 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eb6cc9db-0248-3fe8-8b09-a3f30d5afa12 | -9.7126 | -65.0951 | 2026-10-03 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| abb0ceb0-f655-36b2-a88e-c599813628e4 | -0.4889 | -49.1327 | 2026-10-03 17:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5d06b562-ecdd-30fc-83b2-19799df6948d | -9.1242 | -68.2576 | 2026-10-03 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 1ac019d9-450d-37b5-8fb2-fbf717e0a01d | -13.5007 | -61.1333 | 2026-10-03 17:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0310e257-ae47-364f-8a1d-8d3a01e7df90 | -9.135 | -65.5453 | 2026-10-03 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 54666bf3-140b-389d-83ec-08bda103a323 | 1.7041 | -60.8399 | 2026-10-03 17:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| bce20d89-84c1-32a5-973d-3b93649c7c01 | -9.1335 | -65.8813 | 2026-10-03 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 3ef74caa-be29-30d7-bb6f-3f4b4ff19e36 | -9.4819 | -66.7836 | 2026-10-03 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4aa5d3ef-96cc-3006-9c2e-7f3d88adef2d | -9.6757 | -65.0401 | 2026-10-03 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |


