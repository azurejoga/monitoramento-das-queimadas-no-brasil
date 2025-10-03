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
| 214af038-fe92-3d3f-a1cc-52c9e7399ab9 | -6.2596 | -45.341 | 2025-10-03 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 07ea2858-b576-33c0-b24e-ae55a1b1ea57 | -9.9175 | -43.7682 | 2025-10-03 00:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| d6215b9d-d526-3e48-ac25-85f8cc6fbae1 | -6.0418 | -44.6076 | 2025-10-03 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 5fa21783-5060-38c1-ab2b-1208b86c27af | -8.6139 | -54.9558 | 2025-10-03 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6b32043e-339a-3053-a073-b06c1b8de4cc | 1.5103 | -55.8259 | 2025-10-03 00:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 6cfaee5f-9fea-348d-b2fa-4bd632b7ff2a | -12.6327 | -46.9471 | 2025-10-03 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fab3fe94-96f4-3f6c-9979-26040fd7c849 | -15.1839 | -43.625 | 2025-10-03 00:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 78.3 |
| a133d3e1-fd1c-33f0-be1c-2d0928c7f0a1 | -6.5201 | -49.5753 | 2025-10-03 00:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 9f9ff042-0cef-37b5-bf92-50cef4408f29 | -14.905 | -48.3003 | 2025-10-03 00:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 440ccc58-ebe9-3814-a866-465e32cf18f4 | -6.2594 | -45.3636 | 2025-10-03 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 98604bb2-baac-3289-b643-8d9461be93ed | -4.6504 | -45.8077 | 2025-10-03 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 7e5c6fd8-8b38-339b-b7cc-7143717e02b6 | -12.6135 | -46.9499 | 2025-10-03 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 07cd030e-5fe4-3c64-9f1f-8a5297682b7b | -4.6692 | -45.7842 | 2025-10-03 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 423.7 |
| 7b940ada-c59b-3190-9ac9-043e6712ac7c | -3.9331 | -47.5655 | 2025-10-03 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 1bfa13b3-4cc2-330d-b77e-e517349d43c4 | -13.7769 | -47.5392 | 2025-10-03 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| c12ab68b-8edb-3581-a7c0-86ad0e65a73f | -5.8657 | -43.3981 | 2025-10-03 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 2da05ecc-7a6d-3d2e-a9a2-3d721443034d | -5.3849 | -47.2271 | 2025-10-03 00:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 95.7 |
| efd105db-6c91-3ca0-aec2-ac6de52c7aeb | -5.6363 | -43.9027 | 2025-10-03 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 306.1 |
| c9f63cf9-5968-3b4b-9900-576b715fa9f5 | -5.6176 | -43.9041 | 2025-10-03 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 54bd982c-c9b2-36fd-8156-52afddee5cf7 | -10.8608 | -46.6715 | 2025-10-03 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 5257d61d-0cf8-378b-9e3d-48a18544813a | -12.6323 | -46.9697 | 2025-10-03 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 00c28684-f2f1-3637-8b6f-ecbf1b72a4ed | -6.2221 | -45.3439 | 2025-10-03 00:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fc108168-8b1c-3a3f-8649-b21dcbdbac65 | -17.8614 | -57.623 | 2025-10-03 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 2234d3f7-37e4-30b0-9273-80c40a7d7f44 | -7.7125 | -46.2082 | 2025-10-03 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 35925624-21f8-3a84-b0b6-9f159befe4b7 | -6.0603 | -44.629 | 2025-10-03 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| a83a7102-d0f9-3b93-82be-7e7455f7f741 | -4.5712 | -46.5022 | 2025-10-03 00:10:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 23d55efb-b34e-337e-a474-c64104bd0ea3 | -4.6505 | -45.7853 | 2025-10-03 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 292.3 |
| 454cf339-27dc-3072-a3af-3d055203fe0b | -3.9331 | -47.5655 | 2025-10-03 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 56e78551-1e77-3530-9880-b0330111de02 | -6.0603 | -44.629 | 2025-10-03 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 2074cdab-597c-3c04-ba35-58724881adb7 | -4.6878 | -45.7832 | 2025-10-03 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 54877436-7e34-30a7-bc4e-e4e9062cefc3 | -7.7746 | -42.5865 | 2025-10-03 00:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 220.1 |
| a6c0a500-eb54-3b9d-90e8-81eb8720a242 | -13.1345 | -47.882 | 2025-10-03 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 824e0f2d-085d-34eb-ad22-ff7a5d52eefd | -5.6176 | -43.9041 | 2025-10-03 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 720cebc3-42ac-3593-b5b5-00aa91c2c896 | -5.3663 | -47.2283 | 2025-10-03 00:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ddf279e1-06d0-3a9a-aa26-2cb2872f339a | -14.0323 | -53.8895 | 2025-10-03 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 6eb217d0-03e3-387e-a784-e0e9de3929a2 | -11.1444 | -43.3845 | 2025-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 126.7 |
| 1d7dd57f-52ee-397d-986d-ba09236aef09 | -7.7743 | -42.6103 | 2025-10-03 00:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 817421a2-3995-3625-8050-4c71fa565923 | -9.9182 | -43.7212 | 2025-10-03 00:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 48dbc9d7-ce4b-3144-bf92-34075e1681f2 | -14.9403 | -47.5307 | 2025-10-03 00:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 9e88efdc-4d75-339e-a3e1-206191f727f2 | -18.6837 | -47.823 | 2025-10-03 00:20:00 | GOES-19 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a19cee9e-c885-3263-86e5-c28c3d88ed35 | -5.3849 | -47.2271 | 2025-10-03 00:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| bc098804-5320-3cb4-9274-22118a57f18d | -14.9132 | -46.9684 | 2025-10-03 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7315e0a6-9276-3809-b536-304fc218a032 | -10.1759 | -45.4906 | 2025-10-03 00:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 09d2c9dc-fb16-3b88-9694-50cd3d84f883 | -12.6323 | -46.9697 | 2025-10-03 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 177.2 |
| ed85ce1f-5182-3553-b850-77df4471dcea | -6.0605 | -44.6061 | 2025-10-03 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 4c2a5104-6e07-3973-9d6f-4ccd89721583 | -13.1349 | -47.8597 | 2025-10-03 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6b21b483-b6f9-3f73-b021-1947142db10b | -14.9342 | -46.8965 | 2025-10-03 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 70db7cc7-e0b3-34e4-88ef-84f0ee3e6f21 | -14.905 | -48.3003 | 2025-10-03 00:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b0a033b3-8c34-34df-a2f9-a1d344e49dff | -12.6327 | -46.9471 | 2025-10-03 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| cb96247f-2bf9-3403-9145-04500e0b9399 | -4.5712 | -46.5022 | 2025-10-03 00:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6a574482-433f-398b-992f-940cd63341c5 | -14.9538 | -46.8931 | 2025-10-03 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f2c9a14b-ccfd-3dcd-962f-c029ca013e47 | -14.9408 | -47.508 | 2025-10-03 00:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9839af16-934b-3701-b0b8-902c813cbaa8 | -6.0418 | -44.6076 | 2025-10-03 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| b2f9c91e-0b88-3087-b27e-02759d95c1ab | -10.2762 | -36.3327 | 2025-10-03 00:20:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 530ef75d-bf9d-38c8-8a7f-250939615431 | -7.2578 | -48.4699 | 2025-10-03 00:20:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 502d6a46-acb4-39a8-a33e-f81ef6f0fbb7 | -6.2408 | -45.3424 | 2025-10-03 00:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 816570f6-087e-3174-8259-91d51d67133d | -5.6174 | -43.9272 | 2025-10-03 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2499312f-d494-3f62-878f-d401d3e0d3c6 | -11.144 | -43.4082 | 2025-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 240.4 |
| 97189b6b-4e12-361f-b9bd-1a41ab309d1f | -13.7666 | -48.0777 | 2025-10-03 00:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 412fc846-a315-3638-bbe3-c165f50f8518 | -9.9365 | -43.7657 | 2025-10-03 00:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| c536e98b-c439-3766-88a0-8d990c9b9474 | -14.8937 | -46.9718 | 2025-10-03 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4b8e233e-51b9-3a97-8f6f-6dc4c529e7c7 | -10.2569 | -36.3362 | 2025-10-03 00:20:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 137.0 |
| b5aa1e31-8169-3ba6-8d28-6da638740854 | -7.9137 | -43.5369 | 2025-10-03 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 46243f08-2673-385b-8122-c712dbaf2b5a | -8.6139 | -54.9558 | 2025-10-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d53ad1e7-fbc4-3c70-a84f-b85330f37eb6 | -4.6692 | -45.7842 | 2025-10-03 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 410.7 |
| af256807-010b-3db9-b5d5-8f870fc253c3 | -4.6504 | -45.8077 | 2025-10-03 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 234.1 |
| 12ca3d38-47f0-3fce-b58b-892fdda2c031 | -18.4118 | -50.7824 | 2025-10-03 00:20:00 | GOES-19 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 78e345d5-dcdd-3f12-82e9-40edc72e8595 | -7.7557 | -42.5885 | 2025-10-03 00:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 133.9 |
| e5d89f99-1331-3c65-9c65-1bfbdf3f3c65 | -13.7769 | -47.5392 | 2025-10-03 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 55209838-b591-3926-b756-a72d12a879f4 | -6.0416 | -44.6304 | 2025-10-03 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 8fb8e11a-166c-3ddc-9f12-d37fd54169fc | -10.2564 | -36.3633 | 2025-10-03 00:20:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 105.9 |
| a45a23b6-3151-3f4e-a0b3-ebd31da257b8 | -7.7938 | -42.5607 | 2025-10-03 00:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| d3a51d6d-3356-3f14-9ac3-9c8578b241d8 | -5.8469 | -43.3995 | 2025-10-03 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 698edf2b-c442-3b98-8e95-cc42c5da3d57 | -5.3665 | -47.2063 | 2025-10-03 00:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| eea80d57-8004-3120-aac7-48e40ab1c781 | -4.669 | -45.8066 | 2025-10-03 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 441.6 |
| fe609164-61ea-36e3-9ce4-d85e3540f175 | -9.9369 | -43.7422 | 2025-10-03 00:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 6b175413-f642-3497-a4a4-68c27e1164cb | -7.8951 | -43.5155 | 2025-10-03 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e1158690-83c3-3067-9c76-fb6c46771d53 | -7.7749 | -42.5628 | 2025-10-03 00:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| d1fa0d4d-0001-3f08-9b46-81dff1bc3c64 | -6.2406 | -45.365 | 2025-10-03 00:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 178.5 |
| d7d10d08-6b8b-390d-ad40-cc2189ff3cd9 | -5.6363 | -43.9027 | 2025-10-03 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 292.7 |
| 2f86e860-6f68-3e1d-9422-be2a7162050a | -4.6877 | -45.8056 | 2025-10-03 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 8e9e9acd-83d8-3ff8-a54c-5fcb7e9164b9 | 1.5103 | -55.8259 | 2025-10-03 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 4939cba0-4dc3-3507-af27-bc4351a0fc8c | -7.914 | -43.5135 | 2025-10-03 00:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 97b6a882-6bc6-34ff-af5e-192bd07ebc03 | -7.8948 | -43.5389 | 2025-10-03 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| a17d734a-655c-3b50-a043-24dad7c42428 | -7.756 | -42.5648 | 2025-10-03 00:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| b3538115-4449-39cd-a457-1403150a0629 | -8.6324 | -54.9747 | 2025-10-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9eea38b4-5c4d-3570-9547-12a1b748bb43 | -5.8657 | -43.3981 | 2025-10-03 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 163dde62-181c-370f-854e-1c93e3296e9c | -8.6138 | -54.976 | 2025-10-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 889ac840-af45-3fa6-a626-a6a1d8260efc | -12.6131 | -46.9725 | 2025-10-03 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 7c9e678d-bdd8-3fff-a487-31df52394cfb | -3.8384 | -41.5729 | 2025-10-03 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| 3a754152-6a46-3b5c-ab0c-e0145400001e | -9.9175 | -43.7682 | 2025-10-03 00:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| f85bb3e4-b36a-3b17-b676-f4b91fc88ffa | -5.6361 | -43.9258 | 2025-10-03 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 66778e9f-731d-37c8-af23-8ed5bbe3037a | -17.5956 | -46.6648 | 2025-10-03 00:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 26f47799-3579-3645-8050-8be16603dbd9 | -11.1631 | -43.4054 | 2025-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 72.9 |
| cd6a4636-816e-3f4b-a083-dd94aa451c3c | -5.8655 | -43.4214 | 2025-10-03 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0f120887-a8d0-37e3-a325-3c14c472a31a | -5.3851 | -47.2052 | 2025-10-03 00:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 8105e1d1-8001-3812-a779-1961f04b3e01 | -12.7669 | -44.9137 | 2025-10-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d7b2ab75-9a5d-3247-95ef-c888f838250c | -4.669 | -45.8066 | 2025-10-03 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 429.6 |
| a94f85a5-4640-377d-b30e-04dcc40cdc5c | -14.7531 | -48.1238 | 2025-10-03 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b2a99208-4946-307d-ba5e-c9175d03690d | -9.9175 | -43.7682 | 2025-10-03 00:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |


[Clique aqui para ver as próximas entradas](README3.md)
