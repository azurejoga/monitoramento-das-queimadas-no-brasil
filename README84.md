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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35b479e2-a7fa-3c01-8cee-2a87a0466196 | -16.81658 | -57.45462 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 66638c52-9074-368b-bd70-7f3bd61b1b86 | -16.81619 | -55.90512 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b8ca7726-e5bf-3105-b60e-9a54628d9632 | -16.81561 | -55.89754 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 338f4296-f051-3269-90ec-fc3811db2f2e | -16.8155 | -57.45964 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| edba1e33-1d46-3eb8-8259-71662fcc1a7a | -16.81479 | -55.90154 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| efb4c676-9361-326b-a55f-6fd46a0cfe96 | -16.81398 | -57.45449 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 06564565-b9fb-3dcd-ae6f-39c5a3af9e14 | -16.81396 | -55.90553 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 20111678-74e6-312f-a910-6d4559e2560b | -16.81319 | -57.38041 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 20d7ea55-3f7e-3104-b245-259988f00ca9 | -16.81311 | -57.82392 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cbf18c92-9c36-39fc-815f-6557ca719b90 | -16.81212 | -57.38537 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e758980f-f29c-333e-b971-c803b7c7d327 | -16.81142 | -57.82201 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c8f5b9c6-0a6f-34b6-9a26-3b7abb27db8d | -16.81105 | -57.3805 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8988d2ed-0b3c-301c-9008-b496425d3508 | -16.81026 | -57.82729 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 118c518c-9b4f-37de-bdad-43db92943b7f | -16.7899 | -57.47504 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4ef0bf73-a817-34c3-8fb7-84381a4ea2f5 | -16.78797 | -57.43707 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c4699d92-832b-3845-ad0b-5cc27464158d | -16.78688 | -57.44209 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b4212f23-7687-3453-bd96-e9e8723e2f1a | -16.7865 | -57.47369 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1ee9daeb-2c63-3f33-9035-04f7c265b9eb | -16.78373 | -57.47356 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 83d3fb78-e173-3aaf-96ab-51c7fef2673c | -16.7826 | -57.47857 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4b722c02-a168-3cea-a061-b79aa463fcd8 | -16.78158 | -57.83695 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 83d9d23a-68f0-3028-9ba6-077d6aef63c4 | -16.78103 | -57.49887 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 10b3c367-8a00-39dc-9bbf-e73b1f9d42c1 | -16.78041 | -57.84225 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 615c790a-24db-3344-844f-ad80491164ce | -16.78035 | -57.48859 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| effbb69f-304d-3653-b352-d2abd6c75067 | -16.77924 | -57.47721 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b2339a42-445d-3e1f-873b-99b2e58ad0fa | -16.77921 | -57.49364 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2402ee02-9ce2-366f-ab80-68bef22f787f | -16.77814 | -57.48223 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 136735cf-1f6a-396b-a909-048b562dea6c | -16.77808 | -57.49868 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4078f5d0-79f6-3980-b6e3-2c2c68493550 | -16.77705 | -57.48726 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 9d98e364-5f8a-3bd0-81c9-a06539c62c09 | -16.77485 | -57.49737 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f945ba01-08a1-3905-b298-0b70a68da577 | -16.77347 | -57.44409 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d57be6ec-ffcf-3b43-9f93-90cff6a636b7 | -16.77238 | -57.44909 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2a2520bf-2111-32cc-aaac-2208b1ec003a | -16.77087 | -57.48576 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6c3491e1-2f34-38df-b74e-09f26e236dec | -16.77019 | -57.45914 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b9db1421-96a8-3b13-95f8-186fcb3c317f | -16.76978 | -57.49079 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0793868f-19d8-3bf2-b28d-c0c299cf4c68 | -16.76867 | -57.49585 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 35fafca2-e869-316c-aa05-87100d0042b0 | -16.768 | -57.46916 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ae8e4610-d0a5-39eb-a3bb-df3a5228c521 | -16.76731 | -57.44259 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c4d25300-204b-30d9-95dc-76929f829dcc | -16.7669 | -57.47419 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5e9cd37d-b70f-3a7a-aaa4-cc5b74c1ee24 | -16.7658 | -57.47921 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4f5323f9-2e36-308a-a87e-02839970d683 | -16.7647 | -57.48425 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c98dca6e-bd79-314f-9186-b15f775b2e2d | -16.7636 | -57.48928 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0dbc0715-6fa8-3570-9db1-4aeef45a61a8 | -16.76293 | -57.46264 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1b356997-ff61-3367-adbd-98630f682be9 | -16.7625 | -57.49433 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f92e7d1b-3016-3798-9457-5e4a33f22765 | -16.76182 | -57.46767 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 26e45e36-e16f-30aa-a411-7252c0f26724 | -16.75742 | -57.48778 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 67551310-1312-39d9-b0fd-d87878b70fc5 | -16.75675 | -57.46115 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2adbe057-28e9-3807-bf5d-7594b907ca4b | -16.75632 | -57.49283 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 6375e5cf-42b7-3c32-97b4-79f6365d023d | -16.75565 | -57.46617 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6559789f-a924-3536-a3ea-261e8c43e8e1 | -16.75521 | -57.49789 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 16158beb-7fe6-3db4-9e72-223514fa3076 | -16.75014 | -57.49131 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 17a10c3e-f94c-3dfb-9b33-746f6e4aea23 | -16.73493 | -57.47172 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e7062505-48b4-3418-b970-b64da214acb0 | -16.72986 | -57.46522 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9d579a02-ef73-346e-bf44-f54a450d8a18 | -16.71341 | -57.46215 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a293ccda-442e-31f8-9981-39246f33b198 | -16.70616 | -57.46567 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cb132958-501d-39fe-ad42-d840d1612af8 | -16.69889 | -57.4692 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8419e9e8-8ff6-34fc-b6f8-c4f0bc2c98b0 | -16.69787 | -57.4628 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 21dc3929-942d-3f70-a818-076f50a2ed8c | -16.69675 | -57.46781 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9d2cd184-18e7-34dc-a2e8-c60fc6b6d704 | -16.69381 | -57.46265 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 241f1dc5-c0f8-3cb5-bf88-bee6646ba118 | -16.69169 | -57.4613 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9f040d57-1c82-39f8-b695-1df18dd3c7b2 | -16.68855 | -55.49316 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f02c4655-7976-33db-9036-2de42e993f26 | -16.68778 | -55.49235 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ca448f84-af8f-333a-88c2-88cfcbad7b5a | -16.68776 | -57.44978 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 25671b6f-0337-30ec-8de1-d702a3ec36d3 | -16.68764 | -57.46112 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cddd1c0e-23d8-3b8b-9d81-02c040d2bb59 | -16.68705 | -55.49582 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 11165c19-c776-37e3-b4b3-9dbf556bf492 | -16.68664 | -57.45479 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7db3ac5e-74f1-3ca9-a138-4d34d4232afb | -16.68654 | -57.46618 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8fd316fc-51e9-3c66-a892-82702d8f501f | -16.68552 | -57.45981 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 49a46366-9baa-3e55-8ccd-c12858553407 | -16.68439 | -57.46484 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 71c856eb-ac30-3335-b45a-a65ff6c8db15 | -16.68364 | -57.44957 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c387437f-9e70-3c29-bf4a-5b6a1c8d071a | -16.68302 | -55.49206 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eec7a8f7-1125-3036-8ff0-e5c8514eefb8 | -16.68255 | -57.45459 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 40247ebe-025f-3569-8e6a-8a532b44acf1 | -16.68232 | -55.49546 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bd6c958a-10f2-3f66-9b20-21659e2a3bc1 | -16.68226 | -55.49126 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9ef23e9f-2ea5-352f-b363-fdc1df8d7d41 | -16.68154 | -55.49464 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cc5cd6e2-6cf3-3ff5-a01c-5ddab114a6e5 | -16.68146 | -57.45962 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e80f4432-4e65-3973-9147-d8e370ced706 | -16.68081 | -55.49804 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1a520ab8-2240-3aae-9fa3-f8e1f83040c0 | -16.68046 | -57.45332 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ef153c7f-3746-3e4a-9358-170efdcea7ab | -16.68036 | -57.46466 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9e83141d-a952-348c-836f-059d856b03a2 | -16.67934 | -57.45834 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 214c7034-a4a6-3d3a-bc55-297c10bbc065 | -16.67893 | -55.48397 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2f44c49b-f4d3-38b0-8b7b-224403376b0c | -16.67822 | -55.48314 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 357fa62e-4dd2-3518-b790-5c5f69b0b010 | -16.67821 | -57.46335 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a46851d6-15c2-3a59-88df-91f6a3c957e5 | -16.67818 | -55.48761 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c515c106-add9-3f61-ba7f-786f297519f1 | -16.67747 | -55.49104 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 44f28520-30b1-3435-a7e8-09fd06e5c6ce | -16.67744 | -55.48678 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3737cba7-90be-3289-9ef2-f31e6182e4de | -16.67708 | -57.4684 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 96a4d9d7-885d-3a2c-9238-9a0c9488ba2b | -16.67676 | -55.55073 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ff52a37a-37cb-3250-ba7d-d83130de732c | -16.67676 | -55.4945 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 61bdd6a2-a56b-32db-ace8-128146a43340 | -16.6767 | -55.49027 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3b1a1066-5946-3af9-9898-bd9be8bb302c | -16.67603 | -55.49804 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6138eba1-9a3d-323a-9083-30d1c169fdee | -16.67596 | -55.49375 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 84d7eb45-2a10-342d-87a0-e9709abb39fb | -16.67564 | -55.54958 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 32f27c4b-245a-3206-8406-a755ad8a5d0f | -16.67528 | -57.45813 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fd7783a6-7b57-3faf-b084-ef5843bcf716 | -16.67419 | -57.46315 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| eb88af8b-73ac-3548-9125-adeb470449dc | -16.67341 | -55.4828 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 02c8b067-4497-394a-a5de-db9bbd5c5fe2 | -16.67309 | -57.46822 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 17d32bad-9dcd-3751-a59d-c11b37bedbe8 | -16.67209 | -55.54537 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5f247275-c826-37a3-9579-4d36de1c0382 | -16.6719 | -55.49015 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 84429139-f63e-3f9f-876b-76fae03fd546 | -16.67128 | -55.54929 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0aac17a4-957e-30f0-a2f3-cf9ded023271 | -16.67116 | -55.49376 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README85.md)
