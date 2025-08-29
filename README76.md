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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15ab3968-fcc9-3a99-8517-ebc4fc39fda7 | -20.47911 | -53.67682 | 2025-08-29 05:10:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dda1cc1-006f-37ef-a5eb-c7eed5163947 | -17.54445 | -46.6191 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d58a8b14-698d-3bd4-9402-a5e7f20861bb | -18.21589 | -45.58569 | 2025-08-29 05:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 988c8000-eaaa-360e-88af-031f83f7a8af | -19.14813 | -57.7896 | 2025-08-29 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 96a80215-5448-3c76-bba2-04287fdce761 | -17.54492 | -46.6142 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ab62d2c-0e10-3e9b-b0b0-a61e0bbbbdbc | -19.00308 | -57.62461 | 2025-08-29 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e2fee916-55f1-3d32-85c4-4a0dca3360fa | -18.97733 | -52.9422 | 2025-08-29 05:10:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 604f7877-be62-3963-a516-56ccd3bdb607 | -24.17089 | -49.56926 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 630744f6-b4d8-30c0-8b10-866be68ad175 | -24.16534 | -49.56874 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1276b2b0-48b9-3946-926e-ab4fb27a0c6d | -18.98101 | -52.94666 | 2025-08-29 05:10:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52e3c144-02dd-3e55-b24d-bd721993e1bd | -17.5398 | -46.61788 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31032d47-77d2-3bf1-af8f-97141c2d0868 | -24.17052 | -49.57335 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a5c8e800-1f2d-3d24-b8d9-0b946d887f8c | -18.97684 | -52.94611 | 2025-08-29 05:10:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2794ad7e-b0e8-3921-abb6-0ff9b5f2aad9 | -17.53782 | -46.62331 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab29b6c7-4cc9-36dc-98f7-fafff4a7798f | -19.21002 | -44.92226 | 2025-08-29 05:10:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cc015e0-adc4-3051-a74b-1e1540a3a377 | -18.18975 | -45.59896 | 2025-08-29 05:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c652520-cec1-3d8b-9549-1bfb3b052984 | -19.14478 | -57.78902 | 2025-08-29 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 02fb100a-1603-3d7d-a013-3c026a77860d | -28.30134 | -55.62553 | 2025-08-29 05:12:00 | NPP-375D | GARRUCHOS | RIO GRANDE DO SUL | Brasil | 4308656 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| e4d13dd3-8cb0-31a5-a08b-d5dcd156bfc1 | -28.70052 | -55.58617 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 6e787ae0-37f5-3b2a-adc5-8d3a98cd3db7 | -28.70076 | -55.5816 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| a93d1c3d-c9c6-3798-918b-6412b1e3bce5 | -28.70412 | -55.58818 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 9f15bbe1-12fa-3e52-a3c0-71958425c5c4 | -28.73564 | -55.63513 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 988479cf-a83c-31e6-a7d9-892805aea1df | -28.72891 | -55.65787 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| b0fe9d13-a418-3f8a-9cff-21e385b739a2 | -28.73763 | -55.65324 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| eab80298-d87c-3b29-b71b-316fd8f3f5cf | -28.7336 | -55.65264 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| f6f07cf7-a5c7-33f9-ae44-0f0474b87143 | -28.70123 | -55.58024 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 42bf6c7b-5740-3891-9208-653620c2b2cc | -28.73026 | -55.64619 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| b820d044-5a04-3e6e-8873-000fba8ac532 | -28.73429 | -55.64679 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 2c3d86b1-5641-31de-bdaf-e8264ff7c946 | -28.73293 | -55.65848 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 540cb78c-b71d-3f60-a339-73fd28b0bac2 | -28.70009 | -55.58752 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| c5074d1a-06a1-33d1-9193-08d622534d39 | -28.73496 | -55.64096 | 2025-08-29 05:12:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 30e64a40-336d-320a-8bd9-23470a7fc879 | -4.14703 | -38.47538 | 2025-08-29 05:14:00 | AQUA_M-M | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| daf9386f-4d75-3a1a-8f57-98cb2d0ed489 | -9.59628 | -40.35617 | 2025-08-29 05:16:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.1 |
| fcc23708-fe61-3371-b378-3443227328f4 | -6.5486 | -43.90472 | 2025-08-29 05:16:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 45559917-b1fd-3e2f-bff3-47c7d55df8da | -5.6148 | -44.99055 | 2025-08-29 05:16:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2aac3d1d-74ca-376f-a9fb-b4faf8075da3 | -5.78176 | -42.60449 | 2025-08-29 05:16:00 | AQUA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 576eb422-2623-3f48-9182-941d3e7d1c39 | -12.08646 | -44.97258 | 2025-08-29 05:16:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 81349d75-8127-3194-bafe-76372165b7b3 | -11.87915 | -46.39062 | 2025-08-29 05:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 4c143109-5462-3a36-8aca-d603a32f8bc3 | -12.09374 | -44.70977 | 2025-08-29 05:16:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| f3a196db-8bad-39c9-9ec3-e0a20bfa1e11 | -9.48696 | -45.39406 | 2025-08-29 05:16:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| ee4be1b5-6b3e-3b0a-ba77-25241d5b3c33 | -6.26209 | -43.81237 | 2025-08-29 05:16:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 23daa2a5-05a3-3eb7-8b9b-cebfd743fb17 | -12.08809 | -44.72271 | 2025-08-29 05:16:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e39a0221-05f2-3830-a8ad-1638d7229e16 | -9.59793 | -40.34581 | 2025-08-29 05:16:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 4d759323-f6f5-35ff-b3dc-3e870245da67 | -11.3504 | -43.54307 | 2025-08-29 05:16:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cefed023-5f6b-3dd6-8080-6f67d1fb96f2 | -9.49508 | -45.37828 | 2025-08-29 05:16:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e44a965e-5f23-3b01-be9b-b593da453dda | -10.97621 | -46.89163 | 2025-08-29 05:16:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c4fb5b5f-1111-3b75-b306-581fc54bd569 | -7.05046 | -44.37822 | 2025-08-29 05:16:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 01c8a61d-28f6-3cf1-9a7b-0cc062475103 | -11.88015 | -46.39884 | 2025-08-29 05:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d2d394be-7a5f-303d-b5c3-c741f8b4d1ed | -6.54527 | -43.92496 | 2025-08-29 05:16:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| be32a30a-595e-3909-9b75-2e4e9e4240f5 | -10.9722 | -46.91661 | 2025-08-29 05:16:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| ad1ef6cb-dc89-321d-adea-5222c16dbe62 | -11.34776 | -43.55896 | 2025-08-29 05:16:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 45145c52-e9e9-3a3e-a40c-42a2d8fb21b4 | -12.09041 | -44.72857 | 2025-08-29 05:16:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 172ea3fd-bc02-340a-9019-39515c116a22 | -7.04075 | -44.3536 | 2025-08-29 05:16:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2d791398-2234-304e-8478-5134783034ab | -5.61782 | -44.99588 | 2025-08-29 05:16:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7b3c6867-aa76-3416-aaf6-36864c294f48 | -9.49104 | -45.36979 | 2025-08-29 05:16:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 1619a655-255b-3c8d-b500-956a90e99ea6 | -10.97739 | -46.88707 | 2025-08-29 05:16:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 19c3bcb7-7b25-352e-9a95-4734649f5e5d | -10.97081 | -46.92108 | 2025-08-29 05:16:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2a5748f2-0975-3944-b34e-18c92597adc1 | -13.18305 | -45.26554 | 2025-08-29 05:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 023097ad-2fa7-319a-8a37-d01b13f19b16 | -13.41591 | -46.99 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 91a35fe0-7f4c-3561-ac9a-2a1894d6f71a | -12.91139 | -48.13164 | 2025-08-29 05:18:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 0654b475-8835-3a25-96c2-37cde80c1baf | -13.54946 | -46.86288 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9d6383e4-37a6-30ae-b6a2-575af1579ecc | -12.70105 | -48.18277 | 2025-08-29 05:18:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 36cc9258-a19d-3c9e-80d3-1b62ec78284a | -13.54133 | -46.88287 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f847b338-32b8-3d17-8105-b85ad509e4d6 | -13.42157 | -46.95884 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1fdb92e3-563d-34e1-b6b2-bd54e298c717 | -13.18109 | -45.27263 | 2025-08-29 05:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 71f97734-cfb4-31bf-9a9f-527037ce9f4a | -12.69521 | -48.17412 | 2025-08-29 05:18:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fb322ac2-8162-36e2-8e2a-859858887419 | -12.68481 | -48.18053 | 2025-08-29 05:18:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a9f78e93-41c3-3e29-9767-11d9c385f7c6 | -13.54602 | -46.85697 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| baec36d9-5a92-3a91-b951-7491daec23fd | -13.1923 | -45.28809 | 2025-08-29 05:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b5b8fb06-b538-3e3b-8e80-a9d9d5a2505f | -13.50805 | -46.82169 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 41c38db8-00e9-36a5-9dc1-93e571ae46ad | -13.50351 | -46.84632 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 24b01732-6f4f-3251-bcd0-e4264e0a313c | -12.91515 | -46.34082 | 2025-08-29 05:18:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4ff70c7f-e2e2-3b38-8fc1-2fbcab8ad965 | -13.42154 | -46.96592 | 2025-08-29 05:18:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 13626aa0-fabc-32ed-a2d3-0be8fef1fbad | -13.19383 | -45.27496 | 2025-08-29 05:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9b2ae47b-3c07-3934-854f-7967f40821a2 | -12.921 | -46.34705 | 2025-08-29 05:18:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 149c06e2-b2e2-3492-88fd-f560fcc8b4a6 | -10.9709 | -46.9266 | 2025-08-29 05:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 358f54e3-037d-35cd-902d-7e5d09e8625b | -13.4208 | -46.9864 | 2025-08-29 05:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cb923036-f6ad-3441-b948-86941605cd87 | -9.7728 | -64.2657 | 2025-08-29 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5e71d37d-8cdb-3709-ac8d-f66c38d274e4 | -9.1154 | -65.7886 | 2025-08-29 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b6c5b3ee-df42-31c5-ab5a-e4223e8a7861 | -8.1758 | -61.3755 | 2025-08-29 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| eaf0c893-0a37-3dea-a84f-811f4ccb641b | -9.4433 | -60.5499 | 2025-08-29 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7a0944f1-967f-32a1-8dc3-244f4098718b | -9.462 | -60.549 | 2025-08-29 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 1883b00e-9de6-3797-b7a2-81a7a6f0449e | -9.4618 | -60.5682 | 2025-08-29 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| d9418453-fade-318c-9556-25a5371f109b | -10.99 | -46.9242 | 2025-08-29 05:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7fd7a12d-dfc2-3236-9d41-4c3c69cd93c3 | -9.1155 | -65.7699 | 2025-08-29 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 5173b3cf-7795-3f66-ae04-3e00975ab71a | -9.4432 | -60.5692 | 2025-08-29 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 630f2a5f-a0dd-370c-98a8-4823e34ad5db | -3.4254 | -49.0517 | 2025-08-29 05:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| ae3a1bc9-05a2-36fc-8301-e092d3746b33 | -12.6875 | -48.1899 | 2025-08-29 05:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 46cfc667-90bc-3c5f-8610-e173fa527562 | -13.4212 | -46.9637 | 2025-08-29 05:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 05858a11-e0e2-3805-a0bd-00157c2f2bc7 | -9.773 | -64.2469 | 2025-08-29 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e57ac48e-034c-35c0-8787-4d6081526d20 | -19.21042 | -44.91687 | 2025-08-29 05:21:00 | AQUA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 0eabcc26-5f33-3530-97ce-3a3a5cf9a532 | -24.16262 | -49.57678 | 2025-08-29 05:23:00 | AQUA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 1db5ea08-a7f5-3dbb-9d1e-dc90e02d07db | -3.76304 | -54.81672 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 496bc143-9ae7-374f-96d5-bef1737c4682 | -4.14039 | -54.89729 | 2025-08-29 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b381579a-30bd-3807-8306-4f7df36a4cef | -6.97043 | -59.32633 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e868381-e301-373b-aba4-cb09b3a549be | -6.71142 | -49.45747 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8214175-46a4-3a2d-a5e8-dd51f92464e5 | -3.7669 | -54.82191 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| a8a70228-ae70-31ea-af47-2fa72508ded2 | -6.98054 | -59.33208 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd950ff4-3be1-380d-a1c5-d1a7b1128ab6 | -3.79298 | -49.42796 | 2025-08-29 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c7f066a-7359-30e3-a41c-7d66785c400f | -6.97401 | -59.32689 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README77.md)
