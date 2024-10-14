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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e18d29-beae-3c1f-954b-5e7067a37958 | 0.94912 | -50.20758 | 2024-10-14 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c927c4ad-0dfa-380e-9a12-77c35f9ba827 | -1.42316 | -50.52242 | 2024-10-14 04:42:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c051e3f-52e6-3ebe-ad3a-6ff6c2fb4612 | 3.54116 | -51.51959 | 2024-10-14 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 692f77b4-041a-3b95-a8cb-5ac8e7ace792 | 3.49151 | -51.49713 | 2024-10-14 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edbd16d5-931f-380f-887b-351fd14752e8 | 3.48795 | -51.49769 | 2024-10-14 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9d6443a-0be6-3b2c-9a5d-352f9c0447a0 | 3.36646 | -51.34012 | 2024-10-14 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44c87c5d-e417-3ecd-9685-d3fc3a081c0f | 3.35096 | -51.3102 | 2024-10-14 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a207a3b-46f9-3a47-9f61-78afec7846ed | 3.35035 | -51.30626 | 2024-10-14 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ef3e92f-d03c-3ab3-9df2-0284558f7017 | 2.90786 | -51.4998 | 2024-10-14 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c3702a5-c054-3d0d-8920-3a43df5793a4 | 1.34631 | -51.25913 | 2024-10-14 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 878ffa90-5bff-3f14-ae7a-ad4559895281 | 1.34285 | -51.25967 | 2024-10-14 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33c67e22-4362-368a-871a-b8583d9fda45 | 1.31468 | -51.25191 | 2024-10-14 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9acc6f95-fe5d-3563-8d2d-165aa1af2dac | 1.25004 | -51.20052 | 2024-10-14 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff1bc9de-0692-35ac-9b27-e6faa781149e | 0.97789 | -51.90479 | 2024-10-14 04:42:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0716b389-546b-3fec-8dad-c0756e14e7e2 | 0.9226 | -52.03985 | 2024-10-14 04:42:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b474145e-6a65-35b0-a813-2769041bc25e | 0.50322 | -51.64102 | 2024-10-14 04:42:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df6a639-253a-3e1d-ac0e-8b140cdb1b03 | -0.39665 | -52.01515 | 2024-10-14 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23bd8698-63e5-32e1-bf6d-74119d469347 | -0.39603 | -52.01905 | 2024-10-14 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5316c12a-2c25-3fe3-8955-547b9c1dda10 | -0.11307 | -51.59013 | 2024-10-14 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c542364-26eb-3569-9991-53eebb601b55 | -1.3523 | -52.31321 | 2024-10-14 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57f0f0dd-0a30-3b38-a181-a1bc80648c6a | -4.35757 | -55.13132 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 70274516-130a-3cb8-9721-68da9917a1d5 | -4.35675 | -55.1363 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5945f90e-c5fe-30a7-8c0a-d434f769da7f | -4.35363 | -55.13055 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fb7f8c2-5fed-390d-a1b9-c3f13bc41896 | -4.35281 | -55.13555 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92adb432-215e-394f-9923-5ef854261f7c | -4.34966 | -55.12993 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b182001c-131f-3b60-9f6f-f7d50acff1f1 | -4.3457 | -55.12932 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc84458e-b4d8-3d46-8e4e-429ead815cd0 | -4.32438 | -55.43291 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4db5887f-53e1-3d5a-a7fb-0697076d96fa | -4.29894 | -55.43608 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c48cafc1-d6f3-38da-8fac-77b3b38c0c87 | -4.29548 | -55.4319 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36d0a7b4-3c5f-3437-b3cd-3f30566cfde3 | -4.29144 | -55.43126 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6682ae57-65c7-3244-ae23-a8b3f8082346 | -4.29085 | -55.43478 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7935f79c-8cc1-3849-b6c0-3b7c6037cdea | -4.27536 | -54.97232 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 573cf11c-326b-3627-870c-1a2203fc2f24 | -4.27144 | -54.97165 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 568fec4b-bb1b-304f-a0f7-63d3e2afc60d | -4.27061 | -54.97664 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca86cb69-f4fa-3180-9bb8-25421ec2126e | -4.26216 | -54.95459 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f80feee-6127-3a33-9224-b1119cfb6e40 | -4.26153 | -54.93414 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa37bc16-4b7f-3d34-bb48-720b25777604 | -4.25908 | -54.9489 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 313c719d-bfa6-3dad-8649-a47f686ada8a | -4.25826 | -54.95387 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c507b67f-1492-3466-a0f7-a8c2c52098c8 | -4.14195 | -53.94574 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 304e6695-2fea-3c40-9a41-221152b9655f | -3.82915 | -54.23252 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12343950-c727-3fb1-b77b-821f53e88ed1 | -3.8285 | -54.23487 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d84ea15-9489-3a58-820b-2af6a329c45f | -3.81264 | -54.11759 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ce327a-c44a-3c2a-85be-157664187046 | -3.75461 | -54.33375 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d04c7cd-b17b-376c-8b64-d88c32690a33 | -3.69492 | -54.5801 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ccda60a-36fb-3261-8c8f-e1267bd83f64 | -3.69104 | -54.57953 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227247ca-6509-3c46-98fa-ff2a7389e934 | -7.91162 | -54.87899 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0b9dde6-bf70-3fbb-bb5d-37051f13d3aa | -7.87953 | -54.7286 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e58ef6b1-2e7a-3a8d-816e-72d96f3bcad9 | -7.87575 | -54.70599 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3d5e398-ac25-3390-bd65-cb18ed81ef49 | -7.87357 | -54.71899 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec5591e6-8824-3b4d-b7bf-7db3921624c8 | -7.87278 | -54.70112 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b885817c-2109-3c6f-8a7f-e19ea8178028 | -7.87062 | -54.71399 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b43055-b889-30c4-881b-206b0d5f7b95 | -7.87055 | -54.69189 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27d66293-5c77-31f3-86eb-fe48efb2966a | -7.86988 | -54.7184 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebc205c4-5deb-3916-a9c1-bab645c3b08d | -7.86982 | -54.69621 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01a9a184-03d4-33cf-80c8-5c9cba4080a4 | -7.86767 | -54.70905 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7d59c30-88f1-3ce5-b34a-93b78c67f570 | -7.86694 | -54.71341 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef470eea-dfd4-3da9-a2ae-b4cb32fb717a | -7.86687 | -54.69128 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0730c468-a68d-3ec0-92a0-10f4064d6bb1 | -7.86399 | -54.69258 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d62a2fed-6e58-3451-9025-631fad285e80 | -7.86329 | -54.69687 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2d86a1d-df32-3cf6-b2d8-8d9b576a1c48 | -7.86319 | -54.69067 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f24ae5e4-5a0f-3eb2-83dc-e3b1c4c4912f | -7.86247 | -54.69498 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4855bc29-3a10-35a7-9a1d-506922a6fff5 | -7.8603 | -54.69197 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc96ec12-f0ff-3540-a382-88e20917b0af | -7.8596 | -54.69629 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fc139b8-6686-32fa-93fe-75abb482154e | -7.85879 | -54.69438 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef3d57f1-7ade-3cbd-9459-a29f2c4188fe | -7.85807 | -54.69864 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244282d1-2f1a-3f6f-8efe-4e61816123ab | -7.85592 | -54.6957 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 127623a8-413f-330a-bcc6-b470564b4877 | -7.81194 | -54.71014 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c28e8caa-adcd-3b7d-8027-d6a2eb9b8d0c | -8.17014 | -55.18473 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 205724f9-6f8f-31dc-ad7d-4228142719d1 | -1.7298 | -56.09875 | 2024-10-14 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f758b42-5a46-38c8-8379-d32c49355758 | -1.72062 | -55.22269 | 2024-10-14 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c191ac88-41dc-3794-9738-e27ab51e6a08 | -1.71888 | -55.22212 | 2024-10-14 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc85f557-a7e5-37d3-8bb8-a39a4502ec53 | -1.71807 | -55.14604 | 2024-10-14 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b4f5eb9-bebc-3cb4-a131-da609d28cf99 | -1.67739 | -55.18881 | 2024-10-14 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d29e035-d2a9-3703-9d21-6f9c9a64b2d1 | -1.65093 | -55.09011 | 2024-10-14 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfb11f4a-f7e9-38d6-bfa1-56160383bc3b | -1.65033 | -55.09375 | 2024-10-14 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 49929871-9707-3640-a9cc-70dc5fe4e34b | -1.34522 | -56.035 | 2024-10-14 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25716c12-c08a-3537-a939-920a5f08df58 | -1.34454 | -56.0393 | 2024-10-14 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4a538e0-e6c0-3331-8609-3104553424c5 | -1.23136 | -55.90566 | 2024-10-14 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd28000c-d34f-369c-87c4-67017e89e1f1 | -4.26078 | -55.76806 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e992f62-8e43-3258-828c-dd4933d9bc93 | -4.26016 | -55.7718 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e42862b-dfc5-328f-bda2-6ce08e82006d | -5.00757 | -56.21353 | 2024-10-14 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9edb416b-d6e3-355b-91f9-4813e24d28e3 | -5.00747 | -56.21438 | 2024-10-14 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5bb34a7-a4c9-31f5-a6e5-19eb7ea84d6f | -5.00691 | -56.21744 | 2024-10-14 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90398683-feff-3a64-a779-334cc82e23c3 | -3.99337 | -55.73264 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bf0114b-ef28-3f9c-adc4-721c9a3af7ae | -3.99279 | -55.73623 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 493e43ad-82f9-3587-a6a2-a1d21baaf776 | -3.98923 | -55.73194 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbdf6948-9d5a-37e8-a030-7efb8bda8f91 | -3.98866 | -55.73551 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf8f8b65-e152-3633-a47e-68c768e3fb8b | -3.98806 | -55.73917 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fd15956-b29c-34c9-9b83-c05e1b6762da | -3.98509 | -55.73129 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f634232-c08b-3fa5-896f-682512ee9519 | -3.9845 | -55.73489 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c35bc48-a65c-396f-83a5-6d66d25f702c | -3.98391 | -55.73857 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f39616bf-5f81-3a3d-acc2-afc1023904f7 | -3.97975 | -55.73798 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5891d9a0-c081-347b-8825-f94576a81e04 | -3.96814 | -55.65297 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d262a26-d9a3-33fa-bcc5-632c85c15def | -3.96402 | -55.65224 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5693843-588d-341b-bffe-71598fc12df1 | -3.96343 | -55.65587 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e377b59d-ca64-363d-9a48-45b22f239981 | -3.92852 | -56.02703 | 2024-10-14 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 328614d1-81d1-3c69-aa95-18f15c7bd7de | -3.92788 | -56.03096 | 2024-10-14 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3af88dbb-d9f7-3d8f-b26f-59433c38e8b3 | -3.92723 | -56.03495 | 2024-10-14 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 535d4e3a-7811-3ab0-833a-e9ac7530f2dc | -3.92365 | -56.03027 | 2024-10-14 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a1e6f73-6bcb-3af7-9d73-4b9b44ff4152 | -3.923 | -56.03423 | 2024-10-14 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README70.md)
