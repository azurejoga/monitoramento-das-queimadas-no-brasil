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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a6d6dba-20be-3b50-bcd5-125b58ec4921 | -5.4738 | -45.4201 | 2026-06-29 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| eb4557fe-7784-3b56-8302-db58b473656f | -12.5135 | -48.2802 | 2026-06-29 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| b562547d-6b37-3f91-92eb-e806c11fb7d7 | -8.943 | -45.6573 | 2026-06-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 7d87107e-43eb-3e7e-babd-d9f937e8330f | -11.9093 | -57.4334 | 2026-06-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 8392d9d4-7191-3992-9a8d-e871c685cdb0 | -8.9799 | -45.7212 | 2026-06-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 253.6 |
| d682dfcf-8ec9-3d09-848f-3ffda59bfc23 | -11.9533 | -58.6192 | 2026-06-29 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f6a5eef3-62f3-3f5e-a7d2-c1824ea0435a | -9.6037 | -56.9276 | 2026-06-29 14:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f6ebedff-2aa4-3231-8c1f-99db9bb64d94 | -12.5138 | -48.2581 | 2026-06-29 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 615f7e60-9970-30ae-a757-63f9d38a6d9f | -11.8906 | -57.415 | 2026-06-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 4141543a-ddc8-38bb-a04b-3ff884dae3e5 | -11.8937 | -57.1355 | 2026-06-29 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7f37a1a0-ad60-33c2-baea-b2a27dcbf62b | -8.2907 | -48.1876 | 2026-06-29 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5077d1c0-1729-33d3-b155-14d4cb5dbdea | -11.9284 | -57.4119 | 2026-06-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| a7d0970b-fdb7-374a-96ba-ef2f961c2a4d | -17.7126 | -46.7565 | 2026-06-29 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 5df0a173-6afa-3031-a54f-ff560988f8d8 | -8.943 | -45.6573 | 2026-06-29 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| ad79e7ed-e5b3-3ab9-a4da-6abb57a9c347 | -8.2907 | -48.1876 | 2026-06-29 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a05fa023-5f84-387a-9d99-afa38b50173c | -11.9097 | -57.3935 | 2026-06-29 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 977c4e70-67de-33e8-a508-bbe87d8017f0 | -11.2148 | -53.833 | 2026-06-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 0e1a0e54-034a-305e-b36a-7b6a9add96e6 | -12.5138 | -48.2581 | 2026-06-29 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| db670f61-da7d-3cff-8a2a-9a9cd628f381 | -11.06 | -55.7597 | 2026-06-29 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 182.6 |
| 7be815b6-0bfe-372e-bdec-c79eecd58552 | -11.0414 | -55.7411 | 2026-06-29 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 192c4ac0-f615-30c9-b6a9-2e84ae54719c | -11.9441 | -57.7091 | 2026-06-29 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a9a9f5ab-3b03-3580-b0f4-19fe31a1ca64 | -11.8937 | -57.1355 | 2026-06-29 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 8e833592-5286-3039-8578-56640b7d42b1 | -12.5135 | -48.2802 | 2026-06-29 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| a92d55c2-3525-3e06-ac4f-dd99e9b3b531 | -11.9533 | -58.6192 | 2026-06-29 14:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 7f21d838-324b-3441-8e11-46c2fa81f96c | -11.9284 | -57.4119 | 2026-06-29 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 31d79220-aa9d-3e9b-8943-3254c20331df | -17.712 | -46.7798 | 2026-06-29 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 255.8 |
| 56f110e6-2d25-34b0-a64e-778f9f77934e | -8.9985 | -45.7418 | 2026-06-29 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| a2266647-34b0-3c6a-8c07-db444ec81537 | -17.7126 | -46.7565 | 2026-06-29 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fddb0134-df53-3e88-b7a9-5b2abeb71b81 | -11.8906 | -57.415 | 2026-06-29 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 9a5cc0a5-744f-34b8-94c4-e7ade52df27f | -9.6037 | -56.9276 | 2026-06-29 14:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| dd02e16c-784f-39f9-9027-88f00fc5cac7 | -11.9095 | -57.4134 | 2026-06-29 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 410.0 |
| ae45ce1c-5585-304c-941b-96d3021ac0ad | -11.9286 | -57.392 | 2026-06-29 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 085e430a-4a27-3f9d-ad32-cca85d4262b3 | -11.8906 | -57.415 | 2026-06-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| c2664682-9d99-3b55-a1dd-e6c5d4c20899 | -11.8937 | -57.1355 | 2026-06-29 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 70f058fa-59cd-3343-af06-7735b46cff61 | -11.0414 | -55.7411 | 2026-06-29 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 9718f576-2066-3a19-bcea-306c974691d0 | -11.9095 | -57.4134 | 2026-06-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 375.2 |
| 77ca7a9d-588c-3895-bee2-722f4f2afb1c | -12.5138 | -48.2581 | 2026-06-29 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3ea58afd-857b-32ba-947a-72ba7b64ff95 | -11.2148 | -53.833 | 2026-06-29 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1ca43cde-970e-349b-ab86-2814ea167a3e | -6.1632 | -45.6415 | 2026-06-29 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0cc6e1cd-372e-37d2-9444-270834d8e257 | -11.9093 | -57.4334 | 2026-06-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3f150222-f03e-357a-b3d3-b06ab7c3ad25 | -12.5135 | -48.2802 | 2026-06-29 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| afc94d96-8fed-373b-8a1f-8fe75ee3fda8 | -11.06 | -55.7597 | 2026-06-29 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 3e0615f0-8055-3999-8232-1608ec4ae7e0 | -12.4462 | -58.5023 | 2026-06-29 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 447.0 |
| 5184c6f0-98bc-34f7-9126-34f5216c552d | -8.943 | -45.6573 | 2026-06-29 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 18a0bc56-351a-356c-b17d-eb2bc0374b18 | -5.4738 | -45.4201 | 2026-06-29 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 5702b6d3-3577-3be4-8300-4b18c9ab2606 | -11.9533 | -58.6192 | 2026-06-29 14:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4b234a15-a1e8-3e8f-b7e1-1d1490c62243 | -11.9286 | -57.392 | 2026-06-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 2dea1407-d2b7-3b6b-be65-81eba5d64fe4 | -12.2222 | -56.5467 | 2026-06-29 14:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5671d869-9d00-3810-b45f-f5e11dc73113 | -11.9108 | -43.4081 | 2026-06-29 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 1931a201-f373-34e6-aee1-333ed0b111c6 | -9.6037 | -56.9276 | 2026-06-29 14:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 6f39d788-a86b-3719-808b-82329ba66428 | -17.7126 | -46.7565 | 2026-06-29 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 8dabe534-78ce-3f67-801e-62198ff46bad | -11.9284 | -57.4119 | 2026-06-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 334eb8f2-2a07-34a4-8a77-997f34c5841b | -17.712 | -46.7798 | 2026-06-29 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 276.2 |
| b2d43c56-3403-3321-af24-41b44f84fd7c | -11.9097 | -57.3935 | 2026-06-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| ec1446d1-c139-3ac9-a9a7-b7848a4aa147 | -11.9441 | -57.7091 | 2026-06-29 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b3cdc6b6-de67-3512-aa03-d8ee6c765790 | -12.222 | -56.5668 | 2026-06-29 14:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b51ebef2-08a5-3ca8-ba95-218e252286e5 | -8.9799 | -45.7212 | 2026-06-29 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| e6beb8c5-316f-38c4-bf31-9d6c954e26c5 | -17.7126 | -46.7565 | 2026-06-29 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| dcd597e5-5671-3dbe-a9d7-ee00304ac113 | -11.9533 | -58.6192 | 2026-06-29 14:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c63d05b4-5363-3fa6-ba57-764f4611df72 | -12.5135 | -48.2802 | 2026-06-29 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 50913d77-8000-3257-807d-e9ec3344f638 | -11.9441 | -57.7091 | 2026-06-29 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7b64ebc0-7e5a-3c5b-8f9a-bcbf9427f238 | -9.6037 | -56.9276 | 2026-06-29 14:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 20e0bf7e-5a83-3f2a-bce4-12ea6961c1fd | -11.0414 | -55.7411 | 2026-06-29 14:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 39675912-038b-3b0f-8173-9f3836b3f492 | -12.222 | -56.5668 | 2026-06-29 14:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d811583d-6be4-311a-8217-b70d94dce6e0 | -12.2222 | -56.5467 | 2026-06-29 14:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 43ff5baf-696b-3ec1-b404-6c4298c2f3e8 | -11.8937 | -57.1355 | 2026-06-29 14:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 2d1f3d00-5152-31a7-8a49-c7211393315c | -6.8952 | -43.6833 | 2026-06-29 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1d0bb21d-f125-3d74-aff7-4d08902ce606 | -11.06 | -55.7597 | 2026-06-29 14:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 19dd4223-953b-33c9-b877-5e3f8f7ee7d3 | -17.712 | -46.7798 | 2026-06-29 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 231.9 |
| b719a875-4d92-3683-9a62-a922ee3faf50 | -11.2148 | -53.833 | 2026-06-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d428d0f7-9a3a-3e33-af7c-2cb22ea4acbf | -17.712 | -46.7798 | 2026-06-29 15:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 61c70afa-edc2-3033-b1bf-2486460c1a58 | -9.6037 | -56.9276 | 2026-06-29 15:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 64db5ef0-3128-3f4a-8451-dae8bf0e9cfd | -11.9441 | -57.7091 | 2026-06-29 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| edb8ad43-3b84-3531-9096-26aab65f94b5 | -12.5135 | -48.2802 | 2026-06-29 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 960c4c22-67f2-32ba-b514-2d9c9daf3dfa | -11.8937 | -57.1355 | 2026-06-29 15:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 5be26321-0433-3f74-88a3-fa6698fd1164 | -12.5138 | -48.2581 | 2026-06-29 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7b9d2f5c-699f-33a0-b354-6d00f7c0d71d | -12.222 | -56.5668 | 2026-06-29 15:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e4a190f9-d3dc-3e59-b2c9-f8a8975dc36c | -11.8939 | -57.1155 | 2026-06-29 15:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d7a920d4-d5ce-3a80-aa5b-72d023e0d7a9 | -12.2222 | -56.5467 | 2026-06-29 15:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e50eb54a-9f43-3e98-ae68-7cdb2041adc2 | -11.0414 | -55.7411 | 2026-06-29 15:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 65978547-9345-35d8-bb55-f8688dbf09fc | -11.9533 | -58.6192 | 2026-06-29 15:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 50de8a55-73d8-3737-9bc3-ce4da83e3632 | -6.497 | -42.238 | 2026-06-29 15:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 33b70180-e9bd-3496-94c4-e21f5a209654 | -11.2148 | -53.833 | 2026-06-29 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c7a01b99-01b2-3a29-b0f3-cd089e9d28d9 | -17.7126 | -46.7565 | 2026-06-29 15:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| dd2c74ca-f556-3088-b415-031343a44c83 | -8.0127 | -46.2475 | 2026-06-29 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| cb6c111a-f421-3557-af13-a8d0366f14fa | -13.7128 | -47.8627 | 2026-06-29 15:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 21d7ef5b-2a6d-38a8-80d5-92782898ca5e | -11.06 | -55.7597 | 2026-06-29 15:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a8ee081f-9cff-3fff-b01f-4bd231e3b7e4 | -11.78 | -47.5583 | 2026-06-29 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 842a0542-ad4f-34e9-857b-26d7191568d1 | -11.06 | -55.7597 | 2026-06-29 15:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 204f2e22-791b-374c-b085-247992aebcae | -17.7126 | -46.7565 | 2026-06-29 15:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 00d2cee7-2431-35ff-8514-b5ac2821aa49 | -8.0127 | -46.2475 | 2026-06-29 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| dbfe6da0-3b6d-3b2d-9f6f-175c8a582c32 | -10.2942 | -57.1182 | 2026-06-29 15:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 064ce32f-dc36-3154-a65c-6774e0cf32b2 | -17.712 | -46.7798 | 2026-06-29 15:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 190.7 |
| cd80940e-ea83-39fb-aff4-ea1568ae0858 | -10.9882 | -49.5618 | 2026-06-29 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7a897071-c8f6-3b72-b3a1-5ea1a521900c | -12.222 | -56.5668 | 2026-06-29 15:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 82fbb183-8f84-3bdc-b983-a948c3a8ac62 | -9.6037 | -56.9276 | 2026-06-29 15:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| bfbc6a5c-401f-399e-a267-980b405639d9 | -13.7128 | -47.8627 | 2026-06-29 15:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 77e7aa08-8038-3c03-ada4-641dfb6f368a | -11.9441 | -57.7091 | 2026-06-29 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c1dfb170-3147-350c-8120-c7c271374d99 | -12.5135 | -48.2802 | 2026-06-29 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| edc6b49c-15b1-30b4-85d4-fc3ce60c55b9 | -11.8937 | -57.1355 | 2026-06-29 15:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |


[Clique aqui para ver as próximas entradas](README14.md)
