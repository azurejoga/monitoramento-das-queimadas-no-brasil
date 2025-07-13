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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c068fb-2d6b-3382-8c6c-d44b978e0a8e | -6.83208 | -42.87162 | 2025-07-13 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b10ec4ab-a85b-331c-9444-edfba98e6d11 | -4.85692 | -43.22677 | 2025-07-13 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61f41d32-018b-3930-9dab-24fc3adfd4aa | -6.95248 | -42.73303 | 2025-07-13 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 46e1ff60-e28a-3900-b116-91b815d94cb0 | -5.62454 | -44.27104 | 2025-07-13 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6480842-9259-3b3e-a1ef-f3501c6ea289 | -4.8583 | -43.22364 | 2025-07-13 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 53d58617-c863-3328-a16b-d0939c1a7d67 | -6.26823 | -43.41407 | 2025-07-13 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 597ae9a9-1c70-31ef-b27d-f08626b9074e | -6.27436 | -43.41506 | 2025-07-13 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68138450-8576-3746-9137-0fd8c3145c7b | -7.47508 | -34.8414 | 2025-07-13 03:28:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2034633b-b42b-3268-b438-e4034760f9c6 | -4.85778 | -43.22192 | 2025-07-13 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f381df5-1d43-32e3-8788-c5b96a3d5eb9 | -6.77837 | -43.96967 | 2025-07-13 03:28:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e8448a4-d15a-370e-bdd0-e0e3d6e5d80d | -6.37515 | -37.37383 | 2025-07-13 03:28:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 28c5863b-61e3-3f06-b63e-cab3754fbb68 | -6.6204 | -43.02524 | 2025-07-13 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4da440e0-9dde-3fe1-8c59-00e0ae62d5bd | -3.39795 | -43.37094 | 2025-07-13 03:28:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e72a3ed-2fa8-30c8-af19-dd9d254f726d | -5.74005 | -44.98946 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c16483d2-4660-393f-a700-72dca0a98b34 | -6.78466 | -43.97067 | 2025-07-13 03:28:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b85e089b-c925-3986-a2d1-7be0706703f3 | -6.63622 | -39.32806 | 2025-07-13 03:28:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75ffd6e1-8c56-3d50-93e3-c588a8b310a6 | -4.85746 | -43.2285 | 2025-07-13 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dba5ced3-c0f4-3c36-9145-509c27de8974 | -5.62554 | -44.26567 | 2025-07-13 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6c228c0-7550-3478-b2bc-e165a9c92021 | -6.62117 | -43.02089 | 2025-07-13 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb25b5b9-35dd-334f-a281-882f8ef82363 | -5.73452 | -44.98158 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 398ce3fe-932b-3b65-b735-a83a2b5c68d0 | -4.82113 | -38.85237 | 2025-07-13 03:28:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2bf931d7-82db-3d9d-b963-6854c079bd25 | -6.48644 | -45.26048 | 2025-07-13 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8aef0399-4740-39af-afb2-83042b14cc25 | -5.74795 | -44.98451 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 42d8da42-9730-3f47-850c-8e4c4511784c | -6.64171 | -39.3239 | 2025-07-13 03:28:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dba1f9c2-6c2b-30de-a833-6342b7e4c9b3 | -5.74125 | -44.98299 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 76a45eae-12aa-3c77-a134-1742ca92ab42 | -7.96179 | -37.18569 | 2025-07-13 03:28:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f4a8c31-d3ec-39d3-9249-be2508d1d3b8 | -6.78557 | -43.96573 | 2025-07-13 03:28:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d934902-b255-3e92-b8d7-8a074556428c | -6.65125 | -43.11163 | 2025-07-13 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e54ab45-be90-3db9-a0e7-0cb0224570d4 | -6.26905 | -43.40959 | 2025-07-13 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edd0725b-80d3-378d-bc32-c9574f02b665 | -5.73835 | -44.98878 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| bd16cf55-b554-3a5a-bfe2-a86ea8e3f32a | -5.20831 | -44.3547 | 2025-07-13 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b8d22af-a495-3776-a1c8-3a02584b2b0b | -6.37456 | -37.37744 | 2025-07-13 03:28:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 224028e1-cc5b-3681-9d9e-803ff7a9c4a9 | -6.82544 | -42.87498 | 2025-07-13 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfb8f179-b3a8-3771-83f0-1df6aa609791 | -7.95785 | -37.18834 | 2025-07-13 03:28:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e45f72f5-eca6-3526-9f68-e7d111ab8286 | -6.77928 | -43.96474 | 2025-07-13 03:28:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dfdbc8a-55a8-3615-bb36-8bcc1a0e3df9 | -8.07216 | -34.9761 | 2025-07-13 03:28:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 94899b04-2bd1-36d8-b3a1-a2d76b1f7499 | -5.26285 | -44.87226 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b229ef0c-6ecd-38d9-987b-ee4933ab8a92 | -5.7321 | -44.99466 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 250ea076-86c6-3c87-a808-7f1ad23709ff | -5.73718 | -44.99541 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 787a0045-3f36-3e9c-a9c8-f3fdba951121 | -5.73951 | -44.98227 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 2de74474-0b79-3e0f-8003-6c58a0d30b54 | -5.74675 | -44.99101 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1199fe66-f410-3a8c-b1a0-c7b69594b6ca | -5.73333 | -44.988 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| fd299391-d8de-3472-99b2-45e1cf08eeb6 | -6.65048 | -43.11586 | 2025-07-13 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80038e1f-25f3-33e0-845e-03dc43f64e54 | -5.73044 | -44.99403 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| dece2056-704a-3d0a-bc8f-0666be649282 | -5.73163 | -44.98735 | 2025-07-13 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 902b4e69-6964-3529-97b4-f031de852cb7 | -5.739 | -44.9945 | 2025-07-13 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 5c999101-b3bb-3eff-8f41-70d7ad43b6f3 | -5.7392 | -44.9718 | 2025-07-13 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d8ddc4b2-854c-314d-b32d-908e0eb589fb | -13.8474 | -46.8964 | 2025-07-13 03:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d7b36854-1277-3c5a-b501-9476fa193a44 | -12.70944 | -44.40308 | 2025-07-13 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d143804e-9abe-3193-975b-ddc062e56c56 | -11.72552 | -47.4671 | 2025-07-13 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3052e18d-ea30-3b58-8630-38a2d7d4fdca | -7.98517 | -43.39289 | 2025-07-13 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 99c49545-e2a8-3fc7-84c3-2dd038451740 | -7.30713 | -45.32988 | 2025-07-13 03:30:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1aad6cbb-8f11-31c4-b1e3-3996d9ad9219 | -7.27938 | -45.31582 | 2025-07-13 03:30:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c68572d9-7628-3dd7-abea-7c595b9da3f5 | -8.50137 | -43.28957 | 2025-07-13 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 65d6c8f9-762a-380e-96e7-a998dfb48efd | -8.32522 | -44.93681 | 2025-07-13 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4ccbe21-fc2d-3c35-9a28-134c39232548 | -12.70789 | -45.0267 | 2025-07-13 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e0aa01c-66ac-38d8-8253-aac0d4fd7e27 | -7.3083 | -45.32367 | 2025-07-13 03:30:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3754edbf-a25e-321b-8955-f8aee959826f | -12.70364 | -44.40185 | 2025-07-13 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e7cb0f3-98c7-38b1-a1c6-45cb0717aea7 | -7.28261 | -45.31227 | 2025-07-13 03:30:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64a04c0b-e0c4-3754-9645-c2ce94c98f62 | -8.50649 | -43.28999 | 2025-07-13 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ebcd66bf-f766-3ee5-9493-a290eea8991e | -11.73258 | -47.4686 | 2025-07-13 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6218bd27-4293-3aae-b0cc-1a624602c4a6 | -7.48632 | -43.93573 | 2025-07-13 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f0b155c-573e-36fd-af40-c0ca8234f486 | -7.98598 | -43.38854 | 2025-07-13 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| e1b33e7d-c09d-38b8-9804-fb8c8acd3926 | -7.28813 | -45.31984 | 2025-07-13 03:30:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58356897-7fc3-3680-88bf-e411ffaf38f0 | -12.71394 | -45.02783 | 2025-07-13 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf84a9c0-6d8b-3fa0-a386-8f560d6cb8bc | -8.50213 | -43.2854 | 2025-07-13 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 705e5cb6-eacf-359e-812d-ea12615700b8 | -7.98678 | -43.38419 | 2025-07-13 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 13a74df8-7491-31de-845a-265aec04353b | -12.06647 | -43.49054 | 2025-07-13 03:30:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2336d0b-360c-3136-aa03-01744d9ce8ce | -10.64514 | -44.48583 | 2025-07-13 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ceb0c4b6-e1b3-3fd0-ae4e-a0ad93d316fd | -12.07355 | -43.48383 | 2025-07-13 03:30:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9872cb6f-82ff-3c64-ad29-8a2d6cc5f08b | -11.73061 | -47.46239 | 2025-07-13 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97578361-9ac1-38c1-8b56-ec8a1077b19a | -7.27476 | -45.31691 | 2025-07-13 03:30:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| deaf55ff-0c49-3f99-8bbc-2a3d029ed7a7 | -12.70899 | -44.40094 | 2025-07-13 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b874626-3be9-3fde-b648-00afd46ba64a | -8.50719 | -43.29073 | 2025-07-13 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| de745cb0-56ec-35cf-ae30-db8b48e3d1ff | -11.7291 | -47.4694 | 2025-07-13 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf7d41fd-5c54-3592-be75-e56ff6c6cf68 | -8.32624 | -44.93155 | 2025-07-13 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 534b97bc-988d-33d5-838e-c9e072f7f27e | -12.74787 | -44.41811 | 2025-07-13 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2386ca0d-c381-3dc1-b06f-117eb18afce5 | -12.06719 | -43.48686 | 2025-07-13 03:30:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7737a812-24ec-39ed-9fe0-b587bd080b65 | -8.50728 | -43.28584 | 2025-07-13 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 47e85cbf-2ebe-3ccc-98f5-aa3b384b644d | -7.28144 | -45.31838 | 2025-07-13 03:30:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 858b9662-3ccf-3310-bbf4-6cc3d82cb7ab | -8.50795 | -43.28656 | 2025-07-13 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f4215594-9704-32fb-9cb5-8bffec4dc3e1 | -10.64627 | -44.48486 | 2025-07-13 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 898953c2-9f00-3477-803d-10faac870d23 | -12.70447 | -44.39761 | 2025-07-13 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87ff01f6-ae48-3318-94fb-2d9f74ea123a | -13.88573 | -44.46467 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15b1daf5-2a1c-3878-841c-dd7f5b3b9c38 | -13.88003 | -44.46341 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dc622e7-f456-3d97-8c81-fe3d356a7c22 | -13.83965 | -45.91026 | 2025-07-13 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 350f0b94-a965-31de-a3d5-ea3eb539a7a5 | -13.88129 | -44.46339 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4c17c23-b51a-3b95-8e65-bb6850f99a51 | -13.83657 | -45.89396 | 2025-07-13 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 539cd2d6-79aa-3ab6-9a33-8ba9a0c5bc90 | -13.9182 | -47.41843 | 2025-07-13 03:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eed25169-a905-35b9-81f0-ed653ab2827e | -13.85276 | -46.89498 | 2025-07-13 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b6fdd3a3-60e5-3841-990c-903d0323f1d1 | -13.91145 | -47.42241 | 2025-07-13 03:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a55cbff8-437f-3cae-b1d4-c5976042cca6 | -13.88086 | -44.45927 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61012ca7-7b32-31b6-934c-778e5b441f0a | -13.88168 | -44.45516 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2612f631-30e4-36c5-b821-1eb8bc05cd5d | -13.1224 | -47.28813 | 2025-07-13 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6aee8fb8-4744-3a66-a5e2-58bbf13d3a82 | -13.83863 | -45.9151 | 2025-07-13 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63ff8006-6083-3b11-b827-34f79d828577 | -13.10616 | -47.2972 | 2025-07-13 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ce3b07e-63a0-39aa-b0b3-60aa914c0d10 | -13.91134 | -47.41732 | 2025-07-13 03:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a6545a2-1fb5-3ea6-895c-7bd0e6888608 | -13.88299 | -44.45515 | 2025-07-13 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39ace052-4451-3454-b41f-49999c358a0f | -13.83451 | -45.90372 | 2025-07-13 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f6c985f-cde7-352e-8e33-c87859677ade | -13.85157 | -46.90047 | 2025-07-13 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |


[Clique aqui para ver as próximas entradas](README4.md)
