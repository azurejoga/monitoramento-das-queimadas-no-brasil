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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38fd28f9-fdbb-3672-be32-9cb1f9e91f66 | -20.90579 | -44.90611 | 2026-08-15 11:38:00 | TERRA_M-M | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| d62b802e-f5a0-3faa-9fe1-7ddf759bfbfc | -20.33528 | -46.73563 | 2026-08-15 11:38:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d4761687-61ce-3a88-9897-f51250bf22f8 | -14.4112 | -51.9055 | 2026-08-15 11:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 414cb505-4241-3213-ad21-841d3750298a | -22.45806 | -49.29445 | 2026-08-15 11:40:00 | TERRA_M-M | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 24322b1b-1456-3ed1-963c-96ab9a0bc38d | -16.1216 | -49.854 | 2026-08-15 11:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 9bf714fd-b54b-387b-a6c0-4de27bdd91b9 | -16.102 | -49.8573 | 2026-08-15 11:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 9c6e56e4-0eb6-3e19-8543-c14a7fa0438f | -14.4112 | -51.9055 | 2026-08-15 11:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 17c94b64-5501-3d7c-bbf6-f40aa6bab82d | -16.102 | -49.8573 | 2026-08-15 12:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 5a313ddf-b681-3539-af7d-441bdc5481c7 | -16.1216 | -49.854 | 2026-08-15 12:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 732.7 |
| af93fbd0-6057-3426-ad61-3b5b4deb443d | -16.1211 | -49.8761 | 2026-08-15 12:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 276.9 |
| 1a4d9c4b-0e90-36de-9b30-b9a3ab7cde46 | -16.1015 | -49.8794 | 2026-08-15 12:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1e40bb6b-b6f3-3c99-80ca-30a42fed2a85 | -14.4499 | -51.9004 | 2026-08-15 12:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7e2639d3-45d3-3f20-859b-e795940a8af5 | -16.102 | -49.8573 | 2026-08-15 12:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 77e95f4b-33ba-36b9-aa76-2b3e46524c99 | -11.9347 | -46.3244 | 2026-08-15 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 46274b49-9187-3760-816b-690499464892 | -16.1216 | -49.854 | 2026-08-15 12:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 570.1 |
| 9a17860b-f3b5-33e5-8691-a0b0e17b42d6 | -16.1211 | -49.8761 | 2026-08-15 12:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 267.0 |
| 790d990c-3258-3f4e-9f15-91b46e17d191 | -16.13 | -49.91 | 2026-08-15 12:15:00 | MSG-03 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcaf3bcb-0e1c-367c-a9a8-91e2d8bf6960 | -16.12 | -49.85 | 2026-08-15 12:15:00 | MSG-03 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dfc82433-4961-3b44-b933-920a1416e22f | -14.4112 | -51.9055 | 2026-08-15 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 16e75cf0-0dbf-3831-abd2-00e1f86f5728 | -11.4187 | -46.328 | 2026-08-15 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 138c6829-9b81-3cd5-b75c-a433e96b56d0 | -6.9334 | -43.6333 | 2026-08-15 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e6cc9c6f-7214-3a6b-817d-0c5862b9447d | -11.9347 | -46.3244 | 2026-08-15 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 4bd228b4-81da-343d-8666-f6b23250a93e | -16.1211 | -49.8761 | 2026-08-15 12:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 144.0 |
| b14469c5-345b-3c2a-82e6-89b12e36fa61 | -11.3996 | -46.3305 | 2026-08-15 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 12934ced-f57f-3f9e-be6d-279071f09c80 | -14.4499 | -51.9004 | 2026-08-15 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 356dd5d9-deaf-3763-b32d-fed1309a0b3e | -16.102 | -49.8573 | 2026-08-15 12:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 92b104b0-4120-3e4c-a106-bf06b483fb91 | -16.1216 | -49.854 | 2026-08-15 12:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 451.9 |
| e6acb4b4-779c-3c38-a94a-e1a919fbfd55 | -16.1216 | -49.854 | 2026-08-15 12:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 940158a0-d3c9-3f2f-a3b9-fc9a66883c2a | -16.102 | -49.8573 | 2026-08-15 12:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 28710e03-e482-322b-8b16-0584836ee26a | -10.5281 | -44.8492 | 2026-08-15 12:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 9fb1240b-8f76-3f2d-bccc-4f611d069cf4 | -6.9331 | -43.6566 | 2026-08-15 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8d6ca04d-3377-34a8-844f-31585dd7549d | -6.9334 | -43.6333 | 2026-08-15 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 729babc9-ad7b-3252-98e8-38fecf6a30b2 | -16.1211 | -49.8761 | 2026-08-15 12:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 639caf42-6c5a-3eb7-a0b8-7ca844f7441f | -14.4112 | -51.9055 | 2026-08-15 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 7b3d55a5-d7a0-3b81-989a-75957c40bc52 | -11.9347 | -46.3244 | 2026-08-15 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 624a6287-35fe-364b-a1a9-76d7bb03d7b1 | -16.1015 | -49.8794 | 2026-08-15 12:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8f0528bf-586a-34c3-afad-4d4ad3a6eb13 | -12.446 | -46.6584 | 2026-08-15 12:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 9943ff79-8c56-3d87-8057-fdf30038a51b | -14.4499 | -51.9004 | 2026-08-15 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a8903b8e-e49a-3b57-8601-389a248404ab | -14.4306 | -51.9029 | 2026-08-15 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2ec90d88-330f-3e07-a850-dc788930f430 | -6.9145 | -43.6351 | 2026-08-15 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6e69df11-50cb-38a2-b3c3-162cd6c93152 | -6.9331 | -43.6566 | 2026-08-15 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 711ad1f6-7fe8-3769-b13b-163a0998e939 | -14.4499 | -51.9004 | 2026-08-15 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8f2b2bd2-c0df-3d2a-9e05-da638202f895 | -14.9597 | -46.618 | 2026-08-15 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 135.2 |
| cce3ce60-e25b-3f88-8d00-521d789c73c7 | -14.9792 | -46.6145 | 2026-08-15 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 73049343-b7f5-3102-9cf0-82de62e77daf | -16.102 | -49.8573 | 2026-08-15 12:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 7088bebb-b716-3fa4-8f2d-78605d393721 | -14.4685 | -51.9405 | 2026-08-15 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 638c100b-ba01-397b-a039-5b06c0394727 | -14.4306 | -51.9029 | 2026-08-15 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0ec828db-03ec-3f39-8d08-be27af13fbba | -11.3996 | -46.3305 | 2026-08-15 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3b7f61f2-9107-3fe1-9121-a12776a8cbe4 | -12.3736 | -46.42 | 2026-08-15 12:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cb48ecb8-b389-389c-abb0-c68316bbd4f4 | -14.4112 | -51.9055 | 2026-08-15 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e82c7e21-a597-36dc-ab8d-240246e23763 | -14.4488 | -51.9644 | 2026-08-15 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7dbc03a3-cf32-3e17-8814-a424827d69b3 | -14.4492 | -51.9431 | 2026-08-15 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7db27f8b-d487-3764-9337-b99080766a40 | -16.1216 | -49.854 | 2026-08-15 12:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 524d1351-ef05-367a-8ef0-3f23d917594c | -7.2786 | -44.7091 | 2026-08-15 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5b4029aa-55b8-31df-abdc-f5c518b8be65 | -12.446 | -46.6584 | 2026-08-15 12:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 161.0 |
| ec67f811-3e51-33fb-a073-9b25650f5825 | -11.9351 | -46.3017 | 2026-08-15 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c79a0fc2-a3a5-3cc6-93a2-f06f8703096c | -16.1211 | -49.8761 | 2026-08-15 12:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d3629448-c3ee-373f-8301-7d65cd04dc48 | -6.9334 | -43.6333 | 2026-08-15 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 7068220d-1e9b-345b-8836-aee24494a7f8 | -14.9592 | -46.6409 | 2026-08-15 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 126.9 |
| fb8a4572-ac36-390e-a7a9-a34cd5ec4fff | -11.9347 | -46.3244 | 2026-08-15 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b8042178-6a9c-3423-9e96-b4b294cc5095 | -14.9792 | -46.6145 | 2026-08-15 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| c35f5c5e-2c94-3be7-af01-184c3d7f44c7 | -13.2616 | -54.1835 | 2026-08-15 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3a858f45-eda9-3f97-ac96-7f6393dcb5d2 | -7.2786 | -44.7091 | 2026-08-15 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| ea8be130-0ac1-3937-933e-60b51784a724 | -6.9334 | -43.6333 | 2026-08-15 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 2626d073-5d03-35d3-91b9-39f60277a958 | -10.5281 | -44.8492 | 2026-08-15 12:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5b923269-4522-32d3-a87f-10492b12bef9 | -9.6243 | -48.3635 | 2026-08-15 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 2ed2c716-7de7-379b-9e0a-67e64ee145c1 | -11.3996 | -46.3305 | 2026-08-15 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 36220848-34c5-315c-99dc-4a825748d420 | -13.2804 | -54.2021 | 2026-08-15 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 19b48c5d-4551-3374-8317-b1fd6c66d84c | -14.4499 | -51.9004 | 2026-08-15 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 57cbb141-6999-3dd4-9559-84c8bad9aee7 | -16.1211 | -49.8761 | 2026-08-15 12:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 8f1b0921-2faf-3a60-8f0c-a8ef90013b37 | -6.9145 | -43.6351 | 2026-08-15 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5bfcac47-7c38-3f13-adfc-54810119fc77 | -6.8399 | -45.3621 | 2026-08-15 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| e92b2998-9da3-3863-9b4c-a717b9eca474 | -11.9347 | -46.3244 | 2026-08-15 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| fdfba86c-03f5-3697-940d-951b03e5c4f9 | -14.9597 | -46.618 | 2026-08-15 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c7ac9aab-5b8b-380e-a152-21ca3f6ede93 | -9.6246 | -48.3417 | 2026-08-15 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f1a2f240-808f-3259-96f1-2a46529587e0 | -16.1216 | -49.854 | 2026-08-15 12:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 454.1 |
| 9ac83078-f6d8-30ae-a9ae-67c81300fc8a | -6.9331 | -43.6566 | 2026-08-15 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| e2e6ef0e-3c72-3f1d-89b7-d54acba2faa0 | -16.102 | -49.8573 | 2026-08-15 12:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 9985f72e-c6bd-31c8-af26-9f215875b8a3 | -7.2788 | -44.6862 | 2026-08-15 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 243feba9-2f32-330d-9db2-e798a761f7eb | -12.446 | -46.6584 | 2026-08-15 12:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f82287e0-b71f-30e5-8513-18fea4d5d1c0 | -13.2613 | -54.2042 | 2026-08-15 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 340542f6-7b08-3f65-b1e2-ac69061093ef | -6.8397 | -45.3848 | 2026-08-15 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a09769ab-5199-338b-8e9a-6a35c0a40c78 | -14.4317 | -51.8388 | 2026-08-15 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 4fc86bed-04c5-387c-a6dc-af88161eb334 | -16.1216 | -49.854 | 2026-08-15 13:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 440.7 |
| 470cdc1f-e6eb-317e-a220-3a662a6a314b | -14.4499 | -51.9004 | 2026-08-15 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 76f7effa-6e1e-367a-a35c-9c15c0dc3fb7 | -13.2613 | -54.2042 | 2026-08-15 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 175341a4-d58d-3611-90d9-264c93eea205 | -6.8399 | -45.3621 | 2026-08-15 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 26a30e11-aba2-3493-8fc4-aaaaee351074 | -14.4298 | -51.9457 | 2026-08-15 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d493703e-6ea0-3134-ab69-7e77a681a370 | -16.102 | -49.8573 | 2026-08-15 13:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 147.0 |
| b3bf3dff-5961-3eec-97c6-2bec8f560541 | -16.1211 | -49.8761 | 2026-08-15 13:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 138.7 |
| eac6772a-1cbc-3488-a6cb-8b05f8dff39e | -11.3996 | -46.3305 | 2026-08-15 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 7b3b9292-8dc8-3761-ad54-0581a16d4ab8 | -10.5281 | -44.8492 | 2026-08-15 13:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ed85cc1f-440b-3e0a-b48a-b212c9366d1d | -11.3992 | -46.3532 | 2026-08-15 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b2b49e50-8866-356b-ab23-abec5889bc9b | -11.9347 | -46.3244 | 2026-08-15 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| eae77141-c7be-30e2-a988-bf349355d606 | -6.9145 | -43.6351 | 2026-08-15 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 982aa947-6c3f-3914-91a6-0801ed6dcf22 | -14.4112 | -51.9055 | 2026-08-15 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 47e3354d-b81f-31e9-9a20-2408255f2672 | -7.2788 | -44.6862 | 2026-08-15 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 414198ce-8704-3926-8df2-c79397c41255 | -6.9331 | -43.6566 | 2026-08-15 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f4a2f8b3-df83-3c93-9ad4-4bed83ec6906 | -11.4184 | -46.3506 | 2026-08-15 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 8fb3ccdb-0490-3654-97bb-10d41ed2594d | -12.4456 | -46.6811 | 2026-08-15 13:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |


[Clique aqui para ver as próximas entradas](README51.md)
