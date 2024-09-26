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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cb60fb9-9ed0-3007-8d1c-1ac39a89fce6 | -10.03804 | -53.45739 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 57ffb5d0-30cf-3306-9cf3-778bcc34c9b6 | -10.03748 | -53.46104 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| b3e719b2-771c-3281-87c8-187349b7defc | -10.03693 | -53.46468 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 6e7f0d7a-3269-3bbf-ac33-3ce6420a4172 | -10.03578 | -53.44958 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 981974d0-dba0-373c-b19e-f2bdc8197f65 | -10.03522 | -53.45323 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b2f14bf8-01a4-354b-9e56-614b9a680346 | -10.03519 | -53.4308 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b5b1fb-e118-3449-ab72-a806f673a7ca | -10.03467 | -53.45688 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| bf387f4b-ba47-3a0c-b8de-427896ece28d | -10.03411 | -53.46052 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| fc091603-6fae-3d24-9eb7-ced393a6b232 | -10.03356 | -53.46416 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 4de82e65-8c67-3351-9ede-cef2ee53fc6b | -10.03185 | -53.4527 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e52cb99f-2f8f-300b-8828-f2b544dc3de4 | -10.0313 | -53.45636 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| b0e9f83b-d2df-3b0d-b842-203465669dcc | -10.03127 | -53.43392 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af66dbe2-5ceb-3c7d-bb44-22caa0933cc2 | -10.03074 | -53.46001 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| cde7a8a9-d2ff-3579-abbe-9194dd81b6d5 | -10.03018 | -53.46366 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 5692c134-ebc3-34ef-91fc-9224b2e84abb | -10.02848 | -53.45218 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2baedf11-f831-3e14-a1d8-6891ee9b7eba | -10.02792 | -53.45584 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f418a58-1a39-38e8-942d-432874dc293d | -10.02789 | -53.43339 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75b18a0e-f231-37b0-8844-4659f747bbbf | -10.02737 | -53.45949 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5b29904-5462-3040-8afb-b17c6e83315e | -10.02681 | -53.46315 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3355ff78-4269-307e-9b3c-1faf249cdb9c | -10.02455 | -53.45532 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3e387af-98ae-3abb-a10d-737f8d44e545 | -10.024 | -53.45898 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d45ef4e1-3aba-395d-b2d1-dea806f4b48e | -10.02344 | -53.46264 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 048309bc-3aa1-3248-b499-777243bd2eca | -10.02118 | -53.45481 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e0e5e6b-16f4-3c35-a33f-ad1ce280698b | -10.02062 | -53.45847 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 876a5d2a-9e96-3c76-b3d8-a335e342bfc7 | -10.02007 | -53.46212 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab01a28c-d9dd-34d4-90a4-7372ec3c2f19 | -10.01781 | -53.45428 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c66d7b6-3c68-3191-aa77-895fe337d06b | -10.01725 | -53.45793 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0eb56ea-f5f5-398c-90c8-9eb926f9b032 | -10.01444 | -53.45375 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7d015e4-0c97-33d9-82b5-cab002d39e15 | -10.01388 | -53.4574 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1c57cb0-5323-3d78-9af0-a17fd7858df6 | -10.01107 | -53.45322 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d24fb1e6-9a29-3e4d-a299-9fd53a7134a3 | -10.00881 | -53.44538 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad39de2d-3afe-3bbc-ab91-f047ac4fd8d3 | -10.00825 | -53.44904 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a415da8a-dd61-3d25-aea5-4d08d2306f84 | -10.0077 | -53.45269 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26f23121-6136-3d2b-94db-bc6f1dbd074a | -12.26016 | -53.43949 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db966e0b-6aa4-3923-aacd-765f47d11cc1 | -12.2596 | -53.4433 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3666ddf-6bb3-3c83-acb8-ce476f7dbc9d | -12.84777 | -54.03443 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2556ca8a-d3ae-3596-9cdf-ff3cf8e1b63c | -12.84721 | -54.03812 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 145dde64-2ecc-3c7f-b11d-0cff89b09760 | -12.84666 | -54.04181 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9406d76d-54c0-30d3-a668-08287f241c1c | -12.8461 | -54.04549 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f07fdc69-52f7-32f0-9499-b63eddcd7cbd | -12.84494 | -54.03021 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18416922-18f5-3c77-b4cd-29a7ddc80291 | -12.84439 | -54.0339 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19521eb9-eba1-33a4-9c75-abb518e5ec0d | -12.84383 | -54.03759 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d3d79b0-32f6-3ad6-b94e-87f277727ed9 | -12.84328 | -54.04127 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb04d633-2313-3186-ac4d-98cd4c69e66f | -12.84273 | -54.04496 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cbe0beb-2cba-3ce9-9fcc-f0dea0393f95 | -12.84217 | -54.04864 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28f05b5f-5b08-3bf5-bb48-f37b89da2b6f | -12.84156 | -54.02967 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 623b769f-b33b-37c6-8cbf-101594cd07ed | -12.84101 | -54.03337 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 522452a5-5912-3e10-92fb-a3a00057f989 | -12.83874 | -54.02544 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b37c2737-6976-3aab-b414-b1b78cec3329 | -12.83818 | -54.02914 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccb93529-a5af-39b8-8b14-85b9c40b463b | -12.83763 | -54.03284 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57b3a887-1e22-3314-87d1-f4cf0889381d | -12.83591 | -54.02121 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e421c10-7158-3e99-a1d6-975a15758f1b | -12.83536 | -54.02491 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11471d51-afcd-33bb-b5c2-5e4c830664d2 | -12.8348 | -54.02861 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c779d8a1-742f-35bf-a42a-f179aa05543f | -12.83309 | -54.01698 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d63ee535-3abd-3550-a319-dde8e5f4f5d9 | -12.83253 | -54.02068 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75edc0b5-3c69-3e45-9a68-b25deaa9aa0d | -12.83198 | -54.02438 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2ec49a0-8a6f-3d5e-96ca-9ec7d11f598f | -12.83143 | -54.02808 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5ab292b-da96-3a2a-b9ab-1b7c80f7a29b | -12.82971 | -54.01645 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 852ad025-b8f4-3f3e-8a4d-02e1b07bff3f | -12.82915 | -54.02015 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24b61b21-1417-3759-96b2-74237f241fe1 | -12.8286 | -54.02385 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 083b74b8-9620-3e58-a3ba-1e5691bae2a5 | -12.82805 | -54.02755 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccd1de76-b0a8-3df2-8ae0-25271f08aaca | -12.82632 | -54.01591 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f73dc6f-9d80-34fb-8389-8aaf8b67605b | -12.82577 | -54.01962 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc88a995-2e7c-3f80-bc81-64efd432ef8d | -12.82522 | -54.02332 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47bac112-0a20-3bd9-b294-7b10f417b543 | -12.82467 | -54.02702 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9efdcadb-733a-3c34-9f03-b67883312fb4 | -12.82294 | -54.01539 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acbd412c-39d4-3be1-95c8-087b425e722e | -12.82239 | -54.0191 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c446cc3d-c156-351e-b85d-a6363870ad41 | -12.82184 | -54.02279 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78d88081-6ef9-3746-829b-d5a6f89e5202 | -12.82129 | -54.02649 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6af48e2-fd6e-30a2-9cd0-b46e10d3339b | -12.82074 | -54.03019 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f6436c7-78c6-3caf-9451-052914a72b44 | -12.81956 | -54.01487 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a40197a9-347e-3fff-a6b0-ad4d30b0b8b9 | -12.81901 | -54.01856 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeaa2854-cb45-31ce-a34f-49acc6cbc14b | -12.81791 | -54.02596 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e701ec9-e3ba-32f8-8c9a-7135776bf5ee | -12.77945 | -54.04237 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0d4cbea-00e5-36d0-8636-2a2f08f5723b | -12.7789 | -54.04605 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad817ae0-bc5f-3c9f-a36a-07d0e49365e1 | -12.77834 | -54.04971 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35c7a5c4-8327-399c-8a84-8cc2ea97a119 | -12.77607 | -54.04185 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a4096e2-115a-31f4-8483-12ef431354a9 | -12.77552 | -54.04552 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61d368f5-2523-3bca-a716-52dc270f401f | -12.77496 | -54.04919 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47242b33-5875-31ba-aa8b-403c43db2aef | -12.77325 | -54.03765 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bce53ab6-cc35-31e3-985c-9adcb5794012 | -12.7727 | -54.04133 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1234c8e2-b7b5-3bf4-87db-270ad6e1fd9b | -12.77214 | -54.045 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5ffbe73-01c3-3827-ac09-a94f75b403f7 | -12.76992 | -54.05968 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d008eb70-8927-30a6-98f4-956021e0bbc3 | -12.76988 | -54.03712 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e212c944-30d0-34b1-bbb4-7fe1e4739b87 | -12.76932 | -54.0408 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cd71a13-2492-3c74-90d0-b84e66cb3152 | -12.76876 | -54.04448 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38688f4e-4614-383e-875f-12fd3289ddcc | -12.76765 | -54.05182 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3045906a-4f86-34a5-9984-7922f05e694a | -12.7665 | -54.0366 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f859ace0-10f0-3a48-89b1-817507e482b4 | -12.76599 | -54.06283 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad6ff962-0572-309a-845e-869a8b23faf1 | -12.76594 | -54.04028 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f95c28dc-c383-30e0-9af8-4d1a1bac3486 | -12.76539 | -54.04395 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbe7cc2b-3f7f-336f-ad3b-46798512b6a5 | -12.76257 | -54.03975 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca328987-3ae8-3b03-ada6-3205de16874d | -12.76201 | -54.04342 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fb8d722-7fd0-3b75-90d4-ad1f30bffbf8 | -12.76146 | -54.0471 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c040779d-b3bf-30dd-a452-9755dfacbb10 | -12.7609 | -54.05077 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5db6cee1-6704-331a-b030-3d624c7c9b46 | -12.75808 | -54.04657 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02e732b-0f66-394d-86e7-f64c62355d36 | -12.75697 | -54.05391 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6b0e709-8411-3393-b7dd-8e6c3acfe94e | -12.74241 | -54.08177 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35b13726-dc3f-365f-be91-79d6cf80cb53 | -12.74186 | -54.08545 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a7788d6-3810-3089-976b-b53456c7d260 | -12.7413 | -54.08912 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README124.md)
