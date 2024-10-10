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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf89775f-4ee9-310d-81ea-43afb8d4cb63 | -7.8099 | -44.90008 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.4 |
| f0be5ddf-ab91-312e-994f-af36aaddc1fc | -7.80857 | -44.90946 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 8332c822-8b60-3fcb-952f-de1285b45400 | -7.79947 | -44.90815 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 08af2b79-8e22-32c2-817b-aae8083b1874 | -7.62878 | -45.26622 | 2024-10-10 12:40:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 08e8332b-577d-3031-b009-73b0d590384a | -7.62586 | -44.83342 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 43b7db10-8e35-39a6-81a9-a9d8c9b6d73b | -7.62451 | -44.84292 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 329e14ca-002b-376a-ad33-7ad41463f2ad | -7.61673 | -44.8322 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7e3a1ff0-aff9-3d5e-a580-49abd9913b3e | -6.955 | -45.21241 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d1f564b2-315e-38bf-8ce6-d8b30f90f2db | -6.94486 | -45.21444 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f3d11943-6ae1-322d-b9a9-de4e4a9b4511 | -6.51372 | -44.88043 | 2024-10-10 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 266dbff8-5a05-3287-b055-62897e38cf29 | -6.5047 | -44.87912 | 2024-10-10 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| af769fd7-d43a-3e34-8328-feca0cc9a63e | -6.50338 | -44.88836 | 2024-10-10 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3f20ed41-902b-33e0-ac1f-3f73e328e4f5 | -7.81799 | -44.19284 | 2024-10-10 12:40:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 7773c02d-040b-35b7-8220-94072ee147d5 | -7.81657 | -44.20291 | 2024-10-10 12:40:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 223aa111-d0e2-3df6-b6ef-d8759d5df427 | -7.21521 | -44.14431 | 2024-10-10 12:40:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5ee751f8-cc9c-363e-8a9d-f98c0cfdaeb4 | -7.20992 | -44.00414 | 2024-10-10 12:40:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cbafd062-cf5c-3cbc-87f8-55d79f4b759a | -7.20049 | -44.00284 | 2024-10-10 12:40:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c23fee81-68da-3414-95cb-3a4b62959461 | -6.93895 | -44.07711 | 2024-10-10 12:40:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e09fe6c4-1b3f-3bf3-833f-ad25403967f6 | -8.53105 | -45.46369 | 2024-10-10 12:40:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fc095998-8aea-3f27-b30b-0a17f103d4a5 | -8.06572 | -44.78043 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 6e0985b5-c932-3f2a-8c49-216613c5605a | -8.06441 | -44.78975 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f4991579-c207-3bf8-ab8e-421883289a3f | -7.93559 | -44.85299 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 965bd80b-a846-3b8e-9524-290ab6785308 | -7.92647 | -44.85154 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e7273f56-9048-3441-9db3-143edd0b6e3f | -7.92514 | -44.86114 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 4f7b164b-177a-381c-a007-8efd27844ef8 | -8.61978 | -44.45021 | 2024-10-10 12:40:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5eac6836-0345-3632-b627-28de0bc9abd1 | -8.61838 | -44.46009 | 2024-10-10 12:40:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3d83ab4e-416b-3048-94b7-12def3c1c3d0 | -8.61043 | -44.44886 | 2024-10-10 12:40:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ff8256c7-580f-318c-bd13-213dc49452c9 | -8.60904 | -44.45872 | 2024-10-10 12:40:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 1aa436be-f2cd-3375-a3ae-5fc0ccc04d36 | -8.60765 | -44.46864 | 2024-10-10 12:40:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 0bfc4802-cc40-31e2-90cf-5b51c8028e85 | -8.36001 | -44.12805 | 2024-10-10 12:40:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a6bc2d0d-7db5-3806-ab4d-b6c0c57e6d1e | -8.35624 | -44.0855 | 2024-10-10 12:40:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 9fbeb39e-62c3-3af8-afa7-62fd729d7373 | -8.3453 | -44.09452 | 2024-10-10 12:40:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4f7250f1-ca38-374b-9fb4-95e403a53e80 | -8.3358 | -44.09319 | 2024-10-10 12:40:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 67b64930-353f-328c-abf1-a767ec358ed7 | -6.38189 | -45.73526 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c3186948-1a6c-3952-82dd-212b5e19e6c1 | -6.37302 | -45.73401 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 42f6cd9e-b7a1-3d87-b604-a82ac8b2089c | -6.3312 | -45.70994 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f79bf06d-2d06-36ca-aefd-dd4ef175c5e4 | -6.32024 | -45.71155 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e6adfaae-1ad0-371b-8b4e-8108b47e4bf6 | -6.29242 | -45.65324 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1cf3e0ce-cfd4-386d-a73c-8fb918a53507 | -6.08763 | -45.98267 | 2024-10-10 12:40:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6cb928be-0de9-37b6-bd0d-6c965e0256de | -5.91182 | -45.42055 | 2024-10-10 12:40:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fef7fb89-83a1-3e7d-b6a7-e0be458cc92f | -5.73259 | -45.31278 | 2024-10-10 12:40:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| babc47ee-16c0-3b33-9b3f-7e2e877ec5df | -5.43123 | -45.04187 | 2024-10-10 12:40:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b0d2b2e8-f8a2-3a0f-8e2c-96d557cd90f2 | -5.4272 | -45.89986 | 2024-10-10 12:40:00 | TERRA_M-T | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0402396d-91f9-3b4c-868a-7e29561851c6 | -5.39665 | -45.9858 | 2024-10-10 12:40:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6d9c19a7-5498-3e52-b559-3a8f23df0cfc | -5.18026 | -45.30742 | 2024-10-10 12:40:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f35c6344-be1b-3336-8648-8f70176e0903 | -5.14745 | -45.09342 | 2024-10-10 12:40:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 310f37fc-2bf9-3ead-b9a8-43f58ae06a89 | -5.1012 | -46.1152 | 2024-10-10 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dba21d63-d73a-3954-90b4-bef867d5eab9 | -5.0959 | -45.82832 | 2024-10-10 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 173e71e2-cfed-3d46-9235-f4801f0fd8fa | -7.58229 | -46.806 | 2024-10-10 12:40:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| be8219fa-1279-3bf3-8a82-1cf2de7a064a | -7.36012 | -45.40474 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f0266217-94b4-3945-b166-43fb860d9780 | -7.29736 | -45.52486 | 2024-10-10 12:40:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd26b04b-8e0c-32a5-868d-a836689b2585 | -7.27187 | -45.37719 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b8219612-b531-3164-b5e4-f05dbcab974e | -7.0572 | -45.26998 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fb94a05b-1a33-3b4e-b0c5-fe9b6d12c88a | -7.006 | -45.36735 | 2024-10-10 12:40:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24a929ab-41d3-39a4-87f2-0b164f9f01e3 | -6.95371 | -45.22155 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 437312cc-4711-34b9-bbce-8401689de3a7 | -6.95242 | -45.23064 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 368593bc-70fe-309c-bc73-afccf8f6af2a | -6.94356 | -45.2235 | 2024-10-10 12:40:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 060775de-c89c-3a89-93c6-61c74409be3e | -8.66508 | -46.58333 | 2024-10-10 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c8e939e0-aed2-320e-bde9-74b946df369d | -8.66379 | -46.59224 | 2024-10-10 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ab92ea6f-6b59-3d2e-abbe-e63981eaa784 | -8.64507 | -46.47141 | 2024-10-10 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6f0f3787-08d8-3312-be70-d41f908c93aa | -8.64378 | -46.48031 | 2024-10-10 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 6982b37b-00d4-32fa-b6ed-0aefbdaf9dab | -8.63492 | -46.47905 | 2024-10-10 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6b8997db-b18a-3d26-bd61-1118169bb44e | -8.62476 | -46.48669 | 2024-10-10 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 14f138c1-6a49-3889-8c24-51c2e4d0c5db | -8.38953 | -46.32572 | 2024-10-10 12:40:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b7f092f-8a25-3362-b5ff-d4862c82b94a | -8.31205 | -45.64366 | 2024-10-10 12:40:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 895a3433-7738-3633-bb99-f5a27237c1ff | -4.90647 | -46.69267 | 2024-10-10 12:40:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 53d5a2cb-f559-3932-bed5-21091e06f12e | -4.90513 | -46.70177 | 2024-10-10 12:40:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 34.1 |
| affe210b-c4cb-35e5-bf3d-bf79f1fbe59e | -4.84988 | -47.52172 | 2024-10-10 12:40:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6b5e59c2-ef1b-37a3-a617-c5dff1c06a1c | -6.46051 | -47.16047 | 2024-10-10 12:40:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9077dfc8-0fef-3a2d-bc73-274992b5aab1 | -6.28372 | -46.98312 | 2024-10-10 12:40:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2346ca8f-6daf-3278-9b14-dbff6f58ba4d | -6.28239 | -46.9922 | 2024-10-10 12:40:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 3b5a62db-d3ef-3cf5-93f9-ff6aad33c0bf | -5.84245 | -47.41299 | 2024-10-10 12:40:00 | TERRA_M-T | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d13a22c8-0027-3ec2-acd4-9dcee72d7e3d | -5.84106 | -47.4224 | 2024-10-10 12:40:00 | TERRA_M-T | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 0475622e-39fe-3d1d-945c-93ca4b578617 | -5.55102 | -46.69917 | 2024-10-10 12:40:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c4084954-f26f-3c42-ac5f-f160f6d593e2 | -7.76926 | -47.03773 | 2024-10-10 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ac2e7ec2-a64d-37c7-8656-11937fbedf8f | -7.76033 | -47.03645 | 2024-10-10 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 43d7e138-e8ce-394e-9879-e8e8d20e29aa | -7.13623 | -47.82856 | 2024-10-10 12:40:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f63e6df-2d31-3ea4-b4f1-1b212af248d4 | -7.01664 | -47.20322 | 2024-10-10 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6ba6d62a-ebd0-3518-8bce-043f6c1d8060 | -7.00766 | -47.2019 | 2024-10-10 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 84d8aec3-6fbe-3986-9ca3-f3b343814087 | -6.99116 | -47.37759 | 2024-10-10 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 3b64e7fb-9361-3614-b13b-de80b796b90f | -6.98213 | -47.3763 | 2024-10-10 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 42c2a875-2c90-353d-a45c-cd410b54dcb3 | -6.98078 | -47.38551 | 2024-10-10 12:40:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c81c4aa7-753a-3b52-83b1-9057744e719f | -6.9314 | -47.72201 | 2024-10-10 12:40:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9d718790-5127-35b3-9407-e279395378ea | -6.93001 | -47.73141 | 2024-10-10 12:40:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9dc000c7-cdf5-34bc-8754-3dc067fdb754 | -6.92364 | -47.71127 | 2024-10-10 12:40:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 766e48bd-1fd2-386b-ab28-049ba5b24171 | -6.92226 | -47.72063 | 2024-10-10 12:40:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7d585493-7daa-3e53-a6fa-43a84850d528 | -6.85807 | -47.34251 | 2024-10-10 12:40:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c494881b-54c2-3404-84f5-90ed77fc4548 | -8.18725 | -47.33242 | 2024-10-10 12:40:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 39933ca3-f854-3bc8-9852-aa19c38e5335 | -8.18592 | -47.34152 | 2024-10-10 12:40:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 3fc43ccc-17cf-3651-afb9-834611487feb | -8.16933 | -47.32981 | 2024-10-10 12:40:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a97d6f34-0fcd-31bc-98f1-b85f2337f626 | -7.97282 | -47.78528 | 2024-10-10 12:40:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| d631b405-ccf6-3905-8f91-47452e8806a6 | -7.97142 | -47.79465 | 2024-10-10 12:40:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e5fdc96b-14f9-3851-8962-568938e94356 | -4.99816 | -48.3315 | 2024-10-10 12:40:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 92634da3-6be3-3c97-b6ed-4f3256c560ff | -5.75282 | -49.25047 | 2024-10-10 12:40:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 37189480-0387-34c4-8680-be5bdf0521f8 | -8.07633 | -49.66491 | 2024-10-10 12:40:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| bb5014ed-e767-3d4a-b630-85b7817152f4 | -13.14349 | -51.66803 | 2024-10-10 12:42:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 65e4d1dc-ee82-3df4-9e71-f0ef47b64c40 | -11.28609 | -51.03251 | 2024-10-10 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 044e7ed9-e78d-3a45-8f55-9f340524c752 | -11.94583 | -50.81037 | 2024-10-10 12:42:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ce2a6c52-8584-3303-b3e6-95f44c0eadaf | -11.29455 | -51.04704 | 2024-10-10 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 870ecc07-73a4-34e0-9e64-3d1cf25280e9 | -11.29658 | -51.03418 | 2024-10-10 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |


[Clique aqui para ver as próximas entradas](README148.md)
