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
| deb817c0-b1ed-3da4-89c0-6a251e17efab | -6.9158 | -43.5185 | 2024-12-12 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 409.5 |
| fcc452b4-f7a9-3780-a221-17b5ebbe145c | -6.9346 | -43.5168 | 2024-12-12 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 286.3 |
| e222c9c7-ee51-34ee-b29e-62b62c808fd5 | -5.1648 | -44.3727 | 2024-12-12 00:00:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f5e0468a-a025-3e3e-8060-518d351cfbe1 | -3.2316 | -46.8936 | 2024-12-12 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 8b620811-11ee-3803-b174-63005eb38dd1 | -15.0867 | -59.6288 | 2024-12-12 00:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 73314056-4514-34c8-a359-bd7a596b70ca | -6.9344 | -43.5401 | 2024-12-12 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 52a9248f-147f-304f-a8f7-6ad8b15ba4e4 | -6.9156 | -43.5418 | 2024-12-12 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 6d203190-2fd5-3fbe-8cf4-bee264b4174d | -11.1959 | -53.8348 | 2024-12-12 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 1672efb5-919f-3a13-aeef-f223cbe2eb95 | -3.2503 | -46.8709 | 2024-12-12 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f0d2601b-2eb9-3fdf-b548-c38232d185e1 | -3.2502 | -46.8929 | 2024-12-12 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e9abd655-41f7-323a-8dd6-12de5c58c476 | -11.2148 | -53.833 | 2024-12-12 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| befca9c4-a87a-3812-a293-b7f83c9995d3 | -15.0865 | -59.6487 | 2024-12-12 00:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 354d6907-2b28-3ac6-9916-e36532625327 | -14.7655 | -52.6446 | 2024-12-12 00:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 67054247-c4dc-3c0c-9332-b855c1781db5 | -6.9161 | -43.4952 | 2024-12-12 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| f1f2a842-f647-3180-9b58-72cd43a652f3 | -2.0862 | -52.2834 | 2024-12-12 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b6ccfd2c-15fa-3837-9ddd-bd11c0ce688d | -14.7465 | -52.6259 | 2024-12-12 00:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7a58ba9d-d9be-3eb5-929f-8f4fcc69cc63 | -14.7461 | -52.6471 | 2024-12-12 00:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 165.7 |
| bd970786-6bfc-3f8d-9238-8c1da452ee23 | -14.7457 | -52.6683 | 2024-12-12 00:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 87b46054-0fe0-390e-afbc-6f03cb4d0160 | -6.93 | -43.56 | 2024-12-12 00:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c682001-cce4-3e67-9f95-5c2500a646f3 | -6.92 | -43.52 | 2024-12-12 00:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d337bc0d-1908-3631-86a4-fcf8e91f4dc6 | -6.9 | -43.51 | 2024-12-12 00:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c236c72e-09e4-357d-9acd-e715fe58fbc5 | -3.2503 | -46.8709 | 2024-12-12 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 52d123e9-d456-361c-95ce-8dc251f60640 | -3.2316 | -46.8936 | 2024-12-12 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f65e7ca3-cdbb-3dfc-8851-cf7de003de56 | -6.9158 | -43.5185 | 2024-12-12 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 352.3 |
| aa33ab98-95ca-3528-8454-c9afa8cba64a | -11.2148 | -53.833 | 2024-12-12 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 6d87145a-08ca-32bb-8e48-02456f1d0af1 | -15.9846 | -56.2857 | 2024-12-12 00:10:00 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 434c0b40-e1aa-3c05-9f02-96944cbf7efd | -14.7655 | -52.6446 | 2024-12-12 00:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5b5f797b-bd83-38cb-86b7-6015e8c280db | -15.0867 | -59.6288 | 2024-12-12 00:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 75d43df7-7e34-3512-ac85-5ea315d1839d | -14.7651 | -52.6658 | 2024-12-12 00:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 041c9ba8-ccf0-3c91-8bb0-0630a98db148 | -3.2502 | -46.8929 | 2024-12-12 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 1215d321-7bee-3bbb-b336-9011d11d206d | -6.9156 | -43.5418 | 2024-12-12 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| db49451c-3230-3159-99dd-0864d5a4a9d5 | -6.5631 | -51.1126 | 2024-12-12 00:10:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f71b8314-2739-3e37-84b0-994f958e1343 | -6.9161 | -43.4952 | 2024-12-12 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 39aebc94-a6ad-3d98-bf10-1369a38c012e | -3.2317 | -46.8716 | 2024-12-12 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 06938c75-d4a3-3af7-9ba4-203dc9e85a7d | -1.6221 | -54.6744 | 2024-12-12 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 902ae3b5-33b1-3813-91eb-0d6b685f913c | -5.9371 | -48.0437 | 2024-12-12 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 7af277bb-5afd-35f9-979f-5b38904344b1 | -14.7457 | -52.6683 | 2024-12-12 00:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0556a4c6-e00a-3893-af6d-9f922633e63b | -5.1648 | -44.3727 | 2024-12-12 00:10:00 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 98edaaf4-c700-3448-b1fc-205db6841a03 | -11.1959 | -53.8348 | 2024-12-12 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e02679fd-a3f6-3181-8e1f-53d9443a5808 | -3.2671 | -51.5345 | 2024-12-12 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3136a49f-6f61-3f8b-8b30-8bde58763658 | -14.7461 | -52.6471 | 2024-12-12 00:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| a4287fe0-5934-3ca2-a9ad-2af56707d9f2 | -6.9344 | -43.5401 | 2024-12-12 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 899bb11d-6af2-34f2-9f83-f5f15e0d6439 | -6.9346 | -43.5168 | 2024-12-12 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 291.1 |
| 3a794c1e-02e5-38b8-8fdd-bb815a54709e | -3.8573 | -40.4464 | 2024-12-12 00:12:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 93f12dc2-d7ea-31a0-abed-feb80aef25ca | -9.9719 | -39.173401 | 2024-12-12 00:12:00 | METOP-C | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1e619a1e-55d7-3f34-bf0f-7320bbbb1f78 | -4.7146 | -38.444199 | 2024-12-12 00:12:00 | METOP-C | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f0269f4-b072-3c1c-87e4-a9420a626028 | -5.5975 | -41.379501 | 2024-12-12 00:12:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac69515a-4c26-3934-9621-a106d5da8bc8 | -6.9386 | -43.541 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4a1129-d9e3-37e4-b40f-669fae2da967 | -6.1359 | -43.905899 | 2024-12-12 00:12:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11122f0c-df18-3114-8793-9d7b948eb5c2 | -5.5469 | -37.9874 | 2024-12-12 00:12:00 | METOP-C | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c3bd4761-1d97-3f20-9a2c-0076a45fd136 | -6.9198 | -43.502602 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a2c8e99-226d-36b7-94a6-eb25bdd5848b | -6.1174 | -42.536999 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89b82fd5-bdcb-370f-9c8e-54248e0a4393 | -7.9851 | -35.088299 | 2024-12-12 00:12:00 | METOP-C | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33f9ccca-4d3b-3a19-be8d-e57da596fe88 | -7.2973 | -44.5144 | 2024-12-12 00:12:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c9502238-ffa1-30a8-b2e5-86823502cd91 | -6.8887 | -40.124298 | 2024-12-12 00:12:00 | METOP-C | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 169aef5e-135a-3448-a110-0ccd9e609eb8 | -4.8243 | -44.201401 | 2024-12-12 00:12:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0345b46-7eb4-379d-976a-89489e5b4f60 | -6.1288 | -42.542099 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d94d30c4-6af3-3361-bd12-6b183b4b2a90 | -6.0541 | -44.046398 | 2024-12-12 00:12:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eae03e70-d0a2-3c40-912b-50ca4061545c | -7.4683 | -44.733299 | 2024-12-12 00:12:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3db772dc-a27a-3426-915d-08ede063dad7 | -5.8199 | -39.203999 | 2024-12-12 00:12:00 | METOP-C | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f727e824-39e4-335c-aec1-8059e7f43233 | -8.253 | -41.594101 | 2024-12-12 00:12:00 | METOP-C | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83a230e1-8e3d-3a2d-92d5-c2669fda70f6 | -7.8851 | -42.433998 | 2024-12-12 00:12:00 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19d6a0d9-0747-3bd8-be20-57b93a43c884 | -5.93 | -48.0527 | 2024-12-12 00:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5da858d5-61eb-385c-a1c5-15d21c19ba85 | -6.1223 | -42.558899 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f3344d8-2208-3515-838c-8b9edb16133c | -6.9368 | -43.532902 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 929487d1-6c72-3049-bccf-618a63fe1a26 | -10.5461 | -36.763401 | 2024-12-12 00:12:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f4d8f6d-59db-34ee-bcca-904f9c42e628 | -10.548 | -36.771599 | 2024-12-12 00:12:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9490c0b1-45d7-3633-bb67-b03220ab079e | -2.8326 | -40.2971 | 2024-12-12 00:12:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6295cb0c-085b-3537-8561-1c7d3af6f607 | -10.5373 | -44.6744 | 2024-12-12 00:12:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 652c302d-084f-3743-94dd-dbf70e4a2b6d | -6.1255 | -42.5275 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4655abef-96fc-3631-a78d-994b5e7ce4e5 | -4.8261 | -44.209702 | 2024-12-12 00:12:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 236a7bf9-c636-3d2b-93f2-b6783f537345 | -3.7749 | -47.084202 | 2024-12-12 00:12:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c785e4d-b0ea-3345-be67-215a2de6326d | -9.5505 | -35.839802 | 2024-12-12 00:12:00 | METOP-C | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35da7990-2e0a-3017-ba09-0bf0358a5da9 | -6.9234 | -43.518799 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b8342c03-4e85-3a16-98a5-40b5576c2ee8 | -5.1688 | -44.408699 | 2024-12-12 00:12:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83f0e60f-091b-3985-b3a0-010641ab23e6 | -4.865 | -40.746201 | 2024-12-12 00:12:00 | METOP-C | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cf075573-5161-3179-8302-31c656f340f8 | -9.3119 | -35.535801 | 2024-12-12 00:12:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92a70e22-a1c1-37f2-bed5-5d260acf3481 | -3.8475 | -40.448601 | 2024-12-12 00:12:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a5955a62-61c5-3d5b-aebe-a2f08512a548 | -6.9154 | -43.528999 | 2024-12-12 00:12:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a72d81a1-0c85-3f68-9471-fc20997ad11d | -5.8453 | -39.0462 | 2024-12-12 00:12:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| efa4f5b1-d8d7-3efe-b075-4d5d9bd15cf9 | -5.1494 | -44.368099 | 2024-12-12 00:12:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5411d3a-8dac-321d-a355-a91023c61b36 | -4.176 | -42.425499 | 2024-12-12 00:12:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57e37a4f-e7aa-3fdf-af94-e36242c05c51 | -6.7584 | -44.8167 | 2024-12-12 00:12:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7820c745-22d0-3138-9528-9b5e4e9badd7 | -6.7605 | -44.826099 | 2024-12-12 00:12:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbb5c8d2-e7f1-3311-9ef4-336e1c49db7e | -10.1787 | -36.3484 | 2024-12-12 00:12:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8cf0ef95-c69b-37f4-83cd-c4a73dda0f56 | -3.8491 | -40.455399 | 2024-12-12 00:12:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 311f4983-1868-3cf2-84af-4cf0c5edf109 | -5.9268 | -48.037899 | 2024-12-12 00:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03261145-6243-35a6-9408-506193c519ef | -6.1157 | -42.529701 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d59e5dd-a88e-308c-b92d-e4fc2ab7ebc9 | -6.7126 | -39.181 | 2024-12-12 00:12:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f97a347-de60-3fcd-bc07-e8982ad94d6a | -7.427 | -44.732201 | 2024-12-12 00:12:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a768da30-4ee3-306d-9f6e-c0922fd538f9 | -6.1206 | -42.551601 | 2024-12-12 00:12:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f988788-02ef-39ab-9d3e-283ab3ebbefd | -9.3884 | -38.879902 | 2024-12-12 00:12:00 | METOP-C | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 03d1a039-e529-329c-b3d5-6d1150e54f0e | -9.3143 | -35.545502 | 2024-12-12 00:12:00 | METOP-C | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19d26f09-803f-345c-80fe-fce6ce35fa3b | -3.2384 | -46.885101 | 2024-12-12 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0714a9-410a-3f06-8fb9-0af9914e4988 | -8.9117 | -35.632599 | 2024-12-12 00:12:00 | METOP-C | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26c7aac6-0e3b-3c9c-ac42-b742e13362c0 | -10.5908 | -44.976601 | 2024-12-12 00:12:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6837db95-3acc-329a-aa81-67570e5d7aaa | -4.1858 | -42.423302 | 2024-12-12 00:12:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e94ec817-be0b-3da2-90dd-0cf7025056cb | -3.8557 | -40.439499 | 2024-12-12 00:12:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ce7798bd-2870-31cd-887e-f22df5f53106 | -5.9203 | -48.054798 | 2024-12-12 00:12:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cc54adb-64c7-3152-9f8e-c2827237bc4f | -5.0091 | -41.015099 | 2024-12-12 00:12:00 | METOP-C | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
