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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0afac1fe-889e-3502-9ab8-8dbb21abb3c4 | -2.82138 | -49.2332 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83bdda90-2834-3fa2-abbb-06a46eb0ac46 | -2.81745 | -49.31189 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5a9595c-0ffe-3d09-bcef-196756054df3 | -2.81614 | -49.31215 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1105f701-959d-3c0e-a8f5-bf45d675210b | -2.81395 | -49.31135 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0640c02f-e568-3edb-a045-a41b15e63b5d | -2.81325 | -49.30774 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af5a9198-8a2b-33e6-954b-d1cad19197d2 | -2.81277 | -49.31912 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e52992f4-3c36-3445-8f10-94a333d24fe4 | -2.81264 | -49.31161 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef03d76c-1e4d-377c-9f40-2e52d56193e2 | -2.80169 | -49.623 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 842004f1-899b-334c-a6e5-194e41b46e33 | -2.79214 | -49.47758 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f436e590-dc97-3c3b-9f55-e8ef0a8321d6 | -2.79156 | -49.4814 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74306bea-a732-36bc-a94a-0c33d6f0de13 | -2.79008 | -49.47762 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09602ace-5f72-328a-ba32-8f3ce76f1ee3 | -2.78948 | -49.48143 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7be3fa65-5411-307f-b778-04a53b6a3583 | -2.78867 | -49.47706 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c7c7cb8-43cb-3434-93b1-8083158f58db | -2.78809 | -49.48088 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ff527a5-86c9-31bc-aec8-282e09f0ebce | -2.78601 | -49.48092 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a046bf7b-b966-3949-a2d4-09c4618dc90b | -3.36007 | -50.15902 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56a6f005-72e1-330a-9fe3-c98300c0a3a7 | -3.3595 | -50.16271 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2307aed-e2b0-3e19-b31c-c68cf439c318 | -3.35729 | -50.26693 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12763ded-fb5e-34b5-9437-27151649d49e | -3.3539 | -50.26642 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b24897c-6a72-3597-a40a-90767a9e52ce | -3.35334 | -50.27006 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e254b04-d5ef-3184-a624-8798a4c08528 | -3.32649 | -50.1239 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 893eb206-1276-3048-b986-0c7186fc8144 | -3.31835 | -50.24231 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 736c5b80-f7c3-3f49-95b9-f65b95518561 | -3.28841 | -50.23392 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d86b209-cde8-30e4-bf0e-3139f0f34b91 | -3.28502 | -50.23339 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ad250ad-7a48-3ead-9ddf-29f69d84bd1b | -3.26804 | -50.34221 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c856d231-8b23-3bec-ab1e-8446a1103514 | -3.26748 | -50.34583 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cf90288-dd1a-32b6-be27-ec69fdb6d9d0 | -3.26579 | -50.33446 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6496a54e-1c6c-3ece-8d9f-1f2fa85f5a94 | -3.26522 | -50.33807 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c8199fe2-8b99-33e5-ba5f-831eb8f1f54e | -3.26466 | -50.34169 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 853493c9-db9f-3c65-bd7b-fc14e87b06c9 | -3.2641 | -50.3453 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c824100-dadc-33a2-8c64-3624598b6f30 | -3.26353 | -50.34891 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a381355e-1e97-3a2a-a406-ef681d205468 | -3.26241 | -50.33393 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 299e73d0-40b0-3530-81e9-e1778464b54f | -3.26184 | -50.33755 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b676dd26-4883-3545-a316-c80a4cdae7ac | -3.26128 | -50.34116 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 745bc18e-1145-3f88-aea5-e0f11184896e | -3.26072 | -50.34478 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff61c1c7-5070-3f00-973b-9dba2fb212b0 | -3.26015 | -50.34839 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c0d113a-5245-3fbf-bfb0-5486eca38d93 | -3.25903 | -50.33342 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd0e0849-6f1f-3f0e-87da-10c0662644a8 | -3.25846 | -50.33703 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 122eabd6-5f92-3115-a617-8b8b6dbd68d3 | -3.2579 | -50.34065 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 081bf6d4-53e9-39be-b243-22364b2b46a5 | -3.25734 | -50.34426 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc2ec9b3-9467-32f0-aaec-f9dc15fb211f | -3.25677 | -50.34787 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c7dac27-e7ca-3ac2-8140-624aff6a597c | -3.25564 | -50.3329 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67deab52-c7ad-3615-95a5-4a1f3486c252 | -3.25508 | -50.33652 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f2d00b5-c0a0-3b90-b8ea-fb0c67c2835b | -3.25452 | -50.34013 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbed41b2-b31b-3327-be6b-6f4447b9fbfb | -3.25396 | -50.34374 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf0758b4-3175-3a35-8e24-2bfa0ae67af5 | -3.25339 | -50.34735 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e166e19a-115a-32d0-9f4a-35b23c5a3bcb | -3.2517 | -50.336 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47806d14-a8cc-344c-ba21-969de36a0a58 | -3.25114 | -50.33961 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7ef77ab-75f8-3a08-9708-1031767c70f5 | -3.25058 | -50.34322 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798ba041-4395-30ce-9dcc-a7575d0d8ebf | -3.25002 | -50.34683 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4bbe6b1-be84-3791-a2ea-f952203edecd | -3.24832 | -50.33548 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5464cd4-0522-32c0-9887-3f3283407e3b | -3.24776 | -50.33908 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d523c674-faa0-358e-9dd4-069bfeb5bf30 | -3.2472 | -50.34269 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a270dd15-884a-3c4d-9ae3-afec8c457724 | -3.24664 | -50.3463 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b405e11-d9be-38ea-8a34-96596d462f48 | -3.22616 | -50.1871 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61ca4dd1-2ea4-3848-8c0d-810f13a68729 | -3.22333 | -50.18295 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f024366-d36c-3cfe-b53c-4fbc92770c65 | -3.51149 | -50.28602 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76865d22-bfe9-35ed-9d44-f01fe336ec7c | -3.51128 | -50.47479 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8bd3906-c22d-3bbb-81f2-d2ff9d76305e | -3.51072 | -50.4784 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1461a560-1b69-3a77-a7c9-e464c5878e6a | -3.50791 | -50.47427 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc86eda3-1268-361a-96a3-127f48820916 | -3.50735 | -50.47786 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c19f21cf-5f87-3e6a-9967-3df92ec47ebf | -3.50494 | -49.94576 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50a43a6f-a8ea-3c9b-8b45-7d4f26778192 | -3.50437 | -49.94949 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02dd745f-4125-3059-bdec-72f8f312ff37 | -3.50151 | -49.94524 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a8fef6e-7a08-31a5-9c2e-cec82f0f1791 | -3.50094 | -49.94897 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24fc8384-e7fe-36ce-8b16-792638a5a754 | -3.49221 | -50.49754 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5b7dd00-bf97-3c43-bc0f-ece9caaad2d6 | -3.46402 | -50.30105 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23bf8393-29c2-3f23-ac04-64f4c8736612 | -3.46346 | -50.3047 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5accd775-eec0-3864-899f-e7e74bd3ea4b | -3.4629 | -50.30833 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d92ac6d-9bc1-33c6-b1ee-031e801db612 | -3.46063 | -50.30052 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 91fb758a-571b-3182-a8d5-9a1290b05080 | -3.46007 | -50.30418 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 04f32d02-4c54-3436-a38f-cffcd2afad8e | -3.45951 | -50.30781 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fabf3cb0-b1c8-3aa8-8d90-6a933df131a0 | -3.45894 | -50.31144 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 47a7bfdf-5abb-37f8-92d4-6d8e61bf1f5e | -3.45724 | -50.30001 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e29c4fac-c8e5-3745-bc6a-ab906b5ef918 | -3.45668 | -50.30365 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 46fcdd4e-d21d-3917-af37-96453e9a5e21 | -3.45612 | -50.30729 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1012915c-b07b-3262-b903-2b7fb2d386ef | -3.45385 | -50.2995 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e483a31b-f02f-30ab-a0cf-51310d53d063 | -3.45329 | -50.30313 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c49678c9-748d-3753-9f87-06df033a536e | -3.4257 | -50.2514 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19c72ce6-bdf7-34ff-a5de-1b5884bbd254 | -3.64931 | -50.44049 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a27885b3-bb8b-381b-ba73-931c5f13e90f | -3.64875 | -50.44409 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75d7a0ee-b516-3218-9e0c-d384bb137e01 | 2.35928 | -50.75645 | 2024-10-31 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76605eda-086d-3c6d-8b5b-4c5a60956b47 | 2.19467 | -50.70148 | 2024-10-31 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b700e28-7c25-3976-a3c3-d2d6f4969704 | 1.65587 | -50.88793 | 2024-10-31 04:49:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a395ecd6-8975-3ef8-847b-f068383b81f2 | 1.80457 | -50.45004 | 2024-10-31 04:49:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23fbba60-9923-35bc-8b5a-c50373eae1c0 | 1.80072 | -50.44712 | 2024-10-31 04:49:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e535e4a-313a-3451-8a2c-be895b2c723d | 1.79742 | -50.44764 | 2024-10-31 04:49:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1731c35-d721-37a5-8376-e450f00e3bf0 | -2.8856 | -51.65884 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fb2dc89-b309-37fe-9179-b4ee77107280 | -2.88234 | -51.65439 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 778341fb-3113-361e-8b8b-2e1786491cce | -2.8818 | -51.65782 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2628f0c-5d9a-39dc-a173-0ad33eb0c185 | -2.83165 | -51.80471 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2393a11-4145-3631-b761-b587a0eceee0 | -2.83111 | -51.80815 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aa40373-a382-3c90-b3a8-30002ced77d4 | -2.82835 | -51.8042 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e675ee-26d3-3ef2-8dc3-c97087bd7739 | -2.82781 | -51.80763 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8887b9a-e502-32cb-bc64-47abfa577937 | -2.80624 | -51.94485 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ccc4a6fc-9ce4-32b6-a496-a865f0f72f99 | -2.80294 | -51.94434 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be705009-70b5-30d6-b81a-04f97c178235 | -2.79964 | -51.94382 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 947eb4b6-4240-3408-9bf3-76980ccbeef3 | -2.7958 | -51.94674 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2949945-23cf-388d-8da1-2ddb5aa0ca97 | -2.74443 | -51.64691 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34c5b5c2-5d39-3761-b422-71b887a2a6a7 | -2.73862 | -51.72688 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README37.md)
