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
| 831a04fe-6947-3c45-b784-ff218a4e4561 | -5.26318 | -37.60738 | 2026-01-02 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 11f750e1-f254-3e06-8e6a-b6e559d68417 | -6.75416 | -35.22461 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4438a8fc-6e58-366f-84ca-c732745419e8 | -6.75753 | -35.22514 | 2026-01-02 03:36:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fc436cb0-0899-3382-b7ac-3b11a45d6a12 | -5.93321 | -43.4018 | 2026-01-02 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d79b0595-6ce4-335b-8f9c-bb561f3129bd | -7.8167 | -35.32433 | 2026-01-02 03:36:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 54976ba3-df10-38af-823a-165eddbf0153 | -5.72443 | -45.04124 | 2026-01-02 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0cf62abb-17cf-3401-8911-121dc3814699 | -6.75869 | -35.22893 | 2026-01-02 03:36:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44eed717-0d23-3047-9315-fcbd2a014b05 | -5.28516 | -35.7592 | 2026-01-02 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5455ec60-c7a0-3efe-be9e-f38d3f54253a | -6.73956 | -35.22959 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2cfb218d-c8c9-3d35-b260-32c049ff53f3 | -7.4547 | -35.20048 | 2026-01-02 03:36:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 25dc070c-0eac-391a-8752-64f2da98ee69 | -5.28392 | -35.76685 | 2026-01-02 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 61f3ef6e-592e-3be7-9f64-2cd8ea728ff9 | -7.39332 | -35.16133 | 2026-01-02 03:36:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 163623c9-c86d-3bf1-9f4d-34d6bb7b450f | -3.52863 | -43.66618 | 2026-01-02 03:36:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd1e3a11-9678-3d0c-8b15-4b2705a56c98 | -6.75927 | -35.22532 | 2026-01-02 03:36:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 806e8137-e376-39c4-ad60-48cf6f1ec149 | -6.29646 | -39.60162 | 2026-01-02 03:36:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be2fb70d-cbd1-3b56-a466-fc11ea92e41d | -3.5279 | -43.67041 | 2026-01-02 03:36:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0bdd5d1-3365-3d8b-bba3-45407c9c0c10 | -6.75359 | -35.22821 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 36.6 |
| a2d691ae-a99b-3132-9eae-f10de766d902 | -5.52564 | -36.26757 | 2026-01-02 03:36:00 | NOAA-21 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac169f93-3f07-3187-bc80-bce6ab7ecbed | -4.77291 | -37.82808 | 2026-01-02 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cfe21d59-af80-3723-b278-911e213e7c0b | -3.52875 | -43.6721 | 2026-01-02 03:36:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeed522c-b4b0-3dae-97db-90e9cfe59ce7 | -5.96275 | -35.4577 | 2026-01-02 03:36:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d06c6fbb-e7b8-333c-8010-81dfe1e41c21 | -7.22483 | -34.82938 | 2026-01-02 03:36:00 | NOAA-21 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b0b5167b-0c8d-3693-b0d7-de81548a6f90 | -6.74743 | -35.22351 | 2026-01-02 03:36:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c696290-d905-3710-ad7d-54f756f44a19 | -10.40206 | -36.87669 | 2026-01-02 03:38:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b34d8221-5c07-36b7-a6ed-9fb7ee102cd9 | -12.69694 | -39.73909 | 2026-01-02 03:38:00 | NOAA-21 | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2defb1e1-1d96-3b09-b4ed-837a18a32cf5 | -11.7507 | -43.64385 | 2026-01-02 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c852872c-4a01-3a4b-8495-dcbc2c8b8722 | -10.09813 | -36.45393 | 2026-01-02 03:38:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dd42f5a6-23ab-327a-9043-924ca92709ca | -9.69231 | -35.94939 | 2026-01-02 03:38:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1801d8c3-2e34-3f50-9ff6-c263f553ace3 | -10.23217 | -36.34255 | 2026-01-02 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0df4633c-b987-36e4-b27b-b94352c4ff85 | -10.3986 | -36.87611 | 2026-01-02 03:38:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3c6c3a4f-b317-3aae-96f8-d9617e715bc8 | -8.69881 | -38.6465 | 2026-01-02 03:38:00 | NOAA-21 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 70290dd8-d4f4-3b5e-af9f-0cbc3df1510b | -8.69965 | -38.64166 | 2026-01-02 03:38:00 | NOAA-21 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d594e32e-5950-3aa2-8911-5fa25eb18743 | -8.7035 | -38.6423 | 2026-01-02 03:38:00 | NOAA-21 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 5fdaed8d-c7b2-3200-bc13-d7fb10b170af | -12.95418 | -41.18158 | 2026-01-02 03:38:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 873d9665-f761-3a8d-a05f-142f64e629a5 | -9.69075 | -35.94933 | 2026-01-02 03:38:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 195f4575-f69f-3aa4-8fde-17d2dacc3aae | -10.09345 | -36.35378 | 2026-01-02 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d36b321-74d0-30a9-a97f-576a47e3ff5d | -8.69579 | -38.64101 | 2026-01-02 03:38:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fca4876e-99d2-30a6-ac73-f5f421745b8e | -10.40143 | -36.88054 | 2026-01-02 03:38:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2a5e2c91-63f2-349c-81e1-5894a8e226ee | -10.09685 | -36.35435 | 2026-01-02 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b55f857-0dca-3909-9672-c3c79bb92189 | -8.706 | -38.64047 | 2026-01-02 03:38:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| edc513a4-6173-3774-9f3e-54ab73fb8521 | -8.69828 | -38.63916 | 2026-01-02 03:38:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e74ee770-3791-3448-aa1b-3cd671fd58d0 | -8.70134 | -38.64468 | 2026-01-02 03:38:00 | NOAA-21 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0be0220a-6a1a-3551-a18d-4cf2bb429831 | -16.53646 | -39.60815 | 2026-01-02 03:40:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f422fab2-414b-318b-971c-eccd79fc47d5 | -18.48903 | -39.86716 | 2026-01-02 03:40:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f48dc20b-9e06-3171-ac5a-1f5f7bdbcc2a | -17.06243 | -41.23812 | 2026-01-02 03:40:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ee4cceb-ab56-3164-8786-1a4923adf91d | -18.48542 | -39.8665 | 2026-01-02 03:40:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b40e7063-66e9-32fe-91d5-d0cea4839a59 | -15.30172 | -43.86562 | 2026-01-02 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e24a758b-0b83-3691-a5dd-611bb5265c74 | -17.05774 | -41.24136 | 2026-01-02 03:40:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 02a9f3b2-8adb-30fa-9d64-7c873f71a319 | -17.05851 | -41.2371 | 2026-01-02 03:40:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8f100fb8-2ab9-3e84-abd2-bdc69f4db0e1 | -18.22626 | -42.64972 | 2026-01-02 03:40:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8382d845-5e6c-3158-b212-d00f95dca037 | -6.5631 | -51.1126 | 2026-01-02 03:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b1cac543-de05-313c-aa8c-84b42dd0d87a | -6.5631 | -51.1126 | 2026-01-02 04:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c8fc2caa-c8e2-331b-84d8-e8b15322d29a | -0.8679 | -51.96804 | 2026-01-02 04:04:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb8eab0f-0c36-3a7f-8e02-f527b711e0eb | -0.86895 | -51.9617 | 2026-01-02 04:04:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40e940ed-49dd-3ad0-907e-716fa417879f | -1.0701 | -48.88695 | 2026-01-02 04:04:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4f8cb72-3518-35a4-9dbb-1768e6dfef8c | -1.5228 | -45.8095 | 2026-01-02 04:04:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ec3349-4dfc-3926-8873-a487b4387fdd | -1.75747 | -45.69224 | 2026-01-02 04:04:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0260dec-d32a-3172-96ad-935c2de11b5c | -1.07517 | -48.89177 | 2026-01-02 04:04:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccf9a11d-9de3-3e6a-9397-bb31f4023b38 | -0.08929 | -51.27652 | 2026-01-02 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98e9daf8-a55e-38ef-8e05-b02873888f67 | -0.09298 | -51.27939 | 2026-01-02 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adfadb94-1cd4-35a6-a687-4a7daca49fd5 | -1.06441 | -48.88601 | 2026-01-02 04:04:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d524f657-181d-3978-bc0b-979e36620793 | -6.42769 | -35.24941 | 2026-01-02 04:06:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ea0c7aa0-0274-33d9-8d82-58a5a14d26f8 | -6.08923 | -37.39917 | 2026-01-02 04:06:00 | NPP-375D | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e9ed5f6-c8b6-3d54-a52b-4c4715304331 | -6.29565 | -39.60101 | 2026-01-02 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0b904c6-341f-3085-8e6e-f093a1f336db | -6.02027 | -44.54912 | 2026-01-02 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b3a8f11-c89d-3ffa-87fb-02a91904e362 | -6.02305 | -44.55177 | 2026-01-02 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 076db240-304d-372c-8655-689eba0e4490 | -5.72318 | -45.04007 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72b0dd86-f39c-3f03-be97-d11716e8e933 | -5.93343 | -43.39967 | 2026-01-02 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca6ea348-9096-36c8-aaf1-e69220729147 | -5.72452 | -45.0335 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b3ea9813-fdb0-3a9a-bf50-795e8db35376 | -8.70118 | -38.64206 | 2026-01-02 04:06:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf67c922-ab57-3032-aa29-d6f766866a4c | -8.69716 | -38.64529 | 2026-01-02 04:06:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0135b00a-8959-381f-b502-ecb4319e8297 | -5.71927 | -45.04004 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca0f16bb-5f7d-38f3-88ba-534cba78f593 | -6.29233 | -39.60048 | 2026-01-02 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2e30e89-a317-30a0-8962-1ba1d651196a | -6.01912 | -44.55114 | 2026-01-02 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afa4487a-f422-384e-a43a-766089b3bba0 | -6.74663 | -39.27423 | 2026-01-02 04:06:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67e115be-60e4-31eb-8668-b3988cf3de42 | -7.81661 | -35.32406 | 2026-01-02 04:06:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 64c826fe-d189-3542-9717-b0c47ab92892 | -3.53439 | -41.07024 | 2026-01-02 04:06:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1ff5465-f675-37e7-82f0-2553e57ed93f | -5.26568 | -37.60963 | 2026-01-02 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e694db8-239e-3cbc-b31d-77b29de87a1c | -5.72379 | -45.0365 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 67d2895a-994a-3d00-8bdd-c325f2dec1ce | -5.92975 | -43.39909 | 2026-01-02 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1e09a01-f1c0-3b1e-80b5-72dbf85b4faf | -7.46348 | -35.19286 | 2026-01-02 04:06:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| dd325495-5b47-3160-a631-b7a45e87ba0a | -8.70462 | -38.6426 | 2026-01-02 04:06:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 89791d05-6a87-3d6c-ab38-ff0cc88a9d34 | -5.28466 | -35.75988 | 2026-01-02 04:06:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1ee517d7-3058-38ef-85ef-292661f91634 | -6.35844 | -35.32081 | 2026-01-02 04:06:00 | NPP-375D | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a76b6c1a-8d1f-3829-a9df-5b63cebad7d1 | -7.09577 | -38.78683 | 2026-01-02 04:06:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 80d30f9f-1e2f-3f04-85e0-a67888dc05d1 | -6.01945 | -44.55419 | 2026-01-02 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04004287-2f22-3d62-80bb-b5094680b0fb | -5.7244 | -45.0329 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 01347135-89ec-3876-938f-ac7695c3adab | -3.52385 | -43.67219 | 2026-01-02 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a9a845c-e608-3b9c-868c-a221a48823b9 | -7.4594 | -35.19228 | 2026-01-02 04:06:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 26b2a57d-3748-3669-869b-541ffb3cab98 | -5.74438 | -35.37576 | 2026-01-02 04:06:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 51b9371a-8e23-337d-b9d9-8e65b3856d05 | -7.45835 | -35.19939 | 2026-01-02 04:06:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 864d3130-e36b-3b77-92dd-279cfb9cd9ec | -3.52849 | -43.66803 | 2026-01-02 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d38664dd-b6f0-37d8-a10c-8668a30ff6ba | -6.98712 | -34.91775 | 2026-01-02 04:06:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 86d3475d-eb24-3445-b857-212e8be4b7c6 | -5.23919 | -38.13267 | 2026-01-02 04:06:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1a183528-6ad9-3c76-9472-b5ab05c5252e | -7.45888 | -35.19582 | 2026-01-02 04:06:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6b7f4347-0441-371e-8bbf-b3f49d36ad43 | -5.2628 | -37.60528 | 2026-01-02 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6357e79d-21f0-31af-845c-915dd6531116 | -5.40447 | -39.46141 | 2026-01-02 04:06:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 05dd371c-f886-3380-9568-c102d6986b82 | -7.68916 | -35.29173 | 2026-01-02 04:06:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 50163520-17f3-3567-a235-17298c850fd3 | -3.53235 | -43.66862 | 2026-01-02 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebc555f9-7823-398a-ac26-f32950f03067 | -5.75248 | -39.79842 | 2026-01-02 04:06:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
