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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c250d37-7076-33b0-8387-e70fa4a99c96 | -3.34105 | -53.37439 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ace5ad6-bd76-3965-9c0d-1be9489873a9 | -1.79965 | -50.90856 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d744cfc2-fe63-37f9-9298-d0493296b4fc | -2.83044 | -48.47903 | 2024-12-01 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9bc890a-7f48-38e3-9bea-86e7d18a0955 | -3.30838 | -53.83272 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a479b2c-ecc9-3028-8fe8-453a9e7a8c89 | -1.29618 | -51.72585 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9293e460-c496-3ab1-9e70-121b40239c0b | -2.91147 | -54.11441 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 652c452f-bc5c-330b-b025-abc5504285ae | -2.95915 | -50.5764 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3abb949d-ee28-345d-ba1e-477968b1a4f3 | -1.62328 | -53.89039 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4ab8257-e1a2-326c-9693-cf5cbddc75c0 | -3.09687 | -53.31678 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 183e9a4c-b2b9-314f-a8f3-73655881bc30 | -1.49091 | -52.6441 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8389319-a116-3430-acfb-5fde8ffaba59 | -3.5876 | -50.37134 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3cea608-f72d-3b1c-b71b-9068dc53f9e9 | -4.61878 | -48.02584 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ca14b3d-f188-3ade-b8ab-7c5abdbbec02 | -3.13447 | -54.53403 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0f37ccdd-b6be-3372-bd14-bebe079e07f7 | -2.74863 | -51.74978 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c87545a-3448-3052-bfd4-0b50128f2387 | -2.6308 | -54.20396 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 089625f9-20d8-3ba9-b41a-328ef1165236 | -3.09335 | -53.13171 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e210032b-7c4d-36f7-a6a2-a2782a17a1f2 | -3.09645 | -54.04406 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44eb90e7-cb08-3eb4-ab69-868b8b298f60 | -2.80537 | -45.94087 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e77ac5fe-4849-3123-8602-d5b5bb1cefe0 | -4.90916 | -49.90282 | 2024-12-01 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd63dcd1-44ed-398b-9364-cdcb1627a928 | -1.70321 | -52.44055 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 606c720d-af8a-3c21-a197-073779a88759 | -3.99727 | -49.97828 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e53373fd-cab9-38fb-99b9-bd7f230a4bf0 | -3.31155 | -53.86011 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3708eb8-408b-330f-8fc1-19ad03be5de6 | -1.18474 | -51.76996 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d220eb8f-4012-3316-922b-7a0ab6d18f89 | -2.78536 | -52.86766 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 029a0676-c073-326b-8fd7-b589fdecf878 | -2.81872 | -53.94578 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35f844f6-ad3b-3338-b699-0451d730cae2 | -1.72457 | -52.48799 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 706cf447-3141-3ebd-b55b-7a7e81c108af | -1.74804 | -46.26915 | 2024-12-01 04:44:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea13f093-4626-3f73-a7e9-5c397ce8208b | -3.21147 | -54.17181 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 441b3a26-2f2a-30d6-8af9-9be372c641fb | -2.03025 | -55.77629 | 2024-12-01 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1965afe-9702-3230-8157-160ded012270 | -3.66382 | -54.28508 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5870785f-5674-37dc-9413-17d310973ff8 | -2.06362 | -51.19588 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd5277c7-845a-3b52-8313-b60e82e88f22 | -1.64186 | -53.86803 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca70e593-5f2f-31de-bf66-b8dd91cc8c30 | -4.11026 | -48.88894 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01ff1a77-c9ba-364d-9106-a0c5f35b679e | -3.74075 | -51.83726 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccc36193-a40f-3e3e-8e21-bb95c6725c7f | -2.96978 | -53.89779 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d077c1dd-5069-37e1-8d1e-951b806277f8 | -3.24947 | -53.62201 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55a0a4a7-d846-3b4a-b68d-797ebc6fc600 | -1.06728 | -51.75971 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ffbaef8-3149-3e41-8d1e-27b4fdbff971 | -2.0703 | -50.7183 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80a8f739-daf9-3768-b7d2-ebf96c82de6e | -1.45439 | -51.49836 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aeb9867-fc9d-3d01-b3c5-95a09c735c34 | -2.88201 | -54.00873 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec1f3846-c0d8-3c9f-b5d9-edc0688a72fa | -1.70563 | -46.1489 | 2024-12-01 04:44:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ff48fbc-c46a-3ce8-86f0-da04a80f191b | 0.15533 | -51.62797 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 549291cf-2f83-399e-a391-9f2406baa753 | -3.30714 | -53.86389 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 19c493a5-4078-3c8c-bda0-6b49fa5ce7c5 | -2.1152 | -46.56398 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f648bbce-7dad-3b7b-a643-1d83f2761d39 | -4.20366 | -50.68703 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9d38e91-7ae3-35db-9357-41f2f596f220 | -2.98512 | -53.29139 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e552d45-860c-388c-8e5e-3e2d32cb47a6 | -2.76724 | -53.9792 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43f17f6a-aa9d-3574-b5c0-bbed166ee2b4 | -3.10438 | -53.10871 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fef5dd57-36bd-3612-a97a-56e3f5078186 | -2.58904 | -53.98283 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ae3dc3f-c410-3980-a5ce-dbc3df917167 | -6.86726 | -47.23783 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b3bff56-e0e6-3f7f-acc7-a3656944a68a | -3.11131 | -53.76045 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a11685f3-e96f-3e47-8a16-f2b366d7fbcc | -2.04456 | -54.66262 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e663083b-7571-3050-b895-ef218ae0bb18 | -3.67112 | -50.24636 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 975321c5-b049-3a88-b50a-98ad81094f6c | -3.39551 | -50.30204 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e9078f5-e3a8-3f6f-8d0f-7edd8f79abbe | -1.26629 | -47.87868 | 2024-12-01 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b07bb6a4-379f-36dd-bcf3-0614e0eb7120 | -2.6353 | -46.12559 | 2024-12-01 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b19866b-c3f6-3f30-97da-3c47d9452c51 | -2.63534 | -46.19843 | 2024-12-01 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba7e083f-896e-30f6-b110-9b8ef0d4675c | -3.32484 | -50.14614 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c08e2da4-7b3c-35cc-8e80-595b4c0ec241 | -4.00575 | -44.75267 | 2024-12-01 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| c4825d52-dbe3-3b8f-ae82-907351d72b48 | -3.49067 | -53.82009 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a865af6-af95-33ed-bed7-6d74feaf11f3 | -0.59554 | -51.69161 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9618a11-36fd-38f2-8666-e59dfb2d6252 | -2.42966 | -50.39439 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 861e09bb-f8f1-3c8e-bc37-b7b15599b5d6 | -5.91569 | -43.84501 | 2024-12-01 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09c12b42-21aa-3237-a870-f7900f585adc | -3.05902 | -54.41431 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0d9d968-f273-3b47-9b7c-f0a79308a6b9 | -3.06377 | -53.26953 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c2d41d5-08be-3b35-abea-7ff489966670 | -3.21525 | -54.17243 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 673e1243-8362-31f5-8e4b-3fd1ddfb941f | -3.42932 | -53.89579 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89084726-8b32-3551-8440-acf254f10a47 | -1.32546 | -51.67364 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dc6da6d-855d-30ff-8643-99a9e8833134 | -4.39421 | -49.92993 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9915a56-bf6f-389d-9c10-56838b1e543f | -3.28232 | -53.34806 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf741a65-a441-3d06-9864-bf56f2765699 | -2.8567 | -54.19198 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43f0eb75-40db-3444-9113-d0baa60fefd6 | -1.44581 | -55.20024 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 095b2cbc-00a2-3df1-94fd-ed7f7ba06bb1 | -3.7414 | -53.39098 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fea2976c-4e75-3f7f-82d7-677c59527ece | -3.71682 | -51.06878 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd0dbab6-cff0-395b-a04a-1a6c8ca2b275 | -3.08617 | -51.07741 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e07e970-d21b-348a-a0f8-86163e872b50 | -2.81827 | -53.04954 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0068d696-d977-3c61-975a-98c4a937ce58 | -4.26591 | -48.35571 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02175eeb-435f-3c73-a16b-7639a483d410 | -1.2584 | -51.58776 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7219350f-7807-31c4-ba04-f4a01537b837 | -2.97361 | -53.2939 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d333b9f1-2aba-3311-8cdb-26a49fa9599a | -4.76137 | -50.99458 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d8408e5-be94-3451-8cd7-0be844972f52 | -3.09851 | -53.28333 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 367444fb-3f02-3ff4-884b-731411852733 | -1.9941 | -51.17773 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c374aae7-f769-381b-9740-f5dc11853ed7 | -3.82021 | -46.59207 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99ea039c-d220-3c5a-9b04-40365bddd412 | -2.73501 | -47.99416 | 2024-12-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acb0357f-7f9b-3a87-beb8-6fa93cc157ca | -2.04651 | -54.68729 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e6309c9e-7221-3945-a29c-ef78a21459a3 | -3.31256 | -50.50469 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba49c06-4ad3-3f75-b6f4-b8c7f4ea15c8 | -1.20777 | -51.73547 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87adcdeb-3f7e-3d9b-837c-2212952417fc | -1.43384 | -55.2478 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95f12e95-b5f3-38f9-b4fd-117a0a348583 | -0.26035 | -51.49629 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec8713be-e74d-3846-95a5-fbfbd5366b57 | -3.32237 | -54.1762 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bd8fb31-94c4-3183-9bd4-5dfc9fdb91ce | -3.05524 | -51.06567 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d8288ce-579d-31ee-8696-9c48df3be4a7 | -4.54579 | -43.30708 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 290af948-28f1-37a3-8728-6c9dbb1a8dbf | -2.36267 | -53.68535 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e455e76c-1b4e-3992-8632-5acca05513b0 | -2.87433 | -53.98444 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b2b4595-f426-3ec6-848d-ae920786db10 | -3.52373 | -50.47449 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80311df8-e9ce-3fd9-8fca-9eb85d864fd2 | -2.98471 | -53.90005 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b155f5d5-8a9f-3e86-a384-bca05b69cd20 | -4.14124 | -50.65618 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96993ea3-c1fa-3a1b-900b-386d878f8fe8 | -2.596 | -53.98612 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edc3f41b-6412-3dee-9fec-7cc5c27ab269 | -3.32107 | -53.29062 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bddae833-e045-3d0c-bd66-091bcfd95f76 | -7.02442 | -44.84312 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README59.md)
