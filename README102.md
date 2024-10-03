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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd642d6e-2ab1-3c1f-ac10-5b8d02056865 | -19.269 | -43.78273 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3a65a94-1588-3f56-9ef9-d713f269a6de | -19.26588 | -43.77444 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdcdfa1c-2ebd-35aa-9a25-7f88b3c18430 | -19.26539 | -43.77836 | 2024-10-03 04:29:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62e14de3-4b17-3904-aabc-d5a6f8c38e7e | -19.25915 | -43.76173 | 2024-10-03 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8470aa3b-4928-34b4-9f7d-fa8aeed96ef3 | -19.25867 | -43.76555 | 2024-10-03 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f72cd37f-4aae-3913-b39e-7673257102e3 | -19.25023 | -43.37625 | 2024-10-03 04:29:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dc9dcdf-f6c9-3618-bf6b-6f83ec136c39 | -19.24599 | -43.37611 | 2024-10-03 04:29:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 098b4e28-19ca-3f8f-9ebd-ba4de2a213b9 | -19.24548 | -43.38015 | 2024-10-03 04:29:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08c66ce2-c7f9-312a-8bf4-cb7919fbab08 | -19.245 | -43.38403 | 2024-10-03 04:29:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 98467c21-1d20-3863-a1d5-73a45fad8559 | -19.24233 | -43.37128 | 2024-10-03 04:29:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 950458a3-edc2-368e-94fe-a84e883e731e | -19.19513 | -43.71318 | 2024-10-03 04:29:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1df6a6f1-c6ee-3dc7-a68a-a7d1bb3930cc | -20.06796 | -44.59746 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5d51f5f-f254-3f73-b961-3f26c2ac41aa | -19.96366 | -44.69202 | 2024-10-03 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f71c119a-28ce-361e-88c8-4421655c6468 | -19.45959 | -44.73159 | 2024-10-03 04:29:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c90c2eff-299f-3856-a7cf-dc0e44815cbe | -20.07256 | -44.59286 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6e4bc14d-3bcd-3a6f-954a-697ee252fb8b | -20.02103 | -44.52642 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85a88262-182c-3229-ba3e-e4d539630327 | -20.02034 | -44.53187 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 70e0996e-b72a-36ec-89e3-7a0a981f6cc0 | -20.01916 | -44.50938 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ba78285a-81b0-3bfb-9b58-37fbb85404cc | -20.01847 | -44.51485 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0f82248a-6b25-3c89-b90c-cf49801c404f | -20.0152 | -44.50898 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e033b541-5ec8-330c-b6c9-d68c8c3cab80 | -20.01451 | -44.51448 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aa9386ff-dcbc-37eb-9a3f-7a664da5d6ea | -20.01193 | -44.50306 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e002e10b-d7bb-3bf6-adf5-ee96975a77c6 | -20.01124 | -44.50856 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c9793811-18d4-325c-bea9-87816817bc32 | -20.01055 | -44.51407 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| aa980619-7c14-3070-89f5-6d77e889d2ef | -20.0088 | -44.50144 | 2024-10-03 04:29:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fef65065-feaf-38f2-8e75-91f541388b69 | -20.00798 | -44.50255 | 2024-10-03 04:29:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| df1a32ed-9c5d-316c-8e04-5ffa7f1dfdfc | -20.00735 | -44.51247 | 2024-10-03 04:29:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 607bd18f-3b34-3e5a-99f5-d3b3525378fd | -19.81388 | -43.83109 | 2024-10-03 04:29:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b6fd8cd-e526-38a0-b3f3-4da7700215c8 | -19.81341 | -43.83485 | 2024-10-03 04:29:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef22c69b-24a6-3cd6-bd3b-a1655ea02d1d | -19.81293 | -43.8387 | 2024-10-03 04:29:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bafe35ea-de28-306a-b792-795d0c3bc175 | -19.79953 | -43.64091 | 2024-10-03 04:29:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91746473-b474-3d5b-b336-820c85c14823 | -19.79585 | -43.63645 | 2024-10-03 04:29:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e4ac9ec-8c94-3475-aaaa-0a4305ca4ea1 | -19.76822 | -43.63721 | 2024-10-03 04:29:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3a50c4f-75ec-38f2-9f93-1628187fd4f6 | -19.76409 | -43.63654 | 2024-10-03 04:29:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bcbac09-3559-32c2-86fd-5863b332e805 | -19.75592 | -44.25873 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9cad1db0-119c-315f-b301-2a8813ef0cab | -19.75285 | -44.25089 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64acf06b-0e0c-3c5c-9b02-91f627e92112 | -19.75192 | -44.25821 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e52fa568-a4e3-3bee-95f9-76252c017d7c | -19.75134 | -44.26283 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40038e05-454a-36d9-bf5a-ea4399439223 | -19.74793 | -44.25768 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf73c420-32ab-3fe7-a5d5-9dc47ec22ede | -19.74736 | -44.26217 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33bd03a7-95db-3635-9ed3-978a4e19dfc0 | -19.74338 | -44.26151 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f766032f-f4f9-37f5-bc0c-cb40be4e4503 | -19.7427 | -44.26689 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41ecf201-e71d-3711-bcb9-6667e38e9f7d | -19.74087 | -44.24925 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b5a1f1f-f824-39bc-a719-6534039e7d11 | -19.74042 | -44.25285 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf3b0ae0-e4be-3459-b19b-b30928030e98 | -19.73688 | -44.24866 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33348334-19fb-347f-b291-3f7ebb491888 | -19.72204 | -44.15838 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 679e8c6b-9684-312e-bb39-6095c7b37399 | -19.72108 | -44.1658 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8db3b9cd-c2f8-31de-8cf6-adca72fa0e0b | -19.69711 | -43.70116 | 2024-10-03 04:29:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63a817b6-6c48-3052-b950-d5e613e2ad00 | -19.66503 | -44.22114 | 2024-10-03 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 756012ca-75a1-33af-89f0-382b4373194d | -19.52524 | -44.24983 | 2024-10-03 04:29:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85e584fb-a40f-3cd9-afe2-07c8dbd9a387 | -19.52457 | -44.25514 | 2024-10-03 04:29:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8515e42d-6d4a-36cf-9ddf-e8d3f687e3d2 | -20.14648 | -43.85359 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 28be5e4b-0374-3b5f-9103-c6da1e82c876 | -20.14632 | -43.82124 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53edf94b-8d47-3e1e-8345-e816a01029b0 | -20.14581 | -43.82538 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3355d406-e5f7-3dd8-8af8-f03126ad2fb4 | -20.14287 | -43.849 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 417c0149-8d1e-359f-be13-dbed1bfd9cfe | -20.14236 | -43.85305 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ccb9e14d-6185-38f3-83df-fb300adb48d4 | -20.14218 | -43.82081 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| febbadba-45df-35f7-99a3-6d52845248b8 | -20.14188 | -43.85693 | 2024-10-03 04:29:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 09a76912-3acf-3e63-99e5-50ce4a2862c0 | -20.13924 | -43.84449 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 01a0fdbd-d996-37b3-9284-3b73283f5edd | -20.13875 | -43.84847 | 2024-10-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f1544bcc-6616-399d-8e12-ce99a9e2242d | -19.95395 | -44.17019 | 2024-10-03 04:29:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d89a5f25-8f73-3d58-b93c-eda2359d8ea0 | -20.89979 | -43.8197 | 2024-10-03 04:29:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 58bcabca-07bf-3d18-afb6-bae7a48a78fd | -20.65441 | -44.03073 | 2024-10-03 04:29:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f42eaa2a-b252-3ef8-9c36-ba5b2031b4b3 | -20.48949 | -43.79412 | 2024-10-03 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 43610e68-a6d9-36c2-8f84-b05ce097a7d0 | -20.38126 | -43.86547 | 2024-10-03 04:29:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8bde43fe-792a-3af2-a3f0-d43043473e74 | -20.30549 | -44.03881 | 2024-10-03 04:29:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fd968235-cfc0-3852-a56c-142a80c843b0 | -20.30504 | -44.04249 | 2024-10-03 04:29:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 979f326f-ee16-3f5c-af61-2fdf82f091ce | -20.32281 | -44.91413 | 2024-10-03 04:29:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb23f9b6-4e96-31d6-8b53-87f80d45634f | -20.67182 | -44.80918 | 2024-10-03 04:29:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7440cdd4-2ad9-3f4a-931a-29a1a84784f0 | -20.66792 | -44.80856 | 2024-10-03 04:29:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4a157b77-26dd-3856-ab19-29b81c8b5196 | -21.82168 | -44.39985 | 2024-10-03 04:29:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18dcb4b6-0ab6-338b-9613-16e08d8916b4 | -21.49244 | -44.57874 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ab3bc63e-0d25-38e1-8407-3a0248267aab | -21.47831 | -44.56165 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 153c75d1-2ad2-37e8-b783-9464bb25ab57 | -21.46139 | -44.56659 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6bdd0750-3d15-3b0e-a537-eeefba6e8e77 | -21.45857 | -44.58902 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| ffafe5c9-fee3-3a2c-8b40-64a79d077057 | -21.45813 | -44.59249 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 0221383e-fc15-31c8-b16c-91216d578088 | -21.45769 | -44.59598 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 111f13ce-76e5-3806-83de-b3dd27627a6c | -21.45689 | -44.56996 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cc35212a-a35a-3b3c-bf2a-a695fe16aa0a | -21.45547 | -44.58127 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 6293a3a4-e93e-39f5-94c4-83abeb4ee1dc | -21.45505 | -44.58462 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 8933e90d-3b87-36ae-87e3-5c9582e9e508 | -21.45462 | -44.58799 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 6c774067-384a-3034-97d7-35769f381943 | -21.45419 | -44.59145 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| a1f3ebf6-8b3f-3f93-8bdd-c5b82bda9ce6 | -21.45375 | -44.59496 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| d0fe8a0d-ed09-32e1-b107-546ee943597c | -21.45197 | -44.57677 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0de731aa-ffad-3aae-9638-80a14b814b66 | -21.45151 | -44.58041 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 00fb002b-0f66-3b33-9d34-dbe34bca8bd7 | -21.45108 | -44.58382 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| ddadddc7-c14e-3e1f-9065-830c68810463 | -21.45065 | -44.58725 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| a54f4e69-4c0b-3b15-8a33-0f1e5dbf005a | -21.44711 | -44.58299 | 2024-10-03 04:29:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 196bcf8b-1bb3-3981-b45f-cfa99744b3ad | -21.19482 | -44.93641 | 2024-10-03 04:29:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a425f254-ac56-3778-9e5f-f8998a777400 | -21.67446 | -43.95265 | 2024-10-03 04:29:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 703bd036-276d-39d5-a817-fc3585b36540 | -21.65141 | -44.00233 | 2024-10-03 04:29:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2caad6d3-a348-3643-a0b5-e6eae11495a4 | -21.65093 | -44.0063 | 2024-10-03 04:29:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ca914b97-7b64-3614-bb11-6f68e6312956 | -21.56423 | -43.97489 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| eb8af3cb-e104-3fb6-b361-518b3536211c | -21.16861 | -43.77063 | 2024-10-03 04:29:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6b60810-1c61-37dd-bf25-9c612b2b8ceb | -21.16757 | -43.77161 | 2024-10-03 04:29:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce1a7ad4-4487-36bc-9afc-a0bacfbebcba | -21.16442 | -43.77005 | 2024-10-03 04:29:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e5683dd-309c-3b7a-b2e5-9380e26c05af | -16.56318 | -58.23287 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| b766a766-3c9f-3d85-876c-3eeb8a61066f | -16.56247 | -58.23634 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| d0b52eec-8451-312d-a08e-8daaff1c39df | -16.5621 | -58.2653 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 59add9ca-55f1-3d3a-b318-9e0580ec2cf5 | -16.56176 | -58.23982 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |


[Clique aqui para ver as próximas entradas](README103.md)
