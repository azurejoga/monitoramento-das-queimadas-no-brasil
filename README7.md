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
| 569b809d-855a-383a-a1e5-27ad3968f4b9 | -3.2605 | -61.153599 | 2026-08-20 00:38:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebc86515-4db9-306b-84a3-2e0ae4e64637 | -4.9604 | -56.260799 | 2026-08-20 00:38:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c966d8f-be4d-380b-be99-14b01a815816 | -7.4327 | -59.7775 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e441829-e7e9-3470-aeca-01a29282f1be | -11.206 | -54.003799 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfa62c24-1009-3879-94db-395970f0eda6 | -9.174 | -56.999699 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7460ce9b-03e5-34b5-bb36-6e2192898ed1 | -6.3487 | -54.895 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd6ff21-22cf-3820-a373-1aede5abb000 | -11.2226 | -55.07 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6b4d8a8-dcbc-3cfb-b67e-cf451feadca4 | -11.2178 | -55.048801 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5da92612-7126-3c3c-ba0b-a2e609e17fa6 | -8.5614 | -54.789902 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a8a8b80-7305-3959-8d60-f61f233764e4 | -11.8049 | -44.8074 | 2026-08-20 00:38:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb1c9908-2938-3c97-be53-ae4d605541b5 | -6.7088 | -59.0994 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08931e48-0131-3f98-a28b-669d3bb2eece | -6.7461 | -59.035702 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0f31c7-733a-3fa4-847d-17baa7175aa9 | -6.6957 | -59.086399 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f067bf3e-1244-3685-96db-0d987b682f6f | -8.5372 | -54.8643 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e631ee0-d376-30c2-ab89-8cb436f5b340 | -23.4275 | -47.698601 | 2026-08-20 00:38:00 | METOP-B | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b6590899-3c1f-37d6-b211-80a1b9dcf47f | -6.6875 | -59.0961 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e14f23cd-1c4d-3e26-b1ad-edd6352e6030 | -11.1882 | -54.0158 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 312896fc-f369-3d1e-8f8c-58216ece4e49 | -7.4766 | -55.3195 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac18a74-db59-3951-ac85-a5fc8e8ce75f | -8.516 | -54.8615 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5066f423-4897-39b5-b307-80f2835335e7 | -8.5771 | -54.6786 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fec5910-05a3-3137-ad2f-2bbb22ce5527 | -12.4743 | -54.727402 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76c7c5e6-2195-3b21-81c6-e3f4bc096681 | -14.0288 | -53.630299 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 369727bd-5a3d-3dbb-b8ed-f567244bfe89 | -3.1018 | -61.179298 | 2026-08-20 00:38:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae690e84-f19d-3e82-bd93-f2dbcd9b1795 | -3.524 | -48.183701 | 2026-08-20 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7820b68b-527d-361a-b23f-5976554e8fe3 | -8.9577 | -60.5756 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a86a947e-c9be-3ab6-bc79-adaf8945b00e | -6.3917 | -54.9478 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349f2f1e-4328-369f-b97a-9d5eb0b9c87e | -11.2146 | -55.034698 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44ca4e9f-00f9-354e-8903-a573755ac12e | -6.7033 | -58.934601 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27eb5585-d4e2-36b0-92bc-0c46fc69ed8b | -6.6859 | -59.0886 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 964fdb9b-5df3-3610-993e-9fdb89987a0a | -11.208 | -55.051102 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27638dc3-bd9e-356e-8682-bfce5f16cc83 | -2.5683 | -47.260101 | 2026-08-20 00:38:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82deb9eb-d749-38d5-8604-5904003e21f8 | -13.406 | -54.381802 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 967e1f04-9d70-386b-8bb7-5ef211dc4787 | -9.1286 | -51.140301 | 2026-08-20 00:38:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2a54f06-07dc-3762-99b7-af962bc639a3 | -13.4414 | -57.056099 | 2026-08-20 00:38:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5781a323-a0d4-37df-8a9f-c5186341e718 | -6.8671 | -59.025002 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60a759d7-3778-3c80-9a16-04755733c5a6 | -15.4425 | -48.5802 | 2026-08-20 00:38:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a0b2c60f-1b77-391c-8ce6-b08c67a215e4 | -6.1366 | -57.867001 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f86bf321-0c45-3a2b-9ac2-bbbe61df631f | -14.1656 | -53.0592 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa9f6b1-8c80-3b8d-ba0d-76c16904c676 | -8.5622 | -54.658798 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09c54d6e-4eed-3535-97b3-681907e71525 | -6.028 | -57.796101 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9011d010-29bb-3a64-8e4c-aad7f911b4de | -8.5177 | -54.868801 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1dc4d2-0a3f-3e28-81c1-6de026d0753e | -11.7884 | -44.784401 | 2026-08-20 00:38:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| edd580ee-697e-3c4f-ac88-ae8f2780faa3 | -5.8046 | -55.714699 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b9bb4f1-cfd0-3ca5-a961-c6e117ea6a74 | -8.6699 | -54.6339 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d88bdc31-f761-3b3a-b16b-4e96f2a00144 | -8.5368 | -54.772598 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4835affa-5259-327c-8867-ae038f0e05b3 | -6.8862 | -56.4389 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 507f121c-d9c1-3878-b572-7657f86cb09a | -8.555 | -54.806702 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90453910-f9e1-3285-87b5-2ab205600df5 | -1.8375 | -54.494099 | 2026-08-20 00:38:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd86a7f1-738e-3991-b6c9-e5ac78040892 | -1.8257 | -54.487801 | 2026-08-20 00:38:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69e267ab-5559-302e-aad7-4ea3ac79e72f | -6.6131 | -53.3652 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0f023a-d420-3d89-a7a9-fd22bd87b5e3 | -8.9007 | -60.548199 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf381c4-c0df-3666-9130-6c443d2b0b0e | -8.0874 | -51.658901 | 2026-08-20 00:38:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64a18521-dac3-3e0e-852b-5e843d89c401 | -9.1163 | -51.131901 | 2026-08-20 00:38:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58851c36-401b-3053-9528-a461fb035177 | -6.8846 | -56.432098 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26bdaef6-eda2-306f-953b-99bb6c37da7d | -4.9522 | -56.269901 | 2026-08-20 00:38:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac35d0d9-aa76-3c02-ad5d-c3ac69b484f9 | -13.443 | -57.063599 | 2026-08-20 00:38:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f956464a-d45d-3b59-9642-2ea0e617aaec | -7.8706 | -63.738998 | 2026-08-20 00:38:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0f4b7ce-e5bb-314f-afb7-558b7f9f2c2e | -6.4391 | -52.7533 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 001379bd-7e8a-34b1-ac4e-0237d44e929c | -6.8981 | -55.7197 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd19b3e0-3cce-35c2-b2c2-dec6f8268cca | -12.9466 | -56.6217 | 2026-08-20 00:38:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b08991f-2c94-365a-8c10-428bc21af34d | -6.945 | -52.800701 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc15935b-627b-3aa6-8b66-e611295f2ac1 | -17.3134 | -43.604401 | 2026-08-20 00:38:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 120298e8-67b3-3124-b055-77fde6658bd5 | -8.1636 | -54.9883 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 137814ea-f17b-34f1-a427-94eb7740d664 | -14.2366 | -53.0984 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85f7edc4-2d53-3370-bced-dc0dff9db157 | -8.5841 | -54.754002 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0bbf7c8-d991-36df-be27-3bf053b03bde | -14.1506 | -53.038601 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ebcb9d0-c42d-36d5-92ec-a62083a0e18a | -8.8987 | -60.538799 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9145be8-3831-3724-9ed9-d15caa71204c | -8.7184 | -49.618698 | 2026-08-20 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec9b33d4-d18b-3581-b06a-e2a0ed1a474a | -8.1538 | -54.990601 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95392e6f-40e5-3109-947a-39b9df52f1c8 | -6.6404 | -56.400101 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8d90b6-26af-3668-90f2-f42a73207e24 | -8.5291 | -54.873798 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b15bc701-7155-3193-a75b-e4ce49ca34db | -12.4889 | -54.746399 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d892de5b-a14b-36f2-bab1-c5e3ddb8b0d3 | -8.9536 | -60.556599 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1aaacae-eeec-3c86-823b-a5f7db33affa | -10.7946 | -50.306702 | 2026-08-20 00:38:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e661c804-13ae-3d93-8e91-af811353a062 | -1.8296 | -54.504799 | 2026-08-20 00:38:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 931d23f7-e33b-3f56-965e-a5ea899fc73c | -11.7953 | -44.810101 | 2026-08-20 00:38:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f89bafe-fe56-3c57-a39b-810abcf16821 | -6.5938 | -58.950802 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27cc97c2-6b97-39e2-b61b-1ae5f8477db3 | -8.6598 | -54.589802 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93017564-10ec-33fd-af36-ff7989a95a2f | -6.39 | -54.940399 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4865a69-f56e-3281-bc5c-6a54bb347a4b | -8.5389 | -54.871498 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d932ea1a-8c10-3163-95db-6892e7845ff0 | -8.5824 | -54.7467 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad0055e-7421-334c-a7ec-a04397062ce3 | -6.8033 | -59.015202 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6060c91a-0e94-367c-beff-1784cd364d2a | -8.1751 | -54.993301 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66c27d07-3be7-3dae-bb4c-dde11d5aa186 | -12.4873 | -54.7393 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea8afdcf-361e-3cbb-b36d-c240a3d4827a | -18.8356 | -47.130699 | 2026-08-20 00:38:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 012b82fe-88ce-3ab6-abbd-a8de39dbfa6d | -7.5497 | -55.549301 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf946b51-1995-3e3a-ba98-e7c2d00bc506 | -8.6149 | -54.708401 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c52e7e0-cdb1-30fd-9393-2ca755131a43 | -6.7 | -58.919701 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 315bee92-f373-3437-9035-957769544113 | -12.4825 | -54.717999 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c46e2b0-1eeb-3b40-8c24-8c12183fa028 | -9.2138 | -59.7635 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b124ae2d-a142-35f4-bc48-53b72456a629 | -9.4272 | -60.4259 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01522098-33c9-3af0-93d3-a00a57e6720d | -8.6615 | -54.597198 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4286100-26b6-3633-92bf-8f55888a49ab | -10.3368 | -57.561501 | 2026-08-20 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2522f93a-a2ce-3225-a097-e0d4ec8c1de9 | -8.7087 | -49.621201 | 2026-08-20 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 091ba8f8-7c52-39b5-8dac-a54f43c9e24b | -11.2141 | -53.994099 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0a94afe-90d3-36d8-85ca-f547e375e419 | -11.8194 | -56.590302 | 2026-08-20 00:38:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7735a416-ce8e-3e82-b028-07fff08bfe81 | -8.1653 | -54.995602 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b009156-4eec-3096-ad69-22ee11a261ff | -9.4252 | -60.4165 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce04916-660b-32e2-a2f2-5d2ef7d6921f | -8.6831 | -54.646301 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 476f1658-8908-32d6-9210-398d5f046a5f | -8.6649 | -54.6119 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
