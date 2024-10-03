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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d893b95e-89fb-3192-b1b2-206e81da2fd4 | -19.50245 | -42.33424 | 2024-10-03 00:26:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f3249477-3675-36cb-aaad-491ae71c3f45 | -19.50197 | -42.32759 | 2024-10-03 00:26:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 273cf46f-77cb-38d3-8660-bfa96ce95d0f | -19.50088 | -42.32099 | 2024-10-03 00:26:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 6bd8c799-136c-3b00-aaf9-954e7566d290 | -19.49567 | -42.87851 | 2024-10-03 00:26:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| f509ae6c-16bf-3f98-b95e-cd9b4d55522e | -19.45835 | -43.06725 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| bd286f21-e4bd-3a99-b6eb-d4edfc1ddb7c | -19.44433 | -41.37694 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 5f29dddd-fb3b-38ac-8c08-a757ba834487 | -19.44291 | -41.3658 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| eb4c4c69-1401-37c6-a8e0-d9c9ad29f089 | -19.43483 | -41.37822 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| ab1a300d-4834-3bf9-839d-77a99e1326a6 | -19.43337 | -41.36679 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 5912ef12-f94c-3545-8cab-c30d8260d925 | -19.43202 | -41.3561 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| dd18cdbb-f2ed-3fe4-809b-0a7f2ea057ae | -19.42395 | -41.36867 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a2e72192-1c5f-370d-bcfe-40abed8ab006 | -19.42257 | -41.35777 | 2024-10-03 00:26:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d869141c-4844-351b-a091-a96153410fe6 | -19.27958 | -43.79026 | 2024-10-03 00:26:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe3fc959-7164-311a-afa8-fb799bcc70fc | -19.27786 | -43.77539 | 2024-10-03 00:26:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f240c593-033a-30dd-b152-261b4e0fc5e0 | -19.26676 | -43.77671 | 2024-10-03 00:26:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 57b90af9-30cc-3356-9e10-5002070748ac | -19.26503 | -43.76169 | 2024-10-03 00:26:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 18ccd301-2e22-313b-8a4e-b0068ecd3a60 | -19.24661 | -40.63032 | 2024-10-03 00:26:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 2e54614a-2633-3196-a990-1c9cb7596739 | -19.2427 | -43.38089 | 2024-10-03 00:26:00 | TERRA_M-M | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 62dae47d-b9ce-3aeb-9cab-75e6d3912664 | -19.03935 | -43.20972 | 2024-10-03 00:26:00 | TERRA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| fca1ae83-90f4-313b-8dda-11fe44586cd9 | -19.0287 | -43.21082 | 2024-10-03 00:26:00 | TERRA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 038f981d-8a51-3eb8-932a-90ddcd5694f2 | -19.02696 | -43.19627 | 2024-10-03 00:26:00 | TERRA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 0e689400-a093-3d22-a266-02f508d22904 | -18.97569 | -43.21785 | 2024-10-03 00:26:00 | TERRA_M-M | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| cf4f9bd7-13f3-38ee-bf1b-429d297b94c3 | -18.91511 | -41.27679 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 6234f193-615e-3f95-9f14-f391985e0b28 | -18.91024 | -41.28295 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| fb9625f0-e77a-36eb-89ee-72e3709b6069 | -18.90891 | -41.27267 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 94fd760d-7397-3601-9056-8001997d143d | -18.90721 | -41.21408 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| d6a0f832-0d06-3e89-8ada-67d2d21a66d3 | -18.90214 | -41.22062 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| e58fefd7-dec1-3b62-8159-b4cef36bdb4c | -18.90078 | -41.21022 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.3 |
| faa72fb3-bf19-3714-b728-2bf4e14b11f9 | -18.89278 | -41.22198 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.6 |
| fb6aa16f-4dfa-3355-8830-5da5b15bc721 | -18.89142 | -41.21152 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 132.5 |
| 0b8ef114-9ca2-3fc7-89fd-9c044794e035 | -18.88338 | -41.2231 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 6893ee7b-c660-3a6d-a4c1-2f42a7216f03 | -18.88199 | -41.21245 | 2024-10-03 00:26:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 7ca5818a-27a5-33fd-8cb4-991ed6414885 | -18.87433 | -43.63953 | 2024-10-03 00:26:00 | TERRA_M-M | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 41f073e7-9879-3702-acd5-d2ed16c4ae0e | -18.87278 | -43.62611 | 2024-10-03 00:26:00 | TERRA_M-M | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 9a77a2ca-1e72-3c1d-890b-aaa5cc27f9b7 | -18.84426 | -42.93579 | 2024-10-03 00:26:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.1 |
| 701967c6-3c16-3f23-bc10-282540e28e13 | -18.8426 | -42.92233 | 2024-10-03 00:26:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 7fef60bb-a71f-377e-aa88-75fc76ecc76d | -18.84181 | -42.94297 | 2024-10-03 00:26:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| bb4ac19c-01f4-3b0d-87b6-71210f4c3d9a | -18.84028 | -42.92982 | 2024-10-03 00:26:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| 585c9a75-5f4a-3631-a5cf-48239fd7c423 | -18.77807 | -41.91232 | 2024-10-03 00:26:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 2f5e6bcd-a187-3f44-9e0b-431945224c3c | -18.77666 | -41.90105 | 2024-10-03 00:26:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| c14fb0ba-5dc5-3836-a8a3-ddd3402f2508 | -18.60182 | -43.94701 | 2024-10-03 00:26:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 96cf5775-0a63-3eca-ad27-ca7ffc98277b | -18.60012 | -43.93188 | 2024-10-03 00:26:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 2288e53a-c403-3192-8cb6-6ce2c70b1848 | -18.5997 | -43.9384 | 2024-10-03 00:26:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| f1a2078b-ef9b-3488-914b-29e945a9f0a5 | -18.59067 | -43.94826 | 2024-10-03 00:26:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5335a9a2-2bfa-350a-9f6b-c83f80b07cd0 | -18.58898 | -43.93303 | 2024-10-03 00:26:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7ad1f6e1-0c35-3cf0-8e27-17fff848f0c2 | -18.58856 | -43.93962 | 2024-10-03 00:26:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f9c686c5-2659-3750-8d05-fa0da98c28d1 | -18.544 | -42.24016 | 2024-10-03 00:26:00 | TERRA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 3a55dc87-ef04-3a70-aaa9-0b84e4d8b2e5 | -18.53563 | -42.25357 | 2024-10-03 00:26:00 | TERRA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 6d5638cd-e777-379a-9a7d-be1dd602a618 | -18.53418 | -42.24189 | 2024-10-03 00:26:00 | TERRA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.1 |
| 82ffe28d-e410-390a-8582-299f3fdaa51b | -18.53274 | -42.23029 | 2024-10-03 00:26:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 34732934-f0bc-3fdf-a090-6279119301a9 | -18.52439 | -42.24382 | 2024-10-03 00:26:00 | TERRA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 3042cf53-5a15-3c51-8434-8cf850b2b62e | -18.51447 | -42.24475 | 2024-10-03 00:26:00 | TERRA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b65fe4ff-39c6-3b42-8d63-271876aaab73 | -18.35205 | -39.78123 | 2024-10-03 00:26:00 | TERRA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 26c361b4-2e47-3a78-812e-e854687c8b9a | -18.33056 | -42.99484 | 2024-10-03 00:26:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 656f6265-68e7-3696-a3ab-d8972393cd68 | -18.32692 | -43.23401 | 2024-10-03 00:26:00 | TERRA_M-M | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| ced3e7d2-fd47-33ce-8d79-243df81b2ae8 | -18.32151 | -43.24004 | 2024-10-03 00:26:00 | TERRA_M-M | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| ce3c30a8-59e9-3849-bad7-90359012c7ec | -18.31103 | -43.24167 | 2024-10-03 00:26:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 52a619a6-0f00-3dcf-ab04-03c27f59a3ea | -18.29344 | -42.18128 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f91ac0c5-9a12-3661-9d0c-8e7e90c548a4 | -18.29207 | -42.17003 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 93c341a0-d01d-3132-9757-61fcfd1b20c3 | -18.29072 | -42.17539 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 762b60c8-594e-366c-b3de-ff48d1d83955 | -18.07217 | -42.62469 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| ad63c4ce-bfe0-3d4f-9017-de5e8750c70e | -18.07159 | -42.61867 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 31b7c2c9-f420-3d94-8c5c-04a08c2f0900 | -18.07071 | -42.61246 | 2024-10-03 00:26:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 706ce97a-28bc-3f00-b732-555b121245e7 | -17.92274 | -42.40429 | 2024-10-03 00:26:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 2cbfa2e8-f1f8-306e-8612-2585f17ccf07 | -17.85496 | -42.26097 | 2024-10-03 00:26:00 | TERRA_M-M | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6c33f886-c065-3aa6-9330-c50e192a98fc | -17.85187 | -41.42705 | 2024-10-03 00:26:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 0dca678b-ea85-3827-aa7d-09b56a98d044 | -17.80189 | -42.9079 | 2024-10-03 00:26:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 51bbda9e-f81d-3076-93fe-f7beb4c72e6b | -17.40472 | -41.59407 | 2024-10-03 00:26:00 | TERRA_M-M | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| cf7e518c-f8a3-3528-b7e1-ab13893b6670 | -17.32545 | -42.50936 | 2024-10-03 00:26:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b20f6171-7544-3b85-aa85-5eb2b75d10e1 | -17.32484 | -42.51583 | 2024-10-03 00:26:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f2282f45-7210-31be-a792-ee11490f00b4 | -17.32404 | -42.49779 | 2024-10-03 00:26:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| c67debdc-e3b1-32ee-bf9c-89c15a90adc5 | -17.32335 | -42.5042 | 2024-10-03 00:26:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d5ccb757-d50d-3838-b307-bfaad32936a4 | -17.25785 | -41.96119 | 2024-10-03 00:26:00 | TERRA_M-M | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| c7d0892b-1862-356e-9bf8-7301c49a0913 | -17.25481 | -43.18507 | 2024-10-03 00:26:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1990cc03-f231-33b1-a59a-4f8b826c6a22 | -9.4939 | -68.508 | 2024-10-03 00:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5bd0e507-c853-300d-b1bc-ca2cd0c2cb85 | -9.494 | -68.4895 | 2024-10-03 00:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 48e0bbe0-369f-3500-9a06-44885f85850c | -9.7173 | -64.2302 | 2024-10-03 00:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 698c1ba1-fc40-34a4-b36b-8721913b67b8 | -9.9665 | -63.0094 | 2024-10-03 00:26:03 | GOES-16 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| fb66eb05-8e29-3c69-9384-c6e4bbb961c9 | -9.9667 | -62.9904 | 2024-10-03 00:26:03 | GOES-16 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| dd9a4a42-462d-38c7-a7f0-c71f6919785b | -10.129 | -56.7722 | 2024-10-03 00:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 31512373-07e2-3cc1-a2ef-e634cea84def | -10.1292 | -56.7523 | 2024-10-03 00:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 3f1547e3-273f-33e7-8c3c-0618177b16ed | -10.1615 | -57.2861 | 2024-10-03 00:26:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 521678af-bd02-38ed-8bee-a97fdcdd4c1e | -10.1617 | -57.2663 | 2024-10-03 00:26:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ee91f9d0-587d-37ee-84a8-0973ae649a37 | -10.1802 | -57.2848 | 2024-10-03 00:26:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e0692104-2fa6-3f7c-a839-971a4708ef35 | -10.1804 | -57.265 | 2024-10-03 00:26:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 2b47f363-4943-311c-b4a8-f65d9553fba2 | -10.4475 | -56.789 | 2024-10-03 00:26:05 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 192f5ffa-4743-3e65-add7-b57f082d8f6e | -10.7355 | -46.1692 | 2024-10-03 00:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 5b5dd396-c873-392d-a9df-687acffe593a | -10.6505 | -53.6994 | 2024-10-03 00:26:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 06914974-24a7-3261-a583-d5a2c5ac5d58 | -10.6128 | -64.0611 | 2024-10-03 00:26:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 0002a601-6553-323f-9d88-9c93bc9e81a4 | -10.8942 | -63.8971 | 2024-10-03 00:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2e08ba07-4872-3055-970e-8796d2765a6b | -11.2567 | -46.9123 | 2024-10-03 00:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 50f90fae-7c4a-357d-8469-117ae60b7632 | -11.6742 | -65.0172 | 2024-10-03 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| decbcd42-7df0-3876-919c-f95fef7d4581 | -11.693 | -65.0163 | 2024-10-03 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 234f23cb-b484-3764-9cbc-639e5d4d6719 | -11.9876 | -57.1877 | 2024-10-03 00:26:14 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ebc78001-8db5-3861-9c69-9cf3612a34d8 | -12.2668 | -45.958 | 2024-10-03 00:26:15 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 5ecae880-cf05-3e68-a4bf-0eb43649a7d4 | -12.4038 | -63.0009 | 2024-10-03 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.8 |
| e7ff5559-be0d-3d42-aedf-9055e623f344 | -12.404 | -62.9817 | 2024-10-03 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 410b970d-53f1-3eb7-ad4e-c34ef3cae8b3 | -12.6295 | -63.1225 | 2024-10-03 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bc1c7bd9-a47f-30a7-b83d-c8009943d865 | -12.6484 | -63.1214 | 2024-10-03 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 296c944e-aeed-3271-a3ce-c6c6090b0756 | -12.6486 | -63.1022 | 2024-10-03 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |


[Clique aqui para ver as próximas entradas](README15.md)
