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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 911f7b4c-e458-3ee6-b63e-985885d0de37 | -6.7875 | -48.679901 | 2026-09-24 00:16:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c8aaded5-e3b6-31ef-8dbf-d75dbfe22a47 | -7.0911 | -52.753502 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 378d9c09-99c4-3885-bcdd-cc7174cae1cb | -4.1164 | -51.067501 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac56efd2-b53a-3473-a624-bf936dc353ed | -6.7057 | -44.1492 | 2026-09-24 00:16:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05cc78f3-42e2-3e79-9c2f-e3a07b1e8b82 | -9.2613 | -46.245998 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a92a31e-9e31-3d31-b069-a6bea3837a1a | -4.2846 | -48.6022 | 2026-09-24 00:16:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0892452-b954-3a55-8467-05618c9178f0 | -15.2412 | -43.256401 | 2026-09-24 00:16:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 0a77fdde-a06f-3fb5-92ad-ab7be72a9c8a | -11.9695 | -50.7579 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7881cd3-9575-33bf-81bd-0c5005e374a5 | -2.8167 | -46.709099 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f2ef11b-2a59-357a-a96f-259e85a9aba3 | -2.9752 | -54.141102 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b6633e-0c8f-3880-9a4e-5ee3af31aaa3 | -7.5116 | -61.446201 | 2026-09-24 00:16:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c298dd26-bae7-3ead-8061-41a6ccd2fae9 | -12.0706 | -50.749802 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 453ffa80-4e6b-352f-ac49-d7beb07e4d94 | -5.8119 | -47.764198 | 2026-09-24 00:16:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1ece7a-be6a-3273-bd30-2c47ce79f121 | -8.2991 | -48.213402 | 2026-09-24 00:16:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b301a911-3587-3b6f-baf0-fad7a6e2f087 | 1.6021 | -55.898102 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c437145-8df7-3721-af62-23cfda8b9138 | -6.6035 | -59.893299 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7b29d1-6bab-3be4-a402-5507aa8eb741 | -3.1097 | -51.037701 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 715cc838-8af8-37e9-b70a-35237ca2dfec | -6.774 | -48.6665 | 2026-09-24 00:16:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 87be4b52-a461-3358-a2e8-506b4541679b | -7.4208 | -49.821098 | 2026-09-24 00:16:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e3a40e-3819-35cb-a92c-059f190f299c | -6.5692 | -51.476898 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78afb1df-dfcc-329f-8758-ae6842ea5940 | -5.7673 | -45.082901 | 2026-09-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72d0aaae-80f3-3aed-a33b-50e1a7b9a599 | -8.2447 | -48.201 | 2026-09-24 00:16:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0e02cab-acef-3ebe-b71b-5c100d010c2f | -9.5766 | -45.235901 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f19a303d-f888-352f-ae3e-a854e8fe5116 | -13.8514 | -48.577099 | 2026-09-24 00:16:00 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8d28b802-2c62-3b74-b833-e3baf2fcaa31 | -3.9174 | -59.650002 | 2026-09-24 00:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f16dbaa8-17ff-3083-8a42-e392b32f2e6c | 2.134 | -50.721401 | 2026-09-24 00:16:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 79226fab-91f3-35e0-a8e7-5a54a5cc9756 | -3.1584 | -54.591801 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf1ca75a-4114-3fd3-a5a5-4ffe9eece854 | -5.7835 | -50.192902 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3204ef61-5be6-3adf-a8d8-32bf6d10b07e | -9.2399 | -47.379501 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0ed25aa-095f-335d-9088-cc93bfbc2365 | -4.4254 | -55.0634 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9786cf65-5dbf-310b-ace2-8536bec01c59 | -1.8348 | -55.709301 | 2026-09-24 00:16:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1708fe4-8e17-30cd-95cf-d4c63ca4e515 | -3.9597 | -59.329899 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4468c5b1-64c1-3223-92f2-55385d4f67a3 | -7.4224 | -49.828201 | 2026-09-24 00:16:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49a79f42-7c3d-3ce9-bc6d-8e273e09ea41 | -5.5612 | -42.737801 | 2026-09-24 00:16:00 | METOP-B | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 108f7432-c340-3953-a555-2fd32c946658 | -9.0473 | -48.1465 | 2026-09-24 00:16:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2edbc072-3b7f-3a56-a4a2-e0113111e787 | -6.3096 | -52.6637 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76e834a6-2eb0-306e-b325-3f634a9cf6b5 | -4.4474 | -55.023602 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfe05f62-81da-3219-a34d-d4ae46596271 | -9.8381 | -48.487499 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26290432-f62d-3505-bf1d-acff706b5822 | -4.5381 | -54.969002 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb6c5f25-ccfe-33d3-9ddb-c4014420c805 | -12.0773 | -50.733601 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de856bac-cfd7-3f73-b9e8-efc59a479bfa | -8.1511 | -49.541599 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a48fa260-69e4-315e-b649-c1be33e2741f | -3.8571 | -58.860401 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1d99cac-3cfa-32a4-8f22-3dde7b7317e7 | -4.1109 | -54.480701 | 2026-09-24 00:16:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d6d2a4-7c82-3549-ac3f-659ad48a187f | -4.2921 | -49.127499 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8284877a-fbd9-3a65-be5c-14333d09c88e | -8.4527 | -48.698898 | 2026-09-24 00:16:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab6d56a-c5ef-3ee8-94ec-6190e92b294b | -1.9204 | -58.246201 | 2026-09-24 00:16:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d86bc0e0-f770-3ddb-90a2-c98ebcbff91e | -10.1011 | -46.001099 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a79305de-e377-34d7-a199-bc4da267ba85 | -8.2846 | -54.7831 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c30308a7-23eb-36c4-a07c-a837e5744ec2 | -3.0055 | -51.5327 | 2026-09-24 00:16:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb0274be-20c0-3a85-94c4-5da3fea1df39 | -2.5734 | -54.736599 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec08f6e8-8323-3f05-8535-7fe0eb7fe687 | -3.1716 | -48.020302 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8c4236c-d6bd-3a28-a8d7-e9f5d7cbef73 | -6.9108 | -47.6562 | 2026-09-24 00:16:00 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0806921f-38e7-3a57-8c86-f5e86ef27524 | -3.7138 | -49.0331 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f526e9-65f6-3d3b-86a9-53322d7a42a3 | -4.445 | -55.059101 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9fbb02-6f89-37d5-b7f6-522525622c38 | -11.99 | -52.457699 | 2026-09-24 00:16:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccb9b8e7-22ff-3dbd-89a3-a21c1ed1a3ea | -8.7237 | -47.5993 | 2026-09-24 00:16:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93d07ac8-8213-3230-bf08-1446fb85cf22 | -11.486 | -42.3111 | 2026-09-24 00:16:00 | METOP-B | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 622a953b-a410-33c1-a368-821c79f46e13 | -12.1537 | -50.7533 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edc1e600-32e2-374d-bf9a-a000f96c9784 | -3.5457 | -43.476398 | 2026-09-24 00:16:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd96c4c8-d887-380b-9186-5442fd6f584d | -5.7215 | -49.830799 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4386988-203a-3fd1-88ff-8ab71ceb6572 | -3.8052 | -58.8568 | 2026-09-24 00:16:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab1898a-50bb-3487-898f-d295aff397d9 | -6.426 | -48.4547 | 2026-09-24 00:16:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b0f8b8c2-eebc-30a3-a5c7-8ade3e5b7673 | -11.4901 | -42.327202 | 2026-09-24 00:16:00 | METOP-B | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f62d964e-d88a-3c17-81b2-645662788416 | -3.0014 | -54.166401 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459af610-0937-3e3f-b35c-04f75ce145bb | -11.9597 | -50.760201 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 497273a8-9f71-3571-ae3f-b854e620f3ba | -9.5905 | -47.775501 | 2026-09-24 00:16:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd7c9eb2-ccf7-3b29-bcf2-3978fbaa2efe | -4.8898 | -55.9585 | 2026-09-24 00:16:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ede675c3-c5e7-3c38-a98a-21481b3496ec | -7.1854 | -47.4627 | 2026-09-24 00:16:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38fc160f-a8de-3e08-a542-19078b8fbfe7 | -12.4192 | -46.9347 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6ff2c0d-9794-3d00-8046-96d74c27937d | -11.9566 | -50.746101 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3fba5b-51e4-3784-ab7b-711dadf1bf6d | -12.1177 | -47.367699 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a3d7c6f-1f8a-3e15-8882-22fbe085e205 | -5.5663 | -42.716599 | 2026-09-24 00:16:00 | METOP-B | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a08ddba-a9dd-3ac7-a6bc-0a07ab33ef3b | -8.2939 | -49.8969 | 2026-09-24 00:16:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7fc556-38c5-3c89-9131-fda7f250fe0b | -8.492 | -57.595798 | 2026-09-24 00:16:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50a1f84-c100-33d4-a7fa-9be0114b345c | -12.0788 | -50.740601 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8e7f88b-52ff-3613-ab5f-b299e2adba54 | -2.7045 | -57.487 | 2026-09-24 00:16:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af04d449-a268-32e6-8c7d-809d902303f8 | -6.5723 | -51.490601 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee9cebb-f8d0-305f-ab7a-769452b16e73 | -12.0804 | -50.747601 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 308eb25e-a294-3a98-92c8-27d26d44e255 | -10.9294 | -43.841202 | 2026-09-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 831468cd-a4e5-3046-ae18-49704aa032e4 | -9.3496 | -50.096802 | 2026-09-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cec079b-36e1-324e-bbf7-346e799d7c1a | -3.1722 | -51.358398 | 2026-09-24 00:16:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d31530d7-6673-3484-b001-6242d8609d5b | -1.2126 | -54.5452 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157801e6-a679-3bfb-818b-b76a85009b92 | -12.4133 | -46.953602 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccddb739-d82f-3785-8c51-add7a6cbf756 | -8.8976 | -46.8018 | 2026-09-24 00:16:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0e48db-a673-33b6-aebc-09e22d36a755 | -10.0812 | -46.047401 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdae1ba8-aae9-3e32-b744-b7674cfe7c08 | -4.7171 | -55.966099 | 2026-09-24 00:16:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00076e12-97c5-34f6-8c83-a153cfb6de2d | -2.5938 | -47.345798 | 2026-09-24 00:16:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57fca03f-16e5-358a-bdf8-4b345787e89b | -6.7119 | -44.132301 | 2026-09-24 00:16:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bacaf56-143d-3236-a881-453d00b86300 | -1.6262 | -54.872398 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3c68ee5-2fa5-3088-9738-6872ca032408 | -2.3787 | -48.5131 | 2026-09-24 00:16:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca0942e-bb09-3450-854c-058e916c462e | -12.1552 | -50.7603 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 466c74c8-5f4b-31fb-b6d0-8d57582c2cc3 | -3.004 | -51.525902 | 2026-09-24 00:16:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01e413f1-d178-3f09-8d07-140aff846440 | -11.2446 | -51.343899 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf7d847c-845e-3c97-810a-28760659df77 | -3.5579 | -53.479698 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c533516a-56df-36c9-8c7b-669c98bf0d56 | -14.9621 | -47.521198 | 2026-09-24 00:16:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5260b635-3610-342f-a2dc-6461c9a4bcf9 | -11.2642 | -51.3395 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e3ac2d2-d9de-3ebc-9ebe-16e41f344745 | -8.2085 | -54.715099 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6577da18-e1aa-3b3f-8c8b-25b4cd762dca | -6.7777 | -48.682201 | 2026-09-24 00:16:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2764fae8-f9e1-34f1-861d-587b24fc67f2 | -8.2768 | -54.747101 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ad7d18-ada1-30c5-a659-c06dc39e865b | -10.9829 | -54.082802 | 2026-09-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
