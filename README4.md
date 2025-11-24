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
| 42f92ecf-6d21-31e8-bec1-fcb2cf99c49e | -4.45841 | -44.10613 | 2025-11-24 04:06:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 904fe02c-71ea-3968-b2e5-5a7d91b1ce2b | -3.92962 | -41.92488 | 2025-11-24 04:06:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 908b7a4f-d6ff-303f-895b-93596742e44b | -2.80162 | -45.35989 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a90eeb6b-1d0a-375b-8a54-6a3d1cb4703f | -4.77918 | -42.72355 | 2025-11-24 04:06:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83004242-4e09-3305-8e01-3870d37a3022 | -2.80083 | -45.36491 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15c25806-17d1-3730-ad37-850036bab3bd | -3.28718 | -43.40307 | 2025-11-24 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6c354a6-dd73-3bde-8f35-ca2b90d8b359 | -2.87091 | -51.80141 | 2025-11-24 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f920b4-481c-34bc-a111-6cf4640fda00 | -4.39779 | -40.67733 | 2025-11-24 04:06:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 897024fa-91a2-38de-a96e-7a2693dc0558 | -4.71714 | -46.45778 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bea66cff-d618-3ef5-8b4c-a1a5e021e019 | -3.5984 | -40.98101 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96602f2e-c442-3377-9127-f145f36e8853 | -3.49003 | -46.02011 | 2025-11-24 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc22ce47-0636-31be-b580-2442931e5850 | -4.82657 | -43.82686 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c41620b-5dee-3460-868f-c15e4d2da5de | -4.64442 | -45.9058 | 2025-11-24 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9697591-0088-38b9-9968-afada9b87a8b | -2.43385 | -44.02836 | 2025-11-24 04:06:00 | NOAA-21 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90c85005-3426-3bfb-907f-591f44ef0067 | -3.29419 | -39.99115 | 2025-11-24 04:06:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0559145d-79e5-32c4-9ef7-e918cdb0ab0f | -2.87674 | -45.26632 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bda05759-34e2-3ef4-8384-c4ca14c8ea51 | -3.58957 | -40.97265 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a093e12d-8bbe-3511-8fc4-3116188a2bca | -4.71177 | -46.46462 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e5624de-7bb4-36d8-a80c-235f7e73883d | -2.88219 | -45.28244 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2822e7bb-aacb-3b32-b167-0f06dd80ae88 | -3.22371 | -45.73227 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 066d2035-4da7-39aa-b61c-7b83b9f01bfc | -5.34486 | -40.88636 | 2025-11-24 04:06:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7775ead2-6f98-3415-a19a-ad39c432e826 | -3.92071 | -43.19057 | 2025-11-24 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4924c067-71c1-3d88-91d6-cc80698f208b | -3.82545 | -48.99405 | 2025-11-24 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be41f803-b5fb-304d-9e72-997b01e30c81 | -2.88066 | -45.26694 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3489f093-2d3f-3ebc-91f9-9c0f5537e695 | -3.99137 | -38.34942 | 2025-11-24 04:06:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc479af9-dc1e-3056-92db-69f2cec8828c | -4.45719 | -45.77041 | 2025-11-24 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ebffe90e-fc3d-3623-9e2b-2a42fd984936 | -3.96659 | -43.23692 | 2025-11-24 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88efac71-5662-3514-ba9b-7f77e6820822 | -4.70828 | -46.46023 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f957a0-4d76-3883-a412-68914245c539 | -3.6017 | -40.98151 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d30378c6-733b-3162-9575-18079615f217 | -1.48559 | -45.87351 | 2025-11-24 04:06:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 53292831-d1f8-3836-9221-72d47cf098b6 | -1.8295 | -45.57327 | 2025-11-24 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a25dfb5-0b8f-3f0c-8fd7-7b322b994fce | -3.17816 | -50.24411 | 2025-11-24 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30177b7a-db71-3971-84b0-71382c130de4 | -4.7124 | -46.46086 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 83fa4658-4b2f-338e-882e-1b5047bf31d5 | -4.26694 | -40.86131 | 2025-11-24 04:06:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 4f177ce2-1d5d-3905-91f1-8e4fbbd98a92 | -2.92729 | -48.23464 | 2025-11-24 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b0c5237-515f-3191-b1ea-9dbce607a120 | -5.18074 | -40.14876 | 2025-11-24 04:06:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 632969c3-5a48-3d2b-8218-beece6b55ef5 | -2.87776 | -51.79775 | 2025-11-24 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1f43ed4-b125-31f9-a6e7-32817d9e09aa | -4.3008 | -47.53903 | 2025-11-24 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fd98e78-7d09-318e-804f-7c45464326ad | -1.82893 | -45.57686 | 2025-11-24 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5af0855-9f5f-3bfe-9881-40d40b2956f7 | -3.17271 | -50.24316 | 2025-11-24 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a83914f9-340f-313c-9a56-1997ed2bca40 | -5.70485 | -37.94818 | 2025-11-24 04:06:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46ad1e99-5625-3968-a4d9-fce5ba5a2e92 | -4.5654 | -43.95986 | 2025-11-24 04:06:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 001767aa-0d93-37fd-854a-25df8409da57 | -4.39029 | -45.73338 | 2025-11-24 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6b5d5a6-0e78-36bf-a88c-61ae7cc866af | -2.13692 | -46.41142 | 2025-11-24 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d418a48e-ceb0-32a2-9bfd-351061f57348 | -4.39425 | -45.73391 | 2025-11-24 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3b58631f-6a97-316f-9f99-2c437ebd82d1 | -4.49116 | -46.00426 | 2025-11-24 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1baab921-5450-38c3-ae2d-05da92d4edef | -1.12011 | -47.74051 | 2025-11-24 04:06:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2943b184-dea8-3c4a-92db-95ae2c1c33bc | -3.82607 | -48.99589 | 2025-11-24 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c3db8561-9d77-382f-bced-0f9de46cdd30 | -4.4487 | -44.3271 | 2025-11-24 04:06:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3fc6a2d-28d4-36fd-87f9-8de9117683b4 | -3.43892 | -41.02308 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ebce4aa7-d974-393d-981f-f60169966a1d | -4.71777 | -46.45401 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2de8d5ea-0eae-3622-847c-e1958df46364 | -2.80152 | -45.35695 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5457e268-9d37-356d-b783-450d7e0f5131 | -2.98433 | -44.40543 | 2025-11-24 04:06:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19094c2d-fa42-3574-9cba-0a2393b548c9 | -3.65783 | -42.77312 | 2025-11-24 04:06:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56336086-131c-3f9e-ba08-4add5e320319 | -4.16682 | -44.46934 | 2025-11-24 04:06:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da9edf0b-8dea-32a1-9625-09237fda9e6b | -4.62827 | -45.85486 | 2025-11-24 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ced6e68-363f-3be0-a4a9-fcd803d808d2 | -4.30227 | -47.53957 | 2025-11-24 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e8295dc-363b-39da-9f6d-83664f3da372 | -4.63224 | -45.85543 | 2025-11-24 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b74922b-b4b7-3285-bd8c-c137a57d617f | -0.95043 | -46.87966 | 2025-11-24 04:06:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b193b7d-535f-3349-b557-772f14148b92 | -2.79689 | -45.36423 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a6f732b6-8c99-38b5-8e33-ca749ad97c8b | -1.71473 | -46.47739 | 2025-11-24 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b93ad171-5c07-3230-89f2-d1f946c24c97 | -4.71366 | -46.45333 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a6c5863-d384-3d5f-85a8-573ae5571655 | -2.79767 | -45.35924 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8f21c35-90ef-3778-869f-d5bdb34060df | -1.48619 | -45.86972 | 2025-11-24 04:06:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e1fd855c-1849-36b8-9d78-4284efbae580 | -0.26116 | -48.79956 | 2025-11-24 04:06:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3ea9046-384c-32c7-8798-f421c87b45c7 | -4.96503 | -44.15732 | 2025-11-24 04:06:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f3fe5aa-d7d8-3946-9ddc-97e54080a55f | -3.71321 | -44.00381 | 2025-11-24 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 985733d3-2ca1-3cbf-b489-b56405b26479 | -4.66261 | -46.05767 | 2025-11-24 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0be52408-1b64-3a60-b763-367004549587 | -3.27648 | -46.04912 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ec7b516-9f6a-3fb2-bf44-10723c2ffd7a | -3.9918 | -43.40243 | 2025-11-24 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aeb2dcf-b25b-30e7-939a-5911bb0a1351 | -2.79676 | -45.36126 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d81c60e2-878d-3205-8f1c-7b41e61344a2 | -1.48975 | -45.87417 | 2025-11-24 04:06:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5c913e45-99e7-386f-8b02-376090824b0c | -4.86053 | -43.24706 | 2025-11-24 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d91875d-4584-3836-878c-8b725c1aa297 | -4.71589 | -46.4653 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6df164bc-3c15-333c-8c8a-a65ea3d59eea | -3.90238 | -47.77324 | 2025-11-24 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd0ec3d6-b7e6-3284-82d8-ee87301db8ae | -3.54685 | -45.27674 | 2025-11-24 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba17e410-e798-3078-91b8-18c3b52eb8db | -3.49062 | -46.0165 | 2025-11-24 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d99590f-063c-383d-9955-1778e181b1fe | -4.16809 | -46.49332 | 2025-11-24 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd86bca1-f0fc-3d1e-9361-d334c13c76cb | -2.7984 | -45.35128 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c5ba2bb-1b04-3305-be14-d67d576a72ce | -3.21643 | -44.36255 | 2025-11-24 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cc9113d-a74f-308e-a137-2e4a5b380a42 | -4.82304 | -43.82631 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5986ffa-9628-31b6-b7a1-17992c4d0f37 | -4.66382 | -46.05044 | 2025-11-24 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4f63bec8-525b-3733-bf06-c1a61dbca536 | -2.79593 | -45.3663 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba28aaf5-435f-3f79-b300-5a58a5f5681b | -1.72986 | -46.19154 | 2025-11-24 04:06:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b51d25e-a7ed-36ce-87d3-fc2fbc11d3bf | -1.12135 | -47.7375 | 2025-11-24 04:06:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea30820e-a0dc-36ce-8e45-c25b071bcaf8 | -4.81823 | -43.83369 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1201b69c-5f06-3a3a-9ac5-0c2c38ac17a5 | -3.3685 | -42.37992 | 2025-11-24 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c4fe396-6d40-30d0-bd0c-b0ff12793379 | -2.1461 | -46.40885 | 2025-11-24 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4065b9f-72df-32b0-be72-2cbb63cafc4c | -3.59287 | -40.97315 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0665e884-586e-35c6-a2ab-c376dc405fb9 | -3.59799 | -44.95722 | 2025-11-24 04:06:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f69a11d4-bd27-3c9f-afc4-2c69423856bd | -3.71911 | -43.22271 | 2025-11-24 04:06:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 237cfdb9-cef9-3326-8e20-b34f0c25e4e3 | -3.74138 | -47.12824 | 2025-11-24 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87db6ac8-d685-38a4-ac24-5554dc1a489b | -4.8224 | -43.83027 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f5f03cc5-c9f1-36b8-a8df-b14684e667c0 | -4.82946 | -43.83137 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 14734f1b-13c9-3bac-acb1-52515d5db9d3 | -5.11482 | -40.72681 | 2025-11-24 04:06:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3e45eaf-c2ed-33f6-ab57-ba5603f08a56 | -3.71255 | -44.00795 | 2025-11-24 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dfac4b9-d525-3ef6-b862-007ec215da2f | -3.49121 | -46.01289 | 2025-11-24 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85c6f104-1840-3b91-afc6-e15902a20752 | -4.54179 | -45.49974 | 2025-11-24 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 11e101fc-de96-3ea6-9a8d-299b9b8bdc46 | -1.95152 | -46.27019 | 2025-11-24 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 503a21d6-6ca1-3e16-b15a-edee4579ebfd | -3.97258 | -43.28882 | 2025-11-24 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
