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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5469e399-b2a1-3d1f-800e-6332c10c2290 | -20.4398 | -56.993698 | 2025-08-01 01:00:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4489a01a-fff6-3a61-af3a-6e9b2169801e | -10.1143 | -58.221699 | 2025-08-01 01:00:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa83efc4-0196-3a26-8269-9eb209f282e1 | -20.4137 | -57.0154 | 2025-08-01 01:00:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1aefbff8-b988-330b-baf0-fd3a11a269db | -10.7332 | -50.483101 | 2025-08-01 01:00:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61aed907-b66e-3197-9204-c12787a15159 | -15.084 | -55.203201 | 2025-08-01 01:00:00 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f36d07f4-a805-3f4e-960f-c2455328b9f6 | -20.4121 | -57.008099 | 2025-08-01 01:00:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3b880f19-afc9-370c-af89-e3819da0b26a | -6.7487 | -59.150398 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 776f4caa-e785-3df9-a0ff-ca05e3fa0ece | -6.8442 | -59.253799 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2c9cc36-6fe4-300c-81ba-30dfb0ea5043 | -6.8312 | -59.242001 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4079f809-294d-3646-9579-e13518c26016 | -6.7338 | -59.1758 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b48d396-d8a7-3e3f-941c-eb06ce3055c1 | -6.7373 | -59.145599 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae7234e-b949-3d2c-8194-ab753e3f5137 | -6.643 | -59.093102 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c315be69-d301-309a-8071-5b18d2c400fd | -10.7285 | -50.4645 | 2025-08-01 01:00:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbbd54e5-2ceb-37a3-9d24-edf1468fba9f | -6.6528 | -59.0909 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fffb492-3caa-3689-ae68-680df1507116 | -6.81 | -59.239399 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90a842ff-7903-3776-8e7c-1d070e859f0a | -6.8344 | -59.256001 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66620b88-5b44-38a8-9a3b-023c9b8ef452 | -6.5521 | -56.184299 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c552de-7c9b-33fd-95db-ad9a9b442c09 | -9.4572 | -57.826099 | 2025-08-01 01:00:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c54412c-98ca-3ca0-a11a-3534e8a90cb0 | -6.5445 | -56.195702 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96d19365-af0c-37bc-a750-eb428cec1293 | -6.7275 | -59.1478 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 619e4c9e-2dc9-3f11-98f7-3559d29cb966 | -6.8359 | -59.262901 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98c20d9d-303a-37b5-a76e-209b872c37da | -21.2388 | -48.557499 | 2025-08-01 01:00:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 50216517-4ed3-3d7d-8b33-f4d83fe9231c | -15.4128 | -55.772701 | 2025-08-01 01:00:00 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07e5bd18-f7e8-3db4-b94e-5cf341253eec | -21.448799 | -57.142899 | 2025-08-01 01:00:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a719d759-9213-34c7-bd68-8e6f7691559b | -9.6253 | -63.4034 | 2025-08-01 01:00:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36a40044-4f52-3dee-976b-47d70a5b1bb3 | -6.8116 | -59.246399 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59a4c3ef-d6ff-3a8a-9999-3496d62debc2 | -6.5564 | -56.202599 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01ed1c1-842b-3619-8e45-5d488ec0b13d | -6.823 | -59.251202 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc97896-df3d-30a5-83c2-a6a4021f9379 | -9.6292 | -63.4216 | 2025-08-01 01:00:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78405f37-97fb-326d-a2c9-d179421679d0 | -6.8296 | -59.235001 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e59da291-2934-3086-ab9c-17bdaef5e2a6 | -7.3281 | -59.618301 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0e1b57-1ec7-343b-be9f-79d968c5171e | -23.5065 | -47.806801 | 2025-08-01 01:00:00 | METOP-B | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e792677-d68b-31c7-b6fb-19a7a42843d8 | -15.0898 | -55.228199 | 2025-08-01 01:00:00 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| feab1e95-35d1-30d8-91e7-acd23a695113 | -10.4282 | -47.2635 | 2025-08-01 01:00:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64d8e45b-cd04-3683-9b81-c839390c985e | -6.7436 | -59.173599 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7968b70-be4e-3ffc-8329-4e746e1d4cf7 | -6.8214 | -59.244202 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3600c397-fb86-3785-af99-549d68370aef | -6.8261 | -59.265099 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4b7b756-f43f-37ee-884b-9247f5130b6c | -6.8246 | -59.258202 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd6af5f4-ee06-34b4-b5c0-17267d4405a8 | -6.724 | -59.178101 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be956e30-7534-3414-b164-b2e00d536080 | -14.0386 | -53.594501 | 2025-08-01 01:00:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64c8672f-5746-3999-ad3f-150cd4f52fc5 | -6.7405 | -59.159599 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb2a460a-ccd9-314c-b303-1c3558d48964 | -6.805 | -59.2626 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77dc40b7-66f9-3b93-857e-9c718ddfa45d | -6.6414 | -59.085999 | 2025-08-01 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5df89ea4-7c8d-32e0-97b8-bfdcfe443339 | -10.4377 | -47.260799 | 2025-08-01 01:00:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de866a73-c4c8-39c5-ba7a-38fa4e3c3b1c | -6.6522 | -58.8158 | 2025-08-01 01:00:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffafa7ec-8c55-38ae-a09a-97c369f47b8a | -6.5542 | -56.193501 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03345963-bd23-331d-9c34-a300f3411380 | -6.5249 | -56.200298 | 2025-08-01 01:00:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72667088-a3c5-38b6-bcf3-d30f15b3733f | -7.7444 | -45.0762 | 2025-08-01 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 301.7 |
| e8b4bff1-f00d-301e-9ffe-f07ec04fc6b8 | -7.7632 | -45.0744 | 2025-08-01 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| cb3dad5d-569d-3014-bbae-be6b2dd5ccfa | -11.7858 | -44.9958 | 2025-08-01 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5b68673c-2e05-3674-8fe2-2897ed0ded60 | -9.629 | -63.422 | 2025-08-01 01:10:00 | GOES-19 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| b438b179-a635-30bc-92c7-75265bb93074 | -23.5242 | -47.8109 | 2025-08-01 01:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 179.7 |
| 653cd8ae-30cc-3846-baaf-8f7d5c7137b0 | -8.0324 | -43.1022 | 2025-08-01 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| f678c3a6-2837-34c3-95aa-14035ae52fc8 | -6.7293 | -59.1916 | 2025-08-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 5a87efde-f1d7-330d-96c2-e2380433a58e | -23.5022 | -47.8407 | 2025-08-01 01:10:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 181.2 |
| 9446461e-c0ac-3617-bb4e-6da7fa84eb6f | -7.7255 | -45.078 | 2025-08-01 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d2e7b2c9-28d1-3539-a992-c4b2fc9ccbda | -23.5446 | -47.8293 | 2025-08-01 01:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| c4176e82-520e-3a3d-890b-74c46324f43d | -8.0321 | -43.1257 | 2025-08-01 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 7a8593ef-fd11-3c21-88dc-8adb296d7932 | -11.7666 | -44.9986 | 2025-08-01 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 1cb01c91-ca93-309d-a5b2-4a9d2bf6c45c | -7.7441 | -45.099 | 2025-08-01 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8989b29d-feb7-331a-8127-1049f9a44dbc | -6.748 | -59.1523 | 2025-08-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 8dbe0398-ec71-3219-b91c-ce2ee6d884a9 | -6.7294 | -59.1723 | 2025-08-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 285.8 |
| 59c0b08d-c4a0-3503-8824-025ae0556c96 | -10.434 | -47.2601 | 2025-08-01 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| aab207ab-c1dc-38a3-8ee9-cb3a88900794 | -9.3989 | -45.4928 | 2025-08-01 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 3bc1e0d4-39b7-313d-8a8e-33b10286b534 | -8.3394 | -50.5863 | 2025-08-01 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 6a3034d9-3d02-33c1-a18e-c5762e7e967e | -23.5226 | -47.859 | 2025-08-01 01:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.8 |
| cd680868-b1e0-3a78-ac48-f2bc42c0187a | -8.3396 | -50.5652 | 2025-08-01 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| b65c0dcb-81d9-3b9f-986a-b49733656b40 | -7.7446 | -45.0534 | 2025-08-01 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a406fcae-8ad0-3d8b-800e-82fd3d88b2cb | -6.7295 | -59.153 | 2025-08-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 5a366516-80bb-3baf-a22a-a293c9149cf1 | -8.051 | -43.1237 | 2025-08-01 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| bb28c561-12e7-346f-a6c9-c9e94691c316 | -23.5029 | -47.8166 | 2025-08-01 01:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.4 |
| dba91864-6d4b-3051-8a8c-33ed9902981d | -23.5234 | -47.835 | 2025-08-01 01:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 352.8 |
| 834e4743-0158-329a-a1f2-c19928b5ce1f | -8.3209 | -50.5667 | 2025-08-01 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d9481279-d73f-315f-969c-42caf11496c8 | -8.0513 | -43.1001 | 2025-08-01 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 9bbc042d-2eb4-3618-80f6-1d167a50e771 | -6.7478 | -59.1716 | 2025-08-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 248.8 |
| 63e82081-27c1-32c7-870e-ce7ea5b90401 | -6.7477 | -59.1909 | 2025-08-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5bb8da10-4366-34f2-ad70-57e5e536db58 | -6.6143 | -59.9848 | 2025-08-01 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3a0156c8-71c2-32dc-8091-42fbdd5866db | -7.7444 | -45.0762 | 2025-08-01 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 250.9 |
| 4757d372-3921-3c6e-b133-cd320dca6470 | -8.3394 | -50.5863 | 2025-08-01 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| d433e457-f41b-32b6-b85b-ac3910db89e1 | -6.7294 | -59.1723 | 2025-08-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 431.7 |
| a37b2cfe-d96b-3ce7-8a0a-1b8d99153fff | -23.5022 | -47.8407 | 2025-08-01 01:20:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.2 |
| 375b37d1-008f-3373-bcea-8ff147af1b36 | -6.7293 | -59.1916 | 2025-08-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 1c35aea6-c58a-39d7-9c31-afa2ecc8feea | -11.7854 | -45.0189 | 2025-08-01 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 5b069502-e149-3e9b-82e5-060da361a7e4 | -7.7632 | -45.0744 | 2025-08-01 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 00247d3d-2b42-3139-a1e1-43c3032c1b77 | -6.7295 | -59.153 | 2025-08-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 6a6e02e9-9505-371f-9f4f-cf3048ffe99f | -7.7255 | -45.078 | 2025-08-01 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 2ccc485c-13f4-3fba-a471-5dff6466ce8c | -8.051 | -43.1237 | 2025-08-01 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| ee8c4b17-9de5-3e6b-8592-6eba581ca92f | -7.7446 | -45.0534 | 2025-08-01 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 0a4fbe35-4ff4-3c43-9622-6b75813c97e8 | -8.0321 | -43.1257 | 2025-08-01 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| a0a8fedd-a0c9-36d7-8e3e-ed6cef770f1a | -9.629 | -63.422 | 2025-08-01 01:20:00 | GOES-19 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 81d78eae-f2ae-39c6-92e2-b1b001722bad | -9.3626 | -40.328 | 2025-08-01 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 2a6eb03a-66b7-3bd0-b08a-3cf4cb2760c5 | -23.5242 | -47.8109 | 2025-08-01 01:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.1 |
| 24355edb-d345-346e-bbc4-7ea85adce421 | -11.7858 | -44.9958 | 2025-08-01 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| eda2be98-8702-35e3-a06b-310fb9f9b62d | -6.7478 | -59.1716 | 2025-08-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 218.3 |
| b178bde6-51ca-3901-bfbc-bc2ec9231fc9 | -23.5226 | -47.859 | 2025-08-01 01:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| c51915ce-7a95-3f58-9f43-ddaaa205ae99 | -9.4178 | -45.4906 | 2025-08-01 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 5560b0fe-83ce-35da-92ca-e7da5f36ea1a | -8.0324 | -43.1022 | 2025-08-01 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 7c7dfe33-9af0-3c81-ae5c-f1e6327fb2a8 | -6.748 | -59.1523 | 2025-08-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 566e0adf-eca6-345b-8f65-86395b7e438d | -7.7253 | -45.1008 | 2025-08-01 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 13b65200-124d-3e22-89af-5973cadd3844 | -7.7441 | -45.099 | 2025-08-01 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |


[Clique aqui para ver as próximas entradas](README6.md)
