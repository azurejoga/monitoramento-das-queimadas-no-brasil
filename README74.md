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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4de64a1-d48e-3f38-a61d-0be22b8427f1 | -16.29609 | -50.05879 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ee02ae75-09f4-3d66-9382-2b30fd3ae064 | -16.53952 | -55.17665 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b198d241-5104-3346-abe6-1a87b1587322 | -15.89166 | -48.1804 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd59e14b-9825-3e2d-a799-0ede9609bfc6 | -16.55436 | -49.74352 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3eabdd8-1d36-370f-b1c3-592087ab020c | -19.98494 | -47.61833 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aaf83c8-0e0a-3110-af97-028652b5d441 | -15.14129 | -52.43982 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e437d0b-88b7-3405-83a0-69caf89c7a56 | -16.88482 | -45.7576 | 2025-09-11 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3be0b840-7668-3a61-8dd3-c4c5b302a80e | -19.99929 | -47.636 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e8ba61e-2d02-3bb6-b8fb-e4de4b2a1ced | -18.01164 | -47.13739 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb9e3db4-68c5-3249-9a32-19fc86929b3e | -14.88794 | -55.87561 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10dcf06b-ae34-3be9-b6ea-a64ac9d8d0e8 | -18.57091 | -47.41506 | 2025-09-11 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f0acdac-6504-3d4f-879c-9dad226e1000 | -18.35108 | -49.33064 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40e95973-bfd5-382a-9381-6448e376fea3 | -17.2431 | -46.75942 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8628345a-494d-3487-9078-6626c51b86b4 | -20.39034 | -46.63183 | 2025-09-11 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84af3496-d4fb-307c-bfca-b065ab59fa9b | -18.90703 | -47.89622 | 2025-09-11 04:25:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe78bbc4-7f1e-3a11-88c1-480c6f819e95 | -20.69415 | -47.92224 | 2025-09-11 04:25:00 | NPP-375D | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bfbd88e-5895-37f8-9383-d08e270887f0 | -14.89129 | -55.87761 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4abab6c-c88b-31c7-aaaa-50b731cb3141 | -17.94257 | -44.49105 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74435cc9-e5bc-3aff-b526-e1e0cd53a0e0 | -17.84615 | -44.21998 | 2025-09-11 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7573c7bc-9384-3415-a0d6-90822ad64c5f | -20.00058 | -47.60592 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 823e1e39-f0e8-3051-9997-c40ea53b344c | -20.14765 | -43.66623 | 2025-09-11 04:25:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e5ba16ae-46ac-3e45-9953-1445a19fa1e8 | -20.14367 | -47.38006 | 2025-09-11 04:25:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4822dc3d-49d1-3630-9c97-85a69c3ebeb7 | -18.34358 | -49.33328 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8379ff1-93b0-3b4f-94f4-c9754302400b | -20.08905 | -44.47613 | 2025-09-11 04:25:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fb5378d9-9070-3da4-92d8-356278e436de | -14.50318 | -53.94189 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 828881ac-479d-3ce8-aff0-9941ec5d26ca | -15.83275 | -52.24398 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ea3711c-1e05-313e-b7af-d40aabb4212b | -16.61538 | -49.78684 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67dbe226-6b51-304a-9500-7ab79f786123 | -20.05946 | -47.51403 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1219e66-40c2-367d-a521-c524ca3ab369 | -15.60538 | -52.74918 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bb7411c-708a-30d4-b3cf-efb4c93c8c91 | -16.43239 | -45.68568 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b3d4314-b97f-3aba-896d-b691902caf0a | -15.5246 | -48.56249 | 2025-09-11 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3addc09b-983a-3a5a-884d-55527fa24468 | -17.9467 | -44.4876 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ed86830-b5b1-359a-9712-1d6d93a113e8 | -17.38773 | -44.93015 | 2025-09-11 04:25:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9f646ae5-85c6-3ac1-84f8-e4adb8cf5af5 | -15.12804 | -52.41784 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71565d7b-0233-3e76-830a-a1cc71e155b3 | -22.87021 | -46.40383 | 2025-09-11 04:25:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d5aeeb89-6a4e-3bad-8500-b9191cfe578f | -18.34263 | -44.36169 | 2025-09-11 04:25:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb4edcba-1f80-3fec-a843-eed4e6978977 | -16.75968 | -49.40665 | 2025-09-11 04:25:00 | NPP-375D | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d651b2b-b140-3e4e-aaef-f446322d1611 | -20.70028 | -46.07023 | 2025-09-11 04:25:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 43370ddd-23f7-35b2-ae88-39d2d9a5683a | -18.83675 | -50.11445 | 2025-09-11 04:25:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9198dd3a-4dd7-383d-a7ce-8d0b72c6d4e8 | -15.13977 | -52.44801 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 104ad993-98da-35c1-a979-9117f9773762 | -16.29764 | -50.06515 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fb3b0243-b287-33c8-88e0-3b48aad54ab4 | -15.54675 | -54.75979 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cca1d71-8dca-3181-a434-f01b33e56b87 | -15.56163 | -54.74806 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2c4499a-bea2-3f51-8104-248e21560355 | -14.92247 | -55.83172 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75d6c92f-3e5d-30b0-aacd-ccebf38c7b52 | -18.62691 | -44.26699 | 2025-09-11 04:25:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b052f356-ae2f-37a8-91bc-bf7d6abfe428 | -16.06478 | -49.96374 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 728a09f9-05b3-3bce-8322-098c4479725e | -19.02457 | -46.26361 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e9564d2-bb63-30d5-8299-53b401a60e09 | -15.13657 | -52.4186 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 101326f0-b55e-30d7-afa1-d761319b9174 | -15.98147 | -42.97909 | 2025-09-11 04:25:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d3fbc2d-1584-36d7-b483-95c71fc2c026 | -15.62524 | -47.53677 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdcaf414-2de4-3d01-90c2-87ca9c907491 | -18.60252 | -43.96399 | 2025-09-11 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a104b6b-a674-3884-b961-29048c2338f5 | -17.72689 | -44.42826 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 144af8ff-f926-3288-acc7-8abe74f4b203 | -20.00377 | -47.62923 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f0235b3-3931-372e-8f6d-e28d6ce31426 | -17.512 | -43.74675 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 863e6224-cdf5-3c5f-be96-459269f0f77d | -17.50772 | -43.75056 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b92d430-4edd-3021-bdb2-cf0ae6ece6af | -16.2833 | -45.68081 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a11334d-d1ca-3610-9b57-00c86770bcff | -18.50536 | -47.41864 | 2025-09-11 04:25:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad8f5def-13fc-3c0a-8b4d-87227093d30e | -19.3689 | -43.27309 | 2025-09-11 04:25:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 88a3f715-217d-33fe-b6a4-64806c71bd14 | -17.95795 | -44.48526 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1179c0fe-ec80-3621-a827-ed6163b57032 | -18.89185 | -43.78481 | 2025-09-11 04:25:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 851ea70e-ca18-39e8-92e0-6c39558cfc80 | -16.61329 | -49.41542 | 2025-09-11 04:25:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fd5bdbd-5262-364d-a06d-cfdd4f2de32c | -22.2638 | -49.562 | 2025-09-11 04:25:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86823880-9e05-3cc2-bc19-d0c2743fcdd1 | -16.62656 | -51.8211 | 2025-09-11 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90d088ab-a6a1-3baf-8283-ada4edb08626 | -19.66026 | -45.85622 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b946fa63-89f2-3127-87f5-68b42c8d90c9 | -19.99827 | -47.62069 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 687f2ec1-dc59-3535-b712-5835f6eeb2a3 | -19.54836 | -46.94613 | 2025-09-11 04:25:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7c2101f-b144-3c5b-b29d-cd19a15c6568 | -20.06982 | -45.29127 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df202576-5945-3ed0-8958-ddb8827fc6db | -16.27937 | -45.68396 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63869cd0-63a5-3c3e-8bed-0050d6661c66 | -16.61745 | -49.41204 | 2025-09-11 04:25:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75c637bc-b97a-33e1-848a-60080ce2e315 | -15.48417 | -49.36135 | 2025-09-11 04:25:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85667bda-8d6c-3ab9-99f1-302238deeeec | -22.82536 | -46.43526 | 2025-09-11 04:25:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 49719d5e-7ce8-3de0-b8e5-6ea1d8dbd444 | -19.75072 | -45.18932 | 2025-09-11 04:25:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab070d0b-8f59-3126-9708-5a346ec1ec00 | -14.89815 | -55.84389 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b2cc91d-460a-3f40-82b9-427121d71c4c | -14.88335 | -55.84331 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8378a12e-5154-3323-974b-41464f8e77e5 | -17.33288 | -46.68089 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e923bf3f-0289-385b-a764-97fa96f800a8 | -22.84071 | -47.4573 | 2025-09-11 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 93d4f192-41cd-3241-a25e-3a80bd15ce9e | -20.89334 | -48.4631 | 2025-09-11 04:25:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a935980-6f18-3d3a-9dbe-e07479012f6e | -15.13776 | -52.4355 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c437ec7-36e7-3e9e-a884-ec89edc3a3b8 | -15.79339 | -52.26137 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0edac824-65c2-3c80-9943-e6eccceac581 | -18.01278 | -47.13011 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8276777f-f35e-31ab-8b1b-66b65ceb80e0 | -18.50316 | -47.30226 | 2025-09-11 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b335833-859a-3f96-bc64-5b763fb81f96 | -20.24267 | -43.58107 | 2025-09-11 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 40962ebe-375f-3029-b49d-42a861369448 | -17.20185 | -50.15997 | 2025-09-11 04:25:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79aa455a-308e-377f-a13f-20955a14085e | -14.50118 | -53.95214 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28aa490f-7b24-397f-b316-5a4ed722681d | -19.92343 | -46.16787 | 2025-09-11 04:25:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed595ad9-9851-3b86-8706-9d4cc317f47f | -15.08768 | -50.06107 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36dd4b13-a938-3584-a804-379b1e43b1ac | -20.88873 | -47.01946 | 2025-09-11 04:25:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a7e54c2-ba5c-3612-be9e-32a951ebc0da | -20.47928 | -49.73206 | 2025-09-11 04:25:00 | NPP-375D | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2c3e762-97d8-3a3c-a0c6-da9597e80f98 | -15.95604 | -50.2249 | 2025-09-11 04:25:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ddd2785-ad7f-3f3a-9c10-ba45f3b94cb4 | -20.54377 | -47.67599 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5734ecb-470e-3eb8-b19e-83f9dab0c094 | -16.00482 | -44.86777 | 2025-09-11 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfb73fca-ba25-3d28-bbed-99530659d137 | -19.67308 | -43.97151 | 2025-09-11 04:25:00 | NPP-375D | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4acc8020-ab4c-363f-8ed9-0d454cd6784d | -19.01499 | -46.25818 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c297f3cb-f0ce-3e6d-b5e5-27c3014f3abd | -15.66867 | -47.02982 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cee8b153-5e29-3373-966d-dee64e8d4248 | -18.00412 | -47.99595 | 2025-09-11 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2cc1ad21-a911-37a6-a620-4960ee866f83 | -16.71006 | -49.37849 | 2025-09-11 04:25:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 072b3d76-5f2f-3a53-bda1-36a8c24b5874 | -17.26757 | -46.08106 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 623fd50e-3771-36a8-a7af-723adde44664 | -17.83985 | -46.7421 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aacc46b1-3103-347e-8ee7-eda5e6aa4b2a | -16.69287 | -44.34283 | 2025-09-11 04:25:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b63de23-7382-3f63-84dc-09312da0cdf9 | -19.66251 | -44.89962 | 2025-09-11 04:25:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README75.md)
