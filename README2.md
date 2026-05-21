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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b1c2658-8d58-3dc6-b9c6-8ff9813cf897 | -11.55274 | -54.53534 | 2026-05-21 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 47545771-9d64-3cfb-87f3-054c6cf6cc0f | -10.44673 | -47.95766 | 2026-05-21 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a2e59088-a1c8-30ee-af73-ab5ff085b24f | -11.30965 | -54.71341 | 2026-05-21 00:30:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3d78f791-8a13-36a0-829d-9122c32c8210 | -10.43716 | -47.94788 | 2026-05-21 00:30:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9c08e186-befa-33e8-afe4-17d4af0a5942 | -13.02997 | -49.94935 | 2026-05-21 00:30:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 55a63503-7afa-3de2-9f13-34f6caa86684 | -11.18444 | -55.91854 | 2026-05-21 00:30:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 6ff33483-7fd8-3d67-ac6a-107c87fb77e1 | -11.97098 | -52.4674 | 2026-05-21 00:30:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 49bd6836-85c5-30b3-b624-abf500178d75 | -11.91834 | -54.10227 | 2026-05-21 00:30:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 53f1ad97-6eda-30c8-b161-b73b8ba7e23b | -10.63436 | -48.34022 | 2026-05-21 00:30:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 55bef44a-9578-3dd1-94bd-71efa91fd36f | -10.49353 | -49.37005 | 2026-05-21 00:30:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 152c2556-d7c5-3efe-a370-f2076cf62180 | -12.54598 | -57.22007 | 2026-05-21 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fe9b2a40-775c-3a56-a93e-ac5ad2e2dea9 | -11.9953 | -47.76184 | 2026-05-21 00:30:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ec23c559-21e4-3fed-a1eb-93e0d942e0f7 | -11.46261 | -52.91764 | 2026-05-21 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bee137e1-e082-3bd5-ae7a-99937c2fed10 | -11.67863 | -54.58288 | 2026-05-21 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c35561fa-aa4c-353d-8aaf-f8157225eeb4 | -10.08622 | -52.17896 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7cf8ec05-679b-3308-9c18-02a2c058f587 | -6.393 | -44.1754 | 2026-05-21 00:33:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 35c16a33-0038-32a7-bf1c-13885c36a463 | -8.5434 | -45.98103 | 2026-05-21 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1d17cdf3-b2e1-3204-8896-e4ade780b541 | -9.95891 | -52.45424 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c873e6b4-78ce-35b5-8718-81de610eca4a | -9.29073 | -45.47409 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a875b117-d7d9-3ca0-ad30-178343767839 | -10.08306 | -51.6422 | 2026-05-21 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a47cce54-3e7a-3204-b49f-03e330953e7d | -9.28968 | -45.47964 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3da57f78-8753-3c14-a582-5505c7465073 | -8.54683 | -45.97393 | 2026-05-21 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 56091a40-f916-3193-869d-5c2892f3871b | -9.94999 | -52.45553 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 022bc94e-ce0f-3d2b-a37a-c8480671ad4b | -8.10867 | -44.15042 | 2026-05-21 00:33:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3377631f-e7d1-3f00-9f94-6b64c19383c9 | -10.60009 | -53.47637 | 2026-05-21 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8d6c9289-6390-31be-bf10-062d02fb4ed2 | -8.55755 | -45.97841 | 2026-05-21 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| a9fdf163-4ee3-31fc-a192-81df0e71c0e9 | -8.31821 | -48.01213 | 2026-05-21 00:33:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6ae46c1d-a295-3a55-b024-e57f8d0b0883 | -6.39634 | -44.16774 | 2026-05-21 00:33:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 3b4889a8-d7b7-3f60-883a-49ee03dd10b7 | -10.08753 | -52.18824 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3dbd11eb-5b9a-3071-a1d1-25b8de03bbde | -8.73741 | -47.98584 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| e452bcd5-6b8b-3e30-9e83-87c3c0acbc78 | -10.10986 | -52.4105 | 2026-05-21 00:33:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8bc38f09-6185-38dd-8c29-27edef479609 | -8.10264 | -44.15861 | 2026-05-21 00:33:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8d883042-e596-38c2-8b39-de66dfea1e3d | -8.32246 | -48.00493 | 2026-05-21 00:33:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0de9d1be-f28d-30ff-ae60-5c10292b979b | -8.55097 | -45.99906 | 2026-05-21 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 6993e752-ddff-352e-b7bd-067a28f10643 | -8.1135 | -44.1436 | 2026-05-21 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1714ddd0-fe08-3022-b8d5-c23619a709a0 | -9.3045 | -45.4809 | 2026-05-21 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 17f088fb-cd1b-3fbd-ad7f-4cdf7a4140a9 | -9.3045 | -45.4809 | 2026-05-21 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| fc0ac44a-f7fd-3cbc-a1ea-ed1af42d3331 | -9.2855 | -45.483 | 2026-05-21 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0fd2b352-ea63-3aa6-9d26-0347094bd2d8 | -9.3045 | -45.4809 | 2026-05-21 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f665a736-d3b3-379e-8221-2e4974080021 | -9.2855 | -45.483 | 2026-05-21 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5108cb83-0378-358d-b9f8-b5873508306f | -9.3045 | -45.4809 | 2026-05-21 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2c99b113-feb0-3acd-a6ad-e1fdd52eb35b | -9.3045 | -45.4809 | 2026-05-21 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| cd93b5e0-b822-34a3-8710-cfa602699015 | -9.3045 | -45.4809 | 2026-05-21 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a99f4c67-2d4a-39a0-85a6-72c6f6df22a0 | -9.3045 | -45.4809 | 2026-05-21 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 853646a7-3e9c-3f61-9b96-7ade999591bc | -9.3045 | -45.4809 | 2026-05-21 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9f8de11e-f0a8-3d9b-b02c-8d1fab7db9cd | -9.3045 | -45.4809 | 2026-05-21 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 15b72256-fbe9-3f84-9721-46b191116360 | -9.3045 | -45.4809 | 2026-05-21 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| dfddc540-25ac-3014-aa74-30836f361546 | -9.3045 | -45.4809 | 2026-05-21 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8c9769c5-7af4-3bc6-80a1-0682f936795d | -9.3045 | -45.4809 | 2026-05-21 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 28692d4f-41ba-32bd-87f0-a1e931eb37fe | -9.3045 | -45.4809 | 2026-05-21 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 6a458a89-aefd-3527-8e89-a09e35ac541e | -9.6104 | -40.342 | 2026-05-21 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 720710d5-0df4-3ca6-bc49-b7ff850a6f7c | -9.3045 | -45.4809 | 2026-05-21 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 27f68587-7e98-3929-a047-205d9a34f1e5 | -9.3041 | -45.5036 | 2026-05-21 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| bc51cb27-644b-32ab-9f46-9fc9e7f7fd93 | -9.6295 | -40.3392 | 2026-05-21 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.3 |
| 8cd5efea-7623-38de-8681-6ee1823c5d42 | -9.3045 | -45.4809 | 2026-05-21 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 17cef276-576c-30ab-b4cf-801305e80240 | -9.3041 | -45.5036 | 2026-05-21 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9b440d37-d2bb-3d0d-8185-b9c2853290e2 | -9.3045 | -45.4809 | 2026-05-21 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 6f571005-25ba-3774-a3a6-abc19a1cfda4 | -9.3041 | -45.5036 | 2026-05-21 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ec0e4b5e-23d8-3101-be5f-0c9b370cafef | -6.75674 | -45.01499 | 2026-05-21 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e930eaf1-9bba-39c9-88c3-1b08a662869e | -6.39028 | -44.17016 | 2026-05-21 03:30:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2d6e1838-55a0-3200-bd38-6e803b2a8122 | -4.36793 | -37.89718 | 2026-05-21 03:30:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b519e8ea-759e-35cf-9b22-b24292f0d585 | -4.36349 | -37.89647 | 2026-05-21 03:30:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 43f6f161-c0fc-3338-9403-9a9dda7cba5c | -7.82458 | -42.06079 | 2026-05-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 63786ae0-c5e6-3103-9c39-5947c95e0fd5 | -4.47677 | -37.81094 | 2026-05-21 03:30:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b9893514-0573-3f3d-80c0-3490d09f8ab2 | -5.02314 | -37.04188 | 2026-05-21 03:30:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2f954275-1be6-3286-a6af-3f46a915b29d | -4.47538 | -37.8195 | 2026-05-21 03:30:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6c21e821-7192-3849-9ded-7bbf0482888d | -5.95077 | -43.48985 | 2026-05-21 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d4eddd39-58ca-3b6f-86cb-d650712b7961 | -4.47747 | -37.80667 | 2026-05-21 03:30:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e1f3100c-f100-3239-a674-741f5c5f8bfe | -4.47608 | -37.81522 | 2026-05-21 03:30:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7f79e648-947e-3344-9baf-2098a95b597c | -8.38997 | -42.26764 | 2026-05-21 03:30:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51a2ba80-53f6-31a8-a6ee-57ed203c7677 | -6.3977 | -44.16604 | 2026-05-21 03:30:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8283601d-baa6-354b-bb00-bf71c1a18214 | -6.39675 | -44.17131 | 2026-05-21 03:30:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90760f62-a386-3609-b49e-cda23c89adfd | -12.6007 | -44.51828 | 2026-05-21 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2226b82-bed1-3603-b6c3-a33a524de1a3 | -12.06165 | -45.29083 | 2026-05-21 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b6abd16-c105-3a94-bdb3-fb11a2371ea6 | -9.29727 | -45.48655 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 848f0388-d25f-3d1a-97cb-7c8bb593099a | -8.54771 | -45.98428 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 45c1adac-edce-3225-9750-028042f963f2 | -9.2918 | -45.47927 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ffe2ab83-a254-3f71-9b0c-f65509e56faf | -9.30937 | -45.4953 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 92e123c0-3f59-3283-8d0d-59ad94e65909 | -10.64507 | -42.30005 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f27b253-aa27-353e-894e-162486b72275 | -10.65042 | -42.30105 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1a86d1f-5f5b-30ac-962b-d856b3b42807 | -9.30479 | -45.50003 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 08562d41-9ae5-3eaf-889a-7e881fff701c | -10.65512 | -42.3055 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 679c49d2-dec5-3086-9b26-084cddaac2d0 | -8.55406 | -45.99284 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 472b7f1b-280c-3f6b-a34c-02172c384854 | -9.30042 | -45.48677 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 6d604c2c-5fee-3a0f-95be-3dd4f89eb4be | -9.33371 | -40.21213 | 2026-05-21 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 8282c2c1-283d-3629-91e2-840d41545963 | -14.62812 | -48.02351 | 2026-05-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53204f4a-a2d2-3345-a370-61cf4279f8cf | -10.64374 | -42.30693 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af89dec7-06ac-3eea-b20f-78de46dc8992 | -12.23129 | -44.26599 | 2026-05-21 03:32:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26a4d5bb-29e6-3893-acfd-a9fc771d3d38 | -8.55466 | -45.98553 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9605f1d0-cd55-3a37-867b-2d46749f463a | -8.55531 | -45.98627 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8337be37-3c56-3abd-afc8-c419b5501916 | -10.64652 | -42.30656 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81b87d75-12d5-3e24-86bd-f77960ae52b0 | -10.64976 | -42.30449 | 2026-05-21 03:32:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d94acdc3-9abe-32ae-afe3-6654d9bfaf5c | -8.61578 | -45.99885 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2683088f-4412-33a1-8b6f-21aae07b4ffb | -9.31052 | -45.48944 | 2026-05-21 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| edd75709-ca38-3056-83fa-1b149008a6c8 | -8.62792 | -45.97868 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29bcb028-3335-3dea-9d99-095834da1061 | -9.62137 | -40.341 | 2026-05-21 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 67951b15-cc7d-3811-8121-2e570525298c | -11.99813 | -45.1365 | 2026-05-21 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf5ea476-d832-3544-a130-04f7a854639b | -8.61578 | -46.00418 | 2026-05-21 03:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18379ef6-105d-3589-bb43-62007b00dcc5 | -14.63039 | -48.03394 | 2026-05-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 048e3a94-12bc-387e-ab2a-d5f0295adbe9 | -14.90483 | -47.74782 | 2026-05-21 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README3.md)
