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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42684355-80ff-311e-8c01-0ec5da632bda | 0.4466 | -60.3925 | 2026-02-20 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 8e97ed47-2d33-3a24-8081-ea1bff92a883 | -20.9488 | -48.6387 | 2026-02-20 00:00:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| 22cdbf44-b440-3113-90a3-c531cca176d9 | 0.4466 | -60.4115 | 2026-02-20 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a8e1fc92-404b-3638-8bfc-6dc12b2e2138 | -20.9482 | -48.662 | 2026-02-20 00:00:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| e7082d5e-b58e-3098-8096-a7d3880a00a2 | 2.5434 | -60.7357 | 2026-02-20 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a9376652-7581-389a-8fe5-acad3a8c0284 | 2.5252 | -60.7359 | 2026-02-20 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| dd48973d-d7f7-3c61-b14a-dc06f4a21b8a | -20.9282 | -48.6434 | 2026-02-20 00:00:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| 60f30d56-8687-371a-a6f3-5cb50c877592 | 1.3765 | -60.3119 | 2026-02-20 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| fdc49aa1-dd72-3f9a-9214-c57b9336ece1 | 2.5435 | -60.7167 | 2026-02-20 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 75f79ab6-4b4f-37d9-b920-82ceae9a3990 | 0.4648 | -60.3925 | 2026-02-20 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 116.9 |
| c0f0b1c8-c1ef-3e36-8d47-626b350d4b24 | 2.5252 | -60.717 | 2026-02-20 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fb637d74-7d19-3f11-8928-d7b70de8455f | 0.4648 | -60.4114 | 2026-02-20 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 299fac14-4de0-34f9-9641-4356ef1fbfee | -20.9276 | -48.6667 | 2026-02-20 00:00:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 14fe7a32-6d93-3049-ae15-2b1a09ee8835 | -7.0097 | -34.9921 | 2026-02-20 00:06:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d6743f5-a8c2-3a4a-bcbd-37aaf796b325 | -7.0124 | -35.003201 | 2026-02-20 00:06:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 682d82ae-2f86-3153-b4de-f3edc651931a | 0.4648 | -60.3925 | 2026-02-20 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 1131b3ef-766b-386f-8e69-159365f5dfc4 | -20.9282 | -48.6434 | 2026-02-20 00:10:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| ae2aeab7-8e41-30bc-9292-89d53fe6c124 | -20.9482 | -48.662 | 2026-02-20 00:10:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| 1fd7062f-d194-38df-a0c3-5ce44f2ebfbb | -20.9276 | -48.6667 | 2026-02-20 00:10:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.7 |
| daf1e3e4-becd-338c-b098-2b3eb5a56130 | -20.9488 | -48.6387 | 2026-02-20 00:10:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| ed57e57e-54a9-3446-a1bc-1798b9a5e97d | 1.3765 | -60.3119 | 2026-02-20 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 89a798e9-ab35-37be-b7d6-0ae172670480 | 0.4648 | -60.4114 | 2026-02-20 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1ea56136-a6d8-3b5e-b5a1-2ea87e747529 | 0.4466 | -60.3925 | 2026-02-20 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| cfbc9127-0f2d-3055-a55a-c867a884a1c8 | 0.4466 | -60.4115 | 2026-02-20 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0fa897be-0443-321e-856a-d1ed1e3d9da9 | 2.5434 | -60.7357 | 2026-02-20 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b66a99b1-caff-3a20-8299-6145a22e1e9d | -20.9276 | -48.6667 | 2026-02-20 00:20:00 | GOES-19 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| 82798a6f-b6dc-31c2-a049-b1969d3cf135 | 2.5252 | -60.717 | 2026-02-20 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3e9e4956-805a-3cc6-bdbb-537267c661a7 | 2.562 | -60.5648 | 2026-02-20 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| db30f836-d189-3d74-ab59-eda74aa81442 | 0.4648 | -60.4114 | 2026-02-20 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 7914f9b9-902a-3e28-ac78-515dee690a54 | 0.4648 | -60.3925 | 2026-02-20 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 8de1364d-9492-323c-82b5-16f6d51f499f | 0.4466 | -60.4115 | 2026-02-20 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 91a1eb83-09b5-30d6-8527-f9cc7026d535 | 2.5435 | -60.7167 | 2026-02-20 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 4db708b5-6a89-3f8b-9512-60cf766ffff8 | 0.4466 | -60.3925 | 2026-02-20 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 37cf5f0e-a02e-3455-b63a-ba4b6ce787d5 | 2.5252 | -60.7359 | 2026-02-20 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.2 |
| fb77b83f-88bd-3fed-a957-adaf1e9297d6 | 2.5252 | -60.717 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 4eb2ce77-8687-3e8c-ba8d-120598efbddb | 0.4466 | -60.4115 | 2026-02-20 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cb35b878-8ad6-3175-8f09-d47913e1093f | 0.4648 | -60.3925 | 2026-02-20 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 108.1 |
| edcbf160-d7b8-3e80-817d-230e67463a5d | 2.5617 | -60.7354 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8a7c3be9-7ed0-3aed-990c-8651bd243756 | 2.5435 | -60.7167 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 338.7 |
| cf540503-c155-33ba-9029-65ea3257a705 | 2.562 | -60.5648 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 142.6 |
| a3fe93e3-c412-3df5-9b0f-9f12b8b355d8 | 2.5252 | -60.7359 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 115.5 |
| d3adb493-7bf1-34d8-af0c-11d7bdc666cb | 2.5621 | -60.5458 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2785b46e-f194-3ae4-be77-84d6b21343d7 | 2.5617 | -60.7165 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 93d7c6e2-e96b-3406-8c64-5e478a959625 | 0.4648 | -60.4114 | 2026-02-20 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e2850f13-c636-31d5-aabf-3c101f6d7faf | 2.5434 | -60.7357 | 2026-02-20 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 209.5 |
| c5508681-1e37-385c-865a-90edd7092165 | 0.4466 | -60.3925 | 2026-02-20 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ad0ff752-bc23-3eab-a5c8-a3ed17307095 | 2.5621 | -60.5458 | 2026-02-20 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 286f8b97-9a94-34c3-b601-7ecf5c63f65c | 2.5434 | -60.7357 | 2026-02-20 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 13bdb0f6-3d79-3aff-b281-71e5e0927f8c | 2.5252 | -60.7359 | 2026-02-20 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ebbcc803-fee9-3ccc-8244-a744937ed10e | 2.5438 | -60.5651 | 2026-02-20 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| bfab3446-225c-367c-a034-a8dee4ff660b | 0.4648 | -60.4114 | 2026-02-20 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4c7270de-a1b6-39ca-b108-b3faf0a6b431 | 0.4648 | -60.3925 | 2026-02-20 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 3ffc0cd6-96b3-3d8a-9a08-2354e1af3d6c | 2.5435 | -60.7167 | 2026-02-20 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 266.2 |
| 71f8a81e-f06e-3c04-b733-0f62d847ffcd | 2.5252 | -60.717 | 2026-02-20 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 113.9 |
| b902c80d-8788-3e15-8a64-c008d08390af | 2.562 | -60.5648 | 2026-02-20 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 6fcd5a21-bf40-3d62-953b-c918dc4a3061 | 0.4466 | -60.3925 | 2026-02-20 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 9efa8243-5557-36dd-9a92-00aff8d957d0 | -22.02462 | -49.49813 | 2026-02-20 00:41:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 306480a3-463c-3975-a898-4b0b96fdd6f0 | -22.93417 | -48.68425 | 2026-02-20 00:41:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1e7526cb-3dd6-3e24-a530-ef7e73a7e9d8 | -21.88893 | -52.95949 | 2026-02-20 00:41:00 | TERRA_M-M | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 10d3f304-ff55-396c-87f2-e7eed275874a | -22.02635 | -49.50937 | 2026-02-20 00:41:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 08abd071-e6a6-3309-8a3b-9a2a31062f15 | -21.63704 | -48.98318 | 2026-02-20 00:41:00 | TERRA_M-M | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6e9cc0f6-4149-3bca-9aab-84537d87856f | -22.93217 | -48.67198 | 2026-02-20 00:41:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5548f593-d463-3e36-96ff-b874267b965c | -18.97489 | -52.92116 | 2026-02-20 00:43:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6882c8f7-5352-3658-ab1e-9e9ee821cc64 | -18.97618 | -52.93046 | 2026-02-20 00:43:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4f70a9fa-67d3-37f7-99df-54bdb18fe11a | -20.20925 | -50.74755 | 2026-02-20 00:43:00 | TERRA_M-M | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| e0f71314-1006-3be7-bd08-4dc90c4a6e99 | -20.2108 | -50.75783 | 2026-02-20 00:43:00 | TERRA_M-M | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9d93acde-f3d2-3d3e-8741-cfbea0b0ea81 | -12.41929 | -58.40162 | 2026-02-20 00:45:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 415b8688-4d72-31c6-8f4e-e27dcd731cb0 | -12.30867 | -57.3612 | 2026-02-20 00:45:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 691fff9d-68e8-35e7-a3b3-d3ba42b10157 | 1.3757 | -60.30455 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 9ec3df14-60f7-3cc0-8fab-2a85440b5bab | 2.69269 | -60.24757 | 2026-02-20 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b13196c4-53c3-30a8-a592-c2a9dc92d54d | 2.55675 | -60.56238 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 301.2 |
| 2ba288dc-19fa-3b96-9c86-ee7dbee3c245 | 4.14003 | -61.09182 | 2026-02-20 00:49:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 70519e45-16a0-3d3c-9f3f-d0239cbecd82 | 4.46053 | -60.50246 | 2026-02-20 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0800b159-b2dc-3a64-92bf-afcb48d39c7b | 0.45198 | -60.39981 | 2026-02-20 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| f10acfc0-9b86-3f6f-af0f-3e389d18d6d7 | 2.04628 | -60.56072 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 82d6a287-2b34-39e0-8377-bcd2f2991a0a | 0.96611 | -60.22753 | 2026-02-20 00:49:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 900c21b4-54d5-31c5-a841-e89743d5488c | 2.53343 | -60.72956 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 121.2 |
| c08cba0c-9d8f-387c-8dab-f0e7b7ff5327 | 2.55828 | -60.55138 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| ef42ed88-e075-3003-b6b3-3bff1efc634e | 2.55482 | -60.72113 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ff657d34-4738-3b9d-a767-89c2f1b3263c | 0.46198 | -60.40124 | 2026-02-20 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 28665603-e291-35a3-84ba-6d5c0b5e7cfc | -1.6 | -54.00088 | 2026-02-20 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e2a56ed8-cb69-3ea0-b300-be89235eb801 | 4.38022 | -60.62514 | 2026-02-20 00:49:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5e51bb7-09c0-3199-a045-8019e2528c73 | 0.96457 | -60.23881 | 2026-02-20 00:49:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 39ee0434-0676-32a3-89ba-85d18550fb9b | 0.46355 | -60.38978 | 2026-02-20 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 49317940-2ccd-3433-88df-17af9a5eb461 | 3.28888 | -61.52564 | 2026-02-20 00:49:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 428e05a7-8b97-31bd-8e07-eb5fb618ea25 | 0.47354 | -60.39118 | 2026-02-20 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.2 |
| d4fbe093-a61b-3796-86e9-db39ee4b9122 | 1.15793 | -60.32936 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 595becf5-cca6-31f8-b6a5-feb33680124e | 1.36065 | -60.06002 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 124d5788-15a7-33a4-9d4e-91a712dab079 | 1.15635 | -60.34047 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4bf713b8-1105-3c47-ac2d-64e024961f87 | 3.22379 | -61.20683 | 2026-02-20 00:49:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fffb94e8-ccbc-3634-b60b-337b6039d071 | 0.47197 | -60.40263 | 2026-02-20 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 7b7227cc-07d4-3391-81f2-989fd03eb984 | 3.23542 | -61.19016 | 2026-02-20 00:49:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5728a878-1373-3486-bce2-0612b2168773 | 2.5551 | -60.72694 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f65b1bc3-5eb3-3b47-82a4-149d12b28b2b | 0.96729 | -60.23359 | 2026-02-20 00:49:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 85d1a4ca-1dfb-30bc-8405-36950b5eefdf | 2.53186 | -60.74083 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f6be65fd-d53b-3476-948c-f474b611ddb6 | 4.37873 | -60.63566 | 2026-02-20 00:49:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 6cbc6438-e151-367b-bd8a-6b2a5baeee18 | 2.68603 | -60.2252 | 2026-02-20 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f00c05e6-f08d-381e-846f-9dd6a9d1a318 | 3.22357 | -61.20053 | 2026-02-20 00:49:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cc225fd3-2477-3ee3-b543-706c568dc2ef | 2.54179 | -60.74221 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 14cc29b7-4495-3766-bc3a-b9d1fefbca76 | 2.56655 | -60.5638 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |


[Clique aqui para ver as próximas entradas](README2.md)
