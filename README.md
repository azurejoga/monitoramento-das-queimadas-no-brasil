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
| 546eafd4-8450-39bb-a5c4-37aad4bba5ec | -10.6004 | -45.0928 | 2025-03-15 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 12494a65-8beb-38a0-b400-b72d28bf8482 | -10.6 | -45.1158 | 2025-03-15 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6c611195-3c55-38d5-8144-b8b833054dba | -10.5806 | -45.1413 | 2025-03-15 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 784826fa-2efb-3c06-a50c-df07ddab2db6 | -6.1979 | -48.0482 | 2025-03-15 00:00:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e4581521-fc5d-34f2-b166-05da88a586fd | -6.1979 | -48.0482 | 2025-03-15 00:10:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5fed61a3-3e3c-30d5-b142-660cb0ce17c0 | -10.6004 | -45.0928 | 2025-03-15 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a00117f9-97ee-3aaa-83da-ed6904c87a7c | -10.6 | -45.1158 | 2025-03-15 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 63a76f49-ab07-3b7c-a696-e553b881c074 | -10.5806 | -45.1413 | 2025-03-15 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 405e6824-c5dc-3f50-b019-43dd2dae2ef2 | -10.6004 | -45.0928 | 2025-03-15 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| aba367dd-7bf1-3a1b-b381-31cf2d8117a4 | -10.6 | -45.1158 | 2025-03-15 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b54cfb74-0aa7-3b89-afc1-23547d840f5a | -10.5806 | -45.1413 | 2025-03-15 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 159713f9-5a77-31e4-a904-a5d3a0ba10f2 | -6.1979 | -48.0482 | 2025-03-15 00:20:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cb8446b8-9d3c-3966-bde5-57b1f66bfeb8 | 3.1636 | -61.0103 | 2025-03-15 00:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f34f43e0-1efb-3876-b0d6-6e126b4192eb | 3.1636 | -61.0103 | 2025-03-15 00:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 18a6419a-32f0-39a7-a881-a20d19784be8 | -10.5806 | -45.1413 | 2025-03-15 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 948b8d73-4711-34b4-a288-b3d19873ad08 | -11.5745 | -47.6124 | 2025-03-15 00:33:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42980a77-4a6f-3dfe-a3d1-f7c192525d79 | -6.2036 | -48.0271 | 2025-03-15 00:33:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9a9d296-4c4c-335d-a6f3-8e7f62db06e8 | -11.8916 | -46.937901 | 2025-03-15 00:33:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e507adb7-8c83-3da9-8e4c-38f492d86df7 | -15.2662 | -51.466499 | 2025-03-15 00:33:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09e37a8c-23b5-313d-8709-7204cbd3ca38 | -8.8349 | -50.331402 | 2025-03-15 00:33:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93962b6d-0347-3dbc-a953-0f701c653dc4 | -17.920099 | -43.377499 | 2025-03-15 00:33:00 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dac2a1f6-32a6-3de5-bbec-57e1d88c47de | -23.657301 | -49.3204 | 2025-03-15 00:33:00 | METOP-B | CORONEL MACEDO | SÃO PAULO | Brasil | 3512605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1654da5b-12c9-38b0-bd78-182a080670b4 | -20.232901 | -50.912102 | 2025-03-15 00:33:00 | METOP-B | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44c14a91-802e-3347-a87f-dbde1801c8d6 | -10.5836 | -45.1362 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b0a153d6-d991-3307-8cf7-120cfa702680 | -6.2057 | -48.035801 | 2025-03-15 00:33:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e196d116-4cd1-37c1-be79-8de5837d5e9d | -15.2679 | -51.473999 | 2025-03-15 00:33:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6944299e-b37e-355f-adec-6d7c7165e359 | -10.5766 | -45.149899 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 710da4e9-a596-3fdb-9006-820598a7aa4c | -10.6074 | -45.1063 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 56c01848-7bf8-3bd2-882d-2487a23b9567 | -10.6144 | -45.0924 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1fd0d01-e5b0-3518-bda7-7869ed25b189 | -10.6047 | -45.094898 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edf860d7-e3ed-385d-8d52-fa6e2d060ff7 | -7.2473 | -44.769402 | 2025-03-15 00:33:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d794b4dd-47f2-3074-bc5c-96583a694640 | -15.2646 | -51.4589 | 2025-03-15 00:33:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c19fae0-e6f9-3f0d-a0bf-93483632c8f0 | -10.5712 | -45.1273 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4347d336-6175-35c8-850a-758b93beba5a | -10.6171 | -45.103802 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d364f20-c59b-3a45-be14-d92fc75ad3b3 | -14.2133 | -47.016998 | 2025-03-15 00:33:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 07f98578-7b15-3f8a-91c9-c1bd6946b088 | -11.8895 | -46.929298 | 2025-03-15 00:33:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43fb74ba-17bf-3e07-8b3c-f5747d2e672e | -10.5863 | -45.147499 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6d54a22-3ad0-3f9d-9f5f-d395fe5235e9 | -20.2313 | -50.9039 | 2025-03-15 00:33:00 | METOP-B | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f334702-b547-3941-a620-3d5c49e833d4 | -10.5809 | -45.124901 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf8e15b5-e5e7-30ed-8764-f055e0fa6346 | -10.5739 | -45.138599 | 2025-03-15 00:33:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4c9b149-ee82-34b8-85df-70f59ff78aeb | -12.7286 | -46.284401 | 2025-03-15 00:33:00 | METOP-B | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc6e7c65-0d9d-3a74-a144-2d6b72e5a5cc | -6.2077 | -48.044498 | 2025-03-15 00:33:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 843ff116-90d1-3a4b-abe3-46a3a1725a2b | -12.7189 | -46.2868 | 2025-03-15 00:33:00 | METOP-B | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c8349b5-defa-3cf2-9c3d-fe563b63ae20 | -14.2114 | -47.0089 | 2025-03-15 00:33:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee441bac-410e-322c-9b6c-96d28b63f452 | -15.27061 | -51.47571 | 2025-03-15 00:37:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| aa30a155-7752-3ddc-878d-6813d9ebf255 | -17.51377 | -40.62926 | 2025-03-15 00:37:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| ce88bc3d-f3e1-31fb-ab15-650ffbbfbcb8 | -20.95827 | -44.56593 | 2025-03-15 00:37:00 | TERRA_M-M | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2f1fd8f1-2bf4-3527-8c8b-ae030f4c93f5 | -17.91321 | -43.39211 | 2025-03-15 00:37:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c54b7ea2-3795-3a95-b41e-fbae955c1447 | -15.80551 | -42.59422 | 2025-03-15 00:37:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 07fd475b-e7f8-3bcc-97fc-89cdb79e0dac | -10.61132 | -45.10622 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2a051e91-6152-3948-a61f-2338bbe30c53 | -11.88773 | -46.9425 | 2025-03-15 00:39:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b77fbec4-6f5e-37c7-ae44-2a10d515c7e3 | -10.60108 | -45.0984 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 778a3498-c3a0-3eac-8133-71c47ca2b18e | -10.60369 | -45.11673 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 038bd5cc-1d29-3a92-a76b-12e07b5304ae | -10.05626 | -44.63977 | 2025-03-15 00:39:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 86214fa5-6c02-3fc3-b95c-b9c245a9b943 | -8.83588 | -50.34177 | 2025-03-15 00:39:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc12152e-7284-3403-a0c1-9df7ef9e8e22 | -5.21495 | -44.30668 | 2025-03-15 00:39:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b70b6e8d-0cb3-3ba8-ad64-ce8e3e02a2c1 | -6.20113 | -48.03344 | 2025-03-15 00:39:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3358b1d3-3608-368b-aa3c-b5f1eea1ee76 | -12.61 | -48.37755 | 2025-03-15 00:39:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0bae6e5-b9ee-32bc-b1f2-404cb23f9a23 | -11.57382 | -47.62424 | 2025-03-15 00:39:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 447534b0-a6af-3827-8af9-00437771964d | -12.88216 | -44.87519 | 2025-03-15 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9ebf2181-2b38-3095-836d-bd0d0c9e789f | -5.44297 | -45.43309 | 2025-03-15 00:39:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| af53a032-d592-3ce9-80f9-5ce69658704a | -14.2065 | -47.01842 | 2025-03-15 00:39:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a9be8d61-0b9b-3c05-9e3a-8e02f55deea4 | -10.56386 | -48.51363 | 2025-03-15 00:39:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 03399c0b-8c94-3f30-bef4-25834cc6b957 | -12.88976 | -44.86472 | 2025-03-15 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dafcab4f-93f3-30f0-a26d-f4da896332ab | -11.79259 | -46.6444 | 2025-03-15 00:39:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c23bf2e-0f38-3d26-ae53-7c87a06ae5f8 | -10.58079 | -45.14814 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5a507057-3298-301d-9854-244d2045b9c0 | -12.71953 | -46.29147 | 2025-03-15 00:39:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 704e45d4-22c7-3555-9806-c4f39e055ee4 | -12.89105 | -44.87386 | 2025-03-15 00:39:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 27bd2b4b-8d17-3bf5-837b-f146b7bedeb6 | -7.24669 | -44.77498 | 2025-03-15 00:39:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bec2acee-42b7-35bc-a763-f9380b3b9719 | -10.57186 | -45.14948 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 6363038b-f941-312c-908c-01def6d117d5 | -6.20237 | -48.04254 | 2025-03-15 00:39:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8edb92a3-ed47-3404-b6c2-d19407070e04 | -7.2481 | -44.78484 | 2025-03-15 00:39:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27eecf34-b793-3f21-8b7b-28c043e449c2 | -10.61262 | -45.11538 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7a95ebd3-ec59-3964-9fd0-59867066de11 | -6.20362 | -48.05169 | 2025-03-15 00:39:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e037efe8-3862-39f1-a8d5-53a1e6a482d8 | -10.57949 | -45.139 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 334a37be-49fa-3a30-83ac-efccaa785d5b | -10.57056 | -45.14033 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 8de373bf-2955-37e6-a947-7fd63390f869 | -10.60239 | -45.10757 | 2025-03-15 00:39:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 326f4c88-7779-382a-9019-e81b40b816dc | 3.1636 | -61.0103 | 2025-03-15 00:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1de8ebaf-1d84-3425-8396-7ffb6ad8c583 | -10.5806 | -45.1413 | 2025-03-15 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 7673a559-cfce-356c-9c70-144c04759e41 | 3.1636 | -61.0103 | 2025-03-15 00:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ae31f24b-56c9-3d7f-b0bd-4d7b5c36d377 | -10.5615 | -45.1438 | 2025-03-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0fe57224-5a38-3e9b-8130-6ecff97aac21 | -10.5806 | -45.1413 | 2025-03-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 57e812b0-1fea-3514-b31d-5fa20bb264d9 | -10.6 | -45.1158 | 2025-03-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c28a6112-e4bf-3f5c-8654-99e220d4dbb1 | -10.6004 | -45.0928 | 2025-03-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c227f2e2-b78d-357d-ab18-32e38c8c9d82 | -10.5615 | -45.1438 | 2025-03-15 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 619cc6f8-6f31-3915-bd63-8663271a30ce | -10.5806 | -45.1413 | 2025-03-15 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| aae2a4d6-2f5c-36f1-a48a-cb76c47a65cc | -10.6 | -45.1158 | 2025-03-15 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 82a22fcf-6a4b-3022-abb1-4e00ffb6850d | -10.5615 | -45.1438 | 2025-03-15 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c2d35829-cab2-359e-b449-5e1c5c0a2645 | -10.5806 | -45.1413 | 2025-03-15 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 0476579e-87a9-3c9c-8402-fd9e042ab8d2 | -10.5806 | -45.1413 | 2025-03-15 01:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| c62f53da-559c-31ac-92f6-a4f0a8740e2a | -15.2716 | -51.4748 | 2025-03-15 01:25:00 | METOP-C | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fdb7b4ad-94a6-3aca-b2ac-ccc1db58699a | -12.1463 | -55.917 | 2025-03-15 01:25:00 | METOP-C | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2089c01f-b421-3e66-8d3c-79d6e76cd6f7 | -20.022301 | -55.5275 | 2025-03-15 01:25:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b5e4d42a-cc4b-3c43-9e46-b028d5235d0b | -6.5864 | -51.110401 | 2025-03-15 01:25:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e492938-ef6c-3682-9ba4-815f6868c48f | -23.316299 | -51.335899 | 2025-03-15 01:25:00 | METOP-C | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8f23e4d-9c02-3d8f-8778-9773ab1a9ad0 | -10.5806 | -45.1413 | 2025-03-15 01:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 6480ec16-3d30-30e3-94e7-858d5665f8f3 | -10.5806 | -45.1413 | 2025-03-15 01:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 9203c12b-f612-3ca4-b370-f0b64a925e83 | -10.5806 | -45.1413 | 2025-03-15 01:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| ccaa2858-a867-30a7-90dc-0d6a01838ce7 | -10.5806 | -45.1413 | 2025-03-15 02:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 47a7ab04-c4d6-3df7-996b-791d9b78a733 | -10.5806 | -45.1413 | 2025-03-15 02:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |


[Clique aqui para ver as próximas entradas](README2.md)
