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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06bcb1b7-7a2d-3b09-88b4-7e4f3783b1b0 | -7.71347 | -42.94592 | 2025-11-17 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a83b7a12-5b7a-3b58-ad38-3b879a3f8b9d | -3.59382 | -50.71362 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e22601fc-46ed-36d9-9cec-44928f1406cf | -7.97105 | -50.00359 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9e00a73e-e31c-3f82-828d-25cb27064348 | -3.89002 | -52.82092 | 2025-11-17 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a025095b-f608-391c-94d5-573949dc5eb0 | -5.8379 | -48.83259 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae00f152-7a4e-3508-b3cc-593bf0b63024 | -3.4831 | -49.5928 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d059140-1596-3000-8b33-ee1f7915bb0b | -3.83957 | -51.28433 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c5172ac-2d83-3605-8253-a382038305f3 | -3.15542 | -46.56254 | 2025-11-17 04:38:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 613cdf3c-a9f4-31c1-b078-1ffab79eb6c0 | -5.00183 | -44.35533 | 2025-11-17 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ac06d641-01b0-34fc-92d5-cf118e2a25ba | -3.11063 | -49.4734 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b79fc099-6788-3907-b147-bea45a522909 | -8.24852 | -41.42211 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f413f4da-2462-393c-8f97-974bd159909b | -2.6663 | -51.88192 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d826eb6d-f335-3387-b354-d062859bc84a | -3.48073 | -50.2532 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 456d51e4-1d94-3712-8962-c8b7357d4f7a | -3.83446 | -55.80819 | 2025-11-17 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d0a297f0-8430-3b03-b47a-b08a7462812a | -7.08726 | -42.73358 | 2025-11-17 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 95cdf2e1-1649-3eee-a979-e7fadf094e1b | -7.87664 | -42.87883 | 2025-11-17 04:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f613306-4e11-371d-9a53-7eabb0ee4775 | -4.81936 | -45.66683 | 2025-11-17 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45015f34-14dc-3586-98f1-d066788f46a1 | -8.09853 | -46.05107 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79069e75-637b-3ab4-a6e8-684be45e5a86 | -4.96667 | -44.16154 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7b45dac-21ae-3d26-b088-d828dcef5c80 | -4.65738 | -46.73971 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| e3619bde-a168-3ad2-9335-28194bab70b9 | -3.01328 | -51.34539 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81522a9b-5756-3077-9365-9c7a87b067b7 | -5.95627 | -50.00581 | 2025-11-17 04:38:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a14e703f-23ac-3133-b35c-dba6f6c70580 | -5.83736 | -48.83604 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe4e1395-fe28-3519-9f83-957c28833332 | -3.34876 | -51.37895 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45a969c7-a078-3a1d-b0f1-64f32e3e4285 | -4.73973 | -46.38621 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e7e228c-43b1-31fd-82e1-c90cfdd15955 | -2.71912 | -49.34423 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4887c59-31f1-36bb-bf12-69793f957c1c | -3.60545 | -55.53875 | 2025-11-17 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce2568e8-24ff-39af-9937-01f679bfe173 | -3.81619 | -51.17398 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 845f6ef9-e046-3b39-80f8-ad568b263939 | -7.61999 | -42.57478 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 95c3425d-ed70-339b-85a8-f8e8ca773fb4 | -6.85895 | -42.85758 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 560085d7-137b-39cc-bb4a-e07259c05900 | -2.68709 | -49.33204 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62e20006-1c93-31cb-8aad-a77b1bd45828 | -7.6246 | -42.57547 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 848b837e-fad1-3ba4-83c8-1d3f1adadbbe | -4.4603 | -49.78283 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bfdf225-9423-320d-99ff-22a9525245a2 | -3.88318 | -46.46318 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a4694bf-01d8-36b1-9290-7b282e0901a2 | -7.10214 | -42.72625 | 2025-11-17 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a71b69d2-8fff-329b-a05e-0d9d0bce7ba2 | -3.77472 | -47.75228 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e6ee1d-3d74-380d-bdad-0428ba1c1fda | -6.48635 | -47.18801 | 2025-11-17 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db8e4a65-4341-3270-afe8-00a899f6bd88 | -3.44776 | -51.41854 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03488f77-5053-32ee-892d-726a38a14b15 | -3.34164 | -46.28859 | 2025-11-17 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ad071fb-09fd-3371-8a98-4e8073b355c5 | -4.77049 | -44.42895 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccd6138e-2d34-3ee5-8e58-f72b85317d53 | -2.95356 | -48.58978 | 2025-11-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7cc2031-f8a0-355d-b25b-8e8f225436c9 | -6.33142 | -44.75486 | 2025-11-17 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f14a0c2-aa77-3485-abfd-155908eb8027 | -4.72337 | -46.37587 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1db38789-9450-30eb-a234-4c600f5d4e66 | -3.30088 | -53.85382 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a13312b0-d932-32d3-b215-2c006755a3a2 | -3.39376 | -50.18073 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3ee8bc5-a497-371e-86c7-b6efd86579bf | -6.67967 | -42.0338 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b323bca7-c17b-3e7c-94f2-f943215f4408 | -8.29309 | -44.17195 | 2025-11-17 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eecf8ec0-4b94-3880-8b46-ec4cace00d46 | -3.28017 | -54.85134 | 2025-11-17 04:38:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81700e6a-bfaf-3b45-a3ab-4c0cc61b3474 | -5.8857 | -43.97336 | 2025-11-17 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3547f646-aa8d-30cc-9e65-261c5df8a8e6 | -5.57117 | -47.0946 | 2025-11-17 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e6fab94-a347-3dd9-a446-1bc8fec6d1c4 | -3.83718 | -49.80623 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 53e05a33-e643-3db3-971f-e941817809d4 | -3.7481 | -47.59329 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8aa4702d-896e-3c3d-957e-293aaa5cf860 | -4.00534 | -48.97695 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efb22efe-1125-321a-ba50-0d9dfb19cbb5 | -2.91682 | -47.84388 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e07add14-d21b-3141-a84e-80eea9a79d4c | -4.68991 | -46.30744 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed09ee61-c6ec-30a0-83a0-8288a4b2d7ba | -4.72688 | -46.37634 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 260e8db2-59c8-330b-ab73-dda73bf080d8 | -3.19262 | -51.61082 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20109b37-162e-331c-8dcf-da8e2e8b039a | -3.51209 | -49.92492 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd62f2b4-a36b-3a84-9b91-ab586d430826 | -4.66197 | -46.39525 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9524e6f-89fc-343f-8243-15a767ff6132 | -2.1682 | -48.43119 | 2025-11-17 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1a40141-45b2-304c-bdaa-5bcd84108955 | -1.06174 | -53.02931 | 2025-11-17 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 807a0d22-6170-3650-82dc-e58911d2e755 | -4.45975 | -49.78632 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b8a4165-80fe-3bf5-b879-95bdba8436d4 | -5.49514 | -39.16993 | 2025-11-17 04:38:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 40324809-a1c0-3c7c-9362-edbab1949141 | -3.91271 | -45.79821 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d7666935-223f-35fa-a685-bab23af60713 | -4.01799 | -48.81001 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86928382-d1a5-34f9-8716-814ecd25ba21 | -3.65457 | -50.2252 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da88c4fa-f9bd-37ee-a14f-a12bdf1a3203 | -3.49182 | -50.33648 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e1c9410-3251-3bde-8cf1-1eeac32326e6 | -4.55317 | -48.47516 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc4bfee5-6536-3417-9d86-a28a7a87eb16 | -3.07329 | -45.20558 | 2025-11-17 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6e6ee70-0b83-3742-8226-d30e8de557e5 | -4.39212 | -49.65421 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2382f6d4-4b7a-3371-89de-16f57544ec24 | -5.40973 | -44.06713 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdfc7214-726b-3d71-8331-93200d499822 | -3.55838 | -41.99476 | 2025-11-17 04:38:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2dabd36a-7d6c-33ae-bec1-60db6fd9af6d | -2.94326 | -50.38607 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46932f8e-4f8a-3e76-b004-e777939a5cf9 | -4.61258 | -50.6683 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f61382df-e678-3073-9987-5dd9de3bd479 | -3.39937 | -50.18898 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d09361d-3cde-3ec6-9cfe-f3acb9bf07d0 | -3.27994 | -51.26725 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b91795b-d99b-3d9e-b114-45c8fe9b6b14 | -5.92512 | -44.01537 | 2025-11-17 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5abc5827-d43a-3427-a3bd-4ee9ccff80c4 | -7.26043 | -48.01503 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98ef8d9d-1aa1-323a-ba78-932abba51c09 | -6.71323 | -42.93937 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b6c96f24-8743-33e6-a279-ed6db4f59c4c | -3.24441 | -51.35129 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b32172f3-8f43-3947-b1a3-d6b58dbdba35 | -3.89285 | -47.19186 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e537c6a-602a-3144-ba07-f0be3e061fe5 | -4.66083 | -46.74026 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bdaa42e7-ca4d-3253-b022-ecd7e2d939b9 | -4.9969 | -44.36333 | 2025-11-17 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8f352b6d-30ee-318d-8dca-7cb8276e27ab | -3.18585 | -50.6509 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1101b08-3289-3f57-9a2e-7b116530b071 | -5.35638 | -44.86654 | 2025-11-17 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9057208-05c4-3d03-90bb-b3c119429f0c | -3.88328 | -47.18668 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54ab78ad-8ba4-3043-bdb8-4e0f640598fe | -4.13068 | -47.29444 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 975ce611-3621-319a-b101-2f0843d186c4 | -8.06693 | -46.47398 | 2025-11-17 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4eb110d6-056b-36be-bdd0-8c379b9138bc | -3.77053 | -47.64728 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a22251cc-8570-3da4-9384-b0b3ef32fb67 | -3.95504 | -49.29716 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4ed6d1f-9906-3e90-9935-64461f1715b4 | -4.12449 | -47.28977 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f213618e-fa6c-3d89-9e7c-bab2d74dd2ad | -3.88377 | -46.45938 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58e2fefb-4cbe-39b5-9950-8ecf893b2d41 | -4.11023 | -46.07322 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59991a0b-855c-3c35-a40f-81133c2bddf4 | -4.69482 | -46.30304 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0596cba6-2ab8-351d-96d8-af5a7dbbd0d7 | -2.50636 | -47.81542 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6a3d66e0-5ead-3eb1-b14b-5cba313e1e44 | -2.52016 | -47.81401 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51f0e756-7b6b-33c7-8910-8c4a11c0e7e2 | -2.9977 | -51.01395 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 199089db-6346-3cfb-9065-d09f840ee20a | -2.92293 | -48.63423 | 2025-11-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c07a185-dadb-36c2-aa99-494f9eb2cf57 | -5.03659 | -43.60464 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2213383-5e7b-3eb2-80e5-6e0c44638ad8 | -5.75137 | -42.71603 | 2025-11-17 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README26.md)
