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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75c33401-8411-337f-82d8-90429178a07e | -19.17449 | -40.14014 | 2024-11-30 04:44:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| dd660cf8-3250-3ce7-9187-3bc2c6538653 | -19.94036 | -42.02288 | 2024-11-30 04:44:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 66073aad-5d84-339e-9706-be6f563940a6 | -19.16807 | -40.13942 | 2024-11-30 04:44:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9553d616-4d69-38a3-84be-ef58c5b7a397 | -20.64929 | -56.58366 | 2024-11-30 04:44:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06bfef4a-d506-375e-98c4-b4422273f95a | -20.24652 | -41.18416 | 2024-11-30 04:44:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c0ba8d8f-4ca0-3f1e-8ca5-cbad9116cdbe | -16.24907 | -59.96059 | 2024-11-30 04:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e29d189-817b-342a-bfc9-2ae4a04d2724 | -21.22916 | -56.9197 | 2024-11-30 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c937216b-e2a2-37cf-8f22-0850c3f8e834 | -18.78028 | -55.39521 | 2024-11-30 04:44:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 71a3b39a-cda2-38f6-9d3a-1ec5dba09e23 | -19.82746 | -48.31627 | 2024-11-30 04:44:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2af2889c-d372-3010-9d47-bb1b046e83db | -19.50529 | -56.6055 | 2024-11-30 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7b932309-0681-3611-a446-130d92cc9391 | -19.16759 | -40.14485 | 2024-11-30 04:44:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0e8a3cfc-ba64-3d8b-9704-a2e07ee65014 | -16.25015 | -59.95504 | 2024-11-30 04:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2129c893-933e-3b87-96e9-655a9457eea4 | -20.24694 | -41.17937 | 2024-11-30 04:44:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7ca8df6f-5982-32be-b4b5-c92c61d1fb3d | -9.45087 | -35.91859 | 2024-11-30 04:46:00 | AQUA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 07bd1de2-4b3d-32b9-8269-fd46dfd0d217 | -30.02806 | -51.11086 | 2024-11-30 04:46:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| a8a09d83-0ae4-362a-bca4-0f34a3b248ec | -29.95301 | -51.61574 | 2024-11-30 04:46:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 2de93b00-2e06-3154-88f5-1993359169a7 | -19.17562 | -40.13731 | 2024-11-30 04:48:00 | AQUA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| e6b0a4d1-3b24-32cc-8319-41f2a412efb9 | -3.2591 | -53.6186 | 2024-11-30 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3bdd1063-e7f4-3055-ada5-7fa4e5d92e71 | -1.6602 | -53.8728 | 2024-11-30 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f416c383-0073-3e74-9d91-990c0750ab1c | -3.2406 | -53.6393 | 2024-11-30 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7d8bc5b8-1473-340b-878c-f7382fcaae04 | -1.6938 | -46.7833 | 2024-11-30 04:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 16330da8-080c-37f3-8b37-b8943a3963a1 | -1.0733 | -53.6378 | 2024-11-30 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2d4a50d3-23c4-3e73-b675-5f6620067b5d | -3.259 | -53.6388 | 2024-11-30 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| b315fb8f-94ca-3667-81f8-1dd215f08846 | -1.6419 | -53.8731 | 2024-11-30 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 5d1b0e6b-c93d-30fd-95f7-00a9789568c8 | -3.6061 | -49.9784 | 2024-11-30 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 04ed784a-1808-3171-872f-ce42c7c75ac8 | -3.259 | -53.6388 | 2024-11-30 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| a2b60a03-66e0-3b51-bf3f-f58fe999c22d | -1.6938 | -46.7833 | 2024-11-30 05:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 20edae5c-a977-3f39-81bd-8cda2acc1ec3 | -1.6419 | -53.8731 | 2024-11-30 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 2a7b4576-b8db-3528-846b-db6293ce0067 | -3.2591 | -53.6186 | 2024-11-30 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4beae648-f99a-3564-aed6-1ae9bf24afbe | -3.606 | -49.9995 | 2024-11-30 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 4805ddb6-b2b7-3142-95b9-2d7e0278028d | -1.6602 | -53.8728 | 2024-11-30 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b0da9e0d-62bb-3409-9bd0-1d8802c93e98 | -1.0733 | -53.6378 | 2024-11-30 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c62d856c-ca20-3f4f-bbfa-7866f0932eb4 | -1.17892 | -53.41215 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2721772a-98ef-302c-9700-524fff329233 | 1.64081 | -50.95037 | 2024-11-30 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 669e4d7c-bf68-35ee-a562-c45d939798b8 | -3.24443 | -53.64217 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06439648-9dd6-360d-ae1f-200c9cb97aca | -1.17583 | -53.90659 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d15b8012-dfaa-3b7b-a646-c73127185c61 | -2.57881 | -49.99878 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c7d9624-65f0-3b17-aa7f-8a48fcbccc56 | -1.43284 | -53.39341 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b9b984c-6250-3006-8720-9af925cecb43 | -3.46271 | -48.92686 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62ff95a0-9e43-307d-aa7b-45544674fa9b | -2.96169 | -53.88937 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e970f49-90b7-38ca-a8a9-aee0fc2a2338 | -3.13791 | -45.98276 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aa5640e-0317-33a1-a31d-be79c1cd7d5d | -0.7733 | -52.38803 | 2024-11-30 05:01:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccbb87a4-0de3-308c-a281-dc5faf3645bf | -1.2539 | -54.55176 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 979508ee-0b06-3de8-90d8-1613930d5146 | -1.20476 | -51.74207 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf5adfe7-a89f-3fb3-94b3-5e6a914d9b44 | -3.19783 | -46.56195 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 517b519c-007d-35a1-b285-cbea2cfacf1a | -1.11827 | -53.7337 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ecf39b7-a712-340b-ae20-ff1ee0c0330e | -1.46826 | -52.68266 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5b99658-af21-3175-9b32-c76f1ed879a2 | -2.0287 | -52.07719 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 07ed1ebb-473c-3d8c-850c-f46430302f95 | -2.97185 | -53.28593 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 742dfa9a-c477-3025-b364-ac7aa41d2faa | -1.43983 | -55.13184 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df751ae3-8307-33da-83a6-ed13f55abeb7 | -2.20597 | -48.3832 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44e6fe82-1207-35aa-9b6b-6c5af47a0993 | -1.42734 | -55.27561 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cf682eb-64aa-3e97-bea5-917c35c9fc42 | -3.10337 | -53.8059 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cce4dbe2-f990-3a59-8f3e-ce60d6b50989 | -3.0639 | -53.68319 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46c4d70f-1f12-3422-95c0-3ed0ecd377c3 | -1.43839 | -55.24886 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 39c0b708-feca-3b28-8875-7c1be69afff5 | -2.47424 | -50.36916 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e837326-9d5b-3aca-8c72-f379f0d08856 | -2.75691 | -54.12017 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f26d38-35c6-3780-a640-e8b3f17c358e | -1.69178 | -55.01579 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 749046c4-49bb-32aa-ad64-d502dbb2fdf7 | -3.15323 | -53.82848 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d170029-4463-3374-bcdf-3a56c5f98bc5 | 0.94495 | -50.72768 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b1d8ca6-9f65-3360-b098-c1b6f480aaf4 | -3.47184 | -50.53466 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9a78204-66e4-3c16-a64b-b77c814cdfa5 | -4.01484 | -49.01033 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb34376b-6e00-3e4c-9f33-5cc24b51cefc | -4.07734 | -54.5642 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 725e5c37-5ff4-35d1-8a48-f6fe2c3dc794 | -2.38495 | -54.35364 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba3c837a-deef-3e4e-be86-7c33b028a355 | -1.11868 | -51.9051 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b781155a-2415-39fc-88c6-84c6d2c715a1 | -2.85491 | -54.03137 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4ccca70-cded-3ad1-b8c2-94a873cff9ac | -3.10687 | -54.03823 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae102322-475e-3b39-a096-5ea759880683 | -1.21251 | -51.73916 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f32122d-6e3d-32e4-ab8a-8b546ff551ee | -3.10971 | -53.98422 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 849965a7-e571-3155-a36f-73074ee7509d | -1.37191 | -51.97017 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c56f7d8c-f745-3f40-aef7-762b7be697d1 | -2.97676 | -53.88091 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3a6cec5-179e-3079-a78f-7981f038e695 | -2.0431 | -54.69586 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b78e741-c693-36d8-9a87-2ebb70b0759d | -3.38313 | -50.69411 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d711a321-6137-3131-8f5e-779525a0252c | -3.24894 | -53.63552 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d87b7f22-835a-3de6-ac39-f6f465bbd1c4 | -1.52937 | -51.62221 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37484a05-c2b9-3641-952e-6d9b5a3e2323 | -2.46914 | -53.96414 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98cd93a8-cf35-3c4d-9d7f-6a6df330e0fe | -1.30325 | -55.74468 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b15d80cc-9643-31b0-a029-5e5aa30b2a01 | -3.74815 | -54.68 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10858c47-31a9-3b52-a3ee-ecbdf127db16 | -1.58175 | -53.84475 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7c5bab-6731-392a-820f-25543266b69f | -3.26216 | -54.10876 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbd55959-fd13-3631-9a5e-052485c037bf | -3.92161 | -53.66698 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3ec963d-5427-32fb-854b-38c546b0e5f4 | -2.67769 | -50.50371 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eb05482-b94a-39f2-a976-426e1a9b8709 | -2.38211 | -54.32838 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 01b9f804-c5e8-3d56-a971-65f65812cb60 | -2.3823 | -53.68438 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ead3e97-f151-3f09-9997-a49e6c6aa9bc | -3.49733 | -50.28581 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a13a39b-ff3c-31bf-814c-8aa5806bf141 | -2.43079 | -54.01908 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56869147-734b-3cb5-bf31-47b6ddc34ce1 | -1.18733 | -51.76946 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0997f9d8-74f2-34fb-bbbc-ecbfc2a20275 | -3.03059 | -54.02954 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49f4ceb0-3805-34be-ab81-f04823bfcf3b | -1.50687 | -52.56254 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32f913eb-ac3d-3372-bffb-bc1f97aa2599 | -3.1981 | -52.44003 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7258927-5293-34b6-a529-489f1dc2163b | -3.24765 | -50.6171 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f258bcd4-98f7-3f03-a0af-99d721a36ce1 | -3.28509 | -53.85244 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01bbbccf-9730-36cf-9a3d-5ca2c9754e50 | -2.58223 | -51.92245 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f6480a4-5ccf-388d-b110-800b7b11d99e | -3.51799 | -50.25723 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc8dff33-a138-33c5-823c-4d62df15f6cd | -2.77236 | -54.04385 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0023807-2686-30b5-bef7-96a6caeea3ad | -2.90155 | -51.36879 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ca7afee-2b4a-3fe8-a5df-d12db5150bcc | -1.14924 | -53.66703 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 970efc24-9337-32ca-a4cf-7d805ebbab1a | 0.94528 | -51.93026 | 2024-11-30 05:01:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48047ac6-e70a-34c9-b293-406f85abafdb | -0.58184 | -51.69263 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b055b3b1-3f9f-32c3-82a9-24cf85185f1d | -2.66049 | -48.78284 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README75.md)
