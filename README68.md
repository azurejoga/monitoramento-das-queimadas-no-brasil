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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eb96744-3ff1-3312-9989-006792037750 | -16.88534 | -57.70702 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c3dbc2f5-a466-39d6-a402-3c2f048edcb8 | -16.88437 | -57.71437 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a875adc0-472f-33c5-bbf4-a1142facce95 | -16.87016 | -57.69732 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5a74eddb-9417-34c6-bf6a-9e20466467de | -16.86612 | -57.69674 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 708302bf-e10a-347a-9af8-467bc17924b0 | -16.86177 | -57.72982 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b0f4dd2b-ed9c-3db1-9d58-c404f8ea41fc | -16.8616 | -57.69983 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fd61b7fb-db52-3f48-9d8e-8d5c169f2518 | -16.85804 | -57.69556 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 76f6142a-3e1e-39b2-9de2-068e85ed3803 | -16.85756 | -57.69925 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 62175a9a-d53a-3fe2-a71a-d249cf5c5280 | -16.82614 | -57.55841 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| debe0da4-d048-31c9-892b-cccd6be533bf | -16.82302 | -57.55032 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 41224243-3ce3-343a-9742-58de842596f6 | -16.81954 | -57.54704 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4ed367c9-b03f-34e8-90e8-e959973487e3 | -16.80583 | -57.55651 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 571892ca-db84-393b-a249-a66cbab305a4 | -16.78397 | -57.81201 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3d9d82fe-0d11-3fdb-b106-4b7b23926aa2 | -16.78349 | -57.79646 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1435b351-903f-3867-916c-659d3d593f3c | -16.78239 | -57.79335 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 10b1ad54-5c35-324b-9105-793fb99434ed | -16.78191 | -57.79697 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fe0e8868-1a68-3e0e-9801-c3e6d61e4dee | -16.78164 | -57.81096 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c5cdeb9-972d-3986-b2e6-2adf12c0a131 | -16.78118 | -57.81459 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c7cf9d58-9e9b-3c70-ba3a-f58b9e2daf29 | -16.77839 | -57.79276 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 3fe0917b-1187-3288-b40c-7601b37ace7f | -16.77644 | -57.80724 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| de37917e-65b1-37e1-aaf5-15283f13c5cc | -16.77596 | -57.81086 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 53a30a4f-9963-31e2-9f4d-11d2cf9d303b | -16.77438 | -57.79218 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 4b70877b-0283-3e40-93e8-06089a512f97 | -16.77389 | -57.7958 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 24756c68-f5a8-3344-8a54-5ba28db48c2a | -16.77341 | -57.79942 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b76a08dc-a104-373c-a9eb-6f06097a5ddb | -16.77292 | -57.80304 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 729a55fd-b885-3d73-aafb-9afbc5822d48 | -16.77243 | -57.80666 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 80b9d84d-025c-3ed4-bff0-a9aa79a8adf6 | -16.76843 | -57.80608 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ddae70c0-5b89-3beb-805b-742c4e929b34 | -16.76539 | -57.79826 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1c0eb641-6551-3bd7-9b47-7d284b6fb1f0 | -16.7136 | -57.53173 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| a67408e3-4564-327b-b678-e3ae87d76e05 | -16.70905 | -57.5349 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| dd4db4f3-3872-3f4c-ab6d-808fc152c9c4 | -16.70886 | -57.53606 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c2f7c2a8-104a-3384-ac85-5cfc2e47e25c | -16.70836 | -57.5398 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c33ec56f-4a21-39ac-b9ca-5d3bf95d36b6 | -16.70529 | -57.53174 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 3b4874c8-7b34-345c-a21b-d776f731ec4d | -16.99461 | -57.99004 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9434e834-f0d1-3b64-bfd4-7d20aa019f86 | -16.99063 | -57.98946 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2d76edb5-7d6b-3a40-ab50-8a562ba85bc4 | -16.98995 | -57.99479 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| f9032376-c071-348b-8d33-9107140523a6 | -16.98666 | -57.98887 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 265c18c4-408b-33ee-ac53-80d8cd5ab30c | -16.98597 | -57.99421 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 0163b636-39b3-3464-ab00-c40fc62e1f39 | -16.98358 | -57.99274 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b60318b7-3967-3f4a-a296-df6c21b6a590 | -16.98285 | -57.99805 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c8e727d2-7f39-3e5d-b10a-cd53d2dc3f60 | -16.982 | -57.99363 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a78ebd9c-30f9-311a-8622-dbd53e2c6468 | -16.98132 | -57.99895 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 4cbeee06-08e0-3737-baa5-bf39df5854fe | -16.98069 | -58.01398 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 19c0dc9a-a7d4-3aad-b91a-9ad4ed6235d2 | -16.98063 | -58.00427 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fe318f48-073c-3aef-bb7c-3d679380487d | -16.97995 | -58.00957 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f5583aaf-8d87-3180-aae4-f0a5e0913515 | -16.97926 | -58.01489 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 942148b4-64ca-3bd9-9a70-56070fd09f6c | -16.97816 | -58.00278 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b8b6cde2-9cd0-3632-a8c7-2c3571a7cf06 | -16.97673 | -58.0134 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4870328f-b021-33d1-ac77-1206ae6d0ae9 | -16.97666 | -58.00369 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c664abef-7985-3854-a58d-6d109978963f | -16.97598 | -58.009 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 52fadf02-ff51-39e4-b166-9e04abe3e240 | -16.97348 | -58.00752 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fbcdf79b-6403-36d5-bab0-ff9107e0a7a0 | -16.97201 | -58.00842 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d4d7734a-d31c-32ae-8e3e-faf13e21479e | -16.96997 | -58.02436 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| db75e9f8-9469-3f7a-9415-6edfba21b707 | -16.95822 | -57.94009 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 48dff8d4-5d17-334b-8e2a-ef75091576e6 | -16.95751 | -57.94545 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 95886257-6039-3850-ab32-2bae97bdd967 | -16.95608 | -57.95615 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6394f48c-e252-321f-8337-e7ab78febe1c | -16.95537 | -57.96149 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 141b4ca1-dec8-3099-8089-40b4364cd46a | -16.95465 | -57.96682 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c5baa9fe-e976-30a1-a623-6f35679ab255 | -16.95139 | -57.9609 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 15e0ed94-864a-3bca-91b0-51c529f28454 | -16.95097 | -57.93356 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3d2ec992-db3d-3ce5-b8ec-bd0832a176e2 | -16.94699 | -57.93298 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 22a58817-6189-3e6a-a226-eaddd1f0a73e | -16.93105 | -57.93066 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 06161429-0626-3d54-a6f3-e70cde7b3931 | -16.93035 | -57.93601 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9d7b5084-c263-397d-b1f6-a650eb257e47 | -16.8884 | -57.71495 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6d691093-0173-3c97-84e6-e6b590989267 | -16.88388 | -57.71805 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0cc8a647-c51a-3bb4-9248-cb1cfbe74161 | -16.88131 | -57.70643 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7009c4f3-9491-31a0-adc8-cbb0783fa605 | -16.88082 | -57.71011 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 783c8637-3418-3507-928b-dfa1b692f161 | -16.87032 | -57.72732 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3440956d-6cc9-3e1e-8de7-182f7a863b94 | -16.86629 | -57.72673 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a1371fd6-7e16-3310-b508-63f513bb28be | -16.86564 | -57.70042 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad3531e2-5fcb-355d-9348-726b44e0483e | -16.86208 | -57.69615 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f32d747a-e3b0-3333-8538-1581c1fc9672 | -16.85352 | -57.69867 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 90212b57-b713-3a45-bbc8-8955186c857b | -16.85304 | -57.70235 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bb9f7b1d-dbe9-3e7d-8a43-6e55b77bfafd | -16.849 | -57.70176 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 68cca725-830e-3d57-9c1f-0bf40167f010 | -16.84853 | -57.70544 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8cf906ba-3ebd-32d7-96ee-0ff68d72b581 | -16.82384 | -57.76902 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ab71865f-3e84-3eba-b8d6-f2b6066dc94b | -16.78797 | -57.79342 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d4296899-1ab7-316b-b809-a3dad1590efe | -16.78641 | -57.79393 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| df452137-e910-36f9-a4da-dc2a3de8219a | -16.78565 | -57.81155 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ebf8eb63-6243-366d-bd98-1b20e7733d4e | -16.78445 | -57.8084 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eaec16ff-1712-3bf6-8a77-23e0ae608132 | -16.78395 | -57.79283 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a5950f0f-4292-3c38-9279-4f8d277a7f86 | -16.77996 | -57.81144 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c2ca3e9f-1094-34c5-b5c4-848be8b9a2eb | -16.77947 | -57.81505 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f536ed05-a6a5-3bc3-8f0e-d30ef18270fc | -16.7779 | -57.79639 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 5c23d2d4-067c-396e-a39d-8914bfdb7c16 | -16.77547 | -57.81447 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a5fb8d90-8486-3ed6-a1b6-77ccad27cdb2 | -16.76988 | -57.79522 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1aab8a5b-2a10-37e5-b0be-163bb1bf9ec9 | -16.7694 | -57.79884 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3bca7c81-6bb2-36d8-8b53-e0f3d3421b44 | -16.76891 | -57.80246 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 05ff904c-9961-3313-a842-e7bcdcd3b6d1 | -16.76491 | -57.80188 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f03d55fc-4dd8-334a-a946-ee6d11c630b5 | -17.19998 | -57.39083 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f785d5d3-f161-3ef0-97b1-e5a09fb05c56 | -17.19949 | -57.39472 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a0ee94d4-5ff4-3339-b498-a3f3a9067c22 | -17.19584 | -57.39024 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5484dee5-b4b7-3808-a12a-42a84f7db82c | -17.10219 | -56.73492 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1bb4b933-ed60-3648-beb9-c2aa91b35497 | -17.10165 | -56.73919 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 71d8f12f-4d35-3193-bb7a-abbfc99c33f4 | -17.09787 | -56.73431 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c6b01a04-7a4d-3843-af34-e7a79a7870d9 | -17.09734 | -56.73859 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c31042ad-4814-39c1-826c-a15ee3ed6e0f | -17.07041 | -56.74346 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 633cc177-8e8d-336d-9e46-202ecc04e837 | -17.0661 | -56.74285 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0b828175-808b-3794-8a3f-5bbc5d4a6c3c | -17.06557 | -56.7471 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d2739058-e36f-317f-86d8-99cb163a8b32 | -17.06284 | -56.73375 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README69.md)
