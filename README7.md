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
| 4c212cd8-9405-3ca6-a207-9a6234720a34 | -8.5925 | -62.594398 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69d90d6e-872a-3935-9b98-649ba45fe259 | -9.319 | -63.430401 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a42c88d1-c97b-3c97-aa61-e937c37254f8 | -9.1664 | -59.584999 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbd5737e-8911-39ab-b226-2d0d959f48a8 | -9.1941 | -59.434601 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97d38f4e-b4c0-30fc-be9f-f8a91688efee | -10.5366 | -57.960201 | 2025-08-25 01:03:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8cca5a-f7d0-362d-a9c4-65ccd4434d6d | -8.6825 | -62.864601 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa46bc1a-1ebf-3ca5-8693-6cdee78eb17a | -12.8585 | -60.1525 | 2025-08-25 01:03:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7aaccb0a-259f-3024-813e-724c72030ceb | -8.2418 | -61.427898 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55efc72b-4aba-38e2-bf85-85947b695c90 | -6.2705 | -59.994499 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9572cfa8-4e42-386e-bbcf-90c014308fbf | -9.1969 | -60.909599 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 454302a2-28dc-3981-8908-9ea326e785c8 | -8.6007 | -62.584999 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 02b37d0a-7af2-3a32-9411-cca3129ca198 | -9.1974 | -59.494701 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e43b0494-4144-312a-b183-08a951773112 | -9.1631 | -59.479698 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dfc3f47-0104-3756-bde7-a9608cd6a2fc | -9.168 | -59.455898 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd5a2fa1-ce79-397c-b5d4-1ec83979a43e | -9.0988 | -65.7117 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1f532f8-d01e-3fea-bc6d-c8dedc683397 | -9.1986 | -60.778599 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 018d9baa-1859-30ec-8581-25cb63d8bd24 | -10.4145 | -64.3834 | 2025-08-25 01:03:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbe842c-7c91-3607-b4ec-29e132feecfa | -9.2016 | -60.7924 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 624fdd2d-ed44-3ba1-9681-29bbdd3343c3 | -6.2542 | -60.013401 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc2225b6-7b30-3192-8781-85602c53d28e | -13.149 | -53.7304 | 2025-08-25 01:03:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7eb1351-2b6a-30d9-9e58-81fc07b56d8e | -9.1565 | -59.450802 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7296f2e3-523c-3a26-9d39-45edf616b7c2 | -7.5495 | -63.838902 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45611bc6-633e-369f-b9ba-9b24fa654d0b | -8.8842 | -62.4245 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8055277b-29d3-3ea1-9999-dd4252197696 | -6.3586 | -57.954399 | 2025-08-25 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09a9f185-0bc3-3a57-b5c4-6983ab40eb93 | -9.1454 | -60.725201 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc8ac10-0139-3499-ae92-43101f1dc5b2 | -12.86 | -60.1595 | 2025-08-25 01:03:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ef76b888-f891-3737-8fe3-d87c7b80b65f | -8.8807 | -62.455502 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18c5cc6c-04e2-304d-a2a1-ee822e333920 | -8.9249 | -62.4231 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 38521118-1953-369a-ba3a-c38f27ee40fc | -8.2305 | -61.423199 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5460445-90b6-3f16-aa7a-ed53c5c45cec | -8.9807 | -65.394897 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5076ffb8-3fc6-3d6e-9d19-ea489bcb8310 | -7.9208 | -63.0467 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae2f662a-c400-3fca-81d4-294c5969857d | -9.2575 | -59.7593 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7261e6ab-052b-3e84-b5bc-6c42b35a7b2a | -6.83 | -59.419399 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b351d84d-f3e2-3d51-9d3c-c59cc29c8c28 | -8.9948 | -63.640301 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a754b8f2-2da6-3670-8ef6-172cbba2a40a | -7.6221 | -62.7173 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b46ea09-d021-3743-859a-96e17f970274 | -9.472 | -57.818401 | 2025-08-25 01:03:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc76502-a073-37b1-a91c-748e58570ef7 | -9.1974 | -59.6306 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86c1a33e-7183-350b-acec-df101320e895 | -9.1974 | -59.4491 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c7bafa7-a8e4-384d-98a2-9a7cce60640d | -9.1258 | -60.729599 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1f51d78-2c69-3253-9be0-2ba9bdbbc136 | -6.8365 | -58.952999 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce15210-c791-3774-994b-cd479fdd583e | -8.124 | -62.849098 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5078f8d-285b-3982-9b0c-46d710bb5ae1 | -8.1076 | -62.867901 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0f7417-5efc-39de-bd29-7aed96f89341 | -7.3552 | -57.629902 | 2025-08-25 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ae281d-090a-399d-a095-e41f8300dc78 | -15.6343 | -52.7075 | 2025-08-25 01:03:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10f5f31f-4f9a-311f-9406-dd826664fe92 | -9.8075 | -61.201199 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7d57a0-c905-3764-9d2c-d658921a8bab | -7.6319 | -62.715199 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6387aeb6-967f-3794-babe-b7cb558fed15 | -7.842 | -49.974201 | 2025-08-25 01:03:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08190eb3-d150-3dd6-9796-8177765a8f58 | -8.2212 | -61.381802 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbf52575-1fb1-302a-b353-b2eb170166af | -6.2558 | -60.020599 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9391ec9-9866-3ea8-9437-c7a9f7f3b9c3 | -6.2721 | -60.001701 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f720677-ef3d-3283-8e19-65921e000428 | -8.9885 | -65.383102 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84a98d58-34c2-3fb1-af57-39495956a733 | -9.9678 | -60.166698 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9be2e415-598f-3fc6-aee3-f74fd10242a9 | -8.894 | -62.422401 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 898afa85-1057-320d-ba25-929d68597b4c | -8.6412 | -62.629002 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eea76b0d-ba9a-3baa-a069-22a764074541 | -9.0101 | -65.388603 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab1cb729-49d3-3cba-894e-e45481bf0087 | -8.9069 | -62.434601 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a453f38c-9ffc-3e65-82f1-fb6dc9caa01d | -9.0358 | -65.703796 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 635c8944-27bf-3d8e-a031-9b2fcbfb0e7d | -10.2631 | -59.104 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88ae4da9-fe47-39d6-bedf-7541735068ff | -14.7168 | -55.926899 | 2025-08-25 01:03:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f88cf311-a8b2-3811-81b2-ff781de5d3e5 | -8.5858 | -62.610901 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae62ed9-da1c-3fc9-be92-60f5657b7a6a | -8.9521 | -62.125702 | 2025-08-25 01:03:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8cab402-6d42-392b-b2c5-e42f43f6c734 | -15.6308 | -52.694 | 2025-08-25 01:03:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82636c93-3dfb-3ae8-a879-e1a36ba27ee7 | -8.1044 | -62.853401 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7efeb243-533c-3c41-a55d-1683fbfc4aca | -9.2197 | -60.9189 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ddd7b33-722c-310d-97c2-c0a6869b40e0 | -8.6809 | -62.857201 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d80a7dfb-b6e4-3c9f-a063-c1c17d1540f6 | -7.4416 | -60.0233 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0e7a261-10b0-3c62-a923-56ee58aec05a | -9.2023 | -59.606899 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05b99fdc-db8d-361c-91e5-25eb35dfe0fa | -9.1925 | -59.6091 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8da339b9-cdd5-342c-b3da-cce60f204c03 | -9.2154 | -59.6189 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee30e6eb-a050-31c4-b85c-514c67fe7bba | -8.2259 | -61.4025 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82c946b8-3765-3d31-9520-da1bbe29e29e | -9.2039 | -59.4324 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7da9b4-8ca4-38a3-8fe0-3665a9d50b72 | -9.2234 | -59.699799 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31decb08-afdc-3876-8477-2ee924ceb7fd | -9.1729 | -59.613602 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60c4d072-9df4-3ab9-a22f-3199f7639073 | -8.0791 | -61.529301 | 2025-08-25 01:03:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdcfcbd1-a4a1-3388-92b1-9a810a2373ff | -9.1582 | -59.5037 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9ce2aee-1314-39a7-b8f2-66de1690420c | -8.6923 | -62.8624 | 2025-08-25 01:03:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd7ac542-41bf-356e-985d-27b0d4daadf6 | -8.5909 | -62.5872 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 34afb721-b898-3ab0-b620-2bfbdd3a7d93 | -4.9615 | -55.810299 | 2025-08-25 01:03:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88ee529a-0532-34f4-be87-1df5143977d3 | -9.0771 | -65.705597 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 406afcf9-a454-3a41-8d92-0c11159eb6d7 | -9.2068 | -60.769402 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 368c8304-65d9-34c7-826a-fc1cd8a24197 | -7.5478 | -63.8311 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18488385-24ea-3440-9255-52c380aea919 | -9.1582 | -59.458099 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 034648dc-7f68-3c8e-8485-18cfa1e6cc79 | -8.2228 | -61.388699 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7205c521-15ab-305e-a03e-e79703697dd5 | -7.5723 | -63.426102 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5e04cc-23a9-31e7-8004-c5b661dbcde1 | -9.5179 | -60.5028 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de5427f3-d35e-3de5-97ef-5a31a07d1407 | -7.4316 | -60.6166 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4743511-eb24-3aea-b3ce-0a44c3f90cf8 | -9.1654 | -62.3475 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 294a0b20-6706-31f5-981a-34adaaa2bd94 | -7.8395 | -50.004501 | 2025-08-25 01:03:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e35dc4e6-c35c-3aa6-a33b-83f75ff35ab7 | -9.2448 | -59.612202 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce4201b-d5ce-38fa-96f3-2a68fee3ad62 | -9.6512 | -59.631802 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccf5411f-dc18-3372-8b19-22b5b6d8561f | -8.2387 | -61.414101 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd959d10-a1da-303b-b1fe-f731241f2ed4 | -9.7066 | -54.978298 | 2025-08-25 01:03:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb9a7db8-2a85-3ded-a301-cbb1797ede2a | -8.1174 | -62.8657 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 782cf71d-a22c-32b3-acbc-429423ae046a | -12.0674 | -63.142502 | 2025-08-25 01:03:00 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83fe80d8-c42c-3803-af5a-714aa7b723dc | -8.1256 | -62.8563 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a87fe43-e86f-35de-9cf2-de123a71cfd1 | -8.5988 | -62.623299 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83486d23-ef12-3643-8e06-2119d536d5bd | -7.0775 | -60.053398 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9976f6e-f32c-31fb-aea9-a56577f59c5b | -7.929 | -63.0373 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9807ed38-340c-3a56-9e6b-2dc4e9b81401 | -7.6303 | -62.708 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 746db5ed-991f-39ae-be5d-fcb768aa8a9d | -8.6298 | -62.624001 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
