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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c193201f-4886-3aeb-8ffe-c500d371cac6 | -7.91288 | -44.25581 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3bd8db8b-2c6c-3531-b0aa-f7c4140bb5ce | -6.86655 | -41.70913 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c4365568-88eb-3b59-a6d1-035901ed1103 | -3.39494 | -42.79107 | 2026-08-31 16:33:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 669b9240-d11d-3329-b9c4-5efa7cc4ddf0 | -7.22812 | -42.76759 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 472e688a-e055-3404-ba39-1f5f373034e2 | -8.14011 | -45.58386 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| fdd61ebf-0232-36c5-90d4-b2a3beb1f2da | -5.87086 | -52.09645 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de3cc27f-20f9-3f60-966f-76db7008cbdf | -4.29945 | -49.09455 | 2026-08-31 16:33:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| be37f2eb-0bd7-3238-ae39-316903e1d3e0 | -7.98701 | -44.29033 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3b11a940-4732-3eff-a664-f3f6b9b1b535 | -7.62246 | -44.93742 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b1cce144-bc31-3220-834b-df21abd8a2ae | -1.42091 | -48.95301 | 2026-08-31 16:33:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cbce000-33d2-32b5-8373-d0bf31d19302 | -7.29804 | -46.17599 | 2026-08-31 16:33:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c5f8df8-0fb0-3590-bd73-b579a64b152b | -8.65367 | -49.53999 | 2026-08-31 16:33:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bddf7f0b-d665-31f0-bfd8-03ecda4fdf3c | -4.33707 | -48.71453 | 2026-08-31 16:33:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2631c8f8-42f8-34ec-a310-fadb8f542d94 | -7.41643 | -44.24627 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a36e820-354d-3d3e-946a-c8b07e36718d | -2.70555 | -56.54865 | 2026-08-31 16:33:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bb81657a-4f9e-350c-a727-ab6b8cd6a59a | -7.41977 | -44.26878 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73e8baf2-ce29-30de-9882-db21b6693a6e | -6.8699 | -41.70861 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5426f7a4-63fc-3e21-b524-e9f5bf37639f | -7.35858 | -55.19 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 39438ff4-1390-31db-a03e-04c94fb5f232 | -5.88013 | -52.16305 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 24443516-c8d8-3c30-9942-7a95ea323557 | -8.4435 | -46.90468 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 313085f1-0f49-32cc-85a7-cd6c6b0335d1 | -6.91399 | -55.70522 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2bf6c2b5-d2bb-3583-b2f6-fa67feff304f | -7.17117 | -44.68292 | 2026-08-31 16:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bafb7f5-5c6e-3ebd-98df-6a2d35dd49ef | -1.74513 | -48.24188 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d30250ef-319c-3ed6-8746-fa7e9044feca | -7.35761 | -55.90231 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c525049d-2920-3cc7-b1f7-6663c558f3b8 | -5.5844 | -42.34446 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0dedb5bf-7f02-321f-90d3-1fa2794c2606 | -3.72752 | -44.37335 | 2026-08-31 16:33:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87b093de-95f3-307e-958d-18ae0563ef5f | -7.95101 | -44.2613 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 61bc82c1-c0e9-3425-b86f-c21759a39d91 | -8.45284 | -47.5612 | 2026-08-31 16:33:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f2f2b781-da9f-3a79-b856-75401628f2f0 | -4.90769 | -43.46154 | 2026-08-31 16:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3bc2ac5c-b1b6-31ca-a477-8ac7551f5b41 | -8.44748 | -46.90425 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| b0272172-edb3-3159-854c-0ff24f6de5a0 | -7.11017 | -42.21922 | 2026-08-31 16:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b292880c-e49a-302b-b558-e89ae2e01519 | -7.60311 | -44.92816 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 71171f0c-3dbc-3c69-97fc-dee4c8d68f51 | -1.12245 | -46.3294 | 2026-08-31 16:33:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6edaa029-afae-36c4-ae7d-1ebbca2689ae | -4.36402 | -44.43934 | 2026-08-31 16:33:00 | NPP-375 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5e474c2-0196-32cf-baae-ea12edc05627 | -1.64339 | -50.10518 | 2026-08-31 16:33:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43b95329-1653-33a7-9b24-7c58ddd5bdc5 | -6.25695 | -42.87143 | 2026-08-31 16:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f6ad0f36-1bfb-37cd-af0d-472d639ea80d | -6.67397 | -52.87025 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97eed3db-e7f5-3f59-b818-aa549fd0fa81 | -6.75961 | -56.33931 | 2026-08-31 16:33:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 96f54248-e53e-3b22-91b6-a0dc96d3d26a | -5.9127 | -52.39765 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d87e73a2-f394-3956-8389-1923e1e8f646 | -6.68582 | -38.49343 | 2026-08-31 16:33:00 | NPP-375 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 55fa241f-4cda-3d02-bbd4-b467824bf17e | -5.76047 | -44.12519 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 68495cff-3825-3f64-89a9-79f6126c2c73 | -3.56163 | -56.84334 | 2026-08-31 16:33:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9bb2c483-f618-3272-9981-0c2d2de9086a | -5.82878 | -52.39457 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7bfa2e1-1fbd-37ee-b326-ed6fa737bd86 | -7.08536 | -42.83232 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b446bbd5-f432-3ab3-a1e1-bdd319746228 | -7.98251 | -46.51975 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dee06f5a-5581-301d-9ea5-fa766af61df2 | -1.57779 | -50.5028 | 2026-08-31 16:33:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cdc1eec2-4d4c-35a5-9652-bf4152a29fb6 | -4.90383 | -43.45857 | 2026-08-31 16:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e63a2edf-ec8c-328e-9856-c70bf1c964ac | -6.25999 | -53.65111 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 86b462ee-217d-38ee-87f6-b99befca1efe | -6.29384 | -53.58315 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| aaf9516e-a995-37aa-a458-26be46023b0e | -1.41682 | -48.95363 | 2026-08-31 16:33:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd1bcdf0-55c3-3634-8c4a-a5e5f6f278d1 | -4.09764 | -43.33355 | 2026-08-31 16:33:00 | NPP-375 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a74f824-0b72-3220-91c4-cc07c826b383 | -3.55425 | -42.67718 | 2026-08-31 16:33:00 | NPP-375 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9f4c55f-45f4-38a5-a987-afc3c0fe48a9 | -3.61423 | -44.39505 | 2026-08-31 16:33:00 | NPP-375 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c6ec2df2-2b76-37af-8431-ad51b3264e43 | -6.86601 | -41.7056 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 07e7b562-c1ed-3bba-8afe-85933424dcc1 | -7.64258 | -46.73357 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8ab5eced-68c2-36c1-b4a7-20bb3097b192 | -0.98277 | -48.16598 | 2026-08-31 16:33:00 | NPP-375 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 80ab2de3-769c-31c3-aef1-8f94ebae472d | -4.30316 | -49.0899 | 2026-08-31 16:33:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| cedcc224-81be-33f4-9777-17377105a723 | -6.30059 | -44.61488 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9739aec0-3ecd-3a2e-8ec7-ad1d243a04d9 | -1.72655 | -47.40209 | 2026-08-31 16:33:00 | NPP-375 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7e261604-e9cc-3164-a4f8-16f47644fe25 | -7.77459 | -44.05574 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cdbe4910-c505-30d0-a5f5-fa2923bc3169 | -3.05771 | -45.17646 | 2026-08-31 16:33:00 | NPP-375 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9168ca6b-d9ad-316d-a9d1-28ea5b3e3a0f | -3.80903 | -38.61705 | 2026-08-31 16:33:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 555ea268-f2ec-30ba-9ad8-0ced4b6e55b5 | -2.74045 | -49.29281 | 2026-08-31 16:33:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb9c126d-fd2a-333e-9318-ea7c2f0ecfa0 | -7.01809 | -56.54332 | 2026-08-31 16:33:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d0e1a6c-f830-38d7-903f-5dc770a2cf46 | -6.68056 | -52.87136 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40ac11ed-d928-35b8-8346-1de91c3b8e4c | -7.63322 | -44.8396 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bf15a04d-ccd6-3eb0-8005-62e259bd1301 | -4.14434 | -38.58257 | 2026-08-31 16:33:00 | NPP-375 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 5770f362-33f6-3819-9474-b570d1ed3ae7 | -7.09298 | -43.88056 | 2026-08-31 16:33:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5b86df8-d0b7-3ade-b4ae-d12ee2fed251 | -7.91176 | -44.24836 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9013522a-681a-3d99-9b4b-e6029b457907 | -7.98989 | -44.28605 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7943d335-d120-3ce7-985d-d9f9f91fd413 | -7.22759 | -42.76411 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dc56acad-1833-3bfc-b7a5-36a5e76b8769 | -3.41715 | -43.37327 | 2026-08-31 16:33:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e02971a3-75d9-3660-8f12-b6fbc1b045bb | -6.05995 | -53.83136 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c3a45278-7df7-3d03-906b-f94c611b00bf | -3.54974 | -51.11404 | 2026-08-31 16:33:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8b2c0659-5ec2-341a-b190-1d01c350d1f4 | -4.5171 | -40.84669 | 2026-08-31 16:33:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 86f9a8a3-6b47-3acd-8129-7fc97b36b2c6 | -7.98534 | -44.27911 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 867dc9ae-d95d-3578-9e71-8b6703cfe77b | -5.89974 | -46.12369 | 2026-08-31 16:33:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dadf7956-c52b-3149-a508-3936bd05fbee | -7.99603 | -44.3273 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 18f89dc2-bbde-3986-98d9-c42e29a243d4 | -6.99755 | -55.9001 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fb8f8e9f-f823-3ae5-8838-5862d384a98c | -6.86936 | -41.70508 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8420e21e-30b7-345d-9b47-545dadef26e3 | -5.07347 | -42.88488 | 2026-08-31 16:33:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c36cff3-7cd0-3c22-9c21-a23dbd931c11 | -8.31478 | -47.64178 | 2026-08-31 16:33:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 284f177e-7794-388a-aa4c-7cdbe86d736a | -7.10524 | -42.76154 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| cb1a4868-3def-32ad-8db9-1fadaf5b99b1 | -8.08894 | -45.45998 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9b070fcb-8277-3f11-8e32-19f4992061d8 | -4.21412 | -48.60879 | 2026-08-31 16:33:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1b441d74-0ea4-3eeb-80a8-2f8c455addd5 | -6.83805 | -41.7244 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 3e3a27d0-ad5a-3a52-b3fd-4aaaa5a4e825 | -7.04663 | -45.39995 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86a91f9d-c50d-3965-9084-8ef475ce356d | -6.8442 | -41.71983 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 3982b70f-72bd-38ae-bff0-3822cadd0ab9 | -5.25837 | -55.89061 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 13dc7526-7e43-32fe-bb1f-5c3b88b194f3 | -8.2125 | -54.94667 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3ee24862-1419-3f90-94e7-ae1d13a0a867 | -7.09195 | -45.78707 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d31eec4c-4b5d-3517-adcf-afa00c5c28e9 | -7.98757 | -44.29409 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7db3a312-f6e5-377b-86ae-9ddd527b9e66 | -8.00023 | -44.28449 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 8c6115a4-92b5-3a11-869b-3280757ad89a | -7.36861 | -45.0666 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c84deb88-90c2-32f2-93b5-14caaf8879af | -5.58386 | -42.34098 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 039d267a-61a8-36cf-aafc-b1a78fb06f7a | -2.48285 | -49.06118 | 2026-08-31 16:33:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e006fad6-17f9-380e-bfae-2b8a7aae2d79 | -2.2627 | -47.86779 | 2026-08-31 16:33:00 | NPP-375 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 75adf01d-a1f3-3e13-a0c7-f1ead08e6082 | -7.42639 | -45.27122 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb8c5e0e-4a52-3246-9026-f56efe61b89d | -5.36411 | -45.92487 | 2026-08-31 16:33:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6c5a7b55-11cc-3054-af3d-b99cbc4e7c5d | -7.98913 | -44.32833 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |


[Clique aqui para ver as próximas entradas](README129.md)
