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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da711937-47b1-377d-bd61-7c43d66f1ddf | -14.42881 | -48.92087 | 2025-06-20 00:39:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 2a19294c-9b0c-3463-b9e3-b7bb4fff82e8 | -11.94063 | -48.42182 | 2025-06-20 00:39:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9cecbc46-68e2-35ca-9ee9-78d94066df06 | -12.19484 | -49.6249 | 2025-06-20 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a61a9311-f830-3662-ada9-ffd3f9be0f94 | -10.48532 | -47.05058 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 9f13d69d-4ef1-3bb7-9591-b2e93509f39b | -13.24308 | -49.83294 | 2025-06-20 00:39:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4aa007ad-9a57-3cea-b9c3-c8626e4c63e3 | -14.62434 | -48.12211 | 2025-06-20 00:39:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4cb60edd-f60c-3894-910d-5cc211cf79d1 | -9.84427 | -44.70071 | 2025-06-20 00:39:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0a95db35-a6d1-3182-b257-20fd7f50b257 | -14.047 | -53.37427 | 2025-06-20 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| edc7990b-0460-3202-8b3f-bfb2e86d5901 | -10.86022 | -53.7728 | 2025-06-20 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 83456298-1e09-3bfd-9e23-9d675f080ae4 | -10.73236 | -49.561 | 2025-06-20 00:39:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7dcbd6dd-4c0d-347b-b42d-487ab18e92d6 | -11.93179 | -48.42311 | 2025-06-20 00:39:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8769db3e-50a5-33c1-9604-ef355932bac6 | -11.31301 | -45.20036 | 2025-06-20 00:39:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2530adea-c787-3606-83a6-413af28a1da2 | -12.49107 | -47.48211 | 2025-06-20 00:39:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b8528f64-b45b-3ed7-944e-c38a21f7de44 | -12.34605 | -49.30949 | 2025-06-20 00:39:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 5b35e843-5d8c-332d-ab85-1dede25e4b4a | -14.04495 | -53.35661 | 2025-06-20 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| aebc060f-36e4-36be-8e92-1215d47c8ba8 | -12.39694 | -46.36551 | 2025-06-20 00:39:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b3cedb83-0ce9-3b35-962e-753565490606 | -19.76956 | -48.2859 | 2025-06-20 00:39:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 820e320e-4d15-397b-b0b2-a996003e25a5 | -11.90626 | -51.74353 | 2025-06-20 00:39:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a5c6cf43-3987-3cc0-9cf6-f112f9607d1f | -11.9094 | -51.7687 | 2025-06-20 00:39:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ed9576f8-bac6-37e5-b13d-2dc3c00280b6 | -10.52392 | -47.57918 | 2025-06-20 00:39:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 8148f439-4b32-3043-b1c2-7647e0e94c06 | -13.26488 | -46.82082 | 2025-06-20 00:39:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 158d40f5-6807-39c6-9a33-07a8135dbab7 | -10.54098 | -46.98873 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8f90116e-1410-3d42-bde4-b8b2ecb83b67 | -10.66004 | -49.36363 | 2025-06-20 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 045cb81e-d1cc-3135-886d-64ecd8150bcb | -13.39012 | -48.44659 | 2025-06-20 00:39:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d32c4c36-f33f-3656-800c-17cf61229345 | -13.77698 | -54.19983 | 2025-06-20 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| a8b683cc-3f71-3c39-9f7b-13d746b80d1d | -11.14602 | -46.64252 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 09215f93-c63e-360d-a5ce-c03f2633e542 | -11.12153 | -46.66577 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c9f22f33-5329-3b20-8c88-39acf4da64cf | -10.59963 | -49.46267 | 2025-06-20 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 77465790-e373-3b33-9f6b-075231295bde | -11.80287 | -48.09121 | 2025-06-20 00:39:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 33ed1391-2345-349d-8350-d95ece6d476a | -11.90782 | -51.75607 | 2025-06-20 00:39:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 01085a80-a809-3669-adee-f155f14cd31c | -10.493 | -47.0399 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 43ca86dd-4336-3bed-a290-36c7e458293d | -11.53131 | -57.01298 | 2025-06-20 00:39:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 37a053e7-fbe7-3dd0-bf79-ad0cc5c1c84d | -11.15236 | -46.62202 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cdd4deb3-d91d-3a43-bde7-eeabcf45cfa3 | -11.52789 | -56.98178 | 2025-06-20 00:39:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| d617d1bb-4d0e-31bf-bfbf-2afb9bf8f4cf | -11.31468 | -45.21159 | 2025-06-20 00:39:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dae37022-1bbe-36a5-9f36-096a89e93900 | -12.20397 | -49.62362 | 2025-06-20 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 0781c042-4d86-3599-a509-5fcf37a08511 | -10.5252 | -47.58822 | 2025-06-20 00:39:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 857e6234-26a2-302c-8bd0-533c6875ef0b | -12.47442 | -54.42228 | 2025-06-20 00:39:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| dd95fc58-9777-3849-b53e-6ef5d271c9ea | -10.85819 | -53.7558 | 2025-06-20 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c562d064-2dc9-304c-b683-7c684eabbda3 | -13.39616 | -48.09336 | 2025-06-20 00:39:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cbae27ea-2a3e-3132-8b78-67b37eb801bc | -11.13692 | -46.64384 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e9a3c99f-ec6a-3709-9245-45b6db4fca96 | -13.23376 | -49.83422 | 2025-06-20 00:39:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 42.3 |
| c413a76c-dabb-330b-9a4e-69d326dadb5a | -11.91813 | -51.75472 | 2025-06-20 00:39:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6a5e03d0-9c2e-327b-a986-a0d432df1ac8 | -12.26879 | -44.60513 | 2025-06-20 00:39:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 1ab057db-b354-3425-bdbf-210b7bcfc9c2 | -10.49167 | -47.03057 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a6871c10-68a5-33b5-9d6c-a6a58e7dfb7a | -14.43787 | -48.9196 | 2025-06-20 00:39:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 47.9 |
| f696bac7-0422-3c84-b82f-eebd33d4f8ab | -12.7627 | -44.41589 | 2025-06-20 00:39:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| e36875b9-c427-38e6-90a4-197a96d8020c | -12.22124 | -45.53208 | 2025-06-20 00:39:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| b4fb476e-89b1-39d4-9a2c-6b7507153af8 | -13.23508 | -49.84433 | 2025-06-20 00:39:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 9aeae6f6-907f-31b8-a8b0-62f7d452fc76 | -12.50605 | -58.37467 | 2025-06-20 00:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| a8fe69fe-6365-3a74-b480-67f3a790fb67 | -11.85643 | -51.74326 | 2025-06-20 00:39:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a9ef99a3-ec70-34cb-b867-80e9bb3f6049 | -11.87889 | -54.68177 | 2025-06-20 00:39:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| ce5930f4-13d1-3efa-ab4b-94bfb61bd4af | -13.2444 | -49.84305 | 2025-06-20 00:39:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 02fa153f-e3fe-3d85-ab81-7246a2313962 | -10.66128 | -49.37284 | 2025-06-20 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 1ec78a95-cb6f-3998-a4a6-9e9db419d2bd | -11.57896 | -47.8711 | 2025-06-20 00:39:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d6965f98-a6ba-373f-8c6b-1ca4e20f2479 | -11.86671 | -51.74189 | 2025-06-20 00:39:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 502455c5-8bb6-3011-85bd-d5a004d1254e | -11.14464 | -46.63295 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 35fadf47-5584-3143-b085-c0140ed2886e | -12.22277 | -45.54253 | 2025-06-20 00:39:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5942f6b1-4944-3cd4-a453-6f8fd0f00259 | -11.91971 | -51.7673 | 2025-06-20 00:39:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d4bec7d6-fa16-39ef-97e9-96983379c3f2 | -10.669 | -49.36236 | 2025-06-20 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 087e67c6-4329-34fd-908f-f97de1ab18e5 | -16.47023 | -45.01478 | 2025-06-20 00:39:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 77fc9ede-adff-3b30-9790-a0007ebd5072 | -11.15374 | -46.6316 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| de4666c1-0d41-3baf-95ae-5befe35afc41 | -11.81989 | -54.509 | 2025-06-20 00:39:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 8cc3c014-5588-3609-9f96-cc6c65ed56cb | -11.98198 | -51.61479 | 2025-06-20 00:39:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7b0f3259-264b-3c35-9ebb-07b4b1117f5b | -11.46019 | -47.29544 | 2025-06-20 00:39:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4742b8cf-de5e-3126-a323-240530deb18e | -10.72434 | -45.16701 | 2025-06-20 00:39:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5f922340-d997-39f1-8ed6-3e9b29e17e20 | -10.73111 | -49.55169 | 2025-06-20 00:39:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 07f16807-3f3c-349b-a68a-c0722c9139e4 | -12.20269 | -49.614 | 2025-06-20 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 66d0bc4f-0b6f-3eb5-be15-737201cd85b3 | -14.43009 | -48.93047 | 2025-06-20 00:39:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f00cf438-8a7a-37c8-86de-65b351b89436 | -15.40157 | -47.81166 | 2025-06-20 00:39:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c740bfbf-fd8d-3a39-8fed-a0c7d23f8367 | -11.46909 | -47.29411 | 2025-06-20 00:39:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 57efd412-c323-3cd6-bbb2-e604d92386e0 | -12.2133 | -45.54403 | 2025-06-20 00:39:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2561fb74-ca9f-3e9f-9ac4-9c6a393f0589 | -13.39741 | -48.10242 | 2025-06-20 00:39:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 66e32fce-e586-3d0f-8f49-28f7e7ef3cf1 | -12.21177 | -45.53357 | 2025-06-20 00:39:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 42f1354f-688e-3b6a-898b-c9652939a46a | -12.50468 | -58.37975 | 2025-06-20 00:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 461cc2e8-edaf-378d-8677-9703631f989b | -11.13554 | -46.63427 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12f6bea3-dd92-3131-9701-5d0635178115 | -11.86513 | -51.72958 | 2025-06-20 00:39:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f260fde1-18be-3a85-9915-e4ca9099d83e | -10.48399 | -47.04129 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| c7dd5f0b-c190-3f8b-a01b-8e62049396b0 | -13.39136 | -48.45576 | 2025-06-20 00:39:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| ce8bedfe-40c8-3f35-8f40-c9ffab234633 | -13.09559 | -52.29675 | 2025-06-20 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 9a0b02cf-d963-37cf-8632-6448ef482a35 | -11.58021 | -47.88007 | 2025-06-20 00:39:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 80f051c2-2e22-3dda-9b29-fe099152f45c | -16.78762 | -49.11203 | 2025-06-20 00:39:00 | TERRA_M-M | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 16f8a7d8-b802-3154-add3-44c042eacd83 | -19.54558 | -49.66722 | 2025-06-20 00:39:00 | TERRA_M-M | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| d149e046-cc15-3297-bd7b-5d6f47989bf3 | -11.57014 | -47.87241 | 2025-06-20 00:39:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 62d0e09c-4cac-32c5-aea3-9081a5e66edb | -16.305 | -58.2474 | 2025-06-20 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 133.6 |
| baff4ab2-44eb-36e2-8830-e0bc24cc171a | -14.0404 | -53.3669 | 2025-06-20 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| bdfad82a-780c-3a66-9b73-14f5b69f2d98 | -21.6502 | -53.9667 | 2025-06-20 00:40:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c53a29b7-d720-3ffa-98e7-b40a5030e6b9 | -19.7784 | -48.3011 | 2025-06-20 00:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 72.8 |
| decd81bb-ecf2-3ebc-9731-d6efff2ec277 | -9.4648 | -57.8449 | 2025-06-20 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 9c49454b-a1a1-3a59-ba95-d5a2b8fcf516 | -9.4807 | -56.0801 | 2025-06-20 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 81c5c55c-4640-3223-8a40-d43cd8ffb3f8 | -19.7791 | -48.278 | 2025-06-20 00:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 5879c85a-881f-3d5d-a5ad-729a9f91b440 | -16.3044 | -58.2879 | 2025-06-20 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 3dfdc0f2-3287-3116-8ea6-1f796b6202b1 | -7.2217 | -43.0917 | 2025-06-20 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 158624a6-fb85-3eba-8df0-735efaeccbe1 | -16.2852 | -58.2697 | 2025-06-20 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 0c47e0e5-bb2d-3417-af38-969c9895c252 | -16.3047 | -58.2676 | 2025-06-20 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 259.2 |
| 569caceb-8fe2-3a95-a68a-99d855659015 | -11.9518 | -58.7574 | 2025-06-20 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 015326e1-087c-3daa-92ac-4e56ed1f1ca1 | -7.2031 | -43.0701 | 2025-06-20 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 1a0cf756-fef7-3f8c-a7c4-c3ea4c8c3703 | -19.7587 | -48.2824 | 2025-06-20 00:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f68a655e-32f7-315f-8b7a-9a491338afb1 | -7.2219 | -43.0682 | 2025-06-20 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 282.8 |
| c45dd5f1-cd51-36dd-914c-4f932a487752 | -11.952 | -58.7376 | 2025-06-20 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |


[Clique aqui para ver as próximas entradas](README3.md)
