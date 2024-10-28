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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5824d72e-e6b7-3515-80f9-8a292a448a01 | -4.9496 | -43.2078 | 2024-10-28 13:55:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 515dceaa-5abd-322d-8bdf-dbf4e20d338b | -6.0782 | -44.719 | 2024-10-28 13:55:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 516756f9-5135-39a5-8665-ad9f0c592cf0 | -6.6813 | -40.8958 | 2024-10-28 13:55:43 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 069a3a18-db4e-38a2-8a5a-395fecb2d104 | -6.6765 | -43.0491 | 2024-10-28 13:55:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 35f443c3-37cb-3c4e-9bba-b4e7a28eebd4 | -6.6767 | -43.0255 | 2024-10-28 13:55:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 9f16d69f-13ee-326b-8a53-cbbcc8b56c3e | -6.9593 | -41.3296 | 2024-10-28 13:55:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| b785e44f-d9bf-3f44-acb8-235d4b9b4d8a | -7.3912 | -44.7216 | 2024-10-28 13:55:48 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 88334882-455f-3993-bfab-2b1221931cab | -12.8883 | -44.6143 | 2024-10-28 13:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d1d6758c-315e-3fba-9af3-35c22e779e56 | -13.1898 | -43.0957 | 2024-10-28 13:56:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 7747c79e-41d3-3acb-b60f-8294e4eb994f | -13.2087 | -43.1162 | 2024-10-28 13:56:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 75e607f7-c4d5-30e5-9b43-2e8c84ac2b65 | -13.2874 | -53.7248 | 2024-10-28 13:56:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 61b02af2-c7b2-3f17-bb4c-3d403aab4e07 | -13.2877 | -53.704 | 2024-10-28 13:56:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 4fbb1402-dcc9-3296-a452-74a4e94902aa | -1.0243 | -48.83 | 2024-10-28 14:05:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f2da5a45-48f7-310c-83f0-1f9d4e0cc44d | -1.3743 | -49.273 | 2024-10-28 14:05:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4577e179-d038-374a-b69b-4f84e920aa2e | -1.4892 | -47.2035 | 2024-10-28 14:05:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| df0e38de-6906-3976-94a5-9624542f76a3 | -1.4944 | -54.2763 | 2024-10-28 14:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 576fb3bf-89bb-34c2-8f25-634e44dfdc04 | -2.1878 | -48.8104 | 2024-10-28 14:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0a6b3bb2-049e-3d2b-bae0-f89f9d618fc1 | -2.2703 | -46.1068 | 2024-10-28 14:05:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| fe9ded07-37f8-3357-96f5-f5e75e4b7c21 | -2.3578 | -47.6641 | 2024-10-28 14:05:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| e833b4dc-a618-3c0b-8c38-946121f38665 | -2.3055 | -46.6591 | 2024-10-28 14:05:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a4f853fe-ec6d-35de-9efa-68e51438853f | -2.3919 | -48.5484 | 2024-10-28 14:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 182.8 |
| e2ee5bfd-41c9-30fd-a353-ad2c89a6cd6b | -2.4288 | -48.5474 | 2024-10-28 14:05:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9fe01483-a47f-3ecc-a2f9-4e1effed44a7 | -2.8885 | -49.2397 | 2024-10-28 14:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 169.9 |
| ff4b1cf8-9dba-3c36-878d-c4930ac410e1 | -2.87 | -49.2402 | 2024-10-28 14:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 325.0 |
| ebdf4f1d-5834-3cd4-a862-fc9313696f48 | -2.833 | -49.2413 | 2024-10-28 14:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4e1f852d-103a-3ed9-ad34-632dbeda8cc3 | -2.8515 | -49.2408 | 2024-10-28 14:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 5cf00077-44e4-3cd0-9581-6441c9335ecb | -2.8977 | -57.6823 | 2024-10-28 14:05:23 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b5e6e381-4417-3c80-995a-50f27c712423 | -3.8225 | -44.1522 | 2024-10-28 14:05:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| ba312ff4-9852-347b-831b-6b55dfad3b76 | -3.8412 | -44.1513 | 2024-10-28 14:05:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 89ba2148-e54f-3688-85ff-401f35f7d820 | -4.447 | -42.8889 | 2024-10-28 14:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c2ac5ec8-e248-3b88-b02d-c13c77e0f912 | -4.8432 | -42.4634 | 2024-10-28 14:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 93167ae4-e838-3f7e-82de-bb1e3c1114e7 | -4.9496 | -43.2078 | 2024-10-28 14:05:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0c787237-b0eb-3150-8657-fa6c8c7ca400 | -6.0423 | -42.5859 | 2024-10-28 14:05:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 894f4b2a-a423-3990-9a2c-8831adc803f9 | -6.2248 | -41.279 | 2024-10-28 14:05:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| c4dc55f4-9b4f-3129-8678-80d57c81191d | -6.6228 | -42.7951 | 2024-10-28 14:05:43 | GOES-16 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 09442cd7-cb84-3e4c-b5d3-eee2a31c5ccf | -7.3912 | -44.7216 | 2024-10-28 14:05:48 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 8ad38e4b-eed0-3adc-b67a-804b13b15aba | -7.41 | -44.7198 | 2024-10-28 14:05:48 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f27dbc48-b19b-3605-b0ba-040a488242f6 | -12.8883 | -44.6143 | 2024-10-28 14:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5c38865d-e6b3-366a-8205-01dbb207d690 | -13.1898 | -43.0957 | 2024-10-28 14:06:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 7c01869c-9161-36c5-9a8b-f498c2b7f815 | -13.2685 | -53.7062 | 2024-10-28 14:06:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d5a4f55d-9075-37de-a62e-14c61e71cdcb | -1.0243 | -48.83 | 2024-10-28 14:15:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3708cfdd-30cc-3496-919f-980f46474bad | -1.0621 | -48.2506 | 2024-10-28 14:15:12 | GOES-16 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 2aff17d4-1911-3285-8687-a1d88f7669cf | -1.4396 | -54.0966 | 2024-10-28 14:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ed3f5146-58ce-3365-99ac-7d446a1b7b08 | -1.4213 | -54.0767 | 2024-10-28 14:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8703e7dd-9edc-397e-9de1-bb775ca3247d | -1.4397 | -54.0765 | 2024-10-28 14:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| e5137a89-f05c-3b4d-a01f-1e69014b136f | -1.4892 | -47.2035 | 2024-10-28 14:15:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| db3445e3-7944-363f-9880-a6c0abf4dda6 | -2.0599 | -55.7792 | 2024-10-28 14:15:18 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b26b439b-397e-393e-bb85-1ce5c5b79dcd | -2.3578 | -47.6641 | 2024-10-28 14:15:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6dbfc05b-1f7d-3569-b591-e5d3dcb85f96 | -2.3055 | -46.6811 | 2024-10-28 14:15:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 484eeeb4-bd13-3f26-8579-4ec27dd6587e | -2.3763 | -47.6636 | 2024-10-28 14:15:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 711527f8-8dcd-3588-b746-7e78b959f66f | -2.3919 | -48.5484 | 2024-10-28 14:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 07dcea33-316d-3773-9dc3-beee7e64d484 | -2.3055 | -46.6591 | 2024-10-28 14:15:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| d834a893-c011-3c0d-8298-6cd6b462367c | -2.4104 | -48.5265 | 2024-10-28 14:15:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5b832b15-9635-3eb8-b8c0-25d11c3e4d44 | -2.8515 | -49.2408 | 2024-10-28 14:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 4db6aa2c-48fe-3abf-813c-a1e5a542c36b | -2.8885 | -49.2397 | 2024-10-28 14:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 4a331248-a805-30d0-83c0-81a063abc6c9 | -2.8146 | -49.2206 | 2024-10-28 14:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 297a1e2a-6633-301c-b00d-b09f77005630 | -2.87 | -49.2402 | 2024-10-28 14:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 296.5 |
| 8ce5bb5b-c6f6-35cc-bfc9-5cac3a24379a | -3.0734 | -54.167 | 2024-10-28 14:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3e93d7bc-c7fc-30b3-857a-e82bbc04dd8c | -3.0917 | -54.1666 | 2024-10-28 14:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 27b0d78f-7247-35d9-8bbe-3d40f8a710c9 | -3.3986 | -43.2714 | 2024-10-28 14:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 6d5c7ced-0231-3995-81b3-ebb634c4a4b4 | -3.3891 | -41.6201 | 2024-10-28 14:15:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 1d87334c-962b-3ff2-9582-674281496b18 | -3.5775 | -44.6436 | 2024-10-28 14:15:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 9bf41b69-cb6b-33aa-ba44-c536a12936ec | -3.8225 | -44.1522 | 2024-10-28 14:15:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 00b30dc1-fa8a-32a1-a138-5f903f661160 | -3.8412 | -44.1513 | 2024-10-28 14:15:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| a24df8eb-c009-36d2-a9c1-d8d8229693eb | -3.8411 | -44.1742 | 2024-10-28 14:15:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 90ece965-7296-3a49-8822-f8b2f3ecacb8 | -4.3695 | -43.2674 | 2024-10-28 14:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 84486360-b2d9-3aac-85b2-c4e121658055 | -4.8619 | -42.4622 | 2024-10-28 14:15:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| b50329b8-a354-30b7-9ece-131cac534902 | -4.9498 | -43.1845 | 2024-10-28 14:15:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| bc327570-d8e3-3947-8f92-9aaadad7fc14 | -5.0832 | -42.8945 | 2024-10-28 14:15:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 4e3fa7fa-9f0a-3a62-9d83-b2fe19e728a2 | -6.0611 | -42.5844 | 2024-10-28 14:15:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| e02c7445-8778-36e7-9732-628fa8ee2f89 | -7.205 | -42.9051 | 2024-10-28 14:15:46 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 9ffd096d-d4ed-366e-98aa-0a9ea193cbae | -7.3912 | -44.7216 | 2024-10-28 14:15:48 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 36224060-8e71-3d90-befd-57af4d680ced | -7.41 | -44.7198 | 2024-10-28 14:15:48 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4f638d42-ac09-3095-ad26-d0536c3b05e0 | -7.9756 | -38.8836 | 2024-10-28 14:15:50 | GOES-16 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 59c9eae8-05ae-3a0f-8007-d55d5363dff8 | -12.8883 | -44.6143 | 2024-10-28 14:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f196a7e9-f5a7-3ca5-947e-88c0f16a166a | -13.2877 | -53.704 | 2024-10-28 14:16:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ab40c9fa-a939-3bac-9e35-1c3b3350d7b9 | -23.836 | -55.3114 | 2024-10-28 14:17:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 063e7dbe-3e5b-34e0-8bca-3c7dae712dc2 | 1.6385 | -55.8244 | 2024-10-28 14:24:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 1ffe954e-7e46-3c09-ac57-4445c9569ff3 | -1.0243 | -48.83 | 2024-10-28 14:25:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| b3743cce-0142-3431-b6d9-961c1aad3c04 | -1.4944 | -54.2763 | 2024-10-28 14:25:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 2634b783-71e4-3246-8b3d-6ce5aea13248 | -1.4892 | -47.2035 | 2024-10-28 14:25:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 59f6d90f-6246-3c2c-8cae-a56d8c668606 | -1.5262 | -47.2029 | 2024-10-28 14:25:15 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b0880a03-b4b3-3c62-8a65-98ec4f52086c | -1.8415 | -54.9901 | 2024-10-28 14:25:16 | GOES-16 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| e4768e7b-c5df-35f9-b5f7-1f69ee033f39 | -2.0599 | -55.7792 | 2024-10-28 14:25:18 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f039c9d8-8b73-3ce8-bf3a-33d2b5f10d18 | -2.3578 | -47.6641 | 2024-10-28 14:25:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 548d2f98-c7ca-3b6b-b3f4-627df1af89bc | -2.2664 | -53.7221 | 2024-10-28 14:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 2ab8ddf9-5be5-3913-9f93-f6a47168d190 | -2.3763 | -47.6636 | 2024-10-28 14:25:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| c1c6e365-070a-3262-a997-19c57ef21002 | -2.3919 | -48.5484 | 2024-10-28 14:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| e97798dd-d924-3efe-a2b4-8b4c2f570ac9 | -2.4104 | -48.5265 | 2024-10-28 14:25:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7893f1d1-fc0e-3472-8254-90d9ccc72cd9 | -2.8515 | -49.2408 | 2024-10-28 14:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 7fceb4e7-d97a-33b2-b6db-39b09dc77faf | -2.833 | -49.2413 | 2024-10-28 14:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 60a88b8d-14ba-322a-a752-e339dee55343 | -3.0734 | -54.167 | 2024-10-28 14:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 834db072-9566-3107-bbbd-41e56c404a37 | -3.2796 | -44.6565 | 2024-10-28 14:25:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7e608a3b-2aa6-3055-9738-d05bd8498e77 | -3.3891 | -41.6201 | 2024-10-28 14:25:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 32e0f9c8-e131-3fa0-8101-ce9ebb444522 | -3.5775 | -44.6436 | 2024-10-28 14:25:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 697cee15-c818-3ca5-8351-6359abcde185 | -3.8225 | -44.1522 | 2024-10-28 14:25:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 8eda2134-ef46-3e84-b262-6ef58623cd74 | -3.9961 | -43.2418 | 2024-10-28 14:25:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 76c1c08d-5326-30dc-be8e-69709ab3e8ab | -3.9959 | -43.2651 | 2024-10-28 14:25:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d413ca43-b5da-3dad-8fc5-237a4b409fb0 | -3.8412 | -44.1513 | 2024-10-28 14:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 32f1f800-a65d-33c1-9834-0e5af2f7383c | -3.9712 | -44.2365 | 2024-10-28 14:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |


[Clique aqui para ver as próximas entradas](README88.md)
