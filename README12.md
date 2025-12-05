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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46df3705-3b99-31a1-b1fb-854749ec0d12 | 1.99408 | -55.70175 | 2025-12-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c4ff471-83fc-3f7c-ab1b-91d959dcf2fb | 1.99274 | -55.70118 | 2025-12-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19d3507-807d-3aac-ac7d-142c072a7112 | -1.95922 | -52.72791 | 2025-12-05 05:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14400b26-8df5-32f5-8416-eb0ea32d14d1 | -21.63199 | -56.13525 | 2025-12-05 05:46:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 928b80d9-0fce-3206-8cfd-76a677add7f9 | -20.92243 | -56.37875 | 2025-12-05 05:46:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a1311363-373e-3352-8f44-3d177b04a992 | -19.98177 | -57.46263 | 2025-12-05 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7d3b5370-539b-3ce8-93be-f1b681fab8fa | -17.69191 | -54.34316 | 2025-12-05 05:46:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22d333e1-e600-3680-b4ff-8768a07972ab | -23.70701 | -55.26491 | 2025-12-05 05:46:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4d941d87-fb74-3b44-8e49-8c9ae61e4e23 | -21.63145 | -56.13299 | 2025-12-05 05:46:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 21bd5668-c180-3720-b710-e5b88c5702c1 | -20.91566 | -56.38343 | 2025-12-05 05:46:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc362693-ff4b-3810-bd32-68960e881003 | -20.02827 | -57.41014 | 2025-12-05 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4d2bcc52-7f25-3c02-8acd-69cc86a038c9 | -20.92198 | -56.38401 | 2025-12-05 05:46:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e67c2564-d31b-3c36-91a6-9067f44d3d27 | -21.626 | -56.12859 | 2025-12-05 05:46:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 01c30ee9-7cef-35b1-8aac-fe15d570b9bb | -23.7001 | -55.26457 | 2025-12-05 05:46:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c517197b-c976-3e0a-bef2-9f159ab9c9ca | -20.02693 | -57.41091 | 2025-12-05 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 10b74c71-febe-3a84-a6ae-cf971ce3fea4 | -21.62555 | -56.13453 | 2025-12-05 05:46:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5c25acf-0eff-3d0e-9020-54f3c7c97479 | -21.62501 | -56.1323 | 2025-12-05 05:46:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9cc613de-7f94-3bc0-9d4b-6adf291b4a47 | -6.42432 | -44.77717 | 2025-12-05 06:01:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ffa764f9-a0cb-3e0f-b5dd-da5f4e3eedba | -4.53775 | -44.22541 | 2025-12-05 06:01:00 | AQUA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6d8a58d-309f-3e78-9a23-02938afd3959 | -3.34995 | -42.15586 | 2025-12-05 06:01:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b6cba3ed-6f32-38f9-b6f3-b1bef34fda47 | -20.92119 | -56.38411 | 2025-12-05 06:07:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b646519d-b057-3338-8dee-afea74e71671 | -10.1262 | -36.117 | 2025-12-05 06:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 53.7 |
| 3dec9c28-87bc-3c58-9655-6492f1b5bf31 | -2.83531 | -42.98703 | 2025-12-05 11:55:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 90a5794c-9d41-3522-831d-eb067d3cd7d3 | -3.03704 | -41.97491 | 2025-12-05 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| cc34245c-393b-3496-891a-21ecbbd0a3a3 | -2.90704 | -42.30014 | 2025-12-05 11:55:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| de6e395b-4930-3107-9ad4-76025d5e8b45 | -2.96486 | -40.16056 | 2025-12-05 11:55:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 07db95c3-fafa-3dcd-bcc0-5e9c5189a769 | -2.90578 | -42.30889 | 2025-12-05 11:55:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 4c367fd6-8e51-3597-9728-e1b783ce7098 | -3.01115 | -41.38228 | 2025-12-05 11:55:00 | TERRA_M-M | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4cdc0276-6833-34d2-97d1-4f51afa86ca7 | -3.29696 | -41.25393 | 2025-12-05 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 226206cf-42d6-39c9-a6e0-8278326bfb25 | -2.90101 | -43.04721 | 2025-12-05 11:55:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 32176344-c421-334b-9bcd-9eb684c7c698 | -3.28795 | -41.2527 | 2025-12-05 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7a43ab05-7231-383e-8529-4980956652bd | -2.88317 | -42.40389 | 2025-12-05 11:55:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 554a8266-d6aa-34c9-bb64-e8bbdaed9c65 | -6.14176 | -43.94115 | 2025-12-05 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 34ae451c-e363-32fe-9696-500252208184 | -6.11266 | -44.70726 | 2025-12-05 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fb72cc55-0533-3088-9f0b-c26bd7495e9d | -3.59244 | -42.08904 | 2025-12-05 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5e975276-c17d-3348-83fb-cef1c4071dc7 | -6.14306 | -43.93222 | 2025-12-05 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 14c911a3-9e29-3f0d-a615-3ab5b8e55aca | -3.46305 | -41.51262 | 2025-12-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 835d2855-70ca-35b3-8bed-11821f96a2a4 | -3.5079 | -41.4542 | 2025-12-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3d171bbc-766d-34fd-8cc4-61e42eff9811 | -5.67796 | -35.47501 | 2025-12-05 11:57:00 | TERRA_M-M | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 924b2a95-d142-3ce9-9b87-7b240b24c86a | -3.57729 | -42.06894 | 2025-12-05 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| beb4b36d-1adf-3178-a98a-163863ba57fc | -8.22525 | -37.37673 | 2025-12-05 11:57:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 23328627-b941-38e3-8e6f-5d92f4f7aaee | -3.69591 | -42.01059 | 2025-12-05 11:57:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 6a179ff0-0d0f-3a35-8f5d-ab6e9912b88f | -5.98031 | -37.5304 | 2025-12-05 11:57:00 | TERRA_M-M | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 485ccb9c-0721-3e4a-846c-23b3804a6973 | -8.22625 | -37.38251 | 2025-12-05 11:57:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 4603430f-ebc8-37cf-aaf4-51c6ba45a62b | -6.10219 | -44.71537 | 2025-12-05 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 011d0a98-df01-37e6-8c3c-319d2d11312a | -3.48342 | -41.56148 | 2025-12-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 8381dc97-adf4-328f-8def-8734fb4c1b22 | -3.69718 | -42.00173 | 2025-12-05 11:57:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 143b5006-9c45-3990-88a0-712296b0086b | -6.10359 | -44.70597 | 2025-12-05 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5e3d0227-7584-311f-bd8c-00b3651e2548 | -7.34005 | -37.5521 | 2025-12-05 11:57:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| e1471c24-bca5-3958-bef9-38ef193de0c2 | -3.4324 | -41.47141 | 2025-12-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 2bf1a373-3cf7-3cd6-b522-075f8dd49974 | -3.57603 | -42.07778 | 2025-12-05 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| dd0ac534-6a30-3a6a-84d6-361b3e61b1cd | -4.73395 | -46.38615 | 2025-12-05 11:57:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 7ff9430d-8af8-3d25-abc4-75b5cbc049d0 | -3.51938 | -42.47311 | 2025-12-05 11:57:00 | TERRA_M-M | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| e2de75c8-edf3-3d8a-9366-e316a6a8ae78 | -3.48471 | -41.55245 | 2025-12-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| ea7ea05e-c758-3e30-b68f-9f37e9034e09 | -3.51685 | -41.45545 | 2025-12-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 50.0 |
| c0df3524-4f6c-3f7d-b534-bea95480c146 | -3.686 | -42.0108 | 2025-12-05 12:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| fc57501e-949e-3f25-97ad-c90402dcff64 | -21.66427 | -47.1525 | 2025-12-05 12:01:00 | TERRA_M-T | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| eafb2ff0-f26a-345d-836c-92935c13a0f8 | -22.83894 | -48.00311 | 2025-12-05 12:01:00 | TERRA_M-T | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| eda5e367-d210-32e1-9167-84660ce15749 | -22.25049 | -43.5036 | 2025-12-05 12:01:00 | TERRA_M-T | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 0348adca-c106-3727-9c4a-e8d824143a4d | -29.4546 | -51.52341 | 2025-12-05 12:04:00 | TERRA_M-T | SALVADOR DO SUL | RIO GRANDE DO SUL | Brasil | 4316501 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| eea09e4a-a89a-382e-bb9a-0f9a761739e8 | -3.686 | -42.0108 | 2025-12-05 12:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| b82d3eb6-1ee4-37c8-aed5-3f1192da1164 | -3.686 | -42.0108 | 2025-12-05 12:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 18f825d3-3fdd-3853-8e42-1f4b4e8faa1b | -3.7047 | -42.0098 | 2025-12-05 12:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| b67b18a6-dbe6-385c-b7cd-26e050755a97 | -3.686 | -42.0108 | 2025-12-05 12:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 4762b5c0-5aef-35e6-8d73-7c44d731abd4 | -3.4275 | -41.4504 | 2025-12-05 12:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 8b91aa87-4bf3-3fe9-a45e-3f63eee11d2b | -3.686 | -42.0108 | 2025-12-05 12:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| e551dee0-40cd-3dfa-96f3-3045feb322db | -3.4275 | -41.4504 | 2025-12-05 12:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 156.0 |
| a0e800d0-85f0-329e-b8c1-e3595fa02e22 | -3.4275 | -41.4504 | 2025-12-05 13:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 355.3 |
| 14a91111-2bbc-3735-8064-e2ab6b458da8 | -3.4462 | -41.4495 | 2025-12-05 13:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 142.7 |
| d110d2ee-478a-3117-a914-fcdf68f1c647 | -3.4275 | -41.4504 | 2025-12-05 13:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 143.8 |
| 8beae81c-3cb4-3ec0-8e1b-179f87164381 | -3.4275 | -41.4504 | 2025-12-05 13:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 68632a21-8b31-369f-9d04-4ad996612320 | -21.622 | -56.1312 | 2025-12-05 14:00:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c791cc0d-d2d5-3036-bc2e-4c25f3249b76 | -3.0134 | -41.9475 | 2025-12-05 14:00:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 11165783-880b-3ae5-bfd8-e55aab2a5ecd | -8.2261 | -37.3797 | 2025-12-05 14:00:00 | GOES-19 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 178.8 |
| 73b92161-2d84-3bb0-a7ae-f68d9ef9ce8e | -21.622 | -56.1312 | 2025-12-05 14:10:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 99.6 |


