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
| 96d7fd91-378f-3304-a9a6-9ddad22a6caf | -19.8114 | -47.8321 | 2025-05-06 00:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f4e70094-0243-343b-b6d0-def6f50c38d0 | -14.2257 | -45.4571 | 2025-05-06 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b790e393-7948-3423-ad01-e59964c70efc | -21.3587 | -48.6365 | 2025-05-06 00:00:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| f240bc4f-dea8-3951-8c49-d2b6928af6d3 | -14.2257 | -45.4571 | 2025-05-06 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 1813a4fc-e922-34b4-916a-89ec5d32d7db | -19.791 | -47.8366 | 2025-05-06 00:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1d55cbb4-b889-3c55-b965-95450ca89022 | -21.3594 | -48.6132 | 2025-05-06 00:10:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| 25145a63-18ae-3735-82a7-62af5c268e5b | -21.3587 | -48.6365 | 2025-05-06 00:10:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 18cda6d2-c30a-39e9-8eeb-8538156134fc | -19.8114 | -47.8321 | 2025-05-06 00:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 256fa549-168d-3642-950f-238465f0325d | -14.2342 | -45.460602 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| feab19f3-ef71-3071-ad90-5b7f3610bc15 | -19.7903 | -47.829601 | 2025-05-06 00:11:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d0d33e5a-2617-3aa0-bb44-0cc49f09c60c | -14.2174 | -45.4781 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03a2619c-ee07-328d-8c46-de9509d384fc | -5.1617 | -45.1078 | 2025-05-06 00:11:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f912859-9fb2-3cac-abb2-e3bc045d25b2 | -21.3484 | -48.623402 | 2025-05-06 00:11:00 | METOP-C | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a44c31e2-a958-3933-9a91-7f32afa71785 | -20.0441 | -49.349098 | 2025-05-06 00:11:00 | METOP-C | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0116d26-0af6-3771-994b-baae61f0d017 | -20.0488 | -49.379299 | 2025-05-06 00:11:00 | METOP-C | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80df6011-de52-36ff-b2b1-919c073722bc | -21.353701 | -48.593601 | 2025-05-06 00:11:00 | METOP-C | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd88ebb6-1681-3417-b366-4a93c956e8d3 | -10.9994 | -44.345001 | 2025-05-06 00:11:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a334a8ba-74c1-3595-acf3-2ae614696e58 | -6.969 | -42.798599 | 2025-05-06 00:11:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 638d34fd-b7b3-36e7-b0af-4a64ae14ee85 | -14.2076 | -45.480099 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b20c1a5-37e1-321a-bb6f-9c2eee517d42 | -7.106 | -41.3041 | 2025-05-06 00:11:00 | METOP-C | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d1ad5a26-dda3-3286-8b1e-051384b579ed | -10.7202 | -42.332401 | 2025-05-06 00:11:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 99a84207-2460-347e-8a46-9dced951f319 | -19.7943 | -47.853298 | 2025-05-06 00:11:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 08da0095-ed09-315f-a7b8-5141c50fc8e9 | -14.2049 | -45.466599 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6c1eb73-d251-32a5-b3cc-f80b8181e38e | -21.358 | -48.6217 | 2025-05-06 00:11:00 | METOP-C | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0234c305-2c5e-3c3c-90ea-5cc194458dd0 | -5.7954 | -43.620899 | 2025-05-06 00:11:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3011a7c9-3b4f-3854-b7c4-f4518e5206f3 | -8.071 | -43.130798 | 2025-05-06 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b3f4ceb-a1f9-3877-8421-2a469265f77a | -11.1877 | -44.510799 | 2025-05-06 00:11:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e28c123a-ea77-325c-94ca-1b7239479512 | -5.1596 | -45.098499 | 2025-05-06 00:11:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5689c020-ebc4-3e61-ab9b-dd1f7e8a6f06 | -7.1076 | -41.3111 | 2025-05-06 00:11:00 | METOP-C | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5576e268-63f1-3485-a177-cc897708a885 | -6.9707 | -42.806198 | 2025-05-06 00:11:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8bfcdd85-a4b1-3e54-b0fc-6bb38efaa13d | -19.7806 | -47.831299 | 2025-05-06 00:11:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17d73fcb-9e1f-3404-8a91-014034d777ff | -5.5816 | -43.493099 | 2025-05-06 00:11:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 770bb9d2-2e99-3789-8c5b-62e3725264df | -6.9609 | -42.8083 | 2025-05-06 00:11:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8dbfa29d-1c80-3abe-a02e-e947fb0b266a | -10.7185 | -42.324501 | 2025-05-06 00:11:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2d472ab5-4eb0-3ddd-8ae0-a49d3d74ae60 | -7.5583 | -45.848598 | 2025-05-06 00:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 040d1966-1a09-3f52-be42-335152476047 | -7.5534 | -45.873299 | 2025-05-06 00:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d69a3451-85ba-35da-a787-d5e67ef644c9 | -14.2271 | -45.476101 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05eef0eb-089e-36df-80ed-8ac2ece4bbc2 | -10.73 | -42.330299 | 2025-05-06 00:11:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fc6ecd0b-2a7c-3232-8c23-62e776ed6290 | -8.0728 | -43.138802 | 2025-05-06 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c1493712-efd1-3d4a-9e6f-9295e8ef245b | -14.2244 | -45.462601 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79e3921c-41bf-3c44-acd4-a2cd328c97d4 | -10.7283 | -42.322399 | 2025-05-06 00:11:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab9789c3-a0a9-3a90-abf0-454ba79f6350 | -19.784599 | -47.855 | 2025-05-06 00:11:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3c6635bc-768f-35ab-bc1d-3cdfc9f7e838 | -5.5914 | -43.490898 | 2025-05-06 00:11:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4eb1980-b4cd-33a7-ad79-744b26e00c3b | -14.2369 | -45.474098 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4eaf0d16-5d41-3e0a-b8ab-940624f58946 | -14.2147 | -45.4646 | 2025-05-06 00:11:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7723e950-9b73-34c7-a9db-acc3025c483f | -7.5559 | -45.837299 | 2025-05-06 00:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd7070ab-f638-3b8a-9982-2976618f9310 | -21.3594 | -48.6132 | 2025-05-06 00:20:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| 62939006-b413-3026-9c67-627b2d5a6ba3 | -21.3587 | -48.6365 | 2025-05-06 00:20:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 483ab8da-d04d-3b16-92d9-4f0ae15ccc3e | -14.2257 | -45.4571 | 2025-05-06 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 84556426-081a-37c3-9f90-75f1795882ae | -23.5985 | -49.00611 | 2025-05-06 00:28:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f21a6508-fb3e-3a24-a331-7eb13e727594 | -23.60887 | -49.01128 | 2025-05-06 00:28:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 424db686-13f3-337c-8453-6f8fb2c095fd | -21.3587 | -48.6365 | 2025-05-06 00:30:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.1 |
| 48973000-07ed-3658-8792-29edcc587cbf | -6.6865 | -42.1252 | 2025-05-06 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 319228c5-9e7f-32a8-b845-bc26b4db4def | -6.7053 | -42.1234 | 2025-05-06 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| e62371b4-8795-39aa-8f65-cdd967e4502d | -14.2257 | -45.4571 | 2025-05-06 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f4d8064f-70ad-3951-a0df-1d426613e203 | -21.37245 | -48.63955 | 2025-05-06 00:30:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 39.9 |
| d32333b8-3585-3201-97c6-66a11866c2a2 | -19.79821 | -47.83235 | 2025-05-06 00:30:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9fe7234d-586d-3150-8220-f05890782c99 | -19.79982 | -47.84633 | 2025-05-06 00:30:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 67e77fcf-9664-3525-aba0-5c74b82da016 | -19.83757 | -45.02115 | 2025-05-06 00:30:00 | TERRA_M-M | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ba99eeeb-b452-3ed5-a2b4-07882ac4e50c | -21.36074 | -48.64091 | 2025-05-06 00:30:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| ccc87639-b89c-31ca-a169-4489e41b52f2 | -20.05935 | -49.35513 | 2025-05-06 00:30:00 | TERRA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 3c3ca3fc-6fae-3c29-b1b2-062e2b907711 | -20.06131 | -49.37341 | 2025-05-06 00:30:00 | TERRA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.5 |
| bbc18983-a960-31b5-8f71-4aaa778766cc | -21.3589 | -48.62393 | 2025-05-06 00:30:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| 4f401e39-ea63-350b-a8b0-53e237bc7e88 | -21.37059 | -48.62257 | 2025-05-06 00:30:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.4 |
| 46e19f14-54f8-3afc-8b04-669bfad3171d | -10.98431 | -44.43159 | 2025-05-06 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 95b72e92-6cb2-33e2-9c2e-e8f51c42794d | -14.22348 | -45.4661 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8e37b576-f93f-3306-9adf-334a249136ac | -11.19779 | -44.50885 | 2025-05-06 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38a05830-ba2e-3e39-8489-e7976fbc5664 | -14.20528 | -45.47501 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6e9c8460-4f17-3893-b6c6-4ba385f638de | -14.22224 | -45.45688 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 830e5890-10ac-315e-8247-e79eb5e666e4 | -14.23239 | -45.4648 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 42adc4cc-41a5-350a-aef6-a7f0e09d8d3f | -14.21544 | -45.48293 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b19e20f4-0ec7-377d-8f36-7814d6dfb583 | -15.25591 | -47.46403 | 2025-05-06 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6aee97fb-8c7d-3a28-a4c3-6c21c1ea7a33 | -14.24255 | -45.47273 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1fda60dd-0a96-34d0-bee2-0123f8c26355 | -14.2413 | -45.46352 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fe173bd5-c1f6-32ac-8271-a27dca484205 | -14.21418 | -45.47371 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a502fa21-57d4-3a3f-ada7-ed1ada931237 | -14.23363 | -45.47402 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| de3a29a9-15e4-3098-8ae5-7ccedbb6afc7 | -12.42265 | -43.46917 | 2025-05-06 00:33:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17d85027-4483-3907-a458-b4ab875936e2 | -13.67249 | -47.84455 | 2025-05-06 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3a9d1045-3956-3c59-a84c-6ee455aa181f | -15.8337 | -46.57887 | 2025-05-06 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 75594ba3-72ce-38de-a816-ff35f950d338 | -14.21167 | -45.45528 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e979020c-6bbf-33c5-9f6b-72cc6b83bef1 | -14.21293 | -45.46449 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4233ced1-3f2c-32ec-977b-0ce6521d684b | -11.18889 | -44.51017 | 2025-05-06 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| be7211af-b547-3b58-945a-1f8d5671f062 | -14.23115 | -45.45559 | 2025-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3df91a7e-eb90-333c-a75f-d343d967299b | -7.99229 | -44.39679 | 2025-05-06 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 22b2bc31-6ed0-323e-80f4-a70ee402024c | -8.07047 | -43.13166 | 2025-05-06 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| fc020d7d-0e5b-330e-a9fd-a8d390d6a242 | -8.30548 | -48.04957 | 2025-05-06 00:35:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9f6e6b42-c9bb-3766-a72d-3d73b0bfa37c | -7.55695 | -45.87619 | 2025-05-06 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d2aefe5e-7586-3b25-81b1-fbefa4e56ed6 | -6.94086 | -47.90513 | 2025-05-06 00:35:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa45cb3e-45ad-3890-b6b8-3263d1f6b722 | -5.16126 | -45.10064 | 2025-05-06 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8c83985f-d9d1-316a-8b5d-73434bd823bd | -8.07204 | -43.14253 | 2025-05-06 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 72e441aa-1c4c-3239-8028-b33b3547dddb | -7.56083 | -45.83949 | 2025-05-06 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2df34f73-c386-35fb-a1a6-b766c64dc707 | -8.20854 | -48.9881 | 2025-05-06 00:35:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1561eb44-94bd-3f30-bdd7-0cffce7e5fcb | -8.0802 | -43.1302 | 2025-05-06 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 4b064028-cc2d-37c4-b3f6-3a3c99658aa1 | -6.69659 | -42.13635 | 2025-05-06 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 35.8 |
| 64225335-60ab-32df-a94f-1e49647409bd | -5.58566 | -43.49854 | 2025-05-06 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 06b47111-25ee-3b8f-a0dd-b9a8f0a2e91e | -8.58885 | -45.87781 | 2025-05-06 00:35:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81174cd5-2ef8-3660-ac2e-008e612d06b1 | -7.552 | -45.84074 | 2025-05-06 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f631dca7-08f9-36bd-86f4-0b95e7cace4e | -7.71117 | -45.6609 | 2025-05-06 00:35:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cfd7d7c5-6d30-32e4-bd00-8af82ad3dfee | -7.55571 | -45.86733 | 2025-05-06 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 03c32046-d7f7-3014-8762-d4b662241529 | -6.71471 | -47.59446 | 2025-05-06 00:35:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README2.md)
