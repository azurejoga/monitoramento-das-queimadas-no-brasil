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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9158ea3e-7ade-32ab-b1f7-619e58effbe4 | -6.1891 | -41.0884 | 2025-09-12 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 7ead7ad6-74b3-314b-8d17-7c63a54c7908 | -16.9621 | -45.8176 | 2025-09-12 12:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 115.9 |
| ab0626e3-b3d7-37d4-aa48-530350d1952c | -9.0376 | -47.0819 | 2025-09-12 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1c7d5ec1-cc09-34c8-a825-d9ae5013af82 | -9.0759 | -47.0335 | 2025-09-12 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ec613abd-0686-302a-a574-e63524288d46 | -14.4394 | -47.3206 | 2025-09-12 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 61c1a899-f2d1-3913-bd7a-f511f88b558a | -9.057 | -47.0355 | 2025-09-12 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1edeee59-bb15-3110-8058-69d84919e3a3 | -16.3127 | -50.0868 | 2025-09-12 12:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 148.8 |
| b1ab302b-8c59-3e9e-8f21-75341b751cfc | -12.0849 | -47.6065 | 2025-09-12 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 16954be2-4f99-31c8-86d8-6df9bc5a409b | -15.1402 | -50.1628 | 2025-09-12 12:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f5efc536-2a67-3082-864a-fe861db3be3b | -11.9523 | -51.1661 | 2025-09-12 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d57006ea-484e-3020-a348-578efa7f0013 | -14.2162 | -58.5917 | 2025-09-12 12:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 73dd03cb-5a5b-3b5d-83bc-47269329644d | -10.2217 | -46.2332 | 2025-09-12 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2a8c3544-4e8a-328c-9917-70692d4e98c5 | -11.1149 | -51.3423 | 2025-09-12 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c1054ba8-c2e7-362f-a895-ed1be86bf220 | -14.1907 | -46.2012 | 2025-09-12 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 1d77d17e-b694-3d48-9fd3-7f0b882f7008 | -7.5641 | -44.4068 | 2025-09-12 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 06fe4e34-d8eb-31ec-b74b-b4290683fd19 | -11.4402 | -48.5513 | 2025-09-12 12:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 82c7b0af-0b25-3d51-93af-ee88c79a6424 | -21.17912 | -54.96941 | 2025-09-12 12:40:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 99307d65-222d-3b93-83fa-e809c68a5a0e | -25.02912 | -49.5265 | 2025-09-12 12:40:00 | TERRA_M-T | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 9a9e6044-730d-38a9-b748-3687b33f0462 | -22.66668 | -47.70383 | 2025-09-12 12:40:00 | TERRA_M-T | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| f6d1b044-b2f6-3e78-9e36-9f153410ee0a | -23.12422 | -47.4948 | 2025-09-12 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.4 |
| 08eba99f-cba4-3a66-9b96-e9eaac25daa2 | -23.75614 | -54.80429 | 2025-09-12 12:40:00 | TERRA_M-T | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a6f60eaf-47a9-35e9-a2d2-e226fffe3229 | -22.66456 | -47.70931 | 2025-09-12 12:40:00 | TERRA_M-T | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| ff7e26b6-bfa8-3d86-a14c-cf0a3d7a43ee | -23.63278 | -52.85986 | 2025-09-12 12:40:00 | TERRA_M-T | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 75352174-c8ec-376f-8a4c-b7b933832b7c | -22.04726 | -55.64592 | 2025-09-12 12:40:00 | TERRA_M-T | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 56f66a20-7b94-3a29-adcb-a01e48ad1982 | -21.15384 | -54.9555 | 2025-09-12 12:40:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 6ccc0af2-a3e8-3435-a38e-4451ae269707 | -23.62755 | -52.85251 | 2025-09-12 12:40:00 | TERRA_M-T | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 67ab1ae6-79eb-3e0e-bc7c-28b1a29301dd | -21.84492 | -49.89816 | 2025-09-12 12:40:00 | TERRA_M-T | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| ee2508d9-bd8a-3d1b-9c22-ffe601ddc00c | -21.16133 | -54.96648 | 2025-09-12 12:40:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 26.0 |
| dc6ad986-aa47-3c11-aa38-e9e69981b4ae | -22.26627 | -47.54775 | 2025-09-12 12:40:00 | TERRA_M-T | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 3bbb4f6a-fad7-3afa-a0a0-1b05f195d1a0 | -23.24333 | -51.13696 | 2025-09-12 12:40:00 | TERRA_M-T | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| bc93eb6d-39d7-35d7-b78b-22c0f81ad3f8 | -22.40114 | -55.4365 | 2025-09-12 12:40:00 | TERRA_M-T | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1415b015-9bdc-393a-b16b-bf40dcbd32c6 | -21.72704 | -49.74068 | 2025-09-12 12:40:00 | TERRA_M-T | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 253bcf25-6d69-3a42-a70a-a6257c8e5e2e | -23.63414 | -52.84921 | 2025-09-12 12:40:00 | TERRA_M-T | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 7394ed48-8322-3f13-9656-c9e96bbc4e81 | -22.77762 | -46.7321 | 2025-09-12 12:40:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| 24bda746-95d5-31c8-ae7b-06f80bc738a8 | -25.18484 | -53.14368 | 2025-09-12 12:40:00 | TERRA_M-T | CATANDUVAS | PARANÁ | Brasil | 4105003 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| fc510d0b-3710-3db4-a204-14062e8ba816 | -21.15244 | -54.96501 | 2025-09-12 12:40:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 408.0 |
| 655d07a1-f7e4-30f0-a60d-cf00e7cf9088 | -22.78232 | -46.73842 | 2025-09-12 12:40:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.0 |
| 4bdeabcf-614f-380c-86ef-6010e6e65adb | -23.15534 | -47.45045 | 2025-09-12 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| d77bded6-693b-3ab6-89b9-9165cf98823c | -22.22739 | -49.94253 | 2025-09-12 12:40:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 8db59ae5-7253-30fb-8254-e5235516efb8 | -23.11304 | -47.51 | 2025-09-12 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.2 |
| fe56dcd7-74bc-30b5-ab85-7746928dd6ea | -21.89383 | -49.85948 | 2025-09-12 12:40:00 | TERRA_M-T | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 108a0102-a6b4-3913-8fbd-b2e00268567d | -23.12865 | -47.48849 | 2025-09-12 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.5 |
| 66c75ffb-2087-37b0-9b0c-4594e19ebb0b | -23.12638 | -47.51138 | 2025-09-12 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.7 |
| 728705e3-3e34-3c39-b11d-ab4bd4c89bc2 | -23.15314 | -47.47398 | 2025-09-12 12:40:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| d6e25fd2-4411-3563-92f4-ded941ed3d12 | -29.16138 | -52.21095 | 2025-09-12 12:42:00 | TERRA_M-T | POUSO NOVO | RIO GRANDE DO SUL | Brasil | 4315131 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 8c436b8d-5f53-3862-97b7-827f7d49d056 | -26.32095 | -52.69682 | 2025-09-12 12:42:00 | TERRA_M-T | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e1c0147a-4eac-3378-bbe1-937dbc4cde51 | -27.43929 | -52.35244 | 2025-09-12 12:42:00 | TERRA_M-T | ARATIBA | RIO GRANDE DO SUL | Brasil | 4300901 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 62d8321b-d10a-32e3-bd55-28eba9926c64 | -25.65204 | -53.30013 | 2025-09-12 12:42:00 | TERRA_M-T | NOVA PRATA DO IGUAÇU | PARANÁ | Brasil | 4117255 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 1e86de9c-3e1d-3fa6-b525-ec6243a0eab5 | -26.00592 | -53.17823 | 2025-09-12 12:42:00 | TERRA_M-T | FRANCISCO BELTRÃO | PARANÁ | Brasil | 4108403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6d654e97-7e01-318b-80ae-0010c1385d59 | -29.75827 | -51.65955 | 2025-09-12 12:42:00 | TERRA_M-T | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| d0e78828-e826-31a6-9c45-495797a971d7 | -30.63345 | -52.73801 | 2025-09-12 12:42:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 7.9 |
| b0687d5b-1e2e-3ebe-8735-82e1ae437933 | -29.70824 | -51.82307 | 2025-09-12 12:42:00 | TERRA_M-T | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 9.1 |
| 2faf3ddd-7cf1-3df0-986c-a3b876fe8ae0 | -29.70456 | -51.81656 | 2025-09-12 12:42:00 | TERRA_M-T | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 9.3 |
| bc0a5f37-d007-30dd-8561-92df8e997a10 | -7.5643 | -44.3838 | 2025-09-12 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 092d35df-b97a-3052-a922-66ed2809bbd1 | -6.309 | -42.2311 | 2025-09-12 12:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 080ddaf3-4b59-34f8-b659-950c16aa83f0 | -15.5236 | -48.5332 | 2025-09-12 12:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3a397c8f-c19d-3c6d-8877-e3163be246da | -8.8899 | -49.945 | 2025-09-12 12:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 62bad2d7-f2bb-3d3f-bbeb-407da188a6b8 | -15.2276 | -49.6672 | 2025-09-12 12:50:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 73b27a6d-1917-39f0-99c5-1f29f4f2c3fe | -9.0379 | -47.0597 | 2025-09-12 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| de345655-b3b0-3227-a8ae-9ea668f5f3ac | -12.0657 | -47.6091 | 2025-09-12 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f51ec70a-ed2d-3f0c-a74b-732382856f63 | -15.1406 | -50.1409 | 2025-09-12 12:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9c58b3d1-c89f-3bcd-8766-71f7daa01a80 | -12.0849 | -47.6065 | 2025-09-12 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 307.3 |
| 56773911-917c-372c-9e73-416998f1c8bc | -7.3212 | -49.6255 | 2025-09-12 12:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4b63b004-acb0-335e-bf89-2e810cbbbb22 | -9.0376 | -47.0819 | 2025-09-12 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 21bb3d43-d981-3325-9a6d-042c4c19d28b | -10.0943 | -47.1664 | 2025-09-12 12:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 65c9eb63-649b-37c9-872d-1b0e8c430c2c | -16.9621 | -45.8176 | 2025-09-12 12:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 0d855db1-0348-3da1-9c59-12191c078fd1 | -12.9101 | -54.7558 | 2025-09-12 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 37095931-c83c-3a8b-93ae-702eec9b9c9f | -9.673 | -47.5459 | 2025-09-12 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 6bce7a29-e18a-330c-8655-7b0682f65610 | -9.057 | -47.0355 | 2025-09-12 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5bc43c1e-a6c9-3eeb-b87a-2d9c5092fc22 | -8.9563 | -46.0849 | 2025-09-12 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9e018edf-9f2c-38bd-abfb-a4008cda4102 | -16.293 | -50.0901 | 2025-09-12 12:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 8dce8bbe-a6e9-3a98-af6b-3017b079560e | -12.0852 | -47.5842 | 2025-09-12 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 7f2e4e8e-86d0-3e85-9cb1-38fe54981779 | -6.8184 | -45.6349 | 2025-09-12 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 569064c5-ad48-3bb6-8289-54c297d2dcf2 | -8.8901 | -49.9236 | 2025-09-12 12:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 99a9b8f9-c968-36c6-bd6b-3623594148de | -10.6983 | -48.6393 | 2025-09-12 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| addf0d17-bd67-3d6b-b8d0-6ef4d221156a | -10.679 | -48.6633 | 2025-09-12 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 10ceb5d6-1bd0-34cb-91cb-a58fd77152f2 | -8.5076 | -47.3118 | 2025-09-12 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c34c20e0-ff97-3c6e-b656-819f49e61946 | -11.4863 | -49.2658 | 2025-09-12 12:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 69b77099-2b85-3ac7-9a86-e78290c566f4 | -9.7197 | -46.8972 | 2025-09-12 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cea305d7-0d41-39fb-83ff-298e3c87496e | -8.9746 | -46.1279 | 2025-09-12 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 3215dfa1-506e-3cbf-b715-fbc2948bf06a | -15.1402 | -50.1628 | 2025-09-12 12:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 879a0354-ab9a-345c-8bba-b7eebdc6e3c3 | -8.4888 | -47.3137 | 2025-09-12 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b82ec8e2-7b93-3ded-b5c3-0dcf131dec45 | -7.4598 | -45.3076 | 2025-09-12 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| f8778110-b408-3d8c-aeeb-98330bf36aff | -8.1837 | -46.0965 | 2025-09-12 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ea7e5f11-d30f-3a20-b20f-5475e2ba7ca3 | -7.4786 | -45.3058 | 2025-09-12 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6ab38588-2bc8-31ab-b8ca-e03dc79a0790 | -6.8369 | -45.6559 | 2025-09-12 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| f78569e3-30af-31a1-8932-6b3e99d6b87c | -9.9004 | -51.8811 | 2025-09-12 12:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 67f64585-75f7-39b0-aacc-a2a3b650bf26 | -6.1891 | -41.0884 | 2025-09-12 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 1139ab33-42b8-37ac-9bfe-7dd872b878b2 | -9.6727 | -47.568 | 2025-09-12 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 76f37bc2-85a2-309d-8e2d-7a066d8683ea | -10.6979 | -48.6612 | 2025-09-12 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 21adc0c5-6838-3288-9be3-87f9558c3315 | -12.9292 | -54.7538 | 2025-09-12 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 250.0 |
| 7b6cc699-c11d-3f36-b51d-70b873be4829 | -6.1703 | -41.0901 | 2025-09-12 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 471.0 |
| 3e01c4a7-46d6-3989-943b-75c7f827a295 | -8.4893 | -47.2694 | 2025-09-12 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 04cbb178-09a9-3d9a-8f59-f3286dbb1be0 | -9.77 | -46.0163 | 2025-09-12 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 05d2ba39-f1d3-33fa-836d-563b04bf0d2f | -12.9294 | -54.7333 | 2025-09-12 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7379dd61-3614-38a2-9915-4f216c3057d7 | -7.5641 | -44.4068 | 2025-09-12 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d00b8c72-fcd9-3cc3-b844-91a99b919917 | -9.72 | -46.8749 | 2025-09-12 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c0b598dc-ce57-3550-954d-2463ea38aef5 | -13.2414 | -51.7359 | 2025-09-12 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8f1a41b5-5f32-3dd4-96fa-24f9c6ea616b | -13.0018 | -46.7341 | 2025-09-12 12:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 8588af87-981b-34db-9acd-11a324e84253 | -12.6821 | -45.3209 | 2025-09-12 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |


[Clique aqui para ver as próximas entradas](README128.md)
