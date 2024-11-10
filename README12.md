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
| 9b11129d-993b-36db-a142-a77d423a92a2 | -4.10869 | -49.12903 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 99729fda-da11-3930-a487-f41ff7bcfca3 | -3.56267 | -53.9374 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 484650db-7d78-39c1-85cc-f31f771fd263 | -6.48629 | -47.51688 | 2024-11-10 01:19:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2e9128b3-b280-3c76-bc15-ee0533dc8660 | -3.25227 | -48.75711 | 2024-11-10 01:19:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 52d36d26-36a2-3693-ba11-887925619e04 | -2.95887 | -54.16683 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ee7c88b-4ec3-32fb-a28e-a1675a42d559 | -3.30363 | -50.13129 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 5bf39310-48ed-37ba-bfcc-94708179e95b | -1.50907 | -52.19233 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7420f3d5-f5cb-39ab-b685-d2f0c19b22b2 | -4.68176 | -45.16284 | 2024-11-10 01:19:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5107318b-039d-3044-9d66-b9588fc1e804 | -2.20108 | -51.88102 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c3e23c16-bf02-3980-93eb-de6ff1b9e04e | -3.72633 | -52.40485 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 69022c8b-dbfd-35c2-84d5-c1c1ae365d1d | -2.62195 | -54.39408 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| bdae81c0-e524-3c8c-a9b0-15024a033e76 | -3.28494 | -53.66369 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d1ac9a25-7d6a-366a-8e1d-d773036dfa1e | -3.36897 | -57.24498 | 2024-11-10 01:19:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ec6dc1bd-dd39-3f5d-ab56-0ae05f86c7c8 | -1.48896 | -55.44347 | 2024-11-10 01:19:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 563d8482-eb3e-37e4-8540-ed61f0e0bc50 | -1.16724 | -52.09056 | 2024-11-10 01:19:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 4ddaa2af-e921-301a-9363-3497bc3e1314 | -4.09405 | -49.11366 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e6ac120c-eef1-3721-bf41-16046b0cd0ff | -2.28483 | -53.75975 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f65dd9d-d668-36a1-a90d-5502832b0aec | -0.95009 | -52.44073 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c635ba80-2a81-37c3-bc25-10ac63147b6a | -3.23111 | -50.26859 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2f87705e-6276-3e34-8e77-6efe951c62ae | -3.95706 | -48.19862 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| d2fc22ca-e9c5-36a2-b219-a57a7353bcae | -1.19454 | -51.99762 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 29c20386-df9c-3cce-84de-2ce131563a9c | -3.17504 | -49.11456 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 28a4b202-d153-3897-96ee-fcc4f1b5914a | -2.19941 | -51.86943 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bba46cf2-d07e-3272-951c-cb8994c93b25 | 1.56637 | -55.93801 | 2024-11-10 01:19:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c2896098-5565-3660-add4-81740a1b9773 | -3.96225 | -49.01429 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b865e996-066f-3bcf-8250-6bbaaee0a4ff | -1.75936 | -53.75683 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 41163902-cbba-3784-b117-8e43d9cf7ca3 | -2.09637 | -48.83006 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| b1ae12fd-820e-39d4-a2be-fb5f185d5cfd | -1.67157 | -55.17259 | 2024-11-10 01:19:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e7a93f29-2852-388c-8c35-3dc333cc366a | -2.71861 | -51.71025 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 42022909-8708-3d65-90f2-973e19e1a502 | -2.76867 | -54.0531 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1685a5a9-ee29-3ed1-a656-8f5e38386c86 | -2.3058 | -50.46493 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 84963069-525d-36c2-9ad5-72f749538177 | -4.13805 | -53.5051 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8f0ad716-7dbc-3bef-8d48-c22ae1dcf87e | -1.13695 | -54.11596 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ad475d6e-b149-3ca4-a67e-fdfca175815b | -1.53056 | -52.20078 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| ecf3f308-679a-338e-93f0-9fa5eab4b940 | -5.0546 | -44.26118 | 2024-11-10 01:19:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 0b572bd4-1b69-3f1d-8b6e-989ef83eb264 | -3.10381 | -49.41559 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 6ad6c3b5-c1c2-32b6-ac6a-f5b5d357e2a4 | -3.26254 | -53.70101 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 64972ea7-acbd-363d-8c01-e0797d0cec6a | -3.32894 | -53.19164 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9fc80de1-460a-3bdd-a2ee-cfa0ab016714 | -1.2442 | -51.7589 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| df63f591-efc8-31ac-8392-29f6fd245cb3 | 0.70054 | -59.87395 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 67912adb-39fa-35d5-83b7-2c2bf1886ef9 | -3.278 | -53.41785 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2b6056b5-6e83-3ec6-bf95-179b8b8125c3 | -3.23317 | -50.2831 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.3 |
| b2edcfd8-033c-3b86-96c5-6e3c08cb7cff | -4.85218 | -46.99932 | 2024-11-10 01:19:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 108.1 |
| bff72d98-7253-3700-bdd1-60613c596d16 | -2.05691 | -52.08875 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 27845569-f948-32c1-a100-cd4369569320 | -3.08595 | -53.88761 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a9e244fe-6d8e-3b52-af14-eaa7f06a495b | 1.57765 | -55.9217 | 2024-11-10 01:19:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7a7412f7-286f-399d-bfb3-43ba473e1ca4 | -3.8891 | -52.39057 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b479ff51-fc64-3375-9d31-3c2d6b57a7ea | -3.73086 | -54.74102 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c560c54-8016-3848-b82f-bb273890e1c3 | -2.27195 | -53.79938 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4437f7e-29de-3f94-856d-cc6998336e50 | -2.77795 | -49.36525 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 81fcd1fc-3abd-3df0-9473-ddcb2990ed0a | -1.20914 | -53.64095 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1bfc6b3c-4fdb-3ab3-8fa9-7f68e5420d63 | -3.35151 | -54.13561 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5469d94d-0229-3351-971e-cb208535e40a | -3.07569 | -53.87976 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b39f4889-78ba-3409-91c3-79f2bd872b6f | -2.41094 | -50.31748 | 2024-11-10 01:19:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 85931c88-7776-3288-a637-77cc66bdc1ae | -3.23727 | -50.31207 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| c02d6c33-cabf-3c42-8444-5e1220f64743 | -4.0658 | -49.21063 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 67799569-17e7-37bb-9d05-79cd71e8204f | -4.84833 | -46.97367 | 2024-11-10 01:19:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 287.4 |
| 6e917b43-533a-395b-87b4-712acfa4a4ce | -2.42348 | -50.48563 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 04059262-6bd9-3066-8fb8-908472c2dc81 | -2.20466 | -47.72659 | 2024-11-10 01:19:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5d14903c-4cfd-3bf5-9df4-38fde9964a4d | -3.11488 | -54.15992 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ebadf05-4c82-372c-b14a-628778520a5b | -0.4068 | -51.49023 | 2024-11-10 01:19:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3b472324-b09a-3868-8b15-948a0c398549 | -2.4179 | -51.96605 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b44ab89a-2747-3ae4-a9d2-8e580bcb08a2 | -1.49621 | -52.0309 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e29459ed-a9a5-37e1-8185-4535db159e66 | -4.85158 | -48.48527 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| efecc999-f7a7-332f-9a16-92ced74515b5 | -1.08014 | -53.64624 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e51d0f4-3b52-3fa9-ba53-d9c641c3b6e9 | -5.01853 | -45.04224 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 8453d3ec-c59c-3771-a7da-8d577fb53430 | -2.32113 | -53.88649 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b6cd6314-de4d-38a7-b0e1-63ad1e587250 | -2.68454 | -51.82808 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a6cdbd45-ece2-361d-b77f-edd8a9545afc | -2.92485 | -49.36705 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 75a85191-0293-33d3-9e4e-a9c88cfd914d | -3.15081 | -54.48183 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 617b9cd4-f144-34a9-b561-ab889fba71ec | -2.20254 | -48.3848 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ea7cd14b-a845-3ef6-909b-04c13c93cec5 | -1.19858 | -53.63239 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 60b483dd-bd47-3b51-8fe0-21b5c468784b | -2.61978 | -46.75127 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 532096fb-a738-347e-a215-19e0a97578ee | -3.48813 | -54.58094 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 65d6924e-afbb-3aa0-8aac-9102e61a2470 | -3.11829 | -45.29268 | 2024-11-10 01:19:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 6137b3d8-8518-39a5-8d6f-70162b45d712 | -5.36714 | -48.25025 | 2024-11-10 01:19:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2be7cd34-73f2-3bcd-87c8-8370de7ff74f | -3.22648 | -53.2516 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7fe18bc9-3e23-34ce-802a-a61922a68a8c | -2.77541 | -49.34793 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d115d554-31cf-381e-9423-1a0d7828ed31 | -1.65932 | -55.08466 | 2024-11-10 01:19:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 37e0c248-daef-3775-88ac-d2bf2e494f14 | -2.18464 | -53.63741 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2bafc729-03ef-3674-b0a1-af2007da18c7 | -6.60786 | -51.14536 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 31035ed0-6c50-3738-88a3-e415a6d537e4 | -3.17288 | -53.85067 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 89083234-8772-3b16-a00a-e40bdea1d9cf | -5.29946 | -47.89392 | 2024-11-10 01:19:00 | TERRA_M-M | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| eca6e842-dc6e-3d95-8b04-dd6fccd9c2ba | -1.67481 | -52.06373 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5a4aaaf3-45e8-3e30-8873-084f41f84489 | -3.10727 | -53.71072 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 64a77c74-bce8-318b-a7da-1b1d31968e0e | -3.58014 | -47.35506 | 2024-11-10 01:19:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 75cb3df4-fdfc-3d7e-90d1-c4f6efaecf3f | -1.05692 | -51.75406 | 2024-11-10 01:19:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f0ef4d30-6e57-326a-9f34-d333314982fe | -2.63118 | -54.65527 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e17ff480-deaa-3404-8ebe-72d85b214422 | -1.83998 | -52.15003 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 81a47c40-1080-3563-9318-a8560fee6938 | -3.22202 | -50.28478 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 399.4 |
| 6d018e87-9738-3786-b5d1-dc16416e7196 | -2.92085 | -51.47508 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 18d70c3c-abc3-33e4-b94b-9e0b30845a01 | -2.93431 | -54.3163 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2bc4a550-4141-3b71-94d3-e858c69995b5 | -2.41718 | -46.31081 | 2024-11-10 01:19:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 3bcb31bc-20f3-3080-957b-d3c67f640b5d | -2.25905 | -47.08926 | 2024-11-10 01:19:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 32e44605-53e7-37f8-8b1d-bc7fd517b780 | -2.58967 | -54.02615 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d4ac6990-85e8-32fe-a1bd-0fc03815acc9 | -1.65222 | -52.04981 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d188455f-8316-30bc-879b-9a602016900c | -1.30765 | -54.67509 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 5ad7da68-9d0f-33e3-b3cf-5c82d1fcc0c6 | 0.62489 | -60.09509 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 746aa332-cb5d-3e0e-a1a2-68b523def1cd | -3.02642 | -49.55944 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c7768634-a71b-3ca2-8864-1954ab7ed26e | -2.23289 | -53.78291 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |


[Clique aqui para ver as próximas entradas](README13.md)
