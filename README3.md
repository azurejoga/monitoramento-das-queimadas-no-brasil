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
| 390f0c9b-a0b6-3f8c-9ae1-4fb413e26d06 | -6.42212 | -53.36868 | 2025-08-07 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 18bbbb77-7071-3148-8150-63573fe7b8b5 | -6.64434 | -58.82343 | 2025-08-07 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8c08a0af-4e20-3377-9776-72f97dcea191 | -5.8818 | -57.75043 | 2025-08-07 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 383e69c0-59ed-3f00-8841-2adb67db7b4a | -6.76122 | -59.47422 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b91d8555-588c-3085-a0a1-8e9c24a7e2fe | -7.40695 | -60.02146 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f2957957-0ba3-3c00-a0c1-86be73800dc8 | -7.40531 | -60.00937 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 220.0 |
| 14bdd4ba-0c3f-3154-a56b-b5c0b3e5ffc8 | -5.87287 | -57.75173 | 2025-08-07 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62c0e6c5-88c3-3a05-bb47-5c940cd84c81 | -6.55187 | -56.19918 | 2025-08-07 01:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 956d2249-1241-3265-8350-2222c883f302 | -11.7699 | -48.18 | 2025-08-07 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 35646c52-404a-35db-9963-4a1ad7487e2e | -11.7804 | -47.536 | 2025-08-07 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 39a34408-4e36-341b-b426-8f6e5b7e58b2 | -8.9041 | -60.5577 | 2025-08-07 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 227b0fd2-ea57-343e-962c-aaaa3738ef26 | -8.9212 | -60.7681 | 2025-08-07 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 5f5613d7-cb05-3bef-b424-2c50f393dff1 | -8.9213 | -60.7489 | 2025-08-07 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 225.4 |
| 79f11a2e-a35c-3f50-8aa7-e6f380a33490 | -8.5214 | -43.2828 | 2025-08-07 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| e3ca4069-1d71-32ee-a33f-761a458f0b31 | -10.6441 | -44.7413 | 2025-08-07 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 2035ecfb-5578-3aaf-90f7-58afa4a5b075 | -7.4076 | -59.9916 | 2025-08-07 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| cb5627b1-a9c3-392c-8580-6574f41b039f | -11.7508 | -48.1825 | 2025-08-07 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8fdcbdb1-5620-3280-b4ba-5e4c8413391f | -8.9215 | -60.7297 | 2025-08-07 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| a5be7dd4-6260-3d66-9370-21850d32f51e | -8.5211 | -43.3063 | 2025-08-07 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3bfc720b-6413-35d0-8bbd-6e5feb0d2273 | -11.7995 | -47.5334 | 2025-08-07 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b29dce0f-f6bf-3f09-84ac-9e65b24c8dee | -8.9042 | -60.5385 | 2025-08-07 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 547e8e84-9a3f-3e89-ae09-271f95bd0ae0 | -7.4074 | -60.0108 | 2025-08-07 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 09399fbc-4dd5-3ec5-b92d-c6d76cbf4883 | -10.6441 | -44.7413 | 2025-08-07 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a0ad823f-0601-3b19-a77c-1e917da1d759 | -8.9041 | -60.5577 | 2025-08-07 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0f48eb34-6d77-3aa3-a216-8f01c5548db5 | -10.6247 | -44.767 | 2025-08-07 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 53c09404-913e-3a90-a615-248f619ee39a | -8.9215 | -60.7297 | 2025-08-07 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 7d9c8975-52b5-3ae6-80dd-d379a391fd54 | -5.822 | -46.2035 | 2025-08-07 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5f8b6e58-1040-35d9-b8fb-311f9f450b82 | -8.9399 | -60.7481 | 2025-08-07 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e9527299-92bb-3df2-bf88-a1ee7d1fdc1b | -7.4076 | -59.9916 | 2025-08-07 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8851ad58-7747-3ecc-b5c2-40d0451744b0 | -5.8218 | -46.2258 | 2025-08-07 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| af35adbd-2189-3c8d-b4a6-d9ece0e0be73 | -7.4074 | -60.0108 | 2025-08-07 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.5 |
| e0b9001f-f88e-348a-98e0-6ccb4321b10c | -8.9213 | -60.7489 | 2025-08-07 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 7f33f68d-cc39-34a9-ac6f-c5b57d90c723 | -8.9212 | -60.7681 | 2025-08-07 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d8a0e229-835f-348a-91c0-0611332fc10f | -8.9028 | -60.7498 | 2025-08-07 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 65a6793e-68e2-340c-94e7-7f5433632c83 | -5.8031 | -46.2271 | 2025-08-07 01:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| a89c74cf-bef1-3589-b0ee-4800840f4ff8 | -8.5211 | -43.3063 | 2025-08-07 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| d7aa7215-0916-3242-ba04-6a14b26e817b | -7.389 | -60.0116 | 2025-08-07 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e66ccb8a-43c0-3d67-9d0a-839de4896dd9 | -10.6438 | -44.7645 | 2025-08-07 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ae48fc1f-bbd3-3aaf-892c-fa55e3c72671 | -11.7699 | -48.18 | 2025-08-07 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| faadd038-a21e-3701-b411-dbb96dced723 | -11.7508 | -48.1825 | 2025-08-07 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 95d14a63-b7dc-3988-abd5-d498d5db76e7 | -9.0835 | -45.0499 | 2025-08-07 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 497c9d66-82c9-3a7e-bc4d-8f0f1ee8b10c | -5.822 | -46.2035 | 2025-08-07 01:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 2134b614-7fb2-3f51-8987-c7de70059c6f | -8.9041 | -60.5577 | 2025-08-07 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 926778cf-9c87-38af-950a-c4f925368752 | -10.6441 | -44.7413 | 2025-08-07 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 86ecd2fe-b320-319c-a6b8-d1a9e077795b | -8.9213 | -60.7489 | 2025-08-07 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 192.1 |
| 8078b4a6-e1bc-37a5-9eeb-1fd5c41c7bd7 | -8.5211 | -43.3063 | 2025-08-07 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d5c965cf-78bf-3880-b477-09a3ea6c82eb | -8.9215 | -60.7297 | 2025-08-07 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| add664de-68e4-3838-adb7-18b4aeb5f1b8 | -7.4074 | -60.0108 | 2025-08-07 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 8890f68a-0b7a-392d-b378-487b3676ab15 | -9.0835 | -45.0499 | 2025-08-07 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 28e95c43-8fea-34cb-b9c2-0f88b6416129 | -11.7699 | -48.18 | 2025-08-07 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d1d07186-3c7d-39f3-b1de-80b032f1b267 | -11.7508 | -48.1825 | 2025-08-07 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 3a4a5a20-0228-3d04-b406-79436f31953a | -5.8218 | -46.2258 | 2025-08-07 01:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| c157c352-05d5-3ea9-bd29-5a4d71af3145 | -8.9028 | -60.7498 | 2025-08-07 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 13d680ce-b102-3d46-a01c-cfb5bb184653 | -8.9212 | -60.7681 | 2025-08-07 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9d501079-2088-31f9-ae19-e81f4aad422d | -5.8218 | -46.2258 | 2025-08-07 01:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 38e7eb8e-5ccd-3f3f-9e32-4c1a8a44a8b0 | -9.3626 | -40.328 | 2025-08-07 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 6575a44d-72c2-38bc-9910-1ace83ef0915 | -5.822 | -46.2035 | 2025-08-07 01:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| ec8d93be-ef86-3cdb-bb43-bae4c702f884 | -8.9212 | -60.7681 | 2025-08-07 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5e161dcd-a6e5-32b4-aaf8-f77e80a74997 | -8.9213 | -60.7489 | 2025-08-07 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 448b147d-03a7-3c54-bbf3-6c67b3f88897 | -23.7017 | -51.6543 | 2025-08-07 01:40:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.2 |
| ca566fe8-fe87-39d3-90ed-d3aa013da118 | -11.7508 | -48.1825 | 2025-08-07 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3a0b9890-74dc-389f-90b5-d24417091b46 | -8.9399 | -60.7481 | 2025-08-07 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 70699ae8-5db9-375d-a06e-dd3b8d326b85 | -8.9215 | -60.7297 | 2025-08-07 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0b5f6216-4ca9-3e11-a462-4c2d3e9a2350 | -7.389 | -60.0116 | 2025-08-07 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7e86aae8-6d9a-33f8-b236-e894f79d6b3e | -7.4074 | -60.0108 | 2025-08-07 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| a374ff80-8047-3013-a4ea-c35d7678ec44 | -11.7508 | -48.1825 | 2025-08-07 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8d185148-3803-383c-9c30-203d6ba709f1 | -8.9399 | -60.7481 | 2025-08-07 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3d26ca2c-eb9c-37f1-bad3-db0f1a925a7f | -8.9212 | -60.7681 | 2025-08-07 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 58fb04ac-9f09-310f-95b4-5a53a7a90098 | -7.4074 | -60.0108 | 2025-08-07 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 06082e6c-470d-3dfa-a59c-be9d4bff35a5 | -8.9215 | -60.7297 | 2025-08-07 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f1f812d8-f6d7-31b7-a6cf-8832ec4f8e82 | -8.9213 | -60.7489 | 2025-08-07 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 95cecaca-20d6-305f-88b1-6528cf11b502 | -7.389 | -60.0116 | 2025-08-07 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f7d47b19-2990-3576-8f66-69b25b6cf44b | -11.7508 | -48.1825 | 2025-08-07 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 8627353f-6259-3259-932a-5598c1a3d6bb | -9.363 | -40.3031 | 2025-08-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.4 |
| af5a076b-d967-3bd2-9dab-8cedf8d7739d | -8.9215 | -60.7297 | 2025-08-07 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 07bad8b2-7675-316e-99b0-5723f0da9d99 | -8.9213 | -60.7489 | 2025-08-07 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 1a7c10ef-6ce4-37fc-8c90-a5f10ae3a104 | -7.4074 | -60.0108 | 2025-08-07 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 1735972d-497f-3409-835c-e02422f45321 | -8.9399 | -60.7481 | 2025-08-07 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4057ee11-4e3f-37ac-90e9-73831a20ff61 | -7.389 | -60.0116 | 2025-08-07 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3540fbb3-028b-31f7-8905-d35844d7b116 | -9.3626 | -40.328 | 2025-08-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 832a6d4d-6e9b-3099-89c4-41538135c047 | -8.9028 | -60.7498 | 2025-08-07 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0281b2d0-cfd0-3ea0-bbfd-ecc1f50a9065 | -8.9213 | -60.7489 | 2025-08-07 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 0b7e58d5-e053-3889-b89d-ddacd08977a9 | -9.3626 | -40.328 | 2025-08-07 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.2 |
| a94810d6-49d1-33f0-b0a6-a49d08eae0b6 | -8.9041 | -60.5577 | 2025-08-07 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 681c1988-d2a6-3d9f-bda6-7c7af9e6c9e4 | -8.9215 | -60.7297 | 2025-08-07 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a6c12fba-0169-3ec5-8b40-16b153cf025a | -11.7508 | -48.1825 | 2025-08-07 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 38d261d7-6e3e-3e46-a8bc-65afd3982261 | -10.6441 | -44.7413 | 2025-08-07 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a63871f8-abe0-32e4-b012-4a94c1aa6ef8 | -8.5211 | -43.3063 | 2025-08-07 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5f55a4ac-de25-3585-bfb4-7331d40308c4 | -8.9212 | -60.7681 | 2025-08-07 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ddedd47a-aae2-319a-b87d-9cc6aaac1566 | -10.625 | -44.7439 | 2025-08-07 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| a09c0e17-d2e5-3492-b359-71187c0ac647 | -7.4074 | -60.0108 | 2025-08-07 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 2197da62-4929-3b1b-92d9-fced8e2e95d9 | -10.6438 | -44.7645 | 2025-08-07 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ddde563c-73e6-3491-9043-fe931ff4b4c5 | -10.6441 | -44.7413 | 2025-08-07 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 85d5f95b-b34b-3a82-85a0-c7fc83612bc2 | -8.9212 | -60.7681 | 2025-08-07 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 041c8898-dbbe-36c2-8111-0f85d57bd5a2 | -8.9213 | -60.7489 | 2025-08-07 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 178.6 |
| ae848cb2-cd9a-3a57-b3c7-2038746f3b02 | -11.7508 | -48.1825 | 2025-08-07 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b62a422d-874a-3c25-9d28-889dec0cedcc | -10.6438 | -44.7645 | 2025-08-07 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d5350264-1cb0-30c2-9f87-d6ab717dc52f | -5.8218 | -46.2258 | 2025-08-07 02:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| ea71249a-f6e7-3a2d-8cd4-8646c01bf7e7 | -8.9041 | -60.5577 | 2025-08-07 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3cdcf3dc-9f6d-371b-ab2d-dd0e4d39cdab | -8.9215 | -60.7297 | 2025-08-07 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |


[Clique aqui para ver as próximas entradas](README4.md)
