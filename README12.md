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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7e6b93e-9d3d-3e0a-9845-25a155606a50 | 1.6656 | -50.771599 | 2024-12-01 00:38:00 | METOP-C | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3256b4-06aa-3829-ba11-c2bc50913988 | -2.9735 | -46.941299 | 2024-12-01 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 188390e7-b39f-3aad-a560-0045af164bc8 | -4.5579 | -45.7187 | 2024-12-01 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de038205-93be-3c4a-a04d-cea3242365a6 | -4.1817 | -43.9786 | 2024-12-01 00:38:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64fe1f0d-dbb3-34f0-bb65-baca3dee429e | -4.5561 | -45.711102 | 2024-12-01 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0223781-b981-32f9-8285-2377a2274da9 | -4.8231 | -48.481499 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a33c22d-8cba-331d-9711-b4761cd25ac2 | -1.2383 | -51.790401 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bebce8a-7341-3f7c-adca-c896805b6cc9 | -4.8451 | -44.474998 | 2024-12-01 00:38:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9d870a-1a4f-3459-aef9-f3d8cd090a2c | -4.8319 | -41.299198 | 2024-12-01 00:38:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b26b9133-e91b-37e8-a336-1595410ccdd4 | 0.9397 | -50.743099 | 2024-12-01 00:38:00 | METOP-C | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 740cf66a-e26f-315a-b27a-23ee5b53bfb1 | -0.9592 | -51.650799 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffd22901-e302-3e57-a4fd-2b1e13fc5e9e | -4.3479 | -45.925201 | 2024-12-01 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42a386b7-d500-3513-a09f-c9b84f92fd7d | -3.3228 | -45.642799 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1b232ac-0c6b-37dc-816a-aafab9cd0e15 | -4.2696 | -48.361 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1fe1d63-c208-39b2-a75f-99aef5da3d66 | 0.9381 | -50.750198 | 2024-12-01 00:38:00 | METOP-C | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| faf33a77-3e7e-3572-aeb5-407289218d2f | -3.8272 | -50.130199 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98f46e5-ed41-3432-860d-e63a1d8b551b | -4.5034 | -43.943298 | 2024-12-01 00:38:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f4d28bf-a728-38ed-b829-40b0412e7890 | -1.2561 | -51.778 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0503f4d4-5d50-34b1-8836-a5e0933e16fb | -4.5477 | -43.562698 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29b3f2f7-0412-382b-b503-7c5ec09cf272 | -2.141 | -54.855999 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b112e90-2152-32b5-9b17-6845b095b419 | -2.7023 | -45.413898 | 2024-12-01 00:38:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27838e4c-c457-37de-9fca-bbb359f97f52 | -4.3169 | -48.2071 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 465c6aa5-a76e-3125-afcc-bf85fa67417a | -4.5501 | -43.311298 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aec67e8e-623c-358a-ab5d-d426e8613698 | -3.7846 | -48.089901 | 2024-12-01 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459fb5f8-2b76-3607-b902-b567421079c7 | -1.2469 | -51.737701 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee05c0cc-b1c6-3c9b-8b83-d8e7423bdccb | -1.1538 | -51.691101 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92acb59-52f5-3ae0-af2a-af8c20e037c8 | -4.6929 | -42.394299 | 2024-12-01 00:38:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 502d03ff-13a4-3b4a-a148-95f609c99af3 | -2.7545 | -51.7575 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef667f3-b841-310d-b1dc-dfbd9e583f9a | -3.9727 | -47.247398 | 2024-12-01 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d60bb6-8a47-3935-988a-8ee21df6d868 | -0.5972 | -51.6898 | 2024-12-01 00:38:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7fcc86-0b97-37d1-b2ff-2fd65fcbffbc | -1.3126 | -51.664299 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbabea49-3a5e-3035-b341-e1d551c54edf | -1.2777 | -51.646801 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb399e3a-6782-3db6-a475-a60592185ddc | -4.8018 | -44.994598 | 2024-12-01 00:38:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72e28255-e665-3628-a64e-ab180e4fcf6d | -3.6191 | -49.849098 | 2024-12-01 00:38:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ecce8d-58a8-3ab3-9d15-241bf6f8d172 | -2.1925 | -53.769001 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b10a810-ec01-3098-9f7b-b43e72cd5c70 | -0.2639 | -51.494499 | 2024-12-01 00:38:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3abd10-f4f7-33df-b81a-eec85285a627 | -4.3514 | -45.940201 | 2024-12-01 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b319ee60-4e09-3ed6-9e55-1f51bc14442d | -1.0417 | -51.7411 | 2024-12-01 00:38:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4bba6da3-6d4d-37c3-8113-d72b0689a70e | -3.849 | -46.532902 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78418002-d5b1-3134-9558-ab7c2ca21937 | -4.189 | -50.682301 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b370fa5b-37a4-3564-89d9-ad7320d034f4 | 0.9573 | -50.217602 | 2024-12-01 00:38:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 09de4fe2-f342-354b-8b14-4f667ab70d94 | 0.9479 | -50.752399 | 2024-12-01 00:38:00 | METOP-C | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a5089e3b-3871-35cb-aaae-aa25843d726e | -4.1988 | -50.680199 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6aa980f-90d1-3ff8-b815-8eab22ef2131 | -4.3035 | -48.238701 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 337a89b9-b80a-3663-9a29-ad75c1816394 | -4.6763 | -48.1553 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8b9a4e-e1a3-3073-acb9-170513a35130 | -3.4556 | -44.928398 | 2024-12-01 00:38:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f60bfb2-6581-3859-b701-a141f5933a00 | -1.1801 | -51.761002 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a85a0b2-a6fb-3001-af06-a58794eca5f1 | -2.7526 | -51.7491 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89a05ae0-6201-3454-ad15-3ba9711d55ca | -1.6973 | -52.629398 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 236136ae-da07-3f25-b953-60ba53281984 | -4.5312 | -45.692799 | 2024-12-01 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00a7e87e-9f51-3236-93ce-84a74adb6ad7 | -4.1971 | -50.672501 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf127e41-1345-38de-9bc8-64c6ef63a12c | -4.2006 | -50.687901 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee59498-d61c-30f1-bac2-64783ee4918b | -2.7507 | -51.740799 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b641e3a5-5448-39f4-b9d7-96cd64dfbe47 | -2.9751 | -46.948399 | 2024-12-01 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae4e80d2-7d28-364b-89bc-14519e54e8ea | -1.6681 | -52.094398 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5bf034c-9e6e-3c45-85d6-440fd81a4cd8 | -4.6541 | -49.7332 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 353f067c-7d0a-370d-88ff-efcfc1e893f8 | -3.6673 | -50.242699 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd97103a-1887-3329-95ee-965971cb22b9 | -3.0354 | -49.503601 | 2024-12-01 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b553a07d-731c-37fa-8d8c-9d73bb9d3354 | -4.6191 | -46.471901 | 2024-12-01 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 611aaa28-a949-3615-975e-b77860350316 | -3.7484 | -50.0555 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25503eaf-74b0-30bf-aefa-6e881586727f | -3.219 | -45.772999 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b911ee80-72cf-3c33-bc1b-c4c813e53b14 | -2.134 | -54.870899 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4fc4a1f-3254-3431-9846-53b8a34ec81c | 0.9392 | -50.206299 | 2024-12-01 00:38:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2e469649-1366-3ccd-bfc9-3f30f6cc12da | -1.2763 | -51.731201 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 493fd489-bab8-3fe2-a40c-972972ae0b55 | -4.0687 | -49.062099 | 2024-12-01 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee47e26-bec6-3cbf-a0e0-968644b789b5 | -3.2154 | -45.7575 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30413346-8e2d-3a40-aef8-f5e33070fe9b | -4.8162 | -47.326099 | 2024-12-01 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffae5671-c858-3d8e-8f91-28963243025c | -3.5566 | -48.670799 | 2024-12-01 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeec9751-5ec2-3ebe-bfdc-e02a0ae4c497 | -3.8213 | -46.5467 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51d329e8-5290-366e-bf78-5b39df49c3d8 | -1.2481 | -51.7883 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98b65218-f936-39ba-99db-130aaa5e7d5b | -3.0922 | -53.2519 | 2024-12-01 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05e38ce7-3831-3b3f-9ed4-733cd42f6ba3 | -1.4818 | -52.676998 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e327e452-df31-3615-b10c-7f6d644be97d | -1.5973 | -52.280602 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90519ada-fb2b-3b65-9b24-c5fef80e3184 | -4.4946 | -48.217499 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb0cd3e9-72e3-3c3d-8875-c76186b236d5 | -3.4536 | -44.919998 | 2024-12-01 00:38:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8219e7be-91cb-35f7-980c-4b559d3fe908 | -3.5846 | -45.083698 | 2024-12-01 00:38:00 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fe083354-4cd2-3f35-8d19-7192d330c5cc | -1.7169 | -52.625099 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d273486-8f0a-3c84-94d0-3006be69d887 | -2.5537 | -45.617401 | 2024-12-01 00:38:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5aa1780e-c646-3832-a6fa-3d33e3cf7103 | -2.6124 | -45.4258 | 2024-12-01 00:38:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdca517e-c9a6-3c6c-8d29-60aecae36255 | -2.8855 | -54.1577 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9992fc1-94c6-3337-8193-ebd5f47c8569 | -1.2304 | -51.800701 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1c11f4-9660-3b7f-84ae-f4bfe9b8fe6d | -1.1881 | -51.750702 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb563b02-ed27-3231-b0ce-cb237bca882b | -3.1228 | -45.9809 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a24d0163-7d18-3418-a116-c3f9f4c48531 | -4.5597 | -45.726299 | 2024-12-01 00:38:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3a9f12-c24b-36e6-8d36-1d3e1e3d87b9 | -1.1557 | -51.6991 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244ab2fc-5709-3c0f-a382-6d91228678c0 | -1.9972 | -52.093102 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 597e326b-a1e6-3d4b-a886-4e2806f71f6c | -3.2804 | -50.625999 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 120e3913-9e13-3931-87c8-cfe43436b224 | -2.1438 | -54.868698 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a7cf84-bd0c-3063-b5ad-29494885f537 | -3.7944 | -48.0877 | 2024-12-01 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee3e921-1a05-3f67-a70e-33ddad6eccd5 | -1.2058 | -51.7384 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc177175-3afa-3f81-9d45-33477877d4f9 | -3.8885 | -47.061298 | 2024-12-01 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08fff37e-e891-3f4f-9b90-8008436ef16a | -4.3019 | -48.231899 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3757307c-5b45-3178-9db3-818e12a6d15e | -4.1029 | -49.076302 | 2024-12-01 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44d115cd-7562-39ee-a314-fd4eee5f204d | -1.0702 | -53.2178 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad428c4b-fc7e-3aae-91d6-127119477b0c | -4.7472 | -43.7089 | 2024-12-01 00:38:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23971b37-8feb-37e7-a890-e34ec7b5388f | -3.693 | -43.435299 | 2024-12-01 00:38:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ddf92b5-7d37-31c0-bb56-bf15a5da387c | -1.1979 | -51.7486 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0651c81e-5dde-317d-a65e-18209195e02d | -1.6993 | -52.638401 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc8de5dc-bff7-3f5b-aa36-0aca05a45e19 | -3.6855 | -49.009499 | 2024-12-01 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5a8dc6-135d-3d10-9740-ef1dae43d096 | 0.9557 | -50.224499 | 2024-12-01 00:38:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
