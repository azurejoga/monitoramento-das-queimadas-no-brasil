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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5eb66930-45a8-3c8f-9d75-87d1621316cf | -4.4108 | -55.4884 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74bbc835-06ac-36d0-8b6a-ccc91d1ec297 | -6.1351 | -59.934101 | 2026-09-19 00:19:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48303eef-298e-3b4e-885c-d768ae1b7aaa | -6.5772 | -44.1413 | 2026-09-19 00:19:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc43e089-979f-3105-9cf6-f66bd6aff2c7 | -9.9508 | -46.536598 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee4b298b-b0ed-3724-9b64-d1a5f3064e9a | -5.9103 | -52.113098 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1891317-7b22-39f6-9cb8-78c5801aff68 | -12.8333 | -44.379299 | 2026-09-19 00:19:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 291ddb61-6309-3de3-8d45-9cbd599acf25 | -3.727 | -54.6357 | 2026-09-19 00:19:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2efafab2-f060-384d-8d9a-90ebbcee9bb8 | -5.8907 | -53.5401 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e688bdff-506e-32be-8777-0a5da8546c42 | -3.4256 | -50.6605 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a59c5d0-9f16-3481-ac2f-cdc0f3e4a5b6 | -10.9712 | -49.7477 | 2026-09-19 00:19:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e817637f-7321-37cb-905b-8273d975ef69 | -3.4915 | -49.509102 | 2026-09-19 00:19:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eaefd4d-aac5-34b3-b70c-1a3476052a1e | -11.4578 | -47.662498 | 2026-09-19 00:19:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a6f4254-bca7-335e-9e12-eb70458acebd | -4.061 | -56.227699 | 2026-09-19 00:19:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe373fa-8c10-34b3-834c-d7834ecda894 | -0.5168 | -49.151299 | 2026-09-19 00:19:00 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd7978c-42bd-3763-aa32-f70dd5dac0a5 | -1.315 | -55.813099 | 2026-09-19 00:19:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee96f5d0-43b6-3509-ad15-ee69aef053aa | -21.033001 | -48.2304 | 2026-09-19 00:19:00 | METOP-B | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 843c82ab-65c3-31bb-9944-0e83e7bc7210 | -6.9974 | -49.736301 | 2026-09-19 00:19:00 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df3478d9-cac7-34f5-a779-fae6c99210b0 | -10.6024 | -46.111801 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8eaae730-3e15-336f-b790-c05918f24943 | -11.2976 | -46.7701 | 2026-09-19 00:19:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3515f7c-3bba-3add-9769-d46100f3c5d3 | -9.9964 | -50.266701 | 2026-09-19 00:19:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb02e13b-e23b-3225-9593-8bad56911e45 | -6.7685 | -55.843498 | 2026-09-19 00:19:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa1f897-b753-3cc2-9512-742a49162fc4 | -11.9184 | -50.104599 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8d72206-e1ce-3ce8-818f-39f7df7f9724 | -6.9857 | -42.180199 | 2026-09-19 00:19:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 273aa755-bb27-3446-91c2-623a267ec288 | -10.83 | -50.8997 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9f89532-a758-3d37-a9ab-5a01021e1208 | -9.0374 | -48.744701 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 88e61f21-1f1c-35b0-87c8-6a13741f2d69 | -1.5874 | -54.417099 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd0ac487-73b6-34e7-9656-469581d41fb2 | -12.5404 | -47.086201 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a03f095-3769-3a41-b71d-0dd0178baa96 | -10.6678 | -50.6367 | 2026-09-19 00:19:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e59f1c57-cdb4-3c0d-a9bb-339624f29189 | -6.9992 | -49.7439 | 2026-09-19 00:19:00 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a866966d-24c6-3939-b652-9182f9727826 | -10.7155 | -60.6936 | 2026-09-19 00:19:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f136b507-f374-345b-80d1-c4beff0a8d02 | -1.4952 | -49.471699 | 2026-09-19 00:19:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea47f0c8-82d0-3fdd-8f19-45de5b66a67f | -7.6908 | -46.1045 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2b8ddb-2766-3ed0-9fc5-1a68b2e8e139 | -5.7311 | -52.2323 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b599c33-4900-3d5d-aa6c-7d7ab9025f19 | -14.6757 | -46.677101 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 489b8470-1efc-3ebd-a3a9-d7bd53b27535 | -3.1553 | -53.923698 | 2026-09-19 00:19:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 265a0556-fae1-3bfa-9093-53323d1623f0 | -6.4749 | -43.8069 | 2026-09-19 00:19:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69e972a4-eae3-3a84-8f17-5c00c30b4814 | -14.6617 | -46.6619 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c93dc79-fca4-3093-8c9d-30e1a56ee6d9 | -6.9383 | -55.022598 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30fc69c1-8ffc-3256-9b1a-97424b00a43e | -9.9069 | -46.568901 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d64698e3-e617-30b1-940a-ba7d6ae67719 | -12.3506 | -50.697701 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce3509e-468e-37ea-a0f7-9bef9ce5409f | -13.0005 | -46.935101 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc06b547-8c04-3a6b-be83-8b816059f28e | -7.7721 | -44.864101 | 2026-09-19 00:19:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc3e60f1-4d6e-35bb-a4dc-2a134ca789d0 | -6.428 | -55.552101 | 2026-09-19 00:19:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7b3a804-3ad3-3fdb-8f12-1ae4e803164a | -6.6663 | -50.901699 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad051306-5193-3834-9482-6c9891207186 | -11.9428 | -50.121201 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59a71ab0-7b7a-3026-8efd-4fd34ae119f7 | -3.7235 | -49.040798 | 2026-09-19 00:19:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 396daba4-ee1b-37fc-b133-96af5da15026 | -10.1327 | -49.151699 | 2026-09-19 00:19:00 | METOP-B | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfd3ba14-3652-3a31-998d-d533345586ba | -9.6544 | -49.135601 | 2026-09-19 00:19:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae032de7-3ec3-3a7b-854c-d28616eac038 | -11.9751 | -52.4482 | 2026-09-19 00:19:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf3d3f8e-5b3e-3028-943e-4e1970d3763f | -12.5008 | -50.035999 | 2026-09-19 00:19:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97bb8da8-ff89-3a7b-b9f4-93a5e1ffee28 | -6.7026 | -59.442501 | 2026-09-19 00:19:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28b1209a-5c72-3eb4-9844-517edbf6e363 | -11.8503 | -50.0312 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1a27237-4271-379f-a7aa-f039b511c690 | -11.3233 | -47.355701 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a515ce3d-2aae-3189-ba4c-b1982fcc8b0f | -3.5184 | -50.795799 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43fe33d2-6f2d-3039-9160-3439033be44d | -9.0454 | -48.734299 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 513da78c-08fa-30d5-83b1-2fd7dc635fbc | -7.5954 | -55.684101 | 2026-09-19 00:19:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ead74f55-1c98-314f-96d5-cfac879e511f | -10.7061 | -50.259102 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f55ccd5-6469-375f-aeb9-192b263ae7ee | -3.3543 | -50.438301 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7dcc71c-bd73-3605-8389-34b9ec4d1cd6 | -11.9086 | -50.1068 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa9a2ad9-17ea-34b5-8c87-e2a3cbf76cdd | -3.8125 | -50.729599 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0e8d41b-5368-3fe4-8773-4b801ff78359 | -10.8642 | -54.1026 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 119176d5-1d04-38a1-8023-a9aff76ffffa | -1.5956 | -55.550499 | 2026-09-19 00:19:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723b3d67-0989-3fea-8415-6aa8824d3ca6 | -11.2904 | -47.260201 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 331666ef-4654-3c04-916f-84039770f06e | -10.8674 | -53.974201 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76841bea-0082-3749-a1f1-5c2aa9cc25bc | -6.0253 | -51.7556 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d863bf53-ce35-34aa-b1a1-72f8e88d1c4e | -11.3247 | -47.667702 | 2026-09-19 00:19:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c931bdf6-fe20-333a-be7e-5306eddec2de | -6.6581 | -50.910999 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2dafe7-3178-3ca6-bf5c-1ec3699033dc | -8.61 | -54.591599 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fea44d3f-0ec2-3c0d-96c6-fd74d3f4410c | -13.5981 | -46.927502 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d54516b-ad4d-37a2-913b-14a3cfe80b87 | -15.6331 | -52.713299 | 2026-09-19 00:19:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a35e1493-9628-360d-ae43-9c19a71465cf | -5.8648 | -46.699501 | 2026-09-19 00:19:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c99bb06d-37de-3023-8dfc-9ed6e79ddcca | -9.9441 | -53.974499 | 2026-09-19 00:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a22861b1-3a2c-358d-ba57-d01cff347785 | -3.515 | -50.781101 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e78fe4-412c-3374-958d-7ea60895327f | -5.5175 | -43.796398 | 2026-09-19 00:19:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8d06ac8-32f8-3a3e-b0e1-192ca0e55b23 | -3.8142 | -50.737 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc4f627-91d3-3034-be9a-274d720d2995 | -10.8705 | -54.084099 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88a9303f-5229-3326-9874-bbce16e88dc0 | -5.8835 | -52.039902 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0f069dd-3e11-3e47-b7c5-2efbca39ad43 | -14.1767 | -47.8494 | 2026-09-19 00:19:00 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b6ba9b62-9486-3473-bebf-f37cae13bc84 | -2.2919 | -47.878601 | 2026-09-19 00:19:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebaf1fb9-59db-3538-865e-3268a1f257a1 | -4.1405 | -48.217098 | 2026-09-19 00:19:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5da10b0a-eeca-3a81-a675-a7e724803ace | -0.2645 | -48.4049 | 2026-09-19 00:19:00 | METOP-B | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5768208-d5dc-3b55-b140-a3fde7307ea8 | -13.0102 | -46.932701 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bdf25bc-c080-35b4-aa2f-92f737e86858 | -5.7643 | -57.446499 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d76cf4d-16ed-3ba4-82a8-59d6beef5db4 | -12.3463 | -48.1931 | 2026-09-19 00:19:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65458df4-49c0-32dc-ad8d-a83a3f9fadfc | -10.4447 | -48.671902 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a4fe291-0621-3e3b-adde-61f6c81ee4a6 | -12.5771 | -49.102001 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5c4c0e4-3ce3-34ab-87fd-7ce82d411d70 | -7.8604 | -46.424801 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a75496b8-d575-3d57-8524-2268bcd28147 | -5.7522 | -57.437801 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d87f5ed3-e1b3-3e44-bbe7-bf932060a005 | -5.8571 | -52.0602 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd3fb7e-e00c-326a-97b2-ef6ea79ed0d5 | -7.4032 | -49.841301 | 2026-09-19 00:19:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8358bd67-7fc3-397e-a60f-c9a2801c2b56 | -11.3484 | -44.142899 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e505998-2a66-3f6a-90d8-93f460a31ec1 | -4.3865 | -43.613201 | 2026-09-19 00:19:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f764bfdf-ce16-362c-b1c6-e90c88f4da32 | -10.2094 | -54.253201 | 2026-09-19 00:19:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e621460-7192-3eeb-b86b-320bda8ffcc4 | -6.3714 | -58.270199 | 2026-09-19 00:19:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aca95d31-a465-30d1-a102-1efa7f89b8bb | -11.0621 | -48.2649 | 2026-09-19 00:19:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec98a03a-a71b-3ff3-8dc8-e22fb72f0e1d | -10.7045 | -50.251999 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1051db2-23fe-32c8-99fd-02cd161cf224 | -6.976 | -42.182598 | 2026-09-19 00:19:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a8810666-de95-3bf2-b5c2-270598b549d0 | -10.8888 | -53.978001 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd763b8-31ef-3a82-a279-a77666f0e549 | -3.3323 | -50.117199 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea7bbe53-bcc1-388d-97b0-17528783552e | -12.1171 | -47.000801 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
