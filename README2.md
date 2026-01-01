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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 439d3c9f-944b-3917-a0e1-2ebd32a62351 | -6.60239 | -35.18465 | 2026-01-01 03:06:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ad1d19d8-84b5-37e7-a1c9-51810caa1bae | -6.5957 | -35.19107 | 2026-01-01 03:06:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 008af1fb-b00f-32c4-9acc-c6fd498e218a | -17.35801 | -41.52581 | 2026-01-01 03:08:00 | NOAA-20 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 558304b0-d0ed-3188-b81a-9ef6ecbf6fc7 | -17.35945 | -41.51961 | 2026-01-01 03:08:00 | NOAA-20 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4b25c5f9-ddf6-3831-8e2f-6c29b4ed98ff | -9.5631 | -44.603 | 2026-01-01 03:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 45.3 |
| b105f331-a995-3bd2-b44d-ef47ee5e2255 | -9.5821 | -44.6007 | 2026-01-01 03:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 79011402-b30e-3674-8699-7c01a81ba051 | -9.5821 | -44.6007 | 2026-01-01 03:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 87028278-7855-39dc-8e20-0ff83768c723 | -9.5821 | -44.6007 | 2026-01-01 03:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 5da4dbd4-eee2-38dd-8216-b6ef2da7200d | -3.78371 | -38.70011 | 2026-01-01 03:53:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0b61c23-2d96-3170-b756-9d1e245f34e9 | -1.79062 | -45.90197 | 2026-01-01 03:53:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c93281b3-b553-3bb9-b375-0b7d94823148 | -2.33848 | -44.90164 | 2026-01-01 03:53:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31d4ac1b-311b-3ed6-9c7e-939aa5f16e1d | -3.45605 | -39.26719 | 2026-01-01 03:53:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b2bfb649-3d1f-3640-a93a-7368603a8b32 | -1.48282 | -46.02994 | 2026-01-01 03:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ad5eff5-8882-3166-9836-392aa62f5855 | -3.19935 | -39.71345 | 2026-01-01 03:53:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 313485cc-931c-3e1a-bb6e-0c1e24d0cdf7 | -1.3654 | -46.0568 | 2026-01-01 03:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5511c5ae-e101-3dc4-8308-4f81adbc8dfb | -0.9222 | -46.90368 | 2026-01-01 03:53:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8919bf9f-ac38-3ac2-8fc1-80884c6e8d87 | -4.01501 | -38.87251 | 2026-01-01 03:53:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2b067601-56b3-3459-ba3f-a47c630fb26b | -4.16984 | -40.73529 | 2026-01-01 03:53:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f934f441-ad6b-3fa8-8be4-b12c87678e98 | -3.82854 | -38.4581 | 2026-01-01 03:53:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e8d444e-f092-3f32-b025-171895ce27fa | -3.09157 | -43.37736 | 2026-01-01 03:53:00 | NOAA-21 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b14fd385-6c7d-3c5f-a737-0abcdb8a7e38 | -3.5347 | -43.66799 | 2026-01-01 03:53:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5ff33f3-4e3b-38d4-81b6-848db0e78a35 | -3.71886 | -38.65789 | 2026-01-01 03:53:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3b9f07d6-79b5-31fd-ad96-a0bfb6cf77b5 | -1.36489 | -46.05995 | 2026-01-01 03:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e645b8c8-0562-3d14-baa7-2bab731bc54b | -3.8318 | -38.43734 | 2026-01-01 03:53:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0ed605c8-af9f-3088-b602-106cee88c260 | -1.79112 | -45.89897 | 2026-01-01 03:53:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8016633-2ff7-3694-abf4-20764a991ec0 | -2.27395 | -44.81094 | 2026-01-01 03:53:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76d81af1-c90b-3138-bd91-175799ac5fb2 | -2.95044 | -40.19525 | 2026-01-01 03:53:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2bc9c7ed-c0e0-32ac-9b41-60dc4d9ae7d6 | -3.53406 | -43.67198 | 2026-01-01 03:53:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efc0dc2b-0362-361f-a322-c0e8b9ab22bb | -1.48231 | -46.03307 | 2026-01-01 03:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3f630af-41eb-3a71-bb4f-ffda099c92b3 | -0.92279 | -46.90003 | 2026-01-01 03:53:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 817bf92e-2569-31e7-9029-fac76e8a698c | -2.91533 | -40.45979 | 2026-01-01 03:53:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d5e2baf-3a7a-3ed0-934b-9fe6b2bab17d | -3.53044 | -43.66737 | 2026-01-01 03:53:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09446ca7-f835-3c73-a90a-728c556648e6 | -3.94336 | -38.33433 | 2026-01-01 03:53:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5453fc73-169b-3113-9f63-9d0e91d80797 | -4.3104 | -39.37185 | 2026-01-01 03:53:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20979253-1d01-3ad6-8913-524c80f0c390 | -3.13587 | -40.11742 | 2026-01-01 03:53:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 52d70c51-152c-3c55-a0f8-f9bb289dee53 | -0.96382 | -46.78463 | 2026-01-01 03:53:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a7b51e4-18ef-323c-9052-21ef30c3aa6e | -4.31376 | -39.37237 | 2026-01-01 03:53:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 773435d5-da2e-3131-a707-de9b118cd25d | -1.488 | -46.03072 | 2026-01-01 03:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2582f22e-e654-3602-8cc8-216a71d506c3 | -9.52184 | -40.40941 | 2026-01-01 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a7e69adf-2a95-3ea5-861c-ca2f3e89d34a | -8.03851 | -37.4752 | 2026-01-01 03:55:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e6cdcc7-b402-3201-850b-62e31ca965c2 | -8.11641 | -47.99015 | 2026-01-01 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a621696-528b-3109-9a74-42c312f5c7b7 | -11.74488 | -41.31299 | 2026-01-01 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b6eb4a7-970d-3263-aad3-70eb63c3f6c5 | -9.57373 | -44.59647 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f92520b7-de47-33c9-a3b0-e2965110d1d3 | -6.59313 | -35.17086 | 2026-01-01 03:55:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9998d11a-1951-3610-af73-6b20ed757c6b | -9.56898 | -44.59958 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cfc20a4b-c27a-3609-a576-0f4c93ef8439 | -11.51874 | -40.36694 | 2026-01-01 03:55:00 | NOAA-21 | VÁRZEA DO POÇO | BAHIA | Brasil | 2933109 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 64d1dfd0-9f7c-3a95-b26b-0a3a17c06165 | -8.11348 | -48.06532 | 2026-01-01 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c86bac54-7611-3bff-9894-de5b707ceae8 | -6.42421 | -39.64416 | 2026-01-01 03:55:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5439ce3a-a287-3d8f-94c7-ed0adc741379 | -9.57784 | -44.59714 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 678f24c3-54bd-3e01-aee1-daebc59652b5 | -9.5772 | -44.60093 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 37a10b35-4cce-378a-ad64-a45d3008a8a6 | -5.59216 | -46.36553 | 2026-01-01 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adf5796d-7087-3371-873d-32ebd723f9cf | -6.59847 | -35.18482 | 2026-01-01 03:55:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d4148294-b104-3b64-804a-239cd23ef22a | -6.16062 | -48.03711 | 2026-01-01 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a27624db-6786-30d8-8838-8f61ae70c790 | -7.05995 | -35.20242 | 2026-01-01 03:55:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63db1a3a-47f6-3ad9-ace5-5d7d50ed32fb | -7.8873 | -34.83217 | 2026-01-01 03:55:00 | NOAA-21 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| aecb6695-103c-3301-ac91-fabff0c214cc | -5.72479 | -45.04107 | 2026-01-01 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 23b3dbb6-8678-3db7-9f43-e8aeaecef9b1 | -5.0505 | -43.60752 | 2026-01-01 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de4d4666-67af-35f4-bb40-7e236bb6899c | -6.29696 | -47.00047 | 2026-01-01 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 793ee706-ce8d-32b5-8feb-0128f5337dff | -7.05956 | -35.2042 | 2026-01-01 03:55:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a2447803-1d4a-39e6-92b3-31173109aab1 | -4.60093 | -45.99265 | 2026-01-01 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b1df5661-5df2-3bc6-85bb-50311e31d18e | -9.95532 | -50.28829 | 2026-01-01 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b312837-b36b-356d-867e-ba6386e1fefb | -5.84452 | -39.09472 | 2026-01-01 03:55:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c1005bf0-7cd4-3744-b14b-ec3f279565ac | -6.29749 | -46.9974 | 2026-01-01 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae947376-5fa7-3ec8-9ee8-9219c0b09457 | -9.19045 | -40.5588 | 2026-01-01 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b271a1d1-9ab5-335a-9b11-cd71b5a0b214 | -6.06004 | -43.73815 | 2026-01-01 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 810aa8cc-28c7-30f3-b142-58e834098373 | -5.04637 | -43.60679 | 2026-01-01 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecd72493-c811-35b3-a743-22002a2c168e | -6.59613 | -35.1757 | 2026-01-01 03:55:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4b1352ef-862d-3a15-91b6-4ecabf07bb69 | -10.71277 | -44.15126 | 2026-01-01 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 328ef64e-dfe2-3891-b07a-e9c02d2c93b8 | -9.57245 | -44.60405 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dc7e9dba-656a-358c-acd3-44754c07f8d7 | -7.99109 | -35.25368 | 2026-01-01 03:55:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f13f2c2-cf66-32b8-8cc2-236cc38b2efa | -7.39219 | -35.10774 | 2026-01-01 03:55:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0c5252a0-c608-349b-89f8-d16ffbab32b9 | -4.52908 | -48.66008 | 2026-01-01 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56366563-2082-37bd-8ffb-84cd43ee71d3 | -5.59325 | -46.36727 | 2026-01-01 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6c14e62-1e84-34c7-bceb-68e3e674355e | -4.40878 | -40.69321 | 2026-01-01 03:55:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ba3936d7-8720-3e17-a534-9bf16ebee89f | -5.36368 | -35.47295 | 2026-01-01 03:55:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 071c12bd-6954-37d0-802e-751d75bfcaf9 | -5.72402 | -45.04555 | 2026-01-01 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1630c4e6-fe24-3aae-b786-baf622973314 | -8.11488 | -48.06527 | 2026-01-01 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d4dfe96-f675-3295-9765-5baba7a06c08 | -9.52402 | -40.40972 | 2026-01-01 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f216ef45-fe19-31c7-834b-6503118c22a0 | -6.55179 | -35.29818 | 2026-01-01 03:55:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6618fc8a-5a33-3bf0-b767-c343a8a334f6 | -6.42143 | -39.64009 | 2026-01-01 03:55:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2f1a8e59-a530-3161-a683-f7c29a76fbe7 | -9.95618 | -50.28391 | 2026-01-01 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9900c678-4e39-3a82-b66d-a6eee6ec67a4 | -7.89885 | -38.44831 | 2026-01-01 03:55:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 64ca8bef-1277-37b7-b06b-12716239ea44 | -6.6021 | -35.18547 | 2026-01-01 03:55:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8a36272-68d3-35f2-8a55-9d5b3500b56c | -10.7699 | -40.41151 | 2026-01-01 03:55:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc764d97-f2cd-3480-9ae0-3218eb195249 | -6.59249 | -35.17513 | 2026-01-01 03:55:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 01407676-d1d3-315d-8747-823e0ff06d0c | -7.78362 | -40.43671 | 2026-01-01 03:55:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b975708-71d9-3766-9e39-1c229e9dbf22 | -9.19104 | -40.55518 | 2026-01-01 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ec7064a-f4e6-3a0c-b1a8-2d01f598d2af | -9.58604 | -44.59863 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ee40710-9b65-388c-a81a-cb193d43c2ea | -6.60273 | -35.18126 | 2026-01-01 03:55:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8fc8b882-86f0-3146-a986-15f0261c57ac | -8.45753 | -35.69073 | 2026-01-01 03:55:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 214ca48e-face-37e6-8b4b-013160a60ab3 | -9.57309 | -44.60025 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 83829cc1-6744-35d8-85d4-543861664c20 | -8.1141 | -48.06197 | 2026-01-01 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45dc0d0f-623c-328a-be3f-0b3da742b087 | -10.76993 | -37.14256 | 2026-01-01 03:55:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9bdcef0-b72a-3825-a917-ed48bcf775c3 | -5.52911 | -36.26834 | 2026-01-01 03:55:00 | NOAA-21 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a27f5b1f-d1d1-321a-a34e-26ca5ae4153e | -4.5284 | -48.66409 | 2026-01-01 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37f0e049-ccce-3b60-bafc-1c43da44f5d3 | -8.11547 | -48.06191 | 2026-01-01 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98515659-103a-32d1-bcf3-2db7160af06f | -6.16121 | -48.03371 | 2026-01-01 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d19154b2-e4d8-3d9c-bbe5-c65fe4d6e431 | -11.8868 | -40.49262 | 2026-01-01 03:55:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d4de442-4453-3982-86e1-04f6621f65f1 | -9.56833 | -44.60337 | 2026-01-01 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6cc9bbb5-00b3-3a1d-a9df-ab0da83b2839 | -6.42086 | -39.64363 | 2026-01-01 03:55:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
