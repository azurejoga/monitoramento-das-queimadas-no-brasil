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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4b67f0e-99b6-3bd2-a79e-098dc2ab69f8 | -14.00208 | -56.63962 | 2026-05-09 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68e125ea-a720-3714-b059-50a8e59c8817 | -12.86407 | -43.75532 | 2026-05-09 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c1e2d5e-e1f4-30d3-b6a5-ee6659362d82 | -18.48505 | -51.68422 | 2026-05-09 04:51:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d550188f-faec-35e6-b1fc-efdc84f3a005 | -11.2946 | -54.02788 | 2026-05-09 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd62a682-93e8-328b-a225-15b89d1c3d2e | -14.31914 | -57.73067 | 2026-05-09 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10044318-9494-3957-8ed0-1c0fd4a8dc0c | -22.70056 | -43.35909 | 2026-05-09 04:53:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a33c7ce2-be53-37f7-a26a-5cc0cb83945f | -20.23407 | -46.82816 | 2026-05-09 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 974bcb6d-cd96-3eef-8e82-d8af73c6ff54 | -18.92222 | -53.22197 | 2026-05-09 04:53:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dab494d-a5cd-3d09-bceb-e3a046f8ed64 | -20.23462 | -46.82342 | 2026-05-09 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3867d085-5b7f-35c2-9fe1-93b71db3645e | -21.33651 | -47.02665 | 2026-05-09 04:53:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6bcf933-0023-39ff-8a5e-f0e085e7034e | -22.70017 | -43.36367 | 2026-05-09 04:53:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9ffd458d-b7a6-382a-8ac8-56accd2a94e7 | -21.33188 | -47.0261 | 2026-05-09 04:53:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a7c898-a1e2-3516-b30b-ca8791a988bd | -21.33591 | -47.03184 | 2026-05-09 04:53:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5f6d18d-73bd-38f4-8118-1325d82072c8 | -18.99753 | -52.59231 | 2026-05-09 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 279a3cee-6e53-3cc7-a205-3cd3e121f96f | -21.33588 | -47.02377 | 2026-05-09 04:53:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a252edc-54d9-3b00-9d6f-36b032025231 | -21.33128 | -47.03128 | 2026-05-09 04:53:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d165fdd-2f9e-3514-9c49-a0a287e1c050 | -20.22626 | -46.81467 | 2026-05-09 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86f3db89-1aa5-3943-a47e-c54957e0a4d5 | -22.40703 | -46.6174 | 2026-05-09 04:53:00 | NOAA-20 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cb73db88-3033-3bdc-89ad-ab31ae68fc20 | -21.33531 | -47.02895 | 2026-05-09 04:53:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8dc0c3a-7d19-385e-ae70-6655bec573ed | -6.22445 | -55.64314 | 2026-05-09 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e2d8524-ef72-3825-ad73-459a220aa4dd | -11.9203 | -54.1067 | 2026-05-09 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99b0b9a6-b914-30ed-ab87-dd51cbddacef | -11.60919 | -54.18635 | 2026-05-09 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b77b7084-eaf3-34a5-9c72-0b6eafa9cbce | -10.54754 | -56.33591 | 2026-05-09 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9e3d7e5-4399-30a6-9f3a-a3f157e6c517 | -11.29753 | -54.75616 | 2026-05-09 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62f73d69-a131-3545-9565-3933632bbb46 | -14.00553 | -56.63622 | 2026-05-09 05:38:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ffb79d6-c38e-33c2-8941-58b9a716f10f | -12.21717 | -63.44427 | 2026-05-09 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 456fdd3d-2c0f-3c66-a0dd-bcc44a169cc7 | -10.5617 | -56.3441 | 2026-05-09 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44d8fd3b-117e-3619-8a29-357ae019a710 | -9.96486 | -59.44846 | 2026-05-09 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2398c5c-ab06-3d9f-bec4-0b3a81b51b12 | -11.57498 | -56.95205 | 2026-05-09 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56b1e96a-c30c-3474-961d-def1f07708f4 | -11.60968 | -54.18211 | 2026-05-09 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc93db21-5a2b-3f3b-9756-54d8dd326159 | -11.29707 | -54.7599 | 2026-05-09 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cb13ff8-a692-3651-b46a-f6976a88dab7 | -11.29661 | -54.76364 | 2026-05-09 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 907c6dc9-c8be-324f-9d7a-5e38d13eda1a | -11.92081 | -54.10249 | 2026-05-09 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf8ebabf-f0c7-3205-ae26-740a11562278 | -13.99968 | -56.64178 | 2026-05-09 05:38:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4acdf064-a9ab-363e-9a3d-f824af3be5bf | -10.32928 | -63.66682 | 2026-05-09 05:38:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ad5d300b-96a0-3815-a429-2a8f207879db | -11.50977 | -58.65588 | 2026-05-09 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e2e4a43-e86a-3109-8345-b324aecaae2a | -11.9267 | -54.10321 | 2026-05-09 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa71aca9-1efa-3896-ac24-b97d55c192c6 | -14.00588 | -56.63321 | 2026-05-09 05:38:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc0b0a2-7870-30c2-ba83-55948bfcbb17 | -11.84474 | -57.84739 | 2026-05-09 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 222252ea-4e0e-3c17-92ae-54ea01e7c3be | -16.41337 | -54.9187 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 071d646d-8d62-32fd-baea-1b615ab63a38 | -16.41418 | -54.91059 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2036f476-da12-3d9d-b61d-9f0a8c012dbc | -16.416 | -54.91014 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ddb1520c-c6d4-3de1-ab61-17e73dfee6fd | -16.41377 | -54.91469 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5a866ab-6734-3b3a-a33a-25a4dc0c8d55 | -16.42007 | -54.91153 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1cc9c82-2f1e-3aed-985b-25c34c4e305a | -16.41966 | -54.91559 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73e89bdf-c1b7-394a-97cf-f7f4b3022725 | -16.42145 | -54.9151 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6b99f07-8511-330b-8234-241e46f81983 | -16.41513 | -54.91824 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30fc7454-fbb0-34f0-9f51-b15c0bd0516d | -16.41556 | -54.91424 | 2026-05-09 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8a459d6-6744-35d0-b63b-49ed0fafa85a | -11.82582 | -47.33596 | 2026-05-09 06:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d7ff8e7c-0871-3d75-b752-8859482578b6 | -11.81577 | -47.33454 | 2026-05-09 06:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8097df47-eeb0-33d6-ba6d-fcfbefb0eea6 | -6.98993 | -42.8629 | 2026-05-09 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 9d6e10ec-27ac-38dc-aec8-1e375eae4922 | -6.98865 | -42.87176 | 2026-05-09 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 9d46fa68-f89c-3b80-a516-1763839bd5df | -10.15707 | -46.35944 | 2026-05-09 11:38:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80046e27-1f55-3a63-8b8a-79392a36a409 | -8.95573 | -45.69016 | 2026-05-09 11:38:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| b5ec5b05-7ac3-3bab-8ff1-e4c58d13a0d4 | -13.66374 | -42.98542 | 2026-05-09 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5a63eeff-2e4e-3186-a76a-b3c3b39e02a4 | -12.27525 | -44.63629 | 2026-05-09 11:40:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 52cbd075-43a0-34f2-8857-2424f6e287e8 | -13.75352 | -42.60466 | 2026-05-09 11:40:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ad3785ce-d097-3c83-8699-36d7af443ed6 | -14.23303 | -43.65167 | 2026-05-09 11:40:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 184c4804-18ec-3dd4-96d5-434f1152c196 | -11.7737 | -43.64824 | 2026-05-09 11:40:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 442ca075-28c5-3420-aa7a-4a0d6b2b8c3e | -11.04426 | -43.84093 | 2026-05-09 11:40:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4559de57-bc49-31b9-ae90-9439956fd639 | -13.66502 | -42.97625 | 2026-05-09 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| f20f90a3-8fbb-3677-8553-f0cda4536d1a | -11.60099 | -47.10655 | 2026-05-09 11:40:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 266fa6b7-fc9a-3475-91c9-81dcce41e83a | -11.78125 | -43.65847 | 2026-05-09 11:40:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 86db4f0c-d4a8-317e-8f3c-d20966585693 | -11.77241 | -43.6572 | 2026-05-09 11:40:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b98d4f57-8749-3f13-ae69-7909a4659a63 | -12.27661 | -44.62706 | 2026-05-09 11:40:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ec98f194-b034-35ff-9ac0-b1fb7c47407a | -13.55738 | -44.00515 | 2026-05-09 11:40:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 19dae370-f42e-3da5-9c9d-d5a39a936de3 | -12.28556 | -44.62841 | 2026-05-09 11:40:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 71b2eceb-0acf-30cd-91c3-649140084247 | -13.55609 | -44.01418 | 2026-05-09 11:40:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6831c72b-1bb0-3f60-8968-d25d6141bf0b | -12.86503 | -43.75307 | 2026-05-09 11:40:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2ca9f182-a1c6-38e4-83fd-d03c4e8dc152 | -12.28419 | -44.63765 | 2026-05-09 11:40:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1eb16d38-4904-36ee-9ce9-debac3c0a1d9 | -11.82268 | -47.32685 | 2026-05-09 11:40:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c92a8c9c-d17e-338b-b88b-ebc796ddf1df | -20.23379 | -46.83264 | 2026-05-09 11:42:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dcbe9504-bca4-357f-a845-30af40eb4812 | -17.2676 | -44.28211 | 2026-05-09 11:42:00 | TERRA_M-M | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fd5c78d3-4c71-3469-b89b-3f684feb2c3f | -15.04023 | -41.99259 | 2026-05-09 11:42:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| a4f8f610-639d-381a-abe8-9ddf153ac40e | -20.23528 | -46.82269 | 2026-05-09 11:42:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b214e86-c4fd-350c-a75b-e9bab48bb7d5 | -15.03487 | -43.39407 | 2026-05-09 11:42:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8fd28ff9-52d6-3441-b8fe-3487b1642788 | -14.68819 | -46.15368 | 2026-05-09 11:42:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d7109baf-1b40-351d-a739-c529607e409e | -21.3387 | -47.02998 | 2026-05-09 11:42:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29c9d6ed-3dae-3c51-9b67-b2810cab6bb8 | -15.04159 | -41.98223 | 2026-05-09 11:42:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| eaf396bb-caca-3a4f-9f43-ffed1b668815 | -12.2723 | -44.62 | 2026-05-09 12:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 271.6 |
| 68d6ce67-411d-3668-af73-c48bd704b204 | -12.2915 | -44.617 | 2026-05-09 12:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 6ba6b4c2-0e70-37d4-b49e-6a4e5ea15f84 | -12.2718 | -44.6434 | 2026-05-09 12:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 22d56c73-c5a6-33e9-a7ae-b4ee17bb379d | -12.2911 | -44.6404 | 2026-05-09 12:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 3a68ca77-8778-3d1a-93a4-0b2eda49ddec | -12.2723 | -44.62 | 2026-05-09 13:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 245.3 |
| dd40f5df-d511-3092-8076-68551ce2c422 | -12.2915 | -44.617 | 2026-05-09 13:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2171b7db-8e3f-3af1-922c-c12193372938 | -12.2718 | -44.6434 | 2026-05-09 13:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 9550ca1b-3d51-3171-926b-52e2fedaac7a | -12.2911 | -44.6404 | 2026-05-09 13:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 88305a7e-c88f-3bb4-ae82-78202c191893 | -12.2915 | -44.617 | 2026-05-09 13:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 40bd95c0-d807-37db-8a11-44324494c55f | -12.2723 | -44.62 | 2026-05-09 13:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 332.3 |
| 5f1394a3-ce7f-324f-ac7a-b95ccf637cf8 | -12.2718 | -44.6434 | 2026-05-09 13:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 9a75db60-4c9c-354b-aa86-84b17b35f08a | -12.2723 | -44.62 | 2026-05-09 13:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| e9f9e788-ed6b-3f96-a171-5f12cefc313a | -12.2915 | -44.617 | 2026-05-09 13:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 0c376fc3-dbfb-3c38-9895-1fa59f953da4 | -12.2718 | -44.6434 | 2026-05-09 13:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d32d6149-9ed4-3c31-951a-739f9d110699 | -12.2915 | -44.617 | 2026-05-09 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| c1c6ab48-9da0-3704-924d-c9f9ceed2920 | -9.4071 | -50.6847 | 2026-05-09 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 20598ecf-ffca-32b1-880b-fb5b18f3c7c4 | -12.2718 | -44.6434 | 2026-05-09 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 834d828e-f802-3f74-ac63-988e1421204f | -12.2723 | -44.62 | 2026-05-09 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 391.8 |
| d48e8b8d-09b7-334c-99fa-60222fb06ee5 | -12.2911 | -44.6404 | 2026-05-09 13:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4440ed06-a06e-3109-b235-dbc0240d4ce6 | -12.2915 | -44.617 | 2026-05-09 13:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 13763576-aeb2-3bb9-b19f-d1a30b608c40 | -12.2718 | -44.6434 | 2026-05-09 13:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 172.5 |


[Clique aqui para ver as próximas entradas](README8.md)
