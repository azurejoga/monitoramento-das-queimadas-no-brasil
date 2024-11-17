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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6817b8f0-3159-3c54-b73d-829582dfacb9 | -6.69533 | -44.70407 | 2024-11-17 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec0fde8f-dd3e-3ab4-a322-7dc6502f55f8 | -2.6735 | -46.18479 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85264371-6b4f-3b62-8f8a-a03d6894d172 | -2.66735 | -46.1949 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 572a511f-8910-35c4-8d9f-ae5cb26b5c0e | -4.40145 | -45.52557 | 2024-11-17 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cb96ed8-f3ea-3d89-87f7-bc9cc51997b7 | -4.24093 | -41.92793 | 2024-11-17 04:06:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0e56806-0007-3fc0-9957-56c3389f7d95 | -3.91352 | -46.52436 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e477097d-0dad-3882-9ac8-2fe053400f88 | -4.12006 | -46.76031 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c31050fb-dc73-39e7-9b40-fb00572771ab | -2.41857 | -48.78804 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b21386-fd83-3b49-b2e1-b77d65c17e93 | -4.74055 | -48.11744 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba0fe79-4538-3e9b-9cad-6a072eace2c7 | -4.32299 | -49.38773 | 2024-11-17 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abae999d-a172-3b70-a665-1e74669fb37b | -3.92139 | -46.52597 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9ffae349-e847-3243-a00a-ea76547939f4 | -1.13442 | -51.68645 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1efce8-e103-34f6-bedf-19bb5dab3164 | -3.1439 | -45.97877 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b1f5fbe-3bcb-3fc2-bc08-237d68dd1f7f | -2.66074 | -46.21067 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a89e5af2-c779-3cc1-acbc-50871b734d71 | -2.6745 | -46.20408 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cfdf6a0-5ce2-34bf-9616-e58a451ede69 | -4.47585 | -48.10987 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a192986-fd82-36f0-8f19-e9e23695367a | -3.81079 | -46.52111 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47808ba-fe6a-32ad-b285-58565141ba5d | -2.62888 | -48.56603 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b59cf339-18ab-3eee-9a69-f38137d72ed7 | -2.60896 | -46.18218 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ad29c7c-b401-3845-aa2a-30d6d9a78b93 | -6.17594 | -41.16641 | 2024-11-17 04:06:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c9d2081-ef84-335d-b76b-f787d8c8aaf8 | -2.2989 | -49.12867 | 2024-11-17 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98978341-5696-3d0f-b30d-ed597c1c5f99 | -5.40202 | -42.77093 | 2024-11-17 04:06:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 56a4c739-fde5-32d7-9691-8deec8c68121 | -5.46153 | -42.15236 | 2024-11-17 04:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0291c634-18f8-3632-aaac-73ff8edfe0b3 | -2.60181 | -51.79765 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2cc5d36f-b41a-34ff-8245-d82ff11ee21b | -2.86667 | -46.72491 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 389d23eb-d2b6-3af1-a2cb-95f75cdc2a14 | -1.29566 | -51.74184 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0dd5ba0-4997-3e3f-8ed8-fc466cb4638e | -4.03617 | -47.2088 | 2024-11-17 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dfc8d5a-9a96-362d-a12e-5aab430db362 | -2.66899 | -46.21114 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4495d9fa-3177-3409-a475-cb8fbbee093b | -2.09354 | -48.2702 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4d23ee8f-c3a8-30fa-93e6-10e430a9e168 | -2.15825 | -50.70372 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93cf118f-f6c6-3e43-b9a1-8ec03d170c0b | -5.49632 | -39.53205 | 2024-11-17 04:06:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbbb7f30-157d-3578-afce-a80a68f82327 | -4.2841 | -48.20837 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 900b1699-227f-36c7-9916-ac60364b1848 | -3.3326 | -50.49907 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7acd839f-6504-3549-915e-af2c03cce931 | -4.82184 | -47.32313 | 2024-11-17 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93f7964a-bd24-34cd-84e0-a7d1441bd18e | -4.18936 | -48.56846 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7afefe6b-2041-3c57-b137-220cb9d47d46 | -5.33747 | -40.90335 | 2024-11-17 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe15a38c-998c-300b-bb1a-b0b0ae5c466f | -5.64431 | -43.30251 | 2024-11-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b8bb718-ef16-3339-8ea0-c648d8a8bb8d | -4.45431 | -44.55 | 2024-11-17 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20296cf4-e116-35ad-89e7-808e8edc8355 | -3.66133 | -50.6092 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 794a40be-56e2-3c4a-bd30-991809945628 | -3.00948 | -45.39788 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bae7753d-6692-3e89-98c3-47cc9befcd66 | -3.53531 | -50.26162 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f382a9e8-f06b-3d20-9592-a203948f670c | -3.50036 | -43.78786 | 2024-11-17 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4bfdd212-05a3-3019-98ab-fd2237f5b519 | -3.7812 | -46.04641 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fba95f22-24c9-337f-8ae2-936006c07b86 | -6.17316 | -41.16243 | 2024-11-17 04:06:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eca8163d-5c44-3ce4-b812-53df0a7e878b | -3.56637 | -50.24495 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d810f068-029d-3c0c-804a-19fd1d5699b9 | -4.37699 | -48.08688 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1dca0b9d-f281-3b81-a3cf-13405a6a613c | -5.40319 | -42.76366 | 2024-11-17 04:06:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| da02a5e3-b41e-3bea-a205-f797a012f3dd | -4.18524 | -46.81997 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dccce320-35c7-35bb-888d-1fde7f0f3e8a | -3.52917 | -50.26444 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aed98ec4-82bd-3839-aeea-6b9388c9bfa6 | -4.30057 | -42.18818 | 2024-11-17 04:06:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 496059c5-9c50-3eb7-97b0-7c28aebcf3c7 | -3.6635 | -50.61059 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d902ab6d-0184-3d72-85e8-cd531ba6dfec | -4.21941 | -47.21819 | 2024-11-17 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a829a48-93e7-320c-afac-58bd3f89a480 | -3.50104 | -43.78374 | 2024-11-17 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b054fd00-eaef-3da5-9ce5-b49357858bb0 | -2.22515 | -53.60623 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 794ae50f-79ff-37de-9306-24048e2ea031 | -4.35547 | -45.86697 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87a35de6-f931-39e8-98ce-3f745740468b | -6.16876 | -41.16883 | 2024-11-17 04:06:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c24dc9ba-284e-333d-a69d-1e33c90517db | -4.35489 | -45.87045 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 042ca197-f831-3b00-90ed-5b00dde82b6e | -4.36555 | -43.0089 | 2024-11-17 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a17bb6f-6fc8-3820-a888-eb67beb69c86 | -3.57977 | -50.52631 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33315c53-2f1f-3583-9402-43dd5f81a147 | -4.4506 | -44.5494 | 2024-11-17 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02339cbb-1b1a-3c8a-bf1f-f2d556902841 | -6.48122 | -47.5118 | 2024-11-17 04:06:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 863fc9d0-5927-3c15-b993-b44619524503 | -2.66496 | -46.21138 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fa134ba-db3d-3812-add3-106ae7d0c336 | -2.23146 | -48.36995 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36c176cf-2797-37ee-915d-e3cec16e629d | -3.53283 | -50.51234 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c16ca46-ec19-3fc1-afba-018a3d0e7cdb | -2.46165 | -45.60498 | 2024-11-17 04:06:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bc618c8-9c1a-3efb-9794-5aa1815f8011 | -2.66919 | -46.21208 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cb9d44e9-e221-3ee8-98e6-05c64e5b55a8 | -1.14066 | -51.68755 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0905ea2e-46e7-3c91-abd1-65889f28040d | -3.76842 | -43.24644 | 2024-11-17 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c92b0885-78f2-3bdf-a1cc-469853684c39 | -2.18704 | -48.26439 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13298e4d-56a2-3dee-a6e9-d0e547043a35 | -3.68863 | -50.12038 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87345c2b-2b6e-3025-ac9e-a790c6edbaf5 | -3.95097 | -46.71744 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf22286e-ccce-3272-95ef-d44afad81cf2 | -2.62391 | -48.56522 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 99bbce3f-8408-396f-a9da-bff65c3f6f15 | -6.82259 | -46.77649 | 2024-11-17 04:06:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6f9c152-e76f-3809-96c0-f19ab0091859 | -2.35203 | -47.46699 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e0949491-6b1d-3e14-9374-c89815e6958c | -3.41904 | -41.02704 | 2024-11-17 04:06:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42806fef-5725-3128-9a40-72def1606671 | -3.13294 | -45.90092 | 2024-11-17 04:06:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3440fbed-d13b-3daa-b52f-a134f3372be7 | -5.45818 | -42.15183 | 2024-11-17 04:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3cb57736-feaa-3f1d-810a-d4a93468bb04 | -2.67587 | -46.19722 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce808e82-faab-326b-8784-20991a0bbba6 | -2.60638 | -47.54736 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7325c4f5-44d5-3b67-b5c7-0faa1105d96e | -4.54799 | -46.41639 | 2024-11-17 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eec63cd-5be7-3a22-8195-248f3ba51626 | -3.97928 | -46.70557 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0065cec-7a9d-3881-992a-b265d5fa7e8b | -6.17539 | -41.16987 | 2024-11-17 04:06:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01ab1c12-4408-382a-bc65-7b780fcdaac8 | -3.48605 | -40.64517 | 2024-11-17 04:06:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00fbb138-1340-3a1c-b5d5-bd2e0bdb348d | -3.51874 | -50.25929 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fc4035ed-59eb-36f7-876b-99f1bb1327de | -2.6743 | -46.86224 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe7b7dbb-1a87-300c-befc-9c94348aa673 | -4.47857 | -44.01351 | 2024-11-17 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14d0f35f-aca1-3410-a743-89a48137352c | -2.59939 | -47.56097 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58ce7507-2848-38fb-91c6-61b914a98bf7 | -3.78589 | -43.91108 | 2024-11-17 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 973a1b87-9188-3106-9c42-526a4573b25b | -4.40473 | -45.52269 | 2024-11-17 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f8f3920-2a84-30c4-adbe-52c6fd4c60c3 | -2.67057 | -46.17552 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16fd0a1f-af12-39e3-9c4b-eef27a07a0a6 | -7.47992 | -47.18014 | 2024-11-17 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ead85a3-b79c-361f-a917-e5eb0760c51c | -1.13634 | -51.69007 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8650bd1f-11b4-3d33-ac6c-7a967a64de09 | -3.04484 | -47.97862 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e03cd135-c474-3d88-9559-c55438e21079 | -3.71681 | -51.84111 | 2024-11-17 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbce5e0e-79ed-3783-8a0b-9177d3e90b43 | -4.40225 | -45.52057 | 2024-11-17 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8d4dc24-382e-3894-8e0b-bc773552863a | -4.45802 | -44.55059 | 2024-11-17 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e66a753-eb02-3d85-9e16-dc9fe8e3786c | -1.14258 | -51.6912 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 88ef6e96-9f76-3c95-9bb8-b321ebef9703 | -3.89535 | -45.91283 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f4758c1-4f7a-38f2-bd55-7ac00b59e6cd | -3.57912 | -50.53015 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2171402a-fad5-35bd-a106-4112a1ea3a01 | -3.90513 | -47.08077 | 2024-11-17 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README31.md)
