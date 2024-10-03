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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f45f06f-0774-35ad-bac5-2780d80f0ca7 | -9.0097 | -67.38721 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17a8ee0e-77ca-3a79-839c-b932bd5e0761 | -9.00894 | -67.5298 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c51a2d1-bbcf-3310-8abd-5d016a8730fa | -8.99879 | -67.81285 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f040d142-84fd-368e-bf20-ad322e982645 | -8.99378 | -67.81192 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad910a2-906a-3ffe-bac2-623043d2494d | -8.98792 | -67.40927 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 91cd26a3-ad3e-3f68-8a67-2e30a260cc13 | -8.98596 | -67.42033 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbc0c19d-3f53-3c51-9aed-453ecaf4e85c | -8.98304 | -67.40839 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 529658f7-9b9a-32cf-944e-f435ae576393 | -8.98206 | -67.41389 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ed6dc0c4-d356-3b06-9025-f74e720356f0 | -8.91856 | -67.38941 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29a71009-ab95-376b-ab99-5d6b1e0e7347 | -8.91369 | -67.3885 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 784bd293-1655-3bb9-af74-ddbcb1cf7c5a | -9.36622 | -68.2033 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa4d505-4e6f-35c4-8ba8-5ce73c9ec1a6 | -9.36567 | -68.20634 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 337b1572-76ae-3cb1-9388-34c23d57c88e | -9.36056 | -68.20537 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a44778a-f618-335c-8da0-ef6a4cb9f27e | -9.36001 | -68.2084 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e06dc8e9-e1de-3ddf-b834-6ee48609d85c | -9.35545 | -68.20441 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5cb1ad2-a37e-3411-9579-4d745517aa87 | -9.35489 | -68.20746 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a51692-eb98-37b5-8957-355c86ff01ef | -9.32767 | -68.24057 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3056657d-8efa-37d9-9a87-69a35844768d | -9.3231 | -68.20782 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b57a0af5-01d8-30f3-b238-8085ef440add | -9.32254 | -68.21089 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c813db81-36ac-3b43-85ba-cf1bcf8ec53c | -9.32197 | -68.24274 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df799355-f313-36a9-b1ca-1437cf9f5c72 | -9.27783 | -68.36624 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d97a7939-b556-3713-b682-4d81cb17f9d7 | -9.25174 | -68.83205 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4691c512-9d04-3899-855d-d0e31233d2b5 | -9.24639 | -68.83111 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8261aa99-a496-3481-8d0f-c8f3a1826c0d | -9.24578 | -68.8344 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d0aeb2-daec-38fb-8ad1-4cbc04bdad24 | -9.21696 | -68.16723 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 928d55ef-6a0c-3a38-bced-6cb747bf441e | -9.38089 | -67.83707 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93a07dec-3eea-3642-9d58-8ffcf61210fa | -9.35861 | -67.39373 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9443bcad-2729-3120-ad53-d6aad6766928 | -9.28426 | -67.82913 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10b0ba3a-e269-33bb-ab7a-680c71d3500a | -9.28163 | -67.84351 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6347a8b9-8487-333d-a5cd-3902d2a2d10e | -9.27718 | -67.83961 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a117343-b853-3ddf-bd1a-9e08c40210f0 | -9.27665 | -67.84247 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 505e08e0-22e9-3364-b802-f8cd214e14f5 | -9.27365 | -67.88708 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 96b2a90d-2b80-3c62-8322-cc5af33e9684 | -9.27094 | -67.8174 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00f1cac2-2f22-3617-92cb-4c64c7d9877c | -9.26919 | -67.88316 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a2d9260-201f-3e4e-a9bb-32f17e54ce3a | -9.26866 | -67.88607 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e674598f-d667-3ac8-bd62-7151b1177b5a | -9.26489 | -67.82221 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cbb5a28-17c3-3ece-8595-e97ac2626912 | -9.26471 | -67.82426 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d87d2fa5-3ac4-3886-9aaf-63f77804f000 | -9.26418 | -67.88224 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 918c12b5-bd52-3866-b83a-ce9dd1fd8046 | -9.26327 | -67.60188 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8538c97-df0b-3905-a062-51fd68840f0b | -9.26023 | -67.82044 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cb68551-6cbc-3fd1-9335-3094cc74f20a | -9.2599 | -67.8213 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 028dbde4-d76c-3072-a7de-72ee6edbd6a4 | -9.25937 | -67.8242 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f3eab18-680a-3a7d-90ac-4196ee8cdaeb | -9.25835 | -67.601 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44b9f3b1-8d1c-331c-98a4-2390f32fc601 | -9.25524 | -67.81952 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 614be1ff-e29a-3d9e-b2cf-b6f6cdb01561 | -9.25491 | -67.8204 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02ec0bf3-0206-3a35-a61f-8a4e3bf3408b | -9.25473 | -67.82242 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ba73d6-6bab-306c-bdaa-8be3da6e492b | -9.25437 | -67.82329 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 279c62a3-1b63-3ece-9fc4-79a60953ef0f | -9.25025 | -67.81859 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad344cc7-41e3-38a0-b057-41d6905d89f4 | -9.24578 | -67.81473 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c00303ae-6b0a-365a-a232-8b53348a17a0 | -9.23158 | -67.63673 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88680021-676d-366f-afd2-22ebbbfb3ccf | -9.22665 | -67.6358 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63d00013-3ee9-3565-b5df-4b8637863e15 | -9.22479 | -67.81678 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4364ca48-f404-3c91-a741-d316113eb93f | -9.22078 | -67.78173 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7104e779-cd71-3b1c-99be-a059f7e58619 | -9.1914 | -67.85869 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9da6c178-dfba-3a11-8877-12884cd507bc | -9.18692 | -67.85484 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 877fbc60-d4d6-3693-9360-21dfb2b3e77a | -9.09833 | -67.51182 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3af4c4a5-a522-317f-83e0-53b323e64bd5 | -9.09736 | -67.51736 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f102c7cf-dae7-3b93-a1ec-66a9a523343b | -9.09426 | -67.51653 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6cd0e85-62cc-366b-ad7b-2f19c90d8144 | -9.09344 | -67.51088 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5e7bccab-9046-3127-af10-8ff7339c4fb2 | -9.09324 | -67.52209 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a78bfcbc-11f0-38c8-9e21-b952beb335f7 | -9.09148 | -67.52202 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b612f89-6c53-3f86-bd0a-893c89148857 | -9.08163 | -67.57793 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49646e94-d228-3b59-8b5c-48217dae4015 | -9.07624 | -67.6701 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7c0f31c2-84c3-352e-ae39-6b029284c3e3 | -9.05648 | -67.86233 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ef79b5e-6b82-3794-b53a-e116be64fe78 | -9.05594 | -67.86527 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0109d877-9932-3332-b02e-78ac9054e474 | -9.05146 | -67.86139 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7806985-39ea-3b2d-82d1-057d51d3e236 | -9.05038 | -67.86729 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 528d658b-2095-394c-831d-03921ad24751 | -9.04984 | -67.87024 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf235baa-daf7-3582-b861-13af6f2beca8 | -9.04443 | -67.50177 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5365d98-d29b-3ac1-9ca3-b746e5769c82 | -9.04053 | -67.4953 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a0375cf-5262-3867-9a17-f408b2dd195c | -9.02205 | -67.4156 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69997f8a-b532-3096-88e9-fe72c455ddef | -9.01578 | -67.74696 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 08bc75e8-2983-314f-8fda-ceec4e580353 | -9.01526 | -67.74984 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5bd514b-931f-3c9f-86b0-56626c565b9f | -9.01456 | -67.38813 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29e48e64-5103-3ae4-8f7f-4e42c87b3bbd | -9.0143 | -67.44476 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8604462-c7bc-3d8f-9786-ec6f78551b6b | -9.01236 | -67.44227 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d98aeb5-8f14-3f10-9949-7c3e0aa26d95 | -9.01131 | -67.74313 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 061babcc-2cfe-39e8-a8b8-704a43317988 | -9.01079 | -67.74603 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2de8ebc0-2623-3bd4-add1-fd2902185d15 | -8.98694 | -67.41479 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ddd3126-57dd-3029-bed2-452a03521feb | -8.98692 | -67.38643 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97456559-4b92-3b92-8ffb-c6f446d6173f | -8.91677 | -67.38482 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed9e2b89-3db9-3f18-93f4-c60f41d9da76 | -8.91577 | -67.39029 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fa80bb2-409d-3b18-8955-64a2f60e06d1 | -8.83756 | -67.39163 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f06fb877-e3ab-3027-99cc-6af3313bdd23 | -8.83169 | -67.39619 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a4bb57b-9161-358b-8dcd-acb25699e3c1 | -8.8278 | -67.38979 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b81d77b-e84d-3115-8cdb-855eccde88e3 | -8.77261 | -67.69509 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0108adb1-f982-3c40-9269-56c7f65279af | -8.77208 | -67.69798 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f2e6622-c022-3a8f-bfa8-abbc559bffa3 | -8.77156 | -67.70087 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cd484a1-d9a5-3aa6-a196-b04785a7c3d9 | -8.77103 | -67.70377 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a895adbc-c422-3c67-8969-1f2ca6da7e6a | -8.76762 | -67.69418 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fefee75-d3c2-3075-abe5-7eb951bb87c9 | -8.76709 | -67.69707 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48e47912-f7df-30df-bdfd-d51f094e4375 | -8.76657 | -67.69996 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc0759bb-7519-3e12-8b5b-79e900373f88 | -8.76604 | -67.70286 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8960f3b-a0b3-3105-a061-cad3c170b1d2 | -8.76552 | -67.70575 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d1e112d-8ffd-3743-b759-b00ab13eafac | -8.76499 | -67.70867 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09e54b00-a412-3b92-9f68-474ca832cc97 | -8.76157 | -67.69906 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8a0a222-2351-37e6-bd9c-cb424adbe353 | -8.76105 | -67.70194 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4287ab22-e4d5-3ac0-9485-99abe0ea50de | -8.76052 | -67.70483 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 261caf3d-8418-35de-a125-1c612f0fef03 | -8.75999 | -67.70775 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a7af527-4c83-3e46-a821-48130bdbd434 | -8.75946 | -67.71065 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README155.md)
