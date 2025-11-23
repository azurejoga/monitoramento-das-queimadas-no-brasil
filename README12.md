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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 211118e6-35ab-31ac-8898-d272d4fbc6de | -18.50044 | -55.52189 | 2025-11-23 06:37:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5cb01132-577c-3f6a-8865-40fbaf9843a3 | -0.03897 | -51.11817 | 2025-11-23 12:14:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4bf7e0fb-3bec-3356-82a5-9130af8565bf | -2.98571 | -44.42741 | 2025-11-23 12:16:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| de853b2d-cd29-3a8b-9f6c-22e24909ade0 | -3.12661 | -41.90191 | 2025-11-23 12:16:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5562628a-41a7-3392-b774-90d1471a2cbe | -4.03768 | -42.53322 | 2025-11-23 12:16:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9aa192e4-b70a-3b42-8ab3-2cba1afe5351 | -3.42368 | -42.15038 | 2025-11-23 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 7848b6ed-1325-3d13-9394-4b8d0e498354 | -3.42587 | -42.13423 | 2025-11-23 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| b0809e2b-1d93-3d48-b77f-89976583ace2 | -2.25691 | -45.96734 | 2025-11-23 12:16:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ce2f0c9c-78a5-344a-911c-50c3d20aaeb8 | -5.57616 | -42.28871 | 2025-11-23 12:16:00 | TERRA_M-T | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 3f8f8b71-9360-3f72-af09-f100f8ae4e70 | -8.68795 | -48.29734 | 2025-11-23 12:16:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 75e99bcc-f44b-3a9d-bd2c-573528b76892 | -3.412 | -42.14861 | 2025-11-23 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 104d6d65-10e0-3ab1-a713-de8f95e430af | -2.98878 | -44.42308 | 2025-11-23 12:16:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 2c932a1d-7464-384c-a3e9-fee74a1ebc21 | -3.67889 | -42.55427 | 2025-11-23 12:16:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 41.4 |
| b3bdef98-6565-3ce4-809c-2b3be33790a4 | -3.51962 | -45.0706 | 2025-11-23 12:16:00 | TERRA_M-T | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 29ab524a-a27f-341d-af18-2f83881740f8 | -3.99849 | -43.40611 | 2025-11-23 12:16:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 8f87b9b2-a54c-3d2f-9872-82762ec3beb8 | -3.06679 | -42.41349 | 2025-11-23 12:16:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2eeb0922-2927-3d5e-b52d-b393c5714c72 | -3.39933 | -42.00824 | 2025-11-23 12:16:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| 8622f2f6-dda2-318f-bd01-9fd5bb0fc46e | -2.88854 | -45.28374 | 2025-11-23 12:16:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c83fbe5a-6d13-32c3-8940-b0bdc7ec6c4f | -3.58499 | -44.9173 | 2025-11-23 12:16:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 57b0109f-d3ad-338f-8edb-c9e1bac9338f | -3.41211 | -41.37038 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 3135c5dc-30d4-3b65-970d-1b79cbd07976 | -3.06329 | -42.27168 | 2025-11-23 12:16:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| f10afed8-878c-3803-aafc-a81d9bfe5cf1 | -3.06111 | -42.28743 | 2025-11-23 12:16:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 2074607f-b817-3274-a902-bf7706797fd1 | -2.25561 | -45.97646 | 2025-11-23 12:16:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5cc085a6-eb1d-3a06-b9a4-c857aefd509f | -2.76766 | -45.48804 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 10a468e6-79ce-3065-a011-358851970b7d | -3.67677 | -42.5695 | 2025-11-23 12:16:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 3c235531-e175-3ff7-882b-f6a7f2d2db59 | -3.19939 | -45.03926 | 2025-11-23 12:16:00 | TERRA_M-T | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 01566f2d-5548-3b64-a723-cb48ca0945b5 | -3.95895 | -45.40379 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| ad01210c-3270-383a-b499-461a858c5acb | -3.39701 | -42.02476 | 2025-11-23 12:16:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 7bd022f6-77fb-397c-b971-d6fc9fa9c92e | -5.58154 | -42.29518 | 2025-11-23 12:16:00 | TERRA_M-T | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 3b0070a1-2f28-3e81-a060-4ba784faca71 | -3.40788 | -41.38108 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 261.8 |
| 2c6ed6be-3a1e-3878-ae26-5cb480209a53 | -3.43736 | -41.55672 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| e339c63f-6f83-3f4d-99e3-7eb866b0af4f | -3.16023 | -41.10049 | 2025-11-23 12:16:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 6d9c4def-109a-3685-ab2c-de8618215154 | -3.20371 | -41.61523 | 2025-11-23 12:16:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| bfacae33-6b86-357d-99d3-8c4ea832dae4 | -3.38066 | -44.24487 | 2025-11-23 12:16:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e66bed73-9cd1-3e9e-8ff0-bd82382370c6 | -3.27965 | -42.03584 | 2025-11-23 12:16:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 90513af5-62c6-35e4-a22d-94d11592822e | -3.405 | -41.49106 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 284.2 |
| efe3b3b8-86e1-3ede-b616-603fab017c71 | -8.41731 | -43.94214 | 2025-11-23 12:16:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 26804089-baa1-3b42-afe8-df4a86acbdc2 | -2.98728 | -44.41648 | 2025-11-23 12:16:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 84915ecb-2c51-3115-a99a-b16682e70d8e | -3.14175 | -42.36769 | 2025-11-23 12:16:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 60e3626c-3439-3e21-bf19-cf802e4e5bf2 | -3.4505 | -41.95278 | 2025-11-23 12:16:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| fdbc1230-c4d1-321a-9b09-7bb02883e9fa | -3.19405 | -41.5958 | 2025-11-23 12:16:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| bb3d9840-202d-38ba-9c51-f02b9613b83e | -3.95204 | -45.40646 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 94247fac-ce09-3414-b313-eb21202171bb | -3.19155 | -41.61351 | 2025-11-23 12:16:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 01239972-bd43-3b54-b5f5-4272e9812471 | -3.71236 | -42.48109 | 2025-11-23 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 746d4855-f492-3bf0-915b-7d55397e01ec | -3.55866 | -42.42252 | 2025-11-23 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 0a56cbbb-b90e-3e4f-89bd-389d073e81ed | -3.43488 | -41.5748 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 8d1b5615-cd4e-391f-8dd4-1e19154062cf | -2.76631 | -45.49762 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1bb6ceb8-929c-3a1b-9bab-3a9bdb9bc263 | -9.55649 | -47.77266 | 2025-11-23 12:16:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1619b96-8f3b-32ce-88e5-24e37c48f83b | -3.44472 | -41.50314 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 46.8 |
| f82ca919-7c58-3a73-9a25-d0d34346ab86 | -4.55426 | -48.48606 | 2025-11-23 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 75a86607-5fd0-3ef7-a902-68618cdb8ee0 | -2.63867 | -47.29475 | 2025-11-23 12:16:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4e6e1a5b-8160-3bb9-b0d2-bcdf50e75b46 | -4.32426 | -48.59959 | 2025-11-23 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| efc40e7a-a0a7-36b0-949c-68ba279ff2da | -3.40983 | -41.38753 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 202.8 |
| 6403046c-975c-3928-b228-5f6c5a34b26c | -3.06893 | -42.3983 | 2025-11-23 12:16:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8391342e-e689-3b45-a975-cb499dbf3038 | -3.57447 | -44.4726 | 2025-11-23 12:16:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 90fb4e83-7ebc-320c-bc4b-dcb5a134fa1c | -4.53731 | -48.91651 | 2025-11-23 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 78c27533-fa0a-3214-9531-b57415f59e7c | -4.19412 | -44.8652 | 2025-11-23 12:16:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 617061ad-b4aa-3135-858d-05ccf8b45f22 | -3.57544 | -44.91604 | 2025-11-23 12:16:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 550ce70b-837c-38b3-8538-84b2293b6177 | -3.72389 | -42.47241 | 2025-11-23 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e431f653-a664-3c3a-85bc-2c69f93e526d | -4.11447 | -49.09563 | 2025-11-23 12:16:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2afff46e-3396-3026-a5cd-9f502d7f8ba8 | -3.95347 | -45.39654 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| afbd86fb-fd55-31ad-90c0-b405a6d72176 | -3.7218 | -42.48804 | 2025-11-23 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3e0ddc11-9f62-3560-b0e1-60add0ca3f61 | -3.4077 | -41.49804 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 131.8 |
| 3825c05a-3ac3-3516-9f13-5aa6f8d7c36c | -2.75848 | -45.48677 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 908b5df2-90ed-32bd-a44d-5730d58fb00d | -3.40596 | -42.01471 | 2025-11-23 12:16:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| b0bdb2e1-02a5-3f10-8434-2bd4cc4ba981 | -3.44228 | -41.52092 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 5303e8bf-a95a-3d80-89d1-af818f276e49 | -4.67366 | -48.17478 | 2025-11-23 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d3dd687d-8147-3fa0-85ba-04e5f7dd71b2 | -3.4076 | -41.47267 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 3211e9a6-4eb9-34a7-8ed4-736c4c1ef874 | -3.37087 | -41.37339 | 2025-11-23 12:16:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 6d4357c9-97a9-3437-90b4-acdc09b691f1 | -2.94357 | -42.21782 | 2025-11-23 12:16:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ee36f759-e35d-3623-8bbc-d88e7479fea7 | -3.41551 | -50.02187 | 2025-11-23 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9a4adae3-11ab-3ac4-a1ed-16d60575961d | -3.12401 | -42.41188 | 2025-11-23 12:16:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f2a36de9-945f-34f8-bd1c-0be32064acf6 | -3.38228 | -44.23353 | 2025-11-23 12:16:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ba9fafb6-2486-324a-a13e-7189ff51c581 | -3.78886 | -44.10766 | 2025-11-23 12:16:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f55123b5-c8b9-3cbb-b369-da8080139096 | -3.74253 | -44.72963 | 2025-11-23 12:16:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7c078ede-4c9f-30b1-8373-5984a8be1550 | -3.74404 | -44.71889 | 2025-11-23 12:16:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 40216831-b4f1-3645-b0b8-962a3ec0448c | -4.63181 | -48.64958 | 2025-11-23 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3a20eec0-9c51-3897-8d54-fd716cda5074 | -3.57293 | -44.48367 | 2025-11-23 12:16:00 | TERRA_M-T | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 893d0a50-c9f0-3bb1-ae48-ffb12b02c403 | -2.52599 | -45.95772 | 2025-11-23 12:16:00 | TERRA_M-T | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2c4313c-24ba-3c88-8871-bfb62c06e157 | -2.12246 | -45.9365 | 2025-11-23 12:16:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 768201d4-440f-3c1d-adb8-48fbe62fd360 | -3.18995 | -45.03798 | 2025-11-23 12:16:00 | TERRA_M-T | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f0dcada5-f8cc-3cc3-b371-fd7a57d4bb56 | -3.71243 | -42.47097 | 2025-11-23 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 5ac3ce3d-699c-3697-ab29-0b7eef4ef3f8 | -2.2953 | -46.15422 | 2025-11-23 12:16:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2ba21d0d-6d53-31c9-bd89-1f3e6d078c6e | -3.71037 | -42.48649 | 2025-11-23 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a4b5f233-687d-36a1-9391-96e351e5d16f | -3.41263 | -41.46125 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 04c26e21-4abb-3945-a91a-3fef41caf820 | -3.28873 | -44.68032 | 2025-11-23 12:16:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e921435a-d1fd-3354-93a4-53449259e036 | -2.5221 | -45.98514 | 2025-11-23 12:16:00 | TERRA_M-T | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 233ef1b8-3276-302f-8283-43f99bf1615f | -3.56076 | -42.40693 | 2025-11-23 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 2a8762b3-6c69-3859-a978-5f04e1568635 | -8.74391 | -47.71385 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ff6fce72-a32d-3bcc-9afd-ae4c22a0cc40 | -4.03557 | -42.54856 | 2025-11-23 12:16:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 1c030620-c7fd-3b18-ba11-cf66ca424e56 | -3.38213 | -44.24001 | 2025-11-23 12:16:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4c9c483b-e80f-33d4-b979-aafe38a1ff1e | -3.40261 | -41.44179 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| e7b2baf5-bb78-3935-a36e-cc6d4437fb13 | -4.97062 | -38.28654 | 2025-11-23 12:16:00 | TERRA_M-T | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 31382a3a-be1d-3be1-a065-84d17fc47754 | -2.44352 | -49.09547 | 2025-11-23 12:16:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c1d69293-c4d9-3be7-85b7-d8113b415e40 | -3.96032 | -45.39387 | 2025-11-23 12:16:00 | TERRA_M-T | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f19e6c1a-89a5-3e96-a073-d19b2d599e98 | -3.1954 | -41.62052 | 2025-11-23 12:16:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 8ef39c2e-ed7b-3ac1-82ff-1db5dbd55f35 | -3.20624 | -41.59748 | 2025-11-23 12:16:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| e3e42c5a-eb0f-361b-aa62-b21ac5c1e336 | -3.41018 | -41.4795 | 2025-11-23 12:16:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 201.6 |
| 151a0cdb-dde0-3fdb-970d-a1687ca032e3 | -3.19776 | -41.60284 | 2025-11-23 12:16:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 90235eda-94fa-3fd0-9b06-0c9c2722399d | -4.12352 | -49.09695 | 2025-11-23 12:16:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README13.md)
