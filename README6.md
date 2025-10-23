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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae8dc3f0-8f4d-3cef-b47f-e441dea04310 | -12.0036 | -46.7667 | 2025-10-23 03:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| eef69cce-716f-3cb3-a94a-ef2bf69f5439 | -17.5967 | -46.6182 | 2025-10-23 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a46f328e-1695-30ef-8210-e3e13cfc2e74 | -17.6173 | -46.5906 | 2025-10-23 04:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2df7d27c-d4f4-35bc-9664-e8529b3557a5 | -3.0169 | -49.4694 | 2025-10-23 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 308c7d00-515e-36bd-9253-9d82ad0139c4 | -17.6367 | -46.6098 | 2025-10-23 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| b67a9a9c-16f1-3e6b-b2c9-a4ac0d409d53 | 0.3773 | -50.9413 | 2025-10-23 04:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 40.0 |
| de3c32e0-20fd-3b21-810d-ea845b351d66 | -17.6167 | -46.614 | 2025-10-23 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 367.9 |
| 595b63f7-d17a-3881-b100-1d95af70d74c | -17.6161 | -46.6373 | 2025-10-23 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 131.5 |
| eb4d2cea-96f8-3a9d-9309-1d5f118a4bc0 | -3.0168 | -49.4906 | 2025-10-23 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| dd402b34-48e3-31f9-8334-4c78ed40241a | -11.3643 | -49.7995 | 2025-10-23 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2076448c-8f2d-33db-b7f9-046225e69d50 | -2.25347 | -51.92394 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e287f54-ff86-305d-84ca-8f175f19a450 | -3.38743 | -44.74035 | 2025-10-23 04:06:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6e20fca-14b3-3277-932a-235cb713e4ab | -3.02325 | -49.4857 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b2c4f4b4-dac3-3f75-b053-3f5c256d23d4 | -3.05292 | -48.71048 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e77368d-9669-3f63-b3bf-1130d7ad2391 | -3.11625 | -45.23139 | 2025-10-23 04:06:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a947c1e8-0944-3b43-ac6b-e6a3e2380347 | -5.54045 | -41.36252 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ff3eea4-9178-3948-898d-3670747de80f | -3.68031 | -47.63129 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64e0dca8-6c7d-3ca9-bc60-21f30d8b6cd4 | -3.22203 | -49.3644 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a1975604-432f-3c36-a04b-ec1d3b871afc | -3.14818 | -50.16891 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3145e3a4-601d-3106-9ba6-48f685ff5109 | -4.70612 | -48.12461 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ab5326f1-d408-3d55-8a83-27f79ea903d9 | -5.79302 | -35.59865 | 2025-10-23 04:06:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cf55e078-1cc8-330e-80e6-c9254c0e1ad3 | -2.85936 | -50.73994 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a51f8db3-faf7-3e30-a831-7ac0b71e37af | -2.8557 | -50.74627 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b412b46-fb1c-3a45-af6c-c7b4d14ec710 | -3.6961 | -49.56733 | 2025-10-23 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1505f450-ffbb-3b25-aa54-b4ab2dd0ca85 | -2.73372 | -48.28858 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7409eec5-8e1a-3ca7-8870-2ade59b07c47 | -5.84628 | -43.64794 | 2025-10-23 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bd1b14c-47ec-3dd9-ba8b-8ddce19b870b | -5.43856 | -40.88556 | 2025-10-23 04:06:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fd63ed8e-faf3-3236-9b36-85dc6b8d0685 | -4.8912 | -39.80729 | 2025-10-23 04:06:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b28949b1-b313-36f2-a634-7025ed2a8d9e | -2.25428 | -51.91914 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c31d6e61-1223-33a7-896a-cf7c3001b32e | -2.44354 | -49.374 | 2025-10-23 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f62100f7-291a-3c12-acbc-a2e2d9365de9 | -3.02846 | -49.48653 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8577df7a-e5a1-371d-861e-a4672d7324a6 | -2.99238 | -39.96452 | 2025-10-23 04:06:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 241bdf74-0358-3046-90b8-fa67e67f2a16 | -3.98796 | -47.882 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bd5098ca-a659-3d8f-afb1-963ba543edfc | -6.30672 | -41.88042 | 2025-10-23 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 51c9013b-16ec-34b7-8acf-622f6a47f119 | -2.83657 | -48.55764 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f458b91-cd4d-3f1c-bb04-7723fc1cb0f9 | -2.87205 | -40.42803 | 2025-10-23 04:06:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b07fc00a-6f4e-378c-aade-06c552b9712f | -3.33177 | -50.22614 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53ca5e85-1458-3153-8722-72d87a062720 | -3.79768 | -40.84071 | 2025-10-23 04:06:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 239faf1e-3aa9-3138-b0e3-f3d7e32ad108 | -2.80417 | -51.34745 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4aaf44-d32e-3d71-a8ab-832afc1244c5 | -2.86201 | -50.74329 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1105b4b-52ac-33f5-8926-276449332637 | -4.41424 | -42.13717 | 2025-10-23 04:06:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6043b639-a763-3b81-86d4-31d7ee67445f | -3.98823 | -47.88094 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf701ee1-f144-3eda-8a78-4789a231c88a | -2.87259 | -40.4246 | 2025-10-23 04:06:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 61b5c89f-9365-368a-9d9b-345d5902f192 | -2.869 | -50.71759 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43aca15d-173e-3df9-8f84-6124962fb12c | -3.83318 | -51.29885 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a29d683e-fc2f-3888-8822-bb7c6d1f3c91 | -5.44082 | -37.62627 | 2025-10-23 04:06:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 242d3bc5-ba6b-32ee-9884-21b0c544eda0 | -3.01806 | -49.45244 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 95ff693f-5b0d-3057-9097-d0825ba61026 | -3.94685 | -46.96729 | 2025-10-23 04:06:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4768e0e-d200-3aeb-8c6b-fc295d6899ca | -3.81758 | -50.77145 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf8d550b-900c-3a0d-b1cd-2a8cbcd8ebce | -2.90601 | -48.98069 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 142c5508-d07f-3f5f-b763-7718378ba0aa | -3.95117 | -46.96798 | 2025-10-23 04:06:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99d95671-3ef6-3825-a903-28148ee269e4 | -5.37018 | -46.87313 | 2025-10-23 04:06:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c18ab0f-c7e9-36a1-a3a0-4482533471d4 | -3.12051 | -45.23511 | 2025-10-23 04:06:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 05ff13ff-ada8-318a-9dc9-204c6833b446 | -6.89741 | -38.27192 | 2025-10-23 04:06:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 00a80870-4fc5-3489-9e1a-6ade303f06e1 | -6.55654 | -38.49099 | 2025-10-23 04:06:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9954fe12-2426-3f72-b304-01b6cee6963e | -3.41598 | -51.43388 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0fffc98-2a52-3c3f-91eb-3accdb178931 | -2.2473 | -51.92291 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33f7b48d-d5e7-3ecf-b469-d92af587eea5 | -3.6961 | -49.56732 | 2025-10-23 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f7ae85b-d5fc-398c-89c3-d645d0e70d10 | -4.81442 | -48.64351 | 2025-10-23 04:06:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01cf6c20-6f00-3b94-ab75-db6a3de999d5 | -3.05292 | -48.71049 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2df56ab6-884a-35f6-964b-751395e93272 | -3.48812 | -43.98761 | 2025-10-23 04:06:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bba5d8d8-ac8d-30b0-896f-4d2dbc927af3 | -4.29223 | -49.2758 | 2025-10-23 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6035c325-0e3e-3e53-a25c-466365b3382b | -3.11357 | -51.20991 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fcd3828-8e3a-3969-aa94-61f88f52cc5d | -3.34982 | -40.42278 | 2025-10-23 04:06:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 78aec6f8-8315-35a2-9952-cf8df344078b | -5.79218 | -35.59998 | 2025-10-23 04:06:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d3b01daf-9865-3866-a938-ef3c04c63e9e | -3.0248 | -49.47634 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b790ab3b-6cf7-338a-bbed-be933eb5e463 | -6.32438 | -43.62057 | 2025-10-23 04:06:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de4773f0-9c40-3b96-97bf-35b1e0d33cfe | -6.9004 | -38.27663 | 2025-10-23 04:06:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d86f8fcd-ba23-303a-a584-4a430e2f3d02 | -2.24758 | -51.92559 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b5243c1-70ad-3352-8b30-73afc6eb771c | -2.87598 | -50.71074 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b68b115-d407-36d0-9bcf-48ee4433a499 | -4.42891 | -40.17779 | 2025-10-23 04:06:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 98d05918-dba4-317d-98af-798ff75457c5 | -3.02377 | -49.48255 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 61298634-4f49-3df9-b053-00338e87f964 | -6.30617 | -41.88388 | 2025-10-23 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c0aa3f5b-d771-3c70-8e33-ef9f3c720b65 | -4.33199 | -46.79279 | 2025-10-23 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b4206b-30ac-386f-bfc1-f35dc33c60d1 | -3.98741 | -47.88578 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f7fbb27-499d-3a4a-a8de-6e3562dc1fdf | -2.11304 | -47.1037 | 2025-10-23 04:06:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1d69523-c1ff-3708-954d-1964800b49ca | -3.48518 | -43.98286 | 2025-10-23 04:06:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c8dc1c7-1b6b-3dca-8c89-9898ea16d37c | -3.48878 | -43.98343 | 2025-10-23 04:06:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c806b87c-0eaf-39ac-977c-a66689f9a2c7 | -5.54974 | -41.34636 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 941c2ade-2f00-35d5-8334-dc727d0147a3 | -6.10309 | -39.66427 | 2025-10-23 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3fb78a77-005a-3b27-b2fb-6e8befcf7f5a | -3.2504 | -50.13522 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef073c2e-70cb-302c-a0a0-6f48d2cb0d31 | -3.85191 | -43.96124 | 2025-10-23 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc2b26a-c1ab-3293-985b-43a45a42ac1e | -2.72457 | -49.56536 | 2025-10-23 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ab18df-46df-3de1-bb59-43a2c209fd09 | -3.70183 | -49.56497 | 2025-10-23 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76d32633-134a-380c-a588-50131c0d0a0b | -5.47406 | -47.13598 | 2025-10-23 04:06:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6f538c2-af7d-3ee1-ae23-fdafd9894608 | -3.48945 | -43.97926 | 2025-10-23 04:06:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0dac22cf-10d7-3cd5-a527-48111a318351 | -2.92795 | -48.30181 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1ba65b98-1655-3641-a22e-cbc8ed1fa40b | -3.22718 | -49.36523 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5616c1d9-54e3-3bdb-8bd1-c28e41d21c88 | -5.69015 | -45.97161 | 2025-10-23 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3705e2cb-eba6-36a1-94a0-cff36c0cf6c3 | -3.48945 | -43.97925 | 2025-10-23 04:06:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1ad18c12-06af-3520-9220-c75ee69aaf15 | -2.44354 | -49.37401 | 2025-10-23 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c0dbcc9-303e-39c2-a7ae-2b0e4f0b6799 | -3.11662 | -45.23449 | 2025-10-23 04:06:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 05c07d24-10a8-3707-88f2-f518c8985bb6 | -3.11357 | -51.2099 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cdf9867-17dd-361f-834c-f8932a71770d | -3.21883 | -46.80279 | 2025-10-23 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43fbe8c7-16d3-37d1-aced-bb5c841f4773 | -3.80044 | -40.84465 | 2025-10-23 04:06:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ceebfbe1-0ee4-3af6-9c2b-9c5a2af0fff0 | -3.02326 | -49.45328 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 96d28f0b-4b3f-3385-bc50-852c718e1d95 | -2.24835 | -51.92081 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc15db0-f245-3f56-89ec-2d840570adba | -3.11428 | -51.20574 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6427088-171c-3e76-ae2f-035011bfb8dd | -2.80782 | -50.27642 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 796a5342-958d-35e5-9290-334e8594eb0f | -2.85697 | -50.73851 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README7.md)
