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
| c9ab43fe-b908-31b7-805d-cfd42187c357 | -20.6351 | -47.4558 | 2026-08-22 04:50:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 43.3 |
| e4b1a750-fd6f-3e9f-a479-8bb3e4c65597 | -8.3904 | -62.6774 | 2026-08-22 04:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| b50a43c7-010e-351e-9481-26eaf815fb67 | -6.7509 | -58.6493 | 2026-08-22 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5a6dde0a-1f5e-30a8-97f5-9cf1c7f06bf3 | -8.3903 | -62.6963 | 2026-08-22 04:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f00c1c32-fdd7-3c96-ae1a-02c42b2f2e2e | -10.7982 | -50.973 | 2026-08-22 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e41c2369-1645-3a49-958e-9e0481798b67 | -6.7507 | -58.6687 | 2026-08-22 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8c77cd16-ea35-3e53-9065-d011d55a827e | -6.7692 | -58.6679 | 2026-08-22 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 455cf6b0-541d-3c10-ad27-722ab84f47be | -9.1724 | -59.4436 | 2026-08-22 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 33b83e80-b950-3ad4-8bbe-a3111f1a6faa | -8.522 | -54.8209 | 2026-08-22 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 18705bab-3aa7-3bf5-be78-9d08c3b0f01f | 2.79641 | -50.93083 | 2026-08-22 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32647303-20fc-399c-be6f-34108fb475de | 2.79695 | -50.93427 | 2026-08-22 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94eb4040-5a92-3315-867e-fb691da21d91 | 2.79309 | -50.93135 | 2026-08-22 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5da68c5-724c-3a1a-b64c-9a5ae8729e69 | 2.79586 | -50.92739 | 2026-08-22 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4e25c7-85dd-3f5a-acd8-d064b93be76d | 2.47897 | -50.97671 | 2026-08-22 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e964feb3-748d-30c4-8ba1-930f5f21283f | 2.79363 | -50.9348 | 2026-08-22 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f2921c9-df07-3a09-ab87-8a9eb902f643 | 2.52342 | -50.8498 | 2026-08-22 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cfa5196-8808-3c59-bb95-3567b5ed1cfb | -8.5406 | -54.8197 | 2026-08-22 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 04a30bdb-c71d-3513-8cc3-e5cbf8ebaa76 | -6.7691 | -58.6873 | 2026-08-22 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5a735c7e-5fb5-3115-9e8e-6764796bde50 | -20.6358 | -47.4322 | 2026-08-22 05:00:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 129.9 |
| f54d486a-8a22-38d2-ae48-6680bf2e50d9 | -8.9042 | -60.5385 | 2026-08-22 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 03aaa8be-1916-3955-8ff4-97490eec5063 | -8.5404 | -54.8398 | 2026-08-22 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 31f313cf-d309-3f59-a38b-f0204ac52bef | -8.4089 | -62.6767 | 2026-08-22 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 781ee697-58d3-3dfa-ae42-aaf920edb722 | -6.7692 | -58.6679 | 2026-08-22 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 4240b371-43ba-31ba-a69d-beff08f8f781 | -8.3903 | -62.6963 | 2026-08-22 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ff52ae7a-a164-3f12-89de-b8e022d970d9 | -8.3904 | -62.6774 | 2026-08-22 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 18b52666-c880-3ea2-bdfd-9efc47aba736 | -6.7507 | -58.6687 | 2026-08-22 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5de05e8e-1565-3e16-9206-47134459f4ab | -6.8188 | -59.6696 | 2026-08-22 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 91206602-5ec0-35e3-971c-b2d15cd40ec4 | -10.7982 | -50.973 | 2026-08-22 05:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 51fa723f-069a-3ee9-9ff8-9415a16fa22c | -9.1722 | -59.4629 | 2026-08-22 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 22a9bb8d-ba3b-36f7-ace5-940ac003e382 | -6.7693 | -58.6485 | 2026-08-22 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8d01e691-5c57-3d4e-9e1c-d26cffae505b | -9.1909 | -59.4619 | 2026-08-22 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 9faa1d1a-7987-3c22-9617-4e1b94f98c8e | -9.1724 | -59.4436 | 2026-08-22 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 08762f82-fbe7-3975-acf6-5c167bd52c8c | -8.522 | -54.8209 | 2026-08-22 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 79bf139d-ffa5-3365-915a-55327dbc65a4 | -6.8926 | -43.75179 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69c7048f-807d-330c-a472-d6bdea58417b | -4.65654 | -43.13398 | 2026-08-22 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb9a4810-ff56-3f8d-b9e4-22180afa50a4 | -3.0136 | -51.05308 | 2026-08-22 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4216ec7-281e-356e-9639-d090cf462815 | -5.56187 | -47.39038 | 2026-08-22 05:01:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a60b8a33-70fb-3284-a886-4d34a41b4719 | -6.87846 | -43.73597 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b0d01f7-ba1e-3b73-9300-7af1a4949dad | -4.27279 | -48.19494 | 2026-08-22 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cad14b07-212a-3d56-aa61-70630efe479f | 1.06804 | -52.49512 | 2026-08-22 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6b743ab-90aa-38d1-b998-1e35ef81d78b | -4.17835 | -49.39933 | 2026-08-22 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3b9ea38-0641-3d94-b47d-2ded406a21f4 | -6.34914 | -44.07935 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d92aaf85-23ff-3d22-bea9-5b74b17584b0 | -3.15429 | -51.09993 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e611938c-0182-38e7-94ce-68993a4f0984 | -3.36102 | -50.66802 | 2026-08-22 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8bc924dc-0118-35f1-bdee-1868b0d5939c | -2.45181 | -48.55866 | 2026-08-22 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891ed088-17d8-35a8-85e7-dcbe0fc52531 | -6.8775 | -43.74278 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bfc44f6-b875-3454-b746-82f096a66a6e | -6.35 | -44.08267 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5bce2add-7a77-3cf9-9d70-4cfc3110ea23 | -6.24611 | -43.68214 | 2026-08-22 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f260134f-ac0d-34db-93f4-d76305d7eaec | -3.05468 | -46.92753 | 2026-08-22 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 953ce8d7-49fe-3fd6-a5bf-9a8c46f3459e | -5.82426 | -43.49516 | 2026-08-22 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25ede9d3-b153-3882-bce9-5e4e6ba97909 | -6.34959 | -44.07622 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a71fa443-d13b-3d1b-8ceb-44df145e308b | -4.86373 | -47.40837 | 2026-08-22 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7e6b30d-117e-3d89-8f39-56d7f84421f1 | -3.01305 | -51.05659 | 2026-08-22 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbb93610-a810-316e-a1e3-c388af7a6613 | -6.35042 | -44.07964 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fc3ed7f-53e5-3c5a-8a0c-905c44ba87fe | -5.81368 | -43.79753 | 2026-08-22 05:01:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccb25244-ca7b-346d-aa95-cf21cf4f1352 | -5.71641 | -46.18386 | 2026-08-22 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2adb5cea-a76c-3745-8a85-bb8c1b8ea240 | -6.25142 | -43.68295 | 2026-08-22 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8dccb98-b53a-3215-93e5-a7c12f069209 | -5.59652 | -44.00453 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb76c54b-5cb4-302b-bad8-f6bfb6bdf5b6 | -4.93985 | -55.78363 | 2026-08-22 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 871dc3cb-7418-3d5a-a5e4-01e19b46d697 | -6.34562 | -44.07608 | 2026-08-22 05:01:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe35337a-a1a7-3bd0-b79f-e8c238d41710 | -5.8238 | -43.49847 | 2026-08-22 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c30dd0d-61b6-32e2-963f-34ef68a344ac | -6.88772 | -43.74773 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a25b85b2-25b7-3059-922d-dc6c99b74a6b | -3.15484 | -51.09643 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db2015a2-eb1a-31d3-aba5-6e87d8ae675f | -2.89235 | -48.79501 | 2026-08-22 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff3d5f81-a871-34cf-8ca0-6c119a538c1f | -4.42404 | -55.44605 | 2026-08-22 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b6280d8-5ae7-3ca9-8ab0-59b1ba831189 | -5.71197 | -46.1832 | 2026-08-22 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35b7c8e7-38f6-3d99-ae0d-0fe2bc432e35 | -4.17714 | -48.57352 | 2026-08-22 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d7dcdf-cf0c-372c-99e8-fed8a1b0b23d | -6.88818 | -43.74444 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff5eb1e9-ba5a-30a5-80b6-1f066fb54430 | -4.94055 | -55.77937 | 2026-08-22 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c496c547-ca2f-372e-86c0-3f098524685f | -5.59698 | -44.0014 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f4b3886-278c-3e64-bf6c-64d8bee43e22 | -4.90743 | -45.24591 | 2026-08-22 05:01:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6154b1c8-f5df-30b4-ab16-74e9a94a90be | -4.05863 | -49.10738 | 2026-08-22 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc77e542-0508-3221-998a-65bd9d0bdea1 | -4.53026 | -54.8625 | 2026-08-22 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb526d13-57ac-34a9-ab4d-e87096b22fef | -2.50039 | -48.13188 | 2026-08-22 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ce4e90c-19ec-3e52-9db3-bc6733bd17cc | -5.71576 | -46.18818 | 2026-08-22 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21a36138-3815-36f5-b03a-23c018afbb41 | -1.74621 | -55.24793 | 2026-08-22 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38ab4363-1738-38c0-ba4a-5d44e1c6a854 | -4.11932 | -48.93268 | 2026-08-22 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67d40f52-283e-3093-88f3-ac5d7e3c4058 | -3.26875 | -49.52737 | 2026-08-22 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91a4d24e-9770-3fa3-8d99-49ad49e68e2b | -4.45849 | -55.55502 | 2026-08-22 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff515db5-31fb-37be-98ac-0813071ff4c4 | -2.82832 | -48.65382 | 2026-08-22 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b47b958d-61f7-3afe-a789-93bb34a3fd03 | -4.90931 | -45.24928 | 2026-08-22 05:01:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff23ccad-c8f8-3d52-83fc-fb52f7bf14bf | -4.26898 | -48.19437 | 2026-08-22 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 604f05be-c879-35b7-917a-68afada7016f | -3.53816 | -48.1828 | 2026-08-22 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08c92b08-72a6-3677-a679-cabade8f850d | -3.03623 | -48.41435 | 2026-08-22 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 89fa40ee-2602-3474-b2f2-2e2af616f0fd | -4.52739 | -54.85798 | 2026-08-22 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52b45a01-40c9-3715-ad5d-0f61b70acf00 | -5.59986 | -44.01764 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 012acc90-7c03-3f1e-9fc5-8f30c0bbe961 | -2.45114 | -48.56287 | 2026-08-22 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df819edb-76cc-3831-b298-d572d9a7e1e5 | -4.16824 | -42.44194 | 2026-08-22 05:01:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d9016521-ba4e-3363-98a6-d15b60f49532 | -5.82565 | -43.48529 | 2026-08-22 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 68b14ae8-997a-379c-bdf2-5181ddb6d307 | -5.55634 | -43.43407 | 2026-08-22 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 673e2fce-22f2-37a8-8d3f-400d5e374552 | -3.42794 | -49.47809 | 2026-08-22 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5c1c1ea-7cb7-375f-820f-3e4a544b7460 | -2.50341 | -48.13697 | 2026-08-22 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cd2ba17c-78b3-324c-9be3-de8a046135cb | -4.52675 | -54.86192 | 2026-08-22 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd6c6c50-10d7-3fbd-8836-ac558ead71bc | -6.24564 | -43.68547 | 2026-08-22 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a316d49f-d353-323c-afcb-f345f3b371b5 | -6.25096 | -43.68623 | 2026-08-22 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4548879f-21a9-3025-bd9d-88ba94749c78 | -3.15763 | -51.10044 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c051f727-aff3-3b8a-a9ce-bf2e72effc60 | -6.87703 | -43.74616 | 2026-08-22 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2122e157-cef3-3baf-8b6d-3c3cd8ffc04d | -5.58665 | -44.00007 | 2026-08-22 05:01:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24313a9d-81d7-3a42-80f3-12e17387c0dd | -5.82473 | -43.49188 | 2026-08-22 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd6bb39a-5b5f-3085-932b-1aa60723da88 | -3.15818 | -51.09694 | 2026-08-22 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
