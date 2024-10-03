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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 060e4a5b-8b50-3ea6-8daa-cd6040890ca7 | -9.2719 | -67.604599 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4f0440-9c17-3349-ba42-dcf2e788f18c | -9.393 | -68.151001 | 2024-10-03 01:51:17 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 54764d6a-4ec6-3f18-ad1f-a8ec6ab3dc8c | -9.2559 | -67.579002 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85943f47-1caa-3efa-b33d-a24b4d3ab462 | -9.2575 | -67.585899 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98e8acbd-81d5-39df-b66b-c481b8074f4b | -9.259 | -67.592903 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d38eb5f8-2161-3f4a-b636-133a6b6e152e | -9.2605 | -67.5998 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bb0256d-1825-3849-81cd-52a9945dce95 | -9.4603 | -68.503403 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cc01b1e8-4a9d-34ba-aa58-78dbc2e2c741 | -9.4619 | -68.510597 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0378d2-fdaa-3c50-a154-9259a3de9b6e | -9.3938 | -68.247704 | 2024-10-03 01:51:17 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c7b6757c-8a8f-3c0d-9016-fef21081ea28 | -9.3954 | -68.254799 | 2024-10-03 01:51:17 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 47e7c48c-1004-3fa5-9cce-ac0a31f469a0 | -9.3934 | -68.292503 | 2024-10-03 01:51:17 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa517f9-ab3f-39af-9b5d-9618c4862d9c | -9.395 | -68.299599 | 2024-10-03 01:51:17 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb2f4cb-6912-3126-be87-0e8fb8df5aba | -9.4487 | -68.5438 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ed587c63-ce61-336e-a01c-903e8af6d7dc | -9.367 | -68.313301 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f79bb499-d8db-32bc-8a0e-665afa14fe76 | -9.1648 | -67.308601 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd27ad4-2101-3cbd-aa66-b92d6399175b | -9.1664 | -67.315498 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 319517f3-bf47-3880-979f-cdc6818d75cb | -9.2776 | -67.8153 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d02a2ee5-81b2-3a3f-9ff4-87e050d45062 | -9.2791 | -67.822304 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f928184-2f00-30c7-8bd8-b752f5bd540b | -9.2807 | -67.8293 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e44bcd9c-fee0-314b-8dae-578fa055f417 | -9.2822 | -67.836197 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2098c90f-31b9-3c9d-abde-dad42e4929c6 | -9.2838 | -67.843201 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 402c2c19-8c21-30ea-8189-f5acc5d7755f | -9.3601 | -68.188103 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1941b5-ebc1-3f91-94b2-b8dd70c0c7cd | -9.3617 | -68.195198 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ca557fbc-a110-3b85-8c52-f6866d6b3dc0 | -9.3632 | -68.202301 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| de2249d9-9cc1-379f-aca0-a85fa41031b8 | -9.3915 | -68.330399 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 77a77d3a-4f73-354b-abcc-6ea37867c2cd | -9.2244 | -67.622498 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9148aa38-1c93-3ce4-b342-5416b46e655f | -9.226 | -67.629402 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5ec5ef-6142-326c-a251-1ef1badf2415 | -9.2647 | -67.803497 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da2347ee-3e70-3df1-877b-a66027a9f266 | -9.2662 | -67.810501 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78fd6be4-1cb8-3c29-8dc9-2cff9c50cf0e | -9.2678 | -67.817497 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12cc6aad-4703-3db9-afce-c2dbf582f6cd | -9.3503 | -68.1903 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0445c009-ae89-3dfd-9ec3-77339d807527 | -9.3519 | -68.197403 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 76595706-0f81-3e8b-ab3e-af5e2ca80ec2 | -9.3534 | -68.204498 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cec519b7-5d5b-38c1-ac1c-4d9ecf6e43a6 | -9.3785 | -68.318298 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ee7977cc-9cb0-3484-969d-b83009e48e3e | -9.3801 | -68.3255 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 15709296-0f7f-313c-9b0e-25ec97be66db | -9.3816 | -68.332603 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e9949105-6489-3e58-94c4-f53f6053c791 | -9.2549 | -67.805702 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d56d78e-eb13-3cc7-8804-a36f8091b6d4 | -9.2564 | -67.812698 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f067ffb0-dcd8-314e-a05f-7f41870bcd92 | -9.258 | -67.819702 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9554abfd-c3fb-3f85-a46d-dfe5e118ed3e | -9.2688 | -67.868599 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9722fafb-518d-3cbb-a603-f1bf4e51c781 | -9.2704 | -67.875603 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca7f0cd-1bf8-383c-8cb2-0e7e1392bf3e | -9.2719 | -67.882599 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89838af2-b93b-3ed2-a0b6-d8cba3d2cff7 | -9.4271 | -68.586502 | 2024-10-03 01:51:18 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e8eaae22-d685-37a5-ae81-f82e2e157206 | -9.2435 | -67.800903 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfe94929-b685-3118-a257-c0d7885df093 | -9.2451 | -67.807899 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce10160-03f7-39a9-a43b-89d35e069095 | -9.259 | -67.870796 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a77aa5bb-faea-3055-9459-05675188d0e7 | -9.2606 | -67.8778 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5b7d077-f95a-3d85-8d46-295b2d06064f | -9.3353 | -68.216003 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f230a7e6-d6bd-340f-a9e3-f79a56b4adda | -9.3369 | -68.223099 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e8af51c4-4a71-32c0-a6d8-2fe957aca26a | -9.2058 | -67.677803 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13d0258b-2a94-33de-9bea-998ba643f7c7 | -9.3208 | -68.1968 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 40fc10c5-2552-3209-a438-e36f6999c47b | -9.3271 | -68.225197 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a5f568b0-4a9a-3092-b375-7d2eb4f07e2d | -9.3286 | -68.2323 | 2024-10-03 01:51:18 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9502f0e8-e668-3451-833d-8cb2316980cc | -9.2162 | -67.7705 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd5c884-04fd-33cd-b78b-06c8d3ed231b | -9.2177 | -67.777397 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d91c17ee-beef-3997-8013-2003b87c0e00 | -9.2239 | -67.805298 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1d5a243-3289-37a9-8127-14a0d28e3d63 | -9.2255 | -67.812302 | 2024-10-03 01:51:18 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c73d191-381d-339c-ba32-3edc494b5c80 | -9.1156 | -67.457603 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 336d22cc-2fd7-3bd9-86de-10f11e4855b5 | -9.1172 | -67.4645 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c62fc405-5fd1-3d52-9069-73c050792023 | -9.1805 | -67.7491 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 242f27fb-112c-3f6c-a411-4edbca8415a5 | -9.1909 | -67.842003 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| efc1bfdf-838f-338e-9aed-4a71ec730a2f | -9.1924 | -67.848999 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f805d39-c4cb-32fd-b3ed-31ea7ac9d722 | -9.094 | -67.498802 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad9977e9-1dbe-3cac-8dd2-73ad202175f0 | -9.0955 | -67.505699 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b079e30-fe9f-3cb7-9949-dd82b60d89f7 | -9.0971 | -67.512703 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0ee3d56-28b8-3fc7-aea2-88631bcad307 | -9.1032 | -67.540398 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 560a64a9-d917-3c5f-9fc7-cd64edc087e0 | -9.1048 | -67.547302 | 2024-10-03 01:51:19 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b242886-f456-3cc6-a1b6-1ca45fa65ac4 | -9.0919 | -67.535599 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b08122ea-b0e5-36fd-a7b7-7842bbd29f2e | -9.0934 | -67.542603 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd43da68-0039-3806-a981-08346d1a3977 | -9.095 | -67.5495 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c37edb5b-a07a-3461-89ac-1a1d3d5c5014 | -9.0965 | -67.556396 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02c546a9-2ea4-3f55-8e2a-677a49f15464 | -9.0981 | -67.5634 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 304fe243-febb-3cc9-8357-7fcfd4b3068c | -9.0883 | -67.565598 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd8e9ce-ce37-35de-bdf2-2278006705e9 | -9.0898 | -67.572502 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f201be7-4463-3358-be74-9a547075c060 | -9.2201 | -68.159798 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10a50c70-82e0-380f-b4c6-acadf3cfdcd1 | -9.3576 | -68.785202 | 2024-10-03 01:51:20 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 03508ae8-9a60-3ba6-8f6b-2bfc48d85f47 | -9.3592 | -68.792603 | 2024-10-03 01:51:20 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| dec23e03-423f-3733-af15-123fff65629d | -9.0769 | -67.560799 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1842afda-c520-3a44-a724-3c78ab6bb9fc | -9.0784 | -67.567802 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2124248-fb3d-3bd5-a296-6ed1153de6b2 | -9.08 | -67.574699 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc03ecbd-aaf1-38df-948e-b20e5ef2beac | -9.0815 | -67.581596 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1acd044-0160-37e5-bac6-6132940d7a0d | -9.083 | -67.5886 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd2a73e3-4701-314b-867d-57a5707db4d5 | -9.0846 | -67.595497 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0de8224b-68af-35f3-b717-0d77c80b7f50 | -9.0532 | -67.500702 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad88620-36ae-3a37-b8b2-198df2489ac3 | -9.0717 | -67.583801 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e65cc8c5-eebc-3711-abc9-b87e4e9e7bad | -9.0156 | -67.378403 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcd07f2-508e-318f-89a5-16f57319d28d | -9.0403 | -67.488998 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7883842-7eec-312f-b985-84d070a5b80e | -9.0419 | -67.496002 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad058345-d1c1-3c38-ae24-1c4a5b051178 | -9.0773 | -67.655403 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8d30933-659d-365a-b1fa-5ce20360f11a | -9.0789 | -67.662399 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01e219d7-eaea-3992-8517-2d638ab9ebcf | -9.0804 | -67.669296 | 2024-10-03 01:51:20 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0aa6f9-6507-3a8b-8bd6-0eefaafec564 | -8.9883 | -67.348297 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 879b08b2-4ba5-32ac-afcf-49f90035a2d8 | -9.1867 | -68.241501 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bcfba540-0261-3a1f-a983-4ccbd902eb1a | -8.9878 | -67.391899 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 284b8fd6-9416-3c41-98db-3ab391db1e99 | -8.9893 | -67.398804 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4d67613-0884-3f97-a6b2-a048395ad1b1 | -8.9909 | -67.405701 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0c261b-fb6d-3da9-8784-72f9fe3410dd | -8.978 | -67.394096 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd0c9dd-c8c5-3c0f-acb6-644a9a77f4dd | -8.9795 | -67.401001 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 599554b9-80f7-325a-b164-b85b1db90d43 | -8.9811 | -67.407898 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9abf2b-4594-38bd-9e2e-bbdb89e3ebdd | -9.0057 | -67.5186 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README45.md)
