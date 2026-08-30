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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08c2b059-8f48-3fa8-8e89-0b854420de5e | -12.90267 | -59.87798 | 2026-08-30 00:45:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 259f4e79-f4cf-39b8-8f80-2706ffacae09 | -11.02923 | -57.2399 | 2026-08-30 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 38a86d69-6b39-3938-92ef-b0a3e7c21c9b | -11.30126 | -54.04949 | 2026-08-30 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fded20f0-7587-322e-840b-66c52a799364 | -11.8334 | -51.13027 | 2026-08-30 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7530acf8-fb0d-3ad4-b03a-6c5343004d80 | -11.04508 | -57.21653 | 2026-08-30 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1f46670a-18b7-3d6e-b1d5-df406f351593 | -12.55133 | -55.74191 | 2026-08-30 00:45:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e7914c57-5624-3162-8e7b-7174f05b8cf0 | -14.27533 | -57.04912 | 2026-08-30 00:45:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cabe9603-d5b0-380a-80cb-007fe448d77f | -11.23474 | -54.00939 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b825607c-083a-3ff7-a27a-53cd161dfc39 | -11.83367 | -51.05023 | 2026-08-30 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 3878a150-b603-37b6-93dd-43eb3fcda94d | -11.03716 | -57.22828 | 2026-08-30 00:45:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 16d857cb-7af2-3860-8c1b-ca083d04f3ed | -11.18676 | -55.11086 | 2026-08-30 00:45:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| dd0a6584-f40b-323e-b7cd-d0759653a62d | -13.845 | -54.03419 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 40061ff3-250a-3c37-902d-e3d990201d38 | -14.28304 | -57.03785 | 2026-08-30 00:45:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| df674942-ea4b-3116-84b1-9c56b7906c7f | -13.85931 | -54.1244 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 223.1 |
| a14afa24-b93e-31a0-b548-121deae7e5bf | -10.9952 | -50.54402 | 2026-08-30 00:45:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 191c8b5c-e294-31d8-ad40-764bf5fad847 | -11.83284 | -51.13589 | 2026-08-30 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| c60fb6d8-a07b-35b9-b0d1-644a0569e570 | -11.49698 | -60.46131 | 2026-08-30 00:45:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dee937ff-b3e5-38f4-a1f5-c14f09bc4bb4 | -11.28699 | -54.03498 | 2026-08-30 00:45:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| d26627cc-41ae-3638-b52b-cd6f32adbe65 | -12.90389 | -59.88709 | 2026-08-30 00:45:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2d608c0-c352-3727-9046-03cb2a9b14e5 | -14.51625 | -59.83351 | 2026-08-30 00:45:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e4525dad-fb4f-3c94-9e83-74410a81afd4 | -11.82861 | -51.10278 | 2026-08-30 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b59a9ff4-837b-3ca1-bdbe-bf660cdf4eb2 | -13.87275 | -54.13737 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 20d144a0-0ef8-3c85-ab34-9551cad6d669 | -10.73567 | -54.04294 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1a0bda0b-009a-32a6-b5b2-e81ca272c21f | -11.82824 | -51.10837 | 2026-08-30 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 311e2673-acfc-3c10-a06d-bbbc36754fcb | -11.44143 | -61.48855 | 2026-08-30 00:45:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 35a3e6c4-4473-390c-91a5-68f5bf5e280a | -13.87039 | -54.12243 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b5637cd0-b627-3b37-ad83-d254227c9289 | -10.75628 | -54.05045 | 2026-08-30 00:45:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8474fd78-da2d-3684-bd4d-29a763b15b69 | -13.83709 | -54.12811 | 2026-08-30 00:45:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 44e942f9-2e16-3205-b5b9-816cbdf61d14 | -7.62726 | -61.33948 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4060e8d4-cdda-3389-b5c8-702ac1d69e5b | -10.47938 | -59.60843 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 31c6afe8-4ad0-32de-9837-6ecb177aaeed | -9.16941 | -59.61697 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac91ae1f-1bc6-3046-8136-0a13b182bf2f | -6.84999 | -58.9808 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b2354542-f892-3410-89e2-8241ce87c611 | -7.54929 | -61.31037 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 58545a47-27c9-3a8f-a99c-706231a13981 | -9.93824 | -60.5166 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5eaf3b25-3b34-3466-a74a-eaaf20658da5 | -6.95656 | -55.69395 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d898c51a-c8f1-3f2b-a3ec-b7d7f27ec1aa | -8.95822 | -62.40979 | 2026-08-30 00:48:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 490a0107-bb5e-34c3-8aba-4c3badc3f85b | -10.4894 | -59.61605 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| eabc99e9-6e1a-3a32-909a-028e57cb29b7 | -6.63667 | -53.188 | 2026-08-30 00:48:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 101d1114-0e51-35ff-b8c4-13787f895054 | -9.89636 | -60.27583 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 201b3fa2-0a5c-34c3-aead-472fa1357947 | -6.8823 | -59.40769 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 66d0e247-d102-3fd2-91f9-c9117a519619 | -8.95279 | -62.36861 | 2026-08-30 00:48:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 05ce629f-4a2e-3413-9353-3ea9c4504fe0 | -9.88876 | -60.286 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 3618ff83-3ef2-319b-9c90-9300e16add7f | -9.06961 | -60.4934 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 17ff3c81-4c18-3a72-849c-bb399fc5c74d | -7.57373 | -61.34697 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 41240eef-53d0-3d6f-81a3-0203a0c3146c | -4.22041 | -59.56315 | 2026-08-30 00:48:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 416b6733-5129-3862-9b32-cb66e5044b16 | -7.69472 | -61.15817 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 470cdc2a-ed94-39e2-a3e0-be2ef2e17462 | -5.49423 | -57.1398 | 2026-08-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fde20cf9-080c-3c67-9c11-21a7e6ab7f3f | -5.96258 | -57.68658 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 20f3fb53-cf61-3033-b90d-2c57a5895b3c | -8.63742 | -62.84251 | 2026-08-30 00:48:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e2c0bdec-2359-3a5d-bbd2-6a08dcaa8bcf | -6.87614 | -56.57137 | 2026-08-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| c49acf98-ba81-343b-8042-6da6ec2dac9f | -6.93413 | -55.70417 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 190.7 |
| bda629bf-5e95-3134-8871-3dd7a9d6496d | -7.31562 | -60.60336 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 324e7171-3825-32bc-9ffd-9b112699633d | -9.08929 | -65.48048 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ee832bb3-4906-30af-b112-d770c86c01cc | -3.62915 | -60.55074 | 2026-08-30 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 06b61ecc-db2e-37c9-8520-b664da28d354 | -9.91713 | -60.42797 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cf28911-3a63-3575-bd1d-a588b852a023 | -7.57177 | -55.57205 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cf8b12f0-9a29-3f96-aff8-e2285337ec33 | -4.96327 | -55.84072 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ac5d1f16-a4d6-36fe-a7e5-b89cb05e9f0f | -9.18101 | -59.61809 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d4a053d7-2b1d-3411-900c-89e7f24f03ac | -6.74502 | -55.67008 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1e00c428-8cfe-3c03-a1f9-bf2b847e51ee | -6.94769 | -55.7103 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ece72cbe-35ba-3123-ac30-dfd59aead6a4 | -7.55522 | -61.42081 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7df7a407-8149-3c79-910d-53f892aa4830 | -7.57654 | -61.30032 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2d5ada78-01ac-3c46-a72b-f5d6b12096d4 | -6.74285 | -55.6553 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a23b141e-08d9-34ff-8320-0d86e6d824c9 | -5.88108 | -57.7609 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b09e29cb-8456-329b-8caf-01c0ec30f63e | -6.88863 | -59.45298 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9cb28408-b7eb-3a42-9111-4a77033193e9 | -5.97394 | -57.69616 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 885eb633-5dd6-3bd9-ae3d-3d46b0b28196 | -9.93701 | -60.5076 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3e400175-5a8c-364e-9e0f-eccff84ffb86 | -10.49697 | -59.60589 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f4ad7ffe-ad21-36ee-b1c4-17ab71a80bf9 | -9.93579 | -60.49861 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dcd0ff45-0469-3831-9f7a-f46e73f7f972 | -4.95591 | -55.86382 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 025db0e5-a90c-374e-a096-c47ddeb84356 | -7.62602 | -61.33036 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| df76902f-325a-31d6-9b9b-cc9620c16b7b | -7.00839 | -59.64965 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 22d4be4c-0232-3970-9d38-63cf0f24ca6b | -6.69792 | -60.13475 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d0ff86a7-f2eb-32f0-b2c6-67d4f8778d8c | -6.67915 | -58.75145 | 2026-08-30 00:48:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a6c3f907-4b35-3640-a54a-ce5d1d3d930a | -9.07114 | -60.43871 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e17d0142-4c0a-3312-9fa7-41f19a5f551c | -10.4806 | -59.61732 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 65854457-a52d-3a58-8c69-561219fcd466 | -5.48402 | -57.1413 | 2026-08-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d231c53d-a308-34eb-9e89-64a909413b9a | -9.89758 | -60.28476 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 07e9de74-493b-3a65-94ff-cabda1aa267e | -9.66805 | -55.1174 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f4d407c2-4408-3ab4-b5ca-3e00a26f8483 | -6.90606 | -58.98533 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4fc6f72d-1b2a-3a1b-8305-cc26a0569121 | -5.90055 | -57.75814 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 56e1311a-0d42-3f59-8bf5-f14b5a679bbf | -6.16364 | -57.80041 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a74db092-18da-3503-8211-8e017375f61e | -7.45256 | -59.93348 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 58501af6-cbff-318d-9d16-6155516f6fb1 | -4.95193 | -55.84267 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| d0cd03e6-9002-31d1-8bef-45a90715f53c | -9.09141 | -65.49732 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 439d0f50-ed09-3ffb-ac32-42285dea5ad3 | -7.30562 | -60.59577 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bed59941-ec72-3557-b55f-a16ccc8f9e8e | -9.16245 | -58.31059 | 2026-08-30 00:48:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f19639a2-8ede-336d-9b56-a4629a5ff903 | -9.24271 | -60.41132 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 03e2ea0c-5995-39f0-a52f-e2b0684135ad | -7.55696 | -61.30008 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4d03de5-0bb4-306f-855b-6671b5cc27ad | -8.78039 | -62.45651 | 2026-08-30 00:48:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c7e79951-d2f7-3e11-bc6c-e1cbdd32c6a9 | -9.14422 | -59.62967 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f32926f3-3f7b-3f39-82d3-af9c62565c7c | -9.21828 | -59.7575 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7998e87a-7e10-3344-9c89-fa5e7cc0a15a | -9.27801 | -57.08802 | 2026-08-30 00:48:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 32786765-c472-399b-99be-90eb38e48ad0 | -9.41439 | -56.98281 | 2026-08-30 00:48:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ef0d0018-d1c2-31cf-87e5-51121ab9ba90 | -3.76426 | -59.33295 | 2026-08-30 00:48:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| c3611a02-c36c-30c6-9dd1-2b640a7534cb | -4.69559 | -55.65926 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4ff95ed1-05fd-343e-b0ec-f5a43913a325 | -8.92865 | -67.35716 | 2026-08-30 00:48:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| cbe6376c-553f-3bdc-aede-7b8e8f54a86b | -9.01494 | -57.54324 | 2026-08-30 00:48:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8dbd3d22-0044-338a-a0f6-67d7faed9833 | -6.78278 | -55.68834 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 10864947-6398-35bb-a568-f48c56c94fe6 | -7.59157 | -61.34448 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README11.md)
