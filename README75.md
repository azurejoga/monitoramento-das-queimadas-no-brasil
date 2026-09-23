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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a3c48f2-9518-395c-9f24-5f675b9786e2 | -2.85309 | -57.80435 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcfc396a-c18d-3cd9-871e-0867cddc2c64 | -3.00516 | -54.17726 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 451d28d9-762b-36d6-938d-57fe736185a0 | -1.33101 | -54.66479 | 2026-09-23 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdf85be2-e9e6-3e1f-8a63-0101214a4804 | -2.86438 | -57.78942 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 374eb15b-b420-3c2f-a499-8293a47db937 | 2.06436 | -50.9679 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb72777c-3714-3fce-86b8-2a436fb6bc2a | 1.08307 | -52.55301 | 2026-09-23 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db306d4e-c10c-3a33-8fb6-8ae5aaea99ba | 0.33752 | -51.08752 | 2026-09-23 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea4281f6-eea9-3a5a-9c7d-116122ce56f3 | -3.93992 | -49.99415 | 2026-09-23 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93e074db-4de5-3c46-93aa-ff25581c1a04 | -2.94382 | -50.29986 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45f2cc5d-291d-33bc-a12e-0a62a5051c1f | -1.39813 | -49.05103 | 2026-09-23 05:01:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5aa2833-4edf-3fb7-a166-cdb2c23efdc4 | -3.01032 | -54.18986 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c0d73af-8d59-3d9b-a733-33825ee86b70 | 2.07457 | -50.95226 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d3c6a25-7c64-3fa2-9707-f900c5e12c3c | -3.52858 | -44.84227 | 2026-09-23 05:01:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 088e2f10-ef36-398d-93bf-35a82b6767de | -2.72216 | -57.64701 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dadeb787-3180-3f51-b535-a8745c5a8d6f | -1.11604 | -54.12369 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618a5039-bdd5-3272-94c5-bac3f727bb3c | -3.44589 | -50.61258 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a05aef9-8573-398b-a786-04585b99e9da | -3.80759 | -52.36731 | 2026-09-23 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc63c42b-045e-3219-b90e-f9d7157d71ed | -2.29282 | -47.88703 | 2026-09-23 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d10090e-9c8c-3f0b-a39a-348d3ca21e85 | -2.55053 | -49.10018 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 954bf264-6996-3ce7-94f9-3f55a1659f27 | -3.00682 | -54.18931 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b155aaad-6f02-31ec-94f9-d39409cf06b3 | -2.45678 | -49.21935 | 2026-09-23 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a5089fe-2eb7-3e0a-b49a-6a9c59125227 | -3.07303 | -51.20166 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8299cbce-0b96-30e9-bd95-4cd47d0c6e06 | -1.07348 | -54.10149 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fca42d1-04c6-3fc7-9f0f-cf00ca9d9a01 | -2.85756 | -54.19789 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e58a6a41-7b38-3110-afd8-2dda56c8be12 | -3.00743 | -54.18546 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbfc1500-2964-3623-bd90-db5d8fb6433b | -2.82373 | -49.24511 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5f79232-d779-31fb-8c40-32288ea15b08 | -3.62663 | -49.99319 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e44c10-659a-3631-8799-327ab1298099 | -2.9483 | -54.07835 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5910e40d-8318-30b8-a4ab-3fcb5cd91b56 | -2.81959 | -49.24847 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54455d9e-ec6d-3fca-a03d-2d02e7df9fe9 | -3.8661 | -51.18529 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b658ac5d-90ea-3ec6-828e-4f7809a8cf4b | -3.25585 | -53.96283 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2952cce5-0907-37ea-83a1-bb500057eb18 | -2.86783 | -49.63029 | 2026-09-23 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 407a340a-2e9e-3eb9-94f0-12c38569421c | -2.93755 | -50.49419 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dd7be16-46a1-328c-beb2-db0ae2b0036c | -3.44871 | -50.61666 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 783d34c7-1dcd-3563-9234-61327b241433 | -3.00228 | -54.17287 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f76acb39-0e1e-3b22-8937-4f6568562221 | -3.9405 | -49.99038 | 2026-09-23 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e981614-e7c8-3f9b-88a9-168066e3d959 | 0.97838 | -59.3807 | 2026-09-23 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2944841c-a94e-3bf9-a7c9-4ba4d21a63e8 | -1.92225 | -58.26244 | 2026-09-23 05:01:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 63aac212-1793-3864-a96d-ea022fb884be | -1.63332 | -55.12608 | 2026-09-23 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4913adef-b779-36c4-802b-a29ad480a433 | -2.9566 | -54.07906 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 116c11f9-f960-3496-81ed-cf1370a4fbe0 | -2.17181 | -48.31958 | 2026-09-23 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b40d0e9-36cf-3739-8c8c-dea3e3fd2ec2 | -2.74114 | -51.36986 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74c9bbfc-3cb4-35ff-9b49-71238496afda | -3.53126 | -44.84065 | 2026-09-23 05:01:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 123046f4-1b22-3ee7-b6e8-c8124299c54d | -3.07175 | -54.39071 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1df87bc-b788-3a29-8d92-490d9017910d | -2.98105 | -50.39443 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0407706e-29ef-317b-b08e-17855b6000c2 | -2.95884 | -54.08725 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47c59cb9-f2e2-38c8-9998-2f2620acb690 | -2.9737 | -50.39698 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1611cd0-ee66-38c1-9b17-371ced4bafb1 | -2.97145 | -50.38926 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aee647d7-761f-32d6-8261-2da98789da70 | -2.85243 | -57.80843 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ce1076d-667f-3b0f-98fd-9475e411fe16 | -3.0097 | -54.19372 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32ec0643-c7fc-39c0-a1d6-0e397c5a959f | 2.07214 | -50.95253 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2690736e-9e93-365d-9c58-725e33992f94 | -3.25073 | -53.9505 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 976c1e31-0749-339b-b524-abef2b0f74fe | -4.28653 | -48.61059 | 2026-09-23 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11e2a04c-d46d-3795-b39c-67bd5a2dff51 | -2.56973 | -57.50204 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed9f8fe4-d8e9-3684-8155-47fa2feee84e | 2.46744 | -50.97153 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10a3e7fd-8a6d-3dae-9924-cddd406e7bf3 | -3.01504 | -54.1827 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 848c173c-e2dc-3623-a5dd-79cee914ca01 | -3.24059 | -47.25073 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aef32930-3ede-32e2-a91a-1965978a34cf | -4.28587 | -48.61495 | 2026-09-23 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42abfd8b-a0f0-3379-90b7-7aa28ce5f97d | 2.08841 | -50.95362 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fb2a397-b4f2-3570-8237-92a52af51d66 | -3.42734 | -50.6646 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d5a7735-01c2-3613-8a72-d85a86d686cd | -4.2266 | -48.61642 | 2026-09-23 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2ebfdbd-d6a7-3f86-b602-8110ed3f7f5b | 1.4413 | -50.81836 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6684b51c-65b4-3715-94ef-5af39896e460 | -1.39874 | -49.04716 | 2026-09-23 05:01:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58cdeb40-5d9f-3fb1-936a-a8cb00e90444 | 0.1805 | -60.48721 | 2026-09-23 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 786c1354-202e-3426-bf68-eeb51f03b548 | -2.47988 | -54.50471 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7b1b7a7-8404-3d6d-9929-99da315e0dea | -3.45378 | -50.60646 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e25c943b-c884-382c-8192-e014a493730f | -1.94093 | -56.59238 | 2026-09-23 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfbfe0ea-6189-301c-9593-96f5dcaf82f8 | -3.03271 | -54.40852 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd519a7b-c7fe-3112-bc75-9ece1fcaa4ea | -3.86945 | -51.18583 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bd6e2a5-0f03-330e-806c-1736633bfeaa | -2.86642 | -52.41793 | 2026-09-23 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04e75756-342a-377f-830b-de51eee5cbaf | -3.03966 | -50.26596 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 517c3a65-b1e7-3798-9e16-927fdd12d147 | -2.97088 | -50.39286 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 438b77ff-b699-35f7-b83d-f07d75766c67 | -1.58966 | -54.41801 | 2026-09-23 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97083802-c042-31b2-a18f-cbc4c5751b72 | -2.56548 | -57.50135 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfae4f83-2f3e-353a-9fec-4610e34617fb | -3.20891 | -50.91782 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f22e5462-0339-3e98-b6ad-e4b1ae29f21b | 0.97791 | -59.37772 | 2026-09-23 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e82860e5-4291-322a-8d39-32d18232fc21 | -2.55122 | -49.10149 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88c9a67a-8b20-31c7-b18c-7733046f7a88 | -2.94928 | -51.03875 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b285fb8-25e5-303b-943d-dad6465331cc | -2.97313 | -50.40059 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf018203-260a-3e69-b4db-2033b835e589 | -2.84329 | -53.99235 | 2026-09-23 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 638e84e4-e9e1-32a1-bfd3-c59a8935ef1c | -2.32502 | -49.20782 | 2026-09-23 05:01:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0fb1b4b-78b2-37ee-94ac-bea22ac88afa | -2.74095 | -51.54353 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa78eb51-e6f2-3c26-808b-7ff0ab0477d9 | -2.46729 | -57.9115 | 2026-09-23 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c312b691-eac5-3759-baf5-a45c17b023bd | -3.23344 | -53.9478 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d954fca-eeb4-340d-b0c5-1e08f294f018 | -0.75297 | -49.71619 | 2026-09-23 05:01:00 | NPP-375D | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd3cc8ac-12b1-320a-b07f-96efa52ee6ee | -3.22634 | -46.9441 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 560e93d8-2a34-318f-b1ed-e6ac1e33312e | -3.07112 | -54.39464 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a9ac61d-a17f-348e-80b5-dafda9501e1c | 2.3371 | -50.76924 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ba661dd-a5ad-3c78-9ffd-19348938dc06 | -3.17235 | -51.35949 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e8abe6d-181e-398d-888d-1e41c90dd884 | -4.2962 | -49.12914 | 2026-09-23 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27392bc2-6d85-3a75-ac95-de6ee2467914 | -3.22176 | -46.94709 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31e434d4-524b-382b-a4d5-43c816d2e5a0 | -3.36289 | -50.76075 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb6ce37-c6cb-3a32-a5e8-c634a7254d75 | -3.38223 | -50.44124 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bfdeece-678b-3f97-aecc-2047fc00e9d0 | 1.90947 | -60.57713 | 2026-09-23 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b70272ea-a84b-3df2-b134-f04909dd0865 | 2.33046 | -50.77028 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85e11efa-c5c7-3059-9a77-ba1cfa56d938 | -1.32804 | -54.65993 | 2026-09-23 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b365aa6c-c73d-39d6-866b-f6cde09dece4 | -3.84708 | -51.75995 | 2026-09-23 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10b8e15c-e42e-3c4c-ad81-019702a745b5 | -1.21491 | -54.55072 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e3d066-c35a-37f6-abf5-f55c1fa3ec65 | -3.04455 | -54.40244 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bf2ecb5-7018-340d-b77c-a6e704360746 | 0.78685 | -59.20623 | 2026-09-23 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README76.md)
