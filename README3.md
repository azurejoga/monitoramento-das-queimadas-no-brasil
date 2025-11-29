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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f22b2b54-7996-39d0-9597-85d54fa32f02 | -2.6019 | -47.3465 | 2025-11-29 00:24:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb923b20-7588-359d-a2c8-021db0e0cb7c | -9.8786 | -47.456799 | 2025-11-29 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64b7a4ca-4528-3704-a55b-c156dad7d9c7 | -3.174 | -45.6082 | 2025-11-29 00:24:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de47747c-cb49-36bf-b0e4-5e294a2c0924 | -5.0716 | -40.812099 | 2025-11-29 00:24:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2bf96742-44b1-3164-b259-24a97f9cff6e | -3.2379 | -47.243 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4940255e-2c6f-3a99-bcd1-4fe23ce765aa | -3.5661 | -50.2897 | 2025-11-29 00:24:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 363d163f-fc6b-38cd-b43b-70ec43bbd3cb | -6.4633 | -41.725101 | 2025-11-29 00:24:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6296eb92-22a2-3062-9bff-ca75162a9bb0 | -4.1707 | -43.753201 | 2025-11-29 00:24:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1ce6d1f-4847-3d28-9434-07b25b007a74 | -6.2365 | -40.289001 | 2025-11-29 00:24:00 | METOP-C | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| feb95071-274b-3b7c-a010-287b8ac22b3b | -2.9275 | -45.297901 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91d2b787-44df-33c7-a08e-88ae9e29a1f0 | -8.0319 | -43.1371 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 353088ff-202c-35e5-a974-8491a3a7d5d3 | -8.0515 | -43.132599 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50605a2e-c4bc-30d7-b4cd-91e681f3f3a9 | -22.077999 | -46.820702 | 2025-11-29 00:24:00 | METOP-C | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 83f360c4-6db8-38be-9ae5-265536dded01 | -1.4901 | -47.804199 | 2025-11-29 00:24:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dcd2a05-07c9-373c-8516-49c5e3154d6e | -4.0081 | -49.100899 | 2025-11-29 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfcb050e-bf0d-31f5-924f-a897261412ad | -4.2944 | -44.557499 | 2025-11-29 00:24:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e06f2e0d-2e0a-3de5-956f-07e07715b06a | -3.5633 | -47.178501 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5aa0322-6fb0-334d-b48f-c4a645b1a7f5 | -4.2532 | -46.360298 | 2025-11-29 00:24:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f0a7029-1f54-3686-8149-dcb47e427071 | -2.6525 | -47.387798 | 2025-11-29 00:24:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 275b5a14-d0b0-36fc-a731-8c77b0584c77 | -2.9802 | -45.5728 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96bf80c8-fe99-34b6-8fa7-04369739dabf | -4.9543 | -41.1889 | 2025-11-29 00:24:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 143ad9e6-3c87-36d4-9e0c-8e70934ed75a | -6.2486 | -40.296799 | 2025-11-29 00:24:00 | METOP-C | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 74a4f512-ba63-3cb1-acf5-ecab7603fd33 | -2.9671 | -45.245998 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af84ec07-d0c8-3451-8ba3-8a35fa0d280e | -3.1771 | -45.621799 | 2025-11-29 00:24:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89f9c5ef-bac2-3bc2-bbcd-84b5961e1ad8 | -8.0434 | -43.141998 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40de5368-8587-3f6c-ab3a-ff2db6e12fb5 | -20.184401 | -52.377899 | 2025-11-29 00:24:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed8d3ff-0416-3f72-933d-99ed926144f8 | -6.7109 | -40.8078 | 2025-11-29 00:24:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7188245f-6dff-35e7-b756-199bca9add6d | -3.8972 | -40.771702 | 2025-11-29 00:24:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6af3b32d-c8b0-35f9-ae73-1502cede7157 | -20.1747 | -52.379601 | 2025-11-29 00:24:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4a7357d2-df6f-3539-9fa9-200fe8b086e1 | -3.8948 | -40.7616 | 2025-11-29 00:24:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2050071c-a976-3c27-b009-2088291069e4 | -20.1707 | -52.354801 | 2025-11-29 00:24:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 484080c0-d807-36b1-8244-f8efe439ca3b | -5.3637 | -43.024799 | 2025-11-29 00:24:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 9329f62d-e788-31ed-80ea-c5e4a5609ddb | -3.9789 | -49.016701 | 2025-11-29 00:24:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0fd56e-e3fa-342b-b2ba-9cbc4b9d0e64 | -2.9646 | -45.5047 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff8eac1-751b-30ca-be91-adf6708ef69f | -20.749599 | -47.204201 | 2025-11-29 00:24:00 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e07b8380-e5ea-3ef5-8806-b6cda7f044cb | -3.4678 | -45.900501 | 2025-11-29 00:24:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1686bb16-07d5-37bc-b6c8-6954a5121c1e | -3.3155 | -50.271301 | 2025-11-29 00:24:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181518cf-068f-34cd-94b9-b8c5c960f481 | -3.248 | -43.599899 | 2025-11-29 00:24:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a2856a6-39c6-39d8-9968-74ef97749436 | -2.9965 | -45.4188 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30dc814c-8189-3871-841b-eec68066a6f1 | -8.216 | -41.190201 | 2025-11-29 00:24:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88ef4445-dc2e-34ed-9ad0-c503acec6514 | -9.7434 | -36.254101 | 2025-11-29 00:24:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 461f2785-5d0c-3b33-a193-7785847d7cf0 | -2.7724 | -45.476101 | 2025-11-29 00:24:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17d7393d-99b6-3334-b189-ee38d71a1842 | -2.634 | -48.529301 | 2025-11-29 00:24:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 167d8762-d72f-3834-8589-faf2030da89a | -17.613501 | -46.6703 | 2025-11-29 00:24:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1c22dc-d2a1-3bb9-bd2c-4bd25f10f3ea | -5.1118 | -40.7206 | 2025-11-29 00:24:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8526fcec-eb36-3112-9a60-b8709ac5f073 | -20.4401 | -47.501099 | 2025-11-29 00:24:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f3b3d40c-84b0-3427-b373-28ec4ec18e11 | -9.3194 | -43.0807 | 2025-11-29 00:24:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef9786ff-dc6d-31f1-8b59-00b0d0d23b29 | -8.0417 | -43.134899 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b113dc41-a964-3628-b49c-db7996bee42f | -6.6014 | -43.6894 | 2025-11-29 00:24:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3fcf2d3-9693-3b07-bbbd-84e9083d8bfb | -2.6509 | -47.3806 | 2025-11-29 00:24:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f1a6a46-fdfa-31ab-a8a7-ef502933f67d | -6.5997 | -43.682301 | 2025-11-29 00:24:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50373591-8324-3bd2-a8a5-0158384ffb0a | -8.1694 | -43.1959 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f8494f7-7bef-38cb-8eb4-e2b05c044288 | -3.8831 | -42.293701 | 2025-11-29 00:24:00 | METOP-C | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20798932-166e-3c44-a003-16635dd323bf | -3.8924 | -40.751499 | 2025-11-29 00:24:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 80c997f7-9f4b-3bb7-ae71-1dc3e3e2c440 | -2.7226 | -45.214298 | 2025-11-29 00:24:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 371d25a8-da7c-368f-9b78-23f595705c46 | -2.8425 | -45.782398 | 2025-11-29 00:24:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 825d9fe5-6b1f-3fcd-b2c1-946788deb30e | -3.5869 | -40.854099 | 2025-11-29 00:24:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d696f42b-ea77-39c4-b9ec-b7db65d674ba | -6.6387 | -43.137501 | 2025-11-29 00:24:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 405c6499-58ce-3ca5-a56c-c68d1aa96105 | -6.5229 | -38.863701 | 2025-11-29 00:24:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 611a12cb-b5dc-370f-a587-5b66620eea55 | -2.9688 | -45.568199 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a65b227-4037-35ef-9daf-6f019cdd43fd | -4.9296 | -43.466301 | 2025-11-29 00:24:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81d4a02b-5c22-3437-a017-399e838c642a | -6.5258 | -38.875999 | 2025-11-29 00:24:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 01b2c5ae-4bbd-346e-b30a-dbbc9ce051d8 | -2.9149 | -45.243198 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce3b0d41-39a2-3749-8f37-26a6b3a451d4 | -6.2389 | -40.299099 | 2025-11-29 00:24:00 | METOP-C | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 380e4d07-8abe-3d8a-9e08-fb2c1a6bf98b | -5.9239 | -43.392799 | 2025-11-29 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| db13d7dd-b1fc-3999-bc8f-82877c98cc43 | -3.885 | -42.302101 | 2025-11-29 00:24:00 | METOP-C | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3bc8fef-9547-3fd1-8f90-b06d6029dd69 | -20.2087 | -47.5112 | 2025-11-29 00:24:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d78dc769-b7e0-3734-8b8a-999ca5eee6de | -2.3101 | -45.844101 | 2025-11-29 00:24:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 571b9860-56dd-3568-9675-0c03fc7032ef | -2.9655 | -45.239101 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2542e640-96d5-3110-8b70-3caf8cbd1914 | -8.0499 | -43.125401 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3df9fb94-09d0-3287-bc26-274c893bed52 | -8.1661 | -43.181599 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c63b6836-9b8b-3d8b-b062-05545e423a45 | -20.1667 | -52.3302 | 2025-11-29 00:24:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9a6970b9-6612-3ec9-8888-99008abbc952 | -9.9607 | -42.329601 | 2025-11-29 00:24:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d7d151c9-7b53-3e4d-b2b8-8b6ce8f256b0 | -3.3998 | -47.1847 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d52305dd-b96d-3876-a682-6bacffceff95 | -4.114 | -44.8951 | 2025-11-29 00:24:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f02b4db5-cf94-3f10-8693-7cf88604e930 | -3.1385 | -44.376801 | 2025-11-29 00:24:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd3660e-1c05-3587-bc9c-ecaaa936a79b | -8.7968 | -40.419498 | 2025-11-29 00:24:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a5fdc706-3193-39e3-bc31-d96840f9ad67 | -2.3085 | -45.837299 | 2025-11-29 00:24:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 248e8759-f52b-3b7b-8e88-13e506636743 | -20.2132 | -47.535099 | 2025-11-29 00:24:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 54297242-bb30-38c1-9060-f1e5db1853ef | -6.7784 | -41.704201 | 2025-11-29 00:24:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ebe5921e-f40b-3428-9040-e5c2ba0de4a3 | -9.9507 | -44.306301 | 2025-11-29 00:24:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2ad3ccb-4c30-374b-a359-bf9cb781d77c | -1.5524 | -45.194401 | 2025-11-29 00:24:00 | METOP-C | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1be45af5-cadc-3fc6-aed7-d0953d731ba6 | -2.6357 | -48.537201 | 2025-11-29 00:24:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41ba8f10-8d8f-34f1-9c84-3ab6cd8bed21 | -3.4015 | -47.191799 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 027d1d8a-5cf8-3ca0-b221-c4a2727fd879 | -8.027 | -43.115601 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f72f6c39-a5ab-313a-87d1-4d86a53d73c8 | -8.218 | -41.1987 | 2025-11-29 00:24:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e4154e5-7041-3863-b819-51aa83603b64 | -2.5987 | -47.332199 | 2025-11-29 00:24:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf2061b-bec0-3c39-aa05-4156fb3c2b65 | -6.5356 | -38.8736 | 2025-11-29 00:24:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cb8029ab-5fcb-3e82-8a7a-a44e77cf4078 | -8.22 | -41.2071 | 2025-11-29 00:24:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db12bfcf-8f97-3042-8082-03504a46b5df | -6.4301 | -39.504601 | 2025-11-29 00:24:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0a8344da-d3d0-38b1-a0d5-e863d2258aee | -6.2462 | -40.286701 | 2025-11-29 00:24:00 | METOP-C | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 75368556-9122-3714-bd87-a09f223d2110 | -2.9018 | -45.051601 | 2025-11-29 00:24:00 | METOP-C | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 065cec41-7215-3446-b6df-afada2950b9e | -8.799 | -40.4286 | 2025-11-29 00:24:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 53988818-4002-3b47-8ccb-704fb63fa8be | -8.1711 | -43.202999 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b59267ee-0ac0-37db-b349-06a750e83338 | -9.9522 | -44.313202 | 2025-11-29 00:24:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca9d13ad-7715-3f6b-8d8a-655b26ea1cdc | -2.2258 | -47.505001 | 2025-11-29 00:24:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe91337e-7058-374f-919d-c85f3e009bd9 | -3.7583 | -46.948299 | 2025-11-29 00:24:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 266cf38a-8c69-3217-868d-ba819f782946 | -3.5991 | -40.8619 | 2025-11-29 00:24:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 23bad3c5-eb67-3eea-a045-fa08f47346ce | -5.0005 | -38.5313 | 2025-11-29 00:24:00 | METOP-C | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3a138748-5f62-327b-9cb8-8d752315edd8 | -8.0384 | -43.120499 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
