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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34aff98-1940-38a3-a366-6ae71864a22d | -11.81992 | -47.55205 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a2a6eed-18b2-351a-815e-1b4896d9563b | -19.7182 | -40.35415 | 2025-06-26 03:49:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11d75d4b-2f61-3610-aafc-cd3eaf4d0cbe | -11.81316 | -47.55825 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce135fee-3c43-34e4-ac1f-2d3294971fd6 | -11.23449 | -49.49931 | 2025-06-26 03:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e8f7516-6abb-3326-ba1c-26d410e04f85 | -6.84126 | -43.37571 | 2025-06-26 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e28b1f86-64a7-3692-ac6b-85f5afd7d49a | -12.80778 | -48.73413 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afe05cc1-722e-3ada-8bc0-9892a32bfbc8 | -11.57996 | -46.91198 | 2025-06-26 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69f4f422-3a0b-3075-8a86-f230df3a4cc0 | -6.17936 | -48.07495 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ff7acd7f-9165-3082-bc0e-a7d96158034a | -6.21608 | -43.36367 | 2025-06-26 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11ec4670-d85f-3cd5-95ea-17f21593e9b2 | -13.03631 | -48.82978 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c965df8-8cfb-3721-9171-2a1e3a0133a5 | -15.56711 | -47.85564 | 2025-06-26 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6437cfef-b124-3c70-8378-a55b74afcc0f | -7.93938 | -44.87463 | 2025-06-26 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9a2767c-669d-37f3-be5b-b6598f122464 | -11.83712 | -51.26485 | 2025-06-26 03:49:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3cd132b-989d-37d8-9197-4f5b7b16ecbb | -14.3783 | -50.3318 | 2025-06-26 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d40b872-d640-3cfa-929e-dee71a5e593c | -8.05903 | -43.10476 | 2025-06-26 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 860b9986-3f44-3b90-bb4b-7a84c535d20f | -11.95362 | -47.0234 | 2025-06-26 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba21895e-45cc-377a-afcf-23c1862753c2 | -5.9043 | -43.45233 | 2025-06-26 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc23b4ee-2749-333b-b4ca-b286244eab99 | -7.35819 | -46.23674 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 579e2b2f-60d1-380d-b887-21266ee9f7a4 | -6.17847 | -48.07997 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 88b03355-5f37-317d-bfd1-f84dd5c1982f | -14.41176 | -47.87888 | 2025-06-26 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b61e40b-3c03-3f94-91ee-8c19b35822df | -12.02709 | -47.77493 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 051ce349-9305-3fbc-974f-b37a221da85d | -12.02643 | -47.77839 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b40c0103-5bee-37ae-afe4-f74f5648c7bb | -17.229 | -46.08244 | 2025-06-26 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 846e0c7b-7136-33b4-857d-7aaf56ace973 | -5.90162 | -43.44826 | 2025-06-26 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ac1810c-4092-3880-a811-45caec63653a | -11.81597 | -47.54366 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5192d00e-21b9-3420-9a16-1111c2b89fb4 | -15.80534 | -49.9607 | 2025-06-26 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 88d2a258-722d-300b-a4f3-0ef90a64b31e | -11.36698 | -48.70498 | 2025-06-26 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51500b58-29d1-35e5-b204-1f95f4da794c | -13.04044 | -48.83088 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01e7f036-7aae-30a5-9253-76077aa97512 | -12.80696 | -48.73829 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a528cb1-942c-312d-a5ce-12c1792780a7 | -11.83039 | -51.26351 | 2025-06-26 03:49:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcd1a211-d1e9-3db2-8e54-ee6e65d41194 | -12.78907 | -48.73897 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27c960fd-f654-3bc7-a312-3abcfa55c60c | -13.04204 | -48.8227 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 156f8ec2-a11a-3ba3-9d44-1f3f74c3c1d9 | -17.22468 | -46.08102 | 2025-06-26 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac44fe0f-6068-3739-8122-3f265d516dc7 | -13.03547 | -48.83387 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5155c6bc-7477-3151-abf9-ddb722c298b7 | -6.17667 | -48.08915 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9e2d2ab8-b086-3dc6-8853-c33c7d4ce77f | -7.36209 | -46.23396 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b56dbb3-7cfa-3fcf-b78f-c9dc8832a13a | -11.82493 | -51.25604 | 2025-06-26 03:49:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21fc1222-4005-37ea-8474-34aae91d1e9a | -8.06329 | -43.10551 | 2025-06-26 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0369b6b0-4d5d-3c6e-a61a-60147fe0d0f4 | -13.03555 | -48.8256 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0687b7cc-7e24-383e-8f19-69fa5b1fa502 | -12.79481 | -48.7399 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1531dcb7-7bc3-3c65-ba1a-3b4ff07c9eec | -12.04799 | -48.07853 | 2025-06-26 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8691b17-f591-3f24-9fb3-2058ab7c28cf | -13.03714 | -48.82568 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73b8a3ae-ceea-3131-924e-0451c66bb283 | -11.56898 | -52.10373 | 2025-06-26 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7efe4f7b-22e0-35ee-a2f9-c0f62af5a60e | -13.04937 | -48.82388 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3576005c-e607-398d-9a78-c4bd5243f0f4 | -18.14575 | -47.80364 | 2025-06-26 03:49:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d5ff8a-bf2b-3ef7-be7f-79b54565383b | -13.09603 | -52.29195 | 2025-06-26 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74231b98-36ef-3cc3-8299-0b021e8b1ec3 | -12.7956 | -48.73591 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d539c56d-7ebf-39c2-a6ff-377b1386b2bb | -11.23642 | -49.48958 | 2025-06-26 03:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f1630e1-ab23-37cd-8bef-7e2793d2e122 | -11.5732 | -47.4346 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0ff5ebd-c434-3f85-9b45-30f201f5cfaa | -14.40162 | -47.87519 | 2025-06-26 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8a44a1c-2cfc-328d-a6d3-b7d290cc97c5 | -7.3627 | -46.23066 | 2025-06-26 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b23acfe-cb5e-3db4-be71-8976c4173cbd | -13.04201 | -48.8309 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e3557f2-78e4-370d-9715-1157a7f4a569 | -17.60004 | -48.42648 | 2025-06-26 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aa58ea4-5b91-376e-bfe3-816828ca98d2 | -13.04774 | -48.82386 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96638327-a2cc-3829-bcb8-3dfc7fd3b9d0 | -14.37935 | -50.32688 | 2025-06-26 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80002e24-c4b3-3da5-b7a2-810b164960e2 | -11.93299 | -47.84879 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caf76fcf-94da-3656-8cbb-4d4ecd215a57 | -13.10299 | -52.29348 | 2025-06-26 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bf9e250-f8f4-36da-9ab5-4d9a73eeb8d7 | -11.57932 | -46.91527 | 2025-06-26 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e26c75c-be64-3367-823e-de009eb74e24 | -7.31214 | -45.76197 | 2025-06-26 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a587c9c1-f3c9-3a31-9575-70683c5cbe52 | -13.09965 | -52.29937 | 2025-06-26 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d0fb2c8-f81a-3bb7-bc66-de3315a135cb | -7.10614 | -47.84592 | 2025-06-26 03:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ede45a9-73b8-3b1a-8676-a04c02de3435 | -12.04249 | -48.07729 | 2025-06-26 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b841a671-7e63-37dc-bfa9-0f2ada892eca | -17.88732 | -43.99006 | 2025-06-26 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 535cdeae-1bf3-3764-a4c9-e0fec16431bb | -14.41227 | -47.87629 | 2025-06-26 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a448d3a-30f6-3d42-83b1-429ded974862 | -13.04124 | -48.82679 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1ca7b68-50cc-3aba-b743-caf38fb23b34 | -11.57645 | -47.43269 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d06358c8-ee6e-3522-8a42-6e702064154f | -11.57112 | -47.43156 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d2abe29-5405-3479-81d7-95713cbcb4c4 | -11.80856 | -47.55318 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b0556f5-c412-31ee-8139-43df10f922c7 | -19.62939 | -45.18852 | 2025-06-26 03:49:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a6845a3-a902-36a6-8cca-8e9ccfa93b1b | -16.04325 | -43.81498 | 2025-06-26 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 833e40da-619b-3b9d-a89d-64bea456e7d4 | -6.9596 | -42.81047 | 2025-06-26 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2e477716-4438-3e41-affd-762a644984bf | -12.04176 | -48.08101 | 2025-06-26 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80d648ea-0b28-3800-b0db-0179504557a2 | -11.57067 | -46.89885 | 2025-06-26 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c1cfa30-e4bf-3903-94f3-0e9aa54939bd | -7.31895 | -45.75352 | 2025-06-26 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 621d5878-741f-3643-b8d7-46fc12ca2211 | -6.17672 | -48.08987 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 49d0bd24-ea76-3e62-9691-c2de1a255ab0 | -11.79383 | -47.54294 | 2025-06-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa0d35a6-f68a-315f-b18a-1fb075bf2b07 | -12.78988 | -48.73495 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de3a9910-bf43-3ac8-977d-ec9cd127ca0f | -12.80129 | -48.73706 | 2025-06-26 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0865d07b-53ad-3bc6-b943-e7599ef00076 | -6.95176 | -42.80506 | 2025-06-26 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0019618d-2e51-321a-b2db-78abf4548378 | -13.03393 | -48.83383 | 2025-06-26 03:49:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85e09727-4f5c-3503-a393-d9920a993e30 | -11.57575 | -46.90031 | 2025-06-26 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daf76aa1-5955-3f84-bbd1-c73bccd90ddf | -17.88567 | -43.98698 | 2025-06-26 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd4001bb-03ed-377b-b4bf-160ab73de015 | -17.88348 | -43.98931 | 2025-06-26 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea60f40d-4934-3462-b6c7-ffad894d597a | -11.82365 | -51.26217 | 2025-06-26 03:49:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f4742f4-f118-3b12-843b-408b2362fbaf | -6.17759 | -48.08417 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 65120a9b-0ffe-3d06-ae0e-1724714ca5ed | -6.17762 | -48.08481 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4319248c-943b-3f2c-ae83-2d07a4cd38d9 | -17.19652 | -44.32906 | 2025-06-26 03:49:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b53d6eab-68ab-3958-8b7f-a6f0a9fca2cd | -19.71879 | -40.35048 | 2025-06-26 03:49:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e27e33f-7b03-3c08-8fd1-4e3eb1a1049b | -8.86937 | -37.79191 | 2025-06-26 03:49:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89d3560f-868a-3317-9b6d-28328694e6fa | -6.1794 | -48.07431 | 2025-06-26 03:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 171b25ca-3900-3c45-bc56-c1f06e2063e3 | -9.121 | -49.4528 | 2025-06-26 03:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 211614e3-a2f5-3354-b92c-0875bec63763 | -9.1213 | -49.4313 | 2025-06-26 03:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 394f24d5-42ee-36c6-9a4f-2820e5f5be4c | -6.1791 | -48.0712 | 2025-06-26 03:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| bcdcc30c-876d-3a7b-9aba-2ebbffe1a604 | -11.0644 | -55.3757 | 2025-06-26 03:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 21597498-98dd-36bc-8899-d81432e5b7c4 | -22.53995 | -48.81172 | 2025-06-26 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01467478-2769-32d7-8104-e323a0c3a882 | -22.69696 | -43.34783 | 2025-06-26 03:51:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b2e8759-4ca4-3d84-a5ba-95c7a81e9ded | -22.79553 | -45.1576 | 2025-06-26 03:51:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4a75793c-ce6e-336a-b3f9-f5518e297912 | -22.92189 | -42.32834 | 2025-06-26 03:51:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ff6b703d-9fb0-3caa-aaf0-307d857bc11a | -21.19056 | -48.68824 | 2025-06-26 03:51:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 15841799-accd-3938-9a8b-59337fcf3b7e | -20.25221 | -46.7296 | 2025-06-26 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README8.md)
