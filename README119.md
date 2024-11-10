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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6298287b-8070-3bf6-af8e-18d4300a50e2 | -2.9355 | -51.482 | 2024-11-10 05:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4bd274e5-9cfb-3d81-b4db-4437cefb597b | -3.1422 | -50.4562 | 2024-11-10 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| a7373525-7ee7-385b-8047-2172a92a33c1 | -3.1239 | -50.4358 | 2024-11-10 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| ea091f00-ea24-31bf-8728-4a2581279630 | -2.8802 | -51.4835 | 2024-11-10 05:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 66e24025-c577-3d6b-ac5e-0051407f565d | -2.0953 | -48.8338 | 2024-11-10 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| e73da593-90a4-3cf2-809d-2858b007647e | -3.1423 | -50.4352 | 2024-11-10 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 205.5 |
| ab57f140-ceda-3f49-9f7e-0b05c2239446 | -2.9494 | -52.7748 | 2024-11-10 05:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 4db2fc72-8f37-37f3-ba48-955356287fbc | -2.931 | -52.7753 | 2024-11-10 05:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e2746e30-ec88-3247-a18b-3f2668a10829 | -3.9668 | -48.1932 | 2024-11-10 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 40196832-7317-30dd-9de5-de18f6782fc4 | -1.5347 | -52.2104 | 2024-11-10 05:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 39a01d27-e181-3622-90a2-0fc990eb46f8 | -2.8618 | -51.484 | 2024-11-10 05:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a08c80d0-4ccc-39ed-bd11-e5526b31788c | -3.9669 | -48.1716 | 2024-11-10 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 3858be64-3396-3d44-a34c-af63fbaa2776 | -3.2243 | -53.0727 | 2024-11-10 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 83c2da33-2476-33d4-aa0c-2ea0c29e86c6 | -2.7772 | -49.3492 | 2024-11-10 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ec5df5b2-d04a-34fe-aa02-b4e745f5ec06 | -2.9494 | -52.7748 | 2024-11-10 05:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d4b89b46-8c27-3fb5-9ebb-104b3555a887 | -3.9669 | -48.1716 | 2024-11-10 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 68e887ef-b620-3267-8956-997c274880cb | -3.9668 | -48.1932 | 2024-11-10 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6f287345-2610-35de-aef3-b4094eac3476 | -3.1239 | -50.4358 | 2024-11-10 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 48eefaf8-d08c-3b5b-abdf-41923971f7c1 | -3.9485 | -48.1508 | 2024-11-10 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 84372a2f-d7ec-39bf-b0a2-1b7e8a51fad2 | -2.0953 | -48.8338 | 2024-11-10 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 83530519-b836-324c-a694-0f62e98a915a | -2.931 | -52.7753 | 2024-11-10 05:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ce984610-4ffe-32af-ba15-50b8f33fe711 | -2.9355 | -51.482 | 2024-11-10 05:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c973002d-4c50-3e81-acbc-204586a2485b | -3.1423 | -50.4352 | 2024-11-10 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 193.0 |
| 1f1d0d72-e92f-3120-9e74-5bd17f3a7891 | -3.9483 | -48.1724 | 2024-11-10 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a091da43-44e9-3af6-b3a1-2deaab99e1b0 | -2.8802 | -51.4835 | 2024-11-10 05:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5f31b20a-8cb2-3d17-8ccf-fc4ef997c9bc | -3.2243 | -53.0727 | 2024-11-10 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 03454c06-ba6c-357e-b0cf-c07594be9fda | -1.5347 | -52.2104 | 2024-11-10 05:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 50081daa-20e0-34bf-b28b-9d8f2833f984 | -2.7772 | -49.3492 | 2024-11-10 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6cbe98fb-6897-3043-b3ec-e609011b879b | -3.1422 | -50.4562 | 2024-11-10 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 242d8a68-ef54-37a3-a8ed-d21928e0c8d2 | -3.2244 | -53.0524 | 2024-11-10 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| de762ed2-79f9-3e79-9538-1e670bd91f62 | -2.7587 | -49.3497 | 2024-11-10 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 337d5db2-0d58-3692-aac9-fc259ea6c0a2 | -3.1238 | -50.4568 | 2024-11-10 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c25add5b-d583-34f0-b132-aaa006cca9a3 | -1.5347 | -52.2104 | 2024-11-10 05:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 8218f74b-5d30-39b0-a431-2ebc7995ffe1 | -3.1423 | -50.4352 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 2a7d39bb-7b5f-31ab-a0d5-693642979dbf | -3.1239 | -50.4358 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 01479662-9cd8-38cb-b829-62428e7b0b75 | -2.8802 | -51.4835 | 2024-11-10 05:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 49ae3fd3-6587-3f28-bb7a-817b0733f3bf | -3.9485 | -48.1508 | 2024-11-10 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 246b035a-1fa8-3735-88bf-b6700198ee44 | -3.1422 | -50.4562 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 7135cf29-45b1-362f-9a63-4cc5ebf8aadb | -2.0954 | -48.8125 | 2024-11-10 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 19be57f5-b387-3450-b62b-417b52271def | -3.2352 | -50.3065 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 655c3585-2eed-3f2a-93c7-61c97573c637 | -3.2536 | -50.3059 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 2321c5cc-d675-3b19-a1be-8adc12b99259 | -3.2352 | -50.2855 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| d63c51d0-5716-36df-8fd0-4a0e6cb4c5dc | -3.5064 | -44.0294 | 2024-11-10 05:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| e49aaede-4681-34b3-957f-0c91254dff9a | -2.9355 | -51.482 | 2024-11-10 05:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 5def6f08-9f3a-3c66-bcb1-e77778247946 | -3.9669 | -48.1716 | 2024-11-10 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| cc58ec87-257d-3fb6-b60c-077ec28af573 | -2.931 | -52.7753 | 2024-11-10 05:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 5cc1101c-1315-3c33-bdca-650c6d6ccb07 | -2.7772 | -49.3492 | 2024-11-10 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f7f88777-3a47-3284-9899-eadcdceaa142 | -3.1238 | -50.4568 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| a3215891-c8e1-38b1-90b8-2347d33a9b61 | -3.2168 | -50.2861 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ea3b9341-dc4a-3fa0-9743-bbd7722886f2 | -3.2244 | -53.0524 | 2024-11-10 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b91328ef-ea5a-321c-8401-5515376ae842 | -5.9788 | -45.3621 | 2024-11-10 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d4ab19cb-0c37-3a36-b9de-23fdb100db3b | -3.2353 | -50.2645 | 2024-11-10 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a9a1c9f1-2efa-3afd-9a46-c33c4ebd0111 | -3.2243 | -53.0727 | 2024-11-10 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 46a3f485-ad9e-3b5e-95c7-48bbcfa3323e | -3.9483 | -48.1724 | 2024-11-10 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 40f1c13d-ea4f-3297-84cc-59b19fbca094 | -2.7587 | -49.3497 | 2024-11-10 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 71d7c0f7-f871-3680-9e12-667f3a4c07cd | -2.0953 | -48.8338 | 2024-11-10 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b81e45cc-168d-349f-9b96-6cd99a97438b | -3.2243 | -53.0727 | 2024-11-10 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bebfdcf2-c77c-3384-9ab5-aecf63b31d0e | -2.7587 | -49.3497 | 2024-11-10 05:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1c417d81-dc6b-35f3-8c72-a6e0d16e63fa | -3.9483 | -48.1724 | 2024-11-10 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3a3e670f-347d-34ab-bf59-a29d443514bf | -2.8802 | -51.4835 | 2024-11-10 05:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 23d8c4e3-aed5-323a-80f9-7fae7c248038 | -2.7772 | -49.3492 | 2024-11-10 05:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a00c9ca0-1fbd-3e96-838d-fec18b23ded6 | -2.931 | -52.7753 | 2024-11-10 05:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 5f9b3fc4-d20a-313d-b994-240729a18d8c | -3.1422 | -50.4562 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 812eb005-4f79-3090-8082-773390a1b1a2 | -3.1238 | -50.4568 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 01038458-7905-337a-895f-390067aac5a3 | -3.2244 | -53.0524 | 2024-11-10 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1a2bc5fd-1919-3f2b-9f51-4b16b8054a4f | -3.1423 | -50.4352 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 0aaafcc1-dc02-3d86-bce4-7717ed673c66 | -3.525 | -44.0286 | 2024-11-10 05:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 81ea349d-5ca9-36fb-8330-9e109425fb35 | -3.2353 | -50.2645 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 17c976dd-d464-37b8-84dc-3b45600d3c5e | -2.0953 | -48.8338 | 2024-11-10 05:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 33ddd91c-5483-324e-a0d6-61302a803f27 | -3.2352 | -50.2855 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 4204f7e8-b295-3fcf-b50a-94914f822a09 | -1.5347 | -52.2104 | 2024-11-10 05:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| af5d7fad-3395-3c21-a5c0-ee3a4e28e7ff | -3.2168 | -50.2861 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| a4c54cc7-e2ad-3811-8dd3-82745fc85cb4 | -3.2536 | -50.3059 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 87935364-4e49-37a6-85a0-ac28ee5bae53 | -3.9485 | -48.1508 | 2024-11-10 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a1ab3fa4-a4bb-3d74-b469-29d2181a756e | -3.9669 | -48.1716 | 2024-11-10 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ca5ef6ea-ff83-306b-a77a-f95dc99b47a8 | -3.2352 | -50.3065 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 6306aa96-d844-31b1-840c-7d5b6b906af1 | -3.1239 | -50.4358 | 2024-11-10 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 55b6333b-8e76-34ea-8ff9-5e3efa4d1ab0 | 4.85571 | -60.02277 | 2024-11-10 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ebcc0fe-f86b-3467-beaa-43a412020b4a | 4.85644 | -60.02725 | 2024-11-10 05:52:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a89c006-2a12-34cc-bbdb-9bbb910f6fe2 | -1.15209 | -53.78916 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 942691a1-88ca-37c9-a5d9-d807e2865ca0 | -1.48793 | -55.43603 | 2024-11-10 05:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0731e2a6-866e-3f73-a89f-61188f7ea526 | -1.3848 | -60.35406 | 2024-11-10 05:54:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c0f85ea-23ec-3e0e-afdf-b8633b29c0d6 | -1.427 | -55.26794 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9841d2a-0f8c-3ed5-aaef-28cea6dbde9d | -2.0821 | -54.68156 | 2024-11-10 05:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 45de8d87-a93b-38fa-b825-143a8d06f207 | 2.85101 | -60.08532 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7683e1c7-b216-3876-913f-345d14c93bf6 | -1.48217 | -54.30337 | 2024-11-10 05:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a52f96b9-4063-3b6b-9abb-91f0f8db104f | -1.44377 | -55.51074 | 2024-11-10 05:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fc02e6d-d0ed-3334-a76a-f45f48e47961 | -1.48713 | -55.44129 | 2024-11-10 05:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5719c3d6-8f30-3d60-bc6b-6764d38ab005 | 2.85315 | -60.07423 | 2024-11-10 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c1ded01-fd7e-363a-9119-4debb9d07be5 | -1.43352 | -55.26884 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69272d86-13ae-3b56-8dd5-688824c69a14 | -1.421 | -54.7677 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e9dcf46-96ee-3166-ba77-0ad6a4b7db82 | -1.34014 | -54.62773 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b7446b2e-c258-3ed1-8f16-da18656ac749 | -1.5212 | -54.99168 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fad0c741-ade3-3806-b069-ab0cbdfa6c42 | -1.42019 | -54.77314 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae5587f9-9f1e-34c0-9bbb-adda88844bdb | -1.30778 | -54.67481 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ac6beef-8105-3ef0-99d4-9546a7726d8a | -1.41664 | -54.77412 | 2024-11-10 05:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e68478dd-992b-37fc-972d-9d938afcbda9 | 1.57632 | -55.97857 | 2024-11-10 05:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2059b08f-b3dd-3a83-bc47-170d023a5357 | -1.28865 | -53.71091 | 2024-11-10 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 34990f3d-4b3d-3219-bdf4-b7cc0b266f9c | 1.1295 | -59.4416 | 2024-11-10 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed25ef98-0b91-3ce6-9ec0-d9c420bb48ee | -2.08419 | -54.67986 | 2024-11-10 05:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README120.md)
