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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be945f2a-3da9-3da2-9e44-da40f5b2def5 | -20.47742 | -53.67494 | 2025-03-18 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 469a8812-3caf-385b-b596-058f4cd53544 | -20.73819 | -56.03939 | 2025-03-18 04:44:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94e13e10-049b-3379-95a8-197be2918f65 | -23.15649 | -45.78481 | 2025-03-18 04:44:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ca882c1-a088-33a2-8f3f-9fe9139828df | -20.55632 | -55.32252 | 2025-03-18 04:44:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 317d3e6b-eac2-3a53-8039-95e12a83448c | -23.59321 | -47.43923 | 2025-03-18 04:44:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f59608b-3b06-3276-b760-dd83b329b35c | -23.33914 | -46.7725 | 2025-03-18 04:44:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 426a8e55-5ede-3c30-884e-b713b012f7e9 | -21.83234 | -56.49835 | 2025-03-18 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 512090ed-cd5c-3d32-aae9-779c5a62142e | -23.59307 | -47.43719 | 2025-03-18 04:44:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9a5a8a38-987d-3ef4-88b5-78335dfa52c5 | -20.443 | -56.55864 | 2025-03-18 04:44:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 099feb53-f364-3bd3-a74b-78e060b396f5 | -29.5802 | -51.9841 | 2025-03-18 04:46:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6cf69e9b-c749-3dee-8dd8-2b2d7331fa3d | -30.42773 | -53.52071 | 2025-03-18 04:46:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 6b338e61-0c94-3410-94ea-0638c4dd3e0d | -30.42783 | -53.5223 | 2025-03-18 04:46:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| dfc089ae-d37a-3fe4-bfa4-b2c7a2c33c22 | -29.58376 | -51.98473 | 2025-03-18 04:46:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 997f130b-4e24-3ea4-9127-432aebd87d21 | -1.66131 | -55.58112 | 2025-03-18 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bf70f2d-1017-3657-91dc-f0068ae509b2 | -8.31575 | -55.11049 | 2025-03-18 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4cf8b2a2-80be-30e1-92aa-8a6e68c00b19 | -15.63074 | -57.30812 | 2025-03-18 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1dc83d51-f22c-3056-8ce4-42e9bf4b57dc | -12.84203 | -43.83155 | 2025-03-18 05:04:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2076b644-2f54-3c6e-b97a-76a1f0f420cb | -12.0713 | -45.62674 | 2025-03-18 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18bec015-35ac-3c12-b482-ab59d5480871 | -13.28536 | -54.37077 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8d969a65-d6a7-3bb8-bdbd-5a4531cd5eaf | -15.6335 | -57.31224 | 2025-03-18 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de97ef5c-4efb-3d8b-bb00-e40df2315a71 | -12.84892 | -43.83235 | 2025-03-18 05:04:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 574f1756-840b-3fd8-a3dc-e6ed6353390f | -12.89379 | -45.05146 | 2025-03-18 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c6f06a1-f22b-3d85-9999-b53e53e9b027 | -15.63682 | -57.31279 | 2025-03-18 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56b9b6ac-1014-374a-9fa3-90e540c395aa | -13.30011 | -54.36327 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d267a986-ba32-3c79-928c-a78faca31af8 | -13.29013 | -54.36311 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 41b906ed-73cc-3f06-a70b-15502478835a | -10.31918 | -59.07526 | 2025-03-18 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dad051c5-6a8a-3048-82f8-00b0259e9201 | -13.29186 | -54.37596 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f6c8453-d1be-3e87-ae69-fcf88fc1b019 | -12.0778 | -45.62458 | 2025-03-18 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5f2d14a-b8ce-38ef-8200-32af3996677f | -13.2943 | -54.35954 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c60e80ed-4399-3ce8-82dd-fb6f74b58f1c | -12.55744 | -57.71305 | 2025-03-18 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64bbc673-be00-35b3-9a93-e89da2bb31bd | -14.89793 | -56.64777 | 2025-03-18 05:04:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e5518be-f1ad-30a1-8750-3641456c22fa | -11.96668 | -48.09126 | 2025-03-18 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bc90e54-d275-3168-b5f4-fc92c9471353 | -13.29663 | -54.36831 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8d2cc87f-c19d-3c90-a891-95a6f39024b6 | -13.29123 | -54.37448 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cd05d2d-a7d9-3863-af5c-efe7120b02f2 | -12.89234 | -45.04869 | 2025-03-18 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb6cb707-3626-3a95-a380-a900f88ad1da | -10.32202 | -59.07977 | 2025-03-18 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff97068c-9f89-359f-a50e-214fc29cbae4 | -12.89437 | -45.04611 | 2025-03-18 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8aa51992-bc7a-3c5b-9588-1f4d08f984ea | -13.2924 | -54.36627 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 09e98138-3d4d-3f7e-826c-b6b8bd820a3d | -15.80711 | -58.51595 | 2025-03-18 05:04:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3c534f66-e48d-308e-8589-29e1e181f63d | -13.29369 | -54.36366 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9cb8ca60-946d-37bc-b7df-0fd247eac72a | -14.12184 | -47.68168 | 2025-03-18 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43232be1-4cd3-3d1e-9e9a-a9a3afc7a53c | -14.1214 | -47.68543 | 2025-03-18 05:04:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 176c67c0-ffb0-3cd2-ba12-dea9c97ec833 | -15.07975 | -48.94558 | 2025-03-18 05:04:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74ea4648-60f1-3f76-8583-e09504d24fff | -13.29714 | -54.35859 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5af8bcdd-7fe0-3963-86a9-069c7cb01e0e | -13.30307 | -54.36794 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4335a0b8-b01f-3eec-a1f5-a918935e85b5 | -15.78799 | -59.1819 | 2025-03-18 05:04:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b7ced528-9120-39c5-998e-2ec354c3bb80 | -13.29603 | -54.3724 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8a3b8cb-a95c-35de-b0f7-fa5cda2d8760 | -13.29724 | -54.36421 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6550878d-f900-3333-9060-dd1fe1d08b97 | -13.29478 | -54.37504 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 686b49ab-edb3-3e81-9bfa-fdc9de28de4d | -12.07726 | -45.62937 | 2025-03-18 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9174549-6790-3bef-956d-e4e81d3596c7 | -13.29247 | -54.37185 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 705984b4-5ba9-3e08-8c1b-d87e2cdef101 | -13.28597 | -54.36666 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6624f0a1-fa0f-3f38-adb0-37817fb95720 | -16.09874 | -60.04671 | 2025-03-18 05:04:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d79cb15-cde9-3132-b9c0-86c551a2aa80 | -13.29182 | -54.37037 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f133b0e7-359f-38bd-a27d-26cae19fc8a8 | -13.29655 | -54.36271 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1fe0f9a6-6ff2-35a4-88bf-1e340d965b6f | -13.28475 | -54.37486 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3c184320-e7d0-375d-a924-c4eabd6204fe | -13.28952 | -54.3672 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e7bd67d6-d1bf-3a35-b2ba-765e1f7d8a61 | -12.07742 | -45.62749 | 2025-03-18 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb2d083d-9a6e-3754-a114-0cec38c8aa2a | -13.29308 | -54.36775 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6fc83bb7-0c3c-31fd-b7cd-e229eb977b5d | -13.29537 | -54.37092 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87e7ce5-5e06-36b1-8bf3-835ec86e390f | -13.29952 | -54.36738 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01618b1c-05d1-39e6-8971-9a80d7ecb9da | -15.58261 | -56.01595 | 2025-03-18 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1ea64f5-1b7b-3a27-a23f-d5c5ee80f30d | -14.8946 | -56.64721 | 2025-03-18 05:04:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 272f5cb6-47fc-31c3-880a-bcc64c239ccd | -12.07685 | -45.63226 | 2025-03-18 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb411570-d9cb-3b65-baad-bf768d34cf21 | -13.29299 | -54.36216 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| e1ab6c3b-5441-37f5-8cec-65d32f83a73d | -11.96146 | -48.09071 | 2025-03-18 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b723e3d-b069-3170-89c2-e1c8a96d87ef | -13.29785 | -54.3601 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d33dd22-0c2d-3d10-9b0f-cacdbbefb569 | -15.71976 | -56.17236 | 2025-03-18 05:04:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efaf37c5-8e99-3886-ae83-7f0dbf970fcc | -13.29596 | -54.36682 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 36505412-d1e6-3a66-b24a-daed87be1e47 | -13.28892 | -54.3713 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6958d0b8-a8d3-3fa1-a6cb-eed720689cf5 | -13.28831 | -54.3754 | 2025-03-18 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 21955c20-159c-3e0d-9b37-d6cb4210d97e | -12.55412 | -57.7125 | 2025-03-18 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95f07965-1937-3cea-8341-79708d7399cc | -24.24208 | -50.7385 | 2025-03-18 05:06:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6263f912-68f1-3e81-9b6e-2e692863afef | -21.35112 | -57.65291 | 2025-03-18 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e03d9a04-fe1e-3888-abd8-65bf66b823b8 | -20.44234 | -56.55844 | 2025-03-18 05:06:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfcc4db1-4cb6-32d9-977c-0c5c3e140e22 | -20.56224 | -55.31433 | 2025-03-18 05:06:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7a979e6-2c63-3b92-a7ce-576e1153779c | -20.73557 | -56.04174 | 2025-03-18 05:06:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f07d3f76-825b-3944-bbcd-71c234a3ebd3 | -17.76219 | -56.31672 | 2025-03-18 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 59921a15-0266-3d25-8a1d-f217626f9606 | -20.55733 | -55.32291 | 2025-03-18 05:06:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 243a3dcd-0d85-3891-93a2-d560c46060a3 | -17.65168 | -56.47296 | 2025-03-18 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 86107c60-21ab-35bf-ba19-da1e7c81fae2 | -20.73699 | -56.03888 | 2025-03-18 05:06:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61b25eb7-d06d-3b18-86e1-a9a9c91b4815 | -17.75933 | -56.31229 | 2025-03-18 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3994ed84-2eb0-33f6-af7f-45d684a734dc | -18.41189 | -55.57605 | 2025-03-18 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f50f23a6-90e4-33c6-aecc-a1cf80832f1d | -20.55794 | -55.31835 | 2025-03-18 05:06:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1911e2d-e9a6-3c48-aeb2-1e40a9329998 | -20.47794 | -53.67529 | 2025-03-18 05:06:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bd831bf-5941-3cab-9ec5-dc6988d3dcce | -17.75876 | -56.31618 | 2025-03-18 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9c7a5d25-fca3-35b4-b252-d700723d28eb | -10.31943 | -59.07656 | 2025-03-18 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b351c37-7762-3481-8d2f-b1e512c528a0 | -9.4621 | -36.94915 | 2025-03-18 11:47:00 | TERRA_M-M | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 11.0 |
| f77ab518-a2c5-3f22-816b-749ced724188 | -9.35779 | -38.02526 | 2025-03-18 11:47:00 | TERRA_M-M | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 64e19d5b-7bc4-3e7a-99ef-ffe6275f5762 | -10.80999 | -37.26067 | 2025-03-18 11:47:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 784c2411-8ff7-3e69-8282-33dac47022d9 | -10.76322 | -37.20046 | 2025-03-18 11:47:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 63d29f06-8147-33cc-8cb8-28bef17685b1 | -10.30313 | -38.17378 | 2025-03-18 11:47:00 | TERRA_M-M | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 006e8022-6217-378c-8afa-5bdd05cbc724 | -9.35931 | -38.01509 | 2025-03-18 11:47:00 | TERRA_M-M | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f9d08d2c-e92f-3ad7-a289-316cc859095a | -8.07562 | -37.46443 | 2025-03-18 11:47:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 22.3 |
| a114b434-7401-3497-a962-2346f23a4249 | -9.29766 | -36.68159 | 2025-03-18 11:47:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 17.3 |
| d7e05137-a2ad-3b8e-ad03-46d430256155 | -9.92867 | -37.53461 | 2025-03-18 11:47:00 | TERRA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 7138bad4-339d-3221-8d75-02aaded0e97e | -8.8458 | -36.87115 | 2025-03-18 11:47:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 3ff186ac-1fdb-3373-baff-06833a7d2283 | -12.547 | -45.342 | 2025-03-18 12:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 054a6e3b-19bf-33c0-8e8f-7650c3afcc87 | -12.547 | -45.342 | 2025-03-18 12:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ef1bc4ef-efe2-33f9-9336-3bb035728902 | -12.547 | -45.342 | 2025-03-18 12:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |


[Clique aqui para ver as próximas entradas](README4.md)
