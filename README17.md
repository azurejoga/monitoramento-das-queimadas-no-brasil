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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1bbba14-7c0e-3bc1-81ac-1a6b2a2d6d94 | -11.44917 | -52.92635 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c1ea4ce-5065-3162-987a-8274486feed9 | -6.93601 | -43.70586 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| edba40c7-bf29-3e39-b3c6-a6ecf97351b7 | -5.80409 | -43.80375 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddc895c6-3e24-3238-b8fa-e1c51cec73e8 | -11.04978 | -49.6014 | 2026-07-07 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2ad0f12-4dd0-38f2-abf6-d09f52cffdda | -11.6966 | -44.12974 | 2026-07-07 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 861c8983-2e80-3221-a200-cbe359d280d1 | -10.20316 | -61.48242 | 2026-07-07 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d33db371-6ed3-3629-801e-06b0acfd817e | -6.42926 | -55.79589 | 2026-07-07 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 927c17b7-cf6f-3f9a-a9d5-142a80413dfe | -6.20235 | -42.5178 | 2026-07-07 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ffa10c4e-746e-3af7-abee-b241a0763e59 | -6.29373 | -43.64142 | 2026-07-07 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d41eb893-f27e-33f9-9a75-2a61f10ff514 | -11.68547 | -50.38071 | 2026-07-07 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97bfbe7f-abbf-3bc9-9d5d-0acbdcd9c239 | -5.82205 | -43.59182 | 2026-07-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 430c83b6-4bf9-3681-a7d4-c58359acd100 | -11.6787 | -44.55176 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3c48444-5800-36f5-8acc-9fe8d650b69c | -11.99492 | -45.14041 | 2026-07-07 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dfe0318-8d34-3f7c-bc42-3a877695b7d3 | -12.7911 | -44.51192 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0db4d409-c09f-3f20-b93f-44c9d1b6ea64 | -7.71864 | -49.64177 | 2026-07-07 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9513fc28-cbed-3a5e-af13-b1c2f82f259f | -9.23681 | -50.14083 | 2026-07-07 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac27f6ca-7a0a-3f4f-a71d-0ec38150dd15 | -6.89626 | -43.70828 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95fb4a1e-a920-34f1-a6ae-af84d10e3056 | -10.31939 | -49.90968 | 2026-07-07 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73c92894-f365-3d74-ac93-b091f48253cf | -6.92314 | -43.70397 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e090d68-66d6-33c2-b659-4b23b9e9cddc | -12.68388 | -48.21445 | 2026-07-07 04:44:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 064f3ca4-3cad-35d6-a125-e9fe27cbf1f2 | -11.65849 | -44.57037 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30428696-d121-3fad-8d8d-2e1ac15ee6cf | -10.89826 | -56.85294 | 2026-07-07 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f4ee3ae-0bbf-325c-ad80-e9bfa711673a | -11.6651 | -44.55413 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba911a51-19a4-3d40-8a72-4af6b31c4870 | -6.89758 | -43.70921 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7700260-b291-372a-b99a-83febee59aa2 | -12.75486 | -44.54727 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a76c4b2-82b3-3a72-8829-2b22f1e46407 | -8.70549 | -50.0839 | 2026-07-07 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6102de6e-04f1-3103-be58-61ead5430a5f | -6.89569 | -43.71231 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7b69abf-1ed7-3b19-acfd-f28c70ece1b2 | -9.73046 | -48.26899 | 2026-07-07 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f00a73d-6a4a-3391-b2aa-c6e6139c302e | -6.91397 | -43.70684 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 06404e32-69aa-3799-a384-79ce3c528f2b | -8.11595 | -47.11047 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49546c4d-2aea-38ce-b28e-32ca0ac88bdb | -6.90111 | -43.70492 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c291d9c-3b97-3601-86a7-dc10123b5da8 | -8.07577 | -46.6885 | 2026-07-07 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8a2eefd-282e-38f0-b744-cf60c80088da | -12.78667 | -44.51132 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3fefa08-a033-37ab-87b7-61d534dbd010 | -6.29431 | -43.63739 | 2026-07-07 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69365a5c-7617-31ae-8a20-f613e0be4d6e | -7.01145 | -42.78336 | 2026-07-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a60bcb8f-d8e6-3465-9c18-63a36975ea9a | -11.91916 | -43.3752 | 2026-07-07 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 324a4a78-ac9b-38b1-9ca7-b10caf2a7292 | -6.93661 | -43.70175 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21a133c5-cbe7-3ad1-a4ba-5e64bce091b9 | -11.66716 | -44.57161 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b74e66fe-e7e4-337c-b575-3b775e2ec162 | -10.31885 | -49.91319 | 2026-07-07 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d6dc8d1-24bb-3a4e-bb66-30052250680f | -11.66831 | -44.56317 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32809e7b-f127-3554-a757-abe0cfe3caf8 | -12.68092 | -47.67455 | 2026-07-07 04:44:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 465884de-f30f-36d5-b103-b119fc76b7ed | -6.50015 | -42.23536 | 2026-07-07 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3341b746-03e6-3546-91d7-43f98bacf1b9 | -8.07203 | -45.58094 | 2026-07-07 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 023891bd-ebd2-32f2-9fe0-1bef0ce37840 | -11.68739 | -44.55299 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef616da2-5b22-3c24-bf89-f3bb93aaec06 | -11.04699 | -49.59731 | 2026-07-07 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f20c47-7ab9-36dc-8770-794e9022e8ee | -11.84727 | -48.25118 | 2026-07-07 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6def8d47-3b95-38aa-b7c8-cde1eae3ee21 | -12.45081 | -49.57981 | 2026-07-07 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfe439a1-c7f9-3433-a20d-5661c6133a23 | -6.4249 | -55.79515 | 2026-07-07 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40f2cf6f-1764-3508-9003-614a426c1bc3 | -11.68304 | -44.55238 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7937d164-34fb-3ac6-964f-571766f6b8bc | -11.66283 | -44.57099 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33b028cf-71fc-3dd7-af0a-fb18c44e9bd0 | -8.12304 | -47.11161 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9128b166-729d-32f6-99fd-01f687311ae9 | -6.92197 | -43.71217 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c590ae7a-e792-30d4-b147-ca405050eb2d | -7.74983 | -49.46543 | 2026-07-07 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb02649b-9a0d-3b11-adbe-89e46794652d | -11.66076 | -44.55351 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b0099c9-f97f-30e2-ad3e-19e6c542b870 | -6.42853 | -55.80008 | 2026-07-07 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 622fa6ad-efda-3f99-902c-fd311c9429cc | -7.90569 | -48.2481 | 2026-07-07 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4354836-9dc1-334b-bfa8-c9fce769ffaa | -5.79865 | -43.80416 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b81d855e-4374-3bdc-9291-4f5d642bd81f | -8.12633 | -47.11131 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5aed228f-c2d9-3529-818f-a1f99488d800 | -11.99545 | -45.13649 | 2026-07-07 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2c9e075-7fc4-3193-99b5-58604a886979 | -9.37191 | -48.55315 | 2026-07-07 04:44:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82de0d86-44da-343a-acf1-5614f1e72782 | -10.20237 | -61.4865 | 2026-07-07 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41bb9f76-aa30-3a3e-9b26-b8fdec0018b0 | -12.79348 | -44.49429 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f399a4f7-ff74-3ec7-9849-0c14a5f66ffe | -6.93172 | -43.70523 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 276c0cb2-0c59-3ebd-99a5-71e24f0756e4 | -11.68189 | -44.56081 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 151e0ded-7ae1-3109-b871-b0f36d105969 | -11.65529 | -44.56132 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9f70f5a-9a50-340f-bf53-540c4cdebdb7 | -8.34189 | -46.48358 | 2026-07-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1322f4ad-ef34-3bee-9c71-4db6df959a3b | -7.9023 | -48.24757 | 2026-07-07 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ace5fb57-db0d-3376-8230-2eb0500e487e | -7.90908 | -48.24862 | 2026-07-07 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa79f94f-8ff1-30d6-acd8-e7abb03265e0 | -8.03873 | -45.04065 | 2026-07-07 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6efb2668-c325-31b2-8e9f-ce423a9ed54d | -11.44679 | -52.92673 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4d473db-cf23-36a6-acab-90d595424ed9 | -10.82963 | -49.37588 | 2026-07-07 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6119442-2e5b-3ae0-a9df-c49aa4ba1d6a | -12.75927 | -44.54787 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4999b313-472d-35a2-83f0-8ceb9925f16d | -7.64074 | -50.02692 | 2026-07-07 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c286e62c-aadc-34cf-9bb2-b73ac896a8f9 | -6.90554 | -43.71459 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37669a24-2b5d-3cf3-ac6d-5c6a939dd293 | -11.68216 | -50.38017 | 2026-07-07 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66c75e47-66cd-3ebe-a43c-62f26a9b4b05 | -8.12242 | -47.11562 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19540dbd-eb04-3837-8f44-24f88d0bf856 | -10.93556 | -43.06582 | 2026-07-07 04:44:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 3ed57f29-bf95-32a9-9e86-d647390b0a6c | -6.47559 | -42.93547 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f96730fa-58e4-3287-938e-289120e562f5 | -12.50663 | -48.26434 | 2026-07-07 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dd6f5b1-481b-3e25-9041-45c728af179a | -9.22404 | -48.58395 | 2026-07-07 04:44:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 228a0267-e76a-388d-bd0e-273e2d181a2f | -10.76583 | -46.6325 | 2026-07-07 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3be5ff0-1971-3bbc-a223-50b2d3cc23b2 | -9.28473 | -49.57655 | 2026-07-07 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64bc2d01-9bd5-372d-8ecf-473607b2760b | -8.03474 | -45.04006 | 2026-07-07 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c35f40a3-f653-3108-9c40-7df4367bcbd1 | -10.86338 | -46.35868 | 2026-07-07 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80024f4a-8c4a-3e53-b078-edd06f57894a | -6.92626 | -43.71279 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 62e8a213-01ac-372b-8fc8-ee14fd3b82a2 | -6.93543 | -43.70993 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eef7b95-8494-3c29-9129-1d903cb2f15d | -6.91339 | -43.71092 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b727d997-8015-3319-860f-7bc1baaaa5f6 | -6.49611 | -42.22984 | 2026-07-07 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 365701c6-74f7-3e29-9abc-25af2b2a09d2 | -12.78845 | -44.49812 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 74928a4e-be05-3878-b1cb-c02748a07c03 | -11.65963 | -44.56194 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2ce4da6-2e03-3946-9710-7a57d6522c0d | -12.79023 | -44.48486 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dc7a7148-9771-3795-88d4-b80a4c4e5241 | -6.9054 | -43.70557 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 54f092be-0043-332d-8f34-d76e01b605c0 | -8.07216 | -46.68792 | 2026-07-07 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f9282d3-8dcb-3985-8ea8-8af919e630b1 | -7.10382 | -46.51631 | 2026-07-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 457844fa-0e32-348f-b8cb-d9aba869ef1c | -11.05542 | -50.86452 | 2026-07-07 04:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48124715-11e5-3372-96d0-f41a2728d2d4 | -10.9308 | -43.06517 | 2026-07-07 04:44:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 772094ef-ae94-368a-9614-f9bd5748dd14 | -12.67207 | -48.22096 | 2026-07-07 04:44:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39f9a941-8f44-3343-9aef-7af532c557a1 | -6.92255 | -43.70807 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3bba7b0a-d1e9-3100-acf7-6b8d48cf9d6c | -11.65906 | -44.56615 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6e85769-87aa-3b33-9932-1d68295d1c38 | -6.90211 | -39.55182 | 2026-07-07 04:44:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README18.md)
