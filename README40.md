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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0254073c-81ae-313b-9bf4-41c2c43c85d5 | -20.9077 | -45.54916 | 2025-10-16 03:51:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f32c14a-042c-3b63-97f6-72cd518400e6 | -19.96214 | -49.41681 | 2025-10-16 03:51:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 77610ec2-47a4-3c7e-93cf-a2f415829ca0 | -21.51974 | -45.026 | 2025-10-16 03:51:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ffda533a-8d76-3845-be48-27aec3e4abba | -23.00648 | -52.48038 | 2025-10-16 03:51:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9caf2c4a-fc7d-3f3c-a3bb-68ca9b0f1b75 | -20.48151 | -45.9953 | 2025-10-16 03:51:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91dba34d-63f9-3383-b44e-23bb077e15a5 | -20.3534 | -48.78534 | 2025-10-16 03:51:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67fa8426-47fe-3187-84a9-c0924fe27f04 | -23.00046 | -47.0957 | 2025-10-16 03:51:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| af59513b-0086-3425-8334-159e638679f4 | -20.95899 | -47.41858 | 2025-10-16 03:51:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4b570f1-31b2-3641-b557-f84f2888ffac | -20.95997 | -47.41374 | 2025-10-16 03:51:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae3d8cf3-702f-34a7-b2b1-1d40f2d8fd83 | -23.00755 | -52.4759 | 2025-10-16 03:51:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85f5d482-2e97-3a91-81b1-3910e9af5f8f | -20.95543 | -47.41267 | 2025-10-16 03:51:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca0e4b50-8a03-3b4e-89d9-b9f677aa59a6 | -20.35838 | -48.78667 | 2025-10-16 03:51:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6bc0c15-cae9-3886-b78b-1fdf1bb63422 | -21.55176 | -44.26956 | 2025-10-16 03:51:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb98f9e0-5eb5-3114-912d-f78219c852fe | -22.09537 | -46.544 | 2025-10-16 03:51:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5968ceb3-69b6-3474-9762-e31e8da89960 | -20.4773 | -45.99442 | 2025-10-16 03:51:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdc94642-be36-3019-85de-02a513d8e9c0 | -21.22004 | -46.10627 | 2025-10-16 03:51:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 176b6ec9-87ff-3b36-87b6-2c579d9da360 | -20.94828 | -47.40105 | 2025-10-16 03:51:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ffcae9b-5f67-30d7-b50a-9d2f23d65669 | -20.94927 | -47.39619 | 2025-10-16 03:51:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e45752f4-9c28-3411-8120-14e3181b69be | -20.61156 | -45.91042 | 2025-10-16 03:51:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6ee95e7-f15f-3b56-89af-8c2840ac0c95 | -29.18445 | -50.13036 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fdeb0214-f0a6-3a85-8b84-5089bcf795f2 | -29.16971 | -50.13179 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| db9a3014-1e20-36d9-a093-2246fbcb89be | -29.17541 | -50.12772 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f8aae328-7190-3393-91cf-e7eaf1bfed31 | -29.17775 | -50.11706 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0698938b-509b-30cf-b5a3-4266010f891f | -29.1878 | -50.13704 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 33bad094-6ab0-38a3-8f3a-73619a80143c | -29.1868 | -50.11959 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 1d2bb280-832d-3cde-8352-f3ed1e64c80a | -29.18227 | -50.11831 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| c2052f53-380f-3a8c-b75a-0d03d1872fb9 | -29.1709 | -50.12638 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bab5e660-5435-3a9d-aab2-c113162a8efd | -29.18665 | -50.14232 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 717e143a-8050-3d5c-ab39-c683e0297131 | -29.17206 | -50.12109 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ad35d456-8b5d-3bef-9191-0cd74be03eef | -29.18212 | -50.14102 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ac33eeb3-a220-3391-a26a-69c525acb701 | -29.17658 | -50.12238 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a7c661fb-0c9d-3d88-ad8f-ef089e30df96 | -29.18328 | -50.1357 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 64478523-34ea-3f8d-9a6f-cedc7c2c98f7 | -29.18896 | -50.13171 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 20629766-098f-3501-97cc-d2576570683b | -29.17876 | -50.13441 | 2025-10-16 03:53:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c595bdcf-685d-3c48-8884-2a62f21badb1 | -4.116 | -48.0352 | 2025-10-16 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f6b3dcf2-907d-3185-a00b-508bc5993f89 | -4.3685 | -43.4071 | 2025-10-16 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 295.0 |
| 2ae06e63-32f7-330a-9ad1-d73aa53ec9aa | -4.6437 | -44.1073 | 2025-10-16 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 41b28b73-4c0b-31e5-a2ff-87a8007c6110 | -6.1532 | -40.9215 | 2025-10-16 04:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 18eadb87-e312-3c48-9048-1c9a21ee54bd | -8.4528 | -44.1767 | 2025-10-16 04:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2e92997e-9ee4-30eb-a661-a4dfc0aeca32 | -4.6624 | -44.1062 | 2025-10-16 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 279.9 |
| dd39ea3c-f789-372f-9b88-42e01971d7a0 | -4.3874 | -43.3827 | 2025-10-16 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 447.3 |
| 9d88a69d-4dab-33c0-96f5-dd62e7db0066 | -4.1161 | -48.0136 | 2025-10-16 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| fe43036a-191a-33d7-b8f6-9222646acea7 | -4.0976 | -48.0144 | 2025-10-16 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 173.3 |
| a6690585-a2ae-3a5f-832e-e42c4e8489ce | -4.0974 | -48.0361 | 2025-10-16 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| f4d43bbe-8eca-395b-9943-0e958a251611 | -8.4717 | -44.1746 | 2025-10-16 04:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 8f956223-018d-38ab-9ca4-8f0a9e88c464 | -4.6813 | -44.082 | 2025-10-16 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 036340b3-eb66-3cba-a66f-03321569390a | -4.3872 | -43.406 | 2025-10-16 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 362.7 |
| 0b37a799-5da7-31ee-a094-e9680d062316 | -3.0158 | -45.3679 | 2025-10-16 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 67d3395e-e732-3405-8312-7415cfa8a12c | -4.3687 | -43.3838 | 2025-10-16 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 414.8 |
| 7fbe92a0-ccba-3010-9c0c-601f30838294 | -7.3955 | -39.6845 | 2025-10-16 04:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 62.2 |
| a7db8921-d9ce-35ef-adc8-15028ffc9706 | -4.6626 | -44.0832 | 2025-10-16 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 0399b7a4-bc3e-3b9b-af81-62e3e78b3b9f | -4.4059 | -43.4049 | 2025-10-16 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 9d03d02f-ea9f-3105-9cd1-abb44c4bad9e | -3.0157 | -45.3903 | 2025-10-16 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 3f5232d3-e470-3985-9c76-02a00cedf8fc | -4.4061 | -43.3816 | 2025-10-16 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 65795d6d-b3b4-3087-a72d-4b30cec89396 | -4.6811 | -44.105 | 2025-10-16 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| cadf8d04-36cd-3695-9632-1b9e166a203d | -6.1534 | -40.8971 | 2025-10-16 04:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 933e6f9d-b33c-3a26-9eb3-79fd836c4708 | -11.5917 | -44.0707 | 2025-10-16 04:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 074bde5e-8d45-37e5-9587-7ac17c685ae7 | 1.8218 | -55.7431 | 2025-10-16 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4b906172-ded3-30c1-94bc-408510204be1 | -5.4762 | -42.9367 | 2025-10-16 04:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| e577aaf8-1a58-3a06-a2a8-00b09e6357ad | -5.4762 | -42.9367 | 2025-10-16 04:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| f24828a2-9434-3606-a3d7-9a6ccc101555 | -4.116 | -48.0352 | 2025-10-16 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b0d161fe-9bef-3a6c-87cb-b4436d612400 | -8.4717 | -44.1746 | 2025-10-16 04:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0987dff4-ca1e-3c1f-b4f1-eb0a50c620c5 | -6.1532 | -40.9215 | 2025-10-16 04:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 34b76608-e6bd-3098-ba42-0b9a2dd9d8ef | -4.6626 | -44.0832 | 2025-10-16 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| a3a882b2-7314-3945-bbfe-53fb95299e39 | -4.6624 | -44.1062 | 2025-10-16 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 205.2 |
| a9687c50-f71e-3ee7-b47a-bb1c7efbef18 | -4.4061 | -43.3816 | 2025-10-16 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| c08bd427-374f-34fd-8140-fc1c24adb94f | -4.6813 | -44.082 | 2025-10-16 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 553edc30-06f8-3973-8048-4aa857fa0c82 | -4.6811 | -44.105 | 2025-10-16 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1d0bffa6-48c7-3a29-a514-f0e328099e45 | -6.1534 | -40.8971 | 2025-10-16 04:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| ffb07697-7b39-38a2-ad64-400d10e3e933 | -3.0157 | -45.3903 | 2025-10-16 04:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 119.3 |
| c954a1ef-9114-350d-81d1-3f81fac42cc4 | -4.1161 | -48.0136 | 2025-10-16 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| c6017373-5aea-3434-b7b1-2c53a9afbbb4 | -4.0976 | -48.0144 | 2025-10-16 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 4d5a950d-5e20-3695-856a-d26b589c1dff | -4.0974 | -48.0361 | 2025-10-16 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 0aaa5558-7248-3f30-8428-2f78893c8be8 | -7.3955 | -39.6845 | 2025-10-16 04:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 79224b37-f6ab-353e-806c-b24241486aae | -4.3872 | -43.406 | 2025-10-16 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 305.8 |
| df71aea3-269a-3142-9de5-060b324583d6 | -4.3687 | -43.3838 | 2025-10-16 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 501.2 |
| 4baa1f1c-17fc-3e03-89d0-d8dfaf1f7eca | -3.0158 | -45.3679 | 2025-10-16 04:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 9474d09c-44eb-3d91-a881-2b0994ec2016 | -5.6819 | -45.112 | 2025-10-16 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| d0984022-656d-3904-90d8-c5fec8751051 | -9.6972 | -44.5172 | 2025-10-16 04:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 241427c1-4c20-376f-b309-8399a2c742cc | -4.3874 | -43.3827 | 2025-10-16 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 512.2 |
| cface66f-6085-3556-93e3-a5d92254d92c | -4.3685 | -43.4071 | 2025-10-16 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 240.3 |
| fc656101-90f7-3467-aed4-7cb35260f2c4 | -4.4059 | -43.4049 | 2025-10-16 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 30446b53-ad2e-3750-87ef-81afde0c1445 | -12.9909 | -47.3217 | 2025-10-16 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5e00cc3c-b3a4-39e8-971c-ed6c9ecd1218 | -8.4528 | -44.1767 | 2025-10-16 04:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bd301d84-a8e8-3fcd-8206-d178a7d0e233 | -5.6821 | -45.0893 | 2025-10-16 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f37f8b2e-1263-345f-9ed8-5cbcf7f7a4f0 | -4.6811 | -44.105 | 2025-10-16 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c3321a9a-69b1-39b1-ad3b-7aa035f12bec | -4.6624 | -44.1062 | 2025-10-16 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 300.7 |
| 5b43d213-8155-3089-9b52-7a3a117cf6af | -4.4061 | -43.3816 | 2025-10-16 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 9b495981-895b-3993-9e63-1a29ab568ea0 | -3.0157 | -45.3903 | 2025-10-16 04:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 87629ec1-e37c-3dd9-948e-c908669f4f80 | -8.4528 | -44.1767 | 2025-10-16 04:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 22257d7e-7d39-39a6-865d-e69ac8bea673 | -4.4059 | -43.4049 | 2025-10-16 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| b0cf6f44-dbfd-39e7-b77c-f9df166fb755 | -4.0974 | -48.0361 | 2025-10-16 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| eb4db28f-430f-33fd-aea8-bd9f165f7253 | -5.4762 | -42.9367 | 2025-10-16 04:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 6414bb69-5745-355f-9115-95183ee1336f | -4.6813 | -44.082 | 2025-10-16 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| bad99070-3af9-3ffb-991d-b592116686c0 | -7.3955 | -39.6845 | 2025-10-16 04:20:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 89.9 |
| fadc1303-18b0-37b5-b0d4-9fe33bb5a3f0 | -6.1534 | -40.8971 | 2025-10-16 04:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| ce09e751-cb60-3058-8ec8-34e25b56709b | -4.116 | -48.0352 | 2025-10-16 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 862cb632-2bb3-308b-8c9a-9db56a7f5661 | -4.3874 | -43.3827 | 2025-10-16 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 425.2 |
| 3a13532e-2898-3e63-88ae-ade43ede94e1 | -4.6623 | -44.1292 | 2025-10-16 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 919fdff3-991f-38b9-b85c-1f1bf8e6dcf5 | -4.3685 | -43.4071 | 2025-10-16 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 259.8 |


[Clique aqui para ver as próximas entradas](README41.md)
