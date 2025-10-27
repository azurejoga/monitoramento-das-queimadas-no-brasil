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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67dcf912-0ebe-39fa-8282-b6499f1be0f4 | -7.93172 | -55.01735 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66217ba9-bc36-3e58-be14-eec4cfbea142 | -10.6822 | -47.84078 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c99171b9-aa04-3eca-8130-a8d7e50f5ac0 | -10.56324 | -47.88865 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3212533b-7e00-3723-9c0b-1ce96cc225a1 | -7.86044 | -45.37903 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a74084b9-47cb-3e32-9102-2de29ee12189 | -10.63587 | -52.18873 | 2025-10-27 05:01:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49b9c531-9d24-3941-9356-06b3f81dff7f | -9.12754 | -45.85929 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df1f810c-85bc-3fd2-b951-c525437ca820 | -7.83113 | -46.48874 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c2dddf63-4047-3c85-946b-707400b41173 | -10.93306 | -47.60339 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efadcfbd-b988-3944-99df-821822225f6d | -5.96781 | -42.77246 | 2025-10-27 05:01:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8adcfcbd-e6d0-3911-8cfa-6f92465541d3 | -12.05284 | -46.38088 | 2025-10-27 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db81401b-3c57-322c-ad87-c3da26807999 | -7.25039 | -44.96507 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 825aa1a8-d9d8-39d3-a677-4ae273099022 | -10.75043 | -44.19738 | 2025-10-27 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9cb5735-5b59-3c1f-8215-e9630cafbb2e | -12.51082 | -44.32669 | 2025-10-27 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 410d66a9-c581-3877-b72a-8bb478c3920f | -9.98929 | -47.17879 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01cd1bf6-b064-33b7-bef4-43d922239a1c | -11.42455 | -46.10792 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83dd931d-1e05-3a61-86d3-f2fdb1e8daea | -10.95389 | -47.58025 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2377612-7dd6-30ab-a771-497cd7f50090 | -7.96605 | -45.46879 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01c45fc1-c2ed-32d1-b37a-9747debd9a8a | -10.32318 | -47.15551 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0f941d9-2297-36ad-81db-c2f573d70ea5 | -6.37172 | -44.26265 | 2025-10-27 05:01:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5d6b552d-da53-3da1-9a52-7d613156dcb3 | -7.87064 | -47.25279 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc98db02-a181-3e62-bd02-c7c6f6dc3411 | -7.10696 | -47.94877 | 2025-10-27 05:01:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4781a7e4-a323-3de8-9417-102dcbaba9ad | -12.08308 | -46.39939 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 858ed967-3520-3ccb-8ca5-72cad79774b4 | -7.99277 | -46.20232 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62b3dcae-879c-3efc-8c8a-ae77768bdec2 | -5.57282 | -47.49577 | 2025-10-27 05:01:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bea646f-4df1-3d1b-bf21-426f89f2698b | -6.57463 | -48.76455 | 2025-10-27 05:01:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4e06895-fd74-3414-b39f-aa5566f3d5a1 | -8.2323 | -46.92781 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c0fccd8-e2e5-3a82-9870-f32f1db9c0d8 | -6.64223 | -44.6305 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cbb90ff-f777-3270-886e-c57db0358441 | -12.32591 | -47.49547 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f04682e0-fc8a-3765-82bc-d5b851017837 | -7.96016 | -45.47202 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e042cca-6d1e-3f1d-aa36-6e8cc1c821b5 | -8.52321 | -47.20597 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 483d9395-9503-3492-b503-b5e24c178e95 | -7.33045 | -47.14495 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ee08abdf-53eb-3f3f-8bf3-2700838e9db4 | -10.62867 | -52.18764 | 2025-10-27 05:01:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8c37e8ea-efb0-3edd-9f90-47de8d5525f6 | -12.27582 | -43.75746 | 2025-10-27 05:01:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3837221-9e4d-3351-9622-806a6930a603 | -8.31596 | -46.18293 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1b16edf-6aee-381c-a168-aa87d77d8a4b | -7.95925 | -45.4787 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 190f4651-4f52-38fb-b6b9-9679a7864eb8 | -7.95884 | -45.48177 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6848adab-3032-3013-9d23-456bf88bbee2 | -11.28736 | -45.15118 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c40e001c-df58-3ebc-92be-84af048a2e3b | -8.09218 | -46.95002 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10c9893d-e614-31f1-bad0-9977e461fba2 | -8.30535 | -46.18401 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74b0509a-575d-3e59-9170-7588981617e7 | -10.35057 | -47.17606 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9d779c9e-a599-3830-ae0f-39245983f52c | -11.05321 | -49.90384 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 790b9f9e-a5aa-35ab-aa72-0adef1962940 | -7.83689 | -46.48384 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| aa558d31-4237-30f1-9e4f-0bd40c6fa3d6 | -10.0257 | -47.14536 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b709a9b7-6c14-36da-9728-46c75243d582 | -6.88755 | -45.14923 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ee704d5-c419-36b4-8be7-039f6d95d0d7 | -6.63664 | -44.62988 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d180724d-9110-3a3d-a2b7-893683b57a56 | -8.74151 | -49.60929 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7368098f-16c4-3fb1-b29b-8cd57cc5855b | -6.90291 | -46.13876 | 2025-10-27 05:01:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5dcfa51-c304-38d7-8ed4-58a121d665e2 | -8.64946 | -47.24109 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64720102-93c4-3f83-a425-2e88702571f6 | -7.83571 | -46.45573 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 38998c63-d146-3cae-859d-77c1c83850f1 | -9.2565 | -45.57435 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8ed0a91-fc06-3da8-9823-8c7f4ce5aa01 | -9.22555 | -45.84515 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5b9a118-0809-34c7-91ff-376e894680da | -7.8135 | -45.40239 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3f4f891-ee38-33e1-9091-b9bbdd6919f1 | -9.59702 | -50.78828 | 2025-10-27 05:01:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28dba513-4a54-38c1-848a-05b7b9d8be78 | -6.26121 | -41.82552 | 2025-10-27 05:01:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 456b76e3-50df-323e-8bf9-a34dcfb26c8a | -8.22037 | -46.94207 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a551165-7362-3350-810d-8bbb2829fe36 | -7.78689 | -45.38129 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62b95deb-d042-312a-8222-2289e6f3eccc | -11.28684 | -45.15541 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8c317c1-2e6c-381d-a1a2-3f0b6b7170f6 | -11.02434 | -47.82161 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e859170f-c51c-3e83-89a5-3402e9442136 | -7.441 | -41.87321 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4b138242-8cac-3bd6-8eb9-edbebc51e16c | -6.88939 | -45.15416 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62bf94f4-6bf0-3122-906c-52a086576a31 | -10.32071 | -47.21099 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcb88879-0ada-3c06-adf1-6a3fbd4a72ab | -10.42138 | -47.64814 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e972233e-fadc-3505-beb6-001f7b797648 | -9.44326 | -56.65055 | 2025-10-27 05:01:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21e86ca5-6729-356d-b603-b58b6071a6da | -8.53417 | -47.1995 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f228862d-1b8a-3287-a341-73add0d40e54 | -5.63521 | -50.32005 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09f3a0cf-a004-393b-b1f0-00b6c1fd07c8 | -3.97996 | -55.74273 | 2025-10-27 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96d832ef-9876-36ac-8338-1d1b168407c0 | -10.97387 | -47.87196 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ba0abc6-0c8b-30ce-aed7-e62ca72397a5 | -7.03535 | -43.93175 | 2025-10-27 05:01:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0323595-45af-33af-8124-e9f4dc43142c | -7.68399 | -46.34209 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03df848f-92a0-30f8-9bde-cec0c662574d | -7.85688 | -46.48644 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f79970-d10e-3248-86bf-eeb0a1109576 | -6.88384 | -43.58091 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0b624da2-ca72-3767-a131-a4ee0a264260 | -7.83767 | -46.47825 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2c969021-8252-3ede-acd5-9a273e739301 | -9.73223 | -47.86362 | 2025-10-27 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 072a5a47-b04f-3dc4-8d2c-2278751fa87f | -9.63221 | -57.01591 | 2025-10-27 05:01:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e37a585f-8468-312b-925b-f04e5bb4ecb7 | -7.23659 | -44.98359 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7038288-7f00-3dd5-8ec4-5edd3081c537 | -11.42768 | -46.12621 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15811c6-6e43-3714-9a4f-46822adb7435 | -9.14368 | -51.30663 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de36b2a8-c0ac-35ad-a167-d3dbac0cb22d | -6.88507 | -43.57209 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c0a9b29-ee4b-3887-8327-1a49f4ba6d47 | -11.33682 | -53.93148 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9783ac22-ce94-30ae-9d45-643484f9d4ba | -9.84085 | -52.27082 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a10189e6-2ceb-34ca-b69d-7d514c2fd885 | -10.68273 | -47.83492 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33e64d52-eaf9-38ba-bacb-45fc068ecb56 | -12.27794 | -43.75642 | 2025-10-27 05:01:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5e9d732-9e66-35ea-bd1c-b3c242621913 | -6.88105 | -43.57773 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b37cc34-54a6-3c42-b377-7701ddc1d0d7 | -12.32521 | -47.49468 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5d1ea7cd-613f-364f-9969-75ac665cd874 | -7.9284 | -55.01682 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8d037b0-f5f8-3e03-ab80-62cbfa58cdee | -12.32094 | -47.49486 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 000ead4a-7a17-3839-b59b-98e947c231c5 | -8.3282 | -46.82625 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb21de2-c6db-344d-9997-5007b2c8fd4e | -7.7927 | -45.37886 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ec3acc-630a-35fa-96e5-fea10c2006ca | -7.96561 | -45.47208 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4b3143f-5f4a-3bc4-a593-8f0b4b30db93 | -5.26385 | -50.979 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41bbde2a-bbfb-379a-8aae-6f771e0be023 | -7.94995 | -47.23843 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0002b8b7-517a-383c-8abc-7f4e151c033e | -12.50423 | -44.3289 | 2025-10-27 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 323a695f-ba39-323a-9084-83d17028c53a | -12.28429 | -43.75714 | 2025-10-27 05:01:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8896ea4e-bf8f-3440-9f56-4043b82f45e3 | -7.59543 | -45.68277 | 2025-10-27 05:01:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c74a879a-c9d8-3f58-815b-c3abfae21a5b | -10.68282 | -47.83596 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ade1467-beff-3359-a7c2-3dcc353bd498 | -7.41745 | -46.39041 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b94b990-d007-3269-9ec9-4672c34603a4 | -9.4575 | -56.64915 | 2025-10-27 05:01:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3df9a2fd-0471-3380-8b28-b3fa3d24d5b5 | -7.87922 | -47.25248 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8180c66c-170e-3801-9bec-4834a44c12d7 | -10.58559 | -47.86611 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f8dc14ac-2c0c-306f-9c11-4adf31ce6886 | -9.56931 | -46.90051 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README63.md)
