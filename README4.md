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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df5d387a-68e1-3495-9489-f08b04d0841e | -14.01545 | -50.73045 | 2025-04-30 04:57:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a7b9247-8616-3994-9f76-1aba6f955344 | -15.56923 | -47.8572 | 2025-04-30 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d596e8e3-a6bc-332d-aa73-3c2b16816871 | -11.39394 | -52.94231 | 2025-04-30 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e18a9c7-51e6-3927-a158-91a7c2dad02f | -11.79453 | -47.37352 | 2025-04-30 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a508450e-b317-3474-a0fe-22a8fa85287b | -11.40262 | -52.95552 | 2025-04-30 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35ca3fe2-cea3-3797-9c97-609f6b4229f4 | -12.66316 | -58.08627 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c22115dd-de07-3ed6-b5f3-f5fb3b753fe3 | -11.40726 | -52.94829 | 2025-04-30 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c98a855-0e56-3d27-92bd-1c646e67c19f | -15.19863 | -51.56255 | 2025-04-30 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 864f8a42-875e-39f6-9df9-7c91d8608ba2 | -11.77525 | -48.20198 | 2025-04-30 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bfde5a0-8c98-38ed-abab-e660efcd8064 | -11.878 | -58.05596 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632b36ac-5425-3380-91e8-e08a309b0b88 | -11.49432 | -54.57278 | 2025-04-30 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7b881a1-1bfc-3ee8-9141-3b129de1ed3b | -15.56936 | -47.8563 | 2025-04-30 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5df2966b-8889-3391-b8e6-1215f152fa36 | -13.49093 | -60.37912 | 2025-04-30 04:57:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2100ae4-f508-3cf5-aa37-82611b2c3332 | -12.66032 | -58.08165 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8adadbd0-dec9-308a-a42f-d7118a699e7a | -12.68347 | -58.09398 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cd59876-0bbf-3a3c-8668-704828ad8901 | -14.85948 | -52.84098 | 2025-04-30 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f800fc6-9f2a-38e4-a1ff-6e5c4dc85dee | -11.4032 | -52.95166 | 2025-04-30 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3408dedf-f589-31fb-9f81-090ba7b9104d | -12.66467 | -58.09885 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63bc9040-83bc-323e-b3aa-114035a456c7 | -12.50772 | -54.40667 | 2025-04-30 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c64e01e5-4b01-31c2-a724-9f966450b5e5 | -12.3516 | -54.51438 | 2025-04-30 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 732dba56-2465-3ced-8e27-03f1f981dde0 | -11.58695 | -61.2084 | 2025-04-30 04:57:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff5cfdea-ab38-3b01-b966-d0d7a3135b1c | -11.80134 | -47.37576 | 2025-04-30 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a2445f8a-0f4c-315b-9010-655ac89ff046 | -12.1043 | -51.3953 | 2025-04-30 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff45ade2-f24e-31de-84bb-00cb4ca975d5 | -12.66183 | -58.09425 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bd3d42d4-dd59-32d2-b237-bbe0a3f87f12 | -12.66249 | -58.09026 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb5f43c1-1534-3d09-8f85-e12d6caa5d71 | -12.66117 | -58.09823 | 2025-04-30 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dfd1695-7130-3acc-ad56-55a73d6dca1e | -20.0759 | -44.30595 | 2025-04-30 04:59:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3978cdbc-7edc-370b-8ac7-8e1bab824193 | -19.02337 | -57.62255 | 2025-04-30 04:59:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| fceb5473-275f-3c50-ac29-d8708ae43afc | -20.47657 | -53.67334 | 2025-04-30 04:59:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24229b15-94fd-3698-a31c-5b0200f56e58 | -29.35364 | -51.90546 | 2025-04-30 05:01:00 | NOAA-20 | COLINAS | RIO GRANDE DO SUL | Brasil | 4305587 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e3bf8099-f37b-319b-b7f2-0aa94ee9d5a0 | -8.94936 | -44.2336 | 2025-04-30 05:31:00 | AQUA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5c568fb1-253c-360c-9fb7-be0da8c2793c | -11.79964 | -47.37286 | 2025-04-30 05:31:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3b873c52-694f-3294-90f4-50e18ba97435 | -7.07885 | -44.38437 | 2025-04-30 05:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2e0da331-d2c1-397f-92a6-62e49b1bc015 | -7.07006 | -44.38308 | 2025-04-30 05:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d812c678-2254-3c6c-a3fa-1f3cdd02de93 | -8.94052 | -44.23229 | 2025-04-30 05:31:00 | AQUA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 07792c4d-7f1c-3118-b530-86b33aaa0f3f | -7.08017 | -44.37558 | 2025-04-30 05:31:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2f1443b8-4ab7-3fb6-ae23-2a194b02c700 | -6.6265 | -48.01889 | 2025-04-30 05:31:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9f098c09-6203-3894-9b92-1a9cb9032742 | -8.94185 | -44.22337 | 2025-04-30 05:31:00 | AQUA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e128dfd4-476f-3a4f-976d-3210d3800e50 | -8.89569 | -44.78513 | 2025-04-30 05:31:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6321152b-dd19-3efc-ae8f-bf668c44dec1 | 3.92827 | -59.91852 | 2025-04-30 05:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 391e0b95-ae9a-337c-b095-4e971ad2da7a | 3.92865 | -59.91605 | 2025-04-30 05:44:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17fa39c2-a895-3774-bb77-844264fd2700 | 3.14861 | -60.27285 | 2025-04-30 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d7a633c-b5be-3c4e-ae7c-fed05b9bd502 | -12.66206 | -58.09241 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e66feda-cc9a-37ad-9e51-bcff33f088e2 | -11.58856 | -61.20927 | 2025-04-30 05:50:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b785df9-408e-3905-abe2-97a31e6582a9 | -9.80949 | -68.10411 | 2025-04-30 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f257b6f7-52b0-3cd1-afee-7e5d930f4024 | -12.66161 | -58.09624 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5cead120-626e-31f8-91cb-19ab6cabeba8 | -12.68467 | -58.09517 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e67383a0-4c49-3116-91b4-e86185a7adf5 | -12.67992 | -58.08685 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 963c3799-7010-30b4-ae62-beba5234c81e | -12.6634 | -58.08106 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c26c49c-3ce2-3611-8a99-480df1bb0a32 | -12.66295 | -58.08482 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a35f4dcf-2aba-3afb-815d-1df8af4954b8 | -12.68513 | -58.09126 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 267dfc56-fd24-37ac-963d-ae4716d0ab59 | -12.66251 | -58.08859 | 2025-04-30 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e87f2b05-a5e1-39e4-9e25-a979302b68dc | -10.05882 | -48.01685 | 2025-04-30 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d2488909-91f5-35d5-907a-65d5f1af03b4 | -10.2744 | -47.16261 | 2025-04-30 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02006517-4494-327d-b113-50acc58863aa | -9.72219 | -43.91224 | 2025-04-30 12:17:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d16656cf-8e46-32f5-bd69-d7ae7fd5fc1f | -9.08978 | -37.66447 | 2025-04-30 12:17:00 | TERRA_M-T | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 66f45531-d291-3f0c-b937-2fea7c80c1e0 | -11.86003 | -38.3605 | 2025-04-30 12:17:00 | TERRA_M-T | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 60.6 |
| e18f6778-d372-3867-8a01-e42aca0e046d | -10.24633 | -39.33986 | 2025-04-30 12:17:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 41ed482e-691c-3785-9191-1f44d59c0318 | -11.86084 | -38.35387 | 2025-04-30 12:17:00 | TERRA_M-T | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 5289acde-3053-3514-b4c3-c23e9b5452c5 | -9.29556 | -48.31094 | 2025-04-30 12:17:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| edbd1e10-099d-376d-a4de-11c9659763b4 | -8.90646 | -44.77861 | 2025-04-30 12:17:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c45e7ea4-af12-3c87-b895-9906037c8dd8 | -9.02795 | -36.9356 | 2025-04-30 12:17:00 | TERRA_M-T | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 9b0ed65e-5ec1-3466-b685-f34c7b362b91 | -7.21701 | -43.12132 | 2025-04-30 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 5bbafccc-233c-39f9-99bd-7238bc65479c | -10.24431 | -39.35537 | 2025-04-30 12:17:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 176.6 |
| 67647f6d-097c-3f92-aa9e-388da09f17aa | -6.07366 | -39.14843 | 2025-04-30 12:17:00 | TERRA_M-T | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b20f6f71-b3dc-3e07-a1a8-fa6809fd5ce1 | -10.28364 | -39.39815 | 2025-04-30 12:17:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 91102ff2-f988-3a17-ba15-2f9129ae2eec | -11.79847 | -47.36711 | 2025-04-30 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 31b940d6-270d-3a34-ba91-6bb34bf14cb5 | -22.51999 | -42.6985 | 2025-04-30 12:19:00 | TERRA_M-T | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| fd20555f-941b-3a02-8802-b2718804fcc9 | -17.48925 | -45.29707 | 2025-04-30 12:19:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |


