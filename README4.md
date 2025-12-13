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
| ec03ac80-f231-3908-a6b0-5f0d5ce0e5d1 | -12.27043 | -38.41269 | 2025-12-13 03:12:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9bdba4e-fc02-3d26-a413-ba50eb3dab2f | -9.49916 | -35.94225 | 2025-12-13 03:12:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5c38c05c-4429-383c-b286-492e81a43d35 | -6.78415 | -39.62383 | 2025-12-13 03:12:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 19c64b1b-42d1-336c-ab28-e2aec600f7d7 | -12.26973 | -38.41633 | 2025-12-13 03:12:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ddded597-5a85-39a1-9f2e-717c73a93e56 | -12.2714 | -38.41291 | 2025-12-13 03:12:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cc6c1ed3-1471-3da6-94e4-75cf1cae0791 | -7.63555 | -34.85651 | 2025-12-13 03:12:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 6f9a320d-9c7f-31aa-9ef4-d936aaa2b220 | -12.27517 | -38.41748 | 2025-12-13 03:12:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 79230bfd-b452-3ef4-bee3-bc9316dbd472 | -12.27068 | -38.41652 | 2025-12-13 03:12:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b84f3d76-e388-3ecc-93e0-161dc52b37f0 | -6.78425 | -39.6263 | 2025-12-13 03:12:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 80435bf4-1018-35f0-89fb-06231070748c | -9.49677 | -35.93869 | 2025-12-13 03:12:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 25294391-57ef-30a2-9b25-c750cecaa506 | -10.29544 | -37.80466 | 2025-12-13 03:12:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ded7cd8-383e-3b8f-ae0c-9ec114820996 | -8.0513 | -43.1001 | 2025-12-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 90c3859d-8d6f-3553-88f1-6a7b34a31c9f | -8.0321 | -43.1257 | 2025-12-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 1bec70cf-e455-3d9d-b584-03438177f455 | -3.2007 | -41.8678 | 2025-12-13 03:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 197.2 |
| d077b2c8-5bb5-3ab6-afbe-25f4e6630514 | -8.051 | -43.1237 | 2025-12-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 1ba8e6f1-bfe5-3169-9a81-e3a58255809d | -3.1822 | -41.8448 | 2025-12-13 03:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a1a1e18c-ecc5-3f33-856d-a5b1d8e87e82 | -10.235 | -52.2263 | 2025-12-13 03:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c0b9b917-73ba-3b30-9ac4-8ff76e5569a2 | -8.0324 | -43.1022 | 2025-12-13 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 2ccb4d26-ed3b-3e8b-8e83-69fd7677cff5 | -3.2194 | -41.867 | 2025-12-13 03:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 304148eb-66e1-342b-aa56-d9adee37e309 | -3.2196 | -41.8431 | 2025-12-13 03:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0a10d519-5cc1-39a8-91c9-60fbe277c6d7 | -3.2009 | -41.844 | 2025-12-13 03:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 52528782-62a6-3bc2-bccf-6dbf59715172 | -3.182 | -41.8687 | 2025-12-13 03:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 643660b6-6b18-3702-ac2e-6fe444039c1d | -8.0321 | -43.1257 | 2025-12-13 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.5 |
| b888244e-3d43-3b52-b589-c9f5e55b431b | -2.487 | -47.7692 | 2025-12-13 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 298e2327-da1b-3c28-8820-3ab8cf8ed386 | -3.2007 | -41.8678 | 2025-12-13 03:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 178.4 |
| ee7ec3bb-a4fb-33ce-904d-25232a62cfd4 | -3.182 | -41.8687 | 2025-12-13 03:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 41283d0d-b4b0-3b66-8398-e18c07eddd7b | -8.0324 | -43.1022 | 2025-12-13 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 4151d9f3-3534-3c13-8f7d-0c920a63a38a | -8.0513 | -43.1001 | 2025-12-13 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 82af8e81-2fee-369e-9220-5c5ecaca2a55 | -3.2196 | -41.8431 | 2025-12-13 03:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6fad277f-b459-3797-a6d7-f4e3c578ed94 | -3.1822 | -41.8448 | 2025-12-13 03:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| eab50708-c9fc-3793-b3db-f553588011c9 | -3.2194 | -41.867 | 2025-12-13 03:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 850483f7-9c40-3eb3-9c44-692c9d167010 | -3.2009 | -41.844 | 2025-12-13 03:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 223.2 |
| ba5f42a3-ae74-33f1-b9cc-c31b8b31b975 | -3.2194 | -41.867 | 2025-12-13 03:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8b2d0d28-c66f-3e5b-a9a8-3b9bf76dfbf5 | -3.1822 | -41.8448 | 2025-12-13 03:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a169a594-10ff-394f-b9ab-a6d7fc05dcdd | -8.0321 | -43.1257 | 2025-12-13 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| ed84c515-6825-3499-bb7a-15b70e410757 | -3.2196 | -41.8431 | 2025-12-13 03:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5214b872-08b5-3a23-92ee-0f1cfb1936a1 | -8.0513 | -43.1001 | 2025-12-13 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| cefaedd2-be91-3172-b9b1-97eb621795cb | -8.0324 | -43.1022 | 2025-12-13 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.0 |
| 25ab78ae-5411-362a-91fa-4a1984dd5c67 | -3.2009 | -41.844 | 2025-12-13 03:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 66206656-140a-3faf-a31a-961f88ff1403 | -3.2007 | -41.8678 | 2025-12-13 03:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 2ed13603-6746-37ee-8c79-b1e9e6eb6a9a | -8.051 | -43.1237 | 2025-12-13 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| afc54448-a825-3fe9-8eed-063c6e356c33 | -3.182 | -41.8687 | 2025-12-13 03:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 028be488-d6fd-3291-bd76-660310092ab0 | -7.38222 | -35.21934 | 2025-12-13 03:40:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 32bba430-5546-3f5b-8c84-f722bff10842 | -3.43816 | -41.64818 | 2025-12-13 03:40:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bee26b1c-2a40-3d14-8c42-609f6ee140b0 | -7.38281 | -35.21572 | 2025-12-13 03:40:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 613f1b0c-4fee-3989-8a20-36d0299e4c21 | -5.31603 | -38.00566 | 2025-12-13 03:40:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 41150b33-8cf1-3eac-a2df-e34f8be8869f | -3.47555 | -44.21123 | 2025-12-13 03:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5660f55-18dd-3b8b-b7a3-47bb7fa2b29a | -7.3856 | -35.21987 | 2025-12-13 03:40:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 42775697-a211-365e-93fa-62b5ca3c0f44 | -3.21112 | -41.85226 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 49218ec3-0de2-3fb6-b454-c6c35cc9156d | -7.47952 | -35.24612 | 2025-12-13 03:40:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 236eb5bb-68da-3221-b5bc-0baf7c3be052 | -3.20642 | -41.848 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c9557c68-2acf-38f6-8fe4-92e30d290d6b | -3.47539 | -44.20763 | 2025-12-13 03:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27d7147b-bd9b-331e-a7cd-451533a4d30a | -3.18899 | -41.855 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab90b890-52d3-303a-a371-576fe61318e0 | -7.29513 | -35.77539 | 2025-12-13 03:40:00 | NPP-375D | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 34eaa766-00a3-37fc-9867-f36801f808b9 | -5.07505 | -43.66903 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e81c11db-9f85-3413-9b5b-aa2fb0d36e7b | -7.63885 | -34.85513 | 2025-12-13 03:40:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 25df46be-8e23-3b11-90ee-350c9f7d87db | -3.20535 | -41.85439 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d1f69fa9-78dc-366b-b7b4-b5370a14f096 | -7.6316 | -34.8576 | 2025-12-13 03:40:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 81a4f0f4-392f-3a22-b3e4-98e73b9a6b89 | -7.63551 | -34.85459 | 2025-12-13 03:40:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 74b22055-81e0-371a-a322-209fb3cc340c | -8.17267 | -34.98109 | 2025-12-13 03:40:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b07547bf-b15c-30a6-9d7e-473ec063ca10 | -3.20372 | -41.86421 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45ae1839-51d8-3e7c-bb3e-4c1537a6d054 | -3.43246 | -41.65045 | 2025-12-13 03:40:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a6f08459-c875-364b-87ef-182c0252923c | -3.47634 | -44.20655 | 2025-12-13 03:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9ae5ff1-3fc7-3b4e-ab8c-c99f73b7a59f | -4.33053 | -39.14781 | 2025-12-13 03:40:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7021a8db-b812-3b19-a957-f2d69e81dd76 | -5.1966 | -38.49528 | 2025-12-13 03:40:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 91fe96c0-1a18-32db-9972-e84b54ec1f52 | -3.21058 | -41.85556 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d7da6084-6cf2-3424-b4af-d687757232a0 | -6.74261 | -39.66589 | 2025-12-13 03:40:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2dc317f-ae5b-3eea-86be-11b98752104b | -3.44709 | -44.73772 | 2025-12-13 03:40:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 545eab26-d3ed-3468-b75f-1cc6fae5d5e0 | -7.25177 | -35.11356 | 2025-12-13 03:40:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 260f2411-c6dd-36e2-bcf9-fcca2b1f9652 | -7.78558 | -40.4318 | 2025-12-13 03:40:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3cccd2b7-3ae5-378b-a01f-5e901c8f7117 | -7.47894 | -35.24972 | 2025-12-13 03:40:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3176627a-815a-3884-b011-a05859f33f08 | -5.07861 | -43.6824 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 013edf8a-b002-3a20-9e81-c7a166317839 | -6.56146 | -39.51444 | 2025-12-13 03:40:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5bcb13ab-7d82-379d-a87c-7493c2af0848 | -3.44796 | -44.73266 | 2025-12-13 03:40:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61a69882-14e1-3799-9a26-ea0da7b01364 | -7.5443 | -35.23079 | 2025-12-13 03:40:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 286bc33c-5e77-3d91-8117-95ff58e3b171 | -5.54556 | -41.65553 | 2025-12-13 03:40:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6b521e1-ad03-3e14-a775-4670bff13764 | -7.01226 | -39.63651 | 2025-12-13 03:40:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77dd5ff8-e7b8-3927-ab61-a373d165dcf0 | -7.54372 | -35.23437 | 2025-12-13 03:40:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bf7cd6c5-bd8b-3e88-9faa-0931abccac9f | -3.47621 | -44.20295 | 2025-12-13 03:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84449e12-c30e-34bd-a2a6-081406b51497 | -8.75507 | -39.68578 | 2025-12-13 03:40:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5d93e32-5eb2-3e3d-9676-83e1e1c428a1 | -6.95078 | -40.8142 | 2025-12-13 03:40:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fb7c5e34-eb7a-36be-b38b-217c74a3065d | -3.19427 | -41.85585 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 26565c3a-e5df-34ff-acb4-424806e9890a | -3.19317 | -41.86246 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1955a83-f41d-32ee-ae91-0fb2111907c3 | -3.20009 | -41.85347 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 1ecd04c5-3efa-36be-a08f-9e0395b19a97 | -3.20588 | -41.8512 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5350e84d-d371-304c-aa57-90ebacc34d9c | -3.20481 | -41.85764 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ddbc0835-62fb-3fc8-852f-d73dd6216e41 | -3.1979 | -41.86661 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e3944ab-7374-38f2-9284-ccebb21b16f6 | -3.20062 | -41.85028 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| e634e716-1a4a-3742-abc3-eb86dc81d427 | -2.78911 | -45.20967 | 2025-12-13 03:40:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da9b5d36-96fe-3e6e-98d1-7402ae8d261d | -7.21416 | -43.11275 | 2025-12-13 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3b21061b-ca36-3da9-bcb6-8d2675e41085 | -7.19721 | -40.10761 | 2025-12-13 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e406c1ce-6897-32b7-88c8-36bf12ac3d49 | -3.31811 | -39.35046 | 2025-12-13 03:40:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 332eb9c1-4ac1-3d9b-b382-ac01ac314eb6 | -7.54767 | -35.23133 | 2025-12-13 03:40:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2c8e932a-8d64-3a00-9ebb-d99fa197b52d | -5.07344 | -43.67907 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d9d6f03-4875-37bb-b354-57aa03ac40b4 | -4.70522 | -37.77534 | 2025-12-13 03:40:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f1c1c157-ec90-3e69-8d65-c167ecb9c176 | -3.47456 | -44.2123 | 2025-12-13 03:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dd2d96b-bb83-3cee-b9ce-c2681ec962ea | -2.6728 | -46.89585 | 2025-12-13 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bd46648-4f9f-3dfc-9794-4c716212e8aa | -5.01791 | -39.71971 | 2025-12-13 03:40:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5946de0a-7d59-30af-90af-05d1bf5ff6cc | -7.78853 | -40.43109 | 2025-12-13 03:40:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9fb51696-539d-3d57-8a06-81b0eb2193b6 | -6.78386 | -39.63076 | 2025-12-13 03:40:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
