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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e12fb340-7af7-3fa1-8071-4539485fbc2a | -3.96852 | -48.08486 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cae7a81e-e504-3abe-ae6e-9b1d0a3edaf5 | -5.98021 | -45.3638 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| dbc01471-35f1-3084-bf4d-da237e9f7afb | -3.33878 | -50.07778 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9461076e-0c14-3f41-839d-8b119d6ac4dc | -4.73644 | -46.5098 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad62ab4d-d2b5-317c-b8f3-f968c4e90972 | -3.68561 | -49.57029 | 2024-11-28 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fd3caab-b2fd-381e-9706-a57401307737 | -2.88446 | -51.58625 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47361ec2-2b4a-36de-bd8a-9bbdee25df2a | -4.65863 | -46.9257 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1f65ead-0a39-3ce6-89e7-c79d6c35d1a3 | -3.48867 | -49.89619 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35ce2117-c17b-3921-a136-bf95d0e8fce8 | -2.8017 | -51.59005 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3742370e-2e6a-3d1a-a794-9d894b8bb6cd | -4.65626 | -49.52023 | 2024-11-28 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c7d3b48-03ab-3465-9c17-fc9f38f07a79 | -2.0526 | -47.12132 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 642d8ca1-d909-3695-a41b-58694df19847 | -3.03423 | -48.50304 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 835aaf46-b0a1-3aa3-8b99-4ac312e3ff9b | -3.78209 | -50.1382 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 830a52a3-1dab-365e-895d-084a68b27d6e | -5.46892 | -38.02637 | 2024-11-28 03:59:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf3e24c7-ae51-3cc3-9165-de3b48e1e180 | -2.85693 | -46.87214 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f09a85c-03cb-329c-a423-286393e6afbf | -3.59342 | -50.69051 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ab5c5d3-c301-3834-96c8-ac6adf397eb9 | -4.65787 | -46.92698 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fc7c5a0-4460-3696-8496-df64248a15f3 | -3.62743 | -42.40356 | 2024-11-28 03:59:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1b673f3a-f33c-32be-b69c-4eb5ab9bab10 | -6.37444 | -45.6959 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6ba61398-47e8-394d-bbbb-bc88e0eb945e | -3.38927 | -50.11869 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f203fb00-0396-304a-9673-fd604db2a636 | -5.83197 | -44.07341 | 2024-11-28 03:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad54a4e8-71d3-3518-99e3-2634fbf53115 | -3.54089 | -44.9417 | 2024-11-28 03:59:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3422bb2a-1e71-33e1-9f62-6326098c4d41 | -6.64297 | -46.5393 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29de0646-997e-3f92-812d-df0e4d41b8c2 | -3.78365 | -50.12931 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5c3c21e-bf55-347f-8198-87c032b7c550 | -5.07765 | -44.83896 | 2024-11-28 03:59:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 571dd00f-3066-3ece-ba7f-43481390e00c | -5.94871 | -39.6638 | 2024-11-28 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| f774e7a3-3068-3025-aaf0-5d7a844c621c | -6.3751 | -45.6919 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4df3f12a-a6bf-304b-bbd4-9687d6f0f545 | -5.98314 | -45.3722 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78a49265-1fb2-3a33-a55b-5772bab52ba9 | -4.15206 | -43.81709 | 2024-11-28 03:59:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c13b8af-c1af-37d2-8abe-76d0ebfe6e58 | -1.3327 | -51.95576 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c3586c5-9768-32ab-990e-c2d2431b726a | -3.34475 | -50.52408 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9570fdd8-e6b5-3ba5-8dfc-4b366fc6900d | -6.35013 | -44.80891 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc0147c6-573b-31a4-adb2-1f7e54339f9b | -3.10272 | -50.36275 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f43d2c8d-c7fc-31b3-a37e-e8956376e3d7 | -2.95404 | -51.28819 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cba1ee8d-1b60-355c-811a-01b2f0863d84 | -2.32022 | -51.95987 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d71ad40-30b7-3b96-895d-c8f82696b8b6 | -1.72025 | -52.48427 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5defd3ae-6097-3f49-80d4-afc31239b577 | -4.3526 | -43.32168 | 2024-11-28 03:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25d6d8a4-c011-3d3d-86c1-b7d30d614e43 | -3.37798 | -50.11219 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab29cafa-57f8-3245-9d8c-4c580a4c88d6 | -2.84713 | -46.87054 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23283e8c-3fd3-3531-8414-3f7dacb95e03 | -3.99911 | -46.31408 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeacf795-42f6-36c9-9e62-9912a9ab986d | -2.82931 | -46.84376 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3502cc5-747c-3c49-9969-89ee0009026f | -5.98441 | -45.36451 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78f34701-55e2-34b1-bb8b-7493ec1f961c | -5.16387 | -37.33311 | 2024-11-28 03:59:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68688bc5-27a6-3e77-961d-981eac402177 | -3.08017 | -49.21224 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d37617fa-0878-32e3-9a7c-24111a659dda | -4.3171 | -48.08464 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a29e9bd-5552-3a9f-af3a-114e0ff4290d | -4.80815 | -43.29879 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e27ba8f8-4765-3b77-83ec-9fb45fe21eca | -4.81044 | -43.30848 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3d65d78-70c3-324a-bc9f-db5b31fca046 | -3.81669 | -46.60432 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 586824ae-e321-38aa-99c0-285bf7735ce4 | -3.56287 | -51.03563 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dcb4a48-ae40-33c1-91dd-a79a98447623 | -3.16889 | -48.43757 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c3b63bd-a82a-3ab8-b861-0b1bcc563b0f | -4.21836 | -50.88724 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c32324d-e5e2-39a6-95ed-cd0cc67927f2 | -4.72607 | -43.25525 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbb24019-998f-34e8-ad07-15de655d2e17 | -4.64189 | -41.12857 | 2024-11-28 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 41924073-7fc2-365a-b3b8-1b1095e9bf82 | -5.82947 | -44.11263 | 2024-11-28 03:59:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a5a8969c-2c10-32b6-a5d3-5c7b84095bbc | -2.65665 | -49.5101 | 2024-11-28 03:59:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 046c30c4-7441-30a0-aef2-aeca886cfc82 | -6.01321 | -38.66106 | 2024-11-28 03:59:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 30e004fa-0e43-3b5c-b4ee-439600666151 | -5.44599 | -43.24893 | 2024-11-28 03:59:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 359ce34c-69e3-3d77-a641-641ac8fb4104 | -3.78688 | -50.13394 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 808b5105-9a29-3662-8538-cab2b1d586ca | -2.84085 | -46.83447 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d18f031-518d-32aa-97ec-58f2ffe182d5 | -1.66555 | -52.72958 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1136ceab-d66e-3189-8b39-2105807a59f1 | -4.20782 | -46.55147 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd7124c-f10e-3805-acd0-9ca857e4e5d7 | -3.26765 | -45.37703 | 2024-11-28 03:59:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9216b368-4327-35a5-b30e-938df9dcbd05 | -9.00396 | -35.99136 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 26f9fbd5-7dcb-36c3-b94e-6cc79ed9b48a | -4.00517 | -44.28519 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f33be2b-3409-3ffd-8321-bb6623003c35 | -4.35242 | -48.68469 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faf6275a-6352-36e7-9fa3-144ddf2dee98 | -2.88013 | -46.85358 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 739c17f6-859d-3250-9564-31f4359fd645 | -1.64316 | -52.46372 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85ee86dc-1f0e-30a7-9721-13d8fcf4363d | -5.09149 | -45.84269 | 2024-11-28 03:59:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce52822b-7139-385d-91d1-a69b7fef232f | -3.38773 | -50.11843 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 537ea6ed-f048-31e3-9a58-a083345240ca | -2.84773 | -46.83708 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f05769a-e512-3eb9-8efa-c555c1fed518 | -3.80629 | -52.35583 | 2024-11-28 03:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a79c35d-aa0d-3046-8e50-a58716b7b525 | -7.26525 | -48.50217 | 2024-11-28 03:59:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38dbec35-d80e-3cc1-b894-677b595aa4b1 | -3.30085 | -50.41464 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 831a3fd3-5dbb-321a-a3f3-b8d3fa70a4d6 | -6.46651 | -39.85232 | 2024-11-28 03:59:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de1cf4e5-ab62-3507-8fd1-cf0e599b97c4 | -2.74776 | -48.66143 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 855aa758-302f-3409-8ba3-4e8686cd9fcf | -7.69283 | -42.98182 | 2024-11-28 03:59:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 42be7c6a-442e-30d0-b54f-df6c6f5ae08d | -6.12402 | -46.58573 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c038b4e5-d737-3f95-806e-f0be43bd0a30 | -2.95577 | -51.00591 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4346135f-04b1-33c6-a4bb-df4d69bbe5e5 | -6.56919 | -46.56416 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0f5f88c-6863-3dbe-8b31-8a249953d02b | -3.4904 | -50.07819 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dc7e345-6704-36d2-ab0c-49db87a51763 | -2.64858 | -48.48203 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01dc88dd-24f7-3dc1-99d0-70fbfe8de57b | -3.57834 | -50.33223 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3aa20b9-a8ea-3847-afd8-37123c0f9e2b | -4.48362 | -48.11721 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d6a6c3d-f172-372c-91f6-63b7a2c72d30 | -4.78012 | -44.42664 | 2024-11-28 03:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 476da052-ad14-3abd-99ef-1068c290003d | -3.38552 | -50.10445 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea9dc35a-8ad7-3480-a4be-57541c77a7f9 | -2.74714 | -48.66505 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e04c38dd-0547-3d97-866c-0b0199e2c900 | -4.12 | -48.81919 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 92ad91d9-1bb7-3c43-af05-e0e774cc3585 | -3.96272 | -48.08734 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e5e1d3ac-9083-3adf-be23-716d0a13f165 | -5.65923 | -43.36222 | 2024-11-28 03:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4cedb10-131d-3b07-a632-4ad2eb7d3e12 | -3.49379 | -50.08613 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30016130-059a-3c84-ae88-d25754fb9b76 | -4.74187 | -46.50566 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 635e2b8c-5c8d-3645-b510-b4970937984f | -3.24687 | -50.77441 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2ccd1f4-ee34-335a-9df9-77ee0dfdb356 | -6.66498 | -39.23867 | 2024-11-28 03:59:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b920904d-e5fb-3943-aede-21c693ceb667 | -3.20095 | -46.59795 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 19fc8270-ebd3-386c-8603-123e34bb538d | -4.0222 | -49.54702 | 2024-11-28 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a28419c-449c-33d7-bcdb-1fb23c2ec123 | -2.178 | -47.13958 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c6c3e863-6570-319b-bd8d-2f216bcd336c | -2.53123 | -47.32817 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0d2b529-4b41-3623-bacd-f6cb7c6c9abd | -3.59271 | -50.35812 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a3a1b3c-ea66-38aa-a900-cdc4b1e7dbef | -2.1601 | -48.71203 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88a4fffb-7d60-3b03-a949-d099d49c392b | -3.82151 | -44.44168 | 2024-11-28 03:59:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
