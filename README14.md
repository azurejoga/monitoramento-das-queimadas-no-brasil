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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16f4671e-4694-3dd9-9c89-f7ec0064fa84 | -1.6491 | -45.87171 | 2024-12-27 04:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31c22dc3-015f-3449-a5c1-f12d9e553a0f | -2.28785 | -45.57437 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e08ee4b-90e4-331c-9431-33c7df61ea1a | -5.64526 | -43.71589 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be4c3565-782a-3b3a-8d37-0f5603263913 | -3.76139 | -47.21767 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f90f7154-1488-352c-8779-ae2664d09466 | -5.63943 | -43.71489 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 697ab438-2032-3906-86f2-b635f70c5482 | -4.04866 | -47.03903 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ace09e1b-0830-3fb6-ac7d-4025163d8a3c | -5.64585 | -43.71179 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5dbd5b33-e610-39dc-a1f5-eb6c7f679041 | -5.94338 | -44.44492 | 2024-12-27 04:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 294c64d6-f8e9-3796-aecf-b585b93fa56e | -3.91403 | -46.91104 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 633e8451-e8cd-3195-8d7c-7ac0cc370882 | -4.52602 | -42.06142 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce956cb4-1787-3d12-9fec-1bebf83f98d9 | -5.31394 | -45.45438 | 2024-12-27 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae1cb9db-cc57-3a78-a0da-b1b5da30d0ce | -5.21065 | -44.90633 | 2024-12-27 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea85a894-0fa6-3c6c-b066-20079ca7ff16 | -5.64415 | -43.71792 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 513b4f5c-16c4-3c73-a8a6-562dc98f7aec | -3.93662 | -46.97836 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f640f24-22fb-305f-a6bc-86b2cf37faca | -3.89735 | -46.98923 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8c31d3-66aa-316d-8c68-176180286d9e | -5.91218 | -43.48351 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ac15dde1-0c32-30ca-b2a2-933e24c17110 | -5.63944 | -43.70862 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 184ecb7d-02a9-3c7b-93b8-6b5c955ba149 | -4.52526 | -42.06659 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcba7d3f-2c19-374d-be24-c7d8c20dfa5e | -5.64061 | -43.70662 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99e32e21-1f60-3207-9515-e00b60c799f9 | -4.04341 | -47.04305 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed14d4ed-f0aa-3744-a637-603dafdc219c | -3.93072 | -46.98665 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14b94b8f-06a7-3e7e-9cff-83c5d7ecb900 | -5.9051 | -43.49089 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f34498be-8494-3d75-a56d-c2b271547d93 | -4.32221 | -46.34216 | 2024-12-27 04:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c2fabed-7928-3c29-908d-d7ee2c862a84 | -2.49262 | -54.13992 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3a69d1b-3ac0-3bcd-9736-7023e5f29d86 | -2.53178 | -53.95727 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b50cb24-0e49-3fad-8ee2-6c8a4f510739 | -5.91409 | -43.49074 | 2024-12-27 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cc534846-e26d-30f7-aad6-03d6a290d0c2 | -3.90189 | -46.99005 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8088775a-cd9a-3259-8918-dfeb0dbef2ac | -3.89736 | -46.99148 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea7ab88f-feef-31e9-8030-9955ad81c4c9 | -3.89668 | -46.99615 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 815b3f21-1a9d-36c5-a59e-2ea7ce88f3df | -3.73342 | -47.17931 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95f3755e-369f-3d20-b889-627359d499f7 | -2.97157 | -54.6216 | 2024-12-27 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3887351b-b4a6-376d-b166-ec0461ac10a2 | -3.73679 | -47.33662 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55872a4f-879f-3126-9bc4-dfa7073d309b | -3.92682 | -46.9815 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5c8f0ff2-b49d-3917-ae71-adef9ddb9649 | -5.21603 | -44.90708 | 2024-12-27 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 625576fc-b24f-3859-8464-9ef07affd230 | -3.09053 | -53.71956 | 2024-12-27 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00f9516c-b7ef-391b-a0c6-d50a4b759bbe | -3.68404 | -47.17166 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cef42d3-f71a-33f0-a146-9a256de76499 | -5.63775 | -43.7211 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46c86d78-c18b-33bd-8f4a-b48525948fbe | -3.74123 | -47.33729 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27cba520-c11a-39e2-92c3-67aec6b25879 | -3.9033 | -46.98088 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3377c789-4a0b-3e4e-832b-4a5e309c7bbb | -3.76074 | -47.22209 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d99227d-987e-37a2-9756-42f600169911 | -5.9147 | -43.48647 | 2024-12-27 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6c8e6d05-a5ad-3331-8eaf-8b6067972136 | -5.65229 | -43.70852 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7d6fd9b-3986-34f1-bfce-1ecdc13732e8 | -4.04072 | -47.06112 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2245854f-88a6-3578-bf4a-a025bea3c48d | -2.74315 | -54.03333 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46b25b90-d506-3ea8-b550-c87f00ed554a | -5.94287 | -44.44859 | 2024-12-27 04:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 381c2aa3-67dc-3e9d-9cb2-eaaebf758b3d | -5.91159 | -43.48781 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| eec64456-8dd6-3bbf-8973-b1dfc97f641a | -5.64527 | -43.70964 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7bd1f6f-0263-38b7-8b50-9b72399666e7 | -2.39883 | -54.17921 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8754f1d-d265-31b8-94b3-74bae29f2c16 | -2.40719 | -54.19125 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060827e5-7093-3aaf-9d20-0d497b077e19 | -3.40346 | -52.521 | 2024-12-27 04:57:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b5ee63-c751-3b90-a6dc-21316951dcce | -3.92158 | -46.98536 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee5e65a4-0be8-3510-8084-c52308a1dfee | -5.63241 | -43.72223 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 565a4e29-0496-35cd-ba99-6dbca23365d2 | -4.51743 | -42.08218 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9ca80862-75ef-33d7-9752-371d759ccc64 | -4.51735 | -42.076 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8221f0de-9288-369a-9768-c2865fc3aed7 | -5.9016 | -43.493 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4639319b-7707-3b96-9f6e-c85f4fdcac8a | -5.64467 | -43.71997 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2fbfa260-8744-3377-8841-82f472b0df30 | -3.72826 | -47.18305 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b49049a-08bc-3cdb-9295-0de68b2f42ce | -3.91086 | -46.90108 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2f32e59-7ece-3cbc-9a4d-fd7ddebc34de | -3.94051 | -46.9836 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a98cbc0-0e79-3a5f-9353-9436878716b5 | -5.90815 | -43.48972 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6af7163b-917b-3a68-8607-0a9397f7ec0f | -2.52492 | -51.86563 | 2024-12-27 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a807f930-ff47-309a-9554-ac705b7dc81c | -5.12802 | -43.24093 | 2024-12-27 04:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2bb1af2-d8b5-3ca3-abe3-7cdb9685ff2a | -4.04798 | -47.04364 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5522d6c2-04d1-31f0-80af-2eaa50026986 | -3.93139 | -46.98217 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0fd63782-0289-35b2-9cf6-36cd168aed37 | -3.93595 | -46.98286 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2766258-587b-3dfc-bb57-85e1ee3963cd | -3.73543 | -47.34544 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45ea5190-219a-31da-80fd-1951392822f0 | -5.90452 | -43.49511 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc145668-8165-3a3f-b0f0-282d5a5660e8 | -3.23055 | -53.62457 | 2024-12-27 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4dfc7525-048b-30db-acfb-43ca1bcb0a78 | -4.29767 | -42.3237 | 2024-12-27 04:57:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| adc5ed1f-4d3b-37d1-8a3e-2f13535665dd | -5.949 | -44.44566 | 2024-12-27 04:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a263066-b17d-387b-9220-595a8d072b02 | -2.52151 | -51.8651 | 2024-12-27 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9711175a-a74c-3006-baa8-e06475bb0eb9 | -4.52033 | -42.06143 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15c41f70-2eac-35a1-9286-919007dce192 | -3.0201 | -48.48419 | 2024-12-27 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c8c21ef-a100-3388-9c36-4b549e5226e2 | -5.37049 | -44.84528 | 2024-12-27 04:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d87cf56-aede-3b12-9df0-9b2bc3a8b4d7 | -5.64002 | -43.71075 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4145c7c1-3246-31c5-bb88-4297655ef4b7 | -4.30394 | -42.3247 | 2024-12-27 04:57:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a055dd22-8cc4-3358-a530-f28d8018137b | -5.90283 | -43.48443 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56f06f92-dada-3829-b3e4-30669085923c | -5.64585 | -43.70542 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1f2bcae-eca5-3fac-9775-cad247581f56 | -3.09108 | -53.71611 | 2024-12-27 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db7d4437-ca61-3836-9912-a196eef8b672 | -5.31503 | -46.05719 | 2024-12-27 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b912cc30-8e00-32a5-84eb-577e4be0a75a | -3.73969 | -47.33482 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97406c1a-e58e-3f9d-a79b-2e0f790db69f | -6.23018 | -55.62289 | 2024-12-27 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c5ca124-72a1-3bf2-a107-f120c1774afa | -5.63825 | -43.72311 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 641d23b3-90ad-30e9-bc70-b20db1d54107 | -3.73611 | -47.34104 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef12994f-b933-3df5-ad96-db9e373e547b | -5.13464 | -43.23736 | 2024-12-27 04:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c1f5c00-271b-3f42-8d20-80acdf922488 | -5.90755 | -43.49392 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c1057a3b-c453-3baf-9096-3ffa4d8349bb | -5.5739 | -46.13755 | 2024-12-27 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5194dcc-bd15-32c9-8265-4ac8be78f254 | -3.9026 | -46.98545 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d937ab-e8aa-3802-8732-07bae8fc8a42 | -4.51815 | -42.07698 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 061e2185-1d56-381d-b7a5-68f18c64899e | -5.64359 | -43.722 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 611da03c-1dbd-39ed-85a6-cf390ac94b59 | -5.31058 | -46.05738 | 2024-12-27 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d80fa225-1282-34de-bae7-246acac19811 | -3.91074 | -46.93166 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ea04d01-1e3b-327d-b282-577e5f30b0cd | -3.92549 | -46.99052 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40a98850-eb3e-3edf-aef9-5a86a53121cf | -3.02288 | -53.89242 | 2024-12-27 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e11bfc-525c-3538-a0bf-3e3631c4a9db | -5.2165 | -44.90377 | 2024-12-27 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4968499a-e45c-3d28-b031-1df260dab465 | -2.38243 | -53.66133 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7ae2b1a-7310-33fb-bb12-9ad025a7eec1 | -2.98963 | -53.88723 | 2024-12-27 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f4e1186-28b1-3ced-a44e-7e9d5d6342dd | -5.31007 | -46.05634 | 2024-12-27 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b17f589-9fcb-37eb-9526-7f470e1c97cb | -4.55984 | -44.1267 | 2024-12-27 04:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe2b836f-611e-3dc5-8c8f-9182e993cb43 | -3.89662 | -46.99396 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README15.md)
