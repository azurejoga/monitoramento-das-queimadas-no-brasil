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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0fcecc-ba7c-30d5-96f2-8c62a245e495 | -22.45354 | -44.12589 | 2024-10-02 03:57:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 426d2138-29cf-3dea-bb9c-aa506a41ae6e | -22.45286 | -44.12989 | 2024-10-02 03:57:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b3eccf0e-24dd-3b62-89df-4741a0fa7c1b | -22.35559 | -44.22822 | 2024-10-02 03:57:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| bc7e5b47-6529-3b63-8c95-428c6e08bcb8 | -22.35215 | -44.22753 | 2024-10-02 03:57:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| a97bcb20-923d-3a6a-9c21-8a21f8337224 | -22.35147 | -44.23157 | 2024-10-02 03:57:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 8c537e81-255b-39fe-9477-e993d8c86d21 | -22.34803 | -44.23089 | 2024-10-02 03:57:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56f623fb-3c33-3917-9bd3-310b4c2ea74b | -22.34734 | -44.23491 | 2024-10-02 03:57:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ef17d9a-f52e-371a-82e5-dc58c4948743 | -22.01017 | -44.50346 | 2024-10-02 03:57:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 00b8772f-ac16-3dbb-bf72-c678cde694bc | -22.19902 | -45.47356 | 2024-10-02 03:57:00 | NOAA-20 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f92fd2db-d4d6-3d7f-a6ff-c1b22af87d9e | -22.11246 | -45.08839 | 2024-10-02 03:57:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0c21d58a-362d-3df7-9db5-cb27c5431fcb | -22.11169 | -45.09277 | 2024-10-02 03:57:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60cc4d68-8de4-3bce-9773-baf37a36325c | -21.88427 | -45.34147 | 2024-10-02 03:57:00 | NOAA-20 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f51d1d73-0d26-3178-9157-823d07eb4876 | -21.88344 | -45.34603 | 2024-10-02 03:57:00 | NOAA-20 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a457f10d-ccd9-368b-88a4-15a20e040774 | -21.88065 | -45.34077 | 2024-10-02 03:57:00 | NOAA-20 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0a6de4d5-402c-3a67-89a4-c4897aeab3ce | -23.2905 | -45.29442 | 2024-10-02 03:57:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 46caece3-765c-305c-b96d-e89324451995 | -23.28694 | -45.29383 | 2024-10-02 03:57:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1abf2072-4b3e-3411-a7ac-86b28b21611b | -23.20514 | -45.56917 | 2024-10-02 03:57:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b7814544-271e-33e2-a7cd-ecf48a20fe48 | -23.15327 | -45.07949 | 2024-10-02 03:57:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed4de739-1f34-3f11-8eb6-a4b6ec85e532 | -22.7843 | -44.24893 | 2024-10-02 03:57:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21913b7f-686b-3060-af6d-1d8f9b50a10a | -22.78363 | -44.25284 | 2024-10-02 03:57:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 35ff653a-70d9-32e1-b71c-f805332fd892 | -22.77537 | -44.23902 | 2024-10-02 03:57:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 197168b5-4691-36a5-860e-31785d5f2d90 | -22.77262 | -44.23442 | 2024-10-02 03:57:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 10ead796-2127-3a78-8ad9-12fe5a1303ca | -22.77197 | -44.23818 | 2024-10-02 03:57:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 2ff9a28c-7560-3ebf-8593-abf7aebd3537 | -22.76921 | -44.23367 | 2024-10-02 03:57:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c4dcff24-a89f-3f7e-bf21-838856fc20ab | -22.49189 | -44.15005 | 2024-10-02 03:57:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c8a0b6fd-4240-391b-b72c-1f7857f89bb6 | -22.48847 | -44.14936 | 2024-10-02 03:57:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7e9ca5bc-7178-37de-b9d8-2e56fea4c052 | -22.48779 | -44.15333 | 2024-10-02 03:57:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7fce55e1-61b3-38a8-a05d-4feaca84e3b9 | -22.77036 | -44.65162 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0a0a3f7c-26b0-34c0-8048-c91c841b352b | -22.76966 | -44.65559 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dfa074a7-6883-3998-9782-fa2830e6078f | -22.76896 | -44.65965 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5516095b-c054-3da9-8808-36a13272d1d5 | -22.76758 | -44.64697 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 57595155-b5f7-3a94-bff5-5a7c4dd47ddc | -22.76689 | -44.65091 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5a06bf3a-3df1-3d51-b0b3-9ef73e0f2014 | -22.76619 | -44.65491 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 78da5058-9afc-39ec-910e-623d3b40da0c | -22.76481 | -44.64228 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eaf28bcd-c437-37cb-8acd-16b77cc97430 | -22.76343 | -44.65018 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d2bc5a8-f16e-337c-829d-e2823894e6c2 | -22.90614 | -45.09859 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 20fe310b-65d4-3b92-aec7-e7a9f3cb99c5 | -22.90534 | -45.10306 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 19974bd6-713c-3916-8ae8-b7a0b8326099 | -22.90261 | -45.09787 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| adfbf3fe-bb14-3ff6-9c25-29eff4509aa7 | -22.9018 | -45.10241 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6053dfa6-864f-3e43-bda7-19462b8890be | -22.89985 | -45.09284 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4faa3fda-8afd-32cf-99f7-cf2146a14314 | -22.89908 | -45.0972 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 81a4fef6-75b9-3237-bb7a-0168267da167 | -22.89826 | -45.10179 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a4738c6a-1a0d-345d-82f5-d880b4eb8a4f | -22.89661 | -45.09394 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| fc0aef61-0e10-3f31-a62a-817c639c1682 | -22.89632 | -45.09216 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 128352d0-819a-3c23-b077-7330e9d75285 | -22.89583 | -45.11536 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3dc53e4e-ab09-32d1-b635-1a3500a890aa | -22.89553 | -45.09655 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 95e11b6d-a502-322a-af6d-87438502d02e | -22.89504 | -45.10308 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9746551c-8b81-33aa-a319-a0c933a327a1 | -22.89503 | -45.11983 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2896ce23-0374-323f-88a1-028d36cadd94 | -22.89471 | -45.10116 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1eda3283-d79d-3c79-9141-732bea6f1e87 | -22.89426 | -45.10764 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 26545957-0f95-32be-a01c-99849f25859b | -22.89389 | -45.10575 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c81ad10e-838c-30b1-a3b7-5d9cb10bdbc0 | -22.89382 | -45.08897 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ced28268-5cba-39e4-8363-4f35ab82154f | -22.89355 | -45.08718 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2f380253-05dd-3101-a88d-c91db2f4c3a4 | -22.89307 | -45.09335 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 19085999-84ed-30f0-bf8a-ab8a9e5cebf2 | -22.89277 | -45.09154 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5701ec57-7b28-349b-babb-87c20d954617 | -22.89198 | -45.09597 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 16cc758b-c7c2-3c9a-ada3-5b92f185a39d | -22.8915 | -45.10245 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5c7834bb-3751-3b09-8d9d-a879911a1642 | -22.89116 | -45.10055 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0df0323c-4b9b-3e16-8814-de35d0c9ed2a | -22.89035 | -45.10511 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 56856a2a-2878-3cf1-9473-17242030d357 | -22.89029 | -45.08831 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| e0d5b817-82bf-3b34-9312-353a5f65dc83 | -22.88952 | -45.09278 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 30420ebb-b305-392d-8f09-3d8eb555de18 | -22.88795 | -45.10184 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d5915c08-2d54-331f-9b97-d7545abc75e3 | -22.88675 | -45.08765 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b5992b94-3961-3dd2-9d05-24ea99c4d411 | -22.8856 | -45.11546 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7fb24df6-0e6a-339a-9a28-5d31bf4d1f6a | -22.88321 | -45.08703 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7d53c6a-1bc5-38ee-a7e8-95e3cf470cb5 | -22.88283 | -45.11033 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 41919739-d9e2-30c7-bf77-dbfe69f9da3f | -22.87929 | -45.1097 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a11fb3c-50e6-336f-acc8-90868e7246f1 | -22.86946 | -45.1031 | 2024-10-02 03:57:00 | NOAA-20 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 12e813f3-612e-32ea-bed9-c864b22e3a0c | -22.78737 | -45.19436 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 89dcfa55-5ce0-3da6-bcf8-abb8c360120e | -22.78382 | -45.19362 | 2024-10-02 03:57:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79617673-a9d5-3212-9e53-6f1175ea60b2 | -22.71794 | -45.60179 | 2024-10-02 03:57:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13fba429-6747-3a0c-814a-af78431f6bef | -21.72252 | -45.71473 | 2024-10-02 03:57:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a52c1c7-151c-3169-aee5-cbb093ab37ed | -21.71885 | -45.7139 | 2024-10-02 03:57:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe1764ec-a686-3a97-b643-b179d0576889 | -22.38224 | -45.79291 | 2024-10-02 03:57:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1bdb23a1-8123-32f8-a8e9-cf8b49c5b70d | -22.37856 | -45.79226 | 2024-10-02 03:57:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60cfdae6-af8d-30a1-abe2-b3ddd2cd5ffb | -23.66546 | -47.40063 | 2024-10-02 03:57:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ccfadcec-36e8-3bcc-802b-932b2da7d597 | -23.6646 | -47.40158 | 2024-10-02 03:57:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b409d10a-5964-3e74-8324-af2daed79297 | -23.66392 | -46.11576 | 2024-10-02 03:57:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 14010350-696f-33f1-9fb4-0d745ed66af2 | -23.51579 | -46.268 | 2024-10-02 03:57:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 668398c6-e2af-399b-815f-00fa898b9553 | -23.51211 | -46.26717 | 2024-10-02 03:57:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 61bb351e-0e2e-3af8-8d51-bba799eb9bce | -23.50865 | -47.2235 | 2024-10-02 03:57:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e8bee19a-6d93-32ce-be21-34f499413446 | -23.5076 | -47.22898 | 2024-10-02 03:57:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 56a916f6-a063-3695-8007-c18c3318b017 | -23.50372 | -47.2281 | 2024-10-02 03:57:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fbb09fa4-a494-3155-b6c0-ceb1f31831ff | -23.50192 | -47.21639 | 2024-10-02 03:57:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 758d2ae8-860e-35c7-b254-ec1f61d97c59 | -23.49804 | -47.21552 | 2024-10-02 03:57:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6749b64c-6d0f-3459-b780-b6e2733c9403 | -23.43928 | -47.01344 | 2024-10-02 03:57:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f950f040-052b-3daa-acc9-93b6c375719c | -23.43896 | -46.77175 | 2024-10-02 03:57:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13fab765-5237-3ffa-9d9e-d6c48e64e2f3 | -23.40659 | -46.33113 | 2024-10-02 03:57:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 372099bf-e57b-3645-a20f-a39b6e129087 | -23.40451 | -46.55613 | 2024-10-02 03:57:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c1eec28c-64b2-346e-a88a-868bf79ea3a1 | -23.38431 | -46.43204 | 2024-10-02 03:57:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d619a641-6e79-32b4-8b7f-9a84877bb91c | -23.35383 | -47.01491 | 2024-10-02 03:57:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 25441f8e-23b7-38b0-88e3-0db98b30c4ea | -23.35285 | -47.02015 | 2024-10-02 03:57:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c291f3d0-c253-3d3f-bb6d-056aa361de6c | -23.35179 | -47.02574 | 2024-10-02 03:57:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 10b24df6-1790-387a-8f84-9ae1f791421c | -23.34995 | -47.01428 | 2024-10-02 03:57:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ba7535bf-01a3-3db0-8975-13b718336b42 | -23.33732 | -46.77327 | 2024-10-02 03:57:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c5f1ff3-7f6b-3394-8cec-e5837c7c772b | -23.27951 | -46.66028 | 2024-10-02 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| eeff843b-e2c4-38d3-8ec3-44673821e097 | -23.27855 | -46.66539 | 2024-10-02 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| b91e16ae-b65b-3f8d-9fd2-32c474f784a6 | -23.27485 | -46.64804 | 2024-10-02 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2733d781-c796-3e2e-814e-dfffbfa0b92f | -23.27394 | -46.65304 | 2024-10-02 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 129279b8-a18c-3990-a268-7a8557dc663d | -23.2738 | -46.64881 | 2024-10-02 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README78.md)
