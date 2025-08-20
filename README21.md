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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| deb9ffb1-fcb7-3bbe-bcae-6e98272d5291 | -12.66543 | -45.82252 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1e88b18d-c889-3740-a6de-db4a9259a114 | -12.97633 | -56.88429 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82dfd02d-e501-30a1-ba7b-b3312c5d29e0 | -14.4603 | -48.47599 | 2025-08-20 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 305275c3-11eb-3abc-9803-154fd1dd22a4 | -14.99069 | -54.82132 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a4eb962-1f68-39e7-8660-56fc977f2239 | -17.40092 | -46.69793 | 2025-08-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0801f438-432a-3071-bf08-a55988c3daf5 | -13.58121 | -47.01778 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8064dce4-1a7b-35ac-b77d-ec86044a8bfc | -14.89152 | -48.08362 | 2025-08-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7390afad-bd9d-3b14-9f7f-a6a1d63357b7 | -13.3441 | -54.40165 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 072fcb66-57a9-30fe-8034-1431b9036d3b | -12.81166 | -48.561 | 2025-08-20 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4010beb9-86ff-3c17-8f43-9f913720316b | -13.62998 | -46.88781 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 586e11d8-62f4-36eb-9b65-d180d353f3aa | -13.5849 | -47.01841 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a5bf505-cbfc-3c92-be2d-36e4957cab4a | -15.02837 | -54.83645 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4c83722-d000-376c-8a72-823d41f04927 | -12.97699 | -56.8814 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f4f317f-9264-3482-9f44-c2cf34e302a1 | -11.56347 | -50.46074 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1799bc58-e184-39e0-a7e3-289f24600618 | -15.54526 | -42.2843 | 2025-08-20 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78b507da-c95a-3c46-bd4b-9ef5197fe372 | -12.9897 | -45.18737 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a3cdad7-4278-36f4-8c03-370af3169ca0 | -13.86772 | -45.55463 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4468cb9c-c552-3f33-8d36-a7b9e3f8a33e | -13.03384 | -46.78976 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7528b1cb-0ac1-35a4-ae8c-af93d84838e7 | -13.57445 | -47.03497 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c4f7ee9a-9646-341b-a73a-5b68ba1e56f0 | -14.95228 | -47.00029 | 2025-08-20 04:10:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26d28c3b-3bba-3a2b-bc0a-5e6ca3eda9b8 | -13.17348 | -46.87562 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26b6bcb1-1f71-3cd3-ac3c-5bf592757d4a | -13.5783 | -47.01265 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dd783a6-3d6a-311e-96ac-50167c2e6f21 | -13.1756 | -46.86322 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0376055-04ab-31ae-b6e7-523b32b47ccd | -13.62629 | -46.88734 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88671b69-6d65-31ba-bbc2-9fe1cc49c19d | -13.17855 | -46.8681 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6e912c3-5b7a-3251-b836-45fcb8840498 | -13.19504 | -50.74349 | 2025-08-20 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98a9fc0e-2f59-3bdc-8bc8-1854204aa570 | -16.18313 | -48.86463 | 2025-08-20 04:10:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cb825ad-0230-32fc-bac7-e705cba96ca8 | -12.96894 | -56.85236 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0228cf90-c713-3a3e-9205-277a87c4fb62 | -14.36173 | -52.00319 | 2025-08-20 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da868f46-b401-3eb1-aee0-dcdd8fb3c717 | -13.52919 | -40.69138 | 2025-08-20 04:10:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0d5912ba-f6f4-354d-87a8-ac898f530b5c | -13.14255 | -54.92707 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| afb8873a-e3a7-3d74-ad04-cedd3d5c371a | -15.07944 | -48.39827 | 2025-08-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee2f45c8-3b18-32c4-93d3-cd2e47e7b8c8 | -15.09818 | -47.33537 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9223091-1a2e-3ece-b213-e275df7080f9 | -15.00154 | -54.82824 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9d7168a-097a-3dbb-8206-4ee8d37a24ca | -13.3402 | -54.40833 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7aef574-487f-39ff-b687-3647094dabc4 | -14.46272 | -48.36993 | 2025-08-20 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce44d547-c786-33c6-b1d5-3bd7bf65a825 | -18.45609 | -41.80898 | 2025-08-20 04:10:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 81ddb7a4-0de3-3e27-8584-6e5d997876a9 | -14.16275 | -45.27941 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4445d3c4-c5d0-3cf6-a540-a38db1a53113 | -11.30709 | -44.9258 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f28a14d2-1a15-37a2-89c0-d3aa49916444 | -13.73728 | -52.01885 | 2025-08-20 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20703dfb-ebb1-3f94-b2a6-4407f5108c33 | -13.33644 | -54.40921 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c2fc314c-7072-320a-bcc3-38b81184cbf9 | -13.02629 | -56.85194 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf869d6f-2efe-3a12-af31-97a222f77c63 | -13.58413 | -47.02291 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e269b185-9fe3-3966-9ffa-c441e37ea675 | -13.03306 | -56.85371 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cea7813-c630-3d1e-892f-dd4808252696 | -13.03782 | -46.83217 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7ab2636-fae8-3f00-b64d-fb8b3ff066ad | -13.35384 | -54.40194 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bccb831-0249-33c7-b209-8907b9cdd8cd | -12.97635 | -56.84999 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 404cd99e-cfff-31ae-9b32-bdb8f93a0ada | -15.02757 | -54.84026 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c81eab26-be17-32e2-8669-c499e8a44952 | -14.8932 | -48.07386 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73c40192-85ef-3b9c-aeb0-a9c53fdb6d76 | -12.811 | -48.56474 | 2025-08-20 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61797e37-fb36-3238-b115-6c70cc372391 | -14.16705 | -45.29564 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74b81e3f-fb2c-3fb2-a534-ccbd581035f4 | -12.94306 | -46.15712 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3992657a-decd-337a-b677-5c62b87c88e9 | -16.5231 | -42.51277 | 2025-08-20 04:10:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a86226e-814e-3ea2-ba61-bc775b7bfb33 | -16.6933 | -47.63424 | 2025-08-20 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2d423af-9d69-311f-b2a1-bf4cb4ed8cda | -12.53227 | -45.61713 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95ef019f-798a-3f71-82c3-4173080dc830 | -13.17568 | -46.88487 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25791096-0946-3aaf-8ec2-a79854f08464 | -11.75089 | -48.18703 | 2025-08-20 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 57470c51-79ed-3509-ad9c-59da5d7d3463 | -15.02029 | -54.82652 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ffaebae-77ba-3cf0-b37f-7aa498242a54 | -13.19538 | -46.88042 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 972601a7-1cc6-31a6-a45f-4b425b557107 | -13.6226 | -46.88688 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 480bd696-a505-3396-8865-6e860bcf7e89 | -13.67523 | -44.22281 | 2025-08-20 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b83b1d61-f9e1-371f-8ea6-685ab05f12a1 | -12.98907 | -45.19117 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef275c50-3fe4-30e3-8fc8-7a9cda204f23 | -13.03443 | -56.84728 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c4c445c-f3af-3da1-be39-26d2865a889a | -12.66156 | -44.95877 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e2bfc3b-e92a-3cff-9d62-812f3b796e35 | -17.58186 | -45.38763 | 2025-08-20 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8015bb0a-1528-31d8-9970-fe07ce9387a9 | -14.40992 | -50.41337 | 2025-08-20 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5ad6f2a-2fe0-3c24-b913-ed835c82962a | -12.97584 | -56.85358 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ec93419-7bb3-38f4-a5c3-6e1d348a9807 | -14.15484 | -45.28164 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b8b010a-cb48-3107-bd04-87d643ca41a5 | -13.03492 | -46.78706 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 42b24b5e-0175-3dc0-9429-87461403801f | -15.00026 | -54.80463 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fb6eff2-e833-3c7f-a4db-77e8455ad42e | -16.31499 | -50.18013 | 2025-08-20 04:10:00 | NOAA-21 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d0c1d82-7ce5-3f3d-8597-3f0a86c6f200 | -13.58335 | -47.0274 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55656eff-dd33-324c-bee2-52327a2ed946 | -12.14472 | -48.16448 | 2025-08-20 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b0a49ee-330c-356a-ae52-b1f0fe2e6d1c | -17.40026 | -46.70191 | 2025-08-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09b2c356-3fa6-39c6-9f7f-1df57791ed5c | -10.87392 | -48.46733 | 2025-08-20 04:10:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb7aa779-987d-34c2-8306-3911d97c2a42 | -13.04155 | -46.79257 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 495855ee-73b7-349e-83ec-cf6fc2f5220a | -15.74638 | -46.61934 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a07fa06d-d1db-3aae-b9dd-1389684a8d9b | -12.1121 | -47.89767 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6e33f328-5be5-35b9-a16e-2f88448f6507 | -12.14056 | -48.01624 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52a3a79c-bb3f-3f3d-9bba-940a300b650a | -12.98044 | -56.86464 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d0aed4a-a223-3640-bd3c-a7fa0bca347e | -13.03459 | -46.78543 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a346fc6-bef9-3fdc-8f7e-b81409d3a5c0 | -17.45542 | -46.15844 | 2025-08-20 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1085efd3-cd1a-3248-9817-76068b7d43d1 | -14.30466 | -52.00403 | 2025-08-20 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 769893db-49cc-35b6-a00f-3b196809bee9 | -15.5497 | -48.56902 | 2025-08-20 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd388d2d-1e83-3152-844d-209ff41c048f | -12.66095 | -44.96252 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 513dd130-88e6-3ba6-8846-172c733bcba4 | -13.19175 | -46.87946 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ff69214-6c8a-3ab5-9565-68436e66525f | -10.47091 | -48.35781 | 2025-08-20 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cf1e688-f3ee-3ce6-8011-b4bcfc385b26 | -13.03445 | -46.80799 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f88c39e0-9016-3428-8db2-5622135a72a9 | -13.40523 | -46.3714 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 381d1b7b-e9cd-3c91-b121-7f6cabada886 | -12.52377 | -45.60348 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 907d6b39-b229-3836-8864-eae08c1bcb7c | -13.15583 | -54.92453 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 98f3e456-1e1d-336f-93cc-321fffdb27b7 | -13.15378 | -54.93435 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1cc590b3-e8a6-3ab2-b83b-a06ea088122d | -13.20195 | -50.7433 | 2025-08-20 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33df8c66-97d1-3363-92cb-640475c69369 | -17.93626 | -44.48874 | 2025-08-20 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64207290-453e-3bd8-81c9-9c2b16fa3601 | -14.98952 | -49.56359 | 2025-08-20 04:10:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 25cd5817-89f7-3351-b0f4-910be3a72274 | -13.03124 | -46.809 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4296164-b1b0-3bb0-8354-e53b05db007e | -13.15438 | -54.93226 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2b10ee3-58cc-331e-8878-d4266aa905bb | -13.57966 | -47.02675 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| baa4c646-3f8a-394b-b56d-3cd07db76e9b | -14.88848 | -48.09051 | 2025-08-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13ba3a30-0535-38c1-ab3b-1b4fe627288a | -13.02766 | -56.8455 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README22.md)
