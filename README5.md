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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1faa1bff-2f53-3ee3-a6b6-110a7656df81 | -3.85202 | -46.54339 | 2024-12-01 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b176e2fb-c8d8-339b-b36d-4bbdb057847e | -3.70681 | -51.05452 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e5e39dac-8434-34ee-9a0e-ea677ebad03a | -2.81146 | -53.0426 | 2024-12-01 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d11539d3-38fc-3c6a-9b55-183d2fc7037b | -1.70206 | -46.14625 | 2024-12-01 00:34:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 6eb60bf3-28fb-350a-bc84-7f17a5f1d32e | -3.22296 | -45.76018 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| bf77ba95-3aa0-3fce-b33c-2a21a4519ac5 | -2.94924 | -49.45227 | 2024-12-01 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| a17ede1f-d4f1-3834-b934-e3571950c6c5 | -3.31751 | -45.64148 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a688c99c-5bb6-30b4-936a-a1c40a83da64 | -1.56229 | -46.77774 | 2024-12-01 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9aba65b0-059b-3cfb-836f-f3050ebe6216 | -2.80348 | -53.03853 | 2024-12-01 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| eb89307e-c5bf-3d85-8c8a-086b7affd8a2 | -4.17347 | -48.6136 | 2024-12-01 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| c3f7484f-a6ba-3bc4-a041-71f7ba5cfd6a | -2.62895 | -54.21106 | 2024-12-01 00:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 55c7dd8a-96a2-356c-9dd8-c057125d1cfd | -2.64999 | -51.88881 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ad5fc53b-6f44-30e7-ae54-6f96ce5683a4 | -2.75169 | -45.95697 | 2024-12-01 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| f9547d3f-06ed-3863-af33-0c8a4117931f | -3.33129 | -50.22741 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c884f361-42cd-35af-a378-4a19f38a9e4f | -2.55002 | -45.62045 | 2024-12-01 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 28.4 |
| d9cab317-a960-3d64-accb-031d14c3b67e | -2.95384 | -49.44508 | 2024-12-01 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| acb7675c-2bcd-341f-8080-cd96cc2832ed | -3.96709 | -47.24699 | 2024-12-01 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5c3bbca5-e097-3564-96cc-bd13ed94e6de | -3.70114 | -51.07285 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 5ab4b478-5730-3517-82dc-141269fcef5a | -2.68544 | -46.60788 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd6a83c8-eddb-3836-826e-1cdf655a0502 | -3.5633 | -48.67646 | 2024-12-01 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bd1050a5-9da0-3358-8ed3-dc1056d9455b | -3.86033 | -47.05976 | 2024-12-01 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 48e8d494-f98c-3550-ba94-3509a46feb55 | -3.503 | -53.82446 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 016cc2ae-8b3a-3724-8107-5dbb0bc30d0c | -2.84087 | -49.89743 | 2024-12-01 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 7edd182b-84b1-31d6-98a9-126000d4fa68 | -3.30909 | -53.86183 | 2024-12-01 00:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 31e19b0b-0a60-36f5-9c63-4ec86e5f679d | -3.47005 | -50.28473 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| e3eee57c-77d0-3686-b867-308660fd7095 | -3.54325 | -51.51615 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 89202a5c-71f7-3987-a2a8-4af59ad9c9fc | -3.03453 | -50.25121 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4083fffc-6eaf-3fc9-adc5-0e7f5d8b6ca0 | -2.48011 | -45.44293 | 2024-12-01 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee7e4df4-05de-3ac7-ad34-3095bb829a77 | -3.00273 | -45.42958 | 2024-12-01 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a86db8c-89e2-3c62-8fa8-b31b4242efe1 | -3.08823 | -45.51845 | 2024-12-01 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 04ec5ef1-cb39-35f8-b2d2-1002c31a470d | -3.30552 | -50.03512 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| b47a9310-403e-36ea-943f-e76cc8c59cc0 | -2.75451 | -51.75483 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 32a73405-3ee2-36e6-9d3f-2fc89b4909c6 | -2.01798 | -46.50645 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 882aadda-0fe8-31f3-a1a8-ba096684e426 | -2.61476 | -45.42152 | 2024-12-01 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 359fa934-0260-3a28-9346-2e2df8fcfe71 | -2.70682 | -45.42198 | 2024-12-01 00:34:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f90bef27-8ba0-32e0-9d88-8e8fe245737d | -2.46341 | -46.56976 | 2024-12-01 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 579b196b-f683-3675-b2bd-f78ee4af10de | -2.66536 | -51.88118 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| b0186804-b634-39b6-aea1-d2bd4b885c5f | -2.33412 | -45.6492 | 2024-12-01 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 59989714-3836-3dad-90a0-770b938aba46 | -1.97867 | -46.46566 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7d71840c-263d-346d-a810-a1a1f2990ec2 | -1.11899 | -47.47875 | 2024-12-01 00:34:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f0268ab1-acff-3555-bc2c-41a9bb8417f0 | -3.00801 | -45.13662 | 2024-12-01 00:34:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 42146412-b40c-38df-a281-53327d497ab8 | -3.36065 | -43.83077 | 2024-12-01 00:34:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f2fee21c-0f63-3af4-a4c0-6e0a7ea51297 | -2.64631 | -51.8625 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f124cb21-0232-3243-a6dc-9aee65eddc81 | -2.1116 | -46.23758 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 03e8f1fd-37c3-3d1a-9da8-e613616c28cb | -1.83486 | -46.2328 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6f0a3d0-e7ac-3902-8040-d7f8ac9cfa9a | -3.26729 | -50.04037 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 25204d39-1c70-3e05-bafd-b6fad7ee7feb | -2.66463 | -51.88671 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 71032fc0-d8bc-380f-b7c6-45a2e78fe0f4 | -1.5608 | -46.76714 | 2024-12-01 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| cccee6fe-367e-3353-9836-6f5318485a78 | 0.98215 | -50.2425 | 2024-12-01 00:34:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 55f5f91b-e606-3b5f-bb7b-71ac510fd41f | -2.63921 | -46.19962 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 12d44861-9a5c-3c07-8027-71b4ff3db164 | -3.52163 | -51.14019 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 084d4090-60eb-3b84-b076-2059d6c8c625 | -4.19884 | -50.68596 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1aa5e89d-5714-3fb7-8bdc-6c85d8398123 | -3.82334 | -52.25521 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 16e84b82-6785-38b8-b10d-fa99ade41c12 | -3.89247 | -47.06737 | 2024-12-01 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 32ade766-db5c-30a1-a333-2974e1419323 | -3.02876 | -51.54304 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f7827b36-22a1-38ab-b320-3d4b2b3fb3b0 | -2.65199 | -46.57988 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ea3ff456-7eca-373d-a5ef-190bb7ef4e59 | -2.68531 | -46.14549 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e80ceaa5-7766-3d1e-86e9-9a4a75f5e12a | -3.38695 | -49.85674 | 2024-12-01 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 420c5869-31f7-379a-99af-b9fb83afd435 | -2.55825 | -46.566 | 2024-12-01 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58248ec7-76e8-3f92-aec5-462f7471f07c | -3.01692 | -51.78307 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 8b954eb5-55e2-3311-8e2f-45019d7f9cbe | -3.8618 | -46.54179 | 2024-12-01 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c8a8cef2-6575-30b6-a79e-ad094dfce60c | -2.95034 | -45.71701 | 2024-12-01 00:34:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 471f7d8f-afd6-3a11-ab88-ce0bfbefbd1b | -3.75002 | -52.27023 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 1de61db1-edc9-35cb-8dcf-3093b7ebbd87 | -4.17556 | -48.62904 | 2024-12-01 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 99e56123-6f23-3e1d-88d7-46f7d61c9e4d | -2.99936 | -51.07159 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 4999d352-6e0f-3085-9116-4beef891e2c7 | -3.26554 | -50.22164 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e38becc3-e2c7-30bd-a1dd-8043645ef2d0 | -3.32679 | -45.64022 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 91b42bcc-2b8c-3ddc-9282-e23f5d1e9254 | -3.06069 | -51.05783 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 1d895711-b8b2-3e65-a217-1ba39e888c8a | -2.90035 | -51.59194 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| bc8b87c1-5814-3023-9cf0-b5ad6b605b4b | -1.12056 | -47.49026 | 2024-12-01 00:34:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0ef236eb-afff-34df-b8fa-b89b268e377d | -3.31827 | -50.03341 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5fabf54f-09fe-3fe2-bb29-6a4788d4a9d9 | -3.68904 | -51.81378 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 40032843-8c83-39fd-9617-3b995a1a2d8c | -3.14327 | -45.99012 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e82d38f4-89bc-3f61-89c1-98f2aa5b3770 | -3.76578 | -47.7178 | 2024-12-01 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f9b52e1-9aa4-3b0a-840a-0ec9f4f0eba4 | -3.13248 | -45.98141 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 58407a93-6bf5-37ab-976a-5b7ed74e1dd4 | 0.98702 | -50.24943 | 2024-12-01 00:34:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 006aa00f-35ef-3270-ac1d-06c7077412cb | -2.84001 | -49.87226 | 2024-12-01 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 67aacdba-35c4-388d-8ff4-9b81e6e5fa52 | -2.949 | -45.70729 | 2024-12-01 00:34:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3706b1d4-ec8c-3079-b2d4-7475c0b9ac22 | -2.70939 | -47.73932 | 2024-12-01 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59aa2eba-069e-3054-95ac-aba39437eb3d | -3.20497 | -53.13728 | 2024-12-01 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 09942f36-2d72-3c8b-ba94-0be80126553e | -1.71889 | -52.62432 | 2024-12-01 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 15734521-c0ef-3539-bed6-55cd2a7cb13a | -2.46739 | -46.57428 | 2024-12-01 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a10eaf1e-ef2f-3024-8023-41dc84e6d97e | -3.26199 | -45.37539 | 2024-12-01 00:34:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27adbfb6-fed7-3286-a884-7cee61803b06 | -2.89434 | -51.57377 | 2024-12-01 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 8ec023ba-11cb-3737-852a-ea8b698b59d5 | -2.80786 | -53.07178 | 2024-12-01 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| e752525a-4610-3935-bd66-0beede560057 | -3.71007 | -51.07834 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 7f1c5fc2-5202-3ea8-8b07-81d32f321e2a | -3.30556 | -45.62337 | 2024-12-01 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21eab834-304a-3f47-accc-1593898fed27 | -2.99331 | -51.07906 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7e068599-193c-3956-99fb-501790c7040a | -3.27847 | -50.21983 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7d1e3020-244a-3441-99ff-051d971cb175 | -2.12027 | -46.58213 | 2024-12-01 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ac14a389-a25c-3aec-b657-0e575d38ba02 | -4.2609 | -50.84172 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 30a57526-3851-3b03-aaf8-b61ec4e9eaaf | -2.68969 | -51.71109 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 9daec7ad-aa44-3544-8f07-f8174d9787b2 | -1.59752 | -45.98689 | 2024-12-01 00:34:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0c57507f-fe6b-3094-a736-f5d6c7f08f50 | -1.72368 | -45.77093 | 2024-12-01 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c407d04a-faae-3cd7-9ad7-cf4526556a6e | -2.36732 | -46.37037 | 2024-12-01 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b377de7d-9d95-3f7c-bccb-73f1b1417966 | -3.26992 | -50.05973 | 2024-12-01 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 457b5fbd-0059-3744-be74-fbc488e2a6a5 | -3.65962 | -50.70957 | 2024-12-01 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1aa7291c-4046-33e7-9f53-5615e4eef7fd | -2.5721 | -51.87903 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3172925c-d548-3ae7-be0b-642ae481504f | -2.95866 | -45.17783 | 2024-12-01 00:34:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 44a0796c-0dda-30ab-a66b-ddfda0f9bb8d | -2.65073 | -51.8833 | 2024-12-01 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |


[Clique aqui para ver as próximas entradas](README6.md)
