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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 950e42d9-14c3-3261-9de3-16d9313193e8 | -7.44913 | -57.61825 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c033d27a-08ea-35a6-a614-388813b46294 | -9.22561 | -59.7528 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aef02227-607d-3eb0-b0ad-a0c6aa64f216 | -15.02764 | -54.89708 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ce088a2-3223-37c1-8e47-dace6da9f62d | -8.87816 | -62.42902 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bf77451-9ea5-3272-ad03-320b71ba4df4 | -9.20724 | -59.48112 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2b96ff0-c3f6-3a87-b2af-cc62445b5c2a | -7.29165 | -59.63687 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d441706a-7067-3015-9005-237a7a069341 | -14.29707 | -60.38964 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f17c0f50-4387-3914-9bea-6599691988a6 | -12.30287 | -50.00314 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dba37291-d1be-3d39-8410-1622fd646206 | -8.67375 | -62.87344 | 2025-08-23 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e95a4d9-7675-3abb-88ad-7eca942ba30e | -9.87636 | -47.81008 | 2025-08-23 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa892d18-00e5-314c-992f-b987fa20a0df | -12.31525 | -49.99672 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd41b188-cd37-39eb-ba43-5db30f0b0039 | -9.84214 | -56.07475 | 2025-08-23 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfcd3294-5159-310e-b6e3-f4963ab2224b | -13.01997 | -58.00518 | 2025-08-23 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81b8662c-2fb2-3d6e-98cd-a1926966b20b | -7.23249 | -56.84631 | 2025-08-23 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83866db0-b373-35e5-a76f-94509f286ba5 | -10.75777 | -48.25428 | 2025-08-23 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7ab138e-2996-3228-bded-1586af97e937 | -11.11316 | -62.66558 | 2025-08-23 05:21:00 | NPP-375D | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58d7a7e-622d-355f-85fd-885a644f7490 | -14.31655 | -58.5543 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 359b7a8b-f936-3db1-8b49-014539d94158 | -8.53467 | -48.85962 | 2025-08-23 05:21:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04b624db-42eb-34a2-ab00-bd83f0048a58 | -7.05024 | -59.82889 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c1fc502-797f-3243-9c14-7abe0156e1c0 | -14.75593 | -55.99311 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63efde1f-f59d-3e4f-9c85-b051bea37424 | -12.79371 | -48.72006 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1730cdc4-0bbf-30fe-ac01-6dd08a01c99b | -8.88652 | -62.40062 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a9b1069-9a5e-3205-87a1-cb44d1536d12 | -9.16797 | -59.6002 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39709925-d502-3c4d-8810-89439b82b944 | -11.1825 | -55.01855 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 895af2ac-2986-3255-b902-1d4a6b37c89e | -12.58181 | -60.34969 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b37058d8-ac15-3431-ad34-9c0bf5781a87 | -7.10223 | -60.06238 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7da48bf-9374-3627-8cfb-87497a923de8 | -9.18292 | -59.59184 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ab1ead1-01cd-37e6-9902-8a6cb67b5fa9 | -11.1865 | -55.01913 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76f6d62e-fc85-361a-90c9-2b6cdb0d99c8 | -9.46397 | -60.37248 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f70ec04a-c509-3763-9d5f-b67019cc72bb | -13.43909 | -57.17745 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de30c444-b898-3ed7-b389-7f27bdafd0fc | -11.32157 | -55.22559 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 129cd2e2-44c1-35bf-8a48-400de64eb17e | -9.65655 | -59.6357 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f2ac16a-212e-3146-8b5e-3bb1e1656151 | -9.20502 | -59.47361 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7493f943-36e9-3c4f-bbc7-8710000e2ea5 | -9.22717 | -59.76016 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 754c0637-4c2e-3d69-9fc2-d6abdf6123a3 | -9.5148 | -60.52677 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 256d3ffa-0fd1-3e0d-a03d-cad12bd0d85a | -10.63981 | -50.13121 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7f795e88-55d6-346e-8d5d-4a2784272bc2 | -9.94663 | -60.1931 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca09f6f2-c2d8-33e1-976f-5a0b1ccbf907 | -14.66821 | -56.58451 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1eb2d93e-b66a-3686-8cfb-e674b9184f33 | -14.61975 | -54.83951 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 259078ac-fd88-3c84-9923-6735118a7af3 | -9.39648 | -60.54807 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd2d9aa0-7ff2-3876-9a31-6464190c5b84 | -14.61491 | -54.81018 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab7fddb3-9ab4-38d5-ab13-660da01b18ed | -7.55181 | -63.85655 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b12cbfa3-adec-31b9-b112-58836da4d722 | -9.20604 | -60.9281 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47a9a58e-0ac4-309a-ad34-cdb49d1e66ef | -14.75198 | -55.99252 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0af61f10-2a6d-3f0a-ad94-41ff474251f0 | -9.50368 | -60.51031 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12025b94-44b7-3ea9-a8f1-406767b22dcc | -12.15993 | -60.76819 | 2025-08-23 05:21:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a78e1ff8-ee92-34cf-a0c0-fc779bf83167 | -7.28689 | -57.65296 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c53a235d-cadf-37e1-bfad-e939c1bdfa12 | -7.7934 | -61.57841 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9940e3bf-dbd7-3f21-914e-0815386d4515 | -7.54472 | -63.85006 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f12d6251-a2c0-320c-83f3-107f5e3e2bd9 | -14.76453 | -55.98912 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97c89164-3bed-368b-9cb2-112631233f05 | -7.22903 | -56.84576 | 2025-08-23 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 098e1c4a-217d-3a0d-9652-57527c083e3a | -14.75334 | -55.99128 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5eb5c0e-6f22-368e-94a8-8e2003879480 | -7.56954 | -63.43933 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b863e80-86a0-3d05-a612-d910dc9bd986 | -9.16963 | -59.58971 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f32b543-d2a8-3753-9d51-07c12a132227 | -12.58569 | -60.3467 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f6ec29-b00e-3d00-8e90-b422a1502b7b | -14.2987 | -58.55548 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f8bb5be-91c8-3d3c-ad8c-ac0a8724f90d | -10.34883 | -58.60636 | 2025-08-23 05:21:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac74ffc2-bee4-34b3-9045-24c62606e278 | -12.77397 | -48.70597 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ae8d9b23-a7bb-3b51-98ab-0140ee296af3 | -9.19726 | -59.45804 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1fc1941-678c-3b7e-b30d-48c869f3c9c3 | -9.17129 | -59.60073 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d242d17-0c11-312b-a54e-fbbfac68c732 | -7.29916 | -59.62724 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e236e7ad-8ead-38b1-818f-c33729d03a2d | -11.09279 | -58.94633 | 2025-08-23 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41b22536-3b40-309d-9204-86918446eb61 | -14.61239 | -54.86267 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91fe5ad0-cca8-3cd3-8553-2854dd0246fc | -9.21499 | -59.4752 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b8ae272-a4ba-32b7-bd56-34c7341d5e84 | -14.27712 | -60.3863 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70bc597e-bfe5-3844-a050-cce671d2565a | -13.69007 | -57.75445 | 2025-08-23 05:21:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e849955-7046-31a9-ac0b-c033b73134ef | -9.16189 | -59.68159 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e69d055-77c6-3bda-a515-ccec40da75f4 | -13.0213 | -56.83469 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4af51e-29e4-3e27-9767-57d4c05e2c5c | -8.62462 | -63.67171 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4492562-63d0-3b04-9f6f-e5ba1bda931f | -9.9494 | -60.19716 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 96884ef4-84c2-3c5f-8e7e-7d682717f669 | -9.1035 | -61.42871 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21738f61-d1b6-3a29-845e-7e40d14eac04 | -14.27621 | -58.55244 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a5458c-9562-3320-a317-f5b25f9c2cce | -7.31528 | -59.61185 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3728e316-ccbf-31a9-b25f-8de9b26f6394 | -14.47112 | -56.4814 | 2025-08-23 05:21:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41918210-f733-39ca-8549-1b71de8ad203 | -9.51473 | -60.54873 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 194d6ff9-0e55-397a-afb9-eb82e212a692 | -14.61545 | -54.80602 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b594283-8618-3252-a0ba-e91aae5a3e23 | -8.62029 | -62.63517 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00aafe7e-81e9-3973-bbda-062b9255aca7 | -9.17572 | -59.61577 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc4a0bfa-01ea-3d41-acf1-729ecacc8e53 | -13.13404 | -46.90401 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bd2c592-b636-3284-9ee2-121ff40574b0 | -9.65101 | -59.64916 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10f1f90c-b7c7-3df2-bdd4-db48c6b17303 | -8.92903 | -60.71928 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d71cdbc-df64-3ca6-9c52-5ce4a970b702 | -13.3702 | -54.40138 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba114b23-6646-35d4-b4b0-f1ae55b12121 | -13.04442 | -46.32606 | 2025-08-23 05:21:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2332e581-606c-3fc6-a730-20e0c1e124e2 | -9.94944 | -60.17552 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fdd1feb-f675-316d-8b87-cce260367595 | -15.01184 | -54.88498 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 087591ef-19ef-31cf-876c-00416476e9b4 | -9.19893 | -59.46905 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a12d8bf2-a43c-309c-a924-faa85a0afab5 | -14.26875 | -58.5315 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 669d4002-2ca2-3b3d-bcc3-f3a3adead958 | -11.18753 | -55.04071 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee94ae61-a517-38d8-b32b-0b51d20eb1c0 | -12.78181 | -48.71392 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dae5e37b-adfa-3e07-9a74-48f641083914 | -7.80721 | -63.54976 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5859559b-0dee-340a-b0c9-32fde6661fc5 | -7.0697 | -59.21922 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a36d9f0-8884-3458-9c8d-ff0ddfe2c071 | -14.67137 | -56.58989 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fe90124-b0f6-3783-b874-5262c04d5b33 | -14.28887 | -58.52621 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c37c06a-ee50-3ccf-b4ba-6449f77017c9 | -9.60779 | -55.35767 | 2025-08-23 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5d99703-8c32-394c-b209-be173627de03 | -9.20888 | -59.44915 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edd0b709-c573-378a-856d-62c9f1719431 | -10.71273 | -60.40099 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5f8cafe-2ff9-3850-9b0d-8e4b1243bbb8 | -9.95775 | -60.18769 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 034d36d5-e5ee-3d15-be67-603737e76ff3 | -9.94278 | -60.17442 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcaa0dff-c05d-34ff-8a66-de9f3a3db092 | -14.66477 | -54.92318 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d5ec439-7b93-3584-ae50-866f4101bdb1 | -13.47521 | -46.90257 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README67.md)
