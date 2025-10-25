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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f5ce588-5e8a-3be1-bab9-c0e52a13bb40 | -4.82402 | -50.92834 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08e4c0eb-cf6e-3223-b285-6fac2dbafbb9 | -5.60037 | -47.08879 | 2025-10-25 04:17:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0baf5a49-3752-3cbe-90dd-7b5b50dd712d | -5.41485 | -46.0062 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 216c3a49-6eaf-37e6-8e19-61504945e63a | -3.16677 | -48.6092 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8694c53e-2c61-3eb3-aa39-5257daf38d32 | -3.21506 | -45.4612 | 2025-10-25 04:17:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba519a77-0695-3b1f-9bc0-35c0fbe3089f | -4.81158 | -45.582 | 2025-10-25 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6e9ef344-325f-38e6-b18e-34786fcea639 | -5.57334 | -46.34871 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d375844a-36d8-3c02-a3fa-537899acf288 | -3.86452 | -50.50565 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba7e6e50-d9d3-3be8-bcce-23958e0b1e53 | -4.20001 | -48.36485 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a195c72-beaf-382e-bbf2-b9a907145680 | -4.80821 | -45.58148 | 2025-10-25 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c1f0b4a0-ee1b-30bd-a2a6-34d58e156d80 | -6.31846 | -41.87023 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b3f2497-eba9-3965-8787-44af57968d40 | -5.45693 | -45.41043 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed1a0fb1-3ee6-3909-b2ec-0c66948f3ebc | -3.64963 | -48.97224 | 2025-10-25 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0994c30-a01e-3ca3-a889-5de5c114582e | -3.0849 | -49.47339 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3fcba93-d3ad-35d8-82d6-39c3beeb0940 | -5.47613 | -46.4714 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6efa7309-b7c2-36cb-978b-f62cae7e8649 | -4.5508 | -46.60668 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f89db3bd-3241-362f-8c98-b9ed60ead0db | -2.77197 | -48.01901 | 2025-10-25 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6c7cd126-229c-373b-b020-764f9054a1d0 | -6.10498 | -40.58873 | 2025-10-25 04:17:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| daf170c3-45c8-3171-9364-8990f0070143 | -6.10118 | -43.69972 | 2025-10-25 04:17:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a92a702-63d7-315c-9c21-c2a4167e9fd0 | -4.22409 | -48.60913 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0a8ba727-26e3-3cb7-817f-72c64eb53ca8 | -5.67055 | -46.65743 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 874dcdce-efda-3df9-82b5-a28536cd4f40 | -4.81215 | -45.57841 | 2025-10-25 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1062d1cd-0386-30af-b439-65c8f04a5c1c | -2.89275 | -48.06509 | 2025-10-25 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67786f00-574b-34f2-ba98-16822d6e062f | -6.06856 | -42.15595 | 2025-10-25 04:17:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0afface-5fe2-3b42-a090-232429ff869d | -4.24555 | -48.55367 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8123101-d461-3da1-b7f0-c1711f477589 | -3.42731 | -44.838 | 2025-10-25 04:17:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 495e8a78-bb7f-31d0-9723-931ad26e17c4 | -3.40457 | -39.1703 | 2025-10-25 04:17:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9cf5dc97-57aa-379a-be85-0ad0eea618b0 | -3.22341 | -49.36596 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72274f63-5da3-3634-b46c-dd3b6cb88857 | -2.69156 | -54.77177 | 2025-10-25 04:17:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ac8d348-ac39-3b8d-86b3-ed6b0091ee9e | -4.2709 | -40.70165 | 2025-10-25 04:17:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f8e943c-8deb-3924-92ed-802ba10d005e | -6.06974 | -42.14823 | 2025-10-25 04:17:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dbc7e8d2-2de4-3e7f-beee-0e509f5e7bce | -4.59649 | -49.58441 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22340f19-4768-3255-862f-2ac84032382b | -5.82127 | -40.80606 | 2025-10-25 04:17:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3bc35485-aa35-38db-9a93-3dcc8596580d | -4.90722 | -47.66071 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32fdf366-808d-3ae5-8208-80f96d89f970 | -6.60403 | -42.65943 | 2025-10-25 04:17:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5b5824b7-9ed5-3284-a766-47935f9db9f7 | -2.9932 | -48.74599 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 179de2ac-27da-38f0-92a7-f6196e8acbc7 | -5.10833 | -48.66288 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39b8fb96-6456-300a-8669-0cd9fa8fbb91 | -4.64897 | -50.99532 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e77bfa6-3cda-3e75-a314-ca0b2cd898bd | -2.86867 | -50.72686 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 749c34db-7812-3bf9-9ccd-bd18c686acc7 | -3.25951 | -50.1531 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dad8028-c6d1-3441-ab63-20764d975a18 | -6.1271 | -41.72572 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e1bd5f4c-44f4-31c4-9996-d0fb2be7ea43 | -4.22721 | -48.6147 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89be6d9d-9291-379a-a7aa-89b68768b760 | -4.32943 | -46.29731 | 2025-10-25 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a414be73-3dd6-3724-bc5a-8588037fcd3a | -5.60714 | -45.19347 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 425ecf09-2781-3a0c-8ff3-9c685cb90e83 | -2.85178 | -50.7435 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2110a1f-97bd-32fc-95cd-94e2a2bb641d | -5.65228 | -45.96935 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1081f64c-caef-31d7-aef6-6a567bd90da9 | -3.68995 | -49.94107 | 2025-10-25 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf47433b-3691-39f7-b56c-d9592be86dc7 | -6.13065 | -41.72617 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 698e6cf2-3921-34cd-b02f-06349e1f4980 | -4.56994 | -46.94077 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9b032e7-6f95-3e5b-96a5-0ee8aa0bc76b | -5.54388 | -46.52842 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 015e5d93-e4ea-3e30-a6bd-68b8a9bade1e | -6.43985 | -42.33516 | 2025-10-25 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9308617-e9a2-3a57-97e7-ccaefedd75a4 | -2.85937 | -48.6744 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1997677c-ae47-36b6-8261-dc77f068812b | -1.92254 | -52.14517 | 2025-10-25 04:17:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaafc610-9dd1-3b4c-9b8b-0da9426b72a3 | -4.8718 | -47.53289 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c43735e-1804-3328-935b-eede508a2a76 | -5.67947 | -42.7686 | 2025-10-25 04:17:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d88e7150-3779-3049-8cde-d3ea7dd04f02 | -3.14449 | -50.16614 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c35996e-1d53-394c-a38b-93bcc3b379e2 | -5.91484 | -39.19498 | 2025-10-25 04:17:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae5b2b6b-595d-34d3-8d61-2784624e561a | -3.72743 | -52.43945 | 2025-10-25 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 901e2787-6080-3b9b-8556-507a184a7a47 | -3.04842 | -50.4286 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1868ea09-b4a5-300c-a13b-62f9236db19f | -6.43697 | -42.3308 | 2025-10-25 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7628ecc8-3c44-3ea7-9301-39a5085eed0c | -4.83859 | -50.93401 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 832acff1-078a-34b9-a2f0-be107a67fcd7 | -3.22757 | -49.36665 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d797c75e-43a5-36f8-b8d2-71fb0bef2def | -3.73641 | -42.31013 | 2025-10-25 04:17:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c51812e-4d1e-314b-ba54-eca94abbef9c | -3.43088 | -50.26218 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6743b9e2-8d64-35ba-8c5b-5a69f395d054 | -3.14379 | -50.6229 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6afd0cb8-08e5-3303-ad65-5ea86b102a1e | -5.54596 | -41.38797 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ad407ad6-93ba-3dfd-a0fa-2b077d2ab9fa | -3.49528 | -50.06379 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20bb8f55-304b-37bf-96cd-aee02019b5a1 | -5.68937 | -45.61819 | 2025-10-25 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73f7ed96-712d-3fe2-8756-fbd0ef0a9e52 | -4.8688 | -48.65302 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a785e87c-44ec-392e-9190-dddbc55847a9 | -6.32086 | -43.74807 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 171a3c1c-6b3b-3e0c-949d-46cf1f4d0f36 | -3.23514 | -48.75407 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42850adf-cc11-311e-8e54-e4caa23c5bea | -2.85716 | -50.73951 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9986112-c8b7-3045-af97-68e70adbd3a5 | -5.61233 | -41.12354 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fb6b703b-1008-3c07-980e-322b5dacc5f4 | -5.17493 | -50.12682 | 2025-10-25 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e17e7158-3117-3a80-98bd-575028b6133e | -3.60261 | -45.97348 | 2025-10-25 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac908af7-9216-3a81-bd70-e05f993b9d13 | -4.27634 | -44.39273 | 2025-10-25 04:17:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4806accc-7eb4-3b49-b5a0-9d03ff470b72 | -5.65566 | -45.96989 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eda2780e-52fb-3872-9ef6-132f2cb06024 | -4.81494 | -45.58254 | 2025-10-25 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f3f18ac6-1822-35a8-b708-c2fa330227d0 | -3.13796 | -49.52156 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e271c03-68bb-36a6-ae25-528aa955256f | -4.84233 | -50.93936 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6e6f812-1a8c-3f95-8e20-4a26fc29b557 | -4.55556 | -46.60664 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6929ecc-643b-3295-b5b0-49a0df5a1ec6 | -3.78132 | -52.03157 | 2025-10-25 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08f9714a-c2be-3c57-9248-49919bb39d83 | -5.54528 | -46.52505 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 842911ad-601b-3ccb-b6a1-d485df29b5db | -4.22312 | -48.61604 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a8909bf-e84d-3281-824a-f61f435d7d48 | -2.80076 | -49.14051 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ba96589d-79f5-3bc0-a287-cdf1b1dd09b1 | -5.82058 | -40.8107 | 2025-10-25 04:17:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 998ef898-172e-3dc0-b54b-69c9ae00b1fd | -4.83487 | -50.9286 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ef85d7d-fec9-3785-a558-7ddacf8b2820 | -3.26391 | -50.1538 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3320c796-8b4a-3e09-92cb-b87a7be5776e | -2.89534 | -45.48578 | 2025-10-25 04:17:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63aa7eb4-78b9-3b0f-9cfc-cd9a607c5ee1 | -1.92305 | -52.14206 | 2025-10-25 04:17:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6888b626-a98d-38c6-8cc5-5387af6665c2 | -5.58593 | -41.31864 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| febee232-0c0d-3a8d-b6d9-42231708490f | -6.12831 | -41.71774 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4b21d74-f675-30b7-a0a4-3cfb5cd87ee1 | -5.45717 | -46.41433 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1bd4b2d-f927-32cb-bd8f-38500a42e0fd | -4.26997 | -50.50733 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97497f5f-5d70-3f3d-bd35-3ed720c3729c | -3.82531 | -50.19519 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 71158d86-3bff-3668-bc2a-c1b0e83e2d4e | -4.84994 | -42.38094 | 2025-10-25 04:17:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9253f0f4-f54c-332a-9826-897d6d1f3415 | -3.91823 | -47.68689 | 2025-10-25 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| adb36247-360e-38dc-8ea1-af6596e1925e | -3.72184 | -52.44151 | 2025-10-25 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a123f1a5-b5ab-3210-9813-ef6430c4514f | -6.21937 | -42.54178 | 2025-10-25 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 62e4cc65-49ce-3110-a80e-0b926b78d69d | -6.13443 | -42.45597 | 2025-10-25 04:17:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README30.md)
