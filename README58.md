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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 563360c2-8ba8-30cc-98f7-eac3e8b88f0a | -14.4534 | -53.35482 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae0410d4-237e-3d7b-96b5-dba9bf0d7679 | -9.18914 | -59.53136 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba2b14bd-7d05-3dd3-a84e-e812480de7d1 | -9.18948 | -60.79726 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e6c6ed6-3e88-358e-92ff-7d06d41f8c1a | -14.23959 | -44.12183 | 2025-08-26 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79ddfecf-c168-3ae1-a348-bb8ee6c3d7b5 | -11.5222 | -52.13208 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 9b183e55-9628-3905-a579-632a35fa216d | -10.50073 | -46.88184 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 950982ae-973e-3c39-afc4-802935b539f0 | -9.1959 | -59.5216 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8886dec5-f3c8-38ef-a55b-9fb8ac8bca9e | -8.84514 | -62.44477 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| a9118274-2825-32e4-86a9-715eb57ad65d | -11.53654 | -52.12721 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 07f81520-518a-3567-b3ed-dc758373ac26 | -11.56359 | -52.10638 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3879825f-fd99-3988-8720-f1738126fd5f | -11.5669 | -52.10691 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9ceafa4e-a7d9-3b52-838d-f154df606693 | -8.98788 | -65.42707 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5c568dfb-3f44-376f-b18e-a3cbe711fc7a | -14.44677 | -53.35371 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90c09e6d-79e0-3ef5-85c7-1e60741fb445 | -10.77305 | -46.38677 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4633f99-bae6-3022-9aad-c10bcfec350e | -11.63715 | -44.86852 | 2025-08-26 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9d63968-f4b5-301a-8f04-31a829c2c328 | -11.56193 | -52.0953 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90f271b7-d1ee-3744-a62b-8cbcb2caa607 | -13.4128 | -46.92652 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 473c1368-cd53-3000-b2bf-41567d069267 | -9.16808 | -59.45601 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2d418d70-538b-38ab-b4bb-48a7aa1d8655 | -7.53757 | -61.38868 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6896e82-08c1-3c30-b359-e3fa663dc321 | -9.20646 | -59.4359 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ebe39dfd-c9f4-378f-86c5-1e2a4e9f43c3 | -12.74801 | -48.15775 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2e09b143-2f7d-369f-badd-5e7fbf1bfc0d | -8.99063 | -65.41353 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e5ea4e1b-dbb9-34e8-a701-7d949e84af5d | -9.18366 | -59.45734 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 36351513-cde1-3d4f-8e81-556493c0a539 | -13.00653 | -56.89226 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8028abde-c4cb-38cf-aa1a-8cd6afd88771 | -11.51888 | -52.13155 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9efeddfc-2448-3a16-871d-666712a75f4f | -12.74025 | -48.15695 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22942b46-4e6f-3140-b2f1-2ab425ccd208 | -11.14995 | -44.75108 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49ce094d-4749-377c-9d4c-7e65adb45212 | -11.55034 | -52.12584 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32f72265-0e4b-3558-8f78-48d2da9e71af | -9.17018 | -59.4494 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 09d01c7c-8304-3778-b7db-4d73e14306b7 | -11.54427 | -52.12126 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aefadf70-247e-334f-8702-d92f2d801c93 | -9.18529 | -59.5251 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 158f4389-0045-35f7-b1e8-9466587a9eaa | -9.15625 | -59.54743 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3400b3cf-1c60-30ff-b40a-d41f0717c912 | -8.24902 | -61.46301 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f75cb233-4963-3fbe-a109-6927bb24db1b | -9.18239 | -59.54106 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 306334e4-4a8f-3d51-b65b-f9c5a4de0383 | -14.72364 | -45.37025 | 2025-08-26 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c56f26e1-40d1-3025-aac8-66c99ac58592 | -11.08578 | -49.9964 | 2025-08-26 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72d61a3d-7f9a-342e-9727-81e8d6c85bdd | -9.18241 | -60.80607 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 756aa748-042b-305e-9fe8-090df2f4f98d | -9.7952 | -64.25523 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e3508a6-d27a-38bf-a190-927e2b652aee | -12.39321 | -45.00924 | 2025-08-26 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9b97282-53f2-3820-af75-3d3df47f9ea0 | -10.53446 | -46.79045 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9cac520d-ffd0-3737-8aa5-bc6ce51170c3 | -12.75846 | -48.1391 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fedd7b94-d4d9-3d58-be1a-c95b5d00a1f3 | -8.84121 | -62.44379 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 30a5e392-ba50-3686-946f-6753757b4a9c | -13.60882 | -48.17095 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b198760-eebc-3eee-b5a4-a9510dd12092 | -9.07481 | -65.72503 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d02fa122-e1c1-3347-83fc-2f55a415de99 | -10.0106 | -62.39556 | 2025-08-26 04:46:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f49d7c59-1e31-3229-a12e-ba946b79af0a | -9.19303 | -59.50996 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6438c01a-a619-3314-91cf-51d486dfb03a | -8.55208 | -62.64415 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4e92757-7120-35f6-afbb-51f724c8d914 | -7.87676 | -63.01498 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f474966-3f7c-3726-bcc8-343a87d0bbbd | -7.3841 | -64.34503 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c3b7b88-74a9-3774-8eed-e28ad5d31339 | -10.5185 | -57.9796 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c831396d-b16f-3255-a0a5-304e86106452 | -10.78206 | -46.38362 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6fa5123-8e5a-3b48-a285-56cff41a09de | -13.4378 | -46.86905 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 800868c7-ef11-3157-b12e-69da96c8070a | -11.05197 | -52.01339 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87dee936-6b93-36c8-aca5-1207e7293a8f | -9.19495 | -59.49934 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28dcab3a-2dd7-3503-a586-cc5d38da11ef | -9.07624 | -65.71771 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5489a81-7691-3864-9c6a-bd30d3285e9e | -8.55541 | -62.62631 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd471584-6375-3678-8dba-5ab150eafb8e | -14.30597 | -53.06401 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31dc844b-58ae-30ae-bba7-b3b6f034b4df | -10.41462 | -64.38059 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 977fb920-485b-3e26-a562-5f928d593749 | -15.0642 | -48.69217 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5edb3c30-8392-38f7-bc61-b1840b041cf9 | -8.83049 | -48.1691 | 2025-08-26 04:46:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1fcf1cf-cb9e-3d71-9911-6fdb7bbb4b7b | -9.16313 | -59.51 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5da6711-7d13-3724-ad61-1c58bf19efb5 | -11.30134 | -43.29416 | 2025-08-26 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c120c2d8-329a-3f9b-84e3-4c4c366feaf1 | -8.85606 | -62.45135 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7bc43d7f-c812-38fe-bc72-47f5efc07b40 | -9.0327 | -65.73053 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6816d882-bc2f-398b-a41a-75ef0c0953e4 | -11.3008 | -55.11386 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 738a9168-8ae6-3387-a07b-ea7f2de21f59 | -12.7445 | -48.09706 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0246d59-1822-327a-a7d1-a85a7f211747 | -14.36205 | -51.91625 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 370e12df-d7a0-3d2c-aa61-fc6af354d829 | -10.54404 | -57.95942 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d4cb3d2-c5d8-3111-a557-fff802f8ff20 | -13.48936 | -46.87024 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e1a1950-2dbd-3550-a2c3-3305fb71d9bd | -10.54829 | -57.96019 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce39a532-5f73-3bba-8ee5-3ea623e7bc4d | -11.15404 | -44.76853 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 8f81dc9a-e283-3798-8528-90d51526f423 | -9.18181 | -60.80933 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ff5dcec-d864-30bb-abfc-8927ceee9b65 | -13.44348 | -46.9907 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fde2f8cc-6ffc-3584-a182-8787ee7dbb3f | -12.93733 | -46.33222 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35d96921-ffcc-3287-975e-5145afc90f9b | -10.41356 | -64.38602 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5a9b94d-043c-3e80-b352-6ffdbec72396 | -8.59554 | -62.64333 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32142830-9998-3379-9b2d-2bd74fc0e097 | -10.81746 | -46.3759 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8131e646-1c79-378e-98d0-8a76f922b2e5 | -7.47437 | -61.35314 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c77a4985-86cd-3937-8fd5-deafa540e235 | -11.62193 | -46.22195 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9e09e96-53b1-3639-8fa6-89f4494fcaaf | -10.54105 | -46.80254 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6b12dcc0-fbc5-3bce-a72f-6d26cbc90681 | -11.5531 | -52.10828 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2c992f-d311-3347-a1a8-21fffa72bf3f | -12.70562 | -47.88494 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c720ae91-b27b-3fd0-a223-875be5a30329 | -10.70831 | -55.14109 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05cf20ac-3e8b-33fb-9f75-a459be847eb7 | -8.12293 | -62.87647 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8762c88f-cc07-3936-bca7-bfc5c992dc2b | -12.44169 | -48.71393 | 2025-08-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21df50b3-c44b-3f45-842b-6a58a946d8e3 | -12.76698 | -48.10593 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaf66f06-511e-3e6c-b818-d19fdccf3d28 | -15.02657 | -48.17165 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9a5ab58-3fb3-30f6-b4a0-21c446554f73 | -7.47719 | -61.36951 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eced250e-bc3a-38b7-96a5-7aa7ceb12d23 | -8.87873 | -62.46024 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 262840a3-d954-36b0-ae09-345bbff122c9 | -12.02389 | -49.70792 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dab2d0c-36c3-3446-969f-2749cb4a3029 | -9.17356 | -59.54355 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 109a9786-dae9-3a9f-bceb-ab494c2e940a | -10.41894 | -64.39277 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b65d0ac-0f1d-366f-936b-e2c25875d445 | -9.18627 | -59.51975 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5736003-3658-3ace-8919-8f88f945b8ef | -8.55457 | -62.63077 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5abc7983-c55e-3630-b597-55759ab88b7f | -11.55034 | -52.10424 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32454e25-29ca-30dd-81f8-c4f101d3ed30 | -15.06352 | -48.69719 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5219874-8b34-3413-b811-67061e5048b5 | -14.45009 | -53.35427 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b6912e8-498e-3f15-8e3e-cce28ffcd373 | -11.55089 | -52.10073 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c4d3f4f-efef-36e9-8305-aab877be4c18 | -11.568 | -52.09989 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec1e541a-c919-3f77-af20-86a777374cdb | -8.59938 | -62.5889 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README59.md)
