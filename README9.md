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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57723260-dfe3-33b7-b068-eee4f031be69 | -11.4776 | -45.1099 | 2025-07-30 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c40b960f-0b58-33ed-a08a-021aa45de7d9 | -12.4737 | -47.2621 | 2025-07-30 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 224f4579-9d4e-30fc-8ea0-e4fb106ce266 | -15.7174 | -41.9272 | 2025-07-30 01:50:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| fc588a6b-c9a3-3b7b-bbeb-66f74fec90f3 | -4.6511 | -43.1104 | 2025-07-30 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0a64266b-0372-3bff-aafd-8ffd1df14d6c | -6.5074 | -56.213 | 2025-07-30 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 673538c9-a18f-3da1-9bf9-58735571d0c4 | -10.6172 | -45.2282 | 2025-07-30 01:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d177a2ea-816b-399d-91b2-0f4bd6b2fc04 | -17.4745 | -46.7363 | 2025-07-30 01:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 3316abfc-c18b-3fb9-bb6f-ce7bc1f5d10f | -11.4584 | -45.1126 | 2025-07-30 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| fa5a9d22-33d9-3f58-9301-e47d1d99ed13 | -15.7167 | -41.9521 | 2025-07-30 02:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| f5898492-a343-336a-880b-71689c01544c | -6.526 | -56.1923 | 2025-07-30 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 561c2f81-2bff-3a7d-9b45-8f692a61d51e | -4.6511 | -43.1104 | 2025-07-30 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| bb46fe52-82c9-3398-949d-b12898940341 | -12.4737 | -47.2621 | 2025-07-30 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0cc368ff-b847-33f0-898f-2dba0f0282c3 | -17.4745 | -46.7363 | 2025-07-30 02:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 112.3 |
| a16ba24b-2ac1-393d-8e79-54e2c526a9b7 | -4.6509 | -43.1337 | 2025-07-30 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b1248db7-d239-38b1-9735-e139127d642b | -15.7372 | -41.9227 | 2025-07-30 02:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.5 |
| fc3ea765-84c6-3c49-9509-18a02ddc3856 | -11.5307 | -44.267 | 2025-07-30 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 6b1200d6-9015-39c0-a5c3-ce8ad7dde4fa | -10.6169 | -45.2512 | 2025-07-30 02:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ba30aa79-dbde-3249-826c-15da3154ad10 | -6.5258 | -56.2121 | 2025-07-30 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 1db73f27-d4b4-3706-b601-f4f4c2274962 | -2.9108 | -48.254 | 2025-07-30 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| cee009a6-f93f-3814-84f3-61f8cd7af0cd | -10.6172 | -45.2282 | 2025-07-30 02:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 3a977246-be8d-37b0-8b8d-1d817d2a75fb | -6.5074 | -56.213 | 2025-07-30 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 8ac38614-aa0b-370f-b92d-2337ad375cf6 | -17.4945 | -46.7321 | 2025-07-30 02:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 202.4 |
| b46b824b-f039-360e-9fed-d0b3534c232c | -15.7174 | -41.9272 | 2025-07-30 02:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 196.9 |
| 2b2b54c6-be53-3bd1-be28-3342952e48c9 | -17.9635 | -50.3765 | 2025-07-30 02:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| cf8ec3c2-49a2-394c-b79d-76607ae7b0c1 | -11.3395 | -48.9134 | 2025-07-30 02:00:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| d757c410-5855-3f0a-8e1d-c8969f5722ad | -6.5075 | -56.1932 | 2025-07-30 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 05dcd43e-ca6f-300a-80ea-da51bd9cc412 | -17.963 | -50.3987 | 2025-07-30 02:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 597c6772-5b28-308a-ae27-d14a2ac70111 | -11.3205 | -48.9157 | 2025-07-30 02:00:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a144530b-cbf8-3a29-8250-72b019f3ac00 | -12.4733 | -47.2846 | 2025-07-30 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5f0e4c25-6c3b-3a82-bbe4-2f38b782d6df | -2.8923 | -48.2546 | 2025-07-30 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5dacc753-344f-3903-9db6-d0455614ed9e | -11.4776 | -45.1099 | 2025-07-30 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ed655bf1-30f5-354c-bf95-659fb90b979e | -11.4584 | -45.1126 | 2025-07-30 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c38fae45-e766-3084-87ee-ea8a0a269293 | -4.6511 | -43.1104 | 2025-07-30 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 5322fdae-9871-32cd-8d80-0de7e9cdb18d | -6.5074 | -56.213 | 2025-07-30 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 23146434-aa4f-3046-9b75-85fc5956f9a9 | -6.5445 | -56.1915 | 2025-07-30 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| bc6fc3c7-c371-3698-a13e-f36642f051ce | -15.7174 | -41.9272 | 2025-07-30 02:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| a6a3cc49-f119-33e2-b6e7-898fe30218b0 | -6.5629 | -56.1906 | 2025-07-30 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 8bb2ac9c-c236-3c9e-b643-b22063cb4fb6 | -6.5075 | -56.1932 | 2025-07-30 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0672e654-4aa9-3616-a832-b735db3633aa | -17.4951 | -46.7089 | 2025-07-30 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 269a3b1e-0a4d-3c3e-a433-fad241ff0810 | -11.4584 | -45.1126 | 2025-07-30 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b22aafb1-dbab-32b8-8128-5d118153b627 | -10.6172 | -45.2282 | 2025-07-30 02:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| d568cbc2-a9e7-3d76-abb8-9e5d5b5e1140 | -10.6169 | -45.2512 | 2025-07-30 02:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| bde4e319-513c-33ec-906d-c1c4ba0fe44d | -11.4776 | -45.1099 | 2025-07-30 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0b9dd7ea-cf81-3bea-b049-fa204e33b694 | -6.526 | -56.1923 | 2025-07-30 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 276fb005-d7d4-3fcc-b864-ac2309aae752 | -6.5258 | -56.2121 | 2025-07-30 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| a2363282-68d9-37d0-a7e8-26dab1cfc52f | -17.4745 | -46.7363 | 2025-07-30 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 151.3 |
| d1bb47e8-4893-399e-948a-9a894c746a14 | -11.3205 | -48.9157 | 2025-07-30 02:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| daab82c9-f771-3ef7-886b-1c4bfa63bb20 | -4.6509 | -43.1337 | 2025-07-30 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3947429f-d831-3df0-a77f-2c4c890e4ae8 | -2.9108 | -48.254 | 2025-07-30 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 5ecdd2a8-f08e-38f8-b000-d75037287e9c | -17.4945 | -46.7321 | 2025-07-30 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 348.1 |
| 1137daae-50ae-3822-8707-94972a6d7356 | -12.4733 | -47.2846 | 2025-07-30 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e3069358-b107-311a-bf5e-e6be3840aa4f | -17.4939 | -46.7554 | 2025-07-30 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| cea61768-b310-3c9b-8c86-345407c79043 | -12.4737 | -47.2621 | 2025-07-30 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 21b4c697-f1b6-3ed8-b4a6-075815c4df88 | -11.3395 | -48.9134 | 2025-07-30 02:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 7e04bd34-6f4a-3dd6-a68a-0c33f239e772 | -11.4584 | -45.1126 | 2025-07-30 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e5862050-b9d8-3ab4-b088-297b07c19db7 | -6.526 | -56.1923 | 2025-07-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4516c220-a2b2-3d30-9de8-a69e47ba43ee | -10.6169 | -45.2512 | 2025-07-30 02:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 752426ac-6ab4-3e23-a5e2-ce5368ae8871 | -4.6509 | -43.1337 | 2025-07-30 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0b000031-44ff-3af3-8929-74ab5b4833de | -6.5074 | -56.213 | 2025-07-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a640fb0c-bc16-3055-9e9a-dc8af368cebd | -4.6511 | -43.1104 | 2025-07-30 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d61da80b-a4f2-33c6-8ec6-f464ce02d445 | -12.4733 | -47.2846 | 2025-07-30 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 4c3ec17a-51a2-3aff-b39b-423f58d93071 | -6.5445 | -56.1915 | 2025-07-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| ab3db5a6-ed32-30da-a330-5d058d1f4f82 | -6.4889 | -56.2139 | 2025-07-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c16ddbea-dbaa-3d50-a926-12b75b43fabb | -6.5258 | -56.2121 | 2025-07-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| c76ee47c-43a3-3deb-b624-46e9227974a8 | -11.4776 | -45.1099 | 2025-07-30 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 4a153889-b262-3fad-b010-169a70579faf | -10.6172 | -45.2282 | 2025-07-30 02:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0100f1d0-adcf-398b-a998-f7c3d456df44 | -11.3205 | -48.9157 | 2025-07-30 02:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| b7e6e04c-49fe-3bac-80c0-e99efce28c28 | -6.5075 | -56.1932 | 2025-07-30 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 5cc56456-bb74-3e5a-ad8d-d1bbcba73a10 | -17.4745 | -46.7363 | 2025-07-30 02:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 4f1f6b32-e925-38a6-b087-d6fbb862912e | -8.5211 | -43.3063 | 2025-07-30 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e1000e1f-268a-3f14-b464-90fe4e6d5731 | -17.4945 | -46.7321 | 2025-07-30 02:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 265.1 |
| 10124bf5-2955-301d-92e1-1839926baa5f | -11.4584 | -45.1126 | 2025-07-30 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| d2678803-c4a5-38f0-b8b0-f2e66b8671cf | -6.526 | -56.1923 | 2025-07-30 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 25aa0e9b-578f-31f4-9688-4137ddd1fda6 | -10.6169 | -45.2512 | 2025-07-30 02:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5483dfe9-91f5-31d2-9e53-3a0836362f53 | -12.4737 | -47.2621 | 2025-07-30 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| c010ed4e-42f2-3169-885a-c65a3cc98189 | -10.6172 | -45.2282 | 2025-07-30 02:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 05ec69d2-48d8-326e-93a9-b245ae62c0a3 | -11.3205 | -48.9157 | 2025-07-30 02:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ea210610-7dc0-3759-94c1-c239b85ef9ac | -6.5074 | -56.213 | 2025-07-30 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3df85620-1991-319e-86f9-d7a95767a085 | -11.4776 | -45.1099 | 2025-07-30 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a4d6012c-3b9e-398e-8e06-30ea1a5a97c8 | -6.5075 | -56.1932 | 2025-07-30 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 957defd9-c6bc-32ac-8c46-1305aa3422c5 | -4.6511 | -43.1104 | 2025-07-30 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a199f3e8-491b-3661-bf07-e1eee566e580 | -11.3395 | -48.9134 | 2025-07-30 02:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d567cfd4-2df7-3aa2-acd6-067d8778eba7 | -17.4745 | -46.7363 | 2025-07-30 02:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 190d81df-9435-3307-98a2-6353bb47251a | -17.4945 | -46.7321 | 2025-07-30 02:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 8a11489c-bc79-3efd-8a6c-b07b0cb30093 | -11.3205 | -48.9157 | 2025-07-30 02:40:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 6bf402dc-336b-3518-9cab-7dfe508bba6f | -11.4776 | -45.1099 | 2025-07-30 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| cee79a62-0529-3341-ab47-cc96442d94f7 | -10.6169 | -45.2512 | 2025-07-30 02:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 556fb8d2-0cde-3246-9b71-08f08409c8e7 | -2.9108 | -48.254 | 2025-07-30 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| be780cbc-47ef-354c-9910-4db2e24ef96c | -11.4584 | -45.1126 | 2025-07-30 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b14ba3b5-c1dc-3f8e-bdd5-02458fe9f2f5 | -4.6509 | -43.1337 | 2025-07-30 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 917b3dc1-1795-3c28-8c87-2ceeb7d326a3 | -10.6172 | -45.2282 | 2025-07-30 02:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| bc4b9f92-d0cf-3867-b6b7-c8f6b110f7c0 | -10.6169 | -45.2512 | 2025-07-30 02:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| f2fdcc5c-5e7f-3783-a868-8c091af59ea1 | -10.6172 | -45.2282 | 2025-07-30 02:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| aa8f1479-3de7-3a7b-bf33-d06b27c40015 | -4.6509 | -43.1337 | 2025-07-30 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 673f9a25-b80a-3b3f-92f9-2f21b15c30d8 | -6.5075 | -56.1932 | 2025-07-30 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 98a28bb9-351a-3137-8238-3cd99b3c860d | -11.4776 | -45.1099 | 2025-07-30 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 66b43db8-87f3-3644-9f23-9309ba07e8b9 | -6.5074 | -56.213 | 2025-07-30 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| d71f29ca-31e8-3800-9a1d-d0796158610d | -8.5211 | -43.3063 | 2025-07-30 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1771ddac-3eda-37e4-baba-028d5a69f7bb | -17.4745 | -46.7363 | 2025-07-30 02:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6e6fcfa7-d089-3bec-bbbd-512987d576af | -17.4945 | -46.7321 | 2025-07-30 02:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |


[Clique aqui para ver as próximas entradas](README10.md)
