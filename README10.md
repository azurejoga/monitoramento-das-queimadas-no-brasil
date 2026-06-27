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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c10d1bd-f8cd-3728-bbc5-d6c8093e4575 | -7.30242 | -49.62273 | 2026-06-27 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ea31d09-b9c8-36ed-aee6-9e95a834ba0d | -10.5533 | -46.24786 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e6e2256-79b8-3f76-97c9-a1d57c203c5a | -6.97173 | -42.89436 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3ce58f4e-32e9-3f24-ad34-aa3cd5b091ee | -10.62502 | -50.22418 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ac1da55-6247-300c-a6d7-766af8cdc39a | -6.90402 | -43.68674 | 2026-06-27 04:12:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e28c9178-8edd-38af-8caa-bfe48c2c8a7c | -10.55262 | -46.25179 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ebe46bbe-63cf-3b9e-a30a-ef634f147c41 | -10.77139 | -46.47139 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0161e946-5af6-3e39-90d4-a45ee628669b | -10.69225 | -50.24423 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 175b48ce-b4bb-3cb3-a5c6-afbb52f090ea | -10.35505 | -47.33626 | 2026-06-27 04:12:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0a52d3c-f316-33ca-bd01-1b3525837aba | -6.97944 | -42.89154 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2f4559fc-5c20-3e85-887f-60811b44958d | -6.9788 | -42.89548 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1c4fc532-d877-3b38-ac98-abff63c7edf2 | -6.98297 | -42.89213 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| beb99e9e-3b11-371c-82b6-42f476978da0 | -8.86798 | -46.93214 | 2026-06-27 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0f3be6f-c149-3add-a4ed-5e176977cdb2 | -10.6269 | -50.21434 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9ed2e0d-0edb-3255-b379-e280dbcaa8e2 | -7.74521 | -44.17744 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a34d9eb-dfa6-30fa-bdc2-f175a853e2df | -5.78515 | -45.05902 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c9710f5-6378-3f3d-9cca-c226756df504 | -10.63216 | -50.21538 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92ff0d75-2724-3ce9-b708-2cf1351a346a | -9.06403 | -44.75315 | 2026-06-27 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 319dcb1c-412c-3ade-b72a-285f410c1c87 | -5.95185 | -43.49244 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1c688a-8c6d-34e6-8f7e-2f939e344798 | -7.49585 | -43.38828 | 2026-06-27 04:12:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f13f4885-62a3-3a03-939b-694db17c7aca | -5.78051 | -45.06194 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31fd3482-1588-3758-bd60-2984f3f968f8 | -7.71764 | -44.15889 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c601942a-3afe-3a8d-877f-50a4ce20d98e | -7.74448 | -44.18183 | 2026-06-27 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 75c51eb8-8110-38fa-9140-b3a28cf18ec1 | -10.47543 | -47.08871 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c38a84d4-56a0-3920-890a-2a3c511b287b | -5.78803 | -45.06678 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c7d38ca-bd9a-396b-ad47-3518a42828e4 | -7.62848 | -47.30056 | 2026-06-27 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d14a8d9-0e2e-3258-a030-b4e90830a298 | -10.55733 | -46.24871 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50963e1c-47a4-3347-bf52-782f6bfcd444 | -10.7755 | -46.47207 | 2026-06-27 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1d3d8b0-70f9-399a-80eb-9e1e98df0257 | -8.86873 | -46.92787 | 2026-06-27 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91a1fafe-12a2-3446-bf90-c8a07f1993e1 | -8.67824 | -47.85096 | 2026-06-27 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a570199-c8c6-347c-9409-b63147df5352 | -7.00159 | -42.77809 | 2026-06-27 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07682f3f-3f60-3372-bebd-b62d04182941 | -9.08138 | -44.76585 | 2026-06-27 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f1bcbb3-1cef-38bf-bfe8-09a21bcf88e8 | -9.47401 | -48.06993 | 2026-06-27 04:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bf04366-048a-3d8c-8024-eea1318550d3 | -7.00446 | -42.78259 | 2026-06-27 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eeb47f85-7b13-3018-aebf-e03995b79b63 | -8.31294 | -47.11863 | 2026-06-27 04:12:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58a120c9-3efe-3fed-bdfc-91a8e76044b4 | -6.98233 | -42.89608 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 96f14d5a-ec75-3d0b-81e5-48ad97690d89 | -10.62439 | -50.22746 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8bf3ef6-6c09-308f-8f83-11a86d655de1 | -5.77992 | -45.06551 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 248bc0ad-f2b5-3900-80b1-3797fd9d439e | -10.48039 | -47.08568 | 2026-06-27 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d59b4aef-a1e9-3c8a-95d0-4bc5ef73678b | -5.94817 | -43.49184 | 2026-06-27 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10fa2370-b6f4-3cfc-9a42-70320bd6bbcd | -6.97526 | -42.89492 | 2026-06-27 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9b872983-312d-3378-960c-730e3393d988 | -5.77645 | -45.0613 | 2026-06-27 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8eb0d19d-ff4a-3546-b4c8-a8983ad34866 | -13.43515 | -47.86563 | 2026-06-27 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a568ab4-88f5-3b38-a001-d65934d7022e | -10.53958 | -53.71954 | 2026-06-27 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed0cce8b-c756-3e2d-8292-da44e56223f8 | -11.04632 | -52.46434 | 2026-06-27 04:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed67ffc8-b484-380b-89cf-337d5910c5b4 | -12.79453 | -54.86701 | 2026-06-27 04:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be704f7d-9779-3dbb-93df-65e75395679d | -12.82497 | -44.35281 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4f01b0de-15fb-382d-b2c3-b384069cc812 | -14.87472 | -54.53122 | 2026-06-27 04:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ac7bd1a4-cf44-343b-969e-828fd09036b3 | -12.82715 | -44.36156 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a37ab36-1467-370c-8b2c-a043497fb949 | -15.58931 | -46.8135 | 2026-06-27 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d2b1845-593d-3b70-bf71-b808132eb21e | -14.84508 | -48.14629 | 2026-06-27 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4d2f654-be17-375a-83b3-fdea954bb5bf | -11.7881 | -46.47345 | 2026-06-27 04:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 343e6b24-f632-3900-9611-b43bc9dfd719 | -17.00644 | -49.03231 | 2026-06-27 04:14:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9265e8d-a853-3a01-9794-cf4ebd5a2f44 | -11.7834 | -46.47648 | 2026-06-27 04:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3181ffb8-1431-3e9b-9043-014de2fc3065 | -15.58542 | -46.8128 | 2026-06-27 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 490e7fdc-5dca-3954-a529-4dd4328ec971 | -12.82851 | -44.35345 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f4d73743-3ce4-32b5-9287-653e4e97a047 | -13.93921 | -47.33445 | 2026-06-27 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2e40509-3ee1-3cdc-8f42-7ca27c837e84 | -11.64487 | -54.90268 | 2026-06-27 04:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd99e89c-3aab-3768-9c4b-59e7b074b083 | -14.8458 | -48.1424 | 2026-06-27 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2e35687-e6d7-3677-9554-a5a0065c44ea | -12.83627 | -44.35061 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 015c6e5a-6521-33ef-8db1-c5af510f5eba | -12.44832 | -49.58152 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07638d94-e5c0-3fd8-960f-6dca096d6779 | -12.44729 | -49.58708 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3fcfdbd-2271-3df7-b61f-6a80bfc08c0e | -12.44343 | -49.58061 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4156616d-0f20-37a9-9ed0-d1d18f9d103a | -16.7514 | -45.81511 | 2026-06-27 04:14:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c30051da-8472-3134-8460-0f2d4e3f29ee | -13.66463 | -53.93938 | 2026-06-27 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9b19a43e-8891-34e1-bd7c-bde9fd01e770 | -14.84935 | -48.14704 | 2026-06-27 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db05b8e5-bef4-3563-a9ff-687fca0499c4 | -13.24817 | -54.41462 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7b5e1ec5-e75d-3e7c-8442-d6c6ea2f7765 | -16.52612 | -47.737 | 2026-06-27 04:14:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8822476-dc1f-33e0-a005-660a808658b2 | -13.83575 | -47.14284 | 2026-06-27 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5511224-5bf1-3d52-af74-2d74efedd4f0 | -13.26237 | -54.41186 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48893af2-3207-308f-a8ef-f441f61274fe | -14.70003 | -46.15155 | 2026-06-27 04:14:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcb45cea-3528-3587-9abb-425fc5edb772 | -13.87981 | -47.17213 | 2026-06-27 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50159136-745c-3027-8b96-156bc75e29ae | -12.8398 | -44.35122 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 129fa530-9538-3a8b-b3c5-3de39850ab95 | -12.83694 | -44.34655 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee9dc3f2-b79a-3d76-877a-dde0b894bcab | -14.69788 | -46.14817 | 2026-06-27 04:14:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49e61d99-e64b-3695-9507-bad63e8d49fe | -12.45219 | -49.588 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd260963-f84c-3abd-bce3-111ee5088d8d | -12.4469 | -44.75596 | 2026-06-27 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f2642d-6d40-344d-8bf0-c8fd6c786fa2 | -13.22661 | -54.42717 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc5ef728-bb18-34a4-a194-034efd472ee8 | -12.43852 | -49.57972 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75452a39-f70d-3de5-b7e9-f427ab6038f2 | -11.78571 | -46.43977 | 2026-06-27 04:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1320ce3b-55a8-3c27-b5b5-cf51ac478bdf | -13.65837 | -53.93791 | 2026-06-27 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a50155d-5c6a-349f-b352-5bbb06e60acd | -17.82057 | -44.16673 | 2026-06-27 04:14:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75685aa3-7b53-363d-8b1e-b9646745dcd3 | -13.64601 | -55.29212 | 2026-06-27 04:14:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36ed7c19-b8ef-32bf-8373-0f7d39444aaf | -12.82211 | -44.34813 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f920dec-8cc3-3b86-b2e0-4ab398f89c00 | -13.25712 | -54.40451 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caf8d809-39e3-38a1-84dc-4d01e9d7e665 | -11.64625 | -54.89615 | 2026-06-27 04:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b2118c2-f0e3-364e-ade5-866925e6df05 | -13.9433 | -47.33534 | 2026-06-27 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 521004b1-50c4-3481-9d66-3aea28ed2211 | -14.61018 | -48.00606 | 2026-06-27 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102c5a14-6954-3d1f-be45-7232abbd0d8d | -15.58632 | -46.80786 | 2026-06-27 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e119869-715b-38d8-a066-0c5624692b90 | -13.65071 | -55.29929 | 2026-06-27 04:14:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af9574a4-b150-3a9d-aa11-6e39faf4dbd2 | -12.82986 | -44.34533 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a2e2d9ac-31dc-3fee-ab69-f251d423f554 | -12.83641 | -44.37156 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e5438d9-7c84-37a8-8bfb-d820a66b04f5 | -13.25588 | -54.41034 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3b6d309-dc65-389b-9d6d-d4012695f362 | -12.44003 | -49.58138 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffcb8a89-1158-3002-95f3-5f69da6abb3d | -12.83205 | -44.35406 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 926ced0e-f798-3736-9c28-8a56ea6a9d03 | -14.6987 | -46.14349 | 2026-06-27 04:14:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cac4a875-a577-3ee3-bb61-2282fc8c62d4 | -13.83643 | -47.13904 | 2026-06-27 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cd9f064-4dd8-3742-bef7-b47f69b37c0c | -12.83559 | -44.35467 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cd50d48-6b47-3ad8-b701-59c1cbbe5ba8 | -19.10998 | -44.6354 | 2026-06-27 04:14:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4e453a9-934a-30aa-b985-fda1c1e91dd8 | -15.5902 | -46.80855 | 2026-06-27 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README11.md)
