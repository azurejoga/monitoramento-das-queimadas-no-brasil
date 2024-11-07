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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25c7f244-7ea4-3e86-b03e-3344cd31007e | -6.04714 | -46.60423 | 2024-11-07 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c41699e1-de8a-39e0-86c3-fea3a4c0f377 | -3.66449 | -52.34159 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baf17f35-7d8a-30af-819c-329d8d015df0 | -3.23601 | -50.45002 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d077286-33d5-3108-b17b-eb6da4417ea4 | -3.05522 | -48.03025 | 2024-11-07 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1a2218c-3ce1-3ee5-b88d-c5cd8fcaed04 | -2.86812 | -50.33017 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f796169f-77b6-3752-b164-337f3af5bd27 | -1.33324 | -54.60559 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7974437e-6480-32ae-af1b-94a52114ec4e | -2.61417 | -51.73103 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70b4e22a-9f3f-3c90-8bc2-55ad74990889 | -5.29594 | -46.23644 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09e1cbd2-4204-3b22-8274-1b4ad14f4190 | -2.90791 | -49.39983 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d14847e-52f6-36d1-8181-5df217510fb3 | -2.91086 | -49.40805 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba40260-2c65-3b2c-a3d3-5f67f86c7840 | -1.52415 | -52.14938 | 2024-11-07 04:18:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 261ba9eb-67e0-3471-9c6e-f45dd1c4f67a | -4.68235 | -46.38783 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 879b02f3-4091-3479-973c-752047d26053 | -4.50336 | -42.86829 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9948bda2-c21c-3cf6-8643-e92c985188b5 | -2.8616 | -49.39632 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f73f8dc7-972f-3ef8-87fd-7ac063ed29dc | -3.74006 | -50.07053 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 099cee4a-9661-30ea-b9ba-a590cc893c07 | -3.13624 | -51.20547 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c47f109f-885f-3e7e-a643-52eb5387b1c2 | -5.93756 | -43.77248 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c786bc9-be14-39aa-8345-9c6253533e9a | -2.99168 | -53.84929 | 2024-11-07 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c15112cb-e23c-39d2-bda0-e373eec8dbbe | -3.21352 | -49.2324 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| feb34506-0919-3b04-a063-b14787422344 | -4.0528 | -47.37854 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b36a39c-c4ad-327b-a68c-8ad26211bd6e | -4.38502 | -50.84136 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc088139-db92-3ea8-a880-d462bdb2cc52 | -1.39351 | -54.11063 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c41aeffd-2f4b-31e5-a333-a667b4b5c0e4 | -2.07507 | -52.04551 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cba40ad8-87c9-34b7-964b-b34a3683383d | -4.93288 | -43.63801 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 99b1bbf1-0691-3302-aee3-a03cad486e7f | -4.99583 | -49.89009 | 2024-11-07 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a6c46dc-966c-308d-b488-136b38461517 | -2.14098 | -50.79614 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642e4250-a3a0-3ea6-9dcd-033409ffb9c2 | -4.41298 | -47.25854 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e9f26f2-b3db-38fd-9aef-cbc7d9226f81 | -3.52797 | -50.3473 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07a6a8d-03da-3507-905f-d778d9ded4ec | -2.17516 | -48.32368 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d9ac72-29eb-37e9-a85e-60f445ecf697 | -1.2318 | -54.54292 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ed292c6-939d-3ced-aec8-bc81b0937536 | -5.97452 | -45.3536 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dea780de-8deb-3f29-bfc2-9486352ff159 | -8.50004 | -42.11204 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50a60049-6ae6-3440-8dcb-7d63c95ceee0 | -5.40048 | -46.91174 | 2024-11-07 04:18:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6b34466-1c53-3510-b1cf-68762b824125 | -2.61329 | -51.7365 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 037189e3-48ad-32aa-9559-6dbf507750f1 | -2.80467 | -51.49504 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd0447d8-7fb6-3d1a-91a2-a8a535b15f1f | -2.73699 | -51.89699 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1588c81b-152d-3887-834b-586fb171ec4f | -2.83795 | -52.90186 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1ffabda-06d9-316a-854e-2d8a9526faca | -2.95035 | -49.5708 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8f22613-0975-375b-88de-488eb4f1bdcc | -5.24249 | -46.26217 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c8fa882-e47f-3437-b789-76eb9f52d406 | -5.36899 | -46.25949 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6af7f203-71ef-3c42-a06b-da801d2906f5 | -5.19286 | -46.20168 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0fcf4ff-6011-38b9-8ad2-80bd23393278 | -4.76836 | -45.7376 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb64262-4b63-36d0-ae0a-cdad0d7c02e4 | -4.93119 | -43.62706 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 999c9894-288b-30e2-9a46-899b9ceb4a2d | -5.80812 | -46.1453 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1ab5514-2066-3cf1-8cec-b3bbffafe607 | -8.11891 | -44.4209 | 2024-11-07 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c659d10-203e-301b-9d0d-50eefd778072 | -5.33415 | -46.19383 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e929d81b-a74d-3b22-b24e-1af3dba31539 | -3.29102 | -53.11788 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42b04065-751d-3fcf-aa8e-06b2d9783c37 | -2.59266 | -49.33973 | 2024-11-07 04:18:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73b5df1d-4385-337c-9eb6-5188d4663f44 | -6.49849 | -44.68064 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0017e2c-4a5b-3e43-808e-fb74d57abfde | -3.14913 | -50.20894 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ebe41bc-9a18-3360-af62-83c534085a29 | -2.81702 | -52.96254 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a90f6056-9de2-3dba-a33a-c35edba95ec2 | -2.04753 | -52.08628 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d452b92-2cc0-3530-a5a6-278d7ef5686e | -6.69516 | -46.99888 | 2024-11-07 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc5852e2-0524-3a20-99da-4d49ade70066 | -3.62277 | -49.61814 | 2024-11-07 04:18:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e428b047-ab27-3f74-973b-1a4d94a6ae6d | -5.96898 | -45.36702 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03c3cbcf-d150-3b59-bf06-c0ecdd651953 | -2.88531 | -48.73179 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64c67035-f94a-3fdc-a101-27419c0bfa67 | -4.50847 | -42.8689 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3af57bf2-b4c6-3239-8511-e38e054bb4f0 | -3.00516 | -53.4335 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a797e70-69f2-3afb-8a2f-3c72cfa9f746 | -3.61966 | -50.19859 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c4335ed-6044-319f-836c-121db64bea53 | -5.01655 | -46.47034 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 539191ff-2330-3394-8d11-0c3475c9bc90 | -5.37637 | -46.25692 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a171014e-ef69-3fa1-8d73-4b620bc3dbda | -5.98337 | -45.36212 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| a823d269-193f-3007-a7f8-d43c5b042911 | -2.88449 | -48.73691 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 476ad621-ec90-354f-9efe-801647dadaf5 | -5.98005 | -45.3616 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7e39d27d-a306-30c6-ac31-6d26b5cb476c | -4.24113 | -48.54313 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce3c76af-55f8-3964-af5e-f3c1e2d31151 | -3.16154 | -50.21532 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a5c530b8-3bea-3171-9a44-c91d05ce5f41 | -1.219 | -54.54542 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f525e4a6-e17a-3233-825a-2b2c19d93fd5 | -7.42407 | -42.88102 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c977a9d9-425a-3ca6-b006-b460afd7ea57 | -3.14982 | -50.20472 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b18d345-fe92-3f21-8c09-bacf90e85b45 | -3.74502 | -50.06711 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fee9adb-0e72-3c14-a96f-ec4ce4af9778 | -3.04137 | -53.27474 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a761b05-2658-379a-b071-0d306d4af80e | -4.51128 | -42.873 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f32ab93b-adb7-3c03-9305-21bc0c009bf4 | -4.93579 | -46.77717 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42a7ba5-7f79-396b-bfdb-f703f844aac2 | -5.84205 | -46.26619 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 196f48dc-9ebf-32b8-827b-1c5526ba51c2 | -3.2246 | -50.38115 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17d6e4ce-f00c-3093-b44a-60f869096c28 | -6.10762 | -43.96709 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7b0d5b6-8e66-3826-9280-79be3738d3d0 | -4.34425 | -43.70945 | 2024-11-07 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a389363-2968-36e6-9144-8c2ed32e19d4 | -7.03864 | -47.62416 | 2024-11-07 04:18:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f8940a5-7add-39fc-9d0b-5f953eb50449 | -2.61497 | -51.30021 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2d8c3e51-6d4e-333e-b6fb-0328a184a03e | -4.74217 | -44.42112 | 2024-11-07 04:18:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d44e64c4-17b8-30c2-9366-c0c66f9a5b49 | -2.31852 | -47.91054 | 2024-11-07 04:18:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe35363c-561b-3e83-aa86-943fe2aef127 | -2.81885 | -52.91874 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4d537a3-f132-3b80-b218-af6847941865 | -2.95503 | -53.72628 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec1d565f-9fd4-3133-bd94-4d15df057c1e | -6.12198 | -44.91496 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c044ba0-76c7-3e2a-8761-33fd4e110994 | -1.28179 | -54.1394 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 300131eb-34da-3513-9193-f3c06cf2a0a6 | -4.71131 | -43.79569 | 2024-11-07 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d60a5072-7564-3061-b779-33f77595c5e0 | -3.20535 | -49.23108 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ccd97a1-f7dc-3093-9b46-d6dce73f24d5 | -1.22316 | -54.54718 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c328ed1c-fe37-39b5-910a-0ebf088dca09 | -2.81611 | -52.93523 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 806e755e-c2ee-3e44-b067-bb84efef8a95 | -2.80947 | -51.49583 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a180228-ec58-38e3-bb5f-a17741cde571 | -2.9563 | -53.71881 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bd8d818c-339b-3dc0-bb2c-2275f9aeb7b9 | -5.01253 | -46.47351 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56156117-361e-3bd1-8808-0811fe005743 | -5.30274 | -46.23754 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 108bff6c-734b-3efd-b836-14898ba7817c | -5.61766 | -43.9512 | 2024-11-07 04:18:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 87fa365b-0f23-30d8-9be0-a37b4ca72768 | -6.13271 | -47.02548 | 2024-11-07 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e6fef21-9db7-389b-b433-27aec3c52058 | -7.44157 | -42.90282 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dacbbeb3-7284-33e2-8bdd-0430d94572af | -3.45306 | -52.01296 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 906cfd78-5089-36b9-94bd-f67dc8a5d293 | -3.13705 | -51.2005 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43141761-f8e7-39c4-b5e7-e0ac261b60d5 | -2.92804 | -52.54832 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b687f20-3642-35f6-a6cb-6844096b4473 | -3.03 | -53.27645 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README27.md)
