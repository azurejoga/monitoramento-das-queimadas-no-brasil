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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865c051d-12d8-316f-b156-21ab0d25d2cc | -4.1244 | -43.6064 | 2024-11-19 02:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a84820a2-9126-39f7-b7d7-464ea6dd2e60 | -13.2643 | -56.7947 | 2024-11-19 02:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| e815da08-8fc4-3b4e-a4b8-6de8bbe420f9 | -4.3959 | -47.7618 | 2024-11-19 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b3732fdc-b445-3100-bade-0df4d930e4f6 | -4.1182 | -51.0486 | 2024-11-19 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2d350207-0daa-366a-8f2d-8cfe3564d71a | -8.2659 | -44.0348 | 2024-11-19 02:10:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4f95a1c8-78af-324f-b7d3-f499932fac77 | -13.245 | -56.8167 | 2024-11-19 02:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 42ce10d3-e994-3478-aa36-22c104427e8a | -3.5125 | -50.2343 | 2024-11-19 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 98f2e3a7-f9fe-3d52-9ef4-6c1d8555bff2 | -2.7659 | -52.6163 | 2024-11-19 02:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| cd7b6ae5-cbdd-366e-b4fc-10f9422e27ef | -2.766 | -52.5959 | 2024-11-19 02:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 4707a35b-98e2-348d-9b71-fbd21622000a | -5.9788 | -45.3621 | 2024-11-19 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 9c525e60-4a7e-311f-bfac-07dfbd9fda0d | -4.3958 | -47.7835 | 2024-11-19 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8e1b3703-4471-3d3a-8ff7-a59822d75def | -4.5429 | -48.0151 | 2024-11-19 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4abaf053-a993-390b-9bb5-f87ecd7a1541 | -4.1246 | -43.5833 | 2024-11-19 02:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c628db1d-5c94-3b6e-a3c1-b822f15e5de0 | -5.979 | -45.3395 | 2024-11-19 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 65f5fc1f-a313-3bd3-9b24-239a8b45397e | -2.4293 | -54.6216 | 2024-11-19 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 91758004-f7d3-36a8-b138-54a9ee16f570 | -4.5614 | -48.0141 | 2024-11-19 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 23dd2c45-9675-34cb-ac67-7bee8bf48717 | -4.58 | -48.0132 | 2024-11-19 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9c04d1c3-fc79-3fb6-bb5e-1c3c7fa3174b | -3.5125 | -50.2343 | 2024-11-19 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e553602b-2a2c-3c44-90e7-21c3fe5e0c8d | -2.766 | -52.5959 | 2024-11-19 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0f96e2ae-ff98-3157-a2c7-89061f4631ca | -4.1182 | -51.0486 | 2024-11-19 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1d7d101c-e975-3016-94ee-b66922c36133 | -4.5613 | -48.0358 | 2024-11-19 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d9c5c6d2-161a-3287-b3d6-6ff00e4eecaf | -2.4293 | -54.6216 | 2024-11-19 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| aadd536f-45f8-3dd7-9272-618217ab63b3 | -13.264 | -56.8149 | 2024-11-19 02:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 758117b8-c772-3e1e-a3c0-d082ad167ddf | -4.5429 | -48.0151 | 2024-11-19 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 037d0dac-7efa-3c19-83f0-f6ea042a1c37 | -4.5614 | -48.0141 | 2024-11-19 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| cdb32310-a3bb-378f-9ca1-cb789509cd69 | -1.5869 | -53.7933 | 2024-11-19 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 10530c9c-88fd-3a31-81bb-46f732d461ce | -23.9706 | -54.1372 | 2024-11-19 02:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| 74ea5bc7-d3c2-3264-90b7-cb1bbd93a5f8 | -4.3959 | -47.7618 | 2024-11-19 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 4de55836-3ebc-36f1-8fce-4ea605d58369 | -4.5616 | -47.9925 | 2024-11-19 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| cd540972-60cc-3ccd-b60c-e2282b70000b | -13.245 | -56.8167 | 2024-11-19 02:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 503c1d63-ba8a-3de7-890d-03ef96cda00a | -1.5869 | -53.8134 | 2024-11-19 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ac7c9043-436a-3abd-a490-cd9ab4c0dae9 | -4.1246 | -43.5833 | 2024-11-19 02:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9b8c8fe2-2369-328a-a502-04636a7c0ed1 | -13.2452 | -56.7965 | 2024-11-19 02:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 952d82fc-1848-3ab4-a118-62ab5d73f32f | -5.9788 | -45.3621 | 2024-11-19 02:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 90139495-7794-3d8c-9c6c-5665d9fc9e3f | -5.979 | -45.3395 | 2024-11-19 02:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f35ecf7c-6f78-3777-9782-86905691e124 | -13.2643 | -56.7947 | 2024-11-19 02:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| fc05d52a-43cd-3c5a-b83a-da50b40438d1 | -23.9711 | -54.1148 | 2024-11-19 02:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| c3300fbc-8aaa-3fa6-abc1-f94efdaaad07 | -2.766 | -52.5959 | 2024-11-19 02:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a054a7d0-d403-316d-a4cc-6d2c4527909a | -3.5126 | -50.2133 | 2024-11-19 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0da0d650-7fa9-3d6e-8e61-220891ec8b58 | -4.1246 | -43.5833 | 2024-11-19 02:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a97e2294-38bc-369c-bc70-8d5d6f8239bc | -13.264 | -56.8149 | 2024-11-19 02:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 848afa23-b2d6-3695-80fa-baff203b8745 | -4.5614 | -48.0141 | 2024-11-19 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 7073b1ce-71e5-3792-a3dd-65f48f9df6dd | -13.245 | -56.8167 | 2024-11-19 02:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a368dba6-099d-348b-b033-6f7115e3d100 | -4.5616 | -47.9925 | 2024-11-19 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| b35b7cf3-115d-3b38-a719-53bf503f4a15 | -1.424 | -52.4368 | 2024-11-19 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 21b26369-75bd-328e-a5a4-b98f0fcb9acc | -1.5685 | -53.8137 | 2024-11-19 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 205bb44c-4f9e-3ab2-a23f-ac6f4d70f62f | -5.9788 | -45.3621 | 2024-11-19 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| bf7a51bf-227f-31cb-9665-6943c7bd2468 | -3.5125 | -50.2343 | 2024-11-19 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 624c1c79-d3e1-3802-8203-1de6d78e2a56 | -4.5613 | -48.0358 | 2024-11-19 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3441e282-8a09-3ec2-af6c-78dc534b9ae3 | -23.95 | -54.1191 | 2024-11-19 02:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 638dada7-d1ad-3aa6-ba46-26d83b89b756 | -1.5869 | -53.7933 | 2024-11-19 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 9b6ce100-b48c-30dc-a967-0b68eb0ab63d | -4.58 | -48.0132 | 2024-11-19 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 20a593cb-9d69-3510-b540-30c763479949 | -4.0997 | -51.0493 | 2024-11-19 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7f66fb0e-55c9-36fd-95ae-3787f9538c2b | -4.5429 | -48.0151 | 2024-11-19 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4d53c857-9865-355f-9b91-843c287604d2 | -4.1244 | -43.6064 | 2024-11-19 02:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| b089a747-b542-3eca-9764-475af2577bd1 | -1.5869 | -53.8134 | 2024-11-19 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 1ad2ec5e-6d37-36ad-9cbc-31fd646f38d9 | -13.2643 | -56.7947 | 2024-11-19 02:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d85f6228-cea4-3732-bb78-f8a145271a30 | -23.9706 | -54.1372 | 2024-11-19 02:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 91.6 |
| 9c5aee44-ed59-3e3f-af9e-8f2a2df7e60c | -4.1182 | -51.0486 | 2024-11-19 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ab68932a-b764-3938-9d09-343b0371adf1 | -1.5686 | -53.7935 | 2024-11-19 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 68b8ce64-457f-36a0-bfd8-f2be1bfe9754 | -1.3962 | -47.445 | 2024-11-19 02:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 27f862ab-e439-3c39-abe5-9790076021a5 | -2.4293 | -54.6216 | 2024-11-19 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a979b638-684c-3360-a533-8d3117540c24 | -4.3958 | -47.7835 | 2024-11-19 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 16282736-1de7-33b0-b04d-0a6cac378649 | -4.58 | -48.0132 | 2024-11-19 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| e0be2d7e-5d48-373d-9eee-1b218a43f099 | -4.5429 | -48.0151 | 2024-11-19 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 30d8b274-0a05-37a8-b9fe-e0d4e2c473ce | -13.264 | -56.8149 | 2024-11-19 02:40:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e60ebd8a-b891-32be-a35f-dfcb0f6d41f8 | -4.5616 | -47.9925 | 2024-11-19 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| dbdbc846-2412-34d9-94dc-c7a571001aa1 | -2.766 | -52.5959 | 2024-11-19 02:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| d8ff9245-014d-3ac0-a27d-4b4d35dbc699 | -5.9788 | -45.3621 | 2024-11-19 02:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ac3e50a7-e810-32de-ac81-a8bd57e5c62a | -1.5686 | -53.7935 | 2024-11-19 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 444e10b9-9c7d-3142-9798-adfb8dd10d4d | -4.1246 | -43.5833 | 2024-11-19 02:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e0fe001e-4bfd-370b-9965-0664caaa48e6 | -2.4293 | -54.6216 | 2024-11-19 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4881713f-02bd-32e0-9682-3cc3576d2890 | -13.245 | -56.8167 | 2024-11-19 02:40:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f0b2878f-3a6b-39cd-84cf-7546671fd1fa | -1.5869 | -53.8134 | 2024-11-19 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 9e189c75-4621-3c36-8a24-b7b7e42efa1a | -1.5869 | -53.7933 | 2024-11-19 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 220.2 |
| ac0c38c2-6f13-3c28-a319-2e02d9986d1f | -4.1182 | -51.0486 | 2024-11-19 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 76d6cbac-34ad-3001-b4d5-e8b3ce97bff1 | -4.5614 | -48.0141 | 2024-11-19 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| abb2e2de-f6d5-3f04-b7ae-59f751dd8b23 | -1.5685 | -53.8137 | 2024-11-19 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e0621d14-1e44-3068-98c2-3bb3468562d0 | -3.5125 | -50.2343 | 2024-11-19 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 12eed11f-2bb2-3fdd-a93c-82a18c874604 | -4.1244 | -43.6064 | 2024-11-19 02:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 6679d6b8-3609-3acd-a3e1-e71c581fbaf9 | -4.5613 | -48.0358 | 2024-11-19 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 42951e80-3ee4-3f89-8390-4d6133c9f744 | -2.766 | -52.5959 | 2024-11-19 02:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 81b3d13b-18c0-371d-82f7-fc61258f17fa | -4.3958 | -47.7835 | 2024-11-19 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 06be9118-4425-35b8-bbfc-f2d170386211 | -4.5614 | -48.0141 | 2024-11-19 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| a3bf3d18-1e23-33a3-8be7-ae7e88c3bdae | -4.1246 | -43.5833 | 2024-11-19 02:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 68753679-14b0-368b-bce4-f3066359289b | -4.1182 | -51.0486 | 2024-11-19 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b718e2cf-c8e7-3d6b-9c37-918a244d78f5 | -5.9788 | -45.3621 | 2024-11-19 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 5cdc3609-f98e-3267-b4bf-f268631d082a | -4.5616 | -47.9925 | 2024-11-19 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 575b8ca2-538f-375a-875f-478ae265380d | -1.6053 | -53.8132 | 2024-11-19 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4474b236-4b25-3152-83ea-efd9dd65c5f1 | -1.6053 | -53.7931 | 2024-11-19 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6e4e544e-503c-3e3d-a8a0-3aa8cfd4ce3c | -1.5685 | -53.8137 | 2024-11-19 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 86ea1e44-765f-3276-a05d-e68f1e5e77f2 | -3.5125 | -50.2343 | 2024-11-19 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| aadb4172-9817-3f0a-abad-1a36ec67f3be | -4.5429 | -48.0151 | 2024-11-19 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0b0a4a97-3663-39bc-87ce-273f85e31db3 | -13.264 | -56.8149 | 2024-11-19 02:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| d20f12bb-61a8-3bdc-b333-bb7d514c3234 | -4.1059 | -43.5843 | 2024-11-19 02:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 68c6a9f0-5694-33ef-87de-54b2f4b9657e | -2.4293 | -54.6216 | 2024-11-19 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c1c96415-15d7-37e4-bb06-364543584365 | -1.5869 | -53.8134 | 2024-11-19 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 04f1f35c-9461-3908-a694-1c5d2c8b8afe | -4.58 | -48.0132 | 2024-11-19 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 8b5a9c87-da0f-3b66-aade-ba95fd8b034b | -13.245 | -56.8167 | 2024-11-19 02:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 48355a10-12ac-32ee-ba98-a23208751731 | -1.5686 | -53.7935 | 2024-11-19 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |


[Clique aqui para ver as próximas entradas](README13.md)
