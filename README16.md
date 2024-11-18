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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd69ea48-2c74-3cd9-acfd-663bd52cbc5f | -2.54783 | -47.29605 | 2024-11-18 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e802b31-2601-3df9-ae69-ee481bea4546 | -2.54536 | -47.29144 | 2024-11-18 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b71a075-64cb-3156-8489-f84080475238 | -3.76135 | -45.94734 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d6c6b4c-c212-3201-b1e9-a48206ebbdfc | -4.78852 | -40.40382 | 2024-11-18 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5f7d8eb3-4593-350c-9d3d-4f06672bbbca | -2.6828 | -46.22452 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e177bbc-200f-3c9b-abfc-a761e2ba4ac6 | -3.30273 | -45.68136 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1b45697a-f810-3074-b887-7af8dff79ca9 | -3.07711 | -48.06605 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c27caf01-167b-37a2-9291-602b6f034ecd | -4.59179 | -44.2299 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bbe3567-fbe8-3943-be13-21dcb577fa53 | -4.81701 | -40.31411 | 2024-11-18 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aef8513e-86d9-357b-8f0c-da149d0ab0be | -4.78615 | -40.40549 | 2024-11-18 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7c572e48-feb7-359d-abd0-be35897f1fc2 | -2.11134 | -46.48637 | 2024-11-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5c5eebf-55fa-3783-aa5f-17ca92d0f398 | -2.16946 | -46.39408 | 2024-11-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb6131ce-9c86-3c71-b5d9-27a9588dee27 | -8.27271 | -45.96389 | 2024-11-18 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58c348cf-f39a-3657-8196-dcbd6fb0f8d7 | -2.50608 | -47.23807 | 2024-11-18 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d2a4389-962d-38b3-8895-b68f2390dbd3 | -3.06116 | -48.00167 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df2619bf-ca8f-301a-8e7b-e85a23036ba1 | -3.19038 | -45.44654 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fb6c6fa-05de-3d03-8fd9-c7a12aa16d73 | -2.46315 | -45.61724 | 2024-11-18 03:46:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99765ee0-18c6-30d1-9df0-4666fcbc5e90 | -2.10802 | -46.43237 | 2024-11-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 363c4b59-9bac-3c42-8c1c-d4f20e0f0fb3 | -3.30644 | -45.69339 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae1bf4f-69b5-3549-a2be-d97ab347a714 | -3.92074 | -46.52235 | 2024-11-18 03:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aba6fdf-5f91-3af5-9d79-7449b0435d97 | -2.1754 | -46.39518 | 2024-11-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2a53514-81d6-3823-b4c5-da60d3688653 | -4.74266 | -44.91045 | 2024-11-18 03:46:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79ca8530-8dce-34f9-92bc-131f0613361b | -9.29885 | -46.21173 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65993222-6b90-366c-bb7b-8d626f80c69a | -3.06036 | -48.0016 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8450fcaf-bb7f-36be-9325-2b8311da3c70 | -3.22969 | -45.54964 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40c71bc0-7092-3f87-a0a3-250c1ea07357 | -3.05471 | -48.00029 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f18d98d2-aa59-3d57-b1f0-a640bc7fe3be | -1.70965 | -45.83124 | 2024-11-18 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 24709e44-ff73-3fe7-80f0-4da511c61d4f | -7.71877 | -45.66323 | 2024-11-18 03:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 752b1a1f-314b-3392-8b7f-7b7a059d30f3 | -4.90794 | -44.02276 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0239588d-a693-37b4-b07a-f3b32bcae89f | -3.76761 | -45.94456 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4af98a42-5277-3d22-a324-c0c3ce11f681 | -3.95079 | -46.41654 | 2024-11-18 03:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90f8f9dc-065d-3e88-8b21-0cf4ec86dd59 | -3.07592 | -48.06572 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3608682-fdd7-350c-a75f-67bc0d60924e | -8.27856 | -45.96144 | 2024-11-18 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c0096f6-4d48-33bb-a938-92514f546021 | -3.06027 | -48.00695 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8480b7b5-2ff7-3bac-ad36-731c00f04b01 | -3.57479 | -45.20894 | 2024-11-18 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee36eb22-7fd5-3c4c-a7c7-1ad6bda5ce81 | -8.2733 | -45.96066 | 2024-11-18 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52ef1db6-5fc4-3746-a3a7-54e02244ef90 | -3.14466 | -45.34946 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 549a412d-72d8-3db1-b434-4580ca53d1db | -4.90703 | -44.02819 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| db089522-22ce-3324-9c07-dfce90cbb69f | -3.33027 | -46.01357 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dae58e5-97de-3eb4-82eb-18ee5747d009 | -4.82004 | -40.31945 | 2024-11-18 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c772ef1-c73a-347f-84cb-60ba4e945362 | -3.14991 | -45.98934 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 144089fb-c641-3724-9488-195b92f29560 | -3.31203 | -45.69432 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e7db919-b520-3c5a-92d9-1f647f12b1bd | -2.67697 | -46.22348 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed85edac-ac8a-3579-931b-27046dbf9b41 | -2.54866 | -47.29105 | 2024-11-18 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34c129f0-13f3-33e5-9eea-6a352d9efe56 | -3.05943 | -48.00686 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 248b10d6-6de5-39c7-ab5b-d07598f17166 | -3.18531 | -45.4445 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 297ac1bc-e7d4-34cb-9820-c8cf2f5a7c32 | -3.17161 | -46.59884 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd2a8029-2235-398f-a925-35bf33353aad | -3.16493 | -46.6022 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7331cf54-ad91-3716-87a3-19830463ab49 | -3.7643 | -45.9471 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9de44312-b0af-346d-909e-6f563ad0d2b4 | -11.82086 | -47.06832 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07ab45f2-f7f4-3536-82a5-84d24f0aec49 | -6.49034 | -47.49924 | 2024-11-18 03:49:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14f1d012-4758-3329-a44e-0249d382ccc9 | -5.24103 | -44.75304 | 2024-11-18 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8db655f9-cd69-3357-a571-99275227143e | -7.66358 | -39.29459 | 2024-11-18 03:49:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e2ff067-d0ba-3cee-8f69-e402a9a6e357 | -11.81494 | -47.07049 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 247c15f9-aca8-3ff9-b7f4-77945cda8594 | -5.24447 | -44.75132 | 2024-11-18 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfa30ca4-178c-34db-bb87-28151ea5c4aa | -6.86366 | -38.8825 | 2024-11-18 03:49:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 90a48181-9e26-3c72-997e-2d9f2b6f4fa2 | -11.96634 | -44.23074 | 2024-11-18 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c17b4556-385d-30ec-bbd5-465eb12f04f0 | -12.46043 | -45.35365 | 2024-11-18 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae9fef23-30c7-332f-8295-22313b80747f | -7.09999 | -39.2997 | 2024-11-18 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b781105d-6e71-3d54-ad63-fcd8d46c9334 | -6.86651 | -38.8869 | 2024-11-18 03:49:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c1620fcc-5b11-3fb1-b23c-667f51462f59 | -11.81765 | -47.06779 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1630fad-de39-3150-bc6f-aa0edcd0331f | -7.6642 | -39.29073 | 2024-11-18 03:49:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24cf8e79-4217-3da3-91f8-5036ca9dde1a | -5.24663 | -44.75086 | 2024-11-18 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ff79b2b-035b-3f75-b5a9-888e50a24e1a | -6.86427 | -38.87872 | 2024-11-18 03:49:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b5eabf41-5554-38b9-923b-9813f5405c3d | -6.3748 | -41.54726 | 2024-11-18 03:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 58e22136-6607-3309-a0c2-a596fa6db7b2 | -7.0923 | -39.25825 | 2024-11-18 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7f2fcdc2-d526-3064-a045-4db69e1bd45c | -5.24397 | -44.75419 | 2024-11-18 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 648b9486-dcf5-3c50-b4c2-fd23ef2649b5 | -12.01401 | -43.00701 | 2024-11-18 03:49:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ca53ce6e-7c07-38ff-98e8-6ec760edb781 | -7.40149 | -42.76826 | 2024-11-18 03:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6fb8e1ca-c267-36ce-81a5-cf24e08befb5 | -11.8531 | -46.93086 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b4e6dc6-8d48-3f1a-a6d4-b9dd044c1e97 | -7.5388 | -35.31363 | 2024-11-18 03:49:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 35d73418-0679-330e-bd90-ddec58c10350 | -6.36673 | -41.54618 | 2024-11-18 03:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46f72193-a48e-384d-afd8-6d8d6aa58d3c | -11.83278 | -47.09172 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e427397a-3632-36c2-a9cf-8edf61bf9ee0 | -11.85292 | -46.93764 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3b4b5d9-a26b-3dcb-bdbd-2f3e41f81a17 | -5.95474 | -48.06704 | 2024-11-18 03:49:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec616e08-ca13-33e0-ab9a-4574fb7af126 | -7.16309 | -35.14756 | 2024-11-18 03:49:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 258ca9b2-083d-3455-b2d4-7121b82a483e | -7.30299 | -35.19188 | 2024-11-18 03:49:00 | NPP-375D | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b190b8c-f98c-3182-b021-be9ca5187902 | -6.49241 | -47.50217 | 2024-11-18 03:49:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4805ddd7-7fbf-3d2f-a875-d8b392cd931a | -12.83061 | -43.1972 | 2024-11-18 03:49:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc2a1930-e0e2-3a8b-ac5a-baf9bc0aa86a | -7.09648 | -39.29913 | 2024-11-18 03:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9593376f-1c7c-3470-a1ea-7a08e7bfb01e | -7.39788 | -42.76357 | 2024-11-18 03:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b06d7e65-b7ac-34f3-8f2a-c3dbf147b950 | -13.43475 | -43.02802 | 2024-11-18 03:49:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c523be84-c322-3f76-aefa-d57e461d7b02 | -7.13124 | -46.63766 | 2024-11-18 03:49:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 420bf866-f5f5-3845-9960-331b07b93ee5 | -11.8387 | -47.08955 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c4ca128-07fb-3308-9c9a-938068af328d | -6.31549 | -39.48579 | 2024-11-18 03:49:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 254e8a02-1454-3276-8e57-4fe0aab3650c | -5.95379 | -48.07223 | 2024-11-18 03:49:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e0c261b-600c-3224-8fea-63b9fafaffa7 | -13.42563 | -42.02151 | 2024-11-18 03:49:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 53256f24-c17d-389b-913e-d5c47118aaf9 | -5.32986 | -44.93667 | 2024-11-18 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a24f3408-e430-3446-92ba-4c32ecb96302 | -6.98612 | -39.66253 | 2024-11-18 03:49:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3d9dc201-1567-33d5-af10-1914b74e8209 | -12.45785 | -45.35621 | 2024-11-18 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a524b981-8e29-348c-8c7b-07239e7c6e15 | -11.85414 | -46.93111 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 500d4707-2353-3a79-b5f2-b9d4b2aed537 | -6.37883 | -41.54784 | 2024-11-18 03:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8a1e939-2d4f-3d98-b4c8-8014fd121e3f | -11.83805 | -47.0929 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2a64c3f-60b9-3cdf-808d-c80cce01fabb | -5.23884 | -44.75357 | 2024-11-18 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdf60ccc-3392-31ca-a427-ccdf3c112e81 | -11.93571 | -44.55238 | 2024-11-18 03:49:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 468d582c-a111-3c58-bf26-6ab242734be7 | -6.37077 | -41.5467 | 2024-11-18 03:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8b6f392-e62d-3577-8dff-1ac4ad95992c | -7.74494 | -37.78852 | 2024-11-18 03:49:00 | NPP-375D | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d4fe5d21-4b47-335e-9092-1704b2afe398 | -11.85246 | -46.9341 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9250665f-a41c-3239-84dd-2f09f2c0d806 | -11.82229 | -47.07228 | 2024-11-18 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc9ec341-a1a6-372e-ad3e-0ad23da6c6b7 | -6.40041 | -44.73959 | 2024-11-18 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README17.md)
