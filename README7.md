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
| 8a3da120-352e-317a-8f9f-c92f0b0c9fb6 | -1.93614 | -45.43484 | 2025-12-11 03:49:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e36b891-6f96-3b8b-acda-91015309e01e | -2.21489 | -45.6683 | 2025-12-11 03:49:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9232c84-14b5-3f5c-a575-f4f8a1350bf4 | -2.28863 | -45.60086 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23a9c08a-68eb-3b26-be50-ee823ad4ed38 | -2.28795 | -45.60075 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f36233c7-e344-38af-b663-fe5bf1cb9248 | -7.77605 | -37.89275 | 2025-12-11 03:49:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b1411a0-2310-36bf-9663-7b4de64cc8cb | -9.83257 | -36.05716 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 36038076-30d0-33da-adb3-7d283cd623b3 | -7.86675 | -38.72663 | 2025-12-11 03:49:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bfbf3a68-6657-33ac-8aef-7dceb06afa0c | -12.28175 | -38.419 | 2025-12-11 03:49:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6e540452-23ca-3f31-b796-f31a604a0fcb | -7.50281 | -38.82224 | 2025-12-11 03:49:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c56c5312-5b81-3455-b15e-2c55e1df15f5 | -7.91423 | -37.59973 | 2025-12-11 03:49:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06c3b6e4-7870-32ad-aeec-f1771ab287d8 | -9.83368 | -36.04986 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 4dfc4e57-507d-3b8e-94c7-33934288cdf1 | -2.28308 | -45.59996 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 107a5441-dc4a-32a9-9e38-dc9aa8416d09 | -2.20076 | -45.44545 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fae61967-08e4-3654-9e70-584167d0399e | -3.1265 | -40.23223 | 2025-12-11 03:49:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0af2f2c8-e282-3b0f-8099-fa3452a22939 | -13.2153 | -41.93072 | 2025-12-11 03:49:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bd8d97d5-20af-3de5-bfe3-d3c2fc1d84b6 | -10.02296 | -48.12181 | 2025-12-11 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7567537f-be0b-36ec-b221-bf211a77043a | -9.83595 | -36.05769 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 23146ceb-559e-3b1d-8c7b-0d7636a5051b | -1.69268 | -46.55081 | 2025-12-11 03:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8100a66c-87a7-356c-aba9-3cc0b3e4afa0 | -10.02196 | -48.12228 | 2025-12-11 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6424fb29-6a9f-37f8-a31a-6191aae74ef6 | -1.74998 | -45.60122 | 2025-12-11 03:49:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 013c5b16-ab77-3ce2-ad15-d37e5ac061b3 | -10.02767 | -48.12353 | 2025-12-11 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c030e322-2431-3489-a263-046a9729afe2 | -2.21161 | -45.41436 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45efa0eb-0e0d-3ff2-a455-c892085d37ff | -10.47649 | -50.65675 | 2025-12-11 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8a4d62f-b78d-37a6-8ebb-c32cd79999e1 | -2.19484 | -45.44453 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ad94512-504e-3065-97d6-09125a0bdfc6 | -2.22046 | -45.66924 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 086b58a0-f5a2-339c-8357-40a3dea1be56 | -1.42861 | -45.6629 | 2025-12-11 03:49:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4dda21e-132e-3606-a8cf-7e1c0757abb9 | -9.38013 | -40.75308 | 2025-12-11 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3e74a77e-8d5e-3a4a-97d6-c46ff829190e | -9.86685 | -36.0138 | 2025-12-11 03:49:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a1aa77eb-170f-3227-94e2-03dda157c090 | -9.31171 | -36.95012 | 2025-12-11 03:49:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 011e7ef6-0c09-3489-b007-5e722501bbd9 | -2.21152 | -45.41073 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b29bef9-e2d3-368f-81fa-db1bc9993e3f | -7.86337 | -38.72607 | 2025-12-11 03:49:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c9c527a0-6dcc-3bb9-a962-9ce22783eba2 | -9.8303 | -36.04934 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| db6acfd2-bc7d-3dc5-bde4-ad10efc6c2a6 | -2.99618 | -41.7848 | 2025-12-11 03:49:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2f5eaab7-db6a-3dac-b59b-614ad1bf4059 | -7.86278 | -38.72971 | 2025-12-11 03:49:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2afbe4eb-861c-3311-820f-af785cfc39b5 | -0.85662 | -48.64834 | 2025-12-11 03:49:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f3fc9c3-dbfe-3b2f-b4cc-0b700ec4b1a7 | -10.56427 | -36.78239 | 2025-12-11 03:49:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 184abedc-ed75-34b9-80e6-025a6132d02b | -1.20029 | -47.53365 | 2025-12-11 03:49:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8329bac1-6be9-36a5-99fc-ddcc99e67446 | -9.45264 | -40.56321 | 2025-12-11 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16e0d3be-873c-3b25-9ed9-5b56d3eaf819 | -1.75115 | -45.60369 | 2025-12-11 03:49:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca38f8b-a2a0-3873-8626-088d39f09ace | -10.48025 | -50.6585 | 2025-12-11 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1d884ba-4a72-3f4a-9ac3-5a2034466bff | -9.82919 | -36.05664 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| fd2f1c21-4c39-3ecd-9334-c3ae0a77124d | -9.86347 | -36.01328 | 2025-12-11 03:49:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d9a4b10a-4628-39d4-b320-9f0aa154ac3e | -2.29105 | -45.65032 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71fb87fb-b84f-3b76-b954-430ee9473954 | -9.74829 | -37.68095 | 2025-12-11 03:49:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a3aae6b-dbe3-3819-853a-d87de840ac16 | -7.6254 | -39.06597 | 2025-12-11 03:49:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 984774e6-126c-3e45-b581-8904f534b3e7 | -10.56373 | -36.78595 | 2025-12-11 03:49:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fad243ad-a247-38f2-94ae-0119380a7fe9 | -9.86008 | -36.01276 | 2025-12-11 03:49:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7dda322f-0fb4-30a0-8be5-edc007ab5758 | -1.75174 | -45.59995 | 2025-12-11 03:49:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77ac4434-9860-37fe-b6db-b8e9038d3fe7 | -7.43722 | -39.01323 | 2025-12-11 03:49:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0261216-ebee-3358-8110-29ac319b41f9 | -9.83085 | -36.04568 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e6d0eff7-c0f4-39e0-a8de-da98c2443a55 | -2.20033 | -45.44547 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf133eb-8598-36bf-905d-b9b22cbfec18 | -1.19942 | -47.5388 | 2025-12-11 03:49:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0236a020-ca82-3018-ad9d-5b570674bf24 | -9.16492 | -40.10926 | 2025-12-11 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 596900a7-c944-3169-83b7-b10761cfafd3 | -12.28415 | -43.54222 | 2025-12-11 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb9acca1-b44c-3307-90d8-68744deb325a | -9.16844 | -40.10984 | 2025-12-11 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ed518bbf-3ace-319a-b1aa-54af49760af7 | -1.68938 | -46.55161 | 2025-12-11 03:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44dac79b-6de3-3d57-972c-db97b6990134 | -10.4736 | -50.65725 | 2025-12-11 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9f4b2ec-1a31-364d-837e-9d83dfbb88b5 | -1.75558 | -45.60207 | 2025-12-11 03:49:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da19143b-416b-3682-b2df-cbafc0b9a8aa | -1.43363 | -45.66759 | 2025-12-11 03:49:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01ade744-e779-3496-a926-6db0b7065e0d | -11.66794 | -47.125 | 2025-12-11 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fdc6ecf-d46f-386e-926e-1bf7ea7980e9 | -9.83651 | -36.05404 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| f3ba5449-d957-349a-9025-99cd1f9e76f0 | -10.39265 | -36.59449 | 2025-12-11 03:49:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 562507b0-3941-352c-be31-9de03aa04be5 | -1.93555 | -45.43845 | 2025-12-11 03:49:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 062570bf-60af-316c-8f67-859093f18945 | -2.21095 | -45.41429 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dea00cb-f9ab-3ca8-be5a-aff24843da45 | -7.62823 | -39.07023 | 2025-12-11 03:49:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8c98b47b-2af7-35a6-96fd-97c352749329 | -9.83313 | -36.05351 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| e6e778b1-1faa-3312-a0a6-5cae9bc981ee | -8.23407 | -37.75116 | 2025-12-11 03:49:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 488cc4a9-a762-3ac9-a143-be4e00afdc2e | -9.80441 | -37.73626 | 2025-12-11 03:49:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 949169f3-5541-351d-b6ea-663e54b61be1 | -2.28856 | -45.59711 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4590736b-d8f8-3910-b33e-f940da004b88 | -8.38847 | -35.45612 | 2025-12-11 03:49:00 | NOAA-21 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ccb60939-f0dd-3b5c-871b-abe84efa0817 | -9.82692 | -36.04881 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 9718fac3-752c-34d4-9566-022a845adc48 | -2.28921 | -45.59722 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ecf5a073-0430-357e-8506-6152114f1bcd | -2.21221 | -45.41082 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2742a7b8-5b95-3d3d-af0f-8d7d4a24c0c3 | -8.65703 | -35.99349 | 2025-12-11 03:49:00 | NOAA-21 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 064f32ee-d2b1-383f-acfb-4257caf4149b | -2.29661 | -45.65124 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b042e2a-325f-37eb-ae8e-d8c547738e5c | -9.41053 | -35.64743 | 2025-12-11 03:49:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| af62077f-106f-3551-9ae0-2dd52e5c15e5 | -9.82864 | -36.06029 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 5cad4f25-c408-398e-9ce2-61ae76ab517c | -12.73611 | -38.16804 | 2025-12-11 03:49:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 675d6994-a5be-306a-af6b-a329201b13a4 | -6.0315 | -43.7105 | 2025-12-11 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 457a50c1-88ef-39de-b146-8962249c4b73 | -16.69766 | -44.96306 | 2025-12-11 03:51:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3e9f84f-6e32-33cb-ac0b-37c0f25d938b | -16.70181 | -44.96385 | 2025-12-11 03:51:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48c046e1-0968-34a8-ad50-a8ebb7a7cee7 | -16.70524 | -44.96865 | 2025-12-11 03:51:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30475f68-7fd7-3c51-8b27-8ab18430e31b | -16.69896 | -44.9638 | 2025-12-11 03:51:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a1b1d0a-e4a4-39f4-958d-c49ba677aaaf | -16.70311 | -44.96459 | 2025-12-11 03:51:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86301be5-4450-3a40-8c7b-6373f3ca014f | -16.70596 | -44.96468 | 2025-12-11 03:51:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a6922b1-fa8c-3859-98a3-d8eedd3b110b | -22.96653 | -43.56437 | 2025-12-11 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 98b6b117-3da2-39a0-b4c9-91b263b68595 | -26.25753 | -48.55895 | 2025-12-11 03:53:00 | NOAA-21 | SÃO FRANCISCO DO SUL | SANTA CATARINA | Brasil | 4216206 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8a4ec15-c0d8-39e9-ae93-7bbc7fdf5b43 | -22.68162 | -43.25433 | 2025-12-11 03:53:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5a9b967-f5af-3541-8459-6c773fcedf24 | -23.39847 | -46.29668 | 2025-12-11 03:53:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 993cc6e2-4c0a-37b3-8ee0-f4abcfc7e8d7 | -23.59847 | -46.41665 | 2025-12-11 03:53:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b58591b4-c43e-356c-99c7-842c016e5445 | -23.3838 | -46.41661 | 2025-12-11 03:53:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1735b4e1-7931-3946-b91c-cbd2591e7172 | -6.0315 | -43.7105 | 2025-12-11 04:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 09eb68e2-6789-3d56-b975-782c7b9194c3 | -6.0315 | -43.7105 | 2025-12-11 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 674d3465-8205-3311-9a93-2a15608c51d6 | -3.7589 | -45.4944 | 2025-12-11 04:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 6c0fe97f-a5f6-3228-97df-91a5c65e44ef | -1.69047 | -46.55097 | 2025-12-11 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c1c3342-eda2-3106-8785-3efc88f630f7 | -1.30272 | -46.11806 | 2025-12-11 04:16:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d9cfa07-fa09-394e-8b6b-e550fed9837e | -2.28719 | -45.59641 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dee15a4d-424c-325a-94e5-1a2649824ecb | -0.64798 | -52.39398 | 2025-12-11 04:16:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9beeed-353d-3d78-beae-d7ae6e8f7043 | -2.23646 | -45.68201 | 2025-12-11 04:16:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e890f5bc-2a44-3af9-8d2b-c8166aa02534 | -1.19985 | -47.53822 | 2025-12-11 04:16:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README8.md)
