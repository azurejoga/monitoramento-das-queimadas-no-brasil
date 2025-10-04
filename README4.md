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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5311df4d-a0d8-36f9-8e10-a04d1b6d436b | -5.4847 | -44.1212 | 2025-10-04 01:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 2f77ad8f-1123-31eb-a4be-f855d5da91a9 | -2.9013 | -50.7351 | 2025-10-04 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f274f774-28e0-3c07-aa6f-70fa802761d0 | -13.3422 | -48.0965 | 2025-10-04 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6773cc01-92f9-31ea-a49d-b447650c3332 | -11.9151 | -46.3499 | 2025-10-04 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| c83ab7b4-a208-3eb2-a856-6a937fa4f2c8 | -5.3851 | -47.2052 | 2025-10-04 01:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 559f331f-bc47-32d5-a2d2-809c9657bd05 | -9.3464 | -54.5201 | 2025-10-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| b2be4f20-8a71-3b98-ae51-ede662d4aaff | -11.9343 | -46.3472 | 2025-10-04 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4afe3bc1-e9db-3c2d-811e-42c1aa050df0 | -13.3221 | -48.1439 | 2025-10-04 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7d79c070-5f85-3bff-901d-47cd95ca5634 | -4.6135 | -43.1361 | 2025-10-04 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 11a152b7-b95d-31f5-84c2-f045d9044574 | -16.0212 | -50.9425 | 2025-10-04 01:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 7bd96efc-ce35-33f5-8d49-42884ccd2154 | -11.8959 | -46.3526 | 2025-10-04 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e32a6507-9539-3a7b-8b75-c4a8b1496312 | -9.3274 | -54.5418 | 2025-10-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d7be2dd8-a60a-3af0-b5f4-a42f63a7c3df | -8.7589 | -49.9139 | 2025-10-04 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b5ddb537-d0b5-3d07-90f7-8c5931b8c23e | -4.6322 | -43.1349 | 2025-10-04 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| d78fedaf-df56-3271-bde2-501fb66e2c7f | -4.9538 | -45.0921 | 2025-10-04 01:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 2bed4e32-1298-3008-8448-11eaf8c7b34b | -13.996 | -48.1987 | 2025-10-04 01:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 931fb2ce-fb16-3269-afa8-7c8bc5822965 | -4.4258 | -43.2408 | 2025-10-04 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| ab4920f0-105d-3517-9e4f-78e865f954ca | -6.8774 | -47.2334 | 2025-10-04 01:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 72276bb6-908f-3925-b765-c7bc35412b8b | -11.9147 | -46.3726 | 2025-10-04 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 265.3 |
| 8f210f7e-ac3a-343f-b6c4-0b16743d75fe | -4.4445 | -43.2397 | 2025-10-04 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 550.3 |
| 8f32c69a-9965-3f67-8de3-8f87c5566307 | -4.4845 | -42.8631 | 2025-10-04 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9cbc63a4-c68b-3326-af3a-26aebb7f81cd | -11.9339 | -46.3699 | 2025-10-04 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 359ead1e-7fe0-3756-bd64-1ccc66027c92 | -8.2316 | -46.8066 | 2025-10-04 01:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e9654ecd-b2f1-3dba-93dd-3e127dff1a41 | -5.1967 | -45.0541 | 2025-10-04 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9f8c8159-25a5-31a3-9d28-7d1dcfe72fc3 | -4.5946 | -43.1606 | 2025-10-04 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 8b2eb03e-e858-3c72-be0b-d6d257d573db | -4.632 | -43.1583 | 2025-10-04 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| bec31fbd-6196-3ae0-a883-a4cede0029f5 | -13.3225 | -48.1216 | 2025-10-04 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| d98680f8-a066-399e-b73a-78cda2e9371b | -12.3813 | -54.4603 | 2025-10-04 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c1cafb72-a67f-3cd3-91d3-94c5c9903273 | -17.0903 | -46.2347 | 2025-10-04 01:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 30e4f5c5-f0b0-3e15-aab7-ff3818a43d10 | -10.3343 | -50.3402 | 2025-10-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| dc5e6faf-723c-3d7d-b903-3648142240d2 | -10.3154 | -50.3421 | 2025-10-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| d53e0a74-54d0-3a47-bfab-efa79709bec9 | -17.0903 | -46.2347 | 2025-10-04 01:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6da078cc-f18d-3a80-bc59-5300f110bcb1 | -10.3157 | -50.3207 | 2025-10-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| ccee4c69-960e-3874-b19a-ead336424184 | -5.1967 | -45.0541 | 2025-10-04 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e32265ce-399c-3d39-8023-9cc2b8d32e9c | -4.5946 | -43.1606 | 2025-10-04 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 78cb25ba-6739-3b0a-aa58-1f6b2f7b713f | -4.9538 | -45.0921 | 2025-10-04 01:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 246309b8-58b2-3d97-b28e-62ac99ac1565 | -10.3346 | -50.3188 | 2025-10-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 193.5 |
| b1f59aee-0470-3ed5-bc2d-60fe2f1a2643 | -8.2316 | -46.8066 | 2025-10-04 01:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 459b44bc-2ee6-35f2-9a12-164d64b92a9f | -17.7044 | -47.0821 | 2025-10-04 01:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 0bb0a004-f4c2-3463-ad18-c8ccf7b2d1c1 | -5.1965 | -45.0768 | 2025-10-04 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 35d0540d-4ca9-38cd-8623-955a3202c13f | -4.954 | -45.0694 | 2025-10-04 01:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 228.0 |
| cae2240d-0273-3e5d-af93-b5d2bde99220 | -11.9143 | -46.3953 | 2025-10-04 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 7e95b0fa-2ec5-3f20-8161-97e013d544c4 | -9.3274 | -54.5418 | 2025-10-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4fdbc059-467c-3812-831a-f9ae079fa790 | -13.3225 | -48.1216 | 2025-10-04 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 1f692424-c78c-358b-86f1-43a6c21c7b80 | -6.8774 | -47.2334 | 2025-10-04 01:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 283e82e4-a8a3-3ef1-930c-3d3cf43d000f | -10.3348 | -50.2974 | 2025-10-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 08bf705d-4a19-3548-b6eb-1f4ef82bcfe1 | -2.9013 | -50.7351 | 2025-10-04 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8f5e62f7-a1e4-38b7-a5ec-dc1a035e5e4f | -4.9541 | -45.0468 | 2025-10-04 01:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 974a987b-c872-3a73-8c94-1b18af6be3c8 | -9.3276 | -54.5215 | 2025-10-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f0659b12-d895-39d5-a6e4-5c0a9996cf6c | -5.3849 | -47.2271 | 2025-10-04 01:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 907c734f-c0b9-37ef-99d5-1fd8660e982b | -4.6133 | -43.1594 | 2025-10-04 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c8881867-8293-34de-8e0c-46c7a46a9603 | 1.7666 | -55.8819 | 2025-10-04 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4ee59d21-7c0f-3e1b-ad98-68c42b0ff971 | -16.0212 | -50.9425 | 2025-10-04 01:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e2e61581-775f-318f-a470-346d89d1822a | -14.2321 | -46.0794 | 2025-10-04 01:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c4b06af3-a231-39b6-9a2e-b2f26bc8887a | -4.4445 | -43.2397 | 2025-10-04 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 3829da09-0ea1-34f0-b3b5-8d4d119757f8 | -8.6322 | -54.9949 | 2025-10-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 2971707e-a399-36a6-bd21-d27dd8502638 | -5.3665 | -47.2063 | 2025-10-04 01:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e4a03a9a-c221-3292-a74f-0b56e81e4194 | -11.9151 | -46.3499 | 2025-10-04 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 6cc08b25-b75e-33a9-ba4f-6042c1d4749e | -5.3851 | -47.2052 | 2025-10-04 01:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 442471cb-b188-35fe-a65b-f77acaef6691 | -4.632 | -43.1583 | 2025-10-04 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 2bd3e6d1-c6ba-3750-83a4-a7f4f447ab98 | -4.9726 | -45.0683 | 2025-10-04 01:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 26384b9c-3cdb-3901-95f5-df6f1d9cbda2 | -11.9339 | -46.3699 | 2025-10-04 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| e46ba083-2ba6-3743-80cc-5ecc9c054225 | -11.9147 | -46.3726 | 2025-10-04 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 348.7 |
| c932d36e-e302-362f-9f37-899ac3ee33e9 | -9.3464 | -54.5201 | 2025-10-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| be9f42a0-d519-3182-bb51-443f25189631 | -4.6135 | -43.1361 | 2025-10-04 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 74b9a3a7-2d39-3fd2-8ff5-fb4cd9f24212 | -5.4849 | -44.0982 | 2025-10-04 01:10:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d550b66e-4ca7-302d-b2ff-660777614a8f | -11.8956 | -46.3753 | 2025-10-04 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a13b409d-4e9c-3bea-bb77-e09b75468212 | -11.9343 | -46.3472 | 2025-10-04 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c9f7f788-0e68-364e-81aa-fc3d642076d0 | -4.4443 | -43.263 | 2025-10-04 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| d4321ae3-401b-3d95-8c70-21b67ea7481e | -6.8774 | -47.2334 | 2025-10-04 01:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 35da4f9a-1059-3d5e-a57a-26466a2c4df7 | -4.4259 | -43.2175 | 2025-10-04 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 9dad9192-c46a-3237-a996-ae790e64d093 | -5.3663 | -47.2283 | 2025-10-04 01:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 96dd8c3f-bf51-3812-875b-ac28d9083343 | -16.0212 | -50.9425 | 2025-10-04 01:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 03a72dbc-0d06-35de-a65a-dca3e15ae211 | -4.954 | -45.0694 | 2025-10-04 01:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 5f74f224-155c-3147-948d-8adadd324dce | -12.0507 | -45.1872 | 2025-10-04 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e8f5d53e-509b-3e9d-83fb-7906459a4dcb | -5.4847 | -44.1212 | 2025-10-04 01:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2fbd84bb-69b6-307a-8439-bd5e336aad13 | -17.0903 | -46.2347 | 2025-10-04 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 03228e9b-bee5-3892-a358-16dbfa7f530e | -9.3276 | -54.5215 | 2025-10-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| ff9c2a1f-3be5-3d24-9667-f50194b9aa0a | -4.4256 | -43.2641 | 2025-10-04 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| da43d556-122a-37a8-999e-fd0c7b791cf6 | -4.4632 | -43.2386 | 2025-10-04 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 549e3e2f-f65f-34bb-b9b9-83d3b6e9e859 | -4.4446 | -43.2164 | 2025-10-04 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5f10ce5e-db36-3692-9e0a-c1a2700a3889 | -10.3343 | -50.3402 | 2025-10-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| db00c6a7-1dad-3787-85d9-08e6481935cc | -4.4258 | -43.2408 | 2025-10-04 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| f237c1d6-4012-3bdf-8663-46572756ce28 | -2.9013 | -50.7351 | 2025-10-04 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b812e4c3-66b1-3da2-908f-3236239e5ba4 | -4.6135 | -43.1361 | 2025-10-04 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| c5ebb905-cbf0-3480-9990-6830f371dc6f | -14.2321 | -46.0794 | 2025-10-04 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| bceda827-122a-3010-a638-bba311b7a546 | -10.3154 | -50.3421 | 2025-10-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 83077f06-80b8-3727-8637-c1cfafe4c360 | -5.3665 | -47.2063 | 2025-10-04 01:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 594a8e3e-e516-39e5-9523-43bbb5ccf005 | -10.3348 | -50.2974 | 2025-10-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2f71be8d-985a-3cc1-b573-261b3ca907da | -5.1967 | -45.0541 | 2025-10-04 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| fce5a50a-3bbc-351b-9960-900505663b0c | -13.3225 | -48.1216 | 2025-10-04 01:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8851500e-6396-3393-b4bc-abf5b671ebb2 | -4.4845 | -42.8631 | 2025-10-04 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 62b2adfb-b36b-3c21-a3db-ec6315ecdde2 | -10.3157 | -50.3207 | 2025-10-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 10009bde-9210-3d5f-ab52-ed5568ad790d | -4.4445 | -43.2397 | 2025-10-04 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 396.5 |
| 628f5642-7da5-3cc7-8cab-c720cb5050c4 | -5.3851 | -47.2052 | 2025-10-04 01:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 136.2 |
| ad555336-14ef-34c3-a423-9dfd05f520e3 | -5.4849 | -44.0982 | 2025-10-04 01:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| c4632c6f-dcbf-39cc-b485-a803e4dae6e4 | -9.3464 | -54.5201 | 2025-10-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 237b2294-0fde-3368-a443-2f848d0a66fd | -17.7044 | -47.0821 | 2025-10-04 01:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9685df75-22c9-381d-9589-43548f265dca | -5.1965 | -45.0768 | 2025-10-04 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b83385d6-53dc-327e-b43a-54b0ff0e8448 | -4.6133 | -43.1594 | 2025-10-04 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 187.0 |


[Clique aqui para ver as próximas entradas](README5.md)
