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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c989f921-9bc3-396a-b961-1d3f0432537a | -18.04381 | -44.38735 | 2024-09-27 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14796977-d082-3327-86ab-b91c7c537961 | -18.04264 | -44.38671 | 2024-09-27 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef707468-5a79-35ac-b05d-8aae7ceba076 | -18.0097 | -44.33868 | 2024-09-27 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96542229-f8e8-3d5c-8af1-e0032777427a | -18.00494 | -44.33813 | 2024-09-27 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c1a4e9e8-0671-369a-90a4-e02de4ea10f2 | -18.00435 | -44.34321 | 2024-09-27 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e0bf1e9e-275e-35b8-8012-1d6d62b7324e | -18.70514 | -43.29392 | 2024-09-27 04:42:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 46d3cef9-bb6e-3878-9aef-639995056eac | -18.70313 | -43.29271 | 2024-09-27 04:42:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 691fdac7-9f6a-31d2-8f7c-b906a60460cb | -18.70278 | -43.29587 | 2024-09-27 04:42:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 575b1798-bf19-3e2f-823d-28de7f6ba204 | -18.60695 | -43.41315 | 2024-09-27 04:42:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f86706c-033e-39eb-b1ec-b24807eef1eb | -19.10124 | -43.4568 | 2024-09-27 04:42:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cb18ace4-6d34-3f02-ac32-4523f0b7b5b7 | -19.10089 | -43.46002 | 2024-09-27 04:42:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 948a27ca-c36d-3be1-aa5e-5db90a86b5a4 | -19.09549 | -43.46194 | 2024-09-27 04:42:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3138eaf-f095-319d-85a6-a4388e93c479 | -19.81827 | -44.05848 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6398769-04a0-392a-862a-0568c3009598 | -19.81705 | -44.05869 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60872468-a5b8-3250-b60e-6457fed214d7 | -19.81329 | -44.05799 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2bf29b0-cadf-33a3-87c8-3dbec1adbf3e | -19.75616 | -43.68174 | 2024-09-27 04:42:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0f0dd61-f88b-3ab1-a06c-1eee6f61e66b | -19.6462 | -44.18473 | 2024-09-27 04:42:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82ca55be-f0f0-39ee-a867-ba695fb6c522 | -19.64553 | -44.19075 | 2024-09-27 04:42:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 179ed8cb-1587-3380-9df5-52d7e42a5869 | -19.64452 | -44.15483 | 2024-09-27 04:42:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f1f4395-c9a4-3cab-b81e-aba15f5f65a5 | -20.19184 | -44.32756 | 2024-09-27 04:42:00 | NOAA-21 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d19589d2-57ac-3088-a4ef-fa68e634680b | -20.19121 | -44.33366 | 2024-09-27 04:42:00 | NOAA-21 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3b602a2b-2d42-370e-8418-4abc92b167c9 | -20.18932 | -44.32722 | 2024-09-27 04:42:00 | NOAA-21 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7fe4b94a-02e5-30fe-95f2-6e87e329ce17 | -20.18865 | -44.33331 | 2024-09-27 04:42:00 | NOAA-21 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f042dc3-a3eb-3b48-a925-f151da614724 | -20.18612 | -43.54361 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 362ab311-6f44-36d8-ae0f-060c371d8a82 | -20.1858 | -43.52813 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 134cd25d-1c5f-352c-92c6-e96da88197a9 | -20.18578 | -43.54707 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d09d27e6-c94e-3fc2-8a38-a90959be1819 | -20.18509 | -43.53472 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 78f17f80-7704-3f52-88c0-e4fb094b2252 | -20.18449 | -43.5402 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aa137e46-5f79-35f8-a497-c5e25d308921 | -20.18258 | -43.52657 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e0c3ae8-2a93-304d-9c35-ea2dc4cd1e70 | -20.18201 | -43.53241 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8b185d4b-c77a-3820-bfa1-99455640c6c6 | -20.17819 | -43.5181 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 43851b3a-2f96-331b-bf56-22e3ac5a131a | -20.17779 | -43.52213 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 3689cb05-1a92-337a-bd7c-0c8eb216eeda | -20.17631 | -43.51909 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 5eb584e3-2364-35b4-97c0-822d85be84ca | -20.17584 | -43.52343 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 528df660-292b-326c-ae76-8ed403fc52e9 | -20.17532 | -43.52834 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3853e76f-50ce-3dcd-bb87-74ad27e58f6b | -20.17296 | -43.51819 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 3cac4c03-6e36-3bb1-8642-0f4a29d42c64 | -20.17251 | -43.52279 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| aaa233aa-ad36-3d65-a9da-4e46716b5f4c | -20.17201 | -43.52785 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| ffc9bd2d-ca4c-3118-8c10-2c47472ddef9 | -20.17144 | -43.53379 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| c234b771-e131-3f38-8300-f4ecebbb9c66 | -20.17105 | -43.51933 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| fc79070f-347f-35c6-acac-5dd240e9262c | -20.17054 | -43.52416 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| bc3294ba-4ffe-3047-adb5-d28e19b2f071 | -20.17 | -43.52922 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ed34e6ce-da9e-395a-a091-c1994dcc5877 | -20.16624 | -43.51542 | 2024-09-27 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c38707a6-fb77-3b7c-9329-c18a0a14cd5f | -20.16581 | -43.51941 | 2024-09-27 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1bae9412-c333-3102-bbb7-4417187057d4 | -20.16156 | -43.5592 | 2024-09-27 04:42:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d98a856f-52ba-3f03-aed3-3652b68d4f18 | -20.15923 | -44.32985 | 2024-09-27 04:42:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a2920357-21f6-3d3e-95ce-51fbd7a352e9 | -20.1586 | -44.33563 | 2024-09-27 04:42:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| afd9c4b3-7518-31fb-86ab-66ee4f1780f8 | -20.15676 | -43.5553 | 2024-09-27 04:42:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b47ce1ad-c00e-3b85-aa1a-8ce3d2758f15 | -20.15648 | -43.55796 | 2024-09-27 04:42:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2bec01bd-b7aa-3f65-bbf8-29968093a47b | -20.1562 | -43.56054 | 2024-09-27 04:42:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 16e6ebf4-5630-3bf7-b224-afa9bc709343 | -20.15586 | -43.51455 | 2024-09-27 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f58ccc91-ddbb-3033-94ea-a5857afdc1ce | -20.1543 | -44.32953 | 2024-09-27 04:42:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f6d645ac-92c1-3266-a27d-ca271391b930 | -20.15304 | -44.34106 | 2024-09-27 04:42:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 85a1a348-eaa1-3ae2-a5c9-bd79c9b063e1 | -20.15068 | -43.5141 | 2024-09-27 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4338603b-2a5f-3536-acd9-19534af41af7 | -20.15028 | -43.51794 | 2024-09-27 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 150dcafd-6607-3abf-899a-5480971df6ed | -20.14983 | -43.52218 | 2024-09-27 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| eaf729d0-fbb0-3add-806c-619b0ad713de | -20.14939 | -44.32904 | 2024-09-27 04:42:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b97c2c8c-e4d2-3c7a-9b93-dccd1514584a | -20.13044 | -44.27428 | 2024-09-27 04:42:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 42c38a5b-0011-31cb-9bbe-a014d8820b25 | -20.12481 | -44.28042 | 2024-09-27 04:42:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6fbb6fb9-26cf-39fe-abb4-1c057ef6d8c9 | -20.09585 | -43.83568 | 2024-09-27 04:42:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e0e6e5d5-f512-3c76-a438-dd80f1f81982 | -20.09551 | -43.83892 | 2024-09-27 04:42:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e968eb6-8596-3127-bcf4-b8c84aba4848 | -19.98088 | -44.14504 | 2024-09-27 04:42:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bf81739c-af04-3641-bb4e-1583eeed5adf | -19.94746 | -43.79338 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3851fdd7-d4bc-3396-bad2-070a8f26c869 | -19.94714 | -43.79647 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7eb7aa4c-c8a9-35d9-92fa-d4619a20eb25 | -19.94685 | -43.79933 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 42f4d61c-4c78-3469-a31d-802b21b1fc6f | -19.94655 | -43.80216 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 711a5045-f123-3f95-9635-a3e44f2e1aa7 | -19.94279 | -43.79926 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 27b7c806-d1c8-329d-a620-27208d76f5fa | -19.94248 | -43.80209 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8f5fabe3-0c6f-3c2e-be01-f72f87a7f179 | -19.94177 | -43.79884 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 63929ab3-119d-3a35-be94-ae9ba17771d0 | -19.92729 | -43.80038 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 261c6f00-91ec-3ccd-a082-a479607485ae | -19.92698 | -43.8032 | 2024-09-27 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 17a740a6-f63d-393b-bf32-964ce5edba58 | -14.79426 | -44.17449 | 2024-09-27 04:42:00 | NOAA-21 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61ddb56b-af55-320a-b366-ee8a70684769 | -15.9146 | -44.99462 | 2024-09-27 04:42:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d89611a-f81b-373e-a230-60afd6740ee6 | -16.32212 | -45.67513 | 2024-09-27 04:42:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49be8d53-4eae-315b-993e-e9d29f6e539f | -16.88966 | -45.32843 | 2024-09-27 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3e7d72cd-6eec-3946-853a-bc53753951c6 | -16.88528 | -45.32781 | 2024-09-27 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a95d1d12-540d-3463-b773-96f04e63bc16 | -16.85268 | -44.35911 | 2024-09-27 04:42:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30ae2588-f795-3854-869f-4c3cc39d6eee | -16.84801 | -44.35843 | 2024-09-27 04:42:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ef9cb35-439d-3050-9b8d-002485e1ff29 | -18.93307 | -46.30738 | 2024-09-27 04:42:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 908ea6d5-e2ba-3154-ad20-d6ec421288d9 | -19.89659 | -46.48197 | 2024-09-27 04:42:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be00cd94-a72e-3cf6-8760-81cff09d139b | -19.89608 | -46.48613 | 2024-09-27 04:42:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0616eae1-39ea-391c-bba1-f335c653bd84 | -19.89184 | -46.4856 | 2024-09-27 04:42:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eddbd32-1504-3b49-8b10-72134d00fe52 | -19.62097 | -45.87155 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32232cd3-3aad-3b64-92be-f0f7681ab71b | -19.6204 | -45.8764 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 43f82ba1-dffc-3429-aff0-f6f37b538b5e | -19.61987 | -45.88098 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 84072ffd-d62b-3aa4-a229-dbc33fba6535 | -19.61659 | -45.87086 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13273539-b695-37c9-a520-46c1a8669858 | -19.61603 | -45.87564 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cadcd61c-324d-3c25-a975-9c7490c41b2a | -19.61549 | -45.88025 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e14243b7-c6aa-39fb-8d87-3f7b3cb3d2ef | -19.61166 | -45.87488 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30ad5e6e-3e4b-39ec-961e-d88c8657cfb3 | -19.61112 | -45.87948 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07b32cbb-98f5-3132-a70b-348561edac28 | -19.61062 | -45.88375 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4587854c-fdf8-3e5b-a5d5-b8b09f16cb5c | -19.60727 | -45.87421 | 2024-09-27 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cfc9b280-cc44-3610-9e1a-5ccc86efe239 | -19.58381 | -46.11251 | 2024-09-27 04:42:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eaa5819e-7cfc-332c-8d82-5440bbb9afc1 | -19.5833 | -46.11691 | 2024-09-27 04:42:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e571d3f0-6bdc-3b88-8776-091edd8f207c | -19.58002 | -46.10746 | 2024-09-27 04:42:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a529f35d-663f-3006-a69a-60da0856472c | -19.57951 | -46.11178 | 2024-09-27 04:42:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 095af51f-7c37-3407-9fde-0a8fe015c342 | -14.72812 | -45.511 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aea69beb-7da0-3563-935b-1046cf56c485 | -14.72761 | -45.51497 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7a829dd9-473d-3bc8-93a7-d524c0e86588 | -14.72444 | -45.50632 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a4c2899-e765-3418-9b58-dc86f7cd3c09 | -14.72393 | -45.5103 | 2024-09-27 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README102.md)
