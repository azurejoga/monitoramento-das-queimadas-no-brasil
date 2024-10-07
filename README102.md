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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 413a77a2-8b5b-3952-b7c1-9eae6f7fb8c6 | -17.156 | -57.33963 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fc0d5a9a-0488-3ed6-9eac-8c0a7c6fb7b3 | -17.15534 | -57.34356 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1d6b9456-35fd-399b-834c-fce846a3b202 | -17.15467 | -57.34748 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f7113a55-6e42-3df8-b661-a1e29cce9d81 | -17.15401 | -57.35141 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d77c22ec-a465-34bb-89e0-ad39b00c265b | -17.15334 | -57.35534 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5dfbe2fc-f0bf-30fd-8dfe-922eddededac | -17.15298 | -57.42023 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a96ae3a7-b6db-3b5e-978a-150760b97c1b | -17.15267 | -57.35926 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| da8f98fc-3a59-3d20-bdcd-04e570791f30 | -17.15256 | -57.33901 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b628602d-a548-3a94-87bd-279491607505 | -17.15189 | -57.34293 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 545a23cc-b85d-30fe-ab2e-da3031f7de8e | -17.15123 | -57.34686 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 21398bb8-41e3-36c4-8ae5-a62368db8b79 | -17.15056 | -57.35079 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 030ace9e-c457-321d-8b92-dbf55dc88698 | -17.15021 | -57.41566 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a25cbc11-6d3d-36a7-8469-96c2d77a887e | -17.14989 | -57.35472 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 981b7c1b-be61-3794-a017-a05664e5bcde | -17.14953 | -57.41961 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| e8cdb404-690d-3042-8c40-874e0e130504 | -17.14923 | -57.35865 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bed8e329-1fae-3dc7-897b-b1700aeefda0 | -17.14886 | -57.42355 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 3fa97615-b532-3bbc-94a9-4422f9b45aeb | -17.14819 | -57.42751 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 76fe3ef6-83a9-3a14-b495-e168404e0b55 | -17.14675 | -57.41504 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9da7cdf3-f5d7-3320-b3a4-bd0fe6be2245 | -17.14645 | -57.3541 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7310a062-52a0-3d22-bac0-13ed85fa8512 | -17.14608 | -57.41898 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 7b414426-2fe9-32a0-9cab-fdf6ac27a002 | -17.14578 | -57.35802 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5f36fb00-8a1c-3305-b889-8b187195e20b | -17.14541 | -57.42293 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| db8346da-bba6-39ba-b121-b9ec615cb693 | -17.14474 | -57.42687 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 451a2079-60ed-3b81-ad3e-0bf327db668e | -17.14196 | -57.4223 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7c65b6d5-0931-3387-b1bc-1604258de99a | -17.14129 | -57.42626 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 0a7ec9dc-5f80-3686-ac28-c81493ad2c0a | -17.13784 | -57.42563 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| edb52bd5-b1f6-3bcb-8bc2-0c96673cd053 | -17.85507 | -57.67842 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 163acd81-d236-315f-b5a1-21aa38f04dea | -17.85161 | -57.67779 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 95c8b890-e8b6-3bfe-be12-6b16876fb27c | -17.85092 | -57.6818 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 99bfe76e-e265-3137-847d-747c6bfe4e7e | -17.84746 | -57.68115 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7a6e0026-c947-349d-a3d0-02c14cdb9a52 | -17.84596 | -57.67768 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8d03799b-f440-346f-b0de-02be58d4e008 | -16.70886 | -57.46544 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d5b619dd-fb47-3ef2-8a4e-9b7e59cc009b | -16.70539 | -57.46482 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ea14c98b-e6f2-3e86-b9b7-c2a3d339b1a8 | -16.7026 | -57.4602 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 255d2cbb-2ce9-3e43-aed1-8de9b3eb51a8 | -16.70192 | -57.46419 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 43bbc0a2-34c3-34b3-a1e2-57967e7ba084 | -16.70124 | -57.46818 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9af6a1fd-86d1-36bd-b927-0f6ba77fce5e | -16.69981 | -57.45559 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f5a0fab0-1832-39fa-b71a-f1cd4e080730 | -16.69913 | -57.45958 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 14dd5480-8f99-3ca0-8c19-c318f9711959 | -16.69844 | -57.46356 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2428ae10-3e92-387c-8a5c-b3b186961e18 | -16.69287 | -57.45433 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e8723732-cc94-3fb1-b724-4b3e9c1bc0c3 | -16.69218 | -57.45832 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e25556e5-f2bd-3f2f-80b6-9b010202718c | -16.69144 | -57.44175 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2d962dfa-1d67-39ec-8870-485bb90a5040 | -16.69076 | -57.44574 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 65255bf9-c910-31e8-a3c0-c1b51a71c5a9 | -16.68939 | -57.45371 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8b5844c6-a5ba-35c2-9c22-8fa57a828bbd | -16.66273 | -57.45317 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62eb6c87-63f9-3f6c-a96a-900ba704f9ff | -16.65366 | -57.44331 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 98690b7d-1fe3-3563-b0da-9694ceb302bc | -16.64459 | -57.43344 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8d67584f-4d7c-383c-9323-6428be50ace9 | -16.64392 | -57.43744 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fd4885b9-a3ed-3cb5-9b12-89bfd734c0f7 | -17.13438 | -57.42501 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3c7f6f3d-99d5-3c47-82dc-25f00bd827e4 | -17.13093 | -57.42438 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 98c46fa0-5af8-3f06-8692-71f11602c7c9 | -17.13026 | -57.42833 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 30b34263-2a76-3418-9ac3-13e732357c9e | -17.12748 | -57.42375 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9fafa80d-8ce0-3d66-b2ad-ca7038762c87 | -17.1268 | -57.4277 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 145ad2cb-a587-3128-9e0b-5a86dd8a0930 | -17.12517 | -57.42411 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fbf99088-b2e1-38fa-9310-4fa6783ec9b5 | -17.12403 | -57.42313 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d2f086d7-23a1-349e-a48c-7c563b5a3f4f | -17.12335 | -57.42707 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 337e9361-df98-33dc-b0df-35ee9706d0db | -17.12172 | -57.42349 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a43c2811-da95-3486-9930-2d09c4e52b99 | -17.12106 | -57.42744 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b2d73f2c-a18c-3dad-9ef9-fc7d96c6b1fc | -18.70277 | -57.26635 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c56eae43-be8b-3e56-be1b-0cb829cc7e93 | -17.11761 | -57.42682 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ec5fb006-8b02-3103-8e39-ed755a2093c8 | -17.11481 | -57.42223 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| abc6dee5-2635-39b3-8287-3d70b9fd4bb8 | -17.11334 | -57.40976 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 869eff50-726d-34e7-883f-ec3f75d2a49b | -17.11136 | -57.4216 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cb54e0dd-e907-3602-82b8-8c44709cdeb5 | -17.10724 | -57.42494 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| efdf815e-04a8-3340-9b96-dd3511825448 | -17.10577 | -57.41246 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 46da3fb6-7405-3508-b769-eabfd4468982 | -17.10431 | -57.39998 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| df4263fe-4505-3ff9-9281-69e3848f0aa6 | -17.10379 | -57.42431 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cfae7351-ed51-3bcd-8d85-32a611576872 | -17.10313 | -57.42827 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4cf38ece-2fd6-3c18-ac84-a4eba8516ed1 | -17.101 | -57.41973 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 757113bb-8e40-3a9c-b893-81837476e64f | -17.10085 | -57.39935 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 400292f5-01bb-3efd-a3c9-4d0451710d00 | -17.10034 | -57.42369 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2035b6f8-eb99-333c-8250-3378d15d1932 | -17.10019 | -57.40331 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d972f098-3f28-367c-b916-f6caca095465 | -17.09967 | -57.42764 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7446885d-5fae-3077-87ab-5a64adbd21c7 | -17.09953 | -57.40725 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fae55eed-cc56-37ac-bd0c-7a499ef4abcc | -17.09755 | -57.41911 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| cf59e0e1-35e6-3abd-9a76-3ff0d68b53f9 | -17.0974 | -57.39874 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 39090dd2-f727-39c0-ab09-ce7ce950036f | -17.09688 | -57.42307 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| b0306cb3-342b-33b6-80e0-0672d1773397 | -17.09674 | -57.40269 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 29772d00-8c02-3c56-a7f1-9224ce749b35 | -17.09622 | -57.42701 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 2405103d-a195-381f-a6fa-fb3f7801ad20 | -17.09608 | -57.40664 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a7f666dd-6e83-3a1a-8bff-4d05fe3d292a | -17.09343 | -57.42244 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 22138683-77ac-3f14-add9-1b7b9525bd92 | -17.09277 | -57.42639 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d097f202-23d9-309f-8750-9854fd0130d8 | -17.08998 | -57.4218 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 84ae162f-92ae-30cf-a92c-120a8a114d7f | -17.08652 | -57.42118 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 36b300fe-404c-375a-a514-1af93d468c32 | -17.08506 | -57.40871 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 24a935f1-d3f5-3182-ba4f-1596a37fa9ea | -17.0844 | -57.41266 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dece2dec-234d-3559-bd8d-0a2ce6bb43a7 | -18.70002 | -57.2619 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 907bca7b-1537-3759-a1f3-5781c6768157 | -16.91802 | -57.47688 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d9c5782f-09a2-36c7-9a06-bda23203106d | -16.91734 | -57.48086 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0b082f94-a3b4-3ee8-af69-13b2965013cf | -16.91726 | -57.69211 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 453a7e49-3d9c-39f3-a5fb-bbd9820078a3 | -17.84116 | -57.68507 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2d0cd92d-efaf-365e-9ff7-c55c82f962fb | -17.84678 | -57.68515 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c0bdf719-f28e-38a0-9d12-8b4740f1a9d5 | -17.84331 | -57.68452 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 57ba9cae-e326-3345-9bac-42fda8b376d4 | -17.04379 | -58.0361 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 29abc510-81b8-37ec-97f9-3b57b374c18f | -16.93336 | -57.70341 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 37dd3add-566c-3c8d-95e1-7615fdaa40db | -16.93268 | -57.70747 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c76c5160-71a2-3676-b446-63d28082aef1 | -16.92987 | -57.70277 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 524bae73-53dc-3693-81eb-8eff1d8b1913 | -16.92918 | -57.70683 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7b321258-3a95-30bc-9e43-03a763ecdb89 | -16.92774 | -57.69402 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c4ac937e-34aa-3949-8a3c-2aa52315a024 | -16.92706 | -57.69809 | 2024-10-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |


[Clique aqui para ver as próximas entradas](README103.md)
