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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7382a5ae-fa2e-38e5-b1fe-bb7c0763684d | -2.15889 | -53.73486 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34813bc8-dc30-35a7-bbe9-60a4df817401 | -1.18967 | -53.58661 | 2024-12-27 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 485cb713-3f71-364b-a128-1a9eb59af5ae | -3.76984 | -47.21162 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f80ee9-5c9b-3915-9e1a-b7fd8df6a83b | -3.19138 | -45.98828 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7341d552-38b5-3490-8f20-3e5b1b1469ed | -3.97764 | -46.68554 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79cad241-8ed8-3252-b6d6-6d82720762c7 | -4.04811 | -47.04026 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6f814359-83ed-3785-9d4e-3a61cc92ed04 | -2.72124 | -46.01436 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8851ad34-0ddf-32a0-a9ec-be9a4d23b37c | -2.35363 | -45.41897 | 2024-12-27 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fecdc8b-e347-3e89-b23e-9ec47bcb84a1 | -1.65137 | -45.87414 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| debe619a-2632-3c7b-a326-97af7d2f6ae6 | -3.91117 | -46.9166 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e1deb10-d5c6-3f3e-adc4-ab95496b2ad0 | -1.81297 | -45.57697 | 2024-12-27 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0040dc3-97f7-3e41-a0c4-ae64b7cc8a6c | -1.7149 | -46.20962 | 2024-12-27 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04a9063f-7c81-364a-b947-bf2372179141 | -3.40753 | -44.89838 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 057f7bad-51ac-355f-8b67-923256dcbde7 | -3.18115 | -45.92106 | 2024-12-27 04:31:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bb6474a-4583-39ca-92ec-74b12738c8fd | -3.23497 | -45.97313 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ab14e6ee-7aa2-3167-9421-00e0d38b75cf | -3.72735 | -47.18042 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43399efd-0dbb-39e0-bd2e-152e25c16540 | -3.9815 | -46.68257 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 976604b1-e9cb-3055-bb72-03bee5cd3546 | -2.25403 | -46.39589 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c6ebf89-269e-3ff5-a55a-95a30f46fb3b | -1.02359 | -47.63092 | 2024-12-27 04:31:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e545164-a8f2-3363-a098-e1d98415a589 | -4.16842 | -42.0323 | 2024-12-27 04:31:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6385a190-a501-3613-81ad-9275ae6da2a8 | -3.93843 | -46.98091 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62e5e93b-ed89-3c3a-a424-2e4a330024c6 | -4.5269 | -42.0606 | 2024-12-27 04:31:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 85cc5358-8ab3-3c86-848e-84015eb60578 | -3.02467 | -40.02276 | 2024-12-27 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60ac1b11-7c52-3e9f-ab75-b079e72e767c | -1.72547 | -46.229 | 2024-12-27 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04acb70b-9901-384f-bd48-e57f9d1d540d | -3.89989 | -46.98911 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfb5a2ab-4985-3af5-81ee-2b1d486ec1da | -3.21955 | -45.44489 | 2024-12-27 04:31:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6a6a1c7-fbf5-3588-ae0b-5225d67f7b97 | -2.76388 | -46.13626 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa2a9a32-0e7e-38e0-acd7-d63bbcd1e0b6 | -1.93913 | -45.18893 | 2024-12-27 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ab6ff2b-4038-3c8a-9d7b-a084e7490138 | -2.84939 | -54.09275 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43101639-cf95-3706-92dc-ace6d5a87824 | -2.63812 | -46.11287 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef82eafa-2ff5-3bd5-b7b5-39930bb71995 | -1.91372 | -45.5628 | 2024-12-27 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 756ce612-6303-3abb-876e-3af40db265d4 | -2.79063 | -46.72736 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c6a7167-f958-30e6-a29c-09ca8e238678 | -3.77037 | -47.20818 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c64b9dfe-2b7b-34ac-9355-ef8116b81b70 | -4.04534 | -47.0363 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 197203ac-bd02-34c4-91aa-a738bd13b221 | -4.03443 | -47.06285 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc9bdcc2-430f-3b53-9e4f-6e5d37e7e0cb | -2.73289 | -46.18176 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b4f6047-250b-30ba-abd4-141b5205930f | -1.9098 | -45.56585 | 2024-12-27 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 523aa668-05c2-3e50-8e7c-f2e5c78b1e4b | -3.93959 | -46.9952 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c929384e-a0cc-30be-8639-0823e8211ea9 | -1.95547 | -46.47677 | 2024-12-27 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0df83a08-49c9-375b-bf33-935ecb437121 | -3.94455 | -42.31249 | 2024-12-27 04:31:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 048795da-e34a-3e0c-a350-0fe17f3756a7 | -3.99037 | -46.69109 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee798afb-79c7-314e-ba76-37a674279a44 | -2.76497 | -46.12924 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af61989f-f488-33e9-81b5-5ea62364ee69 | -3.74833 | -47.19774 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3fdf060e-3228-3966-8ada-6ff175f01acc | -3.93458 | -46.98384 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f7228a2-9f5e-3ad5-9354-3a2215ced372 | -4.38588 | -42.14062 | 2024-12-27 04:31:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93a47299-9d12-3e57-bdf4-613e94d636aa | -4.0415 | -47.03925 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5075b9d-eb1f-3114-a572-d75616b679d9 | -2.72452 | -46.16972 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ff06d49-4e97-37f3-9788-201615b88d15 | -3.19865 | -45.98575 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f66ee48d-4b36-3687-90d0-41c596b389e7 | -2.25788 | -46.39294 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2450e119-2d9e-3619-bb56-5088b2a8e96c | -3.88238 | -47.01461 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5c2f8b-5afe-366d-bf9a-374927ac34e5 | -4.2483 | -41.92415 | 2024-12-27 04:31:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 093ed489-ef55-3b90-a65a-2c7a3673c5c0 | -4.0004 | -46.71399 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20c15d82-59b1-35ac-a9f6-7dcb4731cff3 | -3.98398 | -46.05455 | 2024-12-27 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72c2420e-02ea-39ec-bc0c-484da4857e53 | -1.65137 | -45.4604 | 2024-12-27 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 294ffba6-b37a-3a00-bbb3-ec266c529ffc | -2.53257 | -53.95846 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a1ae915-4770-3904-bc57-fad8725cc35a | -2.71898 | -46.00678 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72617ade-c534-3441-80e1-dba7d24c85c9 | -1.55132 | -53.50159 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2c65ce3-5876-3dfc-bf97-e6cc1dff2f8b | -3.10156 | -46.56696 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55b79c09-fe31-3446-ac25-b6bf752b5324 | -3.88595 | -46.94804 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| adf23355-486d-33e5-a436-04f6bd648ec7 | -3.90043 | -46.98566 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a954cbb-a33b-33aa-8442-b91546e62dd5 | -4.0583 | -47.10891 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e90170-18a8-30bd-a568-94fb5a009a65 | -2.28244 | -45.57873 | 2024-12-27 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be089f75-74a4-3456-9fac-35848b22960d | -1.55511 | -53.50655 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a8ceb1f9-2ff4-3513-a538-c996bb5c9fdb | -3.99977 | -46.69609 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d044c99-35c2-378a-924b-28fd3ba2bf6e | -2.73901 | -46.18628 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c220ba3-0d77-383e-b8b9-88104078db2e | -2.73352 | -46.02348 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 777b29d8-4856-3cd0-81fb-084d4fccf915 | -1.02691 | -47.63144 | 2024-12-27 04:31:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01352c0c-b5cd-3ea7-811d-1db2ae120aed | -3.82287 | -46.05927 | 2024-12-27 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47066020-c899-3075-b735-5780473d86ad | -3.98392 | -46.57947 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b990c5df-c737-3dad-80dd-e0d1faddf7fc | -2.25734 | -46.3964 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fbf2ab8-1862-3065-9c8a-0c73e49ed4f3 | -3.88899 | -47.01563 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bef1eca9-6d7b-3d25-bead-887e2b72da9d | -3.87854 | -47.01754 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f77e289c-2969-3c9e-b605-2d103b4886fd | -3.03741 | -40.11646 | 2024-12-27 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 33.4 |
| af97aeaf-a952-367c-9295-0ba614c21145 | -2.63265 | -45.94963 | 2024-12-27 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ed30393-fce4-3117-994d-661c0db5004f | -1.62504 | -45.84871 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1347b602-cc29-3a04-9846-fe0afec52833 | -2.63533 | -46.10884 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7fb5d0f-0322-363f-bfaf-f9d810a2832f | -3.02287 | -48.48517 | 2024-12-27 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5a7da26-7048-3bcb-87de-0c01a7afe47f | -4.0448 | -47.03976 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95848498-42e4-3421-a75c-653be544a9ff | -3.07001 | -41.89647 | 2024-12-27 04:31:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b92e8d6f-1b55-37b2-b4c4-a1ce37ccb8ec | -3.06641 | -40.08102 | 2024-12-27 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| dc7b8a0d-37e4-3b6a-a580-ba20724d0265 | -4.00309 | -46.6966 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e119ea47-be21-393a-8c39-a53f944f6f76 | -4.06365 | -47.07442 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e856cd-c0cc-38ff-ace4-95c1b37a7b40 | -4.52273 | -42.05996 | 2024-12-27 04:31:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1724b357-e574-32d8-98b0-97f2c71563ae | -3.04772 | -46.38791 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80f2c401-767b-380c-b4c5-a9c886a407c0 | -3.32997 | -46.7161 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4010389f-68ee-3aed-a878-006cb5242adf | -3.73726 | -47.18195 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6fe192e-1c09-3306-82db-ed4ebafced68 | -3.41451 | -44.89945 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| da25d93a-8d29-30ea-b247-77b1651d3fd1 | -4.05249 | -47.03387 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 980ea7c4-5713-3864-9ea0-b075462888b8 | -3.484 | -44.98112 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 050ee1ca-d68c-3a01-92c7-44295a3f8cfa | -2.87566 | -45.23878 | 2024-12-27 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4d5a1b3-1130-337b-98f6-f79f9a1dd5fe | -3.90427 | -46.98273 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb0f52ad-b6bb-3e68-a361-51b679fa05e7 | -3.98869 | -46.68008 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9ad824b-fc68-3760-a259-6de5342e5d71 | -3.88184 | -47.01805 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 754a28be-1bb2-3998-94de-d6034a4f3493 | -2.73018 | -46.02296 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 033545a5-d6d0-3736-abb5-411e014c1315 | -3.88195 | -46.53474 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4796724d-62e5-3b7f-8fc5-0d335096d189 | -4.16897 | -42.02855 | 2024-12-27 04:31:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e4beae72-1092-300b-b16c-944478f54a9d | -4.00372 | -46.7145 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 897f8cc6-ff44-3e4c-acb4-4e38f96e0254 | -3.23217 | -45.96905 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51e56ce-8dfc-3e60-b30d-1e2946ee8587 | -4.05196 | -47.03732 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e211feb4-e5d8-3c2b-a88c-1a2c1593949d | -2.50098 | -49.05798 | 2024-12-27 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)
