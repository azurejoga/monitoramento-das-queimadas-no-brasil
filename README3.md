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
| d708d665-ce2a-3f41-a549-a9259e3761f3 | -9.32961 | -46.10275 | 2025-10-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7a17a92c-641f-3708-9808-1a04f232945a | -13.37249 | -47.75444 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 609d566f-c07e-3131-80b5-109d2e4be22a | -11.64347 | -47.52771 | 2025-10-10 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b46d336f-2514-343c-ac7a-67e32b3b302b | -8.60516 | -41.41413 | 2025-10-10 00:33:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 31a51164-cded-3c9f-9116-244b84cb0a58 | -16.8845 | -49.73589 | 2025-10-10 00:33:00 | TERRA_M-M | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6360581a-0d66-3b61-bade-37a7a481307b | -15.90614 | -43.28831 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a8cdb28e-8e4b-3755-baf7-06731ede2e65 | -14.88091 | -48.21545 | 2025-10-10 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 325e35dc-8ef4-3618-88a8-1e9ae0f71ffb | -14.87328 | -48.22578 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| be882ca3-54ba-3200-92a4-f0d367055fdd | -10.16104 | -44.59357 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 926bc026-281b-3ad4-a879-1f63d6aea32f | -15.40131 | -48.04613 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6268d99a-340b-35f8-81f2-ad93a86ab221 | -11.92623 | -41.5343 | 2025-10-10 00:33:00 | TERRA_M-M | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| b756b77f-e485-3e51-b9f3-382767535e47 | -15.47569 | -47.98206 | 2025-10-10 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7b1c1502-b594-3cc9-8668-f5ec9c82fec8 | -9.5448 | -46.318 | 2025-10-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 824bc1ea-df46-3e35-a5b3-f34957b0355d | -14.93876 | -46.77377 | 2025-10-10 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 87b43474-c46e-30b5-b33d-9a39fca0797c | -14.88464 | -48.24284 | 2025-10-10 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e41a4c3f-1faf-3477-8373-6a016a9bb6d8 | -12.43017 | -45.76743 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d5ebb9b7-badf-36d0-85fe-165f6cff62ed | -10.16755 | -44.5652 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6cbb6b0b-594f-3139-a621-ecf233b9721e | -13.30692 | -47.75198 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 33a68f23-b74e-306d-80d1-0f4a57d5b91c | -15.92358 | -43.29378 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 17c3d368-0079-3963-8e13-15e713e20e7b | -13.28653 | -48.00904 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5af0add3-7341-3061-9d55-dad8a2949be5 | -14.56402 | -43.52193 | 2025-10-10 00:33:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e71b6727-286c-3201-a5a2-cd445ff91cff | -15.81751 | -43.78462 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e2b1cac2-3cbd-3ced-a380-01990ef694de | -13.3855 | -44.224 | 2025-10-10 00:33:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 777ceb95-d048-31d3-9724-bc5ceea6a3e7 | -17.04886 | -49.23568 | 2025-10-10 00:33:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fc158db8-d8c4-3d89-add2-9d3c54cb5979 | -13.4216 | -47.65504 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8ab91547-3a5a-3fb6-a46f-586bc9ae4bf8 | -14.94766 | -46.77244 | 2025-10-10 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b107d14d-5da6-3955-9a30-097fd039a65c | -15.82374 | -43.758 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| db4def98-a645-3bd6-9206-b833d5e8b085 | -16.27666 | -47.17626 | 2025-10-10 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a86fbcf8-8189-3068-b0a9-cd7c7ea8ff33 | -10.1715 | -44.59131 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 005a0334-3bc3-31eb-801d-894762cc62c8 | -13.31573 | -47.75067 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0c378849-df08-3859-ad22-5d966471133f | -14.45066 | -50.32387 | 2025-10-10 00:33:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 01473882-8c50-3efe-bd43-6a7e66413c92 | -13.38405 | -44.23072 | 2025-10-10 00:33:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e49696af-c52f-3218-932b-df4b693bf575 | -13.36703 | -50.46974 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8b1590f8-c2b5-3534-9ad1-c7d2d5ae27b1 | -15.42265 | -47.98987 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ff74d428-0fec-3a89-aa13-0ee19ae46d0e | -13.27016 | -48.02065 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7bb53f16-b58b-32fe-81be-3234aa23a29b | -15.43149 | -47.98859 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7250fabe-8819-3815-b590-87d8643fdcf6 | -14.86013 | -48.46193 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8124d964-fa6d-3d45-a44b-330c4945df91 | -15.37228 | -48.03175 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1762918f-9ddf-33aa-b800-31b9be48c96e | -10.16957 | -44.57853 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 25324589-bbbf-3cbf-85aa-e42c1ef827e7 | -11.83147 | -47.0951 | 2025-10-10 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 528670ab-5345-356b-a6f5-b5a75fc665f0 | -16.73143 | -49.8238 | 2025-10-10 00:33:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 62d62c03-47df-38b0-8836-d53125e13a7c | -14.93744 | -46.76443 | 2025-10-10 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7b2acc29-1302-31a3-bdc3-3da53e0088fc | -15.09767 | -46.59461 | 2025-10-10 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 387523d9-53be-3d4d-8180-b4aa3db17d73 | -16.17544 | -42.86512 | 2025-10-10 00:33:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dcda285a-6f2e-39ed-8605-baa438463c4e | -15.39498 | -48.06578 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2d5c5939-04fb-398b-90d9-52f6dd08e71d | -15.742 | -43.95565 | 2025-10-10 00:33:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d4d3a778-b2e3-32c8-9c9f-7c86fb654cab | -14.89324 | -48.22601 | 2025-10-10 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0c43ef2-971b-3f6f-be22-15c75aa09b55 | -13.84427 | -45.83976 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 52eeb5a6-ae38-31ed-ae60-fd19b3f77cc4 | -11.6809 | -47.52509 | 2025-10-10 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| adb2962f-b503-3c1f-8877-c1c43d4bcaf3 | -13.29554 | -47.14432 | 2025-10-10 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88e2bb7d-784b-3e4d-a0b6-bb2bd2a8ffd2 | -9.33115 | -46.11348 | 2025-10-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f6bd7786-ec69-31c5-aec9-1a02c004fa53 | -13.29815 | -48.48598 | 2025-10-10 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61a65152-9bdc-39cc-85f4-2943b67fe242 | -10.62018 | -46.62952 | 2025-10-10 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75f74ea4-cd89-30ae-85ad-cba5929a9f8f | -13.33336 | -47.74803 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d46b15ef-0776-3f32-8bdd-5a38f23ce269 | -11.68218 | -47.53416 | 2025-10-10 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db34ef62-58ea-39db-8e9d-f2e6ccf27a1f | -15.08742 | -46.58671 | 2025-10-10 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ab9f4e03-3160-3a32-aff2-7e255923cff0 | -14.88215 | -48.22456 | 2025-10-10 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| da614af5-8574-3e66-9385-7659f1046d92 | -14.84113 | -48.45544 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| fe6d2634-78c8-3819-8f75-74009f7560da | -14.43023 | -48.00951 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a6ff06dc-2864-3ced-87e3-3b71fe8858e3 | -13.06631 | -43.83729 | 2025-10-10 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 6f21501e-960c-3ae5-9196-459e291c41ea | -13.51562 | -48.12271 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8ba3b8c-07c0-3361-af70-0edeeaee206c | -16.74096 | -49.82241 | 2025-10-10 00:33:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 80f4c2c6-748d-3a7d-be58-ae55a328fb60 | -10.16298 | -44.60629 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| a1a273d0-0466-36d5-9506-f13d15d4ef97 | -10.1926 | -44.58784 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5262e990-c058-348e-9195-5454bedf7dbd | -14.42774 | -47.99138 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| da53e81d-6ff7-303e-a3f0-2ab5a73119bf | -12.62061 | -45.06313 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bea10796-5714-3337-ba44-33fc2c1e6864 | -16.7328 | -49.83452 | 2025-10-10 00:33:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0339ddd3-cfcb-3a08-a367-a1069781cd96 | -13.46568 | -47.63342 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1d228c70-e178-3644-a580-e43c151538a1 | -15.39373 | -48.05663 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 031b94d5-38e4-3444-b66e-718b58e706c9 | -13.3319 | -47.99643 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0875c527-7760-34ee-8f2e-71ae59bed412 | -14.01564 | -48.14721 | 2025-10-10 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 51bb342e-8cc3-327e-8f3a-95178bce8fa2 | -13.3813 | -47.75312 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| c70df5f0-6742-300d-8a69-eceafb11a4e9 | -14.41974 | -48.34189 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5c1e1160-bd5c-3231-977c-a51ae7624c84 | -8.59685 | -41.39595 | 2025-10-10 00:33:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| df1b70b5-2ec6-3048-8435-f14456ca20fc | -10.16557 | -44.55219 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 2fed1de6-1708-306d-9825-2c27a7b7cb9e | -14.88339 | -48.23366 | 2025-10-10 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8cfb0af4-e3e7-3612-89ec-293e9c302ba2 | -13.8413 | -45.81971 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 49b2efbd-6387-3b50-93eb-35a50e72a6d6 | -14.42899 | -48.00046 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| b01b3241-1cca-3851-bd21-d29403b01103 | -13.32455 | -47.74935 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4834e339-f508-3cef-b340-48b67daaaf0a | -13.27141 | -48.02965 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 458cb3c1-4916-3c22-a531-6d8766a59938 | -15.38112 | -48.03041 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| da8de29f-4b72-3f3f-9769-2107ac58f9a8 | -15.39881 | -48.02782 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| bc8a78b9-d7c2-3b46-a210-fc0004b7919e | -15.19563 | -56.77618 | 2025-10-10 00:33:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 26568614-7cf9-36b5-8b12-56da1931d3f0 | -15.91674 | -43.28702 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 337.9 |
| cca63e36-43c8-3a00-a3fe-0b7fec2a059b | -15.45891 | -48.53722 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 56a9fde7-370a-3723-835e-15f924dc60ee | -15.00821 | -46.29114 | 2025-10-10 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 696002d2-af8e-37e5-9bd8-bbf3ab291501 | -12.68964 | -47.6928 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eb0cb33e-3a41-3c82-869f-7ae6fa91b73b | -13.35487 | -47.75708 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d44bafc8-c687-3778-b319-5c66b0e7b1c7 | -15.52091 | -47.96946 | 2025-10-10 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9efe3926-27c4-380a-9374-89488a4779d8 | -14.72795 | -48.36537 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a56d869-b389-3d58-a837-b2260efef26b | -13.38255 | -47.76211 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5aa40c29-fa47-36cd-8340-a0e7406495e4 | -12.44116 | -45.77629 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 91399c0e-44cc-3c5d-87e6-ae3a21b4af05 | -16.6672 | -47.5968 | 2025-10-10 00:33:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24dca712-d08e-3876-9568-1ff59b3c38a2 | -14.92984 | -46.77486 | 2025-10-10 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9f14e13d-6316-3bf4-9669-5c650517c897 | -15.82768 | -43.78284 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 33.1 |
| f55b132a-d0ee-3bb6-b00a-4586d3949634 | -15.90819 | -43.3014 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 123.7 |
| c490e08b-d2fc-38d8-9616-89cd6dfc8414 | -15.3281 | -43.2015 | 2025-10-10 00:33:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.5 |
| e61c5c1a-b5b8-3c82-99dc-88d6721a872d | -13.84279 | -45.82977 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d7d5ade8-5a8c-3be7-9d36-f1ee9de6276d | -12.36654 | -47.22357 | 2025-10-10 00:33:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9508c2b9-f9ff-325c-b119-5082e29f08b2 | -13.35984 | -47.5997 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README4.md)
