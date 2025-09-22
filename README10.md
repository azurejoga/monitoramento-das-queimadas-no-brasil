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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b9fc4c0-960d-3cb4-959f-8abe83ff3985 | -7.3676 | -43.84329 | 2025-09-22 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6bcc9e5-be15-3481-ac90-cbeb6c8fa0c1 | -8.00667 | -45.71891 | 2025-09-22 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28a38676-bbe0-3cf5-bb6b-b1c4d9ada2f2 | -10.35111 | -46.06122 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 91de48d7-f8fe-39c6-b1ca-1ef09661fbd9 | -12.71567 | -47.70827 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f976fff9-f4d4-3f1b-8d7a-4d8e04d4e75c | -11.77627 | -43.76263 | 2025-09-22 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47979a87-9252-3a50-91ff-669ac9f0655c | -10.40201 | -47.85252 | 2025-09-22 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16c622a7-1267-32f3-ba1c-9b1ef72d27b5 | -12.97905 | -46.38224 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5326e355-9207-3198-9c5e-30f17dd509e0 | -7.22621 | -43.75246 | 2025-09-22 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 797f3319-9c5b-3de8-aa7d-f7ba93a91478 | -13.30957 | -47.29641 | 2025-09-22 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 385abf19-4d00-3b8f-b4bb-f8bee8dbdbba | -7.6088 | -44.49153 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cb01a89d-1b91-3656-8040-fefd3ad52829 | -12.69848 | -46.86332 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9915b913-b6cf-3b3c-a34d-589bab0bfdc6 | -10.37098 | -46.06483 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8338910b-a52a-3054-9fa8-262fae49005d | -7.51115 | -43.69553 | 2025-09-22 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cec0b7c8-ea58-3b45-b321-0998651cb6dc | -10.36763 | -46.05507 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f9673d5-7ca5-3758-9b2e-8ccafc48ed92 | -7.3561 | -44.55761 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2f1a407-a27b-36f6-9549-7d89e5a1eb22 | -7.64634 | -44.44157 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4c25779-dee7-3684-902d-b67908b3dd7d | -11.73539 | -47.80157 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1d707a2-7ab3-3eb1-bd36-afd4a01fc494 | -11.5221 | -43.62954 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb0c21d3-5a0b-3551-aaec-ee5dc4e78794 | -11.02093 | -44.64567 | 2025-09-22 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9561d08b-34b5-36cf-b1b6-fb0681214f2b | -11.46853 | -43.5341 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d2355e9-67a0-300f-9c93-83c60fd99303 | -12.71102 | -47.70374 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 407a35bf-b695-37d4-861d-fc3f8ea1365a | -10.04817 | -49.19884 | 2025-09-22 03:49:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e875859d-3e46-3694-9ee7-8f211e79cfd1 | -11.8451 | -38.20191 | 2025-09-22 03:49:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c3418ee5-e80d-3551-82b4-c3d9c1fe73d3 | -11.65982 | -47.48988 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85a6d413-dddf-30f5-9000-baf1c9e9170a | -9.74062 | -45.95202 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6173371f-4af3-39ee-abf7-e55464baaff7 | -11.63467 | -44.33715 | 2025-09-22 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82a9f53e-7aa9-3588-acca-8bb7eada02ec | -11.66566 | -47.50003 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6235cfa-466b-3f30-983f-cb666eec1fd0 | -10.35219 | -46.05533 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd7e869c-2ec8-33b3-a568-6387b426f497 | -10.349 | -46.07265 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b2d5a0b-95b7-3777-8b26-6ddfc013882e | -11.6645 | -47.49425 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a882df0-937c-3e57-873a-9333ab97b0dd | -13.24208 | -47.21953 | 2025-09-22 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21b04fba-438c-3517-be82-55a9bd1204ca | -13.24032 | -47.21675 | 2025-09-22 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3f323ff-037d-3386-9df9-2eb787f9260a | -11.66171 | -47.49162 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03305890-d116-39c1-9433-f163100dec8f | -11.6592 | -47.49309 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f003f4ba-5274-3a8b-9ed8-a620b272858e | -7.36563 | -44.55882 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| beedcda1-e00c-3f65-97f6-9c400a29859e | -13.73729 | -43.78405 | 2025-09-22 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d4c7c7f9-3e2f-3191-ba84-54a7a5a0d60d | -11.50447 | -43.57156 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47dcf7aa-43f9-36ef-a6fa-1cc07a4611fb | -14.98723 | -42.23724 | 2025-09-22 03:49:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d33c8a36-fcf5-35d6-ace6-05cf87fa6411 | -11.42107 | -43.52219 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f9ee0c8-b8e2-34ef-8e6f-ab1625a2b686 | -12.96875 | -46.94041 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f1fa885-6885-33f9-96c2-413be604b463 | -12.43156 | -45.13717 | 2025-09-22 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fd97b28-fcbf-3614-9b97-688f57e1cfed | -14.27209 | -44.38065 | 2025-09-22 03:49:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 253b0ccd-95e8-36f2-958c-0d0bd85b4fb7 | -8.01175 | -45.7197 | 2025-09-22 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbe69821-8b73-333b-927c-4a59e494dfa9 | -12.97812 | -46.37818 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ccb6348-246f-38c7-9ccf-208d17667f77 | -11.52346 | -43.62197 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b82563-9a96-3222-9217-72cb56469e29 | -12.98091 | -46.38982 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2b0ebb9-6e9b-358c-9c70-0b21a0a88a3c | -8.77205 | -37.74797 | 2025-09-22 03:49:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fe9ea780-15cb-39db-8e34-00a009286813 | -12.7256 | -46.83013 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc7fce0e-4926-3881-99ce-671460f10905 | -11.66512 | -47.49109 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 001984fa-2455-3eaf-8f3e-d6b2831cbc4c | -12.98296 | -46.37913 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18e99b38-624a-37cf-9058-aa0fc1bb89d2 | -13.7277 | -43.90935 | 2025-09-22 03:49:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c853c3cc-95a6-34d2-9c72-b39dc4dadc3b | -9.26065 | -45.83742 | 2025-09-22 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 378cb794-8c73-3b95-bbe5-13ea8b574385 | -12.68705 | -46.84148 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40561c91-553e-370a-af2f-c26022291a32 | -12.71463 | -47.70479 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 610b0c31-b404-3df9-817e-fd2a3c3df5f4 | -10.04204 | -49.19777 | 2025-09-22 03:49:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 595207a2-0174-386b-9fc5-328e7a4a9115 | -7.80227 | -46.18877 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 19b82daf-4741-3d3e-b132-f5a7cd8aac83 | -7.02475 | -46.31127 | 2025-09-22 03:49:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 637c691f-afc0-34b1-bd6f-4dea6c3920f3 | -13.23964 | -47.22024 | 2025-09-22 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0db02bc2-4010-3811-b092-da7191a40250 | -10.36655 | -46.06099 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ba6adac-9ae3-31dc-8b01-eec44d62e514 | -7.79695 | -46.18827 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fce85a4c-8510-3885-93bc-aacd40edc4b8 | -12.73115 | -46.82821 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a9c81ab-a4f3-3a56-ae6d-c10eafed2eb0 | -12.7153 | -47.70138 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2476eaf-d86f-3819-b39f-bcab1dce7603 | -8.80383 | -43.06195 | 2025-09-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2dd0a24b-c603-3aa4-b0e4-633d3b7c5a00 | -9.26006 | -45.84061 | 2025-09-22 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fa9053f-2b8c-328c-8a8e-081583351592 | -7.79754 | -46.18504 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 123a7e42-fb80-3f3e-a4ce-8ec5261366b5 | -11.73467 | -47.80524 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e44ab261-a22d-3942-810d-b8778764f3f4 | -12.36264 | -44.21522 | 2025-09-22 03:49:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 984e5464-16ce-3ba3-b0de-467eafa8e78e | -13.61791 | -47.4159 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 708a1df8-f8cd-33e7-9cba-abdf4e012f9a | -7.80158 | -46.19255 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 985beaf6-dd67-32b9-9b99-8d5d89792756 | -7.35323 | -45.62056 | 2025-09-22 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a670881-af9c-358b-bde2-cc97f1aa1572 | -7.34784 | -44.45464 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d45aa09e-8a10-3fbb-bfb2-883065b61785 | -3.17201 | -41.06178 | 2025-09-22 03:49:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c70ef0e-cb6c-33be-9641-b7dfc890cb22 | -10.35057 | -46.06411 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9cbb7033-e07f-3bf0-b2b3-d7f3cdaffebe | -7.22248 | -43.74723 | 2025-09-22 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d30455d6-5c45-34fb-823c-1f53393ddea9 | -14.52721 | -44.87387 | 2025-09-22 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c69707a9-b8c8-3e73-a070-4266c510e6df | -11.02717 | -45.90122 | 2025-09-22 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f5ecc86-bdfb-33f5-9646-83df17ba138b | -2.91534 | -40.38919 | 2025-09-22 03:49:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc694963-40b8-3cf0-8a8d-8c663a5872a2 | -8.84991 | -43.01833 | 2025-09-22 03:49:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9251eb05-02de-3b6a-a8e0-410285ae3d4f | -0.94935 | -47.35159 | 2025-09-22 03:49:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4ef5237-acda-3935-b572-e8165d39d301 | -11.52692 | -43.62646 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac33ea71-2a77-3b11-9f82-b72aa2876985 | -11.28696 | -47.51888 | 2025-09-22 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88d818e0-54bd-3de8-95e5-1ab269268d98 | -11.46281 | -46.93804 | 2025-09-22 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9384eaf-f706-3941-821e-eb390ae8e6b5 | -11.0254 | -44.64643 | 2025-09-22 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 734c51ce-e9bc-338b-9f4c-3e9360ace264 | -10.84915 | -42.26354 | 2025-09-22 03:49:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c5f8b980-9bd4-36cf-9236-ad9d6c364142 | -7.96104 | -43.89853 | 2025-09-22 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30b189a4-3f59-360e-8abe-c2df1f41d91a | -10.40907 | -47.85399 | 2025-09-22 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea23c30c-6e54-31b8-b3ee-2313f76b2a77 | -11.49128 | -43.54964 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2cc80d9-79a2-396f-9597-1eb50acf598a | -13.85664 | -40.94631 | 2025-09-22 03:49:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 21c72ed8-e397-3660-b3e4-1cfbb409f874 | -7.60716 | -44.44569 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d59ffa71-32ee-3bf8-b2d1-a2eeef61bdf9 | -13.08222 | -47.01965 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efffae72-ea43-33d0-a28f-fc9c68996b5c | -10.38824 | -46.08282 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a03aaa3d-e6b1-30bd-83ba-7a00a890b62d | -11.0201 | -44.65021 | 2025-09-22 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73e094a4-6687-350f-b991-bbfde757a1d6 | -11.22054 | -46.16676 | 2025-09-22 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46415774-1985-31b1-a7ee-4f6a0fab8b49 | -12.72257 | -47.69244 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 044320ce-386b-3eff-87c6-57ec543b7602 | -9.26032 | -45.83744 | 2025-09-22 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 291afb21-fbd4-346c-9726-832d157f2526 | -10.38217 | -46.08794 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 845fce47-ac14-37e7-8f22-4dd0da44ed93 | -12.42791 | -45.13179 | 2025-09-22 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9443abd6-2718-31a1-a60b-47aeba147bbc | -8.85204 | -46.15855 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e555c76-8e8c-3dfa-ae17-f0ecebcbd258 | -12.71597 | -47.69801 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68986a67-bf4c-35c9-8271-06d99ea84864 | -7.96177 | -43.89424 | 2025-09-22 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README11.md)
