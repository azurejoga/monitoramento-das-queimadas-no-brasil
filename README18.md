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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49fbb425-5723-301e-a2f1-3fadcb1bae8b | -3.74694 | -46.95653 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae73f05-6172-33b3-9964-65bb2241cc10 | -3.75667 | -46.95344 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d9251753-1799-350a-8576-cfc92c4a8fcb | -5.57158 | -44.97692 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ae90bb9-a433-30ae-96ee-56f13c792631 | -3.18886 | -52.02153 | 2025-11-28 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4804acb-9959-3a3e-9139-6ddfbdfab5c5 | -3.92606 | -50.99681 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec066be5-c745-3ca4-9cf8-a2a8358b129b | -3.17605 | -50.24325 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5e8065c-89a9-348d-a042-d749d8169c7e | -4.2748 | -48.71701 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ced63819-8d21-3cb9-a5fc-c990292ec822 | -3.22456 | -50.31518 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f8b2504-eea9-3937-b5af-ae7cc4be5e6c | -2.71257 | -53.17556 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12f18000-13b0-3e0b-bd95-8fd391cf49ae | -3.92669 | -50.9928 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f87b5fe-4efa-36ff-9678-7a1d08dd9643 | -4.30064 | -55.61109 | 2025-11-28 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a477f2ba-d32d-333a-aa88-bb7f06c471ff | -3.31607 | -50.27591 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a77afe28-f49c-3736-aa2e-d1a9f5eea2ad | -3.92993 | -55.89113 | 2025-11-28 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39a8f461-fa65-396e-b44d-2ea47162d3f2 | -3.45756 | -50.54564 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e38b170a-51a0-3f46-9eaf-48a9b0e113e5 | -3.60295 | -50.42319 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42ee1fcc-3a8f-3e27-882a-a0dd5bd5203a | -3.85601 | -47.03514 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80f9a6e1-e6da-3318-bea2-beb69d9ab377 | -3.03456 | -50.97945 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0a45532-bb04-3d6e-b04a-c7c50096cf99 | -3.23253 | -50.59459 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1181c636-f99d-3985-9450-c9e579c46c7d | -3.92315 | -50.99224 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72491246-679c-3976-b562-018596f9a133 | -3.38907 | -50.78902 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 073200d4-945f-390b-8b23-6700c8657a90 | -4.06113 | -46.56252 | 2025-11-28 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8131ca7-da44-3547-919d-99214775ed3d | -4.31884 | -44.05752 | 2025-11-28 05:01:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cc0a4e0-c250-3308-bd22-b29a93270471 | -4.94985 | -48.63191 | 2025-11-28 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 863b8bd0-5e2d-3009-a681-f49702768443 | -3.86223 | -54.05954 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f01ac06a-614b-312e-a53e-8d9a27428cbf | -3.82952 | -50.1869 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52c7d0dd-aec7-3e88-a648-ac8bbdaf4751 | -3.97708 | -49.99072 | 2025-11-28 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89288a3e-cd46-3f00-8354-74f5a7ca625d | -3.75802 | -46.94456 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac75321f-f73b-3009-b3d0-8a2f424e7d88 | -3.03518 | -50.97554 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89c9d0c2-e342-3e0f-aad7-f0c6e085084b | -2.7217 | -53.18064 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f2dfa4c-320c-3c41-ab4d-ce676c214c59 | -2.71534 | -53.17952 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7fd3c86-2a9e-391c-81af-c86eb310cfa7 | -3.66847 | -45.40686 | 2025-11-28 05:01:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 47de8e2f-39ed-3dab-8ab3-cc8012a679a4 | -3.64092 | -44.88139 | 2025-11-28 05:01:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cabb4d6-2709-3735-bc10-7ef9a0cf4a18 | -2.79467 | -52.95507 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc537d0-800e-3373-8121-cbba45a6408d | -5.04573 | -56.19683 | 2025-11-28 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 739aabd4-7fba-30a2-8216-11c6e8ec8901 | -2.74466 | -54.59315 | 2025-11-28 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1a8d854-818b-3330-a958-ee36a6da9b61 | -3.46713 | -56.3197 | 2025-11-28 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e284bb4d-07d5-3448-8db0-7f1e958296e5 | -3.40884 | -53.30961 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa19692b-dc28-3f6f-a8ed-11b2170d90ad | -3.74273 | -50.96967 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98d313a5-5a2f-3a63-9453-8d52591b685f | -3.93485 | -50.44322 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c9b20ad-4dfa-3cad-8bcd-d9baea216c6c | -5.75441 | -45.11443 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27d5e5a9-3102-357a-a45d-cb8b873b118b | -3.40393 | -54.57732 | 2025-11-28 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 446561ee-eb4b-3e0d-8a2b-342ed96bc992 | -3.59162 | -49.46271 | 2025-11-28 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15077131-7407-3b3d-9391-2e86cea67dc2 | -3.2324 | -50.14347 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4ca27f3-7dea-35bb-8ea8-39161e8c6d56 | -3.71246 | -53.37854 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f44e6984-5a04-32da-8ab0-c1fef48df61b | -3.52471 | -51.63447 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04b8e18c-8859-3617-a539-7b977f5ef879 | -3.30988 | -53.18443 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c8a3e31-d3de-3e51-9a8e-5acdc100f9f4 | -3.03167 | -50.97499 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5c1f49a-aa4c-3ca8-9e64-7512a4bcba52 | -2.96305 | -51.02399 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dec775fc-0823-3093-8012-402df5a92bdf | -2.59047 | -53.96949 | 2025-11-28 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06e6d648-c81e-3b54-8c2b-9996543fe86c | -3.58849 | -52.05675 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9bc5b8a-e4d3-339d-9054-d60ba9374628 | -2.71921 | -53.17659 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfe4fcd3-591a-3125-a6a7-65c31c93d5db | -3.84632 | -47.03823 | 2025-11-28 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5ad731f-3c4a-3e60-a14a-a954bd5f4946 | -4.31934 | -44.05396 | 2025-11-28 05:01:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 947bf57a-7f27-3265-b25d-16c5f9a9386e | -4.7847 | -50.48721 | 2025-11-28 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 307d48c8-525c-3103-a11e-0ac96262eaf0 | -2.80166 | -51.90688 | 2025-11-28 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44f274c6-9276-3148-879a-13980a6ab2a6 | -3.45977 | -53.07322 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a03968af-f7c5-38be-bf6c-930ca931616c | -5.44599 | -44.68573 | 2025-11-28 05:01:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 746ebe7e-2fdb-3115-88b7-ba6f0195f16f | -3.35832 | -50.48978 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 263f77db-1989-3e0b-881c-f6e0cd2329e3 | -5.74955 | -45.11065 | 2025-11-28 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70432136-4daf-3b37-a388-6fbd6febafdb | -5.57873 | -44.58295 | 2025-11-28 05:01:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8a6537f-08a0-31bf-869b-6a03ef35503d | -3.25087 | -50.02322 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf9f9bc6-e12a-3f2a-9ac0-48f87d78079a | -3.39289 | -50.52876 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6afc5777-58a4-3077-932a-611404c60d19 | -3.75214 | -46.95275 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 515dc2d7-fe92-3fdd-ae07-e61bed332ed5 | -4.27451 | -48.71663 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1955c9f3-dc61-3f01-b4f9-16e3dec9c650 | -2.3667 | -56.11357 | 2025-11-28 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89470ecf-29d8-36dc-89ce-a59f15bec469 | -3.03807 | -50.97999 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6ab75d7-16c7-3abf-8c11-f05a0f3d0581 | -3.22197 | -50.79297 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0b32ff2-3541-38e9-84c0-1bdede529834 | -2.89988 | -54.00374 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37287983-2c71-3b27-9516-33df8632c9c6 | -4.29661 | -55.61427 | 2025-11-28 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbed1df1-d099-3d02-a2e8-429876b425c2 | -2.3696 | -56.11819 | 2025-11-28 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed542096-2a0a-3da7-8d8c-5a3f72897fb9 | -2.89759 | -50.49637 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d409037-6f20-360b-b649-636d5897a4e9 | -3.76505 | -46.95926 | 2025-11-28 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e933af2b-b95c-3c31-bfd1-6af3933756f1 | -4.97112 | -50.87748 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdaa64e7-d019-36e8-97f2-66874d3bdbc9 | -3.56402 | -53.03259 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00a46197-9dc2-3041-8ccf-2cfb1d58b802 | -3.44915 | -50.54581 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f9ed472-0502-3fa4-9732-883c0f4cd1fd | -4.06283 | -49.43728 | 2025-11-28 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50c8f0cb-872a-35c9-be22-de2e2fafdf12 | -3.66891 | -45.40396 | 2025-11-28 05:01:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fc6df6db-1b42-3040-91ea-57c303de9604 | -3.36101 | -50.48744 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fea4309f-e34e-31af-acc9-e19c9a333a87 | -3.40691 | -53.19256 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe870c3-1f9a-3bfd-b714-d688c6108f9e | -2.43273 | -53.83086 | 2025-11-28 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa20ca65-01eb-3b7e-8f46-f31552169041 | -5.58474 | -44.58004 | 2025-11-28 05:01:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3b7b02f-5601-3d98-93e1-b5e982c5c823 | -3.93541 | -54.72593 | 2025-11-28 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8837b96d-a346-345b-acd8-7da9c64b8e8d | -3.40672 | -54.58137 | 2025-11-28 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30cc5ae3-e8f1-356d-94d6-9c6bc5fb7049 | -2.7148 | -53.18297 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91d161fb-b159-3401-9f74-5c50a53fab34 | -3.83252 | -50.18556 | 2025-11-28 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd14ffba-87cf-3439-9a3e-50acbb85f6db | -2.37026 | -56.11416 | 2025-11-28 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70062a9d-0d0c-311a-914f-667faefea989 | -3.3693 | -50.82261 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a79a4ebc-d457-3d0e-b438-c41830984160 | -3.39352 | -50.52465 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98d7dd06-5157-3030-8f74-e7f5b3f22f5f | -4.97535 | -50.87393 | 2025-11-28 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac9c0dc0-a25b-3cb6-8a0e-3ef67a13fedb | -5.4455 | -44.68915 | 2025-11-28 05:01:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf26368a-aa89-3a33-af17-bd1bf2488d37 | -3.44851 | -50.54988 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fafa725-ebb0-38da-8430-fa3ca94df8d5 | -3.74005 | -53.35456 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9590d371-954e-336a-9acc-a7c159433158 | -5.13134 | -43.02328 | 2025-11-28 05:01:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89883a99-e17e-3f21-96f6-d3e5ee582f26 | -3.03869 | -50.97608 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77ac592e-4ff4-36eb-9f52-774e30312f14 | -3.48144 | -52.15855 | 2025-11-28 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c128913e-6082-39f2-9139-c66919fa5db2 | -3.68012 | -52.5349 | 2025-11-28 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed9ad95-0de3-382e-973a-848a8010d197 | -3.35207 | -54.09276 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17c26766-c66f-3cab-8a9c-97bc39a6c897 | -3.45994 | -50.54747 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10efd6a7-7c15-309b-b1c6-d564ea8c27a8 | -4.30445 | -48.60077 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09732a82-03d1-3bae-9b2c-5fb10621b4f5 | -3.40337 | -54.58084 | 2025-11-28 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
