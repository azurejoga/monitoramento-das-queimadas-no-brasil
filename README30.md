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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 065bbab6-2bcb-3c14-8031-29e03a01154e | -4.8178 | -45.8429 | 2024-10-31 04:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| f0ae789b-a096-3942-ac67-e11b0f357e8a | -6.1416 | -43.9563 | 2024-10-31 04:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b2708bee-6ad1-35c6-bf38-7ad0f4b29024 | -9.7226 | -36.0805 | 2024-10-31 04:46:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 860a4b3d-ff14-32a1-b5e9-dcbf634f3683 | -9.7419 | -36.0772 | 2024-10-31 04:46:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.0 |
| b3479bb4-9467-3ef7-9907-1182cea472ac | -3.40132 | -41.64131 | 2024-10-31 04:46:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cc2e24dc-80d5-31e6-8a89-7c380d2b127c | -3.39615 | -41.63637 | 2024-10-31 04:46:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 96025525-9736-3347-844d-f944a875b5bf | -3.39555 | -41.64042 | 2024-10-31 04:46:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 09778725-458e-37b4-a1ff-63782604435c | -3.39495 | -41.64443 | 2024-10-31 04:46:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a744caac-d395-304d-92ad-5b8baabaa942 | -3.93991 | -41.48755 | 2024-10-31 04:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f1cfe5cc-e574-3912-a42c-715c40edf12b | -1.56756 | -45.47644 | 2024-10-31 04:46:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 492e72f4-e317-370a-b66a-6efb91eae02e | -3.13186 | -44.47979 | 2024-10-31 04:46:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7b1f286-1304-382e-930d-ce2cbc4961e9 | -3.1312 | -44.47723 | 2024-10-31 04:46:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7426aa51-f188-325c-acbf-fc6ca9129cc1 | -3.13041 | -44.4823 | 2024-10-31 04:46:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1f6455d-4872-3c9e-90b0-04680cba487f | -3.12786 | -44.47399 | 2024-10-31 04:46:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3eb5930-6286-3b53-97e1-0375f3ef4664 | -3.12711 | -44.47908 | 2024-10-31 04:46:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d01d5a9-33dc-3f25-b40f-07f64d7a4596 | -3.12645 | -44.47652 | 2024-10-31 04:46:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d1fbddf-38ac-3220-9e17-8be64dbe938a | -3.12636 | -44.48417 | 2024-10-31 04:46:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 973be987-47af-3c94-a5b8-e9c598545525 | -3.12567 | -44.4816 | 2024-10-31 04:46:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2962c70b-96c2-3e58-9cf3-e01ed5cb3f56 | -3.12236 | -44.47837 | 2024-10-31 04:46:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a9e136e-9780-3f80-84e6-d5396e42e7ba | -3.26097 | -45.97227 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8679dc84-32bb-36c9-977a-e50a4495e203 | -3.25669 | -45.97158 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e35da88-1446-3f52-8d94-9ccdfb333055 | -3.24549 | -45.82892 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04c4f3e7-301c-37a5-8250-1d15d0356ed0 | -3.24484 | -45.83307 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c0ee1f6-de73-3311-952e-d6ec0e986415 | -3.2429 | -45.82716 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c51d3811-2318-308a-875b-d8ef9351b1d9 | -3.24229 | -45.8313 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afe19709-ebf8-396d-ab46-193560ace18a | -3.24116 | -45.82827 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f62f7a02-9d9a-3f82-9653-c1fe419da914 | -3.23857 | -45.8265 | 2024-10-31 04:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9101dc8-0381-37c0-a7d6-e615ae00e19f | -3.01396 | -45.49145 | 2024-10-31 04:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 550aa669-8e95-3dbb-bcc3-ad97aa7fea9b | -3.01332 | -45.49575 | 2024-10-31 04:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5da79710-366e-3e25-9181-c2b89f4ac008 | -3.00955 | -45.4908 | 2024-10-31 04:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 17581705-36fa-3b8d-8be6-6987928eb527 | -3.0089 | -45.49509 | 2024-10-31 04:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2c4c5560-b8f5-3f8e-9b6f-b6b1d338302c | -2.91911 | -45.66928 | 2024-10-31 04:46:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c75e6f94-7257-379c-ad76-0e7abfb34e59 | -2.87272 | -45.82734 | 2024-10-31 04:46:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e33f952-d401-3b98-8d8c-056c2d53fe84 | 0.08262 | -49.87003 | 2024-10-31 04:46:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17381132-5012-3cec-b8d9-c44da7945d0b | -1.94515 | -47.03729 | 2024-10-31 04:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f77d220-1e14-3285-b40c-fb6eb29867ae | -1.78423 | -46.91206 | 2024-10-31 04:46:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c74d4c8c-2301-3aea-9df9-5764be5c8eb9 | -1.78403 | -46.90883 | 2024-10-31 04:46:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f18b5c3b-b0ad-3569-a350-8216716c0ea8 | -1.78327 | -46.91387 | 2024-10-31 04:46:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c15b72c0-ef82-3f13-9476-54cdd43a5097 | -1.59991 | -47.13904 | 2024-10-31 04:46:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6be9da76-90e6-313f-848c-506547a76a5f | -1.59916 | -47.14387 | 2024-10-31 04:46:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11b6f7b6-fdbb-3ca6-a444-5d35dee6f38f | -1.3264 | -46.60042 | 2024-10-31 04:46:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5979f21-a8a3-36a2-a6b1-f2dc2aba21d4 | -1.24927 | -46.60931 | 2024-10-31 04:46:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e96c9a7d-1946-3e0e-8c48-4ef6246ab48e | -2.84488 | -46.69024 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6757a07c-7071-3544-a0ea-a7b47704551b | -2.84434 | -46.69379 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eeff0874-280f-3a16-814f-b668267fa51c | -2.8438 | -46.69736 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d6b8a8b6-1990-38a6-b05e-ac7ed5bba409 | -2.84137 | -46.68605 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 101e0a44-388d-3e00-99ed-60009cc27e0a | -2.84082 | -46.68963 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 16ddd87e-b472-31d3-b223-230e5c873218 | -2.84028 | -46.69318 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e8bdba63-8b92-354a-a490-0d41f02be8de | -2.83974 | -46.69674 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d98d5da9-5eb7-3e76-8ed5-ac9fe512d3aa | -2.83919 | -46.70031 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d96b597-a1aa-328a-abaa-91afe333a6b1 | -2.83731 | -46.68544 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f90b1303-aa19-3b7e-a6f8-165ce019d753 | -2.83676 | -46.68901 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ce8998b-d678-393b-ba0a-81adb17286e1 | -2.83622 | -46.69257 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d197b62b-ec6b-38db-8e68-bb3ee87ff3df | -2.83568 | -46.69612 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f3e5b44-adba-3f4f-acaa-a30311f02da0 | -2.8327 | -46.68838 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c30cff7-7982-3979-8c7a-35805d58cfea | -2.83216 | -46.69194 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 348462d0-08b0-3c8a-a95d-aa4adac8e72b | -2.72196 | -46.70419 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaf57bbe-0b57-3ce4-bc14-1009bb2d24ef | -2.71737 | -46.70715 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f0e911e-a56a-30f5-9121-b556c8ad3434 | -2.7171 | -46.6816 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 317e0464-c368-3c5e-91bd-834db3ead427 | -2.71656 | -46.68518 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c30fb17e-e8e3-3b06-ac50-b484962d434c | -2.45422 | -46.90656 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c3a503c-f09c-314c-ac44-5f35451ee055 | -2.44971 | -46.9094 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 546d34aa-eba0-33f5-8bc1-0b1ae5a7e807 | -2.4492 | -46.91278 | 2024-10-31 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6f87c7f-94f9-3ee0-bf75-63cb8a5fb8db | -2.27554 | -46.49476 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 008dae4a-03f7-3aed-a218-c8dab3e296cd | -2.27518 | -46.49437 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fff58cf-6996-35f6-9db0-8747f0578f39 | -2.27497 | -46.49837 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b42d825b-6943-3a4d-9600-24e772073d67 | -2.27464 | -46.49798 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c19245a1-4b17-34df-8787-26725c8ab5c1 | -2.27147 | -46.49409 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57352768-d47e-3bf7-ac9f-113a804e10a8 | -2.27111 | -46.4937 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe67cc30-1d10-3096-87c8-38ab0f22aab9 | -2.2709 | -46.4977 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 319a5903-1917-3ffc-a961-da5089986d47 | -2.27056 | -46.49731 | 2024-10-31 04:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6eee112-6eea-3d44-9f93-d5367e590c7b | -2.17113 | -47.95447 | 2024-10-31 04:46:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c92b79b-6b23-3776-b546-5dff12a4e1bd | -1.96579 | -47.95372 | 2024-10-31 04:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a281c912-03c6-3ba8-9e81-821d327d9b33 | -1.96208 | -47.95316 | 2024-10-31 04:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c284399e-5c78-32be-8456-1b9a56292ca0 | -1.96141 | -47.95754 | 2024-10-31 04:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34d335b9-d706-3bf1-b89b-5aa20de1d560 | -1.665 | -47.76797 | 2024-10-31 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 839af83a-a625-33c6-829a-050b084a32b8 | -1.66431 | -47.77244 | 2024-10-31 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4041c529-4b54-3ba7-a7ee-fca7c6047881 | -1.66126 | -47.76741 | 2024-10-31 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 90d27957-58d4-3bd5-9821-81b70fdbb3ad | -1.66058 | -47.77188 | 2024-10-31 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc4d0ea6-bebe-3f06-b706-46a18b0b17bf | -1.346 | -47.75232 | 2024-10-31 04:46:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db31615c-8225-34e1-90fc-947188b8731c | -1.2857 | -48.45283 | 2024-10-31 04:46:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b006e85-233d-3aa1-8947-16aeaa69a7ec | -1.27424 | -48.09711 | 2024-10-31 04:46:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 041493b3-850b-3bbd-9c0a-607440c87743 | -1.13203 | -48.3882 | 2024-10-31 04:46:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad70cc42-3ab6-3f79-beba-bf26f6ee1e7f | -1.05377 | -47.63589 | 2024-10-31 04:46:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8dfd8f4-68d9-3a88-91d0-028d5d382cf5 | -1.27466 | -47.23968 | 2024-10-31 04:46:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7a3ebc1-e4c9-344c-8488-b32e07bdf048 | -1.14207 | -47.31761 | 2024-10-31 04:46:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6afd7366-dc4c-3d85-b897-13bc51fcffcf | -1.13899 | -47.31236 | 2024-10-31 04:46:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5237f30b-bbf1-3f80-aac2-8280d97a55a5 | -1.13826 | -47.31699 | 2024-10-31 04:46:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71fb2479-ff41-3b89-93e4-af491dca8332 | -2.91474 | -48.61509 | 2024-10-31 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 542cb9b8-10d5-3d0c-98c5-fd29c03c48bd | -2.91047 | -48.61869 | 2024-10-31 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92cf4aff-9cba-3770-af00-fc57f7ffda0b | -2.90685 | -48.61814 | 2024-10-31 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e591f2c-63fa-3d73-85dc-69fe447ccf92 | -2.90388 | -48.61342 | 2024-10-31 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d84c2ca2-a8c0-3180-934e-18fdbe85b9cd | -2.90323 | -48.61759 | 2024-10-31 04:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5ef7acf-141b-33be-a1c6-f0455ce7343b | -2.88673 | -48.28819 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9f273d4-e0d4-37ea-a087-86c5b7d5ed71 | -2.86057 | -48.46012 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 930a4215-7bd5-3ef1-ab0a-7d0591870f19 | -2.66754 | -48.12911 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3dcf4ca-844b-3c2c-a6d5-5766c117dabe | -2.66586 | -48.12625 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f86a721f-c9b5-3f9e-a3fe-2e8aa49c23d8 | -2.5276 | -48.46193 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9006da67-ff4d-3458-a1ee-fb40d570a7c2 | -2.52696 | -48.46614 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be67c209-230e-3953-8db2-7966b1f73ff2 | -2.52631 | -48.47035 | 2024-10-31 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README31.md)
