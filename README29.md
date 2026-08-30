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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ab2e5f6-bc2d-3156-8f95-b5c7b8fddc12 | -10.75489 | -50.68798 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c64ec19-a1e0-30f3-9d3e-025e596575f4 | -7.06422 | -42.1494 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81ab7111-07ae-35b2-8d9e-d8010a1c3e89 | -9.31667 | -47.62884 | 2026-08-30 04:14:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4eae71d0-ddfb-3334-9269-c7091edc51e3 | -12.92199 | -45.86242 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47ab85f2-4f87-3a1c-b47d-d0d64184d781 | -9.65605 | -55.11228 | 2026-08-30 04:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 65b1c686-0510-3540-9fea-f31f2c06075e | -7.04996 | -42.19332 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af7cb80b-9d26-3d47-a698-1c8c349c73bc | -7.09799 | -42.22433 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa3ff3cb-d809-39b5-89c0-c4f5f932c628 | -13.13625 | -42.01594 | 2026-08-30 04:14:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e0d9289-3888-390b-85b8-1970c0965ddc | -11.53004 | -45.55368 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aedae51-4380-3a41-8d24-930e6c0546d4 | -8.60907 | -54.77329 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b1db24e-b6b0-3944-ad17-139a7c9c98fe | -12.42089 | -42.88564 | 2026-08-30 04:14:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20f85896-0e95-3902-8c05-f990cf50608d | -11.20931 | -45.07614 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19605095-3213-3b0e-b4f3-84a4afa90e7a | -11.21074 | -45.0684 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 654a487e-40bf-387d-8061-97c3a9f3aead | -12.92112 | -45.8673 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 894a5203-66e0-3327-bb45-25adaa5b9117 | -11.79496 | -51.05695 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 5254f207-c391-3fb2-87b9-f967acb032fb | -11.3428 | -45.15394 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ba685a89-602f-3e89-8329-bc38521f9990 | -11.81351 | -51.04942 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6ae8e5a8-68c4-3f3a-a384-fcf21c3589f8 | -7.75572 | -44.75915 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9196c53b-1feb-3d2a-ab02-4afb277120d4 | -7.05673 | -42.15202 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 803a0a10-66d6-3d2a-8c58-d723cd8bd657 | -7.09454 | -42.22377 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 716c43fd-c7c8-369c-8ef3-6e64f6139b5b | -7.10611 | -42.2179 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f4ab087-6064-30e7-af73-e3c9baf0a8cf | -10.94677 | -43.02984 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 21944800-936d-34f9-9faf-158fdbf5499d | -12.90316 | -45.87898 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faf462b5-8db1-3259-ab8a-053723b9ea13 | -10.76474 | -54.04599 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad93c5f7-ff87-3d1f-ac26-438224456fb5 | -11.2416 | -45.0914 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93d58429-8d9b-3b80-a6b1-77977653c5ab | -10.73669 | -54.04655 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b720b854-eac6-320c-a4f7-9b84605e8491 | -11.02227 | -49.6891 | 2026-08-30 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2660f494-b0e1-3e77-9da0-3f713aef522b | -10.95364 | -43.03101 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 58722c1f-1007-3b02-9a40-ac474e751435 | -10.13145 | -45.70317 | 2026-08-30 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c34b8e27-5649-3c2d-8835-2c3134d38812 | -12.9241 | -45.87284 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9d24bfb-3ffa-3a40-abbd-90a27ba6c940 | -6.81753 | -51.15834 | 2026-08-30 04:14:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97d2acd7-8f87-3b26-9fce-ecade8c6becf | -10.76818 | -44.8721 | 2026-08-30 04:14:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8c58495-57af-392d-bcdd-cfb43c9fd07c | -10.95083 | -43.02665 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5e07774a-dd9d-30a4-9aec-a41d837dd75d | -7.61555 | -44.85509 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| a5294ebc-d9f3-3cc2-8790-8d6e8a696cb1 | -8.13814 | -45.47793 | 2026-08-30 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4444385-0e1b-3197-9c14-ad211bfb9c3f | -8.25236 | -46.50802 | 2026-08-30 04:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71d442e5-4f72-3577-a770-0e171a67c776 | -7.12729 | -42.82346 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6b350309-2559-3d32-90cb-01343a84314f | -7.08999 | -42.82966 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 674307df-3a71-38cc-8baf-138eaa5a95f0 | -7.09983 | -42.21297 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1966c28c-5158-3ec9-be85-01208c8101e8 | -11.21094 | -45.06683 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03f8c7cf-56b6-3bf9-8ecc-372273ee58a1 | -9.65655 | -55.10716 | 2026-08-30 04:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 76eb287d-9383-3bb5-8771-23d1db19b1f8 | -11.57489 | -44.03043 | 2026-08-30 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9caed5af-a2f7-3899-9605-94e13102afd6 | -11.16409 | -51.29432 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71b1c58c-94b1-30c3-ae65-3efb08d9e5f3 | -7.94684 | -44.26482 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1536f83b-379f-31e9-a8ff-6d06f092efe2 | -7.61165 | -44.85434 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d4c25609-d8db-3b23-8283-62254e511872 | -7.12634 | -42.76244 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f4f17d9-7103-3bed-aca4-a079e91e7dde | -10.74268 | -50.66327 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32fb03b6-e5d8-316d-8557-0822478ecfa4 | -11.20849 | -45.08083 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0daf16e8-8aeb-390f-9861-68e8f815a4c7 | -12.91169 | -45.87566 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad85d067-5c6e-3d62-8ece-10f4b1c51c4f | -12.90786 | -45.87489 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1897931a-6f94-35cd-a996-444affbf346f | -7.18312 | -43.71667 | 2026-08-30 04:14:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 203b1624-4836-3143-89ce-383b4edc79cc | -12.90364 | -45.85411 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f545a660-a1d0-3574-b959-31ac28262b1c | -7.09576 | -42.83879 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fc658c1-cfa8-38fb-99a9-2e687ff5b373 | -11.69228 | -47.61524 | 2026-08-30 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 16f0abfc-b1ef-352d-8e3d-7abc7f84f203 | -10.95646 | -43.03537 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 844bb8bf-0a7b-350b-b9eb-a2ef219d4efd | -11.24634 | -54.00302 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 244d34bb-f845-3910-aa6e-1198bc0ba47c | -11.51629 | -45.54125 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 401aa971-010c-3a7c-a3be-03d6e60cf7aa | -7.5344 | -44.34418 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8caf966-c509-3aa2-bc37-3c6ce5753c13 | -7.22029 | -42.76062 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2587c3af-1ac2-301a-845d-f1550c290229 | -11.82517 | -51.04807 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5ee35c8c-4128-381a-9729-d5aac341932b | -5.75879 | -51.68944 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8318bd3-e02c-3cb3-88d5-aeef1a95730a | -9.12491 | -50.58789 | 2026-08-30 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da3aabb3-5fc3-3edb-b443-15cc354fb339 | -11.25321 | -45.31991 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77bde287-81ac-3186-b96a-b8a3cf41805d | -11.27311 | -45.31846 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3157ecdf-e9fc-3ea9-99d5-5918d9e8953b | -6.64029 | -53.18099 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d4d7889d-cf30-3d5c-9f49-3eec0e7eb613 | -11.20636 | -45.07082 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8ca670a-07ed-3606-a06c-8169d2031d4a | -11.02285 | -49.68608 | 2026-08-30 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07e53aab-e304-3a06-b7df-4722d004044e | -8.61326 | -54.78956 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0e35869b-b6a7-3d65-b1c7-5b69d7823034 | -7.12956 | -44.31512 | 2026-08-30 04:14:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff00a330-375c-3592-95d3-611e9e97dc25 | -10.75681 | -54.05061 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ef77874-49c3-30c2-a34b-80fef63befb7 | -8.22188 | -40.77216 | 2026-08-30 04:14:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2ab654f-a2d4-38fd-a09b-4bad5691133d | -11.3474 | -45.14984 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1ca223e-8c05-3a86-93ae-3b0d7036ebca | -11.36004 | -45.16685 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 834f3543-c5a6-36dd-8ac1-9804fdda4c86 | -11.21303 | -45.05476 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 255bcbfe-ee3e-301b-8426-2069829ea6d8 | -11.21253 | -45.05774 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99c19d24-06c9-3db1-96d5-ca33c6b78015 | -11.80255 | -51.04717 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| f0d19c5f-5d5c-3116-80df-02f86df942fb | -12.78479 | -44.61361 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08b62a39-8324-3a63-8a46-66d260e9a0fa | -11.49689 | -50.27952 | 2026-08-30 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7f78b18-a93c-3979-b2b8-729a08c516f1 | -12.37171 | -48.19764 | 2026-08-30 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ac7eb78-92c4-318a-9e43-0ff503ccdf38 | -12.64345 | -47.64213 | 2026-08-30 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cd61c984-aa17-334a-98be-2fc065d11422 | -11.26519 | -45.06702 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e99caf8-b66c-3da2-b97f-89182f3a80b9 | -5.75246 | -51.6883 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b1e85db-1eab-35f4-bc00-877603f0ad24 | -11.27513 | -45.3403 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44b70d87-6130-3bef-91e0-642a6643359b | -9.02706 | -40.26081 | 2026-08-30 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 676592d2-c32a-3c62-8618-869363f45c92 | -12.91814 | -45.86176 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27e7ef5a-242c-3df7-b250-7d6cf521ba8b | -8.14921 | -45.51047 | 2026-08-30 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0000505-5b76-3b58-a3e4-a7f591c65313 | -12.8021 | -46.45693 | 2026-08-30 04:14:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa158a55-59f5-3958-aa98-60c0f745517f | -11.21226 | -45.08147 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f9712f5-daf5-37cb-858c-76e8ec083ee7 | -7.05734 | -42.1483 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 94d34a6e-61fb-3ca2-82cd-3eb126521bc9 | -7.11763 | -42.83826 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 999cfdd9-2a58-3156-8b35-b72bca6ac156 | -11.79566 | -51.05331 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 8f4d8764-4957-34ed-991d-2c2a932e8e84 | -9.35936 | -40.6613 | 2026-08-30 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1eb370c8-0aee-322d-9c01-6e7cab358650 | -7.04935 | -42.19706 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b064639-546c-3fac-b21a-c5371f4065bc | -11.23703 | -45.09537 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d3b17be-8506-3f27-ad7f-58e462454c23 | -10.94226 | -51.41726 | 2026-08-30 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64fe6223-5109-352d-b588-fb772559b044 | -8.01292 | -48.00751 | 2026-08-30 04:14:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df2d3ca2-5f6f-3cc5-91df-f6fa3a858561 | -9.65762 | -55.10467 | 2026-08-30 04:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2ba3b6f9-c892-3009-9e01-db1646553aaf | -10.76678 | -44.85762 | 2026-08-30 04:14:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03465936-b8e8-34f1-9b48-a722d5d56d80 | -7.18681 | -43.71729 | 2026-08-30 04:14:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f86010a-32fd-3a0f-858a-b3131d841554 | -11.36383 | -45.16749 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README30.md)
