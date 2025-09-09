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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d61ecc34-8e8d-3c8e-b0f0-2c755cf5bb07 | -14.53212 | -48.76571 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b30c7495-152f-3af7-916b-825d8abe390c | -16.70032 | -48.63873 | 2025-09-09 04:36:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf9b8fdd-93a9-3e08-a1c6-90c633577198 | -20.02841 | -48.53275 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc28ce07-65ac-3cc9-978b-6c7c085a21ef | -15.27191 | -52.35683 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b96bfba0-40a5-31c9-8e97-bf1ab694f2a0 | -17.29907 | -46.72258 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b5a5ea0e-ae0a-35c1-a0e7-f740cb17cd88 | -15.27257 | -52.35287 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f273f009-7914-387c-8022-eb2782e163e5 | -14.74612 | -47.78394 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3d4e10ad-dea2-349a-aa96-7ee361ed443a | -17.6804 | -52.27126 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fe74eb4-1ef6-374d-b3d0-3f99ccba7d7d | -18.82734 | -49.67287 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9bd5d7c6-bc84-367d-ab26-c4eefa9b2d46 | -13.10943 | -56.80626 | 2025-09-09 04:36:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fc6a6b1-2830-300b-b4de-f2c946979f4f | -15.25647 | -53.81155 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 788743a6-0f5a-31ab-92c5-76be1389a777 | -14.68925 | -48.7115 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6e24155-727e-3a65-9106-eb412b953bac | -15.73483 | -53.58855 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c6f31f8-8832-3642-8656-3082b1d71621 | -15.27333 | -53.79479 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c65d31b-0f78-3a13-9e03-1a47ded880ba | -16.90168 | -45.813 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35cf3a87-faeb-3138-8e7f-697b9fcf3bce | -15.53855 | -48.39436 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cad126e-4be2-37da-bce0-a609c15b8ab8 | -15.24927 | -53.78687 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2bf1e47-f3f8-3e6d-b50f-94b1f8d2308d | -13.90615 | -53.96936 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d856f1bb-3fa8-32c0-b0c6-833b76ebf887 | -17.37582 | -49.23148 | 2025-09-09 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 134d3b3f-1d9f-345a-add8-ccc99930196e | -17.67615 | -52.2548 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed98e3e5-4f7c-303e-96b5-b6ea525ff7c7 | -15.52783 | -48.39643 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 710f7ca2-d057-399c-8ea4-8e1698304a5e | -17.2694 | -46.74598 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ddc61a4a-f07c-30f3-866f-0005218b3061 | -19.58277 | -47.3966 | 2025-09-09 04:36:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eeb81c8a-d372-3bb9-9fec-cf786c0a02ab | -17.26818 | -46.7272 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 340c59c2-17bf-3958-b8b2-e5d48dbdf41d | -14.54099 | -48.75238 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff6997b3-7e0e-329e-b8d6-020954597b1f | -16.07553 | -50.48139 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d46b5bed-876c-39ec-b2ae-6075b5eb7e79 | -18.0126 | -47.12175 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4dc279d9-fc9c-3cca-8c53-cad99bc81be0 | -14.54603 | -48.76424 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1e382f3-d1fb-385c-8d92-71383877b953 | -16.43633 | -49.2886 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65c92902-5382-3b9e-b740-95678086ab76 | -14.35951 | -60.31106 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 586825e8-cdc7-3009-a2cb-3ccfb84870ef | -15.21099 | -43.8224 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6a05893-4b18-3559-81de-54ed7aeb87e4 | -16.69805 | -48.6306 | 2025-09-09 04:36:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8d31130-4412-3a52-868d-dac0a6d3a40f | -14.53654 | -48.73669 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e24f7e9-cc79-3a64-bf1b-d73dd38dc940 | -15.52894 | -48.38898 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2012cf1f-4e99-38d9-a9c6-5ba467715b7c | -18.77864 | -48.19993 | 2025-09-09 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f3df807-2b71-3d8e-b3ed-7901adf3e08c | -15.78597 | -53.53077 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f58ae32-8f13-3bc5-8491-a6d4a8325617 | -15.0521 | -50.13125 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67c7ed5f-3bb1-32e6-af39-e3b84de24520 | -15.05871 | -50.13235 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7ed4877-5106-3fb3-8e8e-8c3a4daa81f4 | -16.51949 | -51.76495 | 2025-09-09 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a6c7bb4-66e7-3201-97fa-551064f7ceee | -15.73388 | -53.59023 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad8d1b0a-e098-35ca-b192-363d7ba0b735 | -20.91636 | -44.04977 | 2025-09-09 04:36:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 12518711-347b-341b-ae2a-9c228639cf31 | -15.18506 | -48.06079 | 2025-09-09 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7344919-b742-3966-bdf0-660ef4e7584a | -17.34532 | -43.5816 | 2025-09-09 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d58187c3-d9d1-3034-8c1a-d9861d9f7e11 | -15.83244 | -48.94503 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 07da21ae-212f-33ef-8fa1-42044fec5078 | -18.78324 | -49.64657 | 2025-09-09 04:36:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26326086-c4c2-357d-a148-7796e1c9ec24 | -20.45082 | -48.06148 | 2025-09-09 04:36:00 | NOAA-21 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f89942e0-4a24-3c38-8af8-d3e69e7cff57 | -15.17581 | -47.95772 | 2025-09-09 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1324e967-8ab5-39f9-95e9-5a591346ad91 | -16.51613 | -51.76436 | 2025-09-09 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd227f96-5aec-3250-b8e6-cf8b7020a58d | -17.67153 | -52.26178 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f35eb080-adaa-3b1e-97ef-35661d7bec5d | -14.86729 | -46.68499 | 2025-09-09 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ec7106b-17aa-3d56-9dfe-34e4d30c417d | -15.74413 | -53.52971 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cab8c10f-314f-3ac9-9fcd-b410713162c0 | -17.41214 | -49.12691 | 2025-09-09 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cc4f10c-ef9c-392b-abe6-467dfe5c304e | -14.71605 | -60.24842 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8e112fa-d3a1-321a-ad22-ca6176d47d70 | -18.73791 | -49.6358 | 2025-09-09 04:36:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a0ec263-e4fd-3341-8338-9d4ad7f64391 | -16.32314 | -52.92122 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c27eb8e-45e0-36cb-bbfb-60fef5410249 | -14.83845 | -46.69589 | 2025-09-09 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d206205-66da-34f4-8f30-d87af17314bc | -15.78309 | -53.52589 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40230836-a882-3384-aa7e-6f16de8850bc | -15.7896 | -53.53136 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee1bc1e0-93e6-31df-a936-0d05eb740dd5 | -14.54433 | -48.75294 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ff84ab6-25ad-3d1d-8453-90265f647528 | -14.51818 | -48.74493 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de4a5185-aa1c-30a3-b282-ba241f4aa73c | -18.83069 | -49.67344 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5b35e5af-42db-3ff9-a7f7-06abe7143172 | -15.11044 | -48.04526 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4da7828-1aa5-3c74-ba2b-cd86a0b926d1 | -18.73512 | -49.63149 | 2025-09-09 04:36:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edf5d3dc-4e1c-34fa-a332-e6ba562dcdd9 | -15.54246 | -48.36803 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfb7f3fa-db20-3d26-a1d3-c2a1dbbb79a9 | -16.08045 | -50.49321 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 912f3f49-d599-32ba-a4c7-66a950259f7b | -17.80552 | -47.62005 | 2025-09-09 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11867b5a-942c-3c14-b01b-7a99ffdc8012 | -20.07966 | -47.35529 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f89a6830-871c-386b-9fed-8fedc85e8fc1 | -15.26911 | -52.35228 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 885500f9-813b-38fb-8a33-7bfb4375d7a8 | -14.53598 | -48.74034 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9134d59c-91a0-39ec-ba70-f31acf2b65f6 | -15.73195 | -53.58368 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f61fbc1-7957-39fe-8be6-45555f799752 | -19.35843 | -47.45536 | 2025-09-09 04:36:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 230d4d83-cd58-3d75-b54e-4088efe2bd71 | -19.19045 | -45.67164 | 2025-09-09 04:36:00 | NOAA-21 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 221338a8-cd5b-3f9e-9a33-2833458c7260 | -15.25218 | -53.79207 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 507be4fc-46b3-3def-b641-5055a99c7156 | -15.25664 | -53.78822 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 745e16cc-b317-327b-bc4e-c35799921193 | -15.87149 | -52.3439 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64dc57ee-957a-3677-b644-2df7d20d246c | -15.83349 | -52.25679 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 256e70ae-9604-3dc6-acf7-2b757e7ec528 | -15.2948 | -43.38073 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3281398-806c-36e4-bcfe-f8ab6784fe92 | -15.52615 | -48.17145 | 2025-09-09 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11e80afa-2342-3ea5-8b97-c369f9f03d88 | -15.09851 | -48.05516 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb10f045-da5c-3fbc-bbe0-a958be17cdfd | -16.30536 | -48.89526 | 2025-09-09 04:36:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7939b616-7fa8-3b3a-a989-8afc18724965 | -16.63184 | -51.84959 | 2025-09-09 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cafcde7-86ea-32da-b7a9-30245f1a11d8 | -15.77868 | -56.42883 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f88a8cb5-5def-3d52-9fbf-c771290480b0 | -14.37188 | -60.30823 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 806e0c89-3f27-37e4-b7de-4d6c90f11f6a | -16.32384 | -52.91711 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45c3cb40-a911-3332-9e10-6ecedba6a59f | -14.93086 | -55.82908 | 2025-09-09 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d37e4f8d-8d57-37b8-ac79-ae9f3137516b | -15.53624 | -48.36312 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e4d0fbf5-5186-371d-b3d0-8b441eace17b | -16.62905 | -49.13907 | 2025-09-09 04:36:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84cbcaa9-d235-35a9-9f5e-b5da83ede00e | -20.91607 | -44.05062 | 2025-09-09 04:36:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d910ce2b-ce8b-353f-b1f2-6bad8c75aa02 | -14.7392 | -47.75912 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adbcc302-c100-3d82-ba92-bf082d648d61 | -15.25724 | -53.80703 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af883159-f404-3cb5-b559-b0f8d880986d | -15.05541 | -50.1318 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eafc4344-6a79-3975-96f2-f683724d83ce | -17.15802 | -44.45291 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05684046-49f0-3111-81b9-20a97cd4fc3b | -15.78372 | -53.54378 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69d7892b-9690-3929-a664-f04f7db8055c | -18.33981 | -49.39235 | 2025-09-09 04:36:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e700394-7fc5-3914-9695-b05211bb6f4f | -15.05927 | -50.12879 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71451a63-3126-3a41-86f0-51cca8635820 | -15.04992 | -50.1236 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a80958da-1b8c-3d1e-9fa9-1796d3151c84 | -18.8078 | -49.64294 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26ed5af9-fa3e-3e29-874c-0d5d5750869a | -16.88951 | -45.78555 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 637b645a-4e02-3467-acd2-bb7cea045ae5 | -19.69814 | -49.28297 | 2025-09-09 04:36:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7488668d-037a-3758-8a08-03bca754a663 | -15.54812 | -48.37667 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README49.md)
