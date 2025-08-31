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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd988f2-58fb-3d68-84f0-7e64001af6f3 | -22.24519 | -56.12299 | 2025-08-31 04:34:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f60b435-3b7a-3fc6-a616-e5f44f124778 | -22.88376 | -50.32245 | 2025-08-31 04:34:00 | NPP-375D | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7cc4be6a-05d4-3a23-998e-e2263d312da0 | -22.90355 | -51.15593 | 2025-08-31 04:34:00 | NPP-375D | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9dd261aa-e4c7-3267-b1d8-c1f7e2c3e25e | -22.66767 | -53.37199 | 2025-08-31 04:34:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d897c2f2-d656-30ec-aa23-0f3bba49e7ea | -28.71009 | -55.64062 | 2025-08-31 04:34:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 63845ee0-7f88-31ff-b1bc-edec7aa5f3e6 | -22.24178 | -56.11795 | 2025-08-31 04:34:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f07ae44-276d-3114-a55f-ed2fcced8bf6 | -29.52584 | -50.63718 | 2025-08-31 04:34:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 24c7c786-e149-3583-a181-3c67f3169af7 | -28.70915 | -55.64558 | 2025-08-31 04:34:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 40da4af1-996c-3371-8369-ae9c6b5df475 | -30.20332 | -53.61821 | 2025-08-31 04:36:00 | NPP-375D | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| a01d56f3-8e51-3d41-ab02-e4861dab38fb | -30.19993 | -53.61745 | 2025-08-31 04:36:00 | NPP-375D | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 9181f6a9-7a7d-3434-92a2-a4a2b8371239 | -9.4311 | -62.3493 | 2025-08-31 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b8daaea7-82c3-306b-8f1d-fef06a94970c | -7.9265 | -63.0158 | 2025-08-31 04:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7a9fd41d-2ed3-36bf-84cb-afca3a788c19 | -7.9266 | -62.9969 | 2025-08-31 04:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4a06e5ae-65e8-35de-8d4e-b7cd2b396337 | -6.1667 | -43.3039 | 2025-08-31 04:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 53.3 |
| ec610419-b441-384c-9c0c-1de82b4ca465 | -9.4498 | -62.3294 | 2025-08-31 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 78883c2d-3eec-3c58-9bf6-29e6d270903a | -9.4683 | -62.3476 | 2025-08-31 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 9bf56c45-ac05-3f73-8000-ddc38dfcf365 | -8.744 | -62.379 | 2025-08-31 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 9e0da7ec-9b9e-3280-9a70-6760c4b4a174 | -9.0614 | -65.4355 | 2025-08-31 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 00df7b52-7958-30db-910f-8dc9f04ebdd9 | -9.4684 | -62.3286 | 2025-08-31 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a30f5ffc-12c2-3448-8e8c-8da3304b8e7b | -9.4432 | -60.5692 | 2025-08-31 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 07421dfe-e204-395c-baac-4accde4ae1f7 | -6.1665 | -43.3273 | 2025-08-31 04:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 24f6b8c9-bf23-3d6a-a9be-ef6e9b711e74 | -9.4495 | -62.3675 | 2025-08-31 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ce577ea5-ca7b-3dad-924d-af947bb439d7 | -10.9512 | -50.8509 | 2025-08-31 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c913b32d-aad9-350a-8a85-4a81773e8c22 | -9.4497 | -62.3485 | 2025-08-31 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 105.9 |
| fbc68a2a-1709-379a-8c12-4b5bd6d3b149 | -3.29102 | -47.87246 | 2025-08-31 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b5ca22c-4efd-35a5-b6eb-303135f7b27a | -5.48108 | -44.39835 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5db647c6-3921-3eb2-87f5-e376c81ee776 | -6.17867 | -44.12769 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 346bdb1c-2b12-3501-b283-11454f5729ef | -7.10147 | -44.31307 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c6f7b2c7-fade-3add-975d-a3759f61ee31 | -3.58344 | -49.42878 | 2025-08-31 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d507b37-01c3-3912-9a44-515dab6b66e8 | -4.41931 | -47.60823 | 2025-08-31 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 205eac3f-ff4f-3351-b90a-7f980a87579b | -7.41376 | -47.43919 | 2025-08-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b314d4f-f317-3b9f-a7bb-282e7a2405e6 | -4.55178 | -50.47691 | 2025-08-31 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e0ca1f4d-05ff-3222-8b46-7d08fd4bf2ed | -6.05864 | -44.58168 | 2025-08-31 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8880e72e-769f-3ff0-98b4-f5d62a36f448 | -7.39991 | -44.0868 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9e4668e-1593-377c-9577-c99ab512a794 | -6.16798 | -44.12958 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a4ba247-ff72-3e9e-8507-b3a0f89ab4bc | -6.17352 | -44.1273 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad467106-0403-35f1-a532-b781d8848d5d | -6.57696 | -43.69492 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 842ccef8-c932-35dc-88de-b5fab3cf30eb | -6.48934 | -43.55819 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa2eec58-b8dd-3384-a38d-cca120914671 | -6.83485 | -43.34181 | 2025-08-31 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b60ed342-1a4a-3fd4-8bcd-f74f41d67de2 | -5.47532 | -44.40318 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d8202cc-d176-369b-8c7f-20c8eb96bc30 | -8.00348 | -44.05631 | 2025-08-31 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c9da0d5-860f-3786-9835-188b0678d0c4 | -6.70727 | -51.41939 | 2025-08-31 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c402ace4-b89d-3f97-9e89-1e02d575531d | -3.28873 | -43.41539 | 2025-08-31 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38e8ef31-d0c5-3cfb-b96a-822454ced095 | -8.19669 | -42.30742 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2fb95d43-f6df-395d-a1bf-e02a667b8eea | -6.17208 | -43.56818 | 2025-08-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8144b80-1b16-3356-9edc-90af741bac6a | -6.58231 | -43.69529 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7929cff5-62f2-3af1-a64c-7f5853e261c4 | -5.65778 | -43.64473 | 2025-08-31 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5a57eac-8f17-3c1f-a18b-aa30c491d6e9 | -6.19523 | -53.76461 | 2025-08-31 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73fc16c7-be3f-35fe-8ef8-32b4ae1cd988 | -6.64442 | -44.25575 | 2025-08-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 893fda36-9876-34eb-be8d-2f5428a7bd6e | -6.57742 | -43.69167 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 21de99ba-3219-3919-ba03-d763f375c83f | -6.61906 | -43.7364 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61931e07-0a0e-30ef-a5a7-4e5626f7da23 | -6.17737 | -43.56905 | 2025-08-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a989ee0-3a8e-30fe-ba5a-9bb3cc83ce68 | -5.98733 | -43.36218 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5aac324d-e867-3386-afbb-f7858ab93f5d | -6.28332 | -43.5398 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b579d3e0-167f-3dce-b8f0-3b54d5c3a23f | -6.43103 | -43.97077 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 898263b8-83aa-3eed-a896-c712b8a03825 | -7.57087 | -45.1199 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c77cb11-ee1f-3bd7-95bd-09e897864267 | -6.9633 | -44.31268 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed19ffba-8619-36c4-8116-cc3d841b1065 | -5.82632 | -51.36452 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a7ac4ba-637e-3e60-abd8-8b3ec2010101 | -7.6409 | -42.65537 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c146e069-08fe-355c-abd6-1261af331a76 | -7.58488 | -42.71353 | 2025-08-31 04:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 38fc1683-6e73-35c4-a27a-4cd9c0e375b1 | -5.55906 | -44.21193 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c67d4f12-8940-31d5-9caa-805e1467c278 | 0.01163 | -52.87596 | 2025-08-31 04:49:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3619da0a-75f8-307d-b901-c259d03fa8c1 | -6.216 | -42.77317 | 2025-08-31 04:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3aed805-200c-3b76-a1cd-bb378f214b94 | -6.58278 | -43.69199 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4acc96d2-be28-3b84-a898-b5c87bc0ad58 | -6.28237 | -43.54644 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6394a4e7-4f7a-3407-a575-3235f5a8c71d | -4.27059 | -48.63638 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93d31029-d0e6-34cc-9e8f-1346337b667e | -6.61861 | -43.73969 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbc4d85e-85d4-3117-9665-d46af0a20edd | -6.15062 | -44.14195 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7946eeb0-5698-3e2b-9e5d-10faa0dbc53a | -5.46357 | -42.5771 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6bb6ab9-d9b7-3d3b-8ce0-964480c1a050 | -7.37799 | -43.40025 | 2025-08-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 749da14a-8e94-3f10-9c3d-7ad37d131da8 | -7.48721 | -45.05703 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0c05c7e-9322-3536-b6ab-257411678286 | -6.77099 | -44.63389 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d5dd6ff0-9af2-3101-941f-383d2a070305 | -8.19436 | -42.30529 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0cab9f74-acab-3c3b-b2d9-c0530bf63120 | -4.17083 | -42.03562 | 2025-08-31 04:49:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e756c86a-12c3-3790-9ad7-3653b7077c6b | -6.16878 | -43.32005 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0c792f66-bcf8-30ca-a0a3-71af69223729 | -3.01219 | -52.89025 | 2025-08-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fce83d8a-ec63-3c4b-b8bd-a3b116a99f54 | -4.27195 | -48.63471 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd862346-72db-3847-af71-f36a84e205e0 | -6.95738 | -42.01014 | 2025-08-31 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e054cbb0-08f8-3b22-858b-c11beae68feb | -7.3303 | -44.09059 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d627a5be-2e5c-357a-a43a-fd7208bdf825 | -6.53755 | -44.44188 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14249560-a430-36ee-9c31-faffefa0c79b | -4.27429 | -48.64389 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02dac983-1ece-3e4d-bbed-46de032cf503 | -5.69639 | -45.95457 | 2025-08-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7759aeae-f37f-3a7f-a44d-2713befb74b1 | -6.6195 | -43.73704 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c650a64-a612-30d5-bd11-0e07f60b975f | -7.19872 | -45.43454 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e870daba-6c77-3c13-9e7f-670a8f2847a4 | -4.17291 | -42.0329 | 2025-08-31 04:49:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 246bf4d7-4291-3447-a745-ab86a6a0a239 | -6.1026 | -43.18802 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6eda1d3-0116-33b3-8daa-7d6784762309 | -6.33089 | -42.52623 | 2025-08-31 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b37d9356-f4bd-3bdd-b44b-641aae85144f | -7.40729 | -49.5176 | 2025-08-31 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbb2d7c0-c4f9-3ffb-a5b0-917f909ead03 | -7.41977 | -42.05085 | 2025-08-31 04:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10a452ae-01f1-3b3f-8bcc-efc9a70fb977 | -3.81367 | -41.55616 | 2025-08-31 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91d7910a-49ac-351b-aba1-861808ae2467 | -7.58811 | -45.12364 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c11c76dc-4d91-36fe-8b87-b29b5b130f0b | -6.96505 | -44.31439 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a22c877f-8b79-394f-8495-7625a397bd13 | -6.4431 | -43.96028 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82f1123e-d684-3c14-8237-64bc491e468e | -2.26368 | -47.8567 | 2025-08-31 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 69366d1a-3a4a-3c43-8209-f2278ef1eee0 | -7.32945 | -44.09687 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0754cd01-4c23-3128-858d-a1a9a7b092c0 | -6.48979 | -43.55503 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| def9ed2a-6a84-378b-a00f-950fba29a33f | -7.3775 | -43.40378 | 2025-08-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a222955-343a-30ab-acff-84411a4dee6b | -7.38613 | -46.66024 | 2025-08-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d30512d5-73dd-38ca-a1ed-efc1b5465512 | -6.48845 | -43.56454 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bacd6720-9717-30bd-bbe6-b7f92fc7fdd9 | -3.81716 | -41.57373 | 2025-08-31 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
