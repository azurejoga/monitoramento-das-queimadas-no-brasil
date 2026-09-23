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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e7090cb-60f0-30e1-9030-9326fcc2387d | -3.9646 | -59.347099 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53113c58-0975-34d3-b5c6-4f60ceba4290 | -9.9428 | -48.478901 | 2026-09-23 00:36:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35615790-6a23-33bc-abd5-13f9ec3077ec | -4.27 | -55.447399 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a186ef-3d4f-34d0-8974-dc4dd6d0ec57 | -7.0897 | -52.740299 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 281c44ed-0e0b-3756-b071-01c9544d7d1a | -3.7962 | -52.362099 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c04eb6f2-5a5c-371b-acd0-88586230eaa0 | -12.8177 | -50.8559 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc439e9c-cbdb-3c32-9d9e-d611b091a636 | -3.2923 | -59.424 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d24a5a2b-d663-3aa7-9cd4-4c05bb399764 | -12.8589 | -50.855598 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5472d3f1-293e-3837-9710-37c2d231c94a | -7.1166 | -56.546101 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8b05e07-a18f-3af1-9e6c-2332bacca084 | -9.9644 | -50.248901 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33b03f1a-0107-30d1-8a74-291176fe145e | -3.3249 | -59.7995 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f328556b-94a1-3a17-80c5-ed0c23d143aa | -6.3129 | -43.952999 | 2026-09-23 00:36:00 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90afe67e-2e89-35b7-ad87-37567ea24bcc | -10.3859 | -54.4123 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8b62fa4-6c8a-394f-acf6-f82cf6e86b24 | -3.1598 | -60.073601 | 2026-09-23 00:36:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de91f073-60d8-3abd-95e0-eb170f28045c | -3.0436 | -54.412399 | 2026-09-23 00:36:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c59422a-3f18-3302-ba45-09a969b2e015 | -5.4181 | -60.1992 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44298afc-b64c-3336-8ccb-6c74a716199a | -7.5626 | -57.666801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ac930c-bc97-32eb-a5e6-3c8e2a2a40e5 | -2.4682 | -57.911598 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56563e7c-0efb-368d-a1da-560432a2d486 | -6.907 | -46.539299 | 2026-09-23 00:36:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09c8c99f-1cdc-3e45-bdb3-655047d7d801 | -2.9346 | -57.786598 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b085897-9c20-3f47-93f7-6821d6783f55 | -3.0161 | -57.919498 | 2026-09-23 00:36:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d629d461-4c3a-34f4-96dc-1cdd341af579 | -4.2844 | -49.110901 | 2026-09-23 00:36:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1a27a78-8d96-36a6-a495-8c3301e256c3 | -5.2733 | -60.195099 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5c86b5f-fc04-33c2-9389-b1b12071e59a | -6.6857 | -58.445202 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3154da-d150-386d-8a36-5cb5696ad6e7 | -4.2544 | -60.001598 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4fd56e6-90d6-3616-a654-f8ed9518c7de | -5.8061 | -57.729801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7bf7e3f-8ed1-3705-b41a-9f14a715e3c3 | -11.7487 | -51.009602 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9929970-2fd1-38fa-8442-5284e1a9a496 | -3.1366 | -57.6772 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de4fac88-79c9-36fc-bcb6-ed7a27dce5d5 | -3.1049 | -60.703201 | 2026-09-23 00:36:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77367e99-a9a8-3bf8-b8a2-9e436b38d6c0 | -7.4537 | -61.358398 | 2026-09-23 00:36:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2deaeb-7dd4-3634-bb16-07482b076f5f | -5.7768 | -47.147202 | 2026-09-23 00:36:00 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2df2d0a-ef0d-3296-9d87-b74210acf310 | -8.619 | -54.624001 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7fed921-991c-3111-940b-f2f061ae1d45 | -6.6278 | -59.910301 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c65a78fe-e6c7-3131-8a21-93d41ec4c215 | -10.9057 | -53.933601 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c80475c-7d80-348e-9950-94a45a418023 | -6.1306 | -57.753502 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af494292-ffe9-3604-adf9-f28938f2d3ca | -12.4784 | -46.992599 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8e912db-95d0-306c-add3-ba4ffefccaf0 | -4.3384 | -55.657299 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eece35ee-6604-3c4f-8672-69ac3d77186f | -3.4881 | -59.562698 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f78fbdd-a6e0-3da1-bfd8-12420f2c18af | -6.7447 | -59.459099 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48e8b2cf-96d5-3995-b034-8aba1f289be8 | -3.4681 | -59.519501 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11e1bcc5-70c1-355f-8ed1-baf45e4cb502 | -6.1211 | -59.940399 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed5002cf-525c-3e8d-863c-dec8a1dc822a | -12.4029 | -46.940102 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 924d7112-0ebf-3c75-8d88-afe8ac1d3411 | -2.2798 | -56.669201 | 2026-09-23 00:36:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5dd9671-1ac2-3c3a-ab12-7fbdf59ed6e9 | -8.9117 | -62.363602 | 2026-09-23 00:36:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3666994e-42a2-37d1-bf2d-cf1d6892007e | -3.827 | -59.330101 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aef0dfcb-d61e-33b6-8064-ac054953c9b6 | -3.6285 | -58.903 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f181058-00f0-3169-9373-93bd24ca6c11 | -8.2079 | -56.0844 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53275a82-d965-3f2c-814e-eec737aa064f | -10.899 | -56.190498 | 2026-09-23 00:36:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5c064b6-94c1-398b-a7a3-9c65309569fd | -3.4684 | -59.567101 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2820d2-dc04-32be-a6a8-d5920b101e31 | -5.9843 | -57.697601 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0074a4ac-76fe-31a0-a38b-5b5977a79d4e | -3.5887 | -50.028 | 2026-09-23 00:36:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca67f6dc-53ed-3dcf-85be-cfb0554ed1e3 | -5.9823 | -55.3606 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c20d43d-f39d-3f9c-98b4-05ee46bbcd9d | -5.928 | -59.903301 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbdce631-02c0-3de0-9b51-8b31a4ec3600 | -7.4151 | -49.8582 | 2026-09-23 00:36:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68610a1a-7177-3e9a-bac6-11e211b0f018 | -3.7513 | -58.853199 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5892396-d36b-31b8-8746-565d4cc3acb4 | -3.707 | -60.544998 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aba19ddd-9f7d-38fc-94a8-3780696bf749 | -6.734 | -59.410599 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 365da590-37b5-3b8d-8293-0e8a5baabffc | -9.1043 | -61.4314 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3519e66-3d2e-37a0-9745-b961f888fa93 | 3.6764 | -61.852299 | 2026-09-23 00:36:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 13e00e6b-ffb2-301c-aafa-a27920291374 | -3.2906 | -59.4165 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60b74285-c540-3998-8c63-bd24dc4658a1 | -2.1048 | -49.691399 | 2026-09-23 00:36:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d08e88e-656e-376d-91d5-42c0a6dbefd2 | -6.4546 | -54.990501 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4427d6f0-ed36-30ca-96b7-0a65b4e43d4c | -3.6893 | -60.5578 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9f3b055-2391-3997-96f9-d3a2e7de0fad | -6.0682 | -57.796799 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bac43bd-763a-34fd-b006-6e843cd2e00f | -3.4928 | -59.169998 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f40c61eb-b862-38b4-8ac0-33a12c8aa769 | -6.4551 | -59.9655 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8533bd15-50c2-3ed6-97e1-56f796aca86b | 1.7814 | -56.023899 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1e53921-42ef-39ec-b184-da4994cf2d91 | -3.5294 | -59.6096 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30817d28-28c5-3d0d-9110-a542aa46c2c2 | -2.5617 | -57.504101 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02208027-a85a-32c4-8a1f-4aa6a9d960e6 | -3.0726 | -61.203999 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da56650d-6557-36d9-b7c3-70a46cf41bf5 | -2.8474 | -57.354801 | 2026-09-23 00:36:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 322fbb59-b528-3850-a5ff-8d7d2dc95096 | -3.1479 | -57.681801 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77e18425-02d1-318a-83bd-b4727da8faaf | -3.6121 | -59.013199 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b139aefd-d501-3fd7-b768-faef473b5db1 | -3.0729 | -58.400398 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03b974c7-ff45-3aa3-b9d1-9db6be8eabcb | -3.8778 | -59.557201 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70244c1e-ab91-3dfb-ad97-1c1be0b4001e | -3.7657 | -59.470001 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76193a50-221e-3a68-8223-e2d26d13e8e0 | -12.8612 | -50.865101 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e581ec02-32c5-3c6e-9afa-c34add96673f | -12.7953 | -50.891701 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3bb9469-a830-32e8-832b-c4e29fd9275b | -10.8531 | -56.215599 | 2026-09-23 00:36:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4abffdb6-dd56-37a7-9933-d578e0fef55c | 2.9287 | -60.432201 | 2026-09-23 00:36:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2bafa13d-64e0-342a-b24e-34a536162e58 | -11.0158 | -54.144798 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29e5c61c-ed2d-37aa-940e-5263a3b4379f | -8.1715 | -54.787102 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8b67155-e792-3a2c-836a-c9d20f782e30 | -12.8004 | -50.8703 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 919fbefc-2fec-3be3-820b-0f952686edfc | -3.7309 | -57.2514 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12fecac6-a56f-30b1-91c4-e9eaac25143c | -3.6478 | -60.602299 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45c39a20-a350-3876-870d-2c234e566f84 | -10.2453 | -50.215302 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9a7879-7f0d-3a5c-aa2b-82760b2376b1 | -4.3351 | -55.643101 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a6225c-5337-3d9c-a927-b15aacfe7c98 | -6.618 | -59.912399 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd8d822e-125a-33eb-aeae-c333190b9533 | -2.5632 | -57.511002 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1a0a9cb-7722-3518-9c9a-bc169c91fdee | -4.2066 | -56.3475 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd75168f-0b2a-33a4-a603-20c0d1dcea7c | -6.4239 | -59.963402 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20047698-97f5-30e6-8565-82d523ac4fe0 | 1.5696 | -55.9128 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3b954bb-5fa2-3730-a72c-1b45b3fd0607 | -3.3387 | -59.861599 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 580505be-cd87-3371-8915-d473e5248019 | -2.5495 | -57.313801 | 2026-09-23 00:36:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8dc6d84f-110f-3dbc-a380-f19ec4612d83 | 1.5702 | -55.864601 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce65a9e1-ce9f-37dd-a2e8-80363d52ce37 | -6.4533 | -59.957001 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2775253a-7c0d-388e-a6a7-ed0dae4a9bd7 | -6.1603 | -59.9319 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03fecbcd-85d5-3f51-b72d-1c75ba0c236a | -9.9448 | -53.972401 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7506bd6c-a98d-3a59-82da-4c15bfe4c4b4 | -6.184 | -52.792702 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c967fc5-4421-3213-84bb-3ac1df25292d | -6.1915 | -57.703201 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
