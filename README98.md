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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd6b90b7-6133-3314-a3b1-6d7edced4416 | -12.30934 | -50.57617 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| b08969b7-cf83-36af-8479-5c05fdb2ac20 | -10.46405 | -46.18239 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8a349bfc-6835-3874-a8bf-7df8b92edb8d | -10.92815 | -46.62113 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c8e8aecd-4f28-32d5-adb8-f0dbe5a6a103 | -9.49762 | -37.0003 | 2026-08-28 16:07:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 07982b3f-2efb-3104-a07e-bac7caa66a73 | -11.65289 | -46.72607 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6ab47afa-e084-3ba6-95bb-cfa4128d985c | -9.87749 | -45.85174 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 96d8bf9c-724a-336e-948c-a54f4317bd1c | -5.44651 | -47.53831 | 2026-08-28 16:07:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dd4b3615-875b-36b1-99a7-06c69a2ce9f2 | -10.54864 | -46.2531 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55a91c0e-64ce-3f64-ab23-9f4c3c3d2d92 | -4.1481 | -38.45937 | 2026-08-28 16:07:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 57fe6b87-bd29-340d-bfcb-a4b2cae6f0a8 | -10.5525 | -50.41324 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c3e0c903-3a45-3ce2-949f-cf887590de3d | -9.84554 | -45.84673 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a149a87-c9d6-3a7c-addc-691a3b965241 | -9.4976 | -45.62947 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee0fb0e7-fbf2-3e3b-8d39-5c2429937d4e | -11.25239 | -45.04507 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d45175fe-d168-3fd0-a000-83258664c196 | -10.06783 | -46.96267 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b784f5a5-5aae-319f-834a-82aeb68bd96c | -12.06606 | -47.15313 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 07e899db-1a39-3166-aa5d-66dd4f4ac78a | -4.64063 | -43.04959 | 2026-08-28 16:07:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1f1f4111-72ee-36db-ad08-5e9763cce951 | -9.49983 | -45.64698 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2ac84b1f-af8b-3524-b2ad-b4914f5258c3 | -10.8967 | -46.64326 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3b6bdd37-df13-33a5-bbf8-01a7d6aaa2d5 | -10.46891 | -46.1783 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| be9951a0-3325-3326-ae25-93ef2e14fa65 | -2.08309 | -47.77748 | 2026-08-28 16:07:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aad88b12-3248-3d88-b7cb-914daa3d711e | -11.58239 | -45.52421 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f3b07675-9d3c-3d6b-af79-c4251eefeb43 | -11.81069 | -47.19425 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5df04e9c-e5d7-3240-b23b-b357b92c29f7 | -5.49049 | -45.62143 | 2026-08-28 16:07:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 28060db4-6d9a-3891-b1b7-51aed8033468 | -2.08392 | -47.77687 | 2026-08-28 16:07:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cfd8e56-d428-3be5-a9ee-6d93b7f1d009 | -11.54366 | -48.13304 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3c2bb39c-7d98-3a8b-b677-e9d871dff1fe | -12.2661 | -50.54217 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 27f2e45d-fc9a-30d2-b170-e56d57987fab | -11.76965 | -47.65325 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 319f00e0-156b-3f42-8543-66911c2d88fa | -9.88145 | -45.84189 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 938d4b96-9e6d-3a34-ac7f-7824cbaef065 | -2.58317 | -48.16759 | 2026-08-28 16:07:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c25f13f2-2748-315c-adb1-0be342fc621e | -12.32838 | -50.58525 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 448a246e-d69c-3dfc-820b-7c72bf1c4b38 | -12.08434 | -47.15932 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0577026d-194c-36c2-ad99-0977f206f375 | -10.0729 | -46.95821 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b3d36e3-ccb1-3885-8d2b-3619e0ef1d8a | -9.86487 | -45.83457 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d14ec1c1-f48a-36ef-aa51-ddd96970d117 | -3.96126 | -43.11639 | 2026-08-28 16:07:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4abce8dc-40d1-3d88-8809-ea599d694366 | -11.16733 | -45.05803 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bd6654c9-738b-31de-8802-f5e2bf89759c | -11.66447 | -46.72808 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44f1cb05-ca4b-3c41-ba43-cc1b71d4c8a6 | -10.32707 | -49.9852 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 2ca10917-8cd7-3197-b91b-a58e236881aa | -10.33451 | -49.99046 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 8e2d7459-cd7b-30f6-b138-cd2d59bda917 | -1.69566 | -48.59561 | 2026-08-28 16:07:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3b1edb65-7cf5-392e-9e60-f54bc17d0a11 | -1.76859 | -45.23345 | 2026-08-28 16:07:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 26d2d251-1a27-3aad-9f42-117d03568674 | -1.61692 | -48.10285 | 2026-08-28 16:07:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 93bec7f5-200e-357a-a9bd-e80294c990ed | -1.30849 | -47.90746 | 2026-08-28 16:07:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b116e46-7908-3033-8269-8fa16b99cc37 | -9.88816 | -45.85358 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0ad924b6-665a-36a7-81c1-960ccaad2aab | -11.77569 | -47.63285 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| fc17ca85-63b3-3da5-b139-267f8b0b5de7 | -1.83722 | -44.68511 | 2026-08-28 16:07:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 337c1426-80be-3170-a175-7703e96bb424 | -10.07699 | -46.94613 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e022a1f0-beb5-3970-9ef1-46a33af36683 | -10.08423 | -48.69033 | 2026-08-28 16:07:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 091c2228-1d0c-3c8e-bfc1-6804da1f5eb8 | -11.57725 | -45.52492 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 817bf610-84c2-36da-ba3c-ffe984fa52ad | -11.34991 | -48.39144 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 93ca8a53-6f35-3921-9ed2-3a707efa3a1c | -10.54064 | -46.24561 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e8a5efdf-2188-356d-88a5-18d7ac437641 | -9.87273 | -45.85541 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87eb505a-5f62-3057-851c-c40476aeaca3 | -9.83214 | -46.33505 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eca3a745-aff9-3904-9c86-78c84b443e64 | -3.68199 | -39.34177 | 2026-08-28 16:07:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05c34daa-98fb-3fea-bff5-6eca919adca6 | -10.46363 | -46.17905 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b04951f2-2adb-356e-8d41-f32e34585f1e | -12.31566 | -50.60088 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 1b74c43a-3979-3387-8710-7a45a280a081 | -1.6499 | -48.63015 | 2026-08-28 16:07:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 679750aa-05ee-3c32-9eb5-0fdddeb43178 | -1.52289 | -48.32314 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4e671269-9844-3c30-80af-ff8a48b08ebc | -10.54625 | -50.47934 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1a57443c-c384-34eb-84c7-813f594acf20 | -9.89323 | -46.3487 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 79760ff5-21fb-3ae5-98ab-76f7b9d76176 | -1.56543 | -45.11557 | 2026-08-28 16:07:00 | NOAA-20 | APICUM-AÇU | MARANHÃO | Brasil | 2100832 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 16b1f692-2ff3-3c60-a873-d1b246670fae | -1.83102 | -48.41161 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| edc5025a-d63c-32d5-9950-da59190ff1bf | -11.84409 | -47.22785 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e5546aa3-be40-32ae-926c-229749d06564 | -11.77306 | -47.63037 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f0809fc2-7577-34ac-8209-d808be3b9d38 | -10.00723 | -39.16198 | 2026-08-28 16:07:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 9a3c39f4-dcb4-37a9-bea7-07bba3c6fae3 | -12.30393 | -50.55939 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e8c90003-8c77-3bb2-8ee1-bd943fd0c226 | -11.2538 | -45.0565 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4ff31b80-7a1a-370e-bfe6-79d4e4a620a6 | -12.14985 | -50.63864 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e52b2df1-be06-3933-b8d6-5ef30339c4dc | -11.66313 | -46.7285 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f35fb50e-139c-3226-92ef-01f50a32f9d0 | -9.50675 | -45.66115 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ecb25be6-86c5-32b9-8bc1-d8343b455516 | -2.72826 | -47.04025 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 47df286a-f54e-3462-8391-e0852d598352 | -9.88224 | -45.84808 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d78b3059-880a-3c7f-a920-996b6d7cc622 | -3.26791 | -42.98282 | 2026-08-28 16:07:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a1a33e50-d781-30f3-a7b9-bea6b6e3c9f3 | -11.79591 | -47.6722 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 255864b4-6a1f-3df2-bbd7-bf3955cc1296 | -10.01833 | -45.63187 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ba7a1b63-1960-3a27-a301-940e552152b5 | -2.72369 | -47.04387 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 13573b1c-351f-3939-87c1-3c692c3bff82 | -10.33451 | -45.36053 | 2026-08-28 16:07:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| aa5d539b-3037-3611-9c65-da4a2d4ec431 | -9.88765 | -46.34724 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7ae565a0-d691-3cc4-9306-cb27e43127b5 | -11.24251 | -45.04665 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ca9a0490-7b75-3a60-a5d3-90b42bbd4faa | -10.91632 | -46.62218 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e4f3c61d-2d02-3c81-a7bf-7e96e8055217 | -9.72649 | -45.81464 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2332f6f7-1851-36dc-af00-31c238e80521 | -10.47416 | -46.17725 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ac2769a1-cd3e-3cf3-bbf6-fb53f9155359 | -9.04845 | -40.29989 | 2026-08-28 16:07:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3106575-bbc1-3c45-9c29-9fa050a14ef2 | -12.32578 | -50.59578 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4216f50b-2439-3b1a-85c6-7702c8b48e40 | -10.32709 | -46.74883 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9794eb2f-72b4-3c23-9086-e8c55b56dc22 | -11.77607 | -47.65675 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b842e72a-f7aa-37ae-962e-0ba2e27f9237 | -10.924 | -46.63289 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b8b78379-1a96-3a2e-adb0-aea3a6079a32 | -11.46981 | -46.94224 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a7706883-2928-3f9b-8865-6af31c38138d | -2.72502 | -47.05383 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 5d13e776-62ba-3bb1-b7df-c08580951530 | -10.54691 | -46.25264 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ba3c6e99-4bab-3ff1-ab5f-c6c26438ffd1 | -11.24388 | -45.05779 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| af8a28da-4d09-3544-8259-74c14ea4e81d | -12.31224 | -50.60443 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 4e07ed17-f90f-3ab2-b133-ed3364362760 | -2.72335 | -47.04222 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 59f64925-ef5d-3570-af29-215e4edd67de | -11.34184 | -48.38103 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 15b5f832-2022-375a-b91a-76bdbe5eef26 | -11.24884 | -45.05714 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f8633aa3-96b0-3afd-92be-f840c3338703 | -2.9073 | -44.04645 | 2026-08-28 16:07:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbdbcd84-d369-3ce5-b7b9-fe87d0f13713 | -11.65246 | -46.72258 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5b90cbcc-4f2c-3545-8c77-9d4297c4c29f | -9.22824 | -40.56452 | 2026-08-28 16:07:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0c923374-c343-3131-8eb5-b97dbe7250d6 | -10.08128 | -46.97962 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e304f88d-ec8e-3e07-bf71-1ece7ca39ec4 | -12.32359 | -50.57462 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c4bf6d8f-322c-34cd-96ee-e59dfa5f0534 | -2.23309 | -50.52782 | 2026-08-28 16:07:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |


[Clique aqui para ver as próximas entradas](README99.md)
