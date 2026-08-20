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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bce026b-423f-33b2-88e6-1585ee335289 | -6.89802 | -55.71889 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 21904baf-2aac-34c0-a582-10b3dae43960 | -8.68122 | -54.66176 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 00d756f6-8701-37e0-bece-6d3887007781 | -8.09732 | -51.67524 | 2026-08-20 00:50:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| ca759b8e-9b18-3975-8633-ff94af9976be | -8.28516 | -62.90155 | 2026-08-20 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 2174b642-f939-30af-bfed-6a45eba89db3 | -8.15611 | -54.99514 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0d9a0a5f-f22f-3ab3-88b6-02e9f80d479d | -1.842 | -54.49025 | 2026-08-20 00:50:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| b4541ba6-5e9f-3090-81d7-67dae080007a | -6.13347 | -57.87411 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9c5a87cd-d909-3e4a-b68e-21cd0154f73e | -8.54242 | -54.87488 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 8c103ca5-caa3-3811-b6be-cbb4b39e9203 | -6.58924 | -58.99242 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f6f1e787-e32a-34d0-8d9b-0c87a468ea75 | -9.21589 | -59.77777 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| edfbdcfd-9466-39c7-8f51-29280009a2b0 | -10.91186 | -56.37 | 2026-08-20 00:50:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 3555e1a9-f020-386e-965f-4b52708d4792 | -7.34161 | -55.67375 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4cdddafb-03ab-30dc-9513-23dd6f5e5de6 | -7.60881 | -60.95432 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fa62ef61-a3fa-3742-9307-81294595a227 | -8.67844 | -54.64397 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| dba61b94-c394-3b07-ab0a-2e6b4614065c | -9.21691 | -60.77975 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a5cb4781-5dca-3a19-9f1b-e7e00a7c88e5 | -9.11605 | -61.59805 | 2026-08-20 00:50:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 8e44ccd4-6cb6-3254-a55d-1297e3f67bee | -6.64641 | -56.41822 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bd7e064a-5b44-3a32-8532-b2e577d7485d | -3.10023 | -61.21575 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 537a739e-84e3-3cb0-9967-4766c781a302 | -9.4215 | -60.45193 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| ce0b0f62-1549-389d-95bb-1751d272f460 | -6.57084 | -51.12244 | 2026-08-20 00:50:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 8a71c505-6d66-3b41-9613-7c27eaa3d591 | -9.02038 | -60.49416 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 220ab94d-57f0-3c66-b0d1-681d803e2004 | -1.82809 | -54.49237 | 2026-08-20 00:50:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 125527f3-ca53-36f4-af3d-eaa711acb66c | -10.25141 | -54.37568 | 2026-08-20 00:50:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 561c1a31-842b-361a-875e-efb6b8282b91 | -8.58202 | -54.77419 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 7bcfbbcb-9f85-3186-af7a-e9b2004a9fc0 | -6.69781 | -59.10893 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3853940b-024a-3b10-95d3-548594250dcc | -7.77304 | -61.13551 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4518117f-f016-335e-9610-62ee7b25a13f | -6.95718 | -59.05257 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d0e63acf-8ed7-31b4-a8ac-b6cbddfa97e6 | -3.10144 | -61.22454 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 56e8c5a0-84a4-32ce-b298-b024e4a59881 | -3.13004 | -60.69899 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 29e9416a-ec2f-30c5-a6c9-661e1d967939 | -6.43086 | -52.729 | 2026-08-20 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| f8da06b1-675e-3e89-a111-59c30e2aeb3a | -8.28382 | -62.89133 | 2026-08-20 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02ad7a57-aa29-3bf4-b7aa-ab8c707f7efa | -6.38503 | -54.96205 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d647d39d-4c5e-3752-881f-554999b92709 | -6.80208 | -59.58626 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5c980c75-d118-3d54-92b7-b0d25a5fabfc | -7.80038 | -61.20412 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fec318ee-fdcc-3f72-bdf5-f6f0b63f571c | -10.3224 | -57.57566 | 2026-08-20 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| afd5db42-bba0-34ca-81c7-b106e7b6a484 | -8.53047 | -54.87671 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 8b4ea02f-6ee1-3969-8bc0-fca090f1ec76 | -11.18746 | -54.04168 | 2026-08-20 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 99f14f9c-ce8b-3419-9fa6-e51399d05eaa | -6.59435 | -58.9619 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| aa70adec-5173-3322-80f5-e84de1f74f4b | -6.44561 | -52.72656 | 2026-08-20 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 62736812-b0b8-309a-8794-6d078237c36b | -9.17254 | -57.00812 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c965ef8e-1b23-3ec0-a601-bfd85788921f | -7.05937 | -59.84429 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 288b71d1-42aa-39f5-9bf5-68797d4f17be | -6.69444 | -58.95149 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 6a52cfd3-335e-3c0d-a6de-b892de35a3ea | -7.37749 | -55.5322 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 93028b7c-f6f3-3090-8991-d04129970cc3 | -3.10782 | -61.20572 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f23681b-4f58-37d7-aff2-682cb9b51ebb | -7.5988 | -60.94674 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4a578d31-d32d-302d-87b5-8c691d942b7a | -8.95446 | -60.55503 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4673b80e-6ada-3b53-ae66-428fe8ce0514 | -11.68197 | -54.55622 | 2026-08-20 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 090b951c-9846-316d-98f3-500ca2891ea3 | -6.69308 | -58.94175 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 237abbb0-6548-3eb2-a113-b9d97e24b871 | -11.99923 | -53.43921 | 2026-08-20 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d148bec9-d17d-320e-b430-26fd91b8abf6 | -8.58393 | -54.74368 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 32460d75-5d10-3d9b-8fba-20f603a3403a | -3.0978 | -61.19816 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 06d95bec-75f6-3f62-99e9-128a05ae629d | -9.21713 | -59.78671 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 395d55f3-466c-3224-b35c-27ffa95bdae7 | -5.99785 | -57.86011 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24a58ca9-fbf7-35eb-b42e-97bdb8e7074f | -9.12284 | -51.15675 | 2026-08-20 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 3cb2a7f9-fdce-3940-8f53-1f18e90e7571 | -8.94931 | -60.58286 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 06cc2705-4fc6-3caf-8d34-6504273cf5c8 | -9.20705 | -59.77905 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 85d9c7ba-2cda-3d14-9710-8e00dd50fcc6 | -8.94809 | -60.574 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8afd8e51-9cdf-3b5c-a55a-a142c443c42a | -8.89773 | -60.59922 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb0cfab9-5e0b-3576-bbb0-c8cdd0c81c68 | -8.49869 | -54.87063 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ebed334c-d12d-323f-9dee-b27738cccfba | -6.39466 | -54.94172 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ba8b66a4-1e0d-3b81-8230-9f69885f0073 | -6.24339 | -55.41271 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b7699a16-a7d3-3158-bb2a-4525404c5c41 | -8.6607 | -54.61037 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| fb043691-de13-3e8b-abec-1c457794cfbe | -6.87654 | -56.42732 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 622c6751-ddf7-344a-82b3-29fae47b01df | -11.68561 | -54.56129 | 2026-08-20 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 1b0142b6-93ce-3696-a1df-e379accc24d4 | -6.13511 | -57.88548 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bd2e19d5-907b-3b25-8e25-706009cde193 | -9.20809 | -60.78099 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d09dc04b-6c89-3d66-809c-b6fef1d349ed | -8.09266 | -51.67076 | 2026-08-20 00:50:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a455b688-b208-32c9-8c2d-7a97de5415b4 | -7.79916 | -61.19522 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c4b44589-258f-3a83-a9ff-397cc5c1b4de | -9.42421 | -60.40634 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f3492028-f171-3027-9a00-8106cc564004 | -10.80441 | -50.3124 | 2026-08-20 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 49346db6-d161-3026-bd1c-28819a8835c2 | -7.10431 | -59.76708 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3ad74fb-7fd2-327c-aace-615b1eb90c27 | -4.51445 | -55.45193 | 2026-08-20 00:50:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| eb055ad4-8961-32a6-ad4c-4721ad91e8c0 | -6.97629 | -59.58348 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f7373dc0-33c2-3698-92ca-3f12210f0862 | -7.86511 | -63.75882 | 2026-08-20 00:50:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 64a1b35f-0b37-3c63-bcc5-0af4431cf080 | -7.54688 | -55.59092 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0c7ee102-38f0-3155-88ca-595bbb38426a | -7.79034 | -61.19646 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4dacb46c-5adf-3d81-a362-e248fe1a0f7a | -6.57864 | -58.98407 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 449f5b01-ed00-3847-90a7-c1d9b88c28c4 | -10.45545 | -54.66051 | 2026-08-20 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 625c113a-7b9b-3259-9ad9-54fb9e500723 | -4.38859 | -55.47559 | 2026-08-20 00:50:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7c48b1d9-e386-3cfb-ac92-70806ee7649a | -3.25944 | -61.16326 | 2026-08-20 00:50:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| facfb68d-9331-30d7-99e1-c088e238ddb5 | -9.39937 | -60.5695 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 289e54e2-2231-344f-9d5c-87dec917df72 | -6.71478 | -59.09659 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 1e7e9074-4580-3210-8ba4-af75b0367f61 | -3.09142 | -61.21698 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 25cd3237-6144-35a6-abd5-f6b18f8f3a4f | -1.83315 | -54.47382 | 2026-08-20 00:50:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8a135600-c81d-3e9c-ba8f-ade385730a12 | -7.60001 | -60.95556 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5149cfd-15a1-31ab-9916-53aa2927f4e0 | -6.01149 | -57.87487 | 2026-08-20 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1c49a635-6f60-360f-8035-47793adc7476 | -3.26066 | -61.17205 | 2026-08-20 00:50:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c5a8e910-93ee-3c7a-b048-6be99de7850b | -9.10168 | -60.35036 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 436a8532-e85c-32a9-86fc-6050e0608772 | -6.75729 | -59.46681 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 08390f37-d47b-3fe6-83a1-aae8e29ed1ab | -6.8874 | -56.42564 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 59fa09e3-0b3b-3bc0-b555-80ab194fb11e | -9.15808 | -59.55705 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4cf6bae6-6db1-3556-b29d-ffd0fe928c29 | -9.20829 | -59.78799 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 963121bf-4a1e-327f-9a72-e4adb00e5068 | -7.00694 | -59.60085 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f43e0ddd-ea01-3c86-a07b-9e426e931b91 | -7.44267 | -60.01253 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8e5cbd75-f409-3fb3-8c33-2746c7725d2e | -6.77405 | -59.45494 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5fe5fc1d-63b9-37a9-a61f-47adb67b05d5 | -6.88933 | -55.72588 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3c47fff0-4caa-3ecf-912d-9cd111b498de | -5.80408 | -55.71388 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 39bc8c7a-f966-3e52-a5d6-fd965b125f88 | -9.22591 | -59.77003 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2e5ced84-cf05-39b6-8100-d09605ba3a84 | -6.70367 | -58.95008 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 3c1ab2fd-afaf-3f7a-b89d-6e6286c82c3c | -9.21465 | -59.76883 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |


[Clique aqui para ver as próximas entradas](README12.md)
