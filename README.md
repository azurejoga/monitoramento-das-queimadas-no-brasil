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
| 18f2e9de-abec-3bb3-b8ea-324b28dc6321 | -3.8631 | -40.653 | 2025-12-20 00:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 5754dbe9-9133-35ee-a186-1792db9959bb | -3.8633 | -40.6286 | 2025-12-20 00:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 63.8 |
| bdf257ba-99e2-322f-a8ac-7b3a04f605c8 | -9.5821 | -44.6007 | 2025-12-20 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d37a7eff-8aab-38fb-a31a-985a1daada40 | -9.5631 | -44.603 | 2025-12-20 00:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c5f8ade9-844b-37c3-b39d-decbac5ca507 | -3.1894 | -48.0289 | 2025-12-20 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 59febac2-a56a-35ed-be1f-29ffef65c533 | -3.8819 | -40.6519 | 2025-12-20 00:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 61.0 |
| c8c8d761-2797-329d-b731-7dc06ec71c60 | -7.3983 | -35.2454 | 2025-12-20 00:10:00 | GOES-19 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| d892aa1c-bee0-3b67-8ed7-bf64c5c63c34 | -9.5821 | -44.6007 | 2025-12-20 00:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e725230d-b016-309e-9277-310939c4acf1 | -3.1894 | -48.0289 | 2025-12-20 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c44883de-32ff-3a7f-a864-18522c0535a9 | -9.5631 | -44.603 | 2025-12-20 00:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a29bdbdb-f896-3e35-9749-2bef210d6828 | -3.1519 | -48.1382 | 2025-12-20 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 10a1b075-b312-39e6-943f-ab358bc0d746 | -3.1894 | -48.0289 | 2025-12-20 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f937a125-2e61-3cdf-9ec5-d2a2bdc34e0c | -9.5631 | -44.603 | 2025-12-20 00:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| d7b76d35-f376-3f4c-b4dd-ecce8a50360a | -3.1894 | -48.0289 | 2025-12-20 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| df0874fe-6a35-310a-addd-16b07b3d76d6 | -9.5821 | -44.6007 | 2025-12-20 00:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 71fb8cdf-637f-3b64-a0c7-e0f6ecc2fbfd | -9.5821 | -44.6007 | 2025-12-20 00:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a8dd0e13-049c-36ae-9f06-b4ff1fa23a3e | -2.5627 | -47.31 | 2025-12-20 00:40:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ddca52c7-5718-3bdb-a926-795f6f4f74c4 | -3.8633 | -40.6286 | 2025-12-20 00:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 3ac00b46-939c-3e48-8335-9306ff8f8e40 | -3.8631 | -40.653 | 2025-12-20 00:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 72.0 |
| ce75dc3e-53ef-34d6-998b-c5c3bd7618c5 | -3.9603 | -40.1575 | 2025-12-20 00:50:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 2456bbae-218d-37ae-81a7-3a72f2c4a735 | -18.8277 | -51.622101 | 2025-12-20 00:51:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4b21a903-d46c-36ef-ae2f-6468bdab472b | -18.825199 | -51.6119 | 2025-12-20 00:51:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 12580027-449d-3dec-980a-6825fda63243 | -20.3041 | -57.266899 | 2025-12-20 00:51:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 61d27ac7-46ea-32d8-a384-92ea812559dd | -20.4597 | -56.5499 | 2025-12-20 00:51:00 | METOP-B | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a1444309-9bfc-36bc-ad1f-64662480a3ce | -21.3573 | -56.859501 | 2025-12-20 00:51:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a52625d4-e61e-3c5a-907a-287104ed7181 | -20.3057 | -57.274399 | 2025-12-20 00:51:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b56ae004-26e2-3d52-a8ea-4adb9fb19d69 | -21.2073 | -56.926899 | 2025-12-20 00:51:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7e042276-9675-35ce-aea7-813d64db8766 | -9.7231 | -60.196098 | 2025-12-20 00:51:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 002f6eb9-40cc-3305-9149-415dea1b562c | -20.313801 | -57.264599 | 2025-12-20 00:51:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fe792810-95c6-33b6-b89f-1cb3102bba74 | -20.458099 | -56.542599 | 2025-12-20 00:51:00 | METOP-B | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc5d2e0-c6cf-3272-bcdd-1f170bd30344 | -9.5821 | -44.6007 | 2025-12-20 01:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 23d0dac6-609b-3259-ba63-cf3fb1505454 | -3.8633 | -40.6286 | 2025-12-20 01:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 55.9 |
| abd50e99-5f8e-3c5e-9c89-fb52a4dc7a69 | -3.1894 | -48.0289 | 2025-12-20 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e0427004-73db-3c56-844f-51db52d8aefa | -3.8631 | -40.653 | 2025-12-20 01:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 5861a2a6-c8f0-3e5d-a027-ee702ee0daab | -21.69382 | -55.62767 | 2025-12-20 01:06:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 624bbfca-c58d-3b17-b246-953ad3649279 | -20.45487 | -56.54918 | 2025-12-20 01:06:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df6f99ed-8c76-3610-9db5-fbbf612f5313 | -20.30785 | -57.26886 | 2025-12-20 01:06:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b57286a5-602d-3ce9-a596-3b5d398b9bb6 | -20.30916 | -57.27824 | 2025-12-20 01:06:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 8eec4549-e94b-35a6-8803-cacc91ecfff7 | -3.8633 | -40.6286 | 2025-12-20 01:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 73254a85-a549-3a78-9563-0a2df86c257f | -3.8631 | -40.653 | 2025-12-20 01:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 353a5bb7-c979-3f44-a9ed-edbfa9119ac7 | -2.5627 | -47.31 | 2025-12-20 01:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7f7dcb81-154b-3050-b903-9dfe7df4172f | -9.5821 | -44.6007 | 2025-12-20 01:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b555551e-1da6-3823-bab4-854073dadef8 | -3.1894 | -48.0289 | 2025-12-20 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 03e55b39-cfc7-31a9-97f4-402f666e6bd6 | -9.5821 | -44.6007 | 2025-12-20 01:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 594d410d-6c82-3e2c-a2a2-ec1a6d66cc74 | -3.1894 | -48.0289 | 2025-12-20 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4ae0a784-cb4c-31ba-b409-c895874ff0b1 | -9.5821 | -44.6007 | 2025-12-20 01:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 97ef38fe-564b-33cc-b3c9-6439e8287578 | -3.1894 | -48.0289 | 2025-12-20 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 74bc730b-36e5-304c-a6b8-4e2d8a3e56ab | -20.311899 | -57.270401 | 2025-12-20 01:30:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c42aa1dd-c5a2-317e-9f00-8a0c601fa3dd | -20.313601 | -57.277802 | 2025-12-20 01:30:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 146be045-8b80-3287-9c16-c5f432b12f2d | -19.8223 | -54.744301 | 2025-12-20 01:30:00 | METOP-C | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6305d2de-4005-32d5-bbe0-3c41784a1f80 | -20.456699 | -56.548599 | 2025-12-20 01:30:00 | METOP-C | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 18d59792-347c-3679-bae5-61d724b51b61 | -19.820101 | -54.735298 | 2025-12-20 01:30:00 | METOP-C | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bec966e2-dc9a-39b3-9193-794a8a088f8b | -3.8937 | -41.7135 | 2025-12-20 01:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 6c6882b8-1e04-320d-96b4-299584dc7853 | -3.1894 | -48.0289 | 2025-12-20 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e7ad062f-51f6-3327-8b47-911a5b756ae7 | -3.9126 | -41.6885 | 2025-12-20 01:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| e92dd90b-3537-3364-8446-3e1747cd8207 | -3.8939 | -41.6896 | 2025-12-20 01:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 7f13370f-04d4-39cc-b31b-a8664c363fa7 | -10.1806 | -36.2962 | 2025-12-20 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 148.4 |
| 75043603-2a3c-352f-82bb-b14072a3b5aa | -9.5631 | -44.603 | 2025-12-20 01:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a071081e-f5dc-3734-8301-fa30575d5235 | -3.1894 | -48.0289 | 2025-12-20 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 96158cb4-fd80-3841-b473-fe6be06e0bcf | -9.5821 | -44.6007 | 2025-12-20 02:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e082a9b6-e21c-364b-9f2f-437613cd8fe7 | -3.8631 | -40.653 | 2025-12-20 02:20:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 49.6 |
| fe1b90b9-57c5-3ed9-9c3b-4dd741894135 | -3.8631 | -40.653 | 2025-12-20 02:30:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 5f643912-d0ce-3d51-b373-427992d2766e | -3.8633 | -40.6286 | 2025-12-20 02:30:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 56.0 |
| c2164826-ba1b-3518-a440-ba4729d6d0f4 | -3.8631 | -40.653 | 2025-12-20 02:40:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 71.3 |
| c055399b-aba8-3b8d-a3f0-13daf3c7dad4 | -3.8633 | -40.6286 | 2025-12-20 02:40:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 22925ee3-5ff5-3693-b255-b5cc7c1ca9c3 | -3.8633 | -40.6286 | 2025-12-20 02:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 30a94805-e178-39f7-ab6e-2e56a57fcce2 | -3.8631 | -40.653 | 2025-12-20 02:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 70.1 |
| e1f711d1-3a6b-3c18-bac2-a53205f0acdd | -3.8631 | -40.653 | 2025-12-20 03:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 37762d07-3cf4-3717-9492-0c7dd6880e21 | -5.09098 | -37.55147 | 2025-12-20 03:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 926988fa-1687-3f24-9aa7-9532f984ac6b | -3.8631 | -40.653 | 2025-12-20 03:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 15fcf619-733b-3511-a322-89a6442a6ede | -3.8633 | -40.6286 | 2025-12-20 03:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 56.3 |
| 99621e38-380d-3f93-865f-8a4ee26246ac | -9.38096 | -35.95003 | 2025-12-20 03:10:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 301f54d4-493b-3568-96f2-78109a09863a | -9.43111 | -40.31696 | 2025-12-20 03:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6e152b69-2eb2-3e8f-8512-fc9d6855b678 | -8.62591 | -37.001 | 2025-12-20 03:10:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 480160d2-334c-3d18-97b2-27f2886a9d31 | -9.37618 | -35.95229 | 2025-12-20 03:10:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 5b39cf61-e131-3e53-98be-90a4d77859ad | -8.2548 | -35.82787 | 2025-12-20 03:10:00 | NPP-375D | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1f0f7e2b-20fc-3eb5-bcb3-5c09984151a1 | -9.43247 | -40.31018 | 2025-12-20 03:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a9d68a39-4431-3be2-bcbb-1d8bcdbfb7e7 | -9.74742 | -36.32476 | 2025-12-20 03:10:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f6b422e1-49cc-3dbb-84a0-b9313cbb8773 | -9.95906 | -36.52457 | 2025-12-20 03:10:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 67c352f4-c745-3080-9b31-5f1cc372133b | -9.38159 | -35.95341 | 2025-12-20 03:10:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 416035fb-e3e5-39b5-8399-79ed067f4b92 | -7.40101 | -35.23671 | 2025-12-20 03:10:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| defe63ec-a45f-375e-961f-a85656332ad5 | -9.98006 | -37.03961 | 2025-12-20 03:10:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79fb30cb-cd62-35e2-80cc-a4641001725c | -7.1761 | -35.16768 | 2025-12-20 03:10:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7ca7f0f1-e1aa-319f-a865-1b31c837c573 | -9.37684 | -35.94881 | 2025-12-20 03:10:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 88fa3bb8-ed27-328d-8190-3459877db096 | -7.51909 | -35.23821 | 2025-12-20 03:10:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6176cf17-0d79-3226-9025-aa9e60ab144a | -8.93364 | -35.70685 | 2025-12-20 03:10:00 | NPP-375D | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67d72490-fee1-3c4f-914b-63e00f1a0e35 | -9.38032 | -35.95355 | 2025-12-20 03:10:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| bba490c6-113a-36ee-962e-0734d0de481e | -10.77209 | -37.14289 | 2025-12-20 03:10:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8644f1db-5e99-3a87-b955-7f8a12f8e515 | -9.38226 | -35.94987 | 2025-12-20 03:10:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3a466e82-ba54-3a35-9440-289dfbd91cf0 | -7.39558 | -35.23611 | 2025-12-20 03:10:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e347026-2178-3ecc-9bc7-c4d7940f7488 | -8.26026 | -35.82903 | 2025-12-20 03:10:00 | NPP-375D | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6ecafb8e-404e-31cd-909a-146ea29c0835 | -7.40039 | -35.24014 | 2025-12-20 03:10:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 75275853-71a8-3569-97ae-1e9ba5d97469 | -9.3749 | -35.95247 | 2025-12-20 03:10:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| b42e3832-ab51-36e2-9bef-939723d05ce8 | -7.51377 | -35.23709 | 2025-12-20 03:10:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa72a753-69b0-3784-86e3-a84c402cc84b | -9.95348 | -36.52354 | 2025-12-20 03:10:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46473cec-8f77-3a52-b2c2-efdeb2d4bbf9 | -6.09964 | -38.41352 | 2025-12-20 03:10:00 | NPP-375D | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d670f17-12b6-3169-89ec-85ed5bfd8167 | -9.37554 | -35.94899 | 2025-12-20 03:10:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 53b6a279-3df9-3b5b-a7f4-f1a3955cf4bb | -6.09871 | -38.41856 | 2025-12-20 03:10:00 | NPP-375D | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ba64d09-fc5d-3257-a7d4-96c36cb405b4 | -10.76637 | -37.14179 | 2025-12-20 03:10:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93b5a408-d977-34e7-8556-59a5a8cfe911 | -8.93307 | -35.70996 | 2025-12-20 03:10:00 | NPP-375D | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
