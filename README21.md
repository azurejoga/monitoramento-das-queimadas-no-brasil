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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c2f52a9-ff6c-30a1-9e9a-c6019a01bfce | -4.53609 | -55.52013 | 2026-08-23 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e122a84b-91e7-3e59-b63e-7c82c2eb9e8a | -6.71082 | -58.73142 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 637056f0-ddc7-3d18-b8e2-515803e720c0 | -5.00363 | -56.13741 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71949ce8-b51f-307e-846f-8aa1c8d17c92 | -2.50532 | -48.35137 | 2026-08-23 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ea777c-2fa2-3978-9c20-aadc48db62f0 | -7.25244 | -49.92445 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69847bdd-adf9-3ebd-b5fa-1e3b32955a1a | -8.16218 | -52.05132 | 2026-08-23 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ee08dd3-1808-347a-9122-f760b79515f8 | -6.80218 | -58.98424 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4338ec8d-ba73-3126-8d8e-f246448de977 | -6.53981 | -56.17734 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdf72de0-30cf-3440-b0a7-db69f124f6b3 | -2.9113 | -48.86897 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1b0ee86b-5637-38e4-809a-0dc515a6e874 | -6.95057 | -59.06516 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0d27a55-2e30-3228-bb63-07e011dde315 | -2.95318 | -50.31791 | 2026-08-23 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96f75ee8-daac-3715-999d-e90ddf5e1527 | -3.6542 | -49.44356 | 2026-08-23 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e90bbc9-3948-3bc5-85a9-ff2cc4b5406e | -6.18989 | -55.42964 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d5f34b0-fbaa-3e98-b8ed-fe27b88bbf2c | -1.42169 | -55.7254 | 2026-08-23 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3037026f-2211-32fc-89c9-85fdd7352500 | -6.37253 | -54.94873 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99302222-be8e-39de-a654-6af037f133dc | -6.12368 | -59.92516 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56fdbfb5-35c4-369c-b702-64ff3ec3d30e | -6.18836 | -53.52547 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbdb8e18-0f72-358a-a989-305fb4a478a2 | -6.80308 | -58.646 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc911b71-44c4-3f33-95d1-99304dc1fff2 | -2.96153 | -48.75015 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16eadced-ad00-3208-a856-1be9d255b610 | -7.01314 | -59.55299 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43890e01-065a-387b-bdf6-5e9d7375933d | -1.87117 | -47.98412 | 2026-08-23 04:44:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1337fd7c-d7dc-3023-9828-d9a908d9caaa | -3.69257 | -50.93108 | 2026-08-23 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8455011-1cb3-3a8b-94f1-eb6b25bb8ca7 | -6.25504 | -55.42148 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15ab8804-c599-3fd7-997d-ea2cb85b6c12 | -6.76778 | -58.68516 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b066ec59-6a57-3f81-a623-56e871eee4cc | -6.55823 | -55.09335 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66e05467-cfed-3acf-b97f-7821c0850f52 | -6.02356 | -51.33186 | 2026-08-23 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc616c6-8a8c-39fc-9f1f-464249ebec9b | -6.1855 | -53.51705 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b972c59a-f370-3e2b-9aa5-1892ec109674 | -6.80252 | -59.66035 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8873130-f3ff-325b-b75a-91d136d5d553 | -6.54 | -56.26501 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64d40f99-f39e-3341-b9a5-53dca17f926f | -2.35171 | -48.83103 | 2026-08-23 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e964c018-d02e-3ba9-82c4-607153d2524f | -6.18511 | -55.42889 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bd75d08-71e2-3cf2-aeea-9d3adb520ba9 | -6.94215 | -59.32161 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 163f9745-ff4c-3e67-be6d-a4ae2770a1d6 | -6.86487 | -59.02598 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00bb49c6-48d8-36d3-aae5-554e285529a9 | -5.96324 | -53.62716 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efb6721a-62a5-3afa-8485-edcd4f31303c | -6.86421 | -59.40668 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90f1d0e2-e6d5-3480-9e54-975a46ddaf0b | -6.18396 | -53.52573 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5565349-6307-3908-bb2f-85e8b3a51b23 | -4.31125 | -46.41667 | 2026-08-23 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 901e6c80-5ba0-3d3e-b52e-1f084d181255 | -9.45533 | -40.32393 | 2026-08-23 04:44:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 0ed1c79e-626f-3641-93c8-2e0d58cd325b | -6.94242 | -59.08362 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79c69019-de07-38ba-bc17-f86d2d15efa5 | -7.30236 | -42.9963 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0d782781-516a-35d3-a2c1-e9caf2e3527f | -6.52059 | -51.44791 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b879ed9-f9a6-392e-a119-8fa4bf8464d6 | -6.13929 | -59.91184 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b92052d2-695c-3787-af8c-246a51045b17 | -2.55948 | -47.24881 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9d00c06f-edbb-3aec-bafe-0afe1e42302b | -6.82351 | -59.96498 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c021f035-42c2-3c1d-a172-62f45fb70d5c | -6.67824 | -58.74306 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3a76a68a-976a-3b7a-b535-940461cc827a | -7.25305 | -49.92067 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d137475-d888-3968-8885-cbb4cb6e9651 | -6.80508 | -59.68086 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 494ddd46-9085-32b7-8e27-a5aec1d710a0 | -6.77492 | -59.44372 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 143510be-f67f-3aef-8fe2-4babf44d7440 | -7.69681 | -44.811 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07436595-b160-36bf-bab6-62fee7545782 | -6.78631 | -59.41663 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 680e22f6-7c69-3e11-a027-3b04b5fb8d34 | -6.86405 | -59.03042 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35da021d-790a-326b-a163-a98909766abc | -6.86252 | -59.41603 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e07f6dd8-3544-3da5-b040-4fe9b8c66dd8 | -6.76569 | -58.66309 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d68db41b-29ed-36b0-853e-752615e0c0b3 | -6.36794 | -54.94785 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5719b7f-aad1-3b84-b64a-f2b50bb3d763 | -6.71004 | -58.7357 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e994f5d6-d58b-300b-b043-c9d2c595d6f6 | -4.53205 | -55.5139 | 2026-08-23 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2345943b-d666-3063-b32e-91b62b0cbdf2 | -6.66794 | -58.74516 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 870a9c80-bce1-3d6a-b5b7-56bdfea891f3 | -8.3786 | -46.47272 | 2026-08-23 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 742291bd-c816-326a-93e3-78bc5d2c37d3 | -2.98847 | -48.95583 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8de91bb1-be9b-34a7-99be-98cdfc7e9dae | -6.20201 | -53.49624 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1125d4e4-eb7f-35c9-9622-745056f68bb1 | -6.80742 | -59.43984 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 139e7cd7-8620-3023-a849-e2cb62ed1998 | -7.29881 | -42.9921 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d93c9aa-320c-36b8-b732-803b46128acd | -4.1665 | -42.4409 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d061dc1-21f7-371c-877a-ca7089e9beae | -6.8564 | -59.41487 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81fd8ebf-4acb-3bd3-ab55-b2523cb2d121 | -6.25743 | -55.37906 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52dbc8e1-6d10-3344-8ce6-98c648c74527 | -6.7057 | -58.72617 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d371ed47-ad52-3780-8450-2b680f52e0f3 | -6.93809 | -59.07362 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5c5cfda-aa59-33ac-a19c-4fe6f20c6d1f | -6.02168 | -50.20802 | 2026-08-23 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e29cf51-ecfe-3af2-a641-6165f302b71a | -8.34595 | -46.50204 | 2026-08-23 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb374958-1095-3a33-8ab8-a7b86becee25 | -6.88084 | -59.41989 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e9a4910e-f2a9-3e59-9df5-a91efdd62b4e | -6.37741 | -54.95633 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66b8584c-fb87-3820-afc2-4b11ae943f35 | -6.75681 | -58.67878 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e357034f-e2a2-3111-bbd7-b6f1205161fd | -8.93116 | -48.54121 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4139c28d-4f11-3d7f-9d6a-09a939b21168 | -6.89655 | -55.70885 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f97756df-872e-30b8-a1df-810f4a8854ba | -5.28058 | -45.1094 | 2026-08-23 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49a148cc-bda9-35cf-8943-9157763d2c87 | -6.02505 | -43.01158 | 2026-08-23 04:44:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8b61d847-634b-3cab-937d-b8b6e1a4a8e3 | -6.94457 | -59.06411 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9969ed9f-e903-379f-9999-8f8f012d33b7 | -3.21197 | -48.9347 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2368ff24-7f3c-33ba-9470-f0b9fbd58856 | -6.79566 | -58.65344 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8a3b27a-5181-300b-b770-e957a3e40ce1 | -7.26669 | -44.19941 | 2026-08-23 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f476ac4f-9012-383f-885c-189aab5e80da | -6.19259 | -53.49953 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aac6ad7-fdba-3512-aa8a-98383a4dcb7b | -6.37661 | -54.96107 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89115c73-0f67-3109-a2c5-302bd02a401b | -7.48325 | -55.33177 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b89cb696-36b2-3052-8ace-d00ecee27e2e | -6.55189 | -55.10218 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d70d1bb-2815-354e-b9f0-3783fec82db8 | -6.38121 | -54.9619 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c1cd064-51f9-383a-949c-038d70b5d9e0 | -4.27087 | -48.19335 | 2026-08-23 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4c9260d-129f-3407-bc4a-010bda8e24e4 | -4.16639 | -42.44406 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4012423-f8a7-3aa1-9c16-a89c4de9b81a | -6.20159 | -53.52381 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b44c07b9-0fcd-320a-9273-13d31f970f8d | -7.2691 | -49.90816 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad264c86-fa73-30fa-99a3-4d6b090c1dd1 | -5.16941 | -45.05696 | 2026-08-23 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0e3bac7-55c1-3604-9995-f460662ad183 | -6.38299 | -54.9702 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35b85d50-2b8b-3416-b9b3-35b72c34ddcb | -7.72757 | -46.14325 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0182e8fb-e833-3a84-8a63-b03c544b6313 | -6.79195 | -59.80572 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a97f1559-74b6-3768-8fd2-b3337c67ada1 | -6.12381 | -57.85862 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 340fc14c-a88b-383b-b998-8bebb6e3b709 | -6.90135 | -55.70975 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d31261d-70e1-3a32-8204-e3971425981d | -6.80814 | -58.66242 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c177ac46-6ab7-3bf3-813c-4c4e3a6c4195 | -6.67077 | -58.75046 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e0a6bee8-0434-36b6-99e4-bf677c61520c | -5.94993 | -52.12414 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ea7b00a-b8c8-3f12-b911-b6ac93dc4f53 | -6.36901 | -54.94986 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a757352-29e1-34c8-89ba-9d92dd25ac16 | -6.66205 | -58.7975 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
