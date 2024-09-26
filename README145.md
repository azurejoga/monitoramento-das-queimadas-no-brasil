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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25f05a79-8eef-3c4a-a49b-f12628fa1eec | -16.58214 | -56.02222 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a923f9e8-1a0d-3005-a49a-62bb7a6f311d | -16.5816 | -56.00369 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| ac92c9e7-1e08-3d8f-a70f-3ba632bf9165 | -16.58105 | -56.00729 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e940c97a-8df5-34f4-bde9-81ae2f49b02f | -16.58049 | -56.01088 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d70f25b9-1d3f-336e-9cab-526f7fc5a61a | -16.57994 | -56.01448 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6d6eb8dc-0453-32f0-b7b9-1cb63cafc152 | -16.57938 | -56.01808 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 379a624a-b173-3b68-826d-1b995bc22107 | -16.57774 | -56.00674 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 96221657-d4cf-39c5-bf4a-3633ec4537e3 | -16.57718 | -56.01033 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b78baab3-091e-3b67-b3bc-d4a35d9d3536 | -16.57442 | -56.00619 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b254e8ac-299f-371d-9219-f000c551a823 | -16.57387 | -56.00978 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8cea7ed5-c5c3-3b43-b470-7c6328117c52 | -16.57331 | -56.01338 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bd4381f-fc81-37e9-88e1-65999bbe46ab | -16.57056 | -56.00923 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 18c58da1-71ed-3270-81f4-e8289957c42e | -16.56889 | -56.02002 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fefdc115-9770-3cd1-910c-baabafcbfaeb | -16.5584 | -56.02197 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 68b59884-a0ca-3617-beb9-08be90a25a6e | -16.55729 | -56.02916 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 98ef616d-15d5-3389-aa9c-f3a8cb2dc119 | -16.55563 | -56.03994 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e7c4d787-4c74-3cd2-9cb9-2c7b1ba0482a | -16.55397 | -56.05072 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8765c1d9-ceee-3965-a5de-e848982aaea3 | -16.55177 | -56.04298 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| eb1641ea-b985-3692-95e0-e7c1a3b67076 | -16.5324 | -56.10232 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a5b85040-b5d0-3a1f-9b11-45f30948d23e | -16.78233 | -55.93657 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7d4072d6-edf6-3577-ae30-fd993f45b042 | -16.78011 | -55.951 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a288a6e3-c1d8-354b-93ce-ba0d90a98ecd | -16.77624 | -55.95406 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 9d575c01-2e5c-32ea-bc7d-d4afd6ec0e78 | -16.77459 | -55.94268 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1878d054-60b9-3fe6-82e8-88dab6d32c5a | -16.77348 | -55.94991 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 0c74e12b-15fc-3e9d-bc35-a1dd2d5d3997 | -16.77293 | -55.95351 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| a6543c70-fa53-329e-ac68-a4b237538a5c | -16.77238 | -55.95712 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 172d17b6-2209-3b28-a41f-1c274bd40074 | -16.75902 | -55.91094 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 79883698-153a-3c69-b9c5-e8e29d4e42c5 | -16.7579 | -55.91816 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2af470ce-db2a-3173-b2e8-71330cc7ffbe | -16.75072 | -55.92067 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9a18d56e-3bf0-37f1-89d1-93df731598c6 | -16.74251 | -55.55098 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a2bce3aa-3869-33c4-b72c-75a88db7f417 | -16.74028 | -55.54313 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 21616403-f233-376c-a6b6-6c72754766a1 | -16.73973 | -55.54678 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b46cc565-f4e1-3e9e-8749-845cbbfc8066 | -16.73918 | -55.55043 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1af2df1d-a6f8-33d0-8e6d-dd8e175c1974 | -16.73695 | -55.54258 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3c592024-fa81-3942-84be-61b16311fd26 | -16.73634 | -55.9257 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c8b418e5-af7f-3852-9ec3-2eec2da21609 | -16.93958 | -56.23969 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 147cd859-6daf-34bc-807d-e921696d168e | -16.77956 | -55.95461 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a17b35f6-bcf3-37cb-b529-321c1d1c6f5e | -16.77901 | -55.93602 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 48c94d16-b53e-3f86-9bce-c348d807ddd8 | -16.77404 | -55.94629 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 89653371-b430-3db8-be92-9f20a818fb83 | -16.76961 | -55.95296 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4d43f9e0-134a-3746-80f4-8e0e27eef317 | -16.7557 | -55.91039 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c5d70391-71e1-3151-8450-3423150f4407 | -16.75514 | -55.91401 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1c685722-4402-38d1-a758-455a0d41d1c3 | -16.75127 | -55.91706 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7613203e-905f-34ca-a0b8-ebe8583ffb5c | -16.74077 | -55.91903 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2283cce9-9849-338a-a640-d3ebbf694bd1 | -16.73916 | -55.52795 | 2024-09-26 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b9c05438-edb0-39cd-82c4-2866f3831bfb | -16.73745 | -55.91848 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7ca1733e-611e-3f71-abf6-b66e67634fb4 | -16.73689 | -55.92208 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f186bf0a-7670-3df5-9036-70f2ea9ca37e | -16.73639 | -55.54623 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d2ed0a4f-4f5b-31c2-9ea6-5ac7aa658963 | -16.73582 | -55.52741 | 2024-09-26 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8eea8b5d-2137-3be5-ad7c-7dc101d3b62e | -16.73358 | -55.92154 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| a6114880-a416-3cb7-8afd-5300c5126e17 | -16.73302 | -55.92515 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 7bf7434b-9770-3eda-a3bf-70e959d5070c | -16.73247 | -55.92876 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 47076e7e-2c8c-3a6d-b195-8584500016f9 | -16.7249 | -55.33426 | 2024-09-26 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 05a3ad0c-c49e-3a63-87be-4ac583a04528 | -17.12516 | -56.1819 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1f99160b-5c2a-32cb-afd9-baeada34565c | -17.12464 | -56.16332 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 396b3459-f340-31ac-8d0d-b090ea78f021 | -17.12408 | -56.16692 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3e6325a3-be3f-3a7c-9249-6607306d4f07 | -17.12185 | -56.18135 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 49b30718-1919-37ee-88b3-2fd993ec21a4 | -17.12133 | -56.16277 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b555f8f6-d94c-338b-af3b-384a1577acc1 | -17.11909 | -56.17719 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 91ce0597-e86f-3139-9003-ccaa18a421d1 | -17.11857 | -56.15861 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d33346e5-13ce-3bb2-8fb7-36ca0264a75f | -17.11854 | -56.18079 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 84c8fc15-59ad-37d8-b793-187217cd9748 | -17.11801 | -56.16221 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c42d4343-db54-346c-a265-e771bc740933 | -17.11798 | -56.1844 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 249828aa-a8d5-3ed2-b078-fd8c5bd5b3bb | -17.1169 | -56.16942 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6f917324-9c3e-3b27-acf3-eae063bf211b | -17.11634 | -56.17303 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 42d2e371-76da-3ee7-b0e6-f56b16f63311 | -17.11582 | -56.15445 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eb3f9369-2b7e-3268-bf42-c9ed070a74aa | -17.11578 | -56.17664 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2f24eefb-c805-3b67-8d1f-71bc974cfe67 | -17.11467 | -56.18385 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 84b649c4-5d11-31b1-845b-07bef940412f | -17.11415 | -56.16527 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 212c4676-6cec-3006-bc0b-311eddcd863b | -17.11359 | -56.16887 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5e58bb5c-9a5f-3115-939d-d2f297711e09 | -17.1125 | -56.1539 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ca9febca-d48d-3504-9c2f-1a2295670767 | -17.11247 | -56.17608 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fff2ad88-e275-3549-bdb9-589f37297c28 | -17.11192 | -56.17969 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e291058a-6b03-3280-abee-929847134652 | -17.11136 | -56.18329 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 18fe5a7e-b8a2-3451-a6f6-bca1735a7165 | -17.10972 | -56.17192 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7640f244-7442-3a81-bce6-fa2d4b98640e | -17.10916 | -56.17553 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c697000e-ceae-37a2-a61e-65be31e71409 | -17.1086 | -56.17913 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 502bc33c-f5a0-3086-9ed6-b49023a51780 | -17.10805 | -56.18274 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cb6562b7-b5ff-38ad-9a5e-ed90dbff89aa | -17.10754 | -56.14205 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 578e2c15-1433-3352-8c90-c535dde6ad95 | -17.107 | -56.14558 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fd921849-284b-3ee4-83d9-b36a594daafe | -17.10697 | -56.16776 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3418d087-adfa-3ed2-aff4-627b8036b1eb | -17.10585 | -56.17498 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8e6fb0db-e854-3117-8256-256e9480befc | -17.10532 | -56.15639 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8b1d00d1-38d0-3e61-9860-a088a9fa685e | -17.10529 | -56.17858 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7cbbfdae-a2be-38a6-98fc-6967d0f047ee | -17.10474 | -56.18219 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d8bab2fc-66df-3d73-b45d-f36e2898ead6 | -17.10421 | -56.16361 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 24d34c3f-97ed-333a-8847-779c7ee7259a | -17.10368 | -56.14502 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c18e8e9d-201a-3539-84df-a408b8020b9d | -17.10365 | -56.16721 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3237ecee-be24-3149-a1af-b6b50c6f391e | -17.10254 | -56.17442 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 55c26258-3965-3eef-a9aa-b14da17396bf | -17.10198 | -56.17802 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 02c5616e-2604-3e35-affa-661674016dda | -17.10146 | -56.15945 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d8edb207-27ba-31b9-a9d5-c06c6dafdd5f | -17.10143 | -56.18163 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 09206f04-004d-3ea6-8355-19c364dd0c18 | -17.10092 | -56.14095 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b0ad32d5-67f9-3c2b-9a6a-71850061f191 | -17.1009 | -56.16306 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 12a36918-d599-381d-8199-685fceb60aa0 | -17.10087 | -56.18523 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 05363f80-c432-3b9e-8593-ccfd24c05720 | -17.10037 | -56.14447 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 08148ffe-89ff-346a-8965-d07c4b4e95f1 | -17.09982 | -56.14808 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 992c75ab-9c5b-32c5-a13e-6df861b34b53 | -17.09978 | -56.17027 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 28cfbbe1-bfbf-34a7-954f-fc2fb38c9702 | -17.09926 | -56.15168 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4032a4ac-ea4d-3aec-806d-ec2a5c62bc35 | -17.0987 | -56.15529 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README146.md)
