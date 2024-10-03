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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf1aef98-44e2-31e5-a87c-de508a15c3c4 | -5.73294 | -44.15885 | 2024-10-03 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04e61790-1ece-3f79-b265-f5895f48319f | -6.39221 | -44.75243 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b493b05f-5fce-36c0-9831-5444cf5d446d | -6.32362 | -44.37991 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c66361a-c60a-3eb9-8c34-d8fc324f3dd4 | -6.26975 | -44.72982 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fca6601f-c89f-3083-ac51-82addcfb006b | -6.14282 | -44.77984 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 892e1b43-efd2-3b60-aab4-53b3c3bdd7e3 | -6.12192 | -44.93744 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9947473-53e5-3bb1-9776-ebcf6057cbd6 | -6.12137 | -44.94099 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2155bc5-2580-3748-b8c2-fdf2f66dfc4c | -6.11858 | -44.9369 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29996656-201e-36fd-a883-590fb5fcbe05 | -6.11803 | -44.94046 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa80743d-7ef6-352e-a560-9dcceb7f1039 | -6.11523 | -44.93637 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd18d8ca-03be-32fe-88ad-399244757023 | -6.11468 | -44.93993 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b6c18ca-3920-3c53-8bf8-5296fbd1fb31 | -6.11413 | -44.94349 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17cbf607-907e-316c-a490-765bfd1cb0eb | -6.08693 | -44.7053 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97c58a6d-6f0a-3c35-8641-5ffbefc84862 | -6.08637 | -44.70888 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be21727d-1b6f-3bfb-88e2-07400960d6a9 | -6.08475 | -44.78574 | 2024-10-03 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42af1e15-d379-34e3-8fec-87276b35a2c4 | -6.08301 | -44.70836 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f718943-c5bc-3adc-a518-7a8468c04d30 | -6.08245 | -44.71194 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d07c52c-665b-3696-8df1-bd8ef67ef201 | -6.07517 | -44.71447 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8ecd474-3165-3f8e-8f7a-d703f9a28e63 | -6.07462 | -44.71804 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aac84f6-d396-34da-afb0-89a7a7ad1767 | -6.01644 | -44.55756 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2195f097-2b0b-3e8c-8d06-c6be09ea19b3 | -6.01251 | -44.56067 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50ed6dab-3103-3f0d-bde5-4ba1ad41aa8d | -6.01196 | -44.5643 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0374ec0-a9b9-33ee-9a8a-591031ef9e92 | -6.01139 | -44.5573 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbfd42a1-b13e-38ae-ad14-de89cd289e62 | -6.01083 | -44.56095 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f67b05d9-09f8-3738-b0c3-7fe596032baa | -6.01026 | -44.56456 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abe67445-a60b-3bc9-97f0-2fb7e2d5d230 | -6.00745 | -44.56041 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7300fc3-5f18-32bf-857a-dc3592c863b9 | -5.85069 | -44.60273 | 2024-10-03 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1fed8de-e1a4-31e3-a29f-77a77a86a6f4 | -5.85014 | -44.60635 | 2024-10-03 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84689b14-2b2d-3637-a4b9-7551588cd299 | -5.84995 | -44.87356 | 2024-10-03 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6ada848-29b2-383b-803e-b476ab050da6 | -5.50158 | -44.61539 | 2024-10-03 04:25:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8965816-2eb7-36ce-98bd-23d5eb760854 | -5.50103 | -44.61898 | 2024-10-03 04:25:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6277a11b-077e-3a34-b961-80e1ab7625ba | -5.34266 | -44.52534 | 2024-10-03 04:25:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f087881a-fcbc-3559-95d7-7de7192bbd9a | -7.66155 | -45.20382 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 744feb53-4845-3f17-aa96-f9b23b0f2178 | -7.66101 | -45.2074 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ade86b3a-277d-3784-afdb-a665e13cdc75 | -7.6582 | -45.20329 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2f49b61-c937-369d-92fb-37b8b6c63f84 | -7.65765 | -45.20687 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b095d1fc-ab48-31e8-b0d3-28dfa87a40b6 | -7.65711 | -45.21046 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5a127d0-4a6b-3267-9d21-3d80eb09e76d | -7.65656 | -45.21405 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c22ade7-4118-39d3-866b-83f7f1572529 | -7.6543 | -45.20636 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e601eb1-302c-3e82-ad63-5b31a31d1eb9 | -7.65376 | -45.20994 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28662fde-2c67-3c09-b7c8-f18180c16a45 | -7.65321 | -45.21352 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 045d95d1-8c22-3589-aec5-750bbfd2434d | -7.65186 | -45.20638 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15f5e33d-bfce-3026-ba94-29898ff9fe11 | -7.65131 | -45.20996 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3606e775-1c50-39a0-89ea-33671220e50b | -7.58258 | -45.00772 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e56212d0-95b2-3f0d-9318-e95b8f675cbf | -7.58203 | -45.0113 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5db8bf2-4000-3498-8603-8d39798f8f99 | -7.57921 | -45.00722 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e19ad349-5611-366a-ac85-42bb3f92b7d9 | -7.57584 | -45.00671 | 2024-10-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b048973-ca6d-3e44-b926-70c736dd3744 | -7.75698 | -44.0372 | 2024-10-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 035c47be-cd2a-3b1b-85c5-9b0dcb9dff4e | -7.75349 | -44.03658 | 2024-10-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91f99e3d-4a37-3527-8132-bcf6372daa61 | -7.75 | -44.03601 | 2024-10-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 820b52b1-3cdb-3ab1-a690-17147ea028d0 | -7.63438 | -43.98749 | 2024-10-03 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 854f06f8-c5ec-3297-9c23-e1ee7e0afff9 | -6.63717 | -43.75095 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf4d5d0-aa55-3165-a602-fec59253db29 | -6.63426 | -43.74656 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18a1c184-a898-343d-b32e-5800862dc379 | -6.63367 | -43.75045 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e713b966-0107-3cf5-9c9b-822f631d2dd8 | -6.62424 | -43.78896 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a556e2cd-aaed-38e5-961f-47e91e2962e0 | -7.49291 | -43.93544 | 2024-10-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f70bd86d-866a-3996-b72b-d304dd38359a | -7.49231 | -43.9394 | 2024-10-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| deb54a8e-a9f3-3743-be50-a4a1451e5e3a | -7.49001 | -43.931 | 2024-10-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef48e3f3-1628-383d-8123-9ace260f9160 | -7.4894 | -43.93496 | 2024-10-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec386c88-1d96-3bd2-911c-bace2d262411 | -7.41578 | -44.83331 | 2024-10-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13907be2-fe29-3ee7-b3ea-92cd860bb7fa | -7.41185 | -44.83644 | 2024-10-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d41fd7f6-cf5c-34cf-ad8a-abf7ffe00460 | -7.22573 | -44.23888 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3caf8e0-87fe-3958-a59c-221597ba41b1 | -7.21141 | -44.14716 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e3466d4-2baa-3a51-b983-5ff95be121ef | -7.19931 | -44.15694 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d12c671-5f05-3594-b6aa-eb50681eb51f | -7.19874 | -44.16071 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0e8b1208-f60e-3636-8459-959d644da7ec | -7.19528 | -44.16015 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0086afec-2108-378d-a6b1-6acef7467aab | -7.15279 | -44.23134 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0380bb0-1421-3727-90c0-ee10b293c720 | -7.14974 | -44.23183 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8d91c2c-6b4e-3a1d-8d00-861afb0744da | -7.14935 | -44.23074 | 2024-10-03 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4029d5a-988a-37e0-85cd-dc923d427e38 | -7.01971 | -43.95398 | 2024-10-03 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ba072ed-2317-3f47-a5c9-90dc49c7e789 | -6.86072 | -44.09875 | 2024-10-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46c9623a-d1c4-39fc-8520-af30a5d2290c | -6.86015 | -44.10256 | 2024-10-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58fc6cc0-cc60-3188-88bf-1e237afe4d2a | -6.84281 | -43.99161 | 2024-10-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d5d8152-f9f0-3006-a3e7-09cae78b0efe | -7.3828 | -44.70132 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ab73871-9bd7-33c7-aff7-15cc364a0774 | -7.10016 | -44.46251 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 848a4629-bc2d-3d17-9ed4-4078f11b9435 | -7.09959 | -44.46622 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d00cf677-295d-3113-b5f2-adf95564536b | -7.08199 | -44.4213 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c89a29b5-5b31-3c6e-bc40-d1eb699adf2d | -7.08143 | -44.42502 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 701d2b4e-8252-3dc3-a2d1-866a0573b505 | -7.05916 | -44.41032 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1793e25-7870-31e9-af4b-9631d5391286 | -7.05859 | -44.41409 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30685137-69b5-3966-ac35-edb0e638edcd | -6.97968 | -44.37983 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79ca23a4-0b22-36c4-96dd-b817561f2c01 | -6.97911 | -44.38354 | 2024-10-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46e5519e-7a12-3570-8d20-d2361192d66b | -6.89165 | -44.28965 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63bb5a51-e5a7-3b71-8e05-371177e0ead3 | -6.88822 | -44.2891 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd51e205-23cc-36d3-a4b6-1d2dd6052dff | -6.88764 | -44.29289 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18f3f45a-c74e-3656-832b-b13033b11078 | -6.88537 | -44.28479 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb39a1ae-8885-31b5-b90c-90cc71ec5c54 | -6.88479 | -44.28855 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48fd5411-d74c-33b3-8409-38c36409597f | -6.88421 | -44.29233 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d21b3000-a4a8-36e8-9ab6-fa3cad5715b1 | -6.88136 | -44.28801 | 2024-10-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bfe41b3-e298-366c-b451-fbca4f240430 | -6.85228 | -44.74833 | 2024-10-03 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51951eec-41d0-377d-9c39-63367f574e00 | -6.71375 | -44.53663 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe1ad0ac-1c75-3184-b11f-dd19a9c66f2c | -6.7132 | -44.54027 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b11e7cd3-382d-393e-b272-272c85f3bb5c | -6.71264 | -44.54391 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ee24a08-8920-3bc8-b8a9-ce4aef9c7204 | -6.71036 | -44.53605 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a09423-f69c-3563-9db4-797a8d200b04 | -6.70697 | -44.53548 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eaf27b0-4f00-391c-b329-b672a3ffdb1e | -6.68122 | -44.65869 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd22e183-3c54-35ce-88fc-1328b10415d1 | -6.68091 | -44.52393 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6b498cee-66b2-316f-9e73-3475dd677f4a | -6.68035 | -44.52758 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7121fb49-182c-3113-8bfa-88ffab02709b | -6.67751 | -44.5234 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ec6bfa5-b9bc-34b9-a601-0e1a27c6e4e7 | -6.67728 | -44.66182 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README80.md)
