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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d97a06f-eae1-3c4d-9382-314a0e0f22a6 | -22.60933 | -49.01959 | 2025-09-24 04:55:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0aab139-72f4-3ea3-a1ea-bcfac5d0d14a | -21.00498 | -47.37954 | 2025-09-24 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40714a5a-395a-3365-b73b-1b9c7c0cf375 | -22.37475 | -49.48892 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ca8c0257-7b60-34b2-a14e-4660a6e707cd | -22.37794 | -49.48691 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a41f6884-bd3e-389f-b9c7-ca82bdbf13a5 | -17.95031 | -55.85657 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 84245fcd-ab47-3096-9573-aa67937fe726 | -21.00424 | -47.38649 | 2025-09-24 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69b0a255-672b-3a0e-9d90-6f1476994dc4 | -21.28688 | -55.9051 | 2025-09-24 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44221ff0-fddd-357d-8c23-b5861a362f60 | -17.947 | -55.856 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9ccc062e-6110-3ce6-a8bb-f1a6aca08976 | -23.01427 | -54.86629 | 2025-09-24 04:55:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7dd826c-d068-3d01-8792-777ea954ca22 | -18.53127 | -46.04777 | 2025-09-24 04:55:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 814db82c-2878-31eb-bfb4-7a58ba124fd5 | -20.61194 | -56.71284 | 2025-09-24 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f867356d-d468-3dc1-9a4d-260a161277f5 | -22.61043 | -49.00961 | 2025-09-24 04:55:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1c57f4ff-e1da-34f7-a79d-c89041acafa7 | -20.70941 | -56.7416 | 2025-09-24 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dd23e0f-0b16-3eb8-ba39-7c789d19d63d | -18.5309 | -46.05124 | 2025-09-24 04:55:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ce91065-08ae-35f1-a1bd-3eef960558c5 | -19.04725 | -53.10057 | 2025-09-24 04:55:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc961ee2-1174-3e51-84fe-ccd144e2475a | -23.37025 | -51.40334 | 2025-09-24 04:55:00 | NOAA-21 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0988925f-b9a3-35a9-a01a-26544c5ea718 | -22.37844 | -49.48227 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 911cc9a1-6791-32c4-b238-43dcf5d732b5 | -21.0039 | -47.38415 | 2025-09-24 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dc2790f4-58f5-3be4-827c-6900f2a37e8e | -17.95015 | -55.87886 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5d1e3777-7ee6-3060-825c-8e59a51d8400 | -17.94973 | -55.86019 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| daad614c-17bc-349d-858a-9f2263ae376e | -20.79704 | -56.95973 | 2025-09-24 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46776506-4ed1-33df-935c-50886812695e | -23.57484 | -50.8306 | 2025-09-24 04:55:00 | NOAA-21 | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d8d5886a-be54-3555-8403-55e7e2a578e5 | -20.08592 | -54.62081 | 2025-09-24 04:55:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff61d0d4-c289-3b48-9376-5e992c6bd3cc | -19.01567 | -51.40768 | 2025-09-24 04:55:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a64bb8a4-71db-33a7-93a5-315c1de199f3 | -22.3742 | -49.49371 | 2025-09-24 04:55:00 | NOAA-21 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7720b09-e2ba-3290-9446-ca2333fd7195 | -20.61526 | -56.71344 | 2025-09-24 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e417117a-683c-340a-ba80-1bae97036027 | -21.84398 | -50.56956 | 2025-09-24 04:55:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3ce1830e-433a-3940-b74d-fdcc02eac412 | -22.61396 | -49.02015 | 2025-09-24 04:55:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d93a1e50-a3c6-3aae-b402-bc01b929bad6 | -22.37894 | -49.47767 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5daee8e0-768e-389a-8c68-e498eec2db8e | -22.6145 | -49.01524 | 2025-09-24 04:55:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8b9d6c2c-180d-3614-af45-7f5813480393 | -17.95304 | -55.86076 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a13cda01-a1d8-3f0e-832d-5ff1d039ec65 | -17.94684 | -55.87829 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 0d7410e3-a4b7-3a66-98c8-0ee3ba4459dc | -17.95634 | -55.86133 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b4e9567f-3a2a-3069-9f09-eb161a8d0ee1 | -20.70882 | -56.74527 | 2025-09-24 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56b6774c-4bfc-3458-9c41-b374b4c46794 | -22.37921 | -49.48949 | 2025-09-24 04:55:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8387a227-699f-36c5-b068-006516f6cdcd | -23.01483 | -54.86237 | 2025-09-24 04:55:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7098e186-767b-3cb5-a59b-28fb682bdd95 | -17.95361 | -55.85714 | 2025-09-24 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c2c4eecb-9999-3012-adc4-7f9445bd0266 | -19.73798 | -54.4219 | 2025-09-24 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c002a4a-9b38-3f6e-9a0a-5f4effd642c1 | -28.38394 | -49.28415 | 2025-09-24 04:57:00 | NOAA-21 | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7dd479c4-0283-3b1f-8b12-8c446649e9e5 | -28.38195 | -49.28305 | 2025-09-24 04:57:00 | NOAA-21 | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d08a3591-b8db-3843-ad02-84754c9855ce | 3.98044 | -60.04873 | 2025-09-24 05:38:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f4cc5fd-360d-3f28-9864-1d6eb02cd770 | 0.94087 | -51.19625 | 2025-09-24 05:38:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03d1dfa3-a8cd-321b-971e-aa553da5b4ca | 0.93519 | -51.20294 | 2025-09-24 05:38:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e30bb42a-e064-3594-b83f-fdcd63624a2f | 3.98387 | -59.71464 | 2025-09-24 05:38:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc075bc3-b838-3eac-b2a9-fb433ff05f30 | 4.31726 | -60.73257 | 2025-09-24 05:38:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd73be52-4912-3566-900c-b607060190d1 | 0.94744 | -51.19521 | 2025-09-24 05:38:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fdab4ad-7bfc-34de-b694-7837ada02b76 | 3.97888 | -59.70674 | 2025-09-24 05:38:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c001af84-218a-3680-a784-7207cb0e4758 | 4.54991 | -60.30294 | 2025-09-24 05:38:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b35d955b-8d80-3d01-ab26-1509fec9b3b1 | 3.98093 | -59.71936 | 2025-09-24 05:38:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f033b417-ac81-3410-a7d8-779098d8328f | 4.23646 | -60.62493 | 2025-09-24 05:38:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 908826ad-4759-3505-b994-5a74139efe02 | 0.94013 | -51.19957 | 2025-09-24 05:38:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e2fc108-72f8-3ce4-9427-8f8b7806c143 | 0.93451 | -51.20626 | 2025-09-24 05:38:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c79d571-fa25-333f-b482-a9383bd07e7d | 2.37931 | -60.80055 | 2025-09-24 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb241c23-264a-3226-86ff-23bfc8dd159b | 3.06892 | -61.12983 | 2025-09-24 05:38:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4efc904-4fa3-3bb0-a2cf-ce335a8d7183 | 3.06833 | -61.12611 | 2025-09-24 05:38:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13c0acd9-025a-34c1-a751-dbe83769b51c | 3.14065 | -61.00818 | 2025-09-24 05:38:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e930f874-12f1-3e52-9c2e-e045afcbe08d | 3.14006 | -61.00444 | 2025-09-24 05:38:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f078fa55-072c-3640-a676-c8a5677e201b | 3.97693 | -60.04955 | 2025-09-24 05:38:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9092b920-e7ec-3ec5-a88b-7666f60d9105 | 4.54582 | -60.29969 | 2025-09-24 05:38:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95e98e08-6b02-3faf-9e53-1f7bd18fe365 | -5.94162 | -42.90689 | 2025-09-24 05:40:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 64c8e067-323f-3658-9502-4fd1f0a26c21 | -5.94295 | -42.89804 | 2025-09-24 05:40:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eab04169-4d4c-3208-b3da-62d6f5d484ee | -4.79191 | -43.53576 | 2025-09-24 05:40:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| bfe51406-a64c-39e6-bdc0-3c844db68076 | -5.62322 | -45.72422 | 2025-09-24 05:40:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c687c7c2-b5b5-3bbb-a949-b0a7a9ea58b3 | -5.2451 | -43.72018 | 2025-09-24 05:40:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 73c31496-4332-3a50-b12a-56ca56deee8e | -5.63247 | -45.73148 | 2025-09-24 05:40:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6f89531e-c2dc-3f4c-bb96-3c79a0348771 | -2.18422 | -54.46487 | 2025-09-24 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89b4d39c-eeb0-3fc1-bd33-3350eedde5e0 | -4.78288 | -43.53443 | 2025-09-24 05:40:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4fb88b8-2944-3413-a690-03387ce6248b | -6.88525 | -44.76583 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 54ef408c-17ff-3392-aa45-c71ccc0abdc3 | -1.08339 | -54.11006 | 2025-09-24 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 992808f3-3288-35ca-bdf8-3353c8dfb114 | -4.79251 | -42.75226 | 2025-09-24 05:40:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| af1031e8-1f14-3b5c-af5e-4bed8d78ac5b | -3.41607 | -52.67356 | 2025-09-24 05:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| def8d435-b0d6-3106-8816-c36dfe7c3ce2 | -4.78051 | -42.75383 | 2025-09-24 05:40:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 579a54fb-5dee-3393-8d1d-d85fe06e7ecb | -9.03072 | -44.9471 | 2025-09-24 05:40:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb3ec9a0-f219-36f4-95cd-2b2dd4664195 | -7.94269 | -44.0954 | 2025-09-24 05:40:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e142c84b-713d-315a-a1d1-9d5a73e45e13 | -7.28164 | -41.86109 | 2025-09-24 05:40:00 | AQUA_M-M | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a7f7a866-10c7-3ceb-9acf-fb1df72fb936 | -6.89459 | -44.76735 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1e7b592-3b3c-3a1c-b497-fdd746ce5311 | -6.32313 | -43.62536 | 2025-09-24 05:40:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8ece4220-d817-3640-97c8-8011eece8036 | -5.30562 | -45.31961 | 2025-09-24 05:40:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9494f61e-64cb-313e-9e89-5ed8a1dada2a | -7.94127 | -44.10463 | 2025-09-24 05:40:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 715cc2a8-ac0b-3741-acd5-055b2d4d52b4 | -5.23603 | -43.71885 | 2025-09-24 05:40:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a7c8e7ed-1c84-37f1-9697-0b29c7648081 | 0.16027 | -60.68365 | 2025-09-24 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 102ebdcf-2e59-301e-bdca-48f8c2d63c96 | -3.62287 | -51.91183 | 2025-09-24 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f739e95b-3d37-342e-88a7-c5c0c740cf47 | -5.51796 | -43.86694 | 2025-09-24 05:40:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 580f1f1c-48f5-326f-b9db-df61bd90a31d | -4.39805 | -44.3593 | 2025-09-24 05:40:00 | AQUA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d1ca520b-9489-3fbb-b086-3fe5e81e861b | -5.63434 | -45.71973 | 2025-09-24 05:40:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 04f32a82-0266-3560-b80f-fd0ce6f60d10 | -4.31113 | -48.10084 | 2025-09-24 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 3e1e527f-e484-3c21-bbf6-34e95847039f | -6.95352 | -44.63402 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5934a836-6006-31d9-a485-9b91884eecc7 | 0.16322 | -60.67899 | 2025-09-24 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db733250-0b9e-38b0-a95d-9ac6d7a3c7f0 | -7.64171 | -45.21497 | 2025-09-24 05:40:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f9b1fea4-65b2-35d6-afda-f3c058659624 | -6.41339 | -43.09603 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f5fb83c-55b6-360f-907b-5e9e4758a6bd | -5.62236 | -45.7299 | 2025-09-24 05:40:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 76082535-022e-3309-add5-13a21370bd38 | -6.42358 | -43.08842 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c25bd59f-a09c-33f4-8869-5edc17857a00 | -6.4161 | -43.07825 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d8dab5f9-a863-3b2e-9e85-10adefc1bc20 | -3.4167 | -52.68045 | 2025-09-24 05:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cd73c118-f8a3-3a11-9222-727896af5a28 | -6.42493 | -43.07955 | 2025-09-24 05:40:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a438ab5c-d55a-3fe8-9035-ceb9ca05bc13 | -3.62964 | -51.91237 | 2025-09-24 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5d53ff3-38b3-3ade-b0dc-71ef902fd9da | -5.73208 | -43.79609 | 2025-09-24 05:40:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 205436ed-d54d-30a2-8560-de2843cf587d | -5.54368 | -42.79567 | 2025-09-24 05:40:00 | AQUA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b89382c8-d9d0-380f-8cb9-d14bac589c4d | -1.08847 | -54.11457 | 2025-09-24 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c36c0a9b-6b11-3d4b-a539-600900452df9 | -3.41743 | -52.67538 | 2025-09-24 05:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README19.md)
