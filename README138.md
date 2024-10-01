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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8609eb0-1182-3922-b7ad-2a90c00e509a | -13.02099 | -51.19576 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 534deda7-0564-3f56-8aaa-7eac7a319a62 | -13.02049 | -51.25758 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a20c432c-0dd2-35ac-bf23-c403cd9afa07 | -13.02049 | -51.19339 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d0c80486-c23d-3d42-8420-359d1301d8aa | -13.0204 | -51.25537 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ca63eea8-1c01-3f6f-9f27-8e4c75143367 | -13.02035 | -51.20132 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e8fe3d44-bf89-345d-a4ae-36b3afc2748f | -13.01989 | -51.19898 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| bc72cc2b-79c6-3748-aecb-2909caf41a51 | -13.01985 | -51.26308 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8d56da0d-bd60-35a3-801b-759a30691c98 | -13.0198 | -51.26088 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| be79805a-9a8b-344b-a8b0-065a8ee346a4 | -13.01971 | -51.20689 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bd702a84-1a79-306d-8315-7191d5ab3e79 | -13.01929 | -51.20455 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c025c07c-b5bf-3bdc-8ad1-8c717b0f85d1 | -13.01922 | -51.2686 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fa73faf4-9e59-3a97-bd96-95ef7f0df6f3 | -13.0192 | -51.26641 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 311b2afe-5260-35eb-b826-eefb07435617 | -13.01911 | -51.32768 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f24211e6-962f-3cc8-8aa4-544f3e274f3d | -13.01907 | -51.21245 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ca396c7a-be1b-3207-be9d-3d8f6cbf58a9 | -13.01869 | -51.21012 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5a01b7cd-2ae2-3aff-b968-ecad85ba3455 | -13.01843 | -51.21802 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 24ca68cb-8c7f-3c83-82aa-e9683726e8a1 | -13.01809 | -51.21569 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ef2fb28c-9901-3c11-859e-f50f6da9f2be | -13.018 | -51.27746 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 41bdadd4-6c78-3978-963a-02be2c8241a6 | -13.01795 | -51.27959 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 23223d82-048c-3ad0-a1ec-2cbc194f6639 | -13.01779 | -51.22358 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 873e8030-188e-33b3-bb32-92733eadad51 | -13.01748 | -51.22126 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ccdf572-c869-3801-b928-51187cdcb65e | -13.0174 | -51.28298 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 7cae6d08-ec40-36c6-9a40-7dc4413dd5ab | -13.01731 | -51.28508 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 6905c1ba-dff4-3de9-9117-3a31cba57d3b | -13.01716 | -51.22912 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1ea966d-8974-394d-a55f-818bf31581f8 | -13.01688 | -51.22682 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 54281a51-12d4-3261-b9ca-c5310cf5b876 | -13.0168 | -51.28848 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 0bb0d94d-e333-3bb8-95c1-42157e114f57 | -13.01668 | -51.29057 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 853cb637-a0e7-383a-a936-6b62212bf6a9 | -13.01652 | -51.23467 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 921b568c-8ac2-33e7-9843-076d893bbf8b | -13.01628 | -51.23238 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2183d970-2606-3e6c-9d1d-2627e30a7dab | -13.01621 | -51.29398 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 262c16e7-07c4-3649-a8a9-cdd6de030d80 | -13.01605 | -51.29605 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 44deaea8-7732-3871-afcb-eb78f851e4b1 | -13.01588 | -51.24022 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2360e3ce-2b07-3f02-8b87-f18c4cca70ed | -13.01568 | -51.23794 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 359d4530-dbcd-3f43-a0f0-8b9f1d547dfd | -13.01561 | -51.29948 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b653c0e8-c856-35a0-9b66-c2ee9e6c6fd1 | -13.01541 | -51.30155 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 24573c71-ceca-3341-b135-0a32f266c981 | -13.01524 | -51.24577 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d4654b55-ff80-37c2-84db-e6e2efc0a98d | -13.01508 | -51.2435 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a90698de-482e-3a3f-8a01-0f1358d83f13 | -13.01501 | -51.30498 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b21575bb-4f00-3cee-a2c6-41ec9256fc51 | -13.01478 | -51.30702 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d6f4b73e-52b1-382a-b3e8-78fa00b60dac | -13.01461 | -51.25129 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 42473b44-353e-3cc8-a0bf-1406e2365fb6 | -13.01448 | -51.24904 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 28ef7cc5-d828-31c7-9d1d-f5f2d40ed976 | -13.01397 | -51.25681 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8a78dc8d-f96d-3531-ac5c-12f346608f0d | -13.01388 | -51.25457 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 14adb4e7-156d-305b-88c3-f33fa5fcda9b | -13.01381 | -51.20056 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dadca826-f415-31f1-b7c1-39f9553ffdba | -13.01334 | -51.26233 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0fb3b02e-0c7e-3995-87f4-8aba084e47d9 | -13.01329 | -51.2601 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 26d6ca72-d94a-3093-a6a7-60d2e2b5edcc | -13.01322 | -51.32144 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5a48ac8-e7c6-32e7-83ab-e37a6b57652a | -13.01317 | -51.20613 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e3b0875e-16d0-38f0-ad4f-8707fec62965 | -13.01288 | -51.32344 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82a64d33-23b9-3c5d-958f-741c1b621299 | -13.01275 | -51.20377 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| abd2b644-f318-3bea-b48b-0e0d59e32ab6 | -13.0127 | -51.26783 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4beba8af-73ca-3a5b-a236-76fd7e85fee9 | -13.01269 | -51.26562 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e18f0bfe-d573-3b02-9358-ea0b6ea195fb | -13.01262 | -51.3269 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec7c88fe-eda5-339c-95c1-0f369463d4f4 | -13.01253 | -51.21169 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7c6d92ca-08ec-3aa4-be25-64046dab3094 | -13.01225 | -51.3289 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0bfabb80-05c7-31de-b237-f5e7ee91816a | -13.01215 | -51.20933 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9f028bc6-8f35-3c22-b2ee-37717334cbd6 | -13.01209 | -51.27114 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d0bc8468-2db8-3b7f-8e81-aba8fd6bfac4 | -13.01207 | -51.27333 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| af153f27-f427-3d8b-985a-bf72d8a5ae05 | -13.0119 | -51.21725 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1d0e8661-fdd0-3868-adce-34508b89e753 | -13.01155 | -51.2149 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0e2b22ca-49f5-36de-9006-1efb0aea10fa | -13.01149 | -51.27668 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| d2e3aa2c-a8d0-3734-a214-473d40788e8b | -13.01144 | -51.27884 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ea96b6ec-874e-3f8f-b55a-aff03d27de7b | -13.01126 | -51.22282 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 957a2dab-3927-3df3-90d5-c563d9f0035a | -13.01095 | -51.22048 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4f1b27d5-317b-369e-8baa-d0234edfba13 | -13.01089 | -51.28219 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2942341a-daff-3d8d-81dd-7105c17ec7b6 | -13.01081 | -51.28432 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 358c0a6e-7348-35cf-84fc-e60d50f0214d | -13.01035 | -51.34526 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13d47046-53cf-3141-810e-15c6829c7c0a | -13.01035 | -51.22604 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| feeedfc3-081e-3d69-8668-74aa67712e89 | -13.0103 | -51.2877 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 32e5d8ea-40bf-34a3-aff9-8181eb9ef9dd | -13.01017 | -51.28981 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| acb8e727-e937-30ce-b679-dce4127e5c04 | -13.0097 | -51.2932 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1bed6194-7462-3e1f-a79d-2f33a48b0c76 | -13.00954 | -51.29529 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 32780551-cfe4-3eac-a51d-8c7ea338abb2 | -13.00936 | -51.23945 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9a7688b1-5317-3d84-bce9-50c06725662f | -13.00911 | -51.29869 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1c7f72b7-9bab-302b-821f-1778b56b4729 | -13.00891 | -51.30079 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7141d529-0229-32cc-b93e-01a34f438f0a | -13.00872 | -51.24501 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00a6bb76-e5ab-349a-bb26-f3950fe73ad8 | -13.00856 | -51.24271 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a78df41-39de-3bfd-ab74-463767c8b7cc | -13.00851 | -51.3042 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 97861aa0-c7c7-3ae0-827c-7f1d15efdfde | -13.00828 | -51.30626 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8d8b1bee-abc2-3f44-ac36-1516a85c9be5 | -13.00809 | -51.25053 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6209443f-67c6-3153-a6a9-7f8eff4d6f6c | -13.00796 | -51.24826 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38174230-3227-37e0-af46-f8e9b86f5d95 | -13.00792 | -51.30968 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5df0e05e-039c-3a7a-9b2d-a7b7a83d6321 | -13.00765 | -51.31173 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 605e1f94-df87-3ffa-8dd4-aa5d8a5d7b0f | -13.00745 | -51.25605 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4fc0c2b6-a702-361e-a72c-fb539e3cba9c | -13.00737 | -51.25377 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 31bd9751-b4d9-331b-bb2e-4d39ca8d2754 | -13.00732 | -51.31517 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b3139fb6-0942-326a-9d5c-19929d7b786b | -13.00702 | -51.3172 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 53715a16-8bb3-3128-bdfc-46cc7287ba72 | -13.00682 | -51.26157 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| db433de2-dc25-3a54-9bf5-91080b44d337 | -13.00677 | -51.25932 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| eca9a597-de53-3126-85b8-b261be224b33 | -13.00619 | -51.26707 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a44f43a1-b5c0-3534-b7ea-1965b2cec2f4 | -13.00617 | -51.26484 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 38b27c0e-1628-32ac-b2b0-2fba60826914 | -13.00558 | -51.27036 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cf42ada2-92cc-3202-813b-40f23662de2b | -13.00556 | -51.27257 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a3cdcc4e-a91f-34c4-adb9-c3dab4ffd20d | -13.00498 | -51.27588 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c612318-2a17-35f5-a0a3-162eb47c14be | -13.00493 | -51.27806 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56e193cf-7935-3e3b-b9cb-8a9b65c2aa71 | -13.00473 | -51.22208 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0aec8eac-4560-393f-96a8-e5cd2438d497 | -13.00442 | -51.21973 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 98c979ca-a69c-335d-8cbe-54acee6aea5d | -13.00439 | -51.28139 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb39f597-8c26-3e63-b7f0-2d5c46293d36 | -13.0043 | -51.28356 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47c6677e-1c75-3389-bd91-8115d675c8a8 | -13.00409 | -51.22762 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |


[Clique aqui para ver as próximas entradas](README139.md)
