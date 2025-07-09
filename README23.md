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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d0d7f1e-8028-3108-abff-9ab8c4d7fcf7 | -15.85217 | -56.26219 | 2025-07-09 04:49:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06bde341-40b7-395d-88b9-5b53e48725ea | -17.69332 | -46.75528 | 2025-07-09 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d1990ad-d997-3f23-8ad5-c9c4d7c425ed | -19.65409 | -49.47773 | 2025-07-09 04:49:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3e93149-a689-382f-9f6d-52ee635f7754 | -21.53415 | -49.52713 | 2025-07-09 04:49:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fe3cafde-cdb9-3fa9-8061-0269feaa2541 | -21.19021 | -55.69505 | 2025-07-09 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 774b2ca0-250a-3629-b87a-692734bde9c1 | -20.86 | -55.29731 | 2025-07-09 04:49:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df1b80a3-4c3e-3b5c-8333-12390b274ef2 | -19.36884 | -51.40585 | 2025-07-09 04:49:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb1e4a7e-0474-3e22-90fc-e273f26bf804 | -16.65879 | -46.03183 | 2025-07-09 04:49:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff8cc8d9-c526-309d-a18f-86f0a1c7907e | -19.75188 | -53.99689 | 2025-07-09 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f487e0d-83c3-31ab-8a6f-2dbdf41fcd90 | -21.18654 | -48.94138 | 2025-07-09 04:49:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad84a6ac-550e-382f-aaa8-3b2a56c698bb | -21.44134 | -54.57165 | 2025-07-09 04:49:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8268306-e7b3-334d-abec-988c854282b4 | -21.7919 | -52.75777 | 2025-07-09 04:49:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 538b738a-a5f9-372b-97d5-43186dd8fd45 | -16.38087 | -54.57695 | 2025-07-09 04:49:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9da086f5-732a-3f48-aa0a-b8f01920a78b | -21.42953 | -48.64698 | 2025-07-09 04:49:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 430d998c-962a-3f61-8973-64e18b42f7a0 | -19.09134 | -56.05087 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 22e66e44-d773-3588-8946-ea6ef1e4ea52 | -19.36942 | -51.40165 | 2025-07-09 04:49:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b5af537-7f17-3304-b48a-251c4d568597 | -21.31991 | -56.12515 | 2025-07-09 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4fcd861-c271-3aa9-bc21-7f2fb25ac257 | -18.64419 | -55.72181 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ae3e5205-a9cf-334d-8a4e-1873192f110f | -21.04439 | -45.27452 | 2025-07-09 04:49:00 | NOAA-20 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f669372b-49e7-3e9d-8c08-27405d081e53 | -20.72507 | -56.65343 | 2025-07-09 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73cc3e1a-f555-3c8e-8c58-47df8553e1f8 | -19.33381 | -54.43117 | 2025-07-09 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3be67c6-0f99-3a30-a7cf-1098f2a8ac66 | -17.69508 | -46.74108 | 2025-07-09 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0f72a92-dc61-3a0f-ba72-343fcc806138 | -18.97425 | -54.38398 | 2025-07-09 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be869fec-e80f-38f7-a145-743897dec54f | -21.44076 | -54.57535 | 2025-07-09 04:49:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d23c07b-1a26-37ad-84df-eeb05cb70329 | -19.34492 | -49.92829 | 2025-07-09 04:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48f6610c-1c12-3414-bd6d-00dc4539b8e4 | -18.42467 | -53.03141 | 2025-07-09 04:49:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e13a8a8-37fd-37e7-9fb6-265e908a92f6 | -18.64228 | -55.73326 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e5a9648d-f9fc-36b4-9dc3-ba3024f124f8 | -17.90983 | -54.13372 | 2025-07-09 04:49:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee4e86d4-74cf-358a-9889-603a01a3267b | -17.69055 | -46.74036 | 2025-07-09 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6db91e28-e9f6-31ef-ad18-7f979e727708 | -21.31655 | -56.1245 | 2025-07-09 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5ee2770-80bd-3d92-a413-911a5156c9ff | -21.31602 | -56.00229 | 2025-07-09 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9ccb2467-bca9-39ab-ad5c-0260a55e4258 | -19.64546 | -49.5138 | 2025-07-09 04:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6d3fa41a-b3f6-3a15-997b-18e422f706bc | -15.88612 | -58.55796 | 2025-07-09 04:49:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1ce6cc12-b4b0-305b-81b2-a24e42991e41 | -17.69449 | -46.74583 | 2025-07-09 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c247269e-3a4c-3a85-977a-89c7c791ed15 | -21.53462 | -49.52343 | 2025-07-09 04:49:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f625c76c-c15e-3192-ab82-01a554e44400 | -18.08974 | -54.28381 | 2025-07-09 04:49:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b8b6b70-ed18-35ed-bdc9-9e772fcb45ae | -17.68996 | -46.74513 | 2025-07-09 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2652a950-6877-36f9-89bf-3cf57fb8c62e | -17.77623 | -42.80927 | 2025-07-09 04:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd0bcd74-3ee3-337b-959e-b6cbbedfb2a3 | -19.1586 | -55.32756 | 2025-07-09 04:49:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ff89c00b-b144-3a08-8c40-fb666439b923 | -18.63742 | -55.72056 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ff059e01-4b11-38b9-a481-2040760d2a9b | -20.72851 | -56.65405 | 2025-07-09 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de81ec84-e290-3bc0-a802-db47618d0e29 | -18.64356 | -55.72562 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 5f742dc5-0016-39cb-9dfe-90a9524d7287 | -17.69114 | -46.73557 | 2025-07-09 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0e1a1b4b-f3be-342b-8c29-af6672bf65fb | -18.41636 | -54.70721 | 2025-07-09 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04512e52-8240-3008-8aa7-8ee3cbe95630 | -21.04514 | -56.00096 | 2025-07-09 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 928abb50-0391-35dc-8f8d-a6ecef66625b | -18.64017 | -55.725 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f2598788-66fb-38f9-ac20-9ba0614c0d32 | -18.64292 | -55.72944 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fb559727-6f54-35aa-b0a5-e8784bea948c | -20.42426 | -54.60188 | 2025-07-09 04:49:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70806f7e-f89d-3187-a6b0-d004aedb7685 | -18.64969 | -55.73069 | 2025-07-09 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b3f03e0a-742e-3efd-a607-c16c4f784895 | -8.5025 | -43.285 | 2025-07-09 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 169.3 |
| d65ec0ad-f52e-311a-934b-7a26a9c54f19 | -8.5214 | -43.2828 | 2025-07-09 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.7 |
| 16244b36-1dc1-3286-be66-7e31cfd81a32 | -10.5776 | -49.1316 | 2025-07-09 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c7f44e09-e3d1-315a-9c6b-ad038ddb6333 | -6.1792 | -48.0494 | 2025-07-09 04:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f2b7a9cd-57a0-360c-a981-f0271fce7f28 | -8.5028 | -43.2614 | 2025-07-09 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 94ca4aa9-af47-3c89-8709-96cafb6a266e | -8.5217 | -43.2593 | 2025-07-09 04:50:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 856453b4-3cec-3a2b-bbbb-3a5227df57a5 | -22.62222 | -47.9167 | 2025-07-09 04:51:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 748d1a9e-3024-3175-bfb6-8a92e4078611 | -24.24149 | -50.74141 | 2025-07-09 04:51:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 60d5fdac-08d5-3a03-90bd-5b6bdab329d3 | -21.59164 | -57.60503 | 2025-07-09 04:51:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f6b0345-4221-3fd3-9463-e02e6cd777a9 | -29.33728 | -52.34583 | 2025-07-09 04:51:00 | NOAA-20 | BOQUEIRÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4302451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b3ea8393-9982-3fe6-a77b-0c7646706227 | -22.61772 | -47.91612 | 2025-07-09 04:51:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5a4f0b0-a563-3218-a205-1495819326dc | -23.10971 | -55.14972 | 2025-07-09 04:51:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e5c3aabd-745e-3954-b6f4-fa2727483e8b | -22.53794 | -48.81338 | 2025-07-09 04:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 696567b1-7135-3eca-8cc7-e5b436984bf6 | -24.74196 | -53.80932 | 2025-07-09 04:51:00 | NOAA-20 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 220ccf51-c2c4-3203-9546-2ce9741f0bea | -22.61826 | -47.91121 | 2025-07-09 04:51:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72b489fe-fc08-3795-98b8-152365299a43 | -22.20226 | -52.67841 | 2025-07-09 04:51:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0fa905fc-7cea-3dea-8f24-3dd8e7f1705f | -23.59412 | -47.43938 | 2025-07-09 04:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 27fa52d0-41ab-3e6b-9028-c30eb9c3c27a | -23.54912 | -47.63634 | 2025-07-09 04:51:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1bacc10c-72cc-39bb-8aea-14f6473cebae | -8.5025 | -43.285 | 2025-07-09 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 183.3 |
| 6316f1b9-ea2c-3c89-a72f-083fc5a095ca | -6.1792 | -48.0494 | 2025-07-09 05:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c264e7c7-d1cf-38de-a94e-8a14f5e75046 | -8.5214 | -43.2828 | 2025-07-09 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 165.9 |
| db418eac-e2e8-3c46-9858-d0c4ef325460 | -10.5776 | -49.1316 | 2025-07-09 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 848212ec-cd6a-397c-8cde-9371b4d668d2 | -11.4397 | -45.0923 | 2025-07-09 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 292931ca-3cf1-36e0-ad06-c96bc604d15d | -11.4393 | -45.1154 | 2025-07-09 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 7b10a907-f562-3b5b-a37d-9853b5301f63 | -8.5217 | -43.2593 | 2025-07-09 05:00:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 256c70d6-780b-3825-9b09-b50879aba531 | -8.5028 | -43.2614 | 2025-07-09 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 22dad098-52ad-37f7-be61-5b59be6944b4 | -10.5779 | -49.1098 | 2025-07-09 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 13230637-53c6-3876-9aad-b7c73b30d09f | -7.24024 | -43.05211 | 2025-07-09 05:04:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 2f47d58e-5958-3cf7-8749-e8c2c2b32ffc | -16.62408 | -42.20883 | 2025-07-09 05:04:00 | AQUA_M-M | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| db6b4ddf-8163-37cc-a0e8-3f18cc5e4852 | -8.50106 | -43.25628 | 2025-07-09 05:04:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 77d5c385-52bc-38ca-90d3-cbd6953a3dd5 | -7.23617 | -43.0767 | 2025-07-09 05:04:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 66f3a43b-bdfa-310e-b487-77e711e17989 | -8.50882 | -43.25238 | 2025-07-09 05:04:00 | AQUA_M-M | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 1764f3fe-c173-3899-8273-55d6518d05a3 | -11.6736 | -43.76335 | 2025-07-09 05:04:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9700339c-e065-3cad-adb0-34cb52e782e0 | -8.4969 | -43.27998 | 2025-07-09 05:04:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 5f527949-1ab5-327e-b839-92fd01478451 | -8.50482 | -43.27632 | 2025-07-09 05:04:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 513.2 |
| 3d3f9d60-dabd-3e0d-8efc-6571526d57a0 | -8.515 | -43.25859 | 2025-07-09 05:04:00 | AQUA_M-M | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 5471808e-84b3-3d7f-812c-20eb86c68c41 | -11.66957 | -43.78695 | 2025-07-09 05:04:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| bf107075-dc58-3dae-a527-4cbc7c81db1e | -8.50663 | -43.30655 | 2025-07-09 05:04:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 2ae7cb43-fb19-32c1-94df-036da04d215b | -11.67885 | -43.77197 | 2025-07-09 05:04:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 2d48ba37-5626-3eca-b486-6c0bee5c5adf | -8.50078 | -43.30043 | 2025-07-09 05:04:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 1437c9a4-3d22-34c0-a3bf-3f279121bd59 | -8.51083 | -43.28244 | 2025-07-09 05:04:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 319.9 |
| 89f4711d-5860-3ce3-a6ee-c1990dc4057a | -8.5214 | -43.2828 | 2025-07-09 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 4c383097-89ec-3b3c-848c-4edd22517e26 | -6.1792 | -48.0494 | 2025-07-09 05:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 582a93ab-736e-367d-9bcb-37412dbe8c6a | -8.5028 | -43.2614 | 2025-07-09 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 996236f1-81a9-3596-a73f-448dffdccd7d | -10.5776 | -49.1316 | 2025-07-09 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a2d7f4d6-0c1d-3088-9d74-cadc2f88445d | -10.5779 | -49.1098 | 2025-07-09 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a3748a58-26dc-3856-b3f3-9d1c327afbab | -11.4393 | -45.1154 | 2025-07-09 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 1815ca68-c445-35e8-8efe-3e5183b8eabc | -11.4397 | -45.0923 | 2025-07-09 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| eed89dbf-99a3-3d9e-ae72-5fce13ddd080 | -8.5217 | -43.2593 | 2025-07-09 05:10:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| c5e5be7b-403b-34f3-bab0-8f653ae5fa99 | -8.5025 | -43.285 | 2025-07-09 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 216.5 |
| c2bf7af8-33d4-370f-b5d6-035db0bc80db | -8.5025 | -43.285 | 2025-07-09 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 197.8 |


[Clique aqui para ver as próximas entradas](README24.md)
