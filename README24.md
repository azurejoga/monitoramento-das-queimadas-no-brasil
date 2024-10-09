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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf5f6561-e970-39f5-bffe-dbb7a82fd50c | -16.941 | -57.4654 | 2024-10-09 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| c7fb8f96-75ac-3431-9cc5-e51b877143df | -16.9413 | -57.4449 | 2024-10-09 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| e8f2a58d-695c-3d39-85bd-50a53cf6c2d4 | -16.9518 | -56.7875 | 2024-10-09 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 8fec2218-de61-387c-9fc7-8fc0fee8194c | -16.9606 | -57.4631 | 2024-10-09 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 46d09b99-e857-31ea-b272-0141c69c79ab | -16.9609 | -57.4426 | 2024-10-09 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| d8598949-dc83-3177-a090-d2ea0c88164f | -16.9805 | -57.4404 | 2024-10-09 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 39372ecd-1db2-3aea-91e1-c6036988c4c1 | -17.0878 | -56.8534 | 2024-10-09 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| ece1dba9-4737-3936-9cd4-55a4c293d73a | -17.0992 | -57.3651 | 2024-10-09 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 4e84c754-d340-33d6-8a51-15954cc1f636 | -17.1185 | -57.3834 | 2024-10-09 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| c2840e2e-489c-3b0d-b6af-e32a3073405c | -17.1188 | -57.3628 | 2024-10-09 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.2 |
| 242684c9-6507-3e5c-b1cd-f69df4973cd2 | -17.1191 | -57.3423 | 2024-10-09 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 02439a3a-f5e7-38c3-8582-554beb49a070 | -17.1271 | -56.8486 | 2024-10-09 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| dfb0469b-d5b8-3626-a1a4-4922caeedfa3 | -17.1384 | -57.3605 | 2024-10-09 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| a6699cbd-dbf7-35e2-b4a9-1347a5d1e94a | -17.1467 | -56.8463 | 2024-10-09 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| cb599088-26de-3913-be6c-4218b7c8e56a | -17.1471 | -56.8256 | 2024-10-09 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 8d930920-6922-3557-8e81-5926275335c6 | -17.1588 | -56.1222 | 2024-10-09 01:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 57b23a4b-59e3-3758-8783-ba17f881d378 | -17.2173 | -57.3307 | 2024-10-09 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| e54adbb5-850c-3ff4-93af-fe9513618f65 | -17.3353 | -55.0156 | 2024-10-09 01:06:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 05366712-4296-3652-a2b8-7613c0e1d826 | -17.8985 | -41.4445 | 2024-10-09 01:06:45 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| a67966b6-491e-3b64-8320-86e68b67eafb | -17.7526 | -53.7948 | 2024-10-09 01:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 2465d811-7922-32ca-9b5c-32cb4b37e5f5 | -17.753 | -53.7735 | 2024-10-09 01:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e0e0aaa1-1cc4-385f-b776-f0cd508f5c13 | -18.5993 | -57.2629 | 2024-10-09 01:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 57c9793f-31df-3b24-8f17-a615418ac859 | -18.5996 | -57.2422 | 2024-10-09 01:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 76f96926-7ecb-3b3f-909e-44e53f6473b3 | -19.9924 | -42.4346 | 2024-10-09 01:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.3 |
| 3a84baa6-5dbf-3bf8-a1ba-d1e98003fc3c | -20.0006 | -42.1799 | 2024-10-09 01:06:56 | GOES-16 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 97295e87-11b5-3247-a21f-d7fd14c00ee6 | -20.013 | -42.4287 | 2024-10-09 01:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.3 |
| 58353f5c-cc27-30de-b95b-7f9d150216d7 | -20.1087 | -48.8261 | 2024-10-09 01:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 105.0 |
| e37c3699-cf54-3406-9c1b-05b84bbc0a72 | -20.3346 | -48.7307 | 2024-10-09 01:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 221.7 |
| a29c7db8-8532-3f1c-b223-ad6fbe8c3837 | -20.3352 | -48.7076 | 2024-10-09 01:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 7e2fd5b7-0a0b-3b1f-b34d-85d70fbb8c7b | -20.3551 | -48.7262 | 2024-10-09 01:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 371.1 |
| 3bb7db71-3608-38f1-9314-d2117b57b438 | -20.3557 | -48.7031 | 2024-10-09 01:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 273.3 |
| f1fdf9e6-5a27-3c78-aed0-4bbf7778efd8 | -20.3755 | -48.7217 | 2024-10-09 01:06:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 0be39812-0792-3d4b-a194-6e84d942be31 | -20.4133 | -48.8282 | 2024-10-09 01:06:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7e5c9e3c-3348-3d94-98a7-3faaa2b6094a | -20.7839 | -47.2559 | 2024-10-09 01:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 141a6f65-890a-323e-b8b4-26721d36f2c8 | -20.7846 | -47.2323 | 2024-10-09 01:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 3410bd43-78e2-3881-9380-8dd25702352f | -20.8045 | -47.251 | 2024-10-09 01:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 134.0 |
| e890a168-dd08-3b28-a4ce-01e5517f95f4 | -20.8052 | -47.2273 | 2024-10-09 01:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 114.5 |
| b881e3e0-04cd-3264-9c7f-3e828772244e | -21.572 | -46.9898 | 2024-10-09 01:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 5e1d360a-5697-3f60-b3cc-11360eff0d73 | -21.5727 | -46.9659 | 2024-10-09 01:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 3a514d4e-b9fc-3da0-a8f2-a1c55f301fc1 | -21.5656 | -47.8878 | 2024-10-09 01:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 74.2 |
| badeffa1-4a4f-37cb-b4cf-f09cfa61fb69 | -21.5857 | -47.9063 | 2024-10-09 01:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 75.8 |
| cb7350fd-ba4e-3aa1-8b0e-2fc602a95af2 | -21.5864 | -47.8827 | 2024-10-09 01:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 041b1b75-ae89-3839-8fd1-6b6db47dcfb4 | -21.8165 | -49.1774 | 2024-10-09 01:07:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 227.5 |
| 2f62b627-f6eb-3457-a6e2-82f25cf46414 | -21.8172 | -49.1541 | 2024-10-09 01:07:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.4 |
| 5a69f8d9-a54c-3263-9358-adc552ee60ad | -21.8373 | -49.1726 | 2024-10-09 01:07:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 188.7 |
| d2b8ca33-268f-3c95-9fb7-f7e233c43296 | -21.838 | -49.1493 | 2024-10-09 01:07:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 171.3 |
| 5f067291-5629-363f-85bb-52b117da76fb | -22.8137 | -48.4225 | 2024-10-09 01:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bd213e6e-55fb-3da1-b8b3-e9c158e67978 | -22.19455 | -48.15272 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 8763c4bd-abf5-3b46-854e-09f0d019a916 | -22.19309 | -48.14285 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3945a3e7-41cf-3dd8-af11-c6e4eb01f745 | -22.19163 | -48.13296 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| dc2088d0-ba0e-393b-b8ba-d3bf7031e42a | -23.33709 | -53.9052 | 2024-10-09 01:09:00 | TERRA_M-M | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 1d087838-7686-32e0-9cc3-d27367beb035 | -23.23683 | -48.98709 | 2024-10-09 01:09:00 | TERRA_M-M | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1a767da0-e7e0-337c-bd56-74b98e972fcb | -22.82352 | -48.4194 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 83ea8a05-34e2-3b18-a972-43bf44a63e23 | -22.81742 | -48.44055 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8bcc0de9-0049-3026-9fcb-671c412e913e | -22.81601 | -48.43078 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 4dcafc5d-869b-334e-ae12-f4ee61f4ea92 | -22.81458 | -48.42093 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 06a50a76-30e4-3fb5-91c1-f8acbed01ea2 | -22.80988 | -48.45167 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 16f080ef-c163-35ba-bbda-6170efd5496c | -22.80707 | -48.43229 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 96924cf1-5f00-3de4-8935-7303db887ca9 | -22.80095 | -48.45319 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b0a289a9-065e-3604-b101-c697a8f50d0c | -22.79955 | -48.44355 | 2024-10-09 01:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e7a408a8-b6ac-3f0d-b5cf-7ab275623447 | -22.76901 | -47.42546 | 2024-10-09 01:09:00 | TERRA_M-M | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 046b67d3-5e5f-3f1d-adbc-7b260825ad34 | -22.76025 | -47.25965 | 2024-10-09 01:09:00 | TERRA_M-M | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 92d9e0d8-2a67-3fa8-ad6d-fcd465566367 | -22.75862 | -47.2491 | 2024-10-09 01:09:00 | TERRA_M-M | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 7cf6deed-d2e6-3ce5-a8e1-6ba080d2fb72 | -22.75303 | -47.25652 | 2024-10-09 01:09:00 | TERRA_M-M | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 90bafbf1-4870-37ae-acd8-001e198d5e42 | -22.75142 | -47.24587 | 2024-10-09 01:09:00 | TERRA_M-M | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1bbebddc-cb59-3fd5-8e70-e5f3eef4d13c | -22.74981 | -47.13074 | 2024-10-09 01:09:00 | TERRA_M-M | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f07e7dd9-de50-3842-8e0e-c54df23f5ef7 | -22.57426 | -46.66488 | 2024-10-09 01:09:00 | TERRA_M-M | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d62ea323-5fb8-3c47-af63-b0d8c4cc9d75 | -22.57136 | -46.67083 | 2024-10-09 01:09:00 | TERRA_M-M | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 62744eec-40b1-3034-be4c-9e5a046dc0a4 | -22.56966 | -46.65982 | 2024-10-09 01:09:00 | TERRA_M-M | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 8ea194be-597a-3859-b231-e88ca4eb5c47 | -22.56753 | -48.56173 | 2024-10-09 01:09:00 | TERRA_M-M | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.1 |
| 71705ff7-6654-3dda-9414-059e6aee156a | -22.56613 | -48.55202 | 2024-10-09 01:09:00 | TERRA_M-M | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3c0908d7-214e-31d6-b1ef-25ff807e229f | -22.47954 | -47.59108 | 2024-10-09 01:09:00 | TERRA_M-M | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 38d2b2d8-6d4e-3016-94c5-e1ae24dc5fcd | -22.28846 | -46.82249 | 2024-10-09 01:09:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| df682e2e-5c32-3019-8f2e-5350eb409b3c | -22.28673 | -46.8114 | 2024-10-09 01:09:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 117b156d-f731-305d-8953-47695b7dc75f | -22.2772 | -46.81303 | 2024-10-09 01:09:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 43fdf68f-b08d-3f32-aee6-2dcee739ba02 | -22.20358 | -48.15119 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d14576b0-9d01-3259-91da-d30659a25a82 | -22.19602 | -48.16262 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d30841b2-73f4-3c64-9fb5-4073f784fc48 | -22.187 | -48.16417 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ba10a87f-3906-39ad-b8e3-2643c84862d3 | -22.18554 | -48.15432 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 9d7cb2a0-a19b-3eab-91a5-737af2effd0b | -22.18407 | -48.14445 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3109392c-c650-394b-ac29-43ea0ea731dd | -22.18261 | -48.13457 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 21759175-b24d-3563-85de-ffc6f0744597 | -22.17945 | -48.17563 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a213a3cf-1c16-3a85-bb52-ecdc0bb5abe4 | -22.17799 | -48.16578 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 07032e47-c7a8-3941-918c-310b37a7d1ec | -22.17671 | -48.09483 | 2024-10-09 01:09:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0d6fe4ab-9816-372e-b3d1-e08adb5243ea | -22.1721 | -48.12617 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3c998014-5ad7-3c4a-a7b9-f382fe999d27 | -22.16308 | -48.12775 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 36.7 |
| efc0dc99-6bd3-3090-9d00-5696d1fe1cbe | -22.1616 | -48.11787 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6513886d-f02f-3b23-9430-e26f23327a94 | -22.15405 | -48.12936 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 34f5292b-061d-3ef4-b4a9-220bc3ce8864 | -22.15257 | -48.11945 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 89d86e48-7893-3fc7-a0e7-86e1a46e4e9f | -22.14478 | -48.12704 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ff735a09-4294-3b3e-b465-75253d3e97a7 | -22.14333 | -48.11713 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 23c3da29-4dc3-3ba9-918c-b80e25a3b3f2 | -22.14187 | -48.10725 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0f621fd7-1362-340b-b57f-3a03363ab1f5 | -22.13574 | -48.12856 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 853652e2-8f73-34eb-9b7a-9e015d39e293 | -22.13429 | -48.11871 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4c39757e-fb51-3486-937f-652bef4613fd | -22.13138 | -48.09897 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 985439c5-1db3-3b41-9584-d2684f974acf | -22.12992 | -48.08903 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bb21e808-9c41-35c9-8c5f-86012d90561c | -22.12671 | -48.13013 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2cff8918-2006-3b4c-a00d-392ff5041897 | -22.12526 | -48.12026 | 2024-10-09 01:09:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d5d71153-3435-312b-8d1a-d6044d6925ef | -22.05551 | -46.88908 | 2024-10-09 01:09:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e7906981-fb24-3fa5-8cfc-14127e6c29a7 | -21.88283 | -46.71654 | 2024-10-09 01:09:00 | TERRA_M-M | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |


[Clique aqui para ver as próximas entradas](README25.md)
