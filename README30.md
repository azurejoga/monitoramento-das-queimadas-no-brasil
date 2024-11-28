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
| 72a5e711-5ce4-358f-8b01-007abb324009 | -2.60549 | -46.83733 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ddc4224-713c-36c3-bd5d-36971f0f2410 | -2.91168 | -51.71067 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8b37f5b-1a52-3f48-95ad-997a468bb7a2 | -4.77265 | -44.4219 | 2024-11-28 03:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61a94ba6-454c-39e3-bc48-525baf084ca3 | -2.85751 | -46.83866 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f41d2f81-4dca-3796-919b-4ea69418bc64 | -1.04476 | -51.74027 | 2024-11-28 03:59:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ccaee6af-3d40-3a01-8594-bb8daf0c63e0 | -2.47583 | -47.03783 | 2024-11-28 03:59:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a2ac90f-0e80-3773-971d-66632aa8d436 | -6.0104 | -38.65699 | 2024-11-28 03:59:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 202eb883-f61c-3afc-bba8-ae84af054c43 | -5.11301 | -38.06921 | 2024-11-28 03:59:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc0e1b3c-55d1-3d06-9720-335773b2bd2f | -3.60548 | -52.53978 | 2024-11-28 03:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ba0d3d0-9039-3363-9bba-a330c36eb138 | -6.09023 | -41.9428 | 2024-11-28 03:59:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 09d174ae-9ff4-3105-9f49-1653ee1c6521 | -4.31191 | -48.08371 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 530ad6ff-2680-3881-bb31-1ff73134902c | -2.84315 | -46.86429 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae64b675-377c-31e9-899d-3bdecca237e3 | -2.74837 | -48.65785 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3224d2bc-4106-3fa9-894f-7b819531dc94 | -3.6748 | -45.79208 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 252388d4-e0c7-3164-af5d-4027bbe3d003 | -4.67318 | -44.62 | 2024-11-28 03:59:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6dd18d6-9e57-3bee-b6c6-342071b93acd | -1.32882 | -51.94153 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab7a563d-1a90-383b-aa9b-43a4df96f90e | -3.07924 | -48.66854 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3686bd01-4ae3-3ab1-b66e-d43245623a46 | -2.65734 | -49.50596 | 2024-11-28 03:59:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d50361e-60ab-3bfa-a6d6-e71124a4cb8b | -3.10098 | -50.36945 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8451f0f-49ea-391c-96d3-2b4126e5476d | -4.76156 | -46.37894 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70d53a76-fad2-344f-abc9-5dcdbf9f48aa | -3.29692 | -50.2515 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 088927b1-3239-327c-a88a-99e000e037a0 | -4.93294 | -45.42294 | 2024-11-28 03:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13fd9cda-083f-39d5-a547-6625061a67d2 | -3.70264 | -43.42656 | 2024-11-28 03:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37497086-ec78-3e92-a44c-52e342460cb7 | -4.44029 | -46.34411 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03e6d7f4-79d4-30da-8024-6c9beac2bf59 | -2.87254 | -46.86903 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40288dc7-49c2-314f-a33b-4d000920445a | -5.21826 | -44.91113 | 2024-11-28 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4ff43d8-815d-3d35-a33c-46cb14486b04 | -2.85379 | -46.84769 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3f980b8-d575-3291-a850-20fbfc4df0fb | -6.0937 | -41.94337 | 2024-11-28 03:59:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c89f9380-944e-3c0f-8604-6d1ae2a7493c | -5.976 | -45.36317 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5f7aa34d-63be-3ba4-b5cc-2c228e63c007 | -1.71651 | -52.48322 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7fca1cbe-4efa-36a4-9af8-1d8bcca84500 | -2.83969 | -45.33022 | 2024-11-28 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebb62792-cc08-3aef-8ad9-c9318c5d5b8d | -3.24757 | -50.61736 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6cc1cd44-3822-34d2-a63b-b1658eaa6923 | -2.96306 | -51.00181 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8b7e749-7e78-391e-9150-130f25374be4 | -4.22198 | -50.88613 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59d838fe-35f1-3dcb-a685-e94556ed9d4a | -2.8615 | -46.84483 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b90567f1-49fc-3d3b-aca1-9234d76c5fd9 | -2.26702 | -46.36243 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1750dab-8fc6-349d-b229-6d18031ede3a | -6.60268 | -39.20024 | 2024-11-28 03:59:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 67fec402-8104-36a9-b50d-c1c1bc2bde61 | -3.09962 | -53.25573 | 2024-11-28 03:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77c8b3e7-46b2-339d-aea0-d4e07a2d9c14 | -2.85955 | -46.84302 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f97f20bb-81bf-38fc-b450-86a3ad685b33 | -5.55101 | -41.42906 | 2024-11-28 03:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02645a3a-4bc2-3b24-a1a6-e5a32988ff48 | -4.17557 | -48.62709 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f8d4687e-ebe8-3dd4-a830-205f27579109 | -5.39153 | -40.65809 | 2024-11-28 03:59:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2dde25d-e8cb-3f44-8dc6-5b4c148f2fd6 | -3.69651 | -50.22805 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a589f65-d979-3c73-8405-c70e8f99c1e3 | -2.83507 | -51.83796 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b09c8409-5674-317d-bb24-490db76b6abc | -2.38824 | -47.16688 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 94810682-c8e9-3c1d-a7c3-39265aca2d2b | -3.49649 | -44.60503 | 2024-11-28 03:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada7a64b-1fbf-3e6a-b869-830de29ecd5b | -5.58156 | -43.14902 | 2024-11-28 03:59:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 70411e61-5992-375a-a749-0e4941aa28fa | -4.06169 | -48.96411 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c0f8991-fa5e-391d-9774-2458cea15457 | -1.67341 | -52.73768 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b2e6f9c9-b821-3b00-bd8c-34150b002405 | -4.48477 | -45.44035 | 2024-11-28 03:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fe8fc2d-ff17-307c-a43b-d40f30a2a402 | -3.26967 | -50.62554 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f57b7d5-c8dc-3349-ab65-1cceb9749baf | -2.62261 | -49.07411 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67654e20-53b2-3b9d-b5ce-e3195c79216e | -3.4383 | -50.0128 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26c4458e-1c93-3e9a-a289-868e5a8e4194 | -5.97893 | -45.37152 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d7d760c-7787-39df-8edc-eef99afb9d8b | -6.66641 | -47.87796 | 2024-11-28 03:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 839e6cfc-8521-3e7d-9ca0-adbe68fe59e0 | -8.50068 | -43.28406 | 2024-11-28 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 058eb475-d9e9-3321-a982-b0bfd6ad220d | -2.8441 | -45.33088 | 2024-11-28 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bfea0af-4a22-32a8-a3f9-f5aed2479733 | -4.18352 | -40.55902 | 2024-11-28 03:59:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 091d5d2a-643a-320e-ade8-e467a15b7bf6 | -5.90312 | -43.41005 | 2024-11-28 03:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bafef27-ee00-31ef-8123-e90f90f9b410 | -3.29333 | -45.52015 | 2024-11-28 03:59:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f35afe5b-7b6f-3834-82b0-a0ef91a43ead | -3.51298 | -50.30916 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd4f44f1-666e-3451-b73c-1483ffd85055 | -3.68928 | -50.22999 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36c69135-3fd8-3876-b5e7-80c7bbbe7fe3 | -8.4971 | -43.28346 | 2024-11-28 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc96a962-acd0-36b1-bce2-24386b60a820 | -3.17349 | -48.57822 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14934c20-7001-3162-a667-ee37027a4e5a | -4.50667 | -42.07235 | 2024-11-28 03:59:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 080ecf50-7c88-360d-9997-ffde2f2a9af0 | -3.09657 | -50.36169 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cbf300a-bc09-3a50-bbba-b4651a5606f9 | -6.75911 | -35.09933 | 2024-11-28 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 05750be2-64ad-38fc-8923-240551975e2d | -6.16095 | -42.61906 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c3fe9d45-82e0-3b8f-ad8a-94b24bdbc46b | -2.86042 | -46.83761 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b3d66eb-8a31-35a8-8a89-239771b46e81 | -2.80271 | -51.58418 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2bfda9f1-2814-33b6-9b04-ce9097c27e23 | -3.69123 | -50.22264 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21284a37-0496-3714-83d1-16f8fe9615da | -3.10693 | -53.25691 | 2024-11-28 03:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96634877-1e94-35c0-9294-680ebcf2c3a6 | -1.66219 | -52.4813 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fcd6a7d-462c-345d-b74b-c4bbdef8a37e | -6.54155 | -44.65462 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c193983e-dc32-3264-a230-7092f79d56d9 | -2.85466 | -46.84223 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e1c2160-f451-35a1-81f1-c06813eeb830 | -3.95051 | -46.91692 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 938c71e1-c0b6-318d-84d4-516749e10ca8 | -2.85783 | -46.8538 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaee5845-da46-3cf2-b641-59aec07c53b1 | -4.01333 | -46.98796 | 2024-11-28 03:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c43859-3f75-3a5f-a12f-a2741ed366ea | -3.58641 | -50.69409 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce845b95-5e07-3334-9c28-79d26a13921a | -2.63319 | -51.77761 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 86fd9f3b-012c-3e3d-8f7a-ae449410f0ad | -3.67106 | -45.78689 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e33fb43-76d2-359c-9927-568a8095ae11 | -7.75886 | -46.21765 | 2024-11-28 03:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 067f19e9-15cb-3f7b-9225-d8c64472a603 | -4.83966 | -44.29005 | 2024-11-28 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dba69090-58d8-3216-9b5e-6c55e90689c4 | -4.66969 | -44.61576 | 2024-11-28 03:59:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90579a6a-08b1-327f-a90c-c6074039631c | -4.47415 | -46.36288 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55154c77-2ae2-36ef-933b-92f7e9e824b8 | -3.97529 | -46.73981 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19765719-59d4-310b-80ed-d482f1f14245 | -3.09647 | -50.359 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e34e0e2b-ecc9-3ff2-8b2c-47e5b8e0655f | -4.12001 | -48.81832 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e091d84f-fb59-310c-acce-96e793e4dd87 | -4.05752 | -46.6856 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4777fdbf-5cb2-3e3c-8653-56039a88b40f | -7.70573 | -42.9923 | 2024-11-28 03:59:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 678cb4a2-c6f1-3055-b751-4cca02a16c6d | -4.56985 | -37.79393 | 2024-11-28 03:59:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c5d857a-2e14-3377-a813-bf379ae35f85 | -4.92864 | -45.42231 | 2024-11-28 03:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 329df9ab-610a-33da-a67d-b849d1f3a092 | -6.3634 | -47.06004 | 2024-11-28 03:59:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2bac916-b487-3b70-ba91-5df7fb705cb4 | -3.56967 | -53.02523 | 2024-11-28 03:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58122ffe-15a0-39d5-bc79-f0afaf710113 | -4.17617 | -48.62363 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e10f8a55-5647-3b58-82e5-ea328217603d | -5.22239 | -44.91182 | 2024-11-28 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0c02fed1-3b69-373e-a1ff-9e4745a0fc39 | -1.65623 | -52.47313 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47072186-994e-3c20-8d56-7efeb7258d7f | -4.25869 | -40.70169 | 2024-11-28 03:59:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f4ddb04-e3ae-35ee-8046-198cb93ee74a | -3.93959 | -46.8934 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 760750d0-4746-36c0-9b1e-65acc51e33fb | -3.66944 | -45.78406 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README31.md)
