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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00390a08-8c4f-30d2-b6e2-c8c7c9946ae0 | -12.95072 | -54.77533 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 67d8fa19-f77d-384b-8577-653e038557c2 | -11.21728 | -55.01275 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a953b689-60b9-3de8-992d-260f9838b8a8 | -14.35061 | -60.3243 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f05aad2-fbbe-3a60-9fda-3446ea9d95d0 | -12.6377 | -56.98128 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56f7046b-0040-3e2c-aae3-ad4dd2fd59de | -11.47976 | -55.55436 | 2025-09-07 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eea7fa06-7b31-357b-832c-d363acd774d2 | -12.71504 | -56.55994 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 98c2c29c-95c6-383a-b472-b1d167b69394 | -13.90689 | -54.00831 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7a198af2-d3bf-33ca-adf2-96a78cd9962c | -12.61215 | -56.98354 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c82e71e6-afd8-36d2-ac35-2af670a96f9b | -10.57217 | -61.23996 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a20aeb74-5a13-3f54-a03c-727e0a58e8f0 | -10.88422 | -55.72176 | 2025-09-07 05:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 701a7e7b-458e-3731-938d-441897b05376 | -12.42603 | -63.89533 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcc213f0-9ba2-39e1-961d-8369a6d39fea | -12.15306 | -60.71019 | 2025-09-07 05:40:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 353f0f37-b47b-354e-b055-bf8f821ddff3 | -10.15258 | -61.13587 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6320ed52-1332-3b83-af46-bb26d29c7ba3 | -10.4554 | -53.609 | 2025-09-07 05:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a76b122-30b8-3a2e-b69f-0c05b1a379dc | -12.63768 | -56.98188 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c10b538-cd08-35d7-971d-d317ca8ac7f3 | -11.16901 | -59.15488 | 2025-09-07 05:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb604402-f39d-3528-a724-9012d5f774ac | -10.27868 | -63.43969 | 2025-09-07 05:40:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1978b63-8916-385e-9bef-2b8ac8f5a023 | -12.41873 | -63.8979 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bea4896-09b5-3d9f-b09b-5496c5925232 | -11.16014 | -59.15711 | 2025-09-07 05:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01957b56-2ae5-3d2a-8aa2-124923b21b96 | -9.35225 | -65.41551 | 2025-09-07 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ea5292-ff2e-356c-af4b-dd9658638a44 | -12.92763 | -54.77223 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1e11168e-de41-3d8a-b5a4-b76af98742e3 | -16.28624 | -58.11784 | 2025-09-07 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 98fc453a-bc8d-39f5-a042-513c0a4333a0 | -11.6969 | -60.16404 | 2025-09-07 05:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57a58877-c2fc-38ea-9a23-b96a61b81a95 | -11.77948 | -60.8945 | 2025-09-07 05:40:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c1089f5-80c7-32d0-97fb-4149b10a3cf5 | -14.42577 | -60.19341 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e476bce4-1113-355c-81db-0bda896d5494 | -9.94971 | -60.15248 | 2025-09-07 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8db983a-7132-35aa-b5b9-b50c1954bf5d | -15.70131 | -53.55979 | 2025-09-07 05:40:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d87e6b09-bc18-3039-8b9b-5eca336f8482 | -10.17156 | -61.13421 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c27399f3-cb39-3f22-a8c7-c28ed6958e9d | -10.37619 | -64.80476 | 2025-09-07 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57105c93-6b15-3229-b79f-ad2f138b61e6 | -11.21036 | -55.02314 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a788051e-3a5e-3984-abb0-3f011ec38234 | -12.81776 | -52.93852 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c94bc67-c3e4-30a9-ad7c-9a1afaec2358 | -13.91623 | -53.98044 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3f7577cb-1760-3bf2-a8b3-f00c2282fc0c | -12.81614 | -56.52102 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3273003-0b7a-3b07-b2c9-4f713332b93b | -11.21636 | -55.02019 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33d5497d-4033-36b4-9e7c-826134e5534f | -12.71978 | -56.56368 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| cdd1ef69-419d-3eb6-a1e3-6ad5300c7a53 | -10.57033 | -61.25269 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7a7666a-2f43-31d7-b2ed-9e5774e44dc9 | -14.35068 | -60.31923 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6bb9382-50ba-3e78-a10a-0b148c9709a6 | -11.16378 | -59.16163 | 2025-09-07 05:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bc0e47d-5a03-3f7f-910a-d6b066233e28 | -12.94835 | -54.79556 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f483207-8a1d-309d-a405-9a283c072b57 | -12.43927 | -63.93054 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce856d5e-1e59-37ef-a8d2-15610b087e22 | -14.41755 | -60.19235 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5845c17f-0715-3efe-9474-1a4b9758bf83 | -10.46141 | -53.60992 | 2025-09-07 05:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76a2ec18-8ee3-3cf6-9fe1-150046cf78dc | -15.88418 | -52.19113 | 2025-09-07 05:40:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8b7d1f2b-1e5d-3ecb-82ac-d112c6f68e04 | -13.91249 | -54.01378 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b0ac6480-461f-38e6-abdb-e11c49d180c6 | -12.64267 | -56.98188 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e22d17a6-e7b7-35a4-8ec2-ef2f1f299c97 | -16.33233 | -52.94272 | 2025-09-07 05:40:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77fbeca2-6003-3cb2-a54b-33c9579fd6b5 | -12.77606 | -52.95502 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 397c07df-633d-3c30-b699-629244dc7f94 | -12.63271 | -56.98125 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8736f5cd-9cb7-3650-9046-59a44e5a2c62 | -13.90739 | -54.00375 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6b9ae8b-083d-3a5d-b9ea-ad5184cafda6 | -12.41424 | -63.90461 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84e21500-ce9c-3db4-aad1-82ebfbea1a44 | -19.86397 | -57.88736 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a3061844-685b-3bd0-ae01-4c47d89e9a17 | -19.88597 | -57.89623 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4367e19d-51b8-32a0-97d1-51c3087b073a | -19.86362 | -57.89056 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 196a7a80-d095-30f9-a58c-a6c482a75296 | -19.88563 | -57.89943 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ed3ab5e4-9ef2-3f35-b36a-b43928e290c2 | -19.87356 | -57.89499 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e6be544d-434d-39bc-bebf-9c58c89c518a | -19.88048 | -57.8988 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 43f6c170-e717-3e49-aba8-27fda32921eb | -19.87052 | -57.89434 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| c27221ad-5f58-3f16-9637-47e67e74dad3 | -19.876 | -57.89177 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 01f19c7f-ae4b-378e-b89e-f1394155eb7e | -19.8853 | -57.90262 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 17859d71-8c23-3345-8381-bea297691cea | -19.87871 | -57.89561 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 22a54204-d5ac-3274-8d24-a2f5131c10d9 | -19.87085 | -57.89114 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| ee9360af-ed9b-371e-bd6a-b995a1a95a1a | -19.87392 | -57.89181 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f88be290-3076-3fd9-a659-545a6d4a5f62 | -19.8657 | -57.8905 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 3993df51-dd2b-3cf0-a21d-55cbb7baadfb | -19.88082 | -57.89561 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| dfece62b-aca0-3ddc-874a-7bbca70555ea | -19.87906 | -57.89243 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f22c70b9-86df-3875-bd31-e0f8a51dd8e6 | -19.89078 | -57.90006 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 19f08334-1c2b-3a6e-b841-4d958c63e5a5 | -19.86841 | -57.89437 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cce42453-ee0e-3827-9ad0-d8830aef1d20 | -19.86877 | -57.89118 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9f72cff0-976d-34da-bd49-6e2fe822a278 | -19.87567 | -57.89497 | 2025-09-07 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5aa8bcad-a237-3622-9e7c-7dae515de6fb | -11.3385 | -46.5645 | 2025-09-07 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| c775d0d6-4639-328f-b323-1202286c292a | -12.8055 | -48.0182 | 2025-09-07 05:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 42056a9c-0e42-3341-ba98-f188b630f213 | -12.9482 | -54.7519 | 2025-09-07 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 53e570d5-bb5b-3cfd-a57f-b125263c328a | -12.9477 | -54.793 | 2025-09-07 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f731e8af-23c0-32ae-b50e-124f3b53d874 | -12.9289 | -54.7744 | 2025-09-07 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| fca74ea3-31c3-31ad-aaf5-d162d3e29e39 | -12.7153 | -56.5632 | 2025-09-07 05:50:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fadcb8d6-50d9-3381-a76d-e7504ef286c7 | -11.3194 | -46.567 | 2025-09-07 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 10cf2554-590d-378d-b8a2-59ee6f0c4a08 | -12.967 | -54.7705 | 2025-09-07 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 924991d7-b721-3538-968a-2746c7aab806 | -12.948 | -54.7724 | 2025-09-07 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 179.7 |
| 839181d2-fd67-3f51-9d17-cd3e3adcbb1a | -6.06053 | -57.7998 | 2025-09-07 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a1fc588-2a42-3865-8670-e486c9ef2a28 | -5.78901 | -57.55843 | 2025-09-07 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0e765cd0-0525-3da5-b1a0-b6e68a80356e | -5.7898 | -57.55269 | 2025-09-07 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| feb20f47-59d7-33c9-a43b-6577ac891b96 | -6.06701 | -57.80094 | 2025-09-07 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d5d9f9-8913-3707-9f2d-19830e6c5ed9 | -5.85873 | -57.77528 | 2025-09-07 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf825bb5-dadb-3418-9019-8e66a5cf90b6 | -6.06628 | -57.80636 | 2025-09-07 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3b42b6c-b135-38be-a2e1-ad8d463dd064 | -12.9477 | -54.793 | 2025-09-07 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| eddc5adc-38c7-3785-bef7-b417285f6a61 | -12.948 | -54.7724 | 2025-09-07 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 9793f44c-abdf-3d50-a75e-33f25b3ce88c | -12.9289 | -54.7744 | 2025-09-07 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 32195296-7247-34cb-b5df-7989524b41c1 | -12.8055 | -48.0182 | 2025-09-07 06:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 527204d9-8024-36f1-852c-8926a612683a | -12.9482 | -54.7519 | 2025-09-07 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d8504cc8-e01c-3f71-a037-45fdfb49b278 | -12.7153 | -56.5632 | 2025-09-07 06:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a6630137-6ead-3dae-bbad-41a7d23c7288 | -10.1634 | -61.14099 | 2025-09-07 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6b5824b-8911-3e09-809d-70fbe429d6c6 | -14.41975 | -60.19386 | 2025-09-07 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a17f4b33-d640-3590-b894-bfc942ffafb4 | -11.78024 | -60.89752 | 2025-09-07 06:01:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46f9d5a9-7eb6-3053-b7dc-ee19482d652e | -11.78119 | -60.89706 | 2025-09-07 06:01:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0acaf83-f5a3-3495-b81e-6fed6f3a3699 | -12.41662 | -63.90697 | 2025-09-07 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6a30555-2a16-3233-ad4c-048c1f70acaf | -12.42274 | -63.89718 | 2025-09-07 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 118f1d6b-19e5-33a7-a222-9f1079b44d3e | -12.41321 | -63.89592 | 2025-09-07 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c564b5cb-c00b-3d36-8d2d-129a15161fe1 | -10.16801 | -61.14114 | 2025-09-07 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e386c393-0edf-36ca-9a36-d0544dcfedb1 | -8.9699 | -62.9603 | 2025-09-07 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 721326be-7aa8-3196-acf9-05aeff4fd30a | -10.16839 | -61.13817 | 2025-09-07 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README81.md)
