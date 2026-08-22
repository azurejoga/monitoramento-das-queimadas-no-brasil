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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da8f6999-b648-35ca-b50e-82c0c8ebadf6 | -17.97002 | -44.37054 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8aaef24d-12c5-3b00-833c-5114aaf88161 | -15.05135 | -48.69427 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f73104a8-9b39-3566-9b7f-8de681458b8b | -14.14983 | -48.35513 | 2026-08-22 05:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26c93f0e-1ee1-38b1-9c0d-5f40272ec003 | -15.3448 | -52.92705 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f8ae585-a436-3699-9840-c9b9d1532374 | -14.0092 | -53.6869 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68436f32-e42f-3541-94e8-f35875b3680a | -14.18369 | -53.02286 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c1a17a6-a02a-34fb-8200-b5b270d8ab46 | -13.69363 | -51.85974 | 2026-08-22 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 639cd12a-4921-362b-bd61-4cb1669652c2 | -13.99806 | -53.67036 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 792aa8e2-1ec7-398f-bdf9-c9405d24e589 | -14.01366 | -53.70235 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cd8646ee-2941-3abc-bf72-0ffc77b45208 | -14.54951 | -53.00307 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c6c66b0-f5d1-3f6a-941b-ea0215c39cfb | -14.3147 | -51.86663 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f69929f-4a7f-3735-9f6a-98f863287f05 | -14.54895 | -53.00681 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bee42894-5722-324e-ba94-68b6c7575108 | -13.987 | -53.68363 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8a0a3e1-8099-3b7c-b968-c802b33540c7 | -16.48374 | -47.94749 | 2026-08-22 05:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ad57423-7c05-3591-92d7-32b0fdef12a4 | -17.56334 | -47.88476 | 2026-08-22 05:06:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f16a8c6c-7072-32e2-a0c7-3e140952b478 | -14.13869 | -48.06664 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f510fd0-5dd5-32b5-9e2e-2ba825d69b3d | -18.26886 | -43.7005 | 2026-08-22 05:06:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa8df6f9-1c73-394a-a979-7776669d7c5f | -17.91418 | -44.41243 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52702361-0236-3a63-a472-2634939bbe1e | -15.20119 | -52.77292 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 249a4cd1-90ee-3c7f-badd-057fb30835b3 | -18.75986 | -43.80595 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 776fcce7-17d2-31bf-ac64-8c6c25dc91e5 | -15.21695 | -52.77866 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f45295b7-58cc-3b77-a693-6d865f5cc33d | -14.38893 | -51.79715 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6cb12230-4466-379a-908b-06d92689e5d0 | -17.92009 | -44.41322 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 881b658e-aa1b-3db7-afaa-f9bec4462c90 | -15.2457 | -52.84572 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a22ffbe-8a08-3117-95cf-baddf57d2e83 | -13.87723 | -53.9924 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcbcfc85-7964-3b7e-9378-992182c24dfa | -13.83839 | -54.0007 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e99702ac-24c1-386a-b62c-1d5266d36463 | -15.20347 | -52.78117 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd5170f-6f77-3487-b6d7-06790e3f820b | -17.8452 | -44.46931 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3d289c7-1234-37b9-af0a-91ffb4fdac6c | -13.95123 | -53.84696 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 952feb14-2c7d-386b-8845-71c171b1b94b | -14.97464 | -52.65547 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33a15c26-a563-3724-a9eb-ffafcfa349db | -13.40576 | -54.3671 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5650f03-1f7f-37d0-ac6f-1ad445a4531b | -13.98867 | -53.67286 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cdb53a8-c1cd-3bfe-b7ad-757d3c80fda1 | -19.64676 | -46.03785 | 2026-08-22 05:06:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d172ca18-b3a7-357c-8ca2-6be48471c0e5 | -15.18644 | -48.74961 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fef7a05-7dbc-3ca2-a9d3-33b623691153 | -17.9146 | -44.40825 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f67c00ed-6620-3568-8ec1-92068e8bd086 | -17.96101 | -44.36518 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a9c5974-50d7-3421-9e64-a0f3a6d26cb2 | -14.31824 | -51.86721 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a95bf1d-8f44-3cc6-8589-d7ac25e3bba4 | -14.39189 | -51.80181 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9a50b02a-2a55-398c-b382-345ec8bbbd4b | -18.91988 | -43.5974 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 436d7144-e30f-3dc6-87f5-7ac06dac273b | -15.86254 | -55.55067 | 2026-08-22 05:06:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85fa4a4f-eeaa-3d4f-9204-cfcfc76d473d | -14.32252 | -53.00553 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 308e914a-b78f-32fb-a18e-138355ff7c9d | -17.96489 | -44.42315 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c75461f9-42b8-327f-a4a7-1b0aab39451c | -13.88112 | -53.98939 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 495ae0b9-ed55-3913-b84a-52537e1b6ba9 | -17.9734 | -44.36163 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92783518-1feb-37ca-8ab6-16a9dd0e9966 | -17.97049 | -44.36575 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34d35520-c060-353d-8e4b-6f33a88efd83 | -14.00586 | -53.68636 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb42cf63-2816-31d8-a8ff-21403c4b7bc1 | -14.55743 | -52.99675 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 238b8327-247f-386b-97e5-b0a547824d03 | -14.13371 | -48.07022 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d93c93a2-c463-3697-85a6-8187fa6320f4 | -17.97081 | -44.42379 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c28fde6-eec4-38de-bca2-414003f299d8 | -12.95283 | -56.63597 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cd34ee2-273e-378e-9ca8-35f40cf015d6 | -18.76431 | -43.80281 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2603188e-c89d-3a70-b73a-702a91c89b85 | -13.8197 | -53.99742 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c43cdd1-1158-3186-b3bc-307602cfb7e5 | -14.14222 | -48.06901 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bee6cf55-285f-34bc-95d5-c990bd9e5484 | -18.26936 | -43.69521 | 2026-08-22 05:06:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c933912b-4d6f-3f9b-badb-1f950f3e3580 | -13.38137 | -54.37034 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb36e00-d194-31c1-9fcf-74338eb63865 | -13.87891 | -53.98171 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0fbace6-c03c-37d8-8cb3-6d7317df250d | -14.42505 | -51.79856 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cec0104d-e5d3-390e-8d56-58b525bbee82 | -13.99202 | -53.6734 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2027a6dd-4d59-317a-a296-ad3b5c30711a | -14.00587 | -53.70845 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cf43ac48-d590-3b3c-b7ac-0c9abd4ed88f | -13.38858 | -54.36789 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d705359a-4311-35d6-a6ff-fcb44fd7dfc2 | -13.99585 | -53.70681 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 984180f2-b4ea-3a64-80cf-4895b76ef180 | -17.84901 | -44.46686 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb8afaff-f38f-3345-a568-7c1f3b07139b | -14.0014 | -53.67091 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f84f97db-6421-34bf-8d26-9c975a78c4c5 | -13.82359 | -53.9944 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a6a8ee5-9d25-3f97-8aaf-ff69789d976d | -13.82303 | -53.99797 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae2f3e02-fa99-301c-adfb-8ea7f90385fc | -18.91623 | -43.59884 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e80ab392-a552-399b-a666-b76ca6b7f109 | -15.67895 | -53.77913 | 2026-08-22 05:06:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28b5841b-d921-36ba-ab05-9cbb1a6a2b87 | -14.56198 | -53.01276 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e21a3aae-bc7c-3a5b-aae9-9c0b79ead4ab | -13.99919 | -53.70736 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c50a8ff-0053-38ce-8357-2f4100602555 | -14.97809 | -52.65603 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d4403d3-24de-38e5-a829-861b88896c16 | -14.55578 | -53.05383 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6886fa12-2483-3dad-90c6-a4ca63b9efdd | -14.00253 | -53.70791 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| baf1f344-251e-3948-bd8f-e3107355ec1a | -18.91357 | -43.59681 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b4e6a6fe-c8a6-36fe-a471-10841897daf8 | -13.9975 | -53.67395 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c6920ea-8803-343b-8295-a1361ae4f5cd | -14.00921 | -53.709 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 371282d4-5ef1-3a3c-95b2-277b00a8e094 | -13.39246 | -54.3649 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39c52db4-6d6d-3174-87a3-dceeea94b482 | -13.6919 | -51.84716 | 2026-08-22 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d9983bc6-5d52-3358-bbcb-1466df130035 | -14.39899 | -51.80291 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a5f5a43-de21-3ce5-a157-1b2bfd3ff77f | -17.94099 | -44.44276 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69652161-0b25-3c27-b4b7-f95c8d5ad4b3 | -15.23368 | -52.83201 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45cf198b-042a-33ec-9f09-ce044812c6dd | -15.18322 | -48.74081 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd5bcd9b-0e28-31b3-b17f-459c952f7de7 | -15.18696 | -48.74558 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7ff1271-f32e-3faa-a91e-b0827310776e | -13.98366 | -53.68309 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 93ca22ae-6545-3280-bf27-a8de3ceeb1a9 | -14.13541 | -48.05758 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d71063cb-b7ed-3d38-ada1-ea5715095dab | -13.82082 | -53.99028 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 971deb71-3f84-363a-8de0-f0bf957cb87c | -14.57331 | -53.00695 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3b6d477-bb15-37e4-9ee9-40ce70c946ee | -13.99416 | -53.6734 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4494af3a-c2f0-315c-8d5a-6649ef05fa5a | -14.31764 | -51.87127 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 513a0fd0-ce0d-3bdf-bb20-8054f481eb52 | -13.39967 | -54.36245 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 828d9eb7-427f-31bf-a7bb-bd0b93038910 | -13.38244 | -54.38507 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb4fded1-e923-3e6d-9f4d-a23e6bad19a9 | -18.08599 | -46.9423 | 2026-08-22 05:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bd65e4a7-f0d9-3362-b238-d92e0da52e0e | -14.31685 | -52.99696 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4740789-f575-3804-8921-fd539771b397 | -15.7449 | -56.54 | 2026-08-22 05:06:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aead6ca-c986-3f06-8169-8769f2befc7f | -14.33603 | -52.93892 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4d611d1-a231-3862-8e78-b1db782d37ca | -13.69394 | -51.95384 | 2026-08-22 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e647b904-0862-384e-9d0c-999124e5125e | -15.20862 | -52.79372 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae56afe7-0b4c-3b01-a5c0-52d0e1ff340f | -14.31573 | -53.00444 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c4be779-0fc9-346c-a3bc-61fd1da6936e | -16.27728 | -57.66816 | 2026-08-22 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 099ffa0c-c15b-3dfd-a328-3eb76848b0fd | -15.20463 | -52.77351 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd341a6c-53da-376d-83bf-6e65aa8d0d27 | -17.91668 | -44.38774 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README56.md)
