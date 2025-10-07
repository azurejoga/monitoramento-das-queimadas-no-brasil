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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87d06b41-1555-3b02-abb0-2c927d911f0c | -21.9079 | -44.8726 | 2025-10-07 02:20:00 | GOES-19 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.3 |
| d7f0c3aa-e15a-374f-9c02-4bceb1b0389a | -4.6873 | -45.8504 | 2025-10-07 02:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 2994aaac-cedc-35ea-8349-c2b581132473 | -6.454 | -44.5978 | 2025-10-07 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f518acf1-ad8e-3c4a-bd9b-b91bbb75da0b | -4.706 | -45.8493 | 2025-10-07 02:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 4b1de88e-1d30-36f3-8c9f-49853f2e8337 | -12.2585 | -56.6842 | 2025-10-07 02:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 1b1a5f43-4796-35a3-bcf2-9f0baf06e179 | -11.9492 | -45.5014 | 2025-10-07 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| deca9a9a-9e27-3ee3-ad7f-bd0b3ebb77c6 | -4.4445 | -43.2397 | 2025-10-07 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| bc14c882-628c-3e61-a430-e811cf4366cb | -11.9496 | -45.4783 | 2025-10-07 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 69dc0f95-c580-3c7f-83c6-afb0bc2ef9cf | -4.4446 | -43.2164 | 2025-10-07 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ae14aea9-9743-3ede-90a6-80fa2d42cd4b | -4.6504 | -43.2038 | 2025-10-07 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0584b72f-11af-35b3-8da8-03927cc725a9 | -10.9109 | -47.1129 | 2025-10-07 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a118f3dd-6123-320d-9661-49121c8344d3 | -10.9113 | -47.0906 | 2025-10-07 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| eb8e6a07-38d4-3f79-8346-eb6c88080ebe | -6.9793 | -42.8798 | 2025-10-07 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 20b7ecd2-d289-3762-8144-8e179539aa76 | -14.7775 | -46.03 | 2025-10-07 02:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 180.8 |
| c583ad0f-de4b-3501-9d1a-a92e008b4505 | -22.1829 | -49.3688 | 2025-10-07 02:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 44f7da6f-0421-3df9-886c-b6bc635a634b | -6.4543 | -44.5749 | 2025-10-07 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f08759b0-c89d-389a-8680-f0bb765fc919 | -14.778 | -46.0069 | 2025-10-07 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a6242152-e352-3eec-aa3f-3c217c4aea53 | -10.8922 | -47.093 | 2025-10-07 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| c907c896-c9e0-3169-a5ea-ba129ab0a44b | -4.6505 | -43.1805 | 2025-10-07 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d5282941-d4af-393d-8556-135b1eee5dcc | -22.1621 | -49.3737 | 2025-10-07 02:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 1ea399dc-dc60-38de-89e3-e848cd2ccae9 | -14.7585 | -46.0104 | 2025-10-07 02:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 5a6beda9-175d-395b-9c37-92a208fe160d | -22.0285 | -49.7042 | 2025-10-07 02:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 122.8 |
| 70e5da62-46dd-37b8-bbff-c7327b86341a | -4.6875 | -45.828 | 2025-10-07 02:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 65f9dd18-063c-3392-8045-d56c43f0c909 | -22.0077 | -49.709 | 2025-10-07 02:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 167.0 |
| c27119f0-ddc3-3621-9c85-b8d4a82f6180 | -5.4937 | -43.0761 | 2025-10-07 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| de77fead-255c-37d2-9fe8-862398373a5a | -4.7061 | -45.8269 | 2025-10-07 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 56590105-ee90-3f59-a9d4-f153d32b2cfa | -6.454 | -44.5978 | 2025-10-07 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 46613fd3-652b-3d04-a4dd-ea087ad0ecfd | -4.706 | -45.8493 | 2025-10-07 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b25771e1-9668-3b70-ab08-7fedc3709bef | -12.1468 | -50.8882 | 2025-10-07 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c5a4dd56-b362-3dff-a074-2dd3cbd50b70 | -22.1829 | -49.3688 | 2025-10-07 02:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 0a1dd9ee-ffb7-3815-ac98-c06e04286aaf | -22.0071 | -49.7321 | 2025-10-07 02:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 179.3 |
| 4e1296eb-4588-3417-8055-e0c4b30a8e78 | -14.778 | -46.0069 | 2025-10-07 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 980e551a-b4fe-3104-a48e-4b2b3d47b022 | -22.1621 | -49.3737 | 2025-10-07 02:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 3a4735b5-88f3-35e9-8f20-d9036174c42d | -10.9113 | -47.0906 | 2025-10-07 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 55a77e8c-1eeb-3fa3-8710-31f62d8899b0 | -14.758 | -46.0335 | 2025-10-07 02:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 671627ca-d45b-3462-acc0-53bfd023e30d | -12.2582 | -56.7043 | 2025-10-07 02:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e2446dd8-4aad-3457-88b6-150650c93339 | -4.6504 | -43.2038 | 2025-10-07 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| fd67e0c9-248c-3bc6-897a-e1d7caf9699a | -4.4446 | -43.2164 | 2025-10-07 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 548ddc64-ef2f-33c4-949a-31d255feaa8b | -11.9496 | -45.4783 | 2025-10-07 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f483e04d-fcb7-3e92-bd17-04da166973e9 | -22.0077 | -49.709 | 2025-10-07 02:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.2 |
| b5249835-6c03-3f32-bfce-dc4c9d64b9f2 | -4.6873 | -45.8504 | 2025-10-07 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 09155033-19c4-3391-8b29-6242621e80f3 | -14.7585 | -46.0104 | 2025-10-07 02:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3c5ca0be-49b2-3022-843c-ea19f46b3151 | -15.0579 | -42.3424 | 2025-10-07 02:30:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 58.4 |
| e933d57a-84b4-3e1b-b3e4-586c156fa98c | -14.7775 | -46.03 | 2025-10-07 02:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 67bb3f3a-3209-3f7e-9825-e23eee6a0355 | -6.9793 | -42.8798 | 2025-10-07 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| c9b8a138-ad18-3a27-97fa-a5df61c606b4 | -10.8731 | -51.0289 | 2025-10-07 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e272dd6c-f94d-3847-a7ee-efeb5ee531ac | -4.4445 | -43.2397 | 2025-10-07 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 83ea9876-1719-32f7-af96-bd3d2f4d47ac | -22.0279 | -49.7274 | 2025-10-07 02:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.7 |
| ba64f314-6aad-35d3-82fd-81ffbdc3fbd5 | -6.4543 | -44.5749 | 2025-10-07 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| add15e82-f4ee-3072-8261-a74fdbc9089a | -3.0864 | -50.5835 | 2025-10-07 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 802403d9-2fdd-3117-b010-6ebaa622d34e | -4.6875 | -45.828 | 2025-10-07 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c32b72d4-8dc6-3876-9b97-13a435ca1719 | -10.8728 | -51.0501 | 2025-10-07 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e224fe63-fddc-3396-b946-e74d33c88f97 | -12.2587 | -56.6641 | 2025-10-07 02:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 388395f4-8a10-364b-9580-011550352f46 | -12.2585 | -56.6842 | 2025-10-07 02:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 72dc5729-abcf-3c66-9e54-3f8720098064 | -10.9109 | -47.1129 | 2025-10-07 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9afacb82-1de8-3b5e-85e2-2f47c5683c6f | -4.6505 | -43.1805 | 2025-10-07 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 76f6bc38-33d6-3af1-8807-0a259467175f | -4.4445 | -43.2397 | 2025-10-07 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2ff427f2-e3ab-38d5-9a16-55ddb7abf3b5 | -4.706 | -45.8493 | 2025-10-07 02:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0464d9c3-054a-35f6-bc8f-0bd857512c2b | -10.8731 | -51.0289 | 2025-10-07 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 52da14f4-afc3-3745-a113-a2b3b3ae80d6 | -12.2582 | -56.7043 | 2025-10-07 02:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| acb5178b-aae3-3476-8a79-aef3d8c28b96 | -10.8728 | -51.0501 | 2025-10-07 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 86078dd2-c9da-3ddf-9f9c-ad11bb8dd87e | -22.0077 | -49.709 | 2025-10-07 02:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.6 |
| 1da04b88-a6b7-3694-b554-c9a59f2f0845 | -4.4446 | -43.2164 | 2025-10-07 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| bee1bb98-9547-30d2-b54e-ea646243f14f | -4.6875 | -45.828 | 2025-10-07 02:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 88a172f4-936d-319b-8ce7-8b13e46a8dc8 | -11.9496 | -45.4783 | 2025-10-07 02:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 30b695fb-fe5e-3cf8-ba6d-89b04844b631 | -12.2585 | -56.6842 | 2025-10-07 02:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| d1ad63cb-ae0e-3792-bab3-38538d81e4e5 | -22.0279 | -49.7274 | 2025-10-07 02:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| add0b95d-7e8a-352f-bf83-2f84d8fbca92 | -4.6504 | -43.2038 | 2025-10-07 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6d06597e-3ab2-39e3-9d3a-1caa332bbed5 | -22.0071 | -49.7321 | 2025-10-07 02:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.9 |
| 61c6d19f-cf97-3a79-9fc6-c471d140454c | -4.6873 | -45.8504 | 2025-10-07 02:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 155.5 |
| d0ea056a-3466-3c77-884c-7817ec7cb2f5 | -4.6505 | -43.1805 | 2025-10-07 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b4853476-9072-3dc0-8cc3-aaff8b66b7f8 | -15.0585 | -42.3178 | 2025-10-07 02:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| b5df544c-96cd-3272-b477-83eca9115997 | -13.5072 | -43.6594 | 2025-10-07 02:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 62ecaaf3-7132-332b-a77b-9f39dca92326 | -4.7061 | -45.8269 | 2025-10-07 02:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b3a92d27-109c-3ccc-b783-9d68ee0706c1 | -4.6687 | -45.8514 | 2025-10-07 02:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 085cd348-9fcb-3872-b11f-29eab40545c3 | -6.4543 | -44.5749 | 2025-10-07 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| bfc279c0-fa93-3239-a40b-e1192fad1956 | -11.9688 | -45.4755 | 2025-10-07 02:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7b463f7e-574b-3808-9abc-4b479f72acaa | -15.0579 | -42.3424 | 2025-10-07 02:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 55535e7c-1386-315a-85de-d17bb9f75264 | -4.706 | -45.8493 | 2025-10-07 02:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| d8ee175c-bffd-338c-887e-67c75aaa6ee5 | -22.0279 | -49.7274 | 2025-10-07 02:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| e52453d7-c361-3a1a-a1f8-206be7574e2e | -15.0585 | -42.3178 | 2025-10-07 02:50:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 27dfae96-946d-3fc5-a090-12fbd4aa94b3 | -11.9496 | -45.4783 | 2025-10-07 02:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 0e820db5-afdc-3aed-955e-66caabbce39b | -10.8731 | -51.0289 | 2025-10-07 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b1640601-7923-310d-bcdb-6c7817203853 | -6.4543 | -44.5749 | 2025-10-07 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e0041a9f-592d-3ae5-b57a-2ef2a7948a25 | -22.0071 | -49.7321 | 2025-10-07 02:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| ef07211c-7093-338e-8d10-ed2f3038d51e | -10.8728 | -51.0501 | 2025-10-07 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6b3124c0-1751-3c0f-b4ca-3a0d8b12af55 | -6.454 | -44.5978 | 2025-10-07 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 681f56e3-5d22-3317-8c58-b4fa66205523 | -10.4102 | -50.311 | 2025-10-07 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 11fa71ab-5d03-3f65-ad4d-24c0b46f09dd | -15.0579 | -42.3424 | 2025-10-07 02:50:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 8f0a783e-0d79-3fcf-8c82-d59aaca7c0d6 | -4.6873 | -45.8504 | 2025-10-07 02:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 294ae6c6-24f5-3406-b00d-ef65423471cf | -4.6875 | -45.828 | 2025-10-07 02:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 1f523703-8404-3e2b-8078-d5cb5162ef18 | -4.7061 | -45.8269 | 2025-10-07 02:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9ea5fa41-0c89-3670-8550-325d6e01fcfa | -3.0864 | -50.5835 | 2025-10-07 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 81feb786-4728-3145-bcf1-d84140dfd79e | -18.157 | -53.37 | 2025-10-07 02:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 10e05b5e-7b5e-3a49-a4dd-1259d9aadfa7 | -4.6687 | -45.8514 | 2025-10-07 02:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5a687ffe-663e-352c-826a-818400baa577 | -22.0077 | -49.709 | 2025-10-07 02:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.4 |
| 06d04b20-4a23-39aa-8393-fa9994b1fe3e | -13.5072 | -43.6594 | 2025-10-07 02:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ce728bbe-9183-3830-a4d1-6a742ed5eb4c | -13.5067 | -43.6832 | 2025-10-07 02:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 835ff01d-9b74-3958-b693-2733a29922c9 | -22.0071 | -49.7321 | 2025-10-07 03:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.0 |
| c267a8e9-fad7-3293-834b-ac31acbcbccd | -4.6873 | -45.8504 | 2025-10-07 03:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 196.3 |


[Clique aqui para ver as próximas entradas](README16.md)
