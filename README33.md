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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c96b37ee-03b1-356b-9be1-c092637bf3dd | -13.27845 | -46.97824 | 2025-09-26 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b20782-8e2c-32bb-86ed-8cd097878613 | -13.27763 | -46.97479 | 2025-09-26 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b9d0aa7-e075-3daf-8bc7-1c138236a28f | -12.03596 | -46.59223 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7b593af-23fe-3eef-beeb-bf9dd45183c8 | -11.79375 | -47.64941 | 2025-09-26 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a373fbf7-2e13-3555-a4d4-7937c5c515d5 | -17.03153 | -52.24118 | 2025-09-26 04:44:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| beb4600f-cc2b-35bb-8a98-7b314a323f26 | -10.63238 | -47.48119 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5eb9783-e49e-38b7-ada0-3691a0cb284a | -15.99028 | -59.4945 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed26773f-76d7-357d-aa3a-83e0dc6f05ab | -11.21846 | -45.56884 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 40c393e6-b444-3f95-86fe-4550c00a0399 | -13.64909 | -48.09834 | 2025-09-26 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b987f9d1-a219-3614-9044-7fbf332b6793 | -13.27878 | -50.70093 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cca4f6fc-d8c3-33f2-8634-7a358da228f9 | -16.22279 | -48.8007 | 2025-09-26 04:44:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dfad60f-e76b-3b0c-9843-e41a66c77587 | -11.42575 | -44.9879 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 856f07d3-8eb6-32c6-a716-c469a9ad2d49 | -13.85164 | -45.6049 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee29bef5-a074-320b-a67f-a3c539b0e607 | -13.24741 | -50.66704 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 38730b93-0d88-3b02-bbba-9e0e8fbfdc50 | -15.5134 | -50.42775 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d97fdf2-b19c-3fb4-87b5-883fa1f54fd5 | -11.69665 | -44.40055 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77c46cc6-dfd4-338c-a2a7-733cd7ac2fd3 | -12.53263 | -45.77005 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58738562-e28f-3b16-886b-2c64afd7aa09 | -14.10668 | -51.15395 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08dcaf86-8014-38f7-ae2d-7f7b10f79229 | -12.35649 | -51.20977 | 2025-09-26 04:44:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b601d953-d84d-3291-a996-36ff7a665620 | -11.42153 | -44.98742 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8bebc14e-9fb6-3d05-a296-c2f9bd9f4c4b | -12.00519 | -47.87871 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 991f101d-c345-3de4-9177-b09ddd9a00a9 | -11.97441 | -46.6284 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b527ac5b-b370-38fc-9a8c-de49c484a005 | -15.06584 | -44.98675 | 2025-09-26 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cd8093a-3b6a-3171-a488-d5fc0e600aaa | -11.65385 | -44.42308 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4deb1161-0577-36dd-af8a-5cf3c4e15517 | -10.62563 | -53.89034 | 2025-09-26 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd6715dc-5c66-3807-855d-53043105d899 | -13.85895 | -45.61381 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d7cf152-7eeb-3151-a47c-0a5b91cb8898 | -15.89867 | -59.33469 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a127891-53e6-3e4c-aca4-bf6aa565de14 | -15.40514 | -47.06307 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a2fada0-23a0-34df-a60a-45be004d4656 | -11.24256 | -45.54339 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d58bdc0d-bcfb-3f89-b811-b04f906a8462 | -12.87217 | -47.09797 | 2025-09-26 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc38cc89-e03e-3e88-ba8e-d9b0deaeb078 | -12.35593 | -51.21331 | 2025-09-26 04:44:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 040d1df0-9db0-3eb0-8a65-81b5e5ccdb29 | -15.90926 | -57.49206 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ca27b0f-3bdb-32e7-8350-4d70359ee72b | -11.04479 | -45.88356 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0182e813-31bb-3a52-8df1-7dfb0f6b535e | -10.54369 | -47.52848 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9616928f-83f4-342a-934b-68956713cc96 | -11.97125 | -46.6232 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58030a63-523d-331f-84bf-3d107c577ff8 | -11.00314 | -44.35151 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d10127de-ac1e-31c7-81bb-8ca89f1cc3af | -15.26721 | -51.46996 | 2025-09-26 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 956eec84-d2d2-3436-a636-2ad9ad6e59b7 | -10.94339 | -44.29721 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd34d7f6-7bb9-35a4-9ffa-6188dc4b64ad | -15.99153 | -59.48813 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1b35d21-cf82-37fb-a1d6-9ac1fbecd4c7 | -15.27419 | -46.43069 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc6e588-d9e4-3a2c-8f02-99f010740364 | -10.54551 | -47.51616 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8e7c41f-542c-3cd3-9132-8b68aed1caaf | -15.58736 | -51.69552 | 2025-09-26 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c7f725e-9b24-3a5e-ab77-38af8de4833d | -15.74678 | -59.51204 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea5bd1a8-4bd0-3e32-81d6-32cffd043d73 | -14.11058 | -51.15094 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74e63779-41c0-39c1-85df-22d7d5c6e000 | -12.84651 | -44.70884 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 934eff8d-e593-351d-a28e-8a237d36f56f | -10.48614 | -48.03578 | 2025-09-26 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3fb99c26-6ca9-3242-b4aa-305f5c78d77f | -13.24628 | -50.69604 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d2370a1-46e2-3ac7-b4f1-a2b4805afbd7 | -12.13551 | -47.94763 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 130ada73-9665-384f-8284-bbe6e2c971cf | -14.7747 | -60.19391 | 2025-09-26 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e47ae0ba-d058-333c-8a6d-f89d30a26cf4 | -13.97948 | -49.67617 | 2025-09-26 04:44:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37486477-2fc3-3dd4-8444-f399e57dd76f | -11.95885 | -47.88118 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 002280f2-c92c-3714-a05f-18a91be882c7 | -11.68249 | -44.40973 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85b26e8b-8201-3c9b-a207-cb9682e9defc | -11.61274 | -44.43026 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 002fa147-5135-3b18-a4f1-9ae13d7af6bd | -15.36464 | -59.16769 | 2025-09-26 04:44:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ba72510-d4f0-3fa5-8ec4-ed74e1a32cbd | -16.85463 | -50.4995 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7203204a-98b1-3012-bb35-9fb0f539cc34 | -15.36836 | -59.17396 | 2025-09-26 04:44:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15ee779b-1498-3957-b2e4-53fc09c76cfe | -11.60893 | -44.42539 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 882f2ade-ad18-3389-958f-f4c760bc8e5f | -14.55722 | -48.03558 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 202a84ea-dcf4-384e-810d-d191f5bc2d31 | -12.07071 | -47.99165 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df7d644d-dff8-3ec0-bed6-0410a8fa61d8 | -11.69553 | -44.40913 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a500e3a-986d-3d8a-b769-0615d5de7fcc | -11.96053 | -47.88423 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d97a19b8-6fb1-3e28-a63f-4f6d2ed6f5f5 | -15.5746 | -51.68968 | 2025-09-26 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3a42e67-22fe-3677-b7e4-daad0023d2ff | -10.44706 | -48.08189 | 2025-09-26 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 611a23c6-d3f5-37b7-adad-72679302635a | -10.45127 | -48.22002 | 2025-09-26 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b88e1f53-fa8b-362c-a30a-282fbd2198dd | -11.24561 | -45.55111 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 5b5304f4-d81b-389d-9660-e0c5cd08941e | -15.88355 | -59.33652 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b27b48b-be62-3e6d-b8e5-e070917d69bf | -15.38097 | -46.12377 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fae3dca-256d-388c-8cc1-a25b799b2e1e | -15.26778 | -51.46638 | 2025-09-26 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae1f081f-3730-3716-87f2-d0d5e69af163 | -15.10947 | -46.45903 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a0fba72-a3f2-3f4a-86be-3e4782ad2c3c | -12.96482 | -47.17846 | 2025-09-26 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eebbe7fa-e081-3e96-a79b-2ebcfb431b88 | -15.77223 | -49.93691 | 2025-09-26 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0308fee8-9fe3-376f-848b-4cb17dccfc06 | -14.78039 | -60.19196 | 2025-09-26 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a9ee7eb-e2b7-36b5-b2f5-7125927f20a2 | -11.96303 | -47.87767 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5c649589-02bf-344d-a276-87a4a247cfdc | -15.72908 | -59.4922 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 679b9fe1-b0d1-3f76-902a-3d7174e77a5f | -15.27015 | -46.43014 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c37550b9-eaad-30e3-9f6b-b79d9a644670 | -15.27771 | -49.47548 | 2025-09-26 04:44:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 503ac3bf-aa51-3569-af81-1bda45c4041f | -15.02767 | -46.94499 | 2025-09-26 04:44:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50b76d63-b5ee-3968-b967-484fcfa3cab3 | -15.27427 | -49.47486 | 2025-09-26 04:44:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1267aa9-175e-3d50-aa43-f61d2f0fece6 | -11.4263 | -44.98383 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 202d496e-cdb6-3246-9c6a-3f757238d30e | -15.51733 | -50.42462 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7960446-7ee7-319f-af87-1b0c388172ac | -10.58564 | -46.28509 | 2025-09-26 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e1866a0-94bb-3241-b99e-c5cdf14d4bdf | -11.40838 | -43.51122 | 2025-09-26 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4037a5b3-6be6-34c1-9979-f97b929b957c | -12.73069 | -46.82391 | 2025-09-26 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ab89f62-3f29-3228-9645-a4fbaf171d77 | -11.68097 | -44.45291 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 056b0219-07c0-3f6f-8aab-d5d8c3cbc74c | -11.64666 | -45.34197 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99062c2d-7897-34b6-a778-ec04e3e4bea6 | -11.70003 | -44.41218 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a84f562-91a2-310f-a066-8587c61e76e4 | -15.36456 | -59.16872 | 2025-09-26 04:44:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 234ad213-643e-3686-bda5-e1fe4cfbfbab | -15.9989 | -49.02958 | 2025-09-26 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| acc0646e-ad70-3816-93cc-ba757266f3d7 | -13.84695 | -45.60814 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0506d51c-6cce-3613-b179-e41ede1313fb | -12.13074 | -47.95516 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e8b6a54-bdb2-3f4a-9e00-97e7387e402c | -11.02115 | -44.34981 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ab9c36e-7143-3872-a470-3dc89103ef74 | -12.73537 | -43.45535 | 2025-09-26 04:44:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b215809-cfbc-3a7f-9cc2-52ae8ab7893a | -17.23553 | -52.40593 | 2025-09-26 04:44:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a6dd2a1-b372-3040-9119-67db2073e6df | -12.84784 | -44.7036 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aac7e09d-7448-3c1e-9802-60da0edfa226 | -15.51622 | -50.43192 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 21359652-3936-38bf-bef6-cf66ac1fee9a | -15.26388 | -51.4694 | 2025-09-26 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6d63dc7-cbe2-317c-84af-84f6c230452e | -13.91752 | -46.85886 | 2025-09-26 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a2c3d0b-aa09-352c-97b6-2b96b270a943 | -11.21751 | -45.57573 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f3fff9e-a435-3e0f-b824-f6ab4c953e62 | -12.03401 | -46.59417 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04862796-c673-311e-a464-ca4ca2228dd3 | -14.98419 | -50.057 | 2025-09-26 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README34.md)
