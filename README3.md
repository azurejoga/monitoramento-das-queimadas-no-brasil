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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8bbfe62-376a-3177-9192-01f55fd0db59 | -8.06852 | -43.13222 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0b354555-af8f-3f00-9fe7-9b9cb3da8072 | -8.05269 | -43.14186 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 97127971-8f9d-34d2-9b9b-e36ba07ded8e | -8.06989 | -43.12252 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b11f02a1-3ccf-3c13-bde9-10e8ddcf121e | -8.06129 | -43.13219 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8a9f32dd-4bbc-39d3-998e-b448e7d474e0 | -8.07804 | -43.11714 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6f9a927f-57a1-3fb9-9933-8987c6ec7a2e | -8.05457 | -43.13504 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 32b1d47a-a423-3e53-ad04-e655c736b4c4 | -8.05891 | -43.14767 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3b0354de-9bec-356c-b820-8fa42a5a7482 | -7.21057 | -43.12278 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| fa02950a-930a-3b76-a3ae-2629b63cd2a6 | -8.06309 | -43.12538 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b279aa30-f30b-3fbb-a5d9-d29a2bc7fd0d | -6.83988 | -44.62494 | 2025-05-25 03:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 73a315b9-dc25-31e5-9d7b-45e75c9c712b | -6.84155 | -44.62318 | 2025-05-25 03:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 846489bd-cd8c-3a3f-8777-3d574b00ff7e | -7.20098 | -43.12842 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9fd7bf5-1354-3b83-ba28-394bc83aaf5e | -7.21626 | -43.11968 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a8a30791-0642-3f70-9416-91ef70e9792f | -8.05353 | -43.14056 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a8fb0c25-ef0d-3c4b-afab-28a1e59fe855 | -8.05248 | -43.14613 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dbec8335-ed9e-3492-aefa-13b652faea7d | -8.06102 | -43.13643 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2cda4be7-4046-3500-82e0-aaa9cae81127 | -7.23049 | -43.11634 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7c65f8db-0910-3cba-81be-ef47d4fdf4e4 | -6.84005 | -44.63095 | 2025-05-25 03:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8edf65f-9070-3fc1-ad8b-b8aa2ae9200b | -7.20954 | -43.12837 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3f3d10f3-8c42-3ffb-9484-50e059045db5 | -8.06021 | -43.13773 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bb566013-df24-3917-a06d-cf14a993e5ac | -7.23132 | -43.12073 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 877197b8-87f3-34dd-8dc2-e4de65bae504 | -6.83838 | -44.63301 | 2025-05-25 03:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0f187902-573a-3873-817f-fc944eb03ceb | -8.89555 | -44.78133 | 2025-05-25 03:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6821da2-0bac-3c55-bcbe-021928354c48 | -8.06956 | -43.12667 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 41820344-e94a-3331-917d-5ac499241c68 | -8.07058 | -43.12121 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f605c650-c2ad-3449-a70b-32e4b156be14 | -7.20863 | -43.12404 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d7be7580-d3c4-34d7-9420-3451337acb7b | -8.05912 | -43.14334 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e2d36b54-943b-3eb5-bd2c-14c934ce4f37 | -12.27251 | -44.59786 | 2025-05-25 03:25:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9aee1c1d-c7d1-331c-acf3-50111584c337 | -10.69503 | -37.04803 | 2025-05-25 03:25:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84bcb883-8fb1-3a34-af4b-0ce29206a012 | -8.06883 | -43.12797 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6d5435ef-ec67-3b0c-8a39-0cf582a43037 | -7.22371 | -43.12518 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0aa8c69d-3c6e-38f1-9a01-0c0bacc5d287 | -8.06236 | -43.12669 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3927575f-2122-33f0-a3f5-fa5fd681e4a7 | -7.20969 | -43.11848 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 88eb3f58-d007-35af-a916-638664b7ec0b | -12.27128 | -44.60368 | 2025-05-25 03:25:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 15811063-28f7-3e95-8571-760e2dc78cf3 | -7.22391 | -43.11523 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 753e932e-2bc5-3cbf-93d9-6e45c0b3653e | -7.20297 | -43.12714 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a792aec3-ba66-3d8b-a50e-87d8d8983f79 | -7.22284 | -43.12084 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6dfa222e-a629-3ab7-8e1b-6879a9e27812 | -7.23235 | -43.11514 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c35028a1-23f2-305f-990c-802f80d9bc87 | -8.06747 | -43.13783 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f787d14-fb58-3a47-aef0-7f7c01247499 | -8.06206 | -43.13087 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cf282804-8b95-3168-9153-9cfa19913463 | -8.05997 | -43.14206 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 698033ba-2499-31f7-8bb2-16769e024f8c | -7.22942 | -43.12196 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b10a1437-409c-3ac4-a4a5-28dc3a27d5ab | -8.89415 | -44.78841 | 2025-05-25 03:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a70e6fd3-88b8-3acf-8dc8-421d7cbcb810 | -7.22474 | -43.11958 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7d155289-c779-3da8-8748-90cbb6d16e20 | -11.96964 | -44.15677 | 2025-05-25 03:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1157c3a-a686-386c-95b7-63c4fcf55fd5 | -7.20755 | -43.12964 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e25d8d4b-ebb6-31a3-a1d5-c09e553e0419 | -7.22578 | -43.11396 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1ac8c65-0832-3a93-a521-b1bb6190089a | -8.05376 | -43.13635 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9cac4fe2-51a3-35a6-a3a0-f118df43400c | -7.21714 | -43.124 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 79354e5f-ec04-3063-9471-d57066d35e46 | -7.2152 | -43.12523 | 2025-05-25 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fbd373fb-e44c-338f-a118-3ddc8e55b368 | -8.06667 | -43.13911 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 95e0c296-c5f7-38d9-a59d-f063deab71b7 | -16.37607 | -46.87432 | 2025-05-25 03:28:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d31ad153-b315-3e8b-935b-9672dbd29683 | -17.75315 | -42.8974 | 2025-05-25 03:28:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fee28bd6-b337-3578-8652-eebdbabeba02 | -21.21765 | -48.61436 | 2025-05-25 03:30:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 39ddd8fa-867e-3150-bb4c-ec57d79c9931 | -7.6574 | -46.1013 | 2025-05-25 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| c16cce5f-889c-3b99-8397-15850a3ab3d4 | -6.57568 | -43.6952 | 2025-05-25 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3958f9f3-c72e-363c-aa45-ed07f6961ac2 | -7.20672 | -43.12035 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 58567068-0b07-385b-9a90-91962758b675 | -6.83857 | -44.62202 | 2025-05-25 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dc71e0ac-0bc2-3e51-a430-21d2b0dcd614 | -7.4735 | -43.38139 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a60aa188-7a54-37a2-9ae3-261ac4f28196 | -10.36547 | -47.98096 | 2025-05-25 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10097b0a-a38b-366e-a509-fd7480fb0839 | -7.21107 | -43.12109 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4710f03c-5c02-317f-82f8-523e8e4acbdd | -6.83761 | -44.6275 | 2025-05-25 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9c83f027-5f74-36ac-8ca7-c5d4e9819104 | -11.61685 | -47.9994 | 2025-05-25 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec930233-908f-3702-b875-800d58096bbe | -7.46469 | -43.37987 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81195e38-2bb5-3755-9ec3-4591bd50c461 | -12.36943 | -49.9924 | 2025-05-25 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03395d1a-6d88-3d13-86bd-d09592c73469 | -11.1443 | -48.11568 | 2025-05-25 03:47:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5da7d9d8-5498-3724-90ff-e1fc36fd81d3 | -7.4691 | -43.38063 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a6a70a9-34c7-39a4-8030-2618f390d09b | -7.2383 | -43.56704 | 2025-05-25 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 79cf4ae0-6518-38fd-869c-363a9d52ac70 | -5.56773 | -43.47869 | 2025-05-25 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccb73337-71af-36e2-b5bc-9043adebff82 | -7.59688 | -43.32068 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9077cc6-3750-3023-8a0f-e00f67b3268e | -5.58159 | -43.4519 | 2025-05-25 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09d74963-2177-3ead-a350-0101c534fd28 | -5.5812 | -45.2007 | 2025-05-25 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b15bfb07-5dcc-3125-941f-2dc8170f4e38 | -6.22818 | -43.35565 | 2025-05-25 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf9ae21f-7fb2-3729-8f85-c1d990387054 | -6.5571 | -44.48886 | 2025-05-25 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fda6ef55-4364-3ab4-ab3d-855364cc1a94 | -12.82441 | -47.38559 | 2025-05-25 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae6e0972-2170-3ef7-8208-19ece02d3686 | -10.36133 | -47.97166 | 2025-05-25 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d970175-1726-3c09-9d99-7450f189c386 | -5.54411 | -45.20051 | 2025-05-25 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35c91c8b-e9d3-3214-ba43-06285c43b335 | -5.57659 | -43.58999 | 2025-05-25 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21584204-33e9-3887-ac47-8ef0063a42d9 | -7.5925 | -43.31993 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e810228b-9100-3b9e-b44c-d1ccd1b849c0 | -7.59613 | -43.32505 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea0de13c-5952-330b-907b-453610d7e0b2 | -10.36209 | -47.96766 | 2025-05-25 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7531977-f0bb-3bf5-a514-e8d9cf4cbec5 | -11.76018 | -47.25928 | 2025-05-25 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a11d7d64-44df-315e-a8f2-9144b1315c37 | -7.2212 | -43.11419 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3be0414a-27cd-3e75-ba6e-5b30592be736 | -6.22743 | -43.36013 | 2025-05-25 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98c77e05-fcc2-3684-a066-de46c406ffea | -5.60734 | -45.33504 | 2025-05-25 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4757ae5-4231-38bc-84df-351870d2d2b7 | -7.21179 | -43.11691 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5e53771c-4f39-31e7-989e-6e035a4fac03 | -7.48822 | -43.37499 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0c564c8-ac5c-3e36-8a90-af333b8add07 | -7.51239 | -43.36615 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5679c5f-6a26-3667-8f48-db9232ca7502 | -6.94878 | -42.80441 | 2025-05-25 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b45b9c1-7f1c-3ca2-8408-a562f63381a1 | -10.74259 | -49.28261 | 2025-05-25 03:47:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc51c9c6-83ba-3652-bafd-a568433d58f4 | -6.95304 | -42.80519 | 2025-05-25 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4b9ca0c-6939-376d-a8d0-5d0b35057f2e | -6.9481 | -42.80841 | 2025-05-25 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a0519a58-4417-358f-85b2-e84188c28bab | -11.75556 | -47.25475 | 2025-05-25 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7ad2627-2e8d-3d2d-a9fe-9e5b632dc3b9 | -7.206 | -43.12453 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 90b23f76-cf9c-36c5-87ec-5d3dccfee3c7 | -6.95634 | -42.0669 | 2025-05-25 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b9d7dd1-8b84-3a42-96e2-e5697f0de8c0 | -12.27212 | -44.60053 | 2025-05-25 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2741fdf-17e5-3f5a-ac9f-2512c78d074e | -7.22555 | -43.11491 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 81c94d63-781d-314a-aa48-c55434da48eb | -7.2299 | -43.11562 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cfea4bb7-4b6f-37db-b8b5-09cb8c529d0c | -7.47866 | -43.37782 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58fda3b7-8cb1-386d-8eda-5a68cb854553 | -12.37297 | -49.99481 | 2025-05-25 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README4.md)
