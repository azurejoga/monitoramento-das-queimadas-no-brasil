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
| 7acc44e4-40a9-3927-beea-3633f39486ed | -9.31247 | -57.70231 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e0c81f1-152f-35f0-9b12-da86f2cd5040 | -13.6365 | -48.20537 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b675938-8ce8-3309-a7ae-4fb1a7fd5a8f | -12.66707 | -48.18534 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8b3943c-1656-3fb5-b9ab-21a46ca319c6 | -13.60091 | -46.86736 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 989826e6-4731-3812-af77-5f2780964bb5 | -8.19019 | -61.3759 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d14ced7b-bf4b-38ac-9d41-8cae15958740 | -9.16819 | -59.55983 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 594c8afc-c18a-3a26-b2b2-dbb4ca8802d9 | -13.41905 | -46.97186 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8481e874-52a6-377d-95a1-577b288d918f | -7.54489 | -63.84642 | 2025-08-29 05:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0833946f-a665-330c-a6a3-e7af3373bcfb | -9.11757 | -65.78501 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8b90d11-7566-39f2-bf0f-7fd15bea4a0b | -12.40608 | -46.49509 | 2025-08-29 05:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c5ef46c-671b-3c27-931a-694314f34ca8 | -11.26738 | -45.49601 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de14cc1c-4ebb-3c47-ac5b-bc8ddc00760a | -12.89041 | -48.13958 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b147a456-20bc-3ea6-9a99-a215a367a48c | -11.51613 | -57.99101 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2760111b-6f07-349c-83e5-100cadd9a8e1 | -10.86245 | -47.49412 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a221607e-3082-3a2a-a5e3-011d016687aa | -10.37201 | -57.82623 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6f2679c4-f771-32a0-9a57-134d6a06441b | -12.99825 | -56.92762 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ea07f15-2f00-3831-8947-ce70ed9e1aee | -13.00547 | -56.92516 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f61120e8-9884-3cda-aba7-10078255504c | -12.32028 | -47.05002 | 2025-08-29 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa08dd60-7838-3078-8a3d-d12576baeaab | -9.10933 | -65.7427 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 254993e3-5725-3459-a604-9c0a37168e8c | -9.21947 | -60.8709 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 89c7d5c3-46bb-30a5-89f0-7a7ea797d977 | -11.72969 | -61.75698 | 2025-08-29 05:08:00 | NPP-375D | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25f08bff-6c91-3e7d-93ec-7814f775d06c | -9.15828 | -60.92424 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63dc0ce2-6a5d-35a5-93d9-b17e91af1375 | -9.10999 | -65.7392 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c0fd661-e0a3-323b-bb85-87d0d129f6e6 | -12.8404 | -48.15863 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e58efe0-34ec-3773-8d4a-92d216ba619c | -14.78142 | -59.73159 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df014c44-b5e5-3b27-af03-22da814ac542 | -9.31701 | -57.69563 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8541faf-404d-3daf-b0dc-0f9e721b4c6b | -14.32129 | -60.35951 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe3bca2-9268-3126-9636-5b9f7338060d | -13.37652 | -46.87657 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a99d3f12-87a5-37a9-a053-548b7ce5fb95 | -14.31549 | -51.89101 | 2025-08-29 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd919acb-cd0a-3a54-a067-917437b1099f | -12.69728 | -48.19976 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2976d820-03e9-32d5-aafb-7d683f8ce7dc | -10.97621 | -46.91369 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d5a0a711-1b30-31b1-b509-c96a6edd340a | -12.52199 | -53.81686 | 2025-08-29 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9395aede-f245-3f4c-a7ba-61ed8245b15f | -10.97808 | -46.92747 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 5fc776f1-038a-3075-85c4-b3100e9d3c2f | -9.1163 | -65.79205 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e90c35b-9df8-3bec-9d90-20cf2e8c72cd | -9.18338 | -65.79646 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aef4665-31ee-31b8-845f-0f1ea48a7c87 | -12.39978 | -46.49813 | 2025-08-29 05:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 214ee3bf-0e64-35a1-81bc-e81b1d816944 | -12.92358 | -46.34158 | 2025-08-29 05:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3c5eac2-d14d-3fa3-9aab-ba3afbc92718 | -9.46516 | -60.3013 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f388cc7-d06b-3b63-aa72-464cdf015d1d | -14.3323 | -53.29637 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9440d588-18ed-3100-af19-23b4d314b792 | -10.85414 | -60.81683 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a22955e7-1b11-34ba-a557-6ef9a3b1d231 | -13.49817 | -46.84468 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa046c23-602e-3cec-be08-4b3f97a8c1b2 | -10.98345 | -46.85761 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc1f778e-79e1-309e-837c-f89b71ed7096 | -9.15956 | -59.58906 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ef8eddf-119c-3868-9f96-55b1c2838d05 | -10.38612 | -57.8322 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d691ae7c-4a88-338c-a45f-92b1a0a1bf38 | -11.32013 | -43.56161 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4ca0970-86fe-3ff9-898c-6bfdcc7760b9 | -14.60461 | -54.50103 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6586a185-3b72-347f-b0ee-7e59e7564e58 | -13.41336 | -46.97061 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bb52cfa-6f12-355f-80e2-734f897fa096 | -13.19781 | -45.2883 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6d216a5-7190-3393-8f32-0b9319562ff4 | -13.41639 | -46.98306 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 391c518f-185c-30aa-84c2-43f1201ce1f8 | -12.82817 | -48.17065 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4935081f-b2c5-33a6-a765-3c26b94a1ec2 | -9.10348 | -65.73909 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcdb4a89-cb3d-30ea-a594-7d781abc6cda | -10.37085 | -57.83346 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9b1f14ee-13a1-3498-885e-a9fae4968943 | -12.69802 | -48.19384 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2a43b801-3d46-3445-a4df-b9ea343b4bee | -9.13135 | -65.80457 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74deba9c-4332-357f-bbb8-dbc77a9631e9 | -9.11214 | -65.78398 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 606b3fa4-b14e-3301-bfc0-183230a2663e | -10.41174 | -57.69583 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad71d1aa-6941-3aa8-8b09-32e0e6a9ee0a | -13.51377 | -46.85846 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6f1c17d-0efa-3011-8d55-d9c9efd85e66 | -15.04642 | -48.1305 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d30841-26fa-31d2-aeae-7a52989a3898 | -13.14042 | -54.92683 | 2025-08-29 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc6e3e84-043c-39a1-a0ef-4fc071cc62a0 | -10.45816 | -59.1218 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c9a2a84-439a-339b-97f8-ed80a7e82e0e | -8.12332 | -61.2107 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eeea4412-d3b2-38b6-bcd2-377a7ad36d17 | -14.50574 | -52.07375 | 2025-08-29 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60182142-6a02-3186-a73f-e43841794713 | -13.00048 | -56.91342 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74fe04f5-ff55-3056-8ba2-96006e596191 | -9.11771 | -65.78748 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff4977e-1f9e-32ed-91c1-301d5c2446e1 | -9.45338 | -63.09168 | 2025-08-29 05:08:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 522eb4ee-c5ea-3e55-ac82-3d7412ee5df9 | -9.00375 | -64.15788 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c02f225-f03e-3dfd-acf7-e2b7e0bdf340 | -9.45589 | -60.56384 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ed195acf-563c-3dc9-b1e9-23db59c0cf05 | -11.13762 | -59.22726 | 2025-08-29 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7225b045-3fa3-32a5-b70f-bc37e5233caa | -10.87667 | -56.37277 | 2025-08-29 05:08:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e911c82f-2c34-3b55-aaed-fc76f1abfe00 | -9.11162 | -65.79 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50fb90e1-1bca-3dda-a1dd-90c57f357ce0 | -13.02644 | -56.91364 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35826c1b-fc74-3a5f-a6e7-0e0741952296 | -10.72723 | -47.02207 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8105083d-bfbf-32e7-87f8-2a8c947b7641 | -12.70861 | -48.19448 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f74b1e31-f1bc-36af-b862-ff3939664a6c | -9.45369 | -60.55354 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| c7a0b761-1949-3364-98ec-c70b79241029 | -9.11094 | -65.79356 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddb1b181-9fc7-3c9a-823a-dc41b730c813 | -15.19944 | -52.34146 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00f139b3-eeb3-3ec5-b613-7aed9ec9f919 | -13.00104 | -56.90987 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5425432-0bf4-3785-8da4-a152c34ba224 | -13.54101 | -46.8773 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ff11149-abb4-3eba-b244-83481e415bcf | -10.46466 | -57.97096 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e50bce15-97bb-3a0e-a54d-2a040d22add9 | -13.00935 | -56.92215 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f773707-b5e1-3b52-9a6d-2d89625f0bb8 | -8.2793 | -61.41379 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f234721-2939-3b8f-b652-0129e443d64f | -11.61403 | -46.20266 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4a6881e-62fb-3919-b523-fd4ebd00e11f | -9.72949 | -64.90601 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 339b580f-f30c-3c06-80a5-f3d187ba6e44 | -13.53607 | -46.87194 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 14f803de-a40b-3d1e-87d1-72d4b14387af | -10.37143 | -57.82983 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2fa328ce-1ed0-3a31-bb21-2fa5e86c6df5 | -9.11901 | -65.78056 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cccab5d-3b73-3473-aaf3-a02c3ea49711 | -10.02318 | -51.10921 | 2025-08-29 05:08:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fc29322-2e02-3b3c-b879-ba122aa5f1a2 | -8.29826 | -61.40194 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63d9c2ed-be3d-3a62-ac47-3c1b8af6b025 | -12.91716 | -46.34492 | 2025-08-29 05:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 867a2706-ddae-31bc-a76d-132b3d68c8ac | -10.46711 | -57.93093 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb9c52b9-a429-3ddf-b41e-edf0b6fc495b | -9.41902 | -60.57208 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5ac131b-2306-3f00-806e-c5f91a4f4e23 | -14.7821 | -59.7275 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63ffac35-708b-3b23-96f5-29a613fb4e38 | -11.15706 | -54.3055 | 2025-08-29 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8636392d-5b2f-3e6f-b4df-1de07632a681 | -10.98082 | -46.90503 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dc4a8945-fbd0-3fb3-9fdb-fa10d14f6926 | -10.36538 | -57.80292 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1edf36a2-456e-35e0-bcb8-d58a1e28a20d | -8.17378 | -61.37305 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7419cc0d-9228-34dc-bd60-9e401fa170e8 | -11.4399 | -55.18718 | 2025-08-29 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0309c9b-8e0d-3f2a-8097-2e25ac9f9252 | -14.50988 | -52.07433 | 2025-08-29 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2aaf6597-617c-3d4c-8aed-e9b10e3070ae | -13.01923 | -56.91611 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d453b536-d464-3cbe-a4f7-38ec2c425337 | -10.95106 | -46.8883 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README70.md)
