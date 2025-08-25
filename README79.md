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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8edcd82-0170-3749-9fee-90ceb2737eec | -7.62546 | -62.72015 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fef6a6ca-aafe-3988-b67d-fb131a1d1a59 | -9.17096 | -60.83094 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ebf8dce-f857-3a90-b226-2f35f5e8e27a | -9.01556 | -65.70797 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67513465-be05-333a-9247-b750ca3cbb0c | -9.31568 | -63.4385 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfdaef3d-e124-3748-b371-c55c9f6447a9 | -9.13734 | -60.77157 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e77c8fc-b60d-3fe7-b1fc-bec31eb4e4e4 | -9.15818 | -59.46633 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bbcc620-cfa7-39f9-b149-8421c02012e6 | -9.47414 | -57.83041 | 2025-08-25 05:55:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7a379619-a046-3c2a-9d42-7fb166abe7fc | -9.18868 | -59.62201 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16244634-27db-3a67-997a-8af20c1e0c06 | -7.5724 | -63.43435 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f5d76b8-b281-35b6-aede-220a10ac2308 | -10.42333 | -64.43992 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 62d94ed4-e8a2-3406-880c-690e68eb79d1 | -8.5822 | -62.62617 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 516c7c92-f5b3-3b86-a4a0-5cbd270f4cf5 | -9.82009 | -64.26604 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e647cfaa-7fae-395f-acc6-93d180c09166 | -8.22814 | -61.38203 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 789a5320-90fd-3573-88b9-b54c0ecc684f | -9.24413 | -60.47727 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbf91001-63ae-359e-89e1-4fa155e3db58 | -9.72198 | -65.71194 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80f36e29-210d-36b2-8eb5-0144087f8584 | -9.25545 | -60.92558 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 009203e2-33c8-3b94-b050-03e3a4a9ee92 | -7.62802 | -62.73336 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d461e80-bb0b-3a07-a507-2bf12325195a | -6.7965 | -58.62944 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2b1d22b-f65d-3b51-9a10-6f29d540db81 | -8.21422 | -61.4123 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecf8027d-dab6-35aa-afa6-1504ba008b4d | -7.90823 | -63.07131 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e643c6fc-c0d9-3e7a-802a-e9ea934a7c34 | -9.01581 | -65.38991 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 557355cc-f48d-3499-96f6-975af2defe99 | -9.21601 | -59.7137 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee601df4-1c1c-3133-8f90-a5ebaae2448a | -8.13596 | -62.86331 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e3a7ed3-3a5c-382c-b2b2-0044f509590f | -9.06507 | -65.72878 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 93e9c889-479f-3bcb-86c2-9474507f716d | -8.88034 | -62.45879 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 698ea48c-40cf-34b3-8961-8a4cfbab86b0 | -8.88688 | -62.45687 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c6fe6502-6173-38b9-a6cc-be9280bd64a2 | -9.20072 | -60.91639 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28b1bece-0232-39dd-b1d5-9087df7ec000 | -8.12928 | -62.87936 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 31f51d21-efbc-326b-9e13-33449848ab1c | -10.25267 | -59.10945 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0256417-2b85-3a0a-ba37-cca009097ef0 | -9.16829 | -60.81204 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8912eb67-8044-32e8-b448-59b0d5157020 | -8.24614 | -61.46507 | 2025-08-25 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fb44a64-e79c-36f8-8d76-0714f7b2109f | -8.90291 | -62.46205 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee25018d-1870-3d36-ad21-d9cad8e248ac | -9.02221 | -65.38881 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00b5319f-712b-3504-bbc4-c2bad6cabd23 | -6.84133 | -58.95884 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa7539bf-e00a-3492-9ab0-5d5c6ee6048f | -12.05979 | -63.14785 | 2025-08-25 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a69b624-a553-3a82-9e82-343c9ae4245d | -9.15458 | -59.45052 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4fbd050-e334-3ad4-93c0-8d5a49874126 | -9.0059 | -65.39565 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c42c5c1f-1c0b-3217-b14e-a035228cb97b | -9.20404 | -59.50086 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0541835e-b64e-3514-9b47-7b70d24fa7f1 | -8.23272 | -61.42035 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 320bbe15-7e25-37dc-baf9-5aac21578e0d | -9.26889 | -59.78655 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da82e4e2-eaf7-3a76-8878-8754f2202d69 | -7.10507 | -59.78045 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 044b4d35-16ab-33ab-90a6-45e50f4707f7 | -9.01914 | -65.38372 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2922ecea-c944-3a7a-8887-71f2b5cd1a92 | -9.20426 | -60.92411 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a3397e9-627d-3ff7-b152-043b496d5618 | -9.0547 | -65.72274 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3f04a1c-fa10-33a8-a072-414a992d9e1a | -9.26386 | -59.77271 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9ed2bfe-85cb-3416-8841-7ca8732aec72 | -7.66035 | -63.52778 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60676b7b-5a54-3a5e-8037-8cdece737000 | -7.27623 | -57.66699 | 2025-08-25 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12eae0f2-1760-3a9f-bd39-2375b3700fc2 | -9.16989 | -59.59134 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6a18f73-b4cd-3ca1-8f1a-5792c4e91944 | -7.6609 | -63.52407 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8aa9673-ce49-3b64-87cb-b4cd6559f6d0 | -7.90453 | -63.0667 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6a856427-3648-3785-833c-3b71b5093e27 | -9.50051 | -64.75963 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 410e7844-7e49-362a-ab71-25e66a9bfb71 | -7.99671 | -63.45826 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cd6d698-1b02-3971-a53b-1ff1531c9c9a | -8.88933 | -62.4385 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| debedd61-f53b-33dd-a1d7-9fccde57b730 | -9.19498 | -59.44499 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94085a74-2e5f-3adb-9cd9-8b8804b6f3c2 | -8.89195 | -62.44178 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ebc61a3-528f-315a-8462-b8163992c4f8 | -8.62665 | -62.63262 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfcdb17e-c49d-3b2b-a16e-0f1b94839773 | -8.65235 | -63.42997 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ecd5e48-7895-3e36-83e3-1f3f3488f30f | -9.00359 | -63.63271 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e2f0a46-6ba9-3efc-8bf2-780e7969a53a | -9.19561 | -59.48282 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68fcbf28-3fdb-3f25-8680-c67ae4a1a374 | -8.89065 | -62.45095 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f194239d-2ad9-360a-ad15-c0d35a5fde35 | -9.20708 | -60.79296 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b6cae9e-11ff-31ce-8117-a74b2faa99e9 | -9.20894 | -60.92768 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b71e1e0-0527-3f93-bcb5-7825aa5abe34 | -8.11801 | -62.86494 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5aed52a6-cbad-3932-ad6c-56599c5ce80c | -8.88482 | -62.39385 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 702af2ac-b406-3786-ba35-536405049665 | -8.88821 | -64.18723 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47fd8864-88fb-31b3-841a-68c1fc41b665 | -8.87323 | -62.44376 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fb50581-465b-349b-b439-e760c0c891a7 | -9.19951 | -60.92531 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c284b581-1092-3f36-81d8-578b3aaff130 | -8.91831 | -62.42878 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0ddbe35-dcc8-35f5-8522-216bbbd9ba0f | -7.65732 | -63.51973 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a380bd71-7c7c-377c-9850-41150323a289 | -9.88099 | -64.27864 | 2025-08-25 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0f0d615a-f7f2-3e60-b508-71e3ea36cf3f | -9.18742 | -60.82379 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a517ccb0-0592-33ed-b2f3-c288ff0b39f7 | -8.2167 | -69.86174 | 2025-08-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca15d35b-d3e0-31c8-a32a-297b1cf4ee9c | -7.56237 | -63.85832 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71da8cba-67cf-3a63-8777-ef9782add393 | -6.34076 | -58.18701 | 2025-08-25 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 092aed69-e6d4-3ee6-89e6-4729dc6f4499 | -8.58899 | -68.15266 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eb04396-21bc-3115-bb8d-af33e5e992aa | -9.22147 | -59.71455 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 741e06ec-09f2-3a7e-8caa-b79a1025c14b | -8.90228 | -62.44508 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53b880bb-9a23-351a-9474-93345bec3172 | -9.21 | -60.92373 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2466a1bf-e8a3-3b71-98c5-d21289e70441 | -9.02722 | -65.70525 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62690d67-3398-3c65-86d1-7d3ee713072c | -9.2508 | -60.9218 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f6268f8-b924-3ef5-ab39-cf0d5bf7f941 | -9.51792 | -60.55741 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aefce1d-5d3f-3583-ac2e-7ed770eadad2 | -9.80845 | -64.26065 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24569857-8a2e-30ec-b602-6e7ed99b15e2 | -9.81604 | -64.26544 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90308b9b-4e68-3f18-b85b-558b826276e9 | -9.01405 | -65.39224 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dac7630b-b7f6-3e96-804a-f23d51edb8bd | -12.0643 | -63.14847 | 2025-08-25 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb9a6742-1ef9-3a67-973c-9deff2304b5c | -8.92674 | -62.43469 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69488c4e-e477-3c2c-9f3d-9ec6b0111069 | -8.65576 | -63.43208 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85c67410-c2cf-305d-9c60-bb37448343cf | -9.18971 | -59.48005 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4358f56-ffb8-39f4-aead-a231223c3293 | -8.89299 | -62.41092 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f43125dc-d1ef-3dac-99cb-acdc4877e822 | -9.01517 | -65.39445 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 983f892c-abce-3558-ac16-b58948106a58 | -6.83122 | -58.94962 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d02d0308-8dd5-39ec-818f-b686307f420e | -9.0154 | -65.38316 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7118de5a-4956-3d17-8b39-7c8c9e7d83e1 | -9.19848 | -59.50013 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e439752-ec6c-389d-92b8-f9243f9cd603 | -9.16325 | -59.47083 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eed3a211-1399-3cef-910e-69aec31ef63f | -7.10455 | -59.77789 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 55ee4ae5-ce27-3082-a7f2-3cbff7466853 | -7.65677 | -63.52345 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e10e90e4-354b-3d67-aaa5-29bdbcd81b95 | -10.10562 | -57.7666 | 2025-08-25 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 351d15db-12b9-3fe5-90c3-c61b08b2f406 | -9.07435 | -65.71687 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 191d3f0d-2b01-3a5e-994b-10f598b8af6e | -7.62922 | -62.72498 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8eced809-3dca-31df-95c7-628f3b31f810 | -7.71546 | -66.9197 | 2025-08-25 05:55:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README80.md)
