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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f094499-f217-3cd4-8124-cb4bcb036ca1 | -10.1642 | -36.416698 | 2025-12-19 00:15:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6994326b-ac4e-39ef-b6fe-771755df8240 | -3.2087 | -49.3624 | 2025-12-19 00:15:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94e58d2b-b59d-3d5b-b2dc-c4d21c3b2219 | -11.7521 | -43.323799 | 2025-12-19 00:15:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f75ed0e-29a9-3f56-ab75-0a7e132b186d | -10.4999 | -44.9403 | 2025-12-19 00:15:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c68bf27d-df7b-3523-a6b1-18b0a0c54819 | -13.1728 | -40.334499 | 2025-12-19 00:15:00 | METOP-C | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9879dc92-a681-3a1e-ab56-afb60c29c081 | -7.7189 | -35.107201 | 2025-12-19 00:15:00 | METOP-C | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6a9548d1-3c96-3bae-9b7c-55761b388d1d | -13.3778 | -41.352299 | 2025-12-19 00:15:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8bab1900-5d5e-3e9c-be1a-89b67cd64d61 | -7.7219 | -35.1194 | 2025-12-19 00:15:00 | METOP-C | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ead75510-c103-30de-8b27-8647439de053 | -17.9021 | -40.128502 | 2025-12-19 00:15:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa75fcdc-fe4d-3bff-84ce-f6d9c0dcf0be | -9.493 | -35.948399 | 2025-12-19 00:15:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0bd86dd-4540-3181-b3bb-5b90eb66b581 | -13.3917 | -41.887001 | 2025-12-19 00:15:00 | METOP-C | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2f120fb6-2847-3126-8836-db3ac24ce3ac | -6.0748 | -37.3228 | 2025-12-19 00:15:00 | METOP-C | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| d272ec80-f27f-375e-810e-fd2276fba5e1 | -10.4978 | -44.930599 | 2025-12-19 00:15:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8e90cd6b-371b-305c-8314-aa62e387b62a | -17.9006 | -40.121101 | 2025-12-19 00:15:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0ec3aa02-25f2-30e8-aa72-97c9398de4a6 | -6.0846 | -37.320499 | 2025-12-19 00:15:00 | METOP-C | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| ce54082e-62ff-3533-a07a-41133c664cc6 | -2.9463 | -40.446499 | 2025-12-19 00:15:00 | METOP-C | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e34216b4-195e-3dc1-bc8b-8d6cb3f85164 | -6.5743 | -39.2719 | 2025-12-19 00:15:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| aee2bb13-261a-33e2-b0e5-bb0847c85919 | -13.1842 | -40.339401 | 2025-12-19 00:15:00 | METOP-C | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3b71a7eb-1688-36a4-b94b-306e44607947 | -9.4833 | -35.950802 | 2025-12-19 00:15:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82413f2d-1bd4-3cc5-ab26-d1f245cacf28 | -13.1826 | -40.332298 | 2025-12-19 00:15:00 | METOP-C | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 87c4fd0d-ad9b-3323-96b1-a17df3bbcf3e | -11.7619 | -43.321602 | 2025-12-19 00:15:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8021ea01-9ef8-38bc-a8b7-6d8b51483fdf | -2.9358 | -48.234798 | 2025-12-19 00:15:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b539d1f5-0d22-376b-8cb6-df67331abc44 | -17.899 | -40.113701 | 2025-12-19 00:15:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a644a491-bb91-35a5-8115-f1ef6468a78c | -3.7488 | -49.724602 | 2025-12-19 00:15:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e70a2dd-5f7b-3054-babf-be855a75e6b0 | -2.9365 | -40.4487 | 2025-12-19 00:15:00 | METOP-C | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 87d6ae29-e786-31db-bba0-a5202c267059 | -9.3454 | -35.596001 | 2025-12-19 00:15:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 222e1dd3-6b9a-325d-9d95-57c99de55ed9 | -9.4955 | -35.958599 | 2025-12-19 00:15:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 593e1a82-3973-371f-acc7-8e959031f48f | -7.8078 | -35.175499 | 2025-12-19 00:15:00 | METOP-C | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 06425c8a-a690-3057-ac26-d75bcde78a86 | -11.7538 | -43.332001 | 2025-12-19 00:15:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1847ecb1-9e87-3f81-a2b0-87b4dea0b067 | -13.1744 | -40.341599 | 2025-12-19 00:15:00 | METOP-C | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d24f376b-e175-3bf7-b7e3-9a919e2ae448 | -13.3901 | -41.879398 | 2025-12-19 00:15:00 | METOP-C | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bf9af127-6374-3da8-b94a-2d83e75f1ea1 | -14.5155 | -40.1665 | 2025-12-19 00:15:00 | METOP-C | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3db4d619-f061-30e3-b937-a6a1b5445b1b | -2.9331 | -48.222698 | 2025-12-19 00:15:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84b817e0-af42-3926-877c-65221e99fd14 | -11.7636 | -43.329899 | 2025-12-19 00:15:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 813697db-f438-3850-8466-f2bf54667472 | -2.9382 | -40.456001 | 2025-12-19 00:15:00 | METOP-C | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3315d324-73cd-3e9c-8679-24c079656bd4 | -21.23004 | -49.27354 | 2025-12-19 00:28:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 4341b7ab-dcf8-3c68-b225-b48348261568 | -18.83644 | -51.61566 | 2025-12-19 00:28:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 163ae4e4-87f9-356c-ae4f-569b8861a671 | -21.23134 | -49.28386 | 2025-12-19 00:28:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f092b8ca-e2ff-3051-9bfb-2a14af4caca4 | -18.8262 | -51.61697 | 2025-12-19 00:28:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d82cf53c-2b03-378b-be8c-c13f423e7e4b | -18.82771 | -51.62947 | 2025-12-19 00:28:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 70e5b80f-5234-36d5-88cb-483ed34660e2 | -18.83947 | -51.64068 | 2025-12-19 00:28:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4c8b1ac8-17c7-3828-9fe8-6deea71938f8 | -18.83795 | -51.62812 | 2025-12-19 00:28:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 252.8 |
| 6e4d5f0c-5852-3b19-832c-d9ed60ba777e | -19.56468 | -50.99162 | 2025-12-19 00:28:00 | TERRA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5ab855d1-5d9c-3d68-bcc3-6008234e3fa7 | -13.39309 | -41.88293 | 2025-12-19 00:30:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 91404ec7-d0ad-3515-8d98-c54407bb021f | -11.75216 | -43.32722 | 2025-12-19 00:30:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| f71ffba6-dc4f-325a-a1fa-e438bafe5951 | -3.70293 | -50.15337 | 2025-12-19 00:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 93748d4f-eb12-3cfa-9f31-2ae5b921f8d0 | -3.74504 | -49.7309 | 2025-12-19 00:32:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d00438f0-42ba-37d9-89d2-f09d7c05b967 | -3.75408 | -49.72952 | 2025-12-19 00:32:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 3ea7c14f-1b2f-3f80-a396-42b5806bf4b1 | -3.75278 | -49.72026 | 2025-12-19 00:32:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 854342bd-04cc-3113-9816-0df1e7b55ebb | -3.70167 | -50.14436 | 2025-12-19 00:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e7fe48d8-e336-3570-8fbb-a7367996fe20 | -3.74373 | -49.72157 | 2025-12-19 00:32:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 220656b4-e0ac-3a75-a461-5fabc00e87cd | -3.4536 | -48.83307 | 2025-12-19 00:32:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bccf3e75-78fc-3624-973a-399d2d235c1e | -3.00196 | -52.35028 | 2025-12-19 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb7231d1-3652-3f6d-86f5-ad10b3e62d5b | -2.90529 | -49.79045 | 2025-12-19 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 34da6b9f-a431-3707-b790-4c2903da2067 | -2.11003 | -50.9043 | 2025-12-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8e98b410-1a1a-3df9-99e2-2cfca9d76521 | -2.95937 | -48.5932 | 2025-12-19 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 29286bfb-9f1e-3911-9d1b-7c7296978d90 | -2.51354 | -49.11159 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4550d074-a98a-3a7a-bdf4-01f79756ffc4 | -3.05665 | -49.62214 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4eb15c4b-0079-3362-9140-033a5c1acc19 | -3.0176 | -51.19128 | 2025-12-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 30e7da44-8e4a-3666-9580-dba62896b197 | -3.28698 | -48.89006 | 2025-12-19 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| be7a151c-986b-33e1-8398-320ed5a1d54d | -2.67306 | -51.70783 | 2025-12-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6a56a042-ac32-3a1f-979e-4fd922931795 | -3.28555 | -48.87985 | 2025-12-19 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a1fcbfa3-b9ed-32dc-94d9-770bb95251d3 | -3.15864 | -49.42616 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d7f4d7d4-d713-3bfd-8de5-dc3aa43a8825 | -3.13324 | -51.70295 | 2025-12-19 00:34:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6001fdb3-484d-3da3-bc59-32b66bc1e037 | -3.20447 | -49.36391 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f8c4c9e4-8842-38a6-bebe-0937bb18c69f | -3.09056 | -49.59796 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8cf1f8eb-6743-3193-a406-1f14120a4fa5 | -3.01881 | -51.20005 | 2025-12-19 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b3f94185-4cb8-37d0-8f8a-12ef0b27e87d | -2.74536 | -48.381 | 2025-12-19 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 484745e3-6ab3-3a12-b5ae-a0fea6ed25bd | -2.98657 | -52.37086 | 2025-12-19 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca5ebaae-20e5-36f5-9f96-28894549d9c8 | -2.70247 | -51.64417 | 2025-12-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f09e1ebc-f7e4-3b6f-a6c5-05659fb02ab6 | -3.14942 | -49.42746 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 23fa4148-3bd1-3ec5-843b-328d9ba84e8a | -3.2137 | -49.36261 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 04b572db-aed0-3efc-ad92-c64cce0c4969 | -2.64693 | -49.19894 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90c841ec-b0ab-367a-8c3c-964408723a75 | -3.23218 | -50.54917 | 2025-12-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4329bd7b-a42d-3c57-aea7-356176da08a2 | -3.08923 | -49.58845 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4722fef5-2b7a-34a9-b3d1-7c4c16d7d11c | -2.11125 | -50.91314 | 2025-12-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a13ffa0a-ea20-3b00-b647-4bc83bdabdd4 | -3.20584 | -49.3736 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 810c1ded-e29f-3de0-992f-d5b4cc637041 | -3.18146 | -52.24891 | 2025-12-19 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8fff0c0a-cc45-39a2-8b38-9f4a80cabc80 | -2.90662 | -49.79984 | 2025-12-19 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bd7b1ac3-5e22-3f57-91df-55a1257a08c2 | -1.29255 | -53.05413 | 2025-12-19 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a133eb59-82b9-36e3-a10a-b0a346c6701e | -2.96087 | -48.60385 | 2025-12-19 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 24df54c4-9a26-3ffa-97b8-8f7794014a78 | -2.98781 | -52.37991 | 2025-12-19 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9d46d286-e7cb-30f2-9764-5c964554edc0 | -3.21507 | -49.37228 | 2025-12-19 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7a7f2190-f7b0-3c69-9b6b-354bda662ed8 | -2.2344 | -51.93437 | 2025-12-19 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10bb8af0-4af1-31b6-871b-44b322422663 | -18.8315 | -51.6319 | 2025-12-19 00:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 39884b7c-d128-3a50-801c-f1d927c53758 | -18.832 | -51.6099 | 2025-12-19 00:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7e8127cc-d55c-35af-806b-8ae135e9decf | -18.8315 | -51.6319 | 2025-12-19 00:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 67606c3f-ac48-3932-98ac-712271c5775d | 2.7435 | -61.0735 | 2025-12-19 00:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1d3d97b9-e914-3907-af5c-8c5e7d2bdb78 | -12.3074 | -57.3608 | 2025-12-19 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 85eb0715-30b7-326b-95b6-807c4414036f | 2.7435 | -61.0924 | 2025-12-19 00:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2e0c8a9b-3912-314a-97e2-98feea7d47c2 | 2.7253 | -61.0738 | 2025-12-19 00:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e509bd5c-f49c-301f-b18f-e4b4506004dc | 2.7252 | -61.0927 | 2025-12-19 00:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6152a5cb-e742-3777-91ba-b3aabedabcdd | -18.8315 | -51.6319 | 2025-12-19 01:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 8f30bf60-694c-3416-8755-58e65a6f87bd | -10.1048 | -36.229 | 2025-12-19 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 0c096101-fd9d-31e6-82db-fb523d47ce6a | -18.8516 | -51.6283 | 2025-12-19 01:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e12f6740-f539-37c9-9060-b4bebb62c410 | -18.832 | -51.6099 | 2025-12-19 01:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 7a1520dd-09e9-3231-8ef4-e20caad9ea2e | -18.8204 | -51.616798 | 2025-12-19 01:12:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e5152a31-ba3a-3d68-a649-c512d899e41a | 2.0408 | -61.412498 | 2025-12-19 01:12:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 25e4bd5e-4fd6-313f-a231-f9fc5e591f3c | -9.4648 | -57.8449 | 2025-12-19 01:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8f23ec87-955c-3bac-a033-e48082a49a4c | -9.4648 | -57.8449 | 2025-12-19 02:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |


[Clique aqui para ver as próximas entradas](README2.md)
