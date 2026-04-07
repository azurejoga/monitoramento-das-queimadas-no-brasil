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
| d5849c96-f645-3047-b524-43a79cea3293 | -18.49167 | -55.5042 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b6d575c1-2de4-32f9-a49b-deaa611d92ff | -25.32813 | -49.42274 | 2026-04-07 04:32:00 | NPP-375D | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 44a5b5ed-b694-327a-b674-d6a15f16f324 | -25.32481 | -49.4221 | 2026-04-07 04:32:00 | NPP-375D | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55cdfed8-2fdd-3c2a-91c6-0cd79b98b41c | -20.37479 | -55.04333 | 2026-04-07 04:32:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d323eb5-ca59-3626-9413-7b3e07c6a6a1 | -18.49275 | -55.4988 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ca33c5d7-ed09-3f93-a5f9-f43a98e9ba66 | -27.33366 | -50.78345 | 2026-04-07 04:34:00 | NPP-375D | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8451b4ae-5450-325a-b10c-55d525769518 | 2.37316 | -60.96334 | 2026-04-07 04:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42f081b7-4901-33ba-a29e-cc26a6073065 | -12.0375 | -45.34538 | 2026-04-07 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72b2138e-e80c-3506-9a1d-8c5477ee9ece | -9.45939 | -46.07339 | 2026-04-07 04:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14998d10-db6c-3f38-8bc3-2e0b3ba26d53 | -11.20317 | -56.87804 | 2026-04-07 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57281d91-4297-359c-af8d-d788377deca7 | -13.23022 | -53.32321 | 2026-04-07 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a9f07fd-b511-3092-a453-c499139aab61 | -15.28443 | -53.14001 | 2026-04-07 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daffab29-0538-33c9-9a1c-a84ea14491e3 | -17.9039 | -54.12098 | 2026-04-07 04:51:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92c52b77-637b-38b8-bcaa-a9d388133686 | -13.03603 | -45.06738 | 2026-04-07 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 976d3a77-9b27-31eb-8f34-235d6469a6b3 | -19.59246 | -40.08111 | 2026-04-07 04:51:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f7b6359-3af3-3ddc-b4c6-e47e43683264 | -19.59949 | -40.08176 | 2026-04-07 04:51:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f839f22-28e3-3d37-88e0-59e448641906 | -22.04445 | -56.30476 | 2026-04-07 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f205c4b-224c-30ee-ad3d-85b4503c17d0 | -21.41152 | -57.09069 | 2026-04-07 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81eb054c-9ad1-35c5-b978-c3ca73e53839 | -20.37931 | -55.04305 | 2026-04-07 04:53:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e6364ba-5a8a-334f-9d50-b8ac27477f4f | -18.49441 | -55.49917 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| ae131a12-b4b4-3418-9786-5151ff727d2b | -18.50412 | -55.52442 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 57edbad1-2db7-3e02-9023-b50af1260f38 | -18.498 | -55.51938 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 03245566-1aa4-32e4-9e08-f14b839b2f4e | -18.50539 | -55.51683 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9992b93f-0b9a-34a8-af08-4e766b9b42db | -18.50264 | -55.51241 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d0239c46-0278-363e-ab53-0c21dfca3b18 | -18.49377 | -55.50296 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 98760bea-daec-3443-84d4-52646ad9428d | -22.03772 | -56.30344 | 2026-04-07 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2da893a-c79e-3b55-a9da-48d8dd4bde8f | -18.49588 | -55.51117 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6a98e768-fb94-3547-8aa6-49ca8bcfde38 | -18.49652 | -55.50738 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 2684aad0-bcf0-38db-9f38-60304b73d8e7 | -22.04108 | -56.3041 | 2026-04-07 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d53983f6-948e-3fb6-8209-4435573075a6 | -18.50201 | -55.51621 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0b1e3206-ce5a-337f-89f3-5873698040bd | -18.49863 | -55.51559 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4b6536ce-34de-3fb9-87e5-3b87356d0233 | -18.50074 | -55.5238 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 27b816d1-08c5-3e60-ade4-fc7e90289aa6 | -22.05713 | -53.98549 | 2026-04-07 04:53:00 | NOAA-20 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 05ba1cca-22c6-31ff-8985-373f7847baee | -18.49926 | -55.51179 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0ead4806-1a5d-365c-bed6-7962aaa6bbef | -22.03435 | -56.30278 | 2026-04-07 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31a1d1d5-e76a-330d-8cd3-ce9b3cc21d89 | -20.37599 | -55.04246 | 2026-04-07 04:53:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d716965d-c633-3457-b515-898b06ab3e81 | -18.50137 | -55.52 | 2026-04-07 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 34bdcbf9-d5e4-3bd2-af69-412de15ad60a | -23.0297 | -52.68366 | 2026-04-07 04:53:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 08876065-984a-3a60-8ea5-a54b1dbbc72a | 3.84637 | -59.77753 | 2026-04-07 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14aee01d-5504-351a-896d-797ea838d82f | 1.70341 | -60.34698 | 2026-04-07 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b73d16be-2b03-3462-9bb7-180f74e69f3c | 3.80466 | -60.50483 | 2026-04-07 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e32a2fb-11e5-3825-8bf2-9a527499cc60 | 2.37303 | -60.96548 | 2026-04-07 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 537dff81-9169-36d3-b279-a1806cfe69f9 | 1.75275 | -60.24371 | 2026-04-07 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dada191-1e13-371b-98d3-41d76fdeccd7 | 2.59937 | -61.14886 | 2026-04-07 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c80c61cf-2dae-3013-8f2a-883fe246954f | 2.37249 | -60.96201 | 2026-04-07 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3040a8e-7aa0-39e8-a855-68adfd7fe108 | 2.38427 | -61.45036 | 2026-04-07 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 141df026-7178-31ee-a499-33ee2e294d40 | 2.60938 | -61.31982 | 2026-04-07 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e4e99dd-869d-3447-b6ce-9c32638ee6e0 | 1.70398 | -60.35055 | 2026-04-07 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c66d622-5a33-3765-bf56-8d89df1ea0bd | 2.36917 | -60.96252 | 2026-04-07 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7a5b3ab-1517-3d69-8f9f-4fe2f5f744bf | 2.38151 | -61.45431 | 2026-04-07 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae204f6e-c6e1-3cea-b8ce-1af4a5e63443 | 2.60992 | -61.32325 | 2026-04-07 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b257fb26-7da0-3eb7-9ee9-67e2a63a1489 | 1.75331 | -60.24731 | 2026-04-07 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d987f3dd-c117-3aa6-a3e8-72c84bff535c | -18.50059 | -55.51987 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c7fba07b-f63e-30de-89c3-5faaefb8880f | -18.49642 | -55.50178 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 24adb7dc-782e-3349-9a64-28e52b9d76e4 | -18.50686 | -55.51622 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 21b9806c-1156-3e9d-8863-f40d4871ff15 | -18.50644 | -55.52058 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d1c947f4-cd06-3f3e-ace4-d7c872f47ff7 | -18.50602 | -55.52492 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 95b54147-82bc-3eb0-9ad2-d3ac87e46e1c | -18.496 | -55.50613 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 7846fe3e-2097-3fa7-b2eb-067ab10c4d38 | -18.49558 | -55.51048 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5349f74d-ce3e-3959-a73e-cfe9d1cfbd22 | -18.50144 | -55.51118 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 28fa80c3-c4fa-31e6-8041-031463f7f25f | -17.90696 | -54.11937 | 2026-04-07 05:40:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dce6dc7-7bcf-30fd-b964-3d8347938f88 | -18.50101 | -55.51553 | 2026-04-07 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 0c2e9f83-b5ab-37c3-9ee1-a4a83cccc1ad | -13.03472 | -45.06635 | 2026-04-07 05:59:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 989940ed-6574-31db-82ec-6e66a3080e4e | 2.37131 | -60.96511 | 2026-04-07 06:05:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20bec060-231a-30dc-a330-367bae553961 | 2.60922 | -61.32146 | 2026-04-07 06:05:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4def03ae-a51d-3c8c-a18e-100daebd597c | 1.75375 | -60.24755 | 2026-04-07 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bb3b16f-0577-3a9f-92a1-c861db3b4971 | -9.46738 | -46.07208 | 2026-04-07 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b5002e55-ae5f-3ab9-aec5-1d72e38c2695 | -12.0357 | -45.34563 | 2026-04-07 12:04:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 3abbeb5b-d5c1-30b2-b296-11a90385a5b6 | -12.02795 | -45.24118 | 2026-04-07 12:04:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 02231c92-e5bf-3dae-bdad-3b7a798f0b36 | -11.79556 | -44.73075 | 2026-04-07 12:04:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e25ae7d5-78fa-36ce-9483-333d92c22ebb | -9.46594 | -46.08258 | 2026-04-07 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a1cc68f8-9b18-3d53-9008-cf119fa05127 | -11.79076 | -44.73828 | 2026-04-07 12:04:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 089ba1ec-e0b0-362a-8874-5ca42d5c8c56 | -12.03839 | -45.24253 | 2026-04-07 12:04:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| ac2edcbc-4219-374e-ba38-64eb069e6b06 | -11.79384 | -44.74463 | 2026-04-07 12:04:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e2f30b80-9191-3b25-b1f9-398d29cf8870 | -4.95229 | -42.59598 | 2026-04-07 12:04:00 | TERRA_M-T | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 376232de-0818-3dc6-a8bb-eb5892769101 | -12.04607 | -45.34688 | 2026-04-07 12:04:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 1c857fc6-cccb-3067-8c3f-1479e740e5fd | -13.0339 | -45.0547 | 2026-04-07 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 693a7273-6a1a-30d6-a0ba-079c7b673293 | -13.03576 | -45.07487 | 2026-04-07 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| cc04707a-7a7a-322d-844f-4fb9b5ea7805 | -13.03747 | -45.06104 | 2026-04-07 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 792b2114-248e-3805-8e80-b2b4ea786721 | -13.0321 | -45.06857 | 2026-04-07 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d08ef748-f805-3034-90a9-58b6bd016791 | -22.87728 | -52.27174 | 2026-04-07 12:08:00 | TERRA_M-T | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| f9aa9151-fcad-34be-a610-01b7e3f5b670 | -22.86697 | -52.27987 | 2026-04-07 12:08:00 | TERRA_M-T | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 39.0 |
| ef679b7d-ec5c-3f94-ab38-93b6a48d5208 | -22.86839 | -52.27023 | 2026-04-07 12:08:00 | TERRA_M-T | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 02ea41de-6bcf-3f0d-a478-8472711758dd | -22.87586 | -52.2814 | 2026-04-07 12:08:00 | TERRA_M-T | SÃO JOÃO DO CAIUÁ | PARANÁ | Brasil | 4124905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 73.3 |


