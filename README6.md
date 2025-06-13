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
| 8ce4f76f-a839-3881-85a2-fcb76701904d | -10.7048 | -49.507 | 2025-06-13 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 7d505e70-20c0-3eb5-80f3-b5d7a12cc774 | -7.6674 | -43.6323 | 2025-06-13 02:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 8d208aec-1ab4-32bf-a5b3-7b95ee35943e | -11.5649 | -54.559 | 2025-06-13 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4798cb44-444c-3f4a-8287-7d6675107e9b | -7.686 | -43.6538 | 2025-06-13 02:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 886735e9-a767-38e3-9b11-da3fc761facf | -7.6671 | -43.6557 | 2025-06-13 02:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 163.1 |
| cf11ede4-011a-34b0-930c-193a087a0d3e | -10.6302 | -49.4288 | 2025-06-13 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| f183af20-f3e9-34a3-83b5-01e44cd1acb4 | -10.9355 | -56.8322 | 2025-06-13 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 292e940f-ccba-3a03-86df-34573c05e77d | -13.8867 | -54.6312 | 2025-06-13 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| fd336c6b-68b4-3691-bb6b-8a621bf50956 | -13.9059 | -54.6291 | 2025-06-13 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d3c684e6-9996-3d41-aaf6-7f9af521dec7 | -9.4114 | -57.5529 | 2025-06-13 02:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4935c05a-3113-3559-8c7c-7da36b847806 | -11.5647 | -54.5794 | 2025-06-13 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 278bb344-659f-3840-868e-23bb87b5c7c4 | -10.6492 | -49.4267 | 2025-06-13 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 928c8213-c379-3295-b4ee-a54539d36181 | -13.9062 | -54.6084 | 2025-06-13 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| fa92d82a-1b65-3bac-9c80-b4540ce38ef8 | -10.9167 | -56.8336 | 2025-06-13 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e14f300b-da3b-35a4-aad3-861805121f6b | -10.6302 | -49.4288 | 2025-06-13 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a3e6e53e-d0ef-3bf8-8a8d-a935dd4e5845 | -11.5649 | -54.559 | 2025-06-13 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6658ce8d-7bd1-3da7-995d-42b6a8d73dff | -13.9059 | -54.6291 | 2025-06-13 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 8248f4e0-5dca-3d51-8a4e-339f0206522c | -13.8867 | -54.6312 | 2025-06-13 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 62cefae0-b8b9-364c-9c4b-76c52dd8e914 | -10.9355 | -56.8322 | 2025-06-13 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 2c15c302-cb7b-320b-a28c-22283760c70b | -10.7051 | -49.4853 | 2025-06-13 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| d1475459-6459-3c01-820b-171de538718a | -10.6492 | -49.4267 | 2025-06-13 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ea012e3f-6baa-3b85-a8b7-f1bda9b1515e | -13.9059 | -54.6291 | 2025-06-13 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 113217ef-e8dc-3d27-b01f-94be99f5d3af | -11.5647 | -54.5794 | 2025-06-13 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9c8b409d-12a8-3275-b2af-337a6284c76e | -13.8867 | -54.6312 | 2025-06-13 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 89a61cdd-2d83-389a-963b-f5ce82809b44 | -11.5649 | -54.559 | 2025-06-13 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 34f20a14-8e2b-3fe9-88f7-357817b4ca36 | -13.9059 | -54.6291 | 2025-06-13 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| cb18a009-a0cc-3215-9feb-689105ad426c | -10.6483 | -44.4861 | 2025-06-13 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 55427ad2-b1bb-37cc-ab4b-9a054fc4c2d6 | -11.5649 | -54.559 | 2025-06-13 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 87cebf86-e955-3424-a70f-df4404ccd90e | -11.5647 | -54.5794 | 2025-06-13 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1b7722b4-a5da-37f8-a355-efbf6e752b85 | -10.6492 | -49.4267 | 2025-06-13 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6a29a148-6dcf-3f3d-ab31-33b7a9d8b69d | -13.8867 | -54.6312 | 2025-06-13 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7553049d-e5c7-3b55-9771-261214200166 | -13.9062 | -54.6084 | 2025-06-13 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f2a32e43-2617-3def-8f90-ce7cad6e25a8 | -11.5649 | -54.559 | 2025-06-13 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a1314d65-6da6-341e-b8e5-c8be1492cd77 | -13.9062 | -54.6084 | 2025-06-13 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| a90fb7a1-b0c4-3098-a175-99262c52b7d1 | -10.6492 | -49.4267 | 2025-06-13 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2b6338e4-8dd9-3b4b-baee-859be2bf6840 | -11.5647 | -54.5794 | 2025-06-13 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 79d1e6a2-26fe-3b47-9a71-cfe0face3c52 | -10.9167 | -56.8336 | 2025-06-13 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5246ca4d-4667-3118-9094-ade0fe6eacf1 | -13.8867 | -54.6312 | 2025-06-13 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 39f13390-5fda-381b-8c9b-1d7183f7df68 | -13.9059 | -54.6291 | 2025-06-13 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 30533ee5-ecb3-3493-b48a-a29837814bf0 | -12.34263 | -38.20069 | 2025-06-13 02:51:00 | NOAA-20 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2524db2-d2ef-3d69-b8ea-fbbb888eed95 | -12.34982 | -38.20206 | 2025-06-13 02:51:00 | NOAA-20 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8aaecd91-0f69-362f-8d76-c8b93e9525ce | -13.9059 | -54.6291 | 2025-06-13 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 3636f050-d224-38d7-a68a-847d5303786f | -10.9167 | -56.8336 | 2025-06-13 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 59d3d407-a2a1-3f7d-b37d-4e799741c01a | -10.6492 | -49.4267 | 2025-06-13 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4f7457a3-628a-3b36-a572-bc46b784677d | -13.8867 | -54.6312 | 2025-06-13 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d305d751-9c41-3ffb-8c21-29cfc9c65b34 | -11.5647 | -54.5794 | 2025-06-13 03:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 9ec7c164-f379-3fb2-adba-5ce1f8069ec1 | -13.9062 | -54.6084 | 2025-06-13 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 0b41e36f-a3ca-3ff2-849d-324cf5ffdb9b | -10.6483 | -44.4861 | 2025-06-13 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 64fdf842-17e5-393d-b3eb-4380bd6fc59e | -10.6483 | -44.4861 | 2025-06-13 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 8329746f-b5c3-38e9-8877-45cf7217702e | -10.6492 | -49.4267 | 2025-06-13 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 559c67ca-28b2-3a7d-860d-4747d1eb808e | -11.5647 | -54.5794 | 2025-06-13 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 05e9550c-0734-3fe0-be0d-093060c0c827 | -13.9059 | -54.6291 | 2025-06-13 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 76bdfa9c-00e3-3e68-ace8-eb3c812b72f1 | -13.8867 | -54.6312 | 2025-06-13 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| dd062d4a-b5a3-3715-9403-731941ff9cb5 | -13.9062 | -54.6084 | 2025-06-13 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 30a209cd-87af-3cbd-a760-eb7f33fb5644 | -10.9167 | -56.8336 | 2025-06-13 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 33d23c48-34f6-3a4f-b59d-8774b112f8a4 | -10.6492 | -49.4267 | 2025-06-13 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 3b429190-e635-369e-a252-1908ffa9532c | -13.8867 | -54.6312 | 2025-06-13 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 8e6a9981-2a06-3370-ae62-dad6729fce06 | -10.9167 | -56.8336 | 2025-06-13 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 250da5a4-065c-3f49-a5e8-d4b867146558 | -10.9355 | -56.8322 | 2025-06-13 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c48dc544-da55-3fb3-b370-28181feadadf | -13.9059 | -54.6291 | 2025-06-13 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 4d4b0267-c898-395a-ae87-a0af393e209d | -11.5647 | -54.5794 | 2025-06-13 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| c5243e65-9652-3993-880c-e405ba91b82a | -10.6483 | -44.4861 | 2025-06-13 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1ebdcbbe-6e24-3cb0-95c7-b5099d57dd6b | -11.5647 | -54.5794 | 2025-06-13 03:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6d788e02-cd5a-35e8-9e49-a33c0921a485 | -13.8867 | -54.6312 | 2025-06-13 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a25c54f7-dd02-36d4-bab7-910119fdd793 | -10.9167 | -56.8336 | 2025-06-13 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c63e2ac2-1ef1-3b42-9dc9-926cd4bec899 | -13.9059 | -54.6291 | 2025-06-13 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 41dea3c9-c4e0-351b-8beb-97c1342f2552 | -13.9062 | -54.6084 | 2025-06-13 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 0d0d3482-e828-394a-8095-53dbb8ee0d30 | -10.6492 | -49.4267 | 2025-06-13 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ecc6d4cb-2bf2-35be-ba93-cd5d0aff15c4 | -13.8867 | -54.6312 | 2025-06-13 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| be706c7c-1fd4-35ef-8a7c-05c2e9779aae | -13.9059 | -54.6291 | 2025-06-13 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| aec6289d-d504-3df8-aa96-c2e8ae368580 | -10.9167 | -56.8336 | 2025-06-13 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 8386dfea-204b-3c15-a506-6a45944d627f | -10.6492 | -49.4267 | 2025-06-13 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2dc0c932-95f8-3876-bf3a-19a11a6c49cf | -10.9355 | -56.8322 | 2025-06-13 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| eb79d567-1d6a-38b0-9fc4-9810d8d1c04e | -6.49116 | -42.84679 | 2025-06-13 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0ca49447-34d1-3601-b9fa-917f46f0e83f | -6.94561 | -42.8954 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 698f3eb4-d674-35aa-a273-e67e20772e80 | -6.49026 | -42.85202 | 2025-06-13 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 086d91f2-94b0-3cb4-994e-995227e69cbf | -7.80002 | -40.55334 | 2025-06-13 03:42:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab0f9363-8e04-3537-a299-b43399530af4 | -7.44622 | -45.51702 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c495ace-3c6d-34d8-ba53-80f5173bd202 | -8.07077 | -43.1168 | 2025-06-13 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 3b8061b0-3e6b-3491-a23b-80717b656823 | -5.64633 | -43.59977 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d75bd79-07fa-3e6a-abfb-17401c09e039 | -7.45321 | -45.51024 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6bd5fc1f-b2a0-3bb4-b4c1-b3d2989a718c | -7.45882 | -45.51116 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8604f770-35d4-35f9-9676-6098f892c1b1 | -5.64392 | -43.60396 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76d195aa-ae35-395e-a754-6e3d6aa19fc9 | -3.77748 | -41.66848 | 2025-06-13 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 100a309d-69e0-36e1-ae50-b0156ec4ef79 | -5.64583 | -43.60278 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c1a3a43-0c70-3c18-bb20-6bc302a74349 | -8.07165 | -43.11174 | 2025-06-13 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8972d471-8a31-3688-b9a0-c22776161aab | -8.07548 | -43.11764 | 2025-06-13 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 74833957-1fb7-3a2b-acc9-95d293c90583 | -4.19366 | -38.37143 | 2025-06-13 03:42:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4a66f7a0-7ff8-38ec-a86a-509bc7503d92 | -6.95124 | -42.89101 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e2de855a-4ced-3ab7-8a39-5ed9f55dba9c | -7.80062 | -40.54988 | 2025-06-13 03:42:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc86320b-817d-34ca-9791-119021c005bf | -4.89453 | -37.52708 | 2025-06-13 03:42:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0cbfe12c-8504-304f-a33d-00a5f27d52ab | -6.94649 | -42.89026 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 142fd266-e729-3c37-88b7-08d4249e7a8c | -7.44553 | -45.52091 | 2025-06-13 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ac93726-b05f-31a7-9ba4-f010962b4c21 | -7.02957 | -37.2905 | 2025-06-13 03:42:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d97c00e-2eed-3480-a447-c7c8cf2427ae | -4.18997 | -38.37085 | 2025-06-13 03:42:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 75199b26-1778-30ae-81c2-8a097d2906ac | -5.64532 | -43.6058 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3e31e2a-9ad9-33a8-9c90-84f2a27976ed | -5.64901 | -43.60481 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be50c7b1-1a41-3950-a291-d6483e1df501 | -7.45676 | -45.52277 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc1f9eb3-0ac1-39e6-876f-e589884625b2 | -5.6499 | -43.60969 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c417657e-c240-393c-b8ed-1c9e8d4d6a72 | -5.90252 | -43.45336 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README7.md)
