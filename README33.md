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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8b26bc0-06d9-3686-a98c-7104e22719c3 | -1.65333 | -55.07734 | 2024-12-10 05:16:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d48a98f8-5958-392e-bbcc-1d217c43dad6 | -2.45728 | -53.979 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3acb1b9d-9de4-3a94-9370-ff1bdf03f3d0 | -3.83285 | -52.35435 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2108f00-ff4f-39b3-8ca3-3b6bb5ce6c0c | -3.10141 | -54.07669 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0acc850b-05ea-369c-b1f8-244f452a11dd | -3.83347 | -52.35022 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f3cdf4b-8aeb-32f7-81ae-ab5dfbad5f84 | -2.98701 | -52.85181 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff489f0-6e9b-3aae-9517-f56c5695c26f | -1.60086 | -54.64127 | 2024-12-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d66ea8ca-d12f-3774-9acd-4eb880cb363e | -3.86098 | -54.78866 | 2024-12-10 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 909546bb-867a-331b-8cd0-e889d111823d | -2.2516 | -53.87274 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab38f06f-7873-39e4-a914-5364b5a86f74 | -3.87359 | -50.36251 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9b85ce13-f992-3bc8-84e8-bc7bd50eff53 | -1.72571 | -52.47945 | 2024-12-10 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25c97f4e-4bfd-3398-9145-289447a76bf0 | -3.62878 | -52.67732 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dadb795-7ceb-34ad-9b01-41bf843bfeda | -1.50206 | -53.4283 | 2024-12-10 05:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08189cd-f1b0-3ae0-bee4-91aeb4be1c83 | -3.08735 | -54.07716 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c202759d-3330-3c20-8b22-d3f0e6277997 | -3.04212 | -54.24174 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a349c1c1-5d22-3248-9173-a33d957392b0 | -3.06783 | -54.24784 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d748c02d-e0a7-3a8e-b832-5c0c0fe32c6e | -2.61097 | -54.23637 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7773f88-be9a-3d01-bd07-383e70fb5f65 | -3.10438 | -53.25446 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9b84e3a-fad6-3e8b-92fc-30f6e7332aec | -1.32121 | -54.94952 | 2024-12-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 43435acf-3ae2-33bd-b634-61d3433d11da | -3.46482 | -53.96799 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f6e6a20-8449-3449-be4a-3956b06d37a9 | -2.81658 | -53.04755 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c87e0c8-406d-3c4c-9156-5ec69c6c6b4f | -3.09676 | -53.25012 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8ab6b52-4153-34ed-8f63-d40aded196a0 | -2.99002 | -52.85992 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 439e0f69-8ffa-35b0-bafa-50223b810415 | -2.45088 | -57.92734 | 2024-12-10 05:16:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66956cb0-3f05-3128-a0a9-d54b20e8c804 | -3.07202 | -54.07479 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c89bcb0-81ab-3d3f-80da-030903cfc927 | -3.06701 | -53.79914 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc2d4837-ae5e-377d-bcd9-06bb3958acfd | -8.14107 | -54.86259 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbef2b54-58c0-3d38-b90c-4d9849e0d3cf | -1.27259 | -52.11989 | 2024-12-10 05:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb5e88d2-7f2f-3aef-9fd5-53afb122ba99 | -2.86688 | -54.22683 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1acf6ab-7971-3ec7-8a94-d1d912c30c80 | -2.78708 | -52.86132 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3af4bf44-9762-363d-926c-74eaf4efe1c3 | -3.08905 | -53.35254 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3f195ce-2664-3af5-8983-c9bc37a49b6b | -2.96357 | -53.11695 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df7ca2f0-8390-3da5-b87d-ac80c243cfa7 | -2.83074 | -53.06441 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92521fb5-767e-3ef0-8b6d-b1b6c1dfecc0 | -2.99527 | -52.85323 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db2bf70e-4a0d-3ac8-92cf-0a7614a2ca95 | -3.27732 | -51.07475 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6768cddd-d900-3b4d-b81b-490da5601fd8 | -2.83127 | -53.06082 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 768e70b3-1234-3194-b84a-d6c367096a0e | -6.65402 | -54.93914 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f17fba9-bea1-3f0e-8492-2db15da443b1 | -1.60421 | -54.88406 | 2024-12-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80df77dd-5993-3b7d-8440-f068e43382ed | -2.45559 | -53.64407 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecbf3299-175f-39c6-984f-43975d93ed72 | -2.82098 | -53.07389 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2daa06f8-d0ac-3133-b0ea-67a1ac5f1a4e | -2.3636 | -53.90954 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58421ea7-ab1f-3125-8063-a4bbb33ac28d | -2.78596 | -52.86865 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be9acec7-e4df-375c-8b87-03aebd633390 | -2.47274 | -53.63661 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d40fdf8-eac2-35db-9eb1-3e44c5befa3d | -3.68156 | -52.37861 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e08a4dac-9f87-3bb4-8938-1f782d0f1bf8 | -2.81415 | -53.06601 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b3c0512-59e9-39ed-9135-59477d7b07d4 | -3.02789 | -54.1829 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 283ee8fc-1464-37d6-a568-dd6523fdb878 | -4.38806 | -47.76021 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6b1617fd-e096-3662-a407-02b9f036f48d | -2.78255 | -53.24126 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33a95b31-1f4b-3af3-a40a-56b3848a98d7 | -4.38336 | -47.75037 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5732efea-b873-3bb1-b9f3-5818f1b01719 | -3.1008 | -53.25076 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f177b1b-56da-3709-ac27-33c4ad569351 | -3.61019 | -53.49416 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cce7dcab-2e5a-3117-a373-5f0aebd5d2b8 | -2.75409 | -54.15482 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73ddb8a1-9ed4-31a5-8eba-ea9593f23126 | -2.91855 | -52.95542 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9d89d09-1c3f-3f49-b503-118aa4ab2c6e | -3.83877 | -50.15021 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13b557a0-1a52-33d1-b60d-277c338f7265 | -2.46414 | -53.64048 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efe634df-acd6-3cb3-9569-53915035acd2 | -4.12449 | -50.42695 | 2024-12-10 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6d8d241-b915-3c57-85d1-33990fc661d2 | -2.88178 | -49.01498 | 2024-12-10 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 544f3fe2-abcc-30a5-8312-c96167500439 | -2.99181 | -53.01418 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a515bae1-9353-3335-98df-13197a080673 | -4.38933 | -47.75135 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ba2dca0-40cf-39b1-9d96-642c63386f63 | -1.65986 | -53.41494 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3557ccea-e5b6-3699-a428-44a802716bd0 | -2.22078 | -53.63809 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ebf663c-a94e-3349-be24-e7a9de1cb879 | -2.8823 | -49.0116 | 2024-12-10 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d53684b8-b39e-36d9-bec6-abb948e27604 | -3.05353 | -54.24334 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b30b9859-a442-3a02-8f39-2bbb54325b3e | -4.39346 | -47.76514 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| af8e728a-2436-3993-a322-7c6ca82703f3 | -2.918 | -52.95899 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ec5951c-12ae-3d12-8628-10f9fbef2b0f | -3.06818 | -54.07423 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6c4a3bf-448c-36dc-b4f9-81f4f452cd72 | -2.81142 | -52.97648 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 568985ff-f5c2-3415-a952-a223b583ffd5 | -1.72198 | -52.78011 | 2024-12-10 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d21b085b-77b3-3f44-8e27-b065a9c2c7b7 | -3.2077 | -46.81237 | 2024-12-10 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a076aa8e-326c-32bb-b9c4-e1cea45ebdb6 | -2.2244 | -53.71799 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f53f898-a629-3937-98a8-53f18ac78223 | -3.12271 | -54.06566 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a3e8316-0d1e-35c1-89f4-affba0582276 | -2.61547 | -54.2323 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c95efb3-ea10-365a-ba51-3efb3a8544e6 | -2.78652 | -52.86499 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f60815e6-f3ff-3242-8e06-d59c53fd97a9 | -3.94098 | -51.03839 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba2127ed-44f7-3b50-ae42-41f3315bc88c | -2.30049 | -54.00209 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07155f55-8d71-32b4-be98-60809a7dbef4 | -3.52772 | -54.69176 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7ff5e39-fc75-3c0c-bcf5-2bdac0dea971 | -3.30178 | -51.6273 | 2024-12-10 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fc5191e-afaa-33ff-9f30-968dbf5ff631 | -2.75795 | -54.16265 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 915f4b40-858d-34a6-bc1b-94f50dbf0817 | -2.99198 | -53.04038 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 159ca669-3753-3201-ac05-0374ebdbb458 | -5.70914 | -46.54938 | 2024-12-10 05:16:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77586500-2756-3bba-8bf9-18645ffe00e6 | -2.81905 | -52.98132 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 518eb59b-b200-3c2b-b6a1-0e56ffbc9a7d | -3.69718 | -50.9405 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a5fc396-7ee3-3f29-bb2d-238306989c5c | -1.67637 | -54.34557 | 2024-12-10 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9848240a-d987-3b29-a60d-e4a739c491c4 | -3.80856 | -52.24812 | 2024-12-10 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fed91f10-c095-3137-8db9-037d937038b8 | -3.753 | -52.10769 | 2024-12-10 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58d9fd2a-9f99-37c9-9239-652ac5921e00 | -2.61926 | -48.05733 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98200ab5-2933-318f-a99c-dc9e67bdbdaf | -3.09758 | -54.07608 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f8471fb-f3fd-3774-904e-d7f06e9ba9ab | -2.77257 | -44.9972 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3936484-c0cd-3de1-a4c3-be894c906349 | -3.75364 | -52.10342 | 2024-12-10 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb18e588-d619-3df7-9ee1-b97661936170 | -5.91729 | -48.05391 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62c50fae-aab0-367f-aad3-efeadc6827c6 | -2.81087 | -52.98 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 245c2155-c233-333d-9d06-3667d4372c71 | -3.35007 | -53.80391 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4076ef08-d6a6-35b6-ac07-08b65801c477 | -3.61014 | -54.30384 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa7576fd-b214-3041-92c4-0ab1327c2b91 | -3.09688 | -54.08075 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e40ec39-3771-343c-9599-a4140f05428d | -3.09012 | -53.34563 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84056205-8d4d-34fe-b620-01e3312cb598 | -2.78757 | -53.24176 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 995b62b2-61b6-3260-a25e-df2f1c4f4a72 | -5.91417 | -48.05043 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ca106ee-f7b0-367c-bbfe-3c40ebe8e278 | -2.83182 | -53.05723 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 210f5d5a-5a0c-3809-9753-1382758e40f9 | -2.93425 | -53.88617 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c6e4c51-2136-36e7-aa28-75bc0b6a5c83 | -4.04424 | -54.09707 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README34.md)
