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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53790d4a-697b-3377-9c69-6c3484d37c79 | -16.07565 | -60.09504 | 2024-11-18 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35f43bd4-5049-3cdf-8812-14c77708da64 | -12.57271 | -57.77723 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81b20484-2025-32f9-9359-d487140c0eea | -11.5376 | -51.27374 | 2024-11-18 05:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3041b8fc-4562-3fce-b047-b3125594008c | -1.3148 | -51.7408 | 2024-11-18 05:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5046d261-f619-3b12-aa3f-91c61f32c792 | -1.2964 | -51.741 | 2024-11-18 05:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 37eafa17-6060-333c-a82a-49e5399ccf6a | -17.60263 | -57.58149 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0b484e83-5309-3b62-890e-c32df9c44ef1 | -19.49219 | -56.61396 | 2024-11-18 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f6394edc-bccc-3ccf-ace3-6912ac943599 | -17.60876 | -57.58626 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6d29f475-f345-3870-a35f-ac840a87ee0b | -19.48871 | -56.61341 | 2024-11-18 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2f9941b7-40c1-3bb7-85f2-2acce9246358 | -17.62602 | -57.58532 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 726d491b-13ff-3532-948a-83e0347551bf | -17.61934 | -57.58423 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5246d6da-ebeb-3bed-a6bc-0cf77a8b936d | -17.61878 | -57.58791 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6e11d377-fa39-3a10-ac6e-92672a0a4e39 | -17.62045 | -57.57687 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cb39c909-f2f9-3995-b875-5498eef0ae71 | -17.62714 | -57.57797 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 69ceedfd-cebf-32c7-b558-6b9ec46c30d9 | -17.60264 | -57.6041 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 264ec3e7-3354-3219-82db-efa690269baf | -17.61655 | -57.58001 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c7749526-9b53-3121-b3ce-9b8703f16ac5 | -17.62435 | -57.57373 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4417a08f-ca64-3fa6-bedb-ac6798204f79 | -17.62379 | -57.57742 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| cabf4d37-eacc-3044-aef3-563ad6495c0d | -17.62268 | -57.58478 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cb97ec88-56bf-39d8-afd9-bc17cd48a2f7 | -17.60597 | -57.58204 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 82db732b-9c0d-3c71-9e13-4760eb9bdd75 | -17.62658 | -57.58164 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ed837b02-c2ab-3197-b8cd-8278846ad654 | -17.60542 | -57.60832 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4a55b093-37b8-3a42-88a6-40d5808d065a | -23.9337 | -54.08972 | 2024-11-18 05:10:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 19b3cb0d-1fff-32fb-b2f1-0d2b522c8da4 | -17.60208 | -57.60778 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bfb7f419-e84d-39c7-b3a9-71685da57131 | -23.93713 | -54.13254 | 2024-11-18 05:10:00 | NOAA-21 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2c080d62-e6b9-3b95-9a75-20c6bd95c7d5 | -17.61154 | -57.56787 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 538b7140-cbd6-3990-bbe8-46cdd3c716d5 | -17.61544 | -57.58736 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| aeaa1915-580c-341a-a91d-c99b5073787d | -17.616 | -57.58368 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6b0e0a6d-e0a0-3339-a7bb-4ac9d0a4179e | -17.61043 | -57.57522 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2f0e9c5b-6f8c-385f-83ca-8f799d1f15e1 | -17.62324 | -57.5811 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 90724f02-c26d-38d9-b074-b8b2ab11b5be | -17.60653 | -57.57837 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 56658515-b9f6-39d3-87a0-ca66c459a896 | -17.61822 | -57.59159 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d8d9ee0d-f24f-3bc4-b3ed-808124ee1f99 | -17.6199 | -57.58055 | 2024-11-18 05:10:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 09196f47-99b6-3dc9-af31-64a39510e499 | -1.2964 | -51.741 | 2024-11-18 05:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 40f49164-cc96-3530-aa31-30479b71d5ef | -0.89335 | -52.72113 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1918afcc-e22d-3f93-96a0-2a8477164671 | -1.62214 | -53.30027 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c1d568bd-9483-3a02-b6fa-3b4250aa92e9 | -1.76998 | -50.744 | 2024-11-18 05:27:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a542c833-0491-3896-acf1-cb5f66ffe2a9 | -1.29611 | -51.73866 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67430372-1894-3589-91f3-f1b757036fbf | -1.20104 | -51.77195 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4e7e22e-4682-3765-a9db-3a73e3afdb96 | 2.67649 | -61.17524 | 2024-11-18 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25b1a38e-671f-3c65-8c21-cf19da0123c9 | -0.09359 | -51.32227 | 2024-11-18 05:27:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97d98c39-d75c-3757-88d5-3438e718df2b | -1.21502 | -51.78765 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c17a5aca-03ec-3b41-b50e-3a0fbbffa49c | -1.63263 | -53.29637 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fa2fda3-c836-3999-8b14-3754c848cd95 | 0.61349 | -51.77386 | 2024-11-18 05:27:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d4bfadad-8503-366c-b593-8ab813d70838 | -0.18174 | -60.68247 | 2024-11-18 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c832587f-6847-340b-be2c-d0d7964d09f7 | -2.1755 | -50.60958 | 2024-11-18 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4903453e-1948-3cc3-a1b9-9ae72c5df2b3 | -1.76936 | -50.74799 | 2024-11-18 05:27:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9824752-c947-3c99-86e5-92dc8efe0cb9 | -1.44414 | -53.38245 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d6e5edc-110d-3832-b40e-9b91003aa351 | -1.30581 | -51.74705 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e449c817-c54d-383b-bf62-263fc23978e6 | 2.23873 | -55.83146 | 2024-11-18 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e50e85e0-a16d-35c2-b15d-6d47b85a2f8f | 1.06075 | -60.60089 | 2024-11-18 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38acad41-fc1c-3e59-af12-cf678e02d963 | -1.21641 | -55.82027 | 2024-11-18 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88ebe590-fa5f-3c2d-8ba9-6360012c60d7 | -1.30682 | -51.74034 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1ee3da49-abe1-3439-b754-dae84487121c | -1.21237 | -55.81966 | 2024-11-18 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53cae3ca-c359-3710-aacf-19b9d6b5cd5c | -1.27514 | -54.665 | 2024-11-18 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34204b0d-61a4-33a4-acc6-a493fc9d9039 | -0.95775 | -51.72652 | 2024-11-18 05:27:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da3f45f1-2c4f-35da-b3c4-7f513c51521c | -1.15755 | -49.11867 | 2024-11-18 05:27:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 975066bf-594b-39ce-909d-5e23bf8d57bb | -1.29322 | -51.74193 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5220bcc5-42d0-30f2-96fa-8282781a5fef | -1.20839 | -54.17134 | 2024-11-18 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1f8da0b-dbf4-304f-a6e1-5e90975533e6 | -1.36991 | -54.15809 | 2024-11-18 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02d998d2-3f1b-3fcd-8593-8198bfa84840 | -1.15908 | -49.10853 | 2024-11-18 05:27:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db67847a-d10e-3c0f-93a1-f441681f635e | -1.18468 | -55.72869 | 2024-11-18 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fb1d387-8423-3671-8d6b-ce3bc59e5f28 | -1.63343 | -53.29114 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d013beb0-8f24-32bd-bf04-6fe351d76d64 | -1.2102 | -51.78352 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57603756-7365-3c22-a20c-54a1fe224e94 | -1.346 | -55.44346 | 2024-11-18 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 856a924b-7f51-3f54-9a66-eeee3260c6e7 | -1.2991 | -51.73941 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e73c6bac-6013-3f8b-bc8c-f05f7a692b99 | -0.18505 | -60.68298 | 2024-11-18 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd25f784-8319-3b81-b60a-ee596a1ebed3 | -1.2948 | -51.73188 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 260667dd-09a2-3bf5-9cab-2b98e207c3ad | -1.29561 | -51.74202 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0817b39-f631-3101-8822-7cbacbd10ad0 | -1.29375 | -51.73857 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0e668319-e7e2-37dd-8e2e-bae4747f0194 | -1.64573 | -52.77388 | 2024-11-18 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eef8e8ad-a59c-354a-97ff-5ddf30f998f5 | -1.14376 | -51.69527 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9571cfa5-9e40-3668-8829-1b7af8d09a06 | -0.099 | -51.32311 | 2024-11-18 05:27:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bcc29bdc-a599-39da-a2da-1473fa89e955 | -1.43376 | -53.38613 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f704bc1d-8874-3b6e-bf8c-73b03b5bd0de | -1.41506 | -52.42776 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 549b81b7-c5c3-3094-a86d-d39ac7b2b5dc | -1.29712 | -51.73195 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a534d7c4-868b-3cee-bfbe-1a41ae92cf35 | -1.20205 | -51.76528 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c6ca084-0364-3bd1-8943-be90e5e94430 | -2.25374 | -49.04668 | 2024-11-18 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0661b68f-ba7b-3ff3-8ff0-1786de79c896 | -1.62284 | -52.62051 | 2024-11-18 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 892fe826-2efd-3a57-bfaa-e9bcca54a573 | -1.30197 | -51.73614 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 340ed6ad-1a46-32fb-bea4-45dd385ddf9b | 1.18018 | -60.21936 | 2024-11-18 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08726633-ef8b-3cd6-aa7c-92d08c93ff1c | -1.20789 | -51.76277 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69dae977-6353-3128-9588-1af5ad7e4c69 | -1.3981 | -51.98938 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 750c01d9-bc51-333b-83cb-35ed8b56ebd8 | -1.72393 | -53.26889 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9ab3bc0-7717-37d9-b7e8-df1b794134e5 | 2.238 | -55.82687 | 2024-11-18 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f779299-9081-3d01-a8d2-c197b29e9e53 | -1.30147 | -51.7395 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3ea54a73-d826-3303-b0e5-4259dfba31d3 | -1.30339 | -51.74694 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| b06f6f60-5ac6-3ef3-9700-b1445d288da0 | -1.20587 | -51.7761 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16020fab-85c0-32ca-9033-940d4efabf25 | -0.94709 | -51.72488 | 2024-11-18 05:27:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61a2f9a7-1b78-3b84-a5f6-6837216392ba | -1.30445 | -51.74024 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 34bca93d-759d-30d2-b3b3-88fb0527f4a8 | -1.29963 | -51.73606 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 13bc6fba-ea19-31a7-8184-8122eec92fa1 | 0.79696 | -50.2232 | 2024-11-18 05:27:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08da371e-9864-3fda-9cec-3ec16a322fde | -1.29857 | -51.74276 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5041632c-1503-342b-b2c4-41bf488a2589 | -1.43856 | -53.38676 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 54e56708-fb6e-359b-93d7-391d2c74fb17 | -0.95242 | -51.7257 | 2024-11-18 05:27:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a707218e-ad7f-3948-8b7b-b8105a5cf419 | -1.15831 | -49.1136 | 2024-11-18 05:27:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c2e83c-cb9d-3df8-9f1c-e970a1d06cc8 | -1.07497 | -53.36789 | 2024-11-18 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a292a9d-c11b-3b3e-a234-f87988c3eba8 | -1.29428 | -51.73522 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1dde5435-520a-32c4-8625-0f16882fe438 | -1.1384 | -51.69447 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2560fb2-c11d-3104-8a97-01f11c16403c | -1.29662 | -51.7353 | 2024-11-18 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README40.md)
