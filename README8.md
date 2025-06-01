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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9031da5e-42e8-3df0-9e67-b55775d29bc7 | -11.42865 | -55.00038 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e02a008-ae95-379b-8d55-d338849209c2 | -13.09335 | -45.26861 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4559cc4-67c2-3e38-a12d-833295a1d77d | -16.68079 | -43.88355 | 2025-06-01 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c066fb9-ac7e-3043-906b-4fe9569cd4c3 | -14.69239 | -45.10646 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f7d38d5-4c0e-3bb5-adae-56786d85ef3d | -13.10168 | -45.26495 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40771149-f354-33ba-bf49-8ea220306c0e | -12.01701 | -49.52332 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1483a0ca-f701-3430-bce4-41557a782762 | -11.90751 | -47.4441 | 2025-06-01 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 955d275a-0355-3c2b-81f5-171c10e865f4 | -14.68291 | -52.69127 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcf55857-a6b9-38ff-aa1d-237f0d438e61 | -10.7625 | -48.56224 | 2025-06-01 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc2f9d7f-f7ed-3b50-a600-fb6553a948d9 | -10.13878 | -50.69229 | 2025-06-01 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ca056bca-7621-38c3-9034-b000bcece82d | -10.65289 | -49.42858 | 2025-06-01 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1feb7d4-ca8d-3529-86ab-fd1544523e3e | -11.14435 | -53.94035 | 2025-06-01 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68b4983b-3e51-35b0-80ae-a00a9eb9af54 | -13.90744 | -54.66671 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d317f8ee-249f-31cc-b0df-922b26965092 | -12.90616 | -55.04205 | 2025-06-01 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 218f6bc9-e051-3e12-b338-85942b2ba070 | -14.68785 | -52.68367 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08187c5e-68b0-3cb9-8891-706666ef5f3f | -14.37128 | -48.82277 | 2025-06-01 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ff5852f-4a67-307b-b4bf-9a43bbc6daec | -10.73287 | -49.28192 | 2025-06-01 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8df6a183-7e18-32d5-b65c-ec675f3c5699 | -14.68242 | -45.12072 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4686e195-cd5b-30c7-ae11-6d2a99486b9d | -12.52356 | -57.19355 | 2025-06-01 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51acf5bc-1fda-3ce2-acd5-777bed0b5f27 | -11.44074 | -55.00667 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9fa0dc0-b5a6-31a8-8dc2-521f460bfe7c | -13.95194 | -54.48951 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52691e3f-ddaf-37be-831b-12c768873433 | -14.65503 | -45.40995 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c67129d-dfa9-3836-9746-573000c5691e | -14.65048 | -45.41431 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25c115a0-e63b-33f9-b5c9-d14e0fdfeee4 | -14.64661 | -45.41372 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f1ef063-9e03-3f08-abd2-2353ef10ad21 | -13.63697 | -52.18411 | 2025-06-01 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 098454a6-642f-3180-b5c8-e3dbfe9f49b7 | -11.43148 | -55.00922 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb5a44cd-5455-32d8-b982-868a97d9e14a | -13.64049 | -52.18471 | 2025-06-01 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1b3a204-3df2-3b3c-a831-fc4788d0be80 | -17.09518 | -43.8054 | 2025-06-01 04:36:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f80fc97-6216-3105-9b48-895015fc8d1d | -10.07428 | -52.75402 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 074275e2-90c6-3ed8-8eec-54658605bbeb | -14.68429 | -52.68304 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eea582b8-38ff-37f8-b796-317fe601bac4 | -11.45284 | -55.013 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c15f00b0-afb1-3ca9-8954-589ba82ae5cb | -16.02918 | -43.68042 | 2025-06-01 04:36:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4207f3ca-a263-348e-a81e-3c7557339937 | -10.65567 | -49.43265 | 2025-06-01 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4137087-f940-33a8-b14b-1acf4bd7c008 | -11.44927 | -55.00821 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56af1a5c-f2d3-3c7a-b61b-7418d580369f | -14.60528 | -47.96513 | 2025-06-01 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a0a7e71-9783-3da8-be1d-380e2484dee7 | -12.02034 | -49.52387 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16c29a42-84f4-3d2b-8def-1331ef67ad88 | -10.51583 | -53.65572 | 2025-06-01 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7259643d-1f08-3a44-9a3d-93efb8902ebb | -16.34875 | -43.69732 | 2025-06-01 04:36:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06cb74d8-8e17-3d87-b448-26ec21d41611 | -9.92786 | -59.9034 | 2025-06-01 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9f2d8b3d-f580-352b-8500-2b532a521529 | -10.1403 | -52.14001 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54d672ae-cc03-3122-8ef3-f1f4d72fe27c | -13.09269 | -52.04816 | 2025-06-01 04:36:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecfe0b96-5c41-3408-9af1-c3fa0721f83d | -10.63062 | -49.43946 | 2025-06-01 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f102842-7d53-3322-9c80-2c0a04e44df8 | -11.57837 | -47.45578 | 2025-06-01 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d122d97-8583-3f56-8297-0db971558cd6 | -11.07454 | -54.77741 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc0bf38c-a1e7-3740-9613-c3a2301f62ca | -14.68489 | -52.69015 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c471a1e3-f61f-3d1f-b3d6-945928955b3e | -14.69055 | -45.09034 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a010f3b-1f47-30c4-9dd7-e1893ae5301f | -11.57552 | -47.45149 | 2025-06-01 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5e74b10-d77d-3529-91e2-6875600dd8c2 | -11.43576 | -55.00996 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0401ebba-c11c-3e25-b686-c3c1b2774bb8 | -10.29695 | -57.14194 | 2025-06-01 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 854b37c7-6f82-3f69-8332-20a53786a601 | -14.0176 | -55.12333 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c868b5-2800-3886-b51a-b1d3f9c34c34 | -11.07522 | -54.77348 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4239531-7e85-3ebe-9a03-4a11de316e13 | -14.67452 | -45.11963 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f71640ef-3be7-3c52-b04c-dbc9a9e35de6 | -11.0759 | -54.76955 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb6429c4-1c8a-3d69-86e7-b4c954b866ff | -11.44501 | -55.00744 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee6fa1b8-c772-3e79-bba1-3b6260946ecc | -10.14103 | -52.13571 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43728ff3-beed-3dd7-8f7e-b364191da954 | -10.1447 | -52.13632 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbad4ef1-2afc-32f3-9030-ab75f7a33da0 | -11.90694 | -47.44783 | 2025-06-01 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6713d0a-05d5-3a03-8976-239118a9aa20 | -11.80071 | -41.19646 | 2025-06-01 04:36:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9c1df30e-f6bf-3504-9a07-a5aa8f7d6bea | -12.02756 | -49.52143 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0c48f73-bca5-3cf4-81c0-419b58173f98 | -11.71226 | -56.45427 | 2025-06-01 04:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b39622fc-f13c-3b47-981c-760f6a32c498 | -10.61527 | -57.61106 | 2025-06-01 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15423663-7ea9-307e-a9b4-37ffcd5c6ab3 | -14.57427 | -58.75235 | 2025-06-01 04:36:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ae76a4d-93fe-3e29-979c-9a9808420598 | -14.691 | -45.11677 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1a5440b-1903-38d2-bdf6-c1eb077fb174 | -11.83117 | -47.28312 | 2025-06-01 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36180d42-34ae-374f-9f7b-331c7f324df1 | -11.57621 | -47.62952 | 2025-06-01 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af20cb6c-79dc-36c4-a269-70e8ca606dd1 | -12.52839 | -57.19451 | 2025-06-01 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1c27ed7-8551-39c1-9a78-dd27bbeb45ee | -11.08013 | -54.7703 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11a9e7ce-77b1-3878-af8b-12a0a2e2273a | -14.02796 | -55.13684 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9bae99c2-f092-3336-a185-b9e5517e45a7 | -11.91402 | -54.4165 | 2025-06-01 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0782da44-0d73-3ef6-9958-654c5f3a186a | -11.14222 | -53.92904 | 2025-06-01 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b33e815-2c25-3031-a111-474539c19d12 | -12.08445 | -54.58014 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ccf52f9-57c3-3a6b-86fa-d03c1a7f42cb | -11.80143 | -41.19083 | 2025-06-01 04:36:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e91109d8-86dc-38ce-9671-3b6e8bbfdf2a | -10.61013 | -57.61003 | 2025-06-01 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c3ae75d1-218a-31fd-a682-efc2120c408e | -12.12418 | -54.59498 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f520b8e0-afad-31bd-9971-49709671190b | -13.09717 | -45.26918 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f552f9c6-ad87-3298-9ebf-5eb4064e508d | -11.4322 | -55.00517 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f841121c-8326-3711-ad61-12ec6521590e | -13.71254 | -45.25826 | 2025-06-01 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70ca535c-f90f-3b98-8b87-6909ea3e3aad | -11.8274 | -51.2758 | 2025-06-01 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd18550c-f086-3733-948f-8348a8ed038c | -13.09267 | -45.27339 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 459d58b9-8431-30e9-a010-b3a9affaca79 | -13.91207 | -54.66403 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b70809c4-3ec4-356f-b549-7e5e8fbc81ac | -11.90637 | -47.45156 | 2025-06-01 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87ca92cc-91bb-3299-ace4-fa37139816ef | -10.19611 | -52.64925 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3911bf6c-2063-32e7-a727-234e0c26a96b | -11.91337 | -54.42011 | 2025-06-01 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63635e3e-fd24-3c83-a475-6ea66a9a250e | -11.45424 | -55.00497 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043dab75-76a9-3de8-b03f-358c2abdb169 | -14.6856 | -52.68604 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4fc904a-00d5-3a28-bc99-967e0cfa1603 | -12.53142 | -57.17838 | 2025-06-01 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0194e594-2473-3e58-a9f5-81a190dec0f7 | -14.0245 | -55.13233 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdd290cb-4c2a-38b8-9b26-3d4876e18dbc | -12.7187 | -54.97691 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e44507a5-f899-3436-84ad-1e42705b6314 | -10.82555 | -56.95062 | 2025-06-01 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f518c07-8805-34b2-a2a8-95707fb7fe39 | -14.82273 | -48.09581 | 2025-06-01 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7299e29-31a3-376c-9e39-cc104a1003d5 | -9.92695 | -59.90803 | 2025-06-01 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9fdf2ae3-049e-366e-9bfd-cc5d232c227a | -11.08215 | -54.77713 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a563981-c812-30cc-a1cd-eaf75d07653a | -12.03145 | -49.51844 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01a6acde-d047-3891-a70d-9a9fc3c9e8c0 | -9.92622 | -59.90868 | 2025-06-01 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0914fac6-af52-3ec3-8de4-1b8cbd1b5ab5 | -10.72645 | -47.89896 | 2025-06-01 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68d3e9fc-ebf1-3e41-8b5f-dc403be49935 | -12.09431 | -54.66695 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26d05e2f-edaf-3478-94c0-b678c666bd87 | -14.68705 | -45.11621 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 061da38f-3a4f-35e2-a050-c46153175d53 | -13.10337 | -52.28807 | 2025-06-01 04:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39b45e0e-fb5f-3409-ae5e-52159854a4ee | -11.57438 | -47.45901 | 2025-06-01 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bee81965-b20a-362c-b40a-8e4b6d17c84f | -12.72007 | -54.96925 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README9.md)
