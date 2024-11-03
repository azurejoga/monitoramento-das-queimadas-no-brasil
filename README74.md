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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1715f74-315b-3e35-bd9e-2817fe1e20cd | -2.39123 | -47.2404 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33b40cf0-b737-3b9a-9427-eec3c2bb4d0c | -2.38793 | -47.22567 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f543cc7f-d910-3310-bcf0-f199e0011d48 | -2.35854 | -47.18407 | 2024-11-03 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 82aca9e7-53c4-3fa8-99fb-b4c079154ccd | -2.35555 | -47.31008 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 789b2ed8-432f-30e2-b6fe-ac1b9162ac96 | -2.35504 | -47.31336 | 2024-11-03 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d191c6e7-d698-3e90-b3ed-aa773e69e6b9 | -2.22001 | -46.54739 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac55878-832f-37ca-ae47-c71158a86041 | -2.21552 | -46.53917 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9285cb88-b986-367e-a128-31788033392c | -2.21496 | -46.54287 | 2024-11-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80a9674-e989-3ff6-acb8-e7be64207b38 | -3.88433 | -46.90051 | 2024-11-03 05:08:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 045073b3-fdfc-3048-8ab5-2ad98bc9b581 | -3.87154 | -47.10138 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a817feb7-fea8-33b3-ad89-0de8057f08b8 | -3.87113 | -47.10015 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 863927c4-ba05-34a7-be5d-8aa8b19f828f | -3.87099 | -47.10501 | 2024-11-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4dabba0-f4d9-3211-a452-9da743f6288a | -3.87062 | -47.10379 | 2024-11-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c17a17b-69f2-356b-bf77-7598dc15bc9f | -3.86599 | -47.10057 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8baaca55-f24c-34d4-989e-e63cd60ebd48 | -3.86545 | -47.10424 | 2024-11-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f69287d1-c55b-3214-821f-83b9f3addd9a | -3.81807 | -46.39116 | 2024-11-03 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9419dfb5-6d0c-3ffb-8a38-43ec41275063 | -3.77732 | -47.05888 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0464bde9-bf43-3476-a64b-d92a1b25a6c9 | -3.77177 | -47.05805 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e00247c3-efbd-33af-b1fc-96b056267681 | -4.33944 | -46.58277 | 2024-11-03 05:08:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6e7c85a7-33c7-3e7f-93ee-ead3467eefad | -4.10057 | -47.02418 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd04e10e-f4cb-3a2e-a8e8-68ba9903be3a | -1.31561 | -47.17891 | 2024-11-03 05:08:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e99e04bd-70a1-36ce-a819-d06240163882 | -4.09683 | -47.02111 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb4b83de-3f3d-3909-a7ee-ee4422d0223c | -4.09629 | -47.0247 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79b4b72c-37aa-3b66-9815-48736d1a42c7 | -4.09495 | -47.02352 | 2024-11-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fa39b06-f99d-319d-9c42-bf8cc470a5ab | -2.08578 | -48.22738 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a640693-fc92-375c-8528-d5f44f7b0715 | -2.04022 | -48.12247 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e4e4c21-597f-337a-a805-a8ce1b8b3989 | -2.03873 | -48.13245 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a5e33ce-4b9d-3905-b339-f2b8e25b9fa9 | -1.86921 | -47.97319 | 2024-11-03 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec3f9970-7456-37af-9323-a402e68d4080 | -1.81677 | -48.0846 | 2024-11-03 05:08:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33043fa4-13b3-3d9a-81b1-3a7b28b36c68 | -1.37529 | -47.69848 | 2024-11-03 05:08:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bc0074c-5d60-3cf5-80e7-12a1c980cf78 | -1.37482 | -47.70152 | 2024-11-03 05:08:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c223f9e5-2c83-39bb-b1df-cc0793092e7a | -1.31653 | -47.18083 | 2024-11-03 05:08:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d481519-3ff0-3a4e-bd9b-ac69c3db1708 | -1.31601 | -47.18413 | 2024-11-03 05:08:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b0153dd-6556-362b-9092-61c4f07a9795 | -1.31512 | -47.18221 | 2024-11-03 05:08:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed129b86-738b-39fa-92fd-b46d3708f4db | -0.88504 | -47.87252 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d8f98a73-5187-3f7f-b745-08b8ae27e8f8 | -0.88413 | -47.8782 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| da2fa892-9997-35bf-b1ba-ad8b67507b68 | -0.88379 | -47.87286 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 2c523572-1b6a-3e97-99bc-3250b1d11c6e | -0.88321 | -47.88397 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 115afd98-dfc5-39b9-8e77-d22db00b012e | -0.88293 | -47.87856 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3577e802-60e3-30e3-8543-51f77db7347a | -0.88002 | -47.87172 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| db4b3937-4bb1-35d9-996a-5bf7b0c3af0d | -0.87911 | -47.8774 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0f6b9695-9c09-33c7-8024-bb09155a50e7 | -0.87877 | -47.87208 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d895dbeb-1364-31ee-a4c5-eb4de8053037 | -0.8782 | -47.88313 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| bd4230e0-bdbf-3473-8afd-356264f6d06c | -0.87791 | -47.87775 | 2024-11-03 05:08:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3deb72f-ef0c-373d-85ae-2445855972e7 | -2.07024 | -48.4997 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4c20e47a-6e53-32d8-9e1a-348bc976aa38 | -2.06914 | -48.49718 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5a15acd3-bcac-30af-97ba-3e532050b9bd | -1.98918 | -48.78827 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f11ea6f9-634b-3a42-b0df-d7c6adb8a64c | -1.98839 | -48.79339 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 104591d6-9738-3814-af00-7c55e133ed3b | -2.09078 | -48.2281 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f99abf-8ee2-3160-aea7-0fb62ce53cb4 | -2.03958 | -48.12673 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 136a2806-92a8-37ca-bc98-8459063802e2 | -1.91245 | -48.25757 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 16a3f1a7-304e-393b-af56-45144d16171d | -1.83301 | -48.75229 | 2024-11-03 05:08:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad6785bb-1867-31e6-bde0-4c7deb2021e2 | -1.82939 | -48.75047 | 2024-11-03 05:08:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 812250a8-7f6a-3eed-b39e-9197d319fad9 | -1.82179 | -48.0854 | 2024-11-03 05:08:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bc37077-cc2b-3aa5-a940-0fb620c8d367 | -1.82118 | -48.08628 | 2024-11-03 05:08:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36a7b2ed-5313-3a81-96cf-28354c4b899f | -1.81616 | -48.08548 | 2024-11-03 05:08:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f335ce02-c5fa-367c-9341-4381b4687d7a | -1.11102 | -48.08984 | 2024-11-03 05:08:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3b33d5b-989b-31de-af41-0ee433560ac9 | -1.10605 | -48.08908 | 2024-11-03 05:08:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bf38cb7-f12f-3fa0-98d7-8af1cf8e8892 | -3.289 | -47.62983 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bc0c0cc-e2e9-30b3-acde-89e586d3888a | -3.28373 | -47.62886 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fac4de7-aba8-3216-9e1b-0101fb392017 | -2.90743 | -47.54197 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a56442e-d9e1-3f4b-98bb-e38145e08a96 | -2.90695 | -47.54519 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 121887d7-a90c-32a1-8cca-c1fb6d65c073 | -2.90213 | -47.54119 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81a5cdc5-0dc3-3ca4-98d7-a23206b5add9 | -2.90165 | -47.54442 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75257998-34fe-3399-8cf1-6ae1dc890d4e | -2.899 | -47.96294 | 2024-11-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22b5f762-ed8c-3725-a5b9-0379667d7cee | -2.89713 | -47.96227 | 2024-11-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ed168b12-7c8a-3bc0-b4ed-a8b00fc99b12 | -2.89667 | -47.96531 | 2024-11-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 816afac7-290f-344d-8e6c-9d5940850390 | -2.89385 | -47.96215 | 2024-11-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1a0f3680-b249-3b17-bed1-f46bf2c586ab | -2.42338 | -48.18703 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35b3f45a-242d-3bf7-a66e-3b68c5527ab9 | -2.42294 | -48.18987 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97789c35-60f3-31bf-a526-2d3b6926b20c | -2.36744 | -47.47244 | 2024-11-03 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cacd24cd-e647-31f3-8a29-81f19ca87fb2 | -2.36695 | -47.47571 | 2024-11-03 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bee19a1-ff6f-3bcb-af04-4b95b6b0d64a | -2.32122 | -48.19035 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74600445-33fd-381f-9a11-86c308bf2979 | -2.30275 | -48.00704 | 2024-11-03 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f51d436f-7ef2-3755-a89d-ceb46ca29df2 | -2.3023 | -48.01001 | 2024-11-03 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ce8a42-e7e7-31d1-b978-bbd5526f1175 | -2.30185 | -48.01298 | 2024-11-03 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0e0c6ddb-1485-39f5-8cdc-26c560b1e598 | -2.2972 | -48.00932 | 2024-11-03 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 220dc05f-8b7c-3240-8262-a3a88ca36c04 | -2.29675 | -48.01227 | 2024-11-03 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 69970e16-3d7c-3e98-b857-56a991c34752 | -2.54892 | -48.69951 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6091565b-487d-39ff-aa39-4e807e302b9a | -2.54324 | -48.70409 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1402b84a-8b13-3885-982d-28155da5e182 | -2.49292 | -48.46621 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cddb7013-bb6c-329b-8972-32cc10c9378a | -2.48833 | -48.46774 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 280094be-5be4-30d5-8d30-58cb8182aacc | -2.48798 | -48.46544 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c21071-c4ab-3f50-8e19-6e9cef812a57 | -2.48713 | -48.47095 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1f7e607-129d-3f64-8481-3f7e2e80efcf | -2.47864 | -48.53394 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81740c6c-4e32-3df3-9843-99679c08e405 | -2.47784 | -48.53938 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| faac902e-76c5-329e-b38b-3201af79c72b | -2.47778 | -48.53151 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b6be1b67-ca68-39d3-953d-b0bd278a469e | -2.47694 | -48.53694 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 39954f31-2978-3197-bbb8-31412390eb91 | -2.4761 | -48.54239 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cb45c9ed-fda9-3e69-8a20-6ef94f8c6635 | -2.47371 | -48.52527 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7019323-5aaa-382c-9529-f6ea85b9f4af | -2.47287 | -48.53071 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 74d9ca77-f969-33ef-8e2e-31ce14c5f1cd | -2.47203 | -48.53616 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ef34be6a-623a-3e8d-ba73-87e578dbcc7d | -2.47118 | -48.54165 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7eef63cc-1e2c-36b8-a0a0-b7f70ebfa617 | -2.46878 | -48.52457 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be1bb08a-0280-3c26-9598-5ec3f91ad42c | -2.46795 | -48.52994 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 25005134-8694-3419-9a77-2ca8bfd27a8f | -2.46711 | -48.5354 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d02632fc-2761-3b80-8eba-40c63153308e | -2.46677 | -48.40536 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ac0588c-21e7-3463-8565-f0211f6e1dc2 | -2.46626 | -48.54095 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e2b29efb-1e3f-31b7-9eb6-524e56441902 | -2.2916 | -48.45158 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc864c0b-38d6-3f59-a249-16616a473c66 | -2.29079 | -48.45709 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README75.md)
