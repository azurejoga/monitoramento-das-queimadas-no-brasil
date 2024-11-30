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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b660c1b-4aad-336a-8ea4-b7f03f248e26 | -3.26801 | -51.62363 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cecde643-2476-30e1-b108-8d10f8e0971a | -2.72584 | -46.28896 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b879c257-70ca-31c0-9725-4355016c5229 | -4.37001 | -45.52388 | 2024-11-30 04:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d96f2813-4b63-3c70-bd6f-ddde51cfdcbb | -3.25256 | -50.40092 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab5ad020-4141-3dcd-b416-21c7b10c6dc7 | -1.67357 | -52.4963 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b5453b1-b2d6-3171-937c-42d29f84b546 | -4.05681 | -50.95256 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c08da096-deaf-312d-921e-4f80218ef1fe | -2.80247 | -54.1258 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e6fdd6b-11f3-36fb-b9cb-6e22cbd44a9c | -1.66483 | -47.72293 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6222dab-a8b0-3371-9d0b-afc368e0cc0c | -2.279 | -46.43676 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a36da1-6565-3dd4-9247-d7907cad0473 | -3.20107 | -48.58297 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ea66de1-3b8d-3758-b457-34b9daebf3f4 | -3.49588 | -50.45724 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 919e2e03-1dd3-35f8-b7c5-4cd78fc66e89 | -1.97265 | -46.44599 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7249cdbf-4a76-3bc2-82d5-dbadc0e05fc3 | -7.21549 | -39.77766 | 2024-11-30 04:40:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0b79dfbc-86dd-3bfd-8f13-654d2b2ea437 | -1.09901 | -53.39299 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed79514c-a6a5-3bb1-aea1-d3a430b01a3c | -1.17194 | -48.15639 | 2024-11-30 04:40:00 | NOAA-21 | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac19f462-1df3-3ca1-9f52-7b0902c5293f | -1.15749 | -53.68573 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3549532-dee5-38c5-abf3-3c6c83b2b351 | -2.86166 | -54.04262 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96cf4cc9-7fbe-3855-9ee2-c938ad0bb4c6 | -2.88174 | -45.51343 | 2024-11-30 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72524c02-5899-34e2-9b6f-01da8f6a380e | -2.74946 | -46.11125 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea4eb963-e4e6-3220-8a6d-6b2eff0e2820 | -2.36097 | -49.06321 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38ea924c-a7b3-3980-ba4b-5bdea0a58760 | -3.80206 | -46.68423 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05750b11-4467-3f95-90d3-28f1b2deb347 | -1.41084 | -52.61314 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 502e918a-65c9-356c-8eb9-b88ad24e4ed3 | -1.75057 | -50.54861 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ffd215a-8873-3ea4-80b5-b7496f0de783 | -2.70099 | -48.66987 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31682bf4-c535-3b85-8b14-63fd4b7eb520 | -2.71644 | -48.67928 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6ac81b6-4022-39cc-8eae-6f3b98c727dd | -2.65305 | -46.12609 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e380853f-225e-319c-879e-83208a5e386c | -2.54832 | -48.18725 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c4b8035-5287-3385-91ab-90e0b8b904d4 | -1.3033 | -51.73035 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e03f60f3-de2e-3197-ac53-33abaeb55310 | -3.30552 | -54.16526 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f891ea56-aeea-3e1d-8966-068e5bd4f88a | -3.41646 | -50.24817 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32520e2c-5189-3cea-beb6-941a4f876c7b | -4.04826 | -48.33876 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a33bbce4-6aba-368f-b244-eb4777306cba | -2.57286 | -47.01174 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4710c6-c5d9-3c29-89ba-ba48d841996e | -3.34667 | -46.6093 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 960b87aa-0881-319f-9112-b2f1f3024c94 | -1.26035 | -51.7592 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3c5436c-eb72-3d6c-aeb8-f1f55b6a31a3 | -3.26623 | -50.20621 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cae456d2-65de-3b3d-99ba-2b51e3c1bd37 | -3.07426 | -50.3259 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f22f26e2-790d-3746-93e8-d7d9a1f7e82d | -2.72482 | -46.24874 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3604ef87-c358-3120-b18a-4ef36d3d3e73 | -2.6001 | -53.98235 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f09bee8-fb1c-3b6b-8666-4490e48cd94f | -3.85619 | -47.05968 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 679809ea-cc61-3924-87f6-7d10e738f55b | -4.02318 | -48.87341 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 776016a1-5695-3cde-8e63-46a6eba0e743 | -4.13582 | -48.93663 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37b7ea8a-5ec9-372e-8b83-e0101030b732 | -1.23569 | -51.7983 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc8f4c27-bf5d-3fb2-81b0-30ab3a7cd683 | -1.15398 | -51.69708 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bfc27b02-2b91-3261-b784-8d8b0b39be45 | -1.53525 | -51.6167 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa6c0e07-7da2-3234-99f4-ecb1c0a6ab68 | -2.80829 | -54.06369 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3095e90-9f71-3271-9c0f-cd71a11eb09f | -3.23169 | -53.63309 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ff4d48a-e34b-32f9-912e-7f3089881913 | -3.24127 | -51.56004 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77580d36-bc0c-3c59-90e4-6139e32889dc | -1.65746 | -48.20782 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a8d3657-2cd3-3392-842d-dcedcb3c26fe | -1.70112 | -47.97079 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aae5382-50a4-3235-8951-f98214fda27a | -2.69154 | -51.98418 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3430cb3c-44c5-378e-ae76-2d900dc64d18 | -3.02252 | -53.40742 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 635c9969-44f6-312f-9fe6-fcec6d9d2d91 | -3.05942 | -53.67636 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d6c9eed-416a-390c-a386-73c32d79eed0 | -2.71384 | -48.58743 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67242c35-337b-339e-8887-5ec015308f61 | -2.85042 | -48.10283 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06298461-2bfa-3aee-aad4-7603b4a04846 | -2.32077 | -44.82722 | 2024-11-30 04:40:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2b0c1a9e-c10c-38cb-9159-337c3656773d | -3.15169 | -53.82741 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b534314-38c4-3ab3-8150-7e8049b89cb5 | -2.11034 | -46.55077 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0567b871-e62c-362b-ad05-c97622323045 | -2.20603 | -50.44212 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1390df77-dcc9-3b5b-81c7-a343442b68f3 | -3.01977 | -47.79982 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1048d5cc-8238-3e94-b883-481e870130c1 | -3.14656 | -53.83374 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3594b015-0d84-3abc-967d-a76c83596a85 | -4.05812 | -49.06198 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cb3d0839-7b7d-349d-a69b-81f685d22449 | -4.53495 | -46.41888 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8137cff5-cbfd-399b-9751-cb00f093b299 | -1.69559 | -52.45361 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c85296c2-e605-334d-85e4-4c869b63d448 | -2.46485 | -46.57265 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b65d7339-02b2-3042-a95d-d365d7aa3c84 | -3.23838 | -51.55557 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39a307c3-a8c1-3ccc-907b-622f6efb933b | -1.58687 | -52.28313 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edf17b7f-6ea9-3124-bdcb-be62b1d6ca4d | -1.70836 | -52.76757 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a0b3e16-76a8-3ab8-a5d2-b5978a302e71 | -3.8286 | -50.13557 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae1cddf1-29cf-30fa-a295-a2cd2ea635a2 | -3.32877 | -50.22312 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e0a5d3-c8fa-387f-a9d7-f93bea95b2d3 | -1.9984 | -52.09774 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8aade9e6-fecf-3170-b47a-3c924b19f108 | -2.74975 | -48.61759 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88a849ec-85dc-3a74-b408-d41e43f1b128 | -3.34442 | -50.74889 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5e5a0f91-880b-395e-825e-4ffc003082d7 | -3.5798 | -50.3315 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f705a825-35e4-3213-aaf9-705eff17a123 | -2.43779 | -50.39639 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45473290-91a8-3b94-9357-683984850cb9 | -1.0884 | -53.35635 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4577e23b-5c0e-387f-a8b0-d0baef41d9f0 | -1.09186 | -53.36036 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c90684f-00f0-3464-bbea-b787dcd3e9ef | -2.14775 | -50.61306 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40cfd24f-18db-3fc3-b470-fcb466efab9d | -3.29089 | -51.15476 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45363377-1b55-3cd1-b1b2-2bbed9ebca8e | -1.32367 | -51.74195 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94cb5179-fe66-3d85-974a-681aba8e8c03 | -3.98076 | -41.52275 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6eb8c563-d6d6-308c-8359-5e8dd163319e | -2.19644 | -48.41492 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e6428b2-f940-37df-aeaf-bae10fcb0995 | -1.53966 | -49.26663 | 2024-11-30 04:40:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c21080b9-22e3-3c95-97ef-fc7f290c6c65 | -4.11739 | -48.48473 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e64430d-bee7-3fee-9e04-bea045829ab0 | -1.25746 | -51.63552 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24e98cf6-1d2b-3b8c-8e6c-2ee051ae9b82 | -3.93628 | -48.13863 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f3f39ba-d57b-32eb-8dc9-c17d23101925 | -3.94902 | -46.725 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8bcc384-bed3-3df1-9e5e-d195df675512 | -3.96974 | -49.91043 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94d3505b-6c2f-3957-a179-de0d75b60d8a | -1.35198 | -51.96588 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e92d2d1e-a60b-35f2-b321-226ce8aaffce | -5.52258 | -45.40503 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72bfdc31-69eb-38d1-a478-290752b99bf3 | -3.03656 | -47.99996 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5231ee6-d2e4-3dff-8ce3-20bfb649a070 | -3.97509 | -47.24449 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 332db982-b7fd-3fe7-965b-c1ed8fabebff | -2.23161 | -46.39816 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 208048ab-a413-3b26-8faf-8e4232ba7db6 | -2.31091 | -49.0765 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf666743-03c8-3cc0-b9cb-f215d128a9e5 | -3.13077 | -51.12194 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81db2b67-49b9-310f-b109-c2cdbb708525 | -3.52336 | -50.4799 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a94b7ee5-7d06-382a-9209-c07d55a70117 | -3.4733 | -50.53463 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fd669db-7b4b-34ff-a001-c65de9e46b15 | -4.88445 | -41.29639 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| e6983996-a3e7-3ddf-ab7d-e22be9f23ce8 | -1.95994 | -46.25235 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d20459e-21a9-3ea5-beb8-be9311748b9a | -4.04083 | -46.85965 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c18f8a8-1b37-3cb1-b43a-344be291385f | -3.0922 | -50.34331 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README66.md)
