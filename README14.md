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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f426aba7-16f0-348e-ab34-d7f086c20f6f | -22.78478 | -49.32276 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a5d7cb53-8f16-335c-9af8-91c2011f6a49 | -13.94422 | -54.49918 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dbd2253-f293-3891-80ae-6474ae53623f | -11.96503 | -58.7405 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 582c6751-c967-3653-a134-e5b83cd5f02c | -23.98545 | -48.91793 | 2025-06-18 04:19:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c8acc0f-498d-34e2-8ed5-697169906803 | -19.479 | -49.29262 | 2025-06-18 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f5ded77-9fc1-3533-b6d8-845947dd61dd | -19.47975 | -49.28833 | 2025-06-18 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1dcb225-275a-37c1-83b3-ea808d275b46 | -15.38153 | -47.69582 | 2025-06-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ab26c2d6-6d84-3d60-8478-b09b5eb7f74b | -12.6474 | -54.13121 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b06f950-6b34-31d5-82c1-f0f97d0b5d16 | -19.17218 | -57.54643 | 2025-06-18 04:19:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| aeae4961-4e89-363c-8ee5-b36376706848 | -22.77395 | -49.31788 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a677b905-5a51-3d90-8ca0-71527d5dccc5 | -19.47618 | -49.28762 | 2025-06-18 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 080af0a1-958c-39de-a175-bdb061463168 | -23.33714 | -46.77165 | 2025-06-18 04:19:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4682b548-2b62-3eb7-909b-f23e56562d57 | -23.59455 | -47.4379 | 2025-06-18 04:19:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 93e7b901-c125-3d89-b09d-ea7448fccd3a | -23.39174 | -51.12436 | 2025-06-18 04:19:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d375ee38-76ef-30f3-bf07-7099eae3e829 | -14.43632 | -48.90406 | 2025-06-18 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cab76236-be08-34aa-be49-f4e2213cf03b | -22.78132 | -49.32204 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 26489ccd-6fbb-36d4-a3f0-be6dfa901ecd | -12.50528 | -58.35997 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3f328b4-51e8-3c05-be36-95bed506fbe2 | -14.19832 | -45.50742 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed8524c9-1d31-3805-831a-4839b19d66f2 | -19.78444 | -47.46987 | 2025-06-18 04:19:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bb83e7f-e642-3fe8-ab19-6d749142948a | -12.65689 | -54.11091 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd588176-6ee5-3013-82ab-7e003b9a4722 | -19.58268 | -53.50169 | 2025-06-18 04:19:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5c71974-23dc-3c2e-9ae7-ce66bc980c01 | -14.19992 | -45.51871 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df878522-3bd4-3ad4-a8d2-82e8ee7f3132 | -14.07052 | -53.3811 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2dd14ef6-c06f-3593-ba5d-4c8c6aeecf65 | -22.22038 | -48.70008 | 2025-06-18 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7559a8e-9924-3b15-898e-183d2419e26a | -22.36137 | -45.17433 | 2025-06-18 04:19:00 | NPP-375D | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f02ff37-d7d5-393a-8a10-f6106ebac744 | -21.86384 | -49.74228 | 2025-06-18 04:19:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4bda2878-0477-3fd5-974f-14edd02bd205 | -13.65481 | -53.94178 | 2025-06-18 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ab4338-a04b-362c-9906-e1d6619edf90 | -22.76013 | -47.70115 | 2025-06-18 04:19:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 777a17ec-1fbb-36ea-98c9-b8d97e76a0e0 | -14.19208 | -45.50983 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39664be6-fe63-3382-9f31-d7922213c100 | -13.80198 | -54.29516 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5499a84f-48bc-3173-9966-6b719ed7006f | -13.77686 | -54.19742 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee0a03d3-c75e-3a5d-bd80-721efc39d35f | -22.90173 | -43.7541 | 2025-06-18 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6e0f1eb9-9e24-312e-a8c0-d98dcfc6c6c4 | -14.00401 | -46.1841 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82cbf37a-c1bf-39f0-a017-3036e6b65e9c | -12.27739 | -57.27627 | 2025-06-18 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a94e382d-68c2-3145-b7d6-6baae840e44d | -18.99587 | -52.0867 | 2025-06-18 04:19:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4cd4e59f-96ef-334b-8310-a5443039b403 | -14.43551 | -48.90867 | 2025-06-18 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0dc6faf3-bb76-3691-bbd5-17c9a5fecb02 | -14.02423 | -55.12061 | 2025-06-18 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7a3b6c2-9327-3d9f-8245-c2dfcd7a9a03 | -11.96302 | -58.72466 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e204327f-8f49-301d-9a61-68d04b992aff | -12.64808 | -54.12763 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90932ab3-9be1-3df9-b100-67dff1cac29d | -13.80133 | -54.29852 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef3506b2-9a1d-3a90-8736-4da809e5746b | -19.00086 | -52.08339 | 2025-06-18 04:19:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 867adfc6-2d16-3119-b8b8-ea009f7a1608 | -11.88442 | -54.67737 | 2025-06-18 04:19:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 709bfb46-49c0-3a5e-9548-6ac702f9108a | -11.62344 | -58.29505 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a85159cb-2ca9-3c28-9402-bd63ec7ff7ba | -12.51369 | -58.35464 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39e5bf72-86ca-3188-ba3d-39bb9691ae0a | -20.9896 | -47.38792 | 2025-06-18 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e79b0f8f-8864-312e-8e29-1792eefbed0f | -20.98899 | -47.39166 | 2025-06-18 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 305bfa17-fb69-3b7f-99ec-4c312873bb3e | -12.58045 | -56.98088 | 2025-06-18 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fad20dc-88b7-3f12-8276-9b8cab08b694 | -11.96156 | -58.7314 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0e4bfc98-95dd-3c43-8a75-0c9c21d80f34 | -22.00008 | -46.80161 | 2025-06-18 04:19:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7af6cbd2-fedf-3cb6-8a58-c1d96506f8d9 | -22.78549 | -49.31868 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a44c7365-fe12-398d-985a-6960597f9e81 | -14.20165 | -45.50798 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6a8827d-263b-366f-99bf-5b7a1610e60e | -13.79534 | -54.30074 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e6c57a2-3a56-38da-a6fd-c5df45f99c7d | -20.31068 | -45.58432 | 2025-06-18 04:19:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 427d0444-9352-3e00-9ed5-7c6dd855dc69 | -12.49727 | -55.74605 | 2025-06-18 04:19:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c83c1f0c-166e-34af-83dc-3ca56299ac0a | -21.07066 | -46.22054 | 2025-06-18 04:19:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e296eaba-4849-3488-b77a-85f0469cf047 | -19.17315 | -57.54205 | 2025-06-18 04:19:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0ab5943c-67f0-3f60-b64b-4e81b05aa775 | -14.02909 | -55.12549 | 2025-06-18 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c19b6f7-0f3c-3483-acab-719e0f3ef85e | -12.51515 | -58.34774 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4294ae2-1015-36b9-b1c5-5a9a02112122 | -20.41862 | -45.58376 | 2025-06-18 04:19:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f823883d-32fa-354b-ae8a-60e3198fc5a1 | -14.19441 | -45.51044 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f44999a7-7afd-3197-a018-a2457465db0d | -20.50257 | -45.58599 | 2025-06-18 04:19:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e32a36fc-7f58-310b-a3d8-65f207cee313 | -19.9641 | -47.20132 | 2025-06-18 04:19:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7e34491-58f3-3ecb-b66a-52aeb309e29a | -19.90285 | -49.35147 | 2025-06-18 04:19:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| b18962ab-7b53-3c73-96c8-4542dd0a6c0f | -13.79599 | -54.29741 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 838802f3-cdd7-395d-8da0-3afd2d53905b | -22.77858 | -49.31725 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23a90f32-ba7f-3d94-aa04-42d64a3a9787 | -13.64957 | -53.94078 | 2025-06-18 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b75e4cc-286e-3159-8104-fc1a86b56f8a | -14.2005 | -45.51514 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c666b1c-4c48-3782-9e4c-c7480f050902 | -20.99233 | -47.39227 | 2025-06-18 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d37cdf7-5181-3bae-b9a8-68b4a8933aee | -19.47543 | -49.29192 | 2025-06-18 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b9b55a-a1cb-3e87-901a-7ae9b70098a0 | -11.95939 | -58.7316 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80b28d35-9f14-3ba3-8a82-8f49c2f9268f | -14.19774 | -45.51099 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4fd078c-832b-37df-81a0-77b2d64e27ac | -20.98838 | -47.3954 | 2025-06-18 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e4f8cfc-6317-3fbb-99aa-67dfd046a8aa | -14.1915 | -45.5134 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2cef367-fba0-3280-877d-a83d5ff4902e | -11.95437 | -58.73 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9c06e33-6e37-32d3-a5be-e545e74a2b40 | -21.35863 | -56.12067 | 2025-06-18 04:19:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ec3bba8-d185-302c-b760-d10ad4ea65f3 | -23.61021 | -49.00517 | 2025-06-18 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 36f21134-276a-36ba-a613-f8109e12e0eb | -22.54037 | -48.81181 | 2025-06-18 04:19:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 356141ef-5308-3b21-95a1-161e020c976b | -14.06664 | -53.3742 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40d88d0a-6e53-3607-8e6d-a8b07022b9f6 | -13.77753 | -54.19405 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 913eab52-ddb3-316e-b470-2be436db58be | -12.6562 | -54.11451 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c5dae50-47a5-35c0-986b-617a8b1e5583 | -12.42767 | -54.87027 | 2025-06-18 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14b8bd3f-a6d2-3e59-ac56-f6a9ddc05f63 | -12.53283 | -57.72234 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dcccbef-8d79-3e7b-8965-d83d7d7b63be | -21.13163 | -47.80227 | 2025-06-18 04:19:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| deb98ea2-3ad5-364b-bc1a-2bed4dcbba1c | -21.06733 | -46.21994 | 2025-06-18 04:19:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e6beccd3-481c-3941-9d20-63e4a9561980 | -25.19063 | -49.32546 | 2025-06-18 04:19:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 49f1fdbb-19e4-34d7-a6e0-606647231359 | -14.20441 | -45.51212 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| accb2baa-e1e8-3ce1-bd89-2444ca9764f6 | -15.38223 | -47.69173 | 2025-06-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f5e01f50-8800-3503-b0ed-bdd0c6997bcf | -21.62741 | -43.46837 | 2025-06-18 04:19:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7baca784-3be4-33ff-84de-0663eb8608b3 | -21.62461 | -43.46658 | 2025-06-18 04:19:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 007304cb-2f6d-39f7-86ec-33e2df4a9873 | -19.00008 | -52.08755 | 2025-06-18 04:19:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb7bf2b4-791c-3d63-b4e0-794824bfca3a | -14.07438 | -53.38807 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d985a96-d985-3717-98dd-c2a1ed491fb3 | -11.96004 | -58.73846 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a0c66f7b-d92d-34c4-a4be-09795cfb6b8a | -15.41227 | -47.83451 | 2025-06-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 730e608e-276e-3422-9181-86de4602636c | -25.19403 | -49.32612 | 2025-06-18 04:19:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4f5829e8-8b2f-3874-934e-8f9172598ff7 | -20.23173 | -46.73494 | 2025-06-18 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8364d855-ed90-31f5-8c6f-6292f618c774 | -11.88518 | -54.67346 | 2025-06-18 04:19:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 182fec9a-fd23-344a-9363-813a149c83bf | -22.85443 | -42.98228 | 2025-06-18 04:19:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 218628a4-dbe3-3294-aff6-94018a794d8f | -19.0642 | -53.44985 | 2025-06-18 04:19:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 992dbfe5-5fc0-3a0f-bff1-776b0de8c039 | -14.06551 | -53.38008 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9c65725-0c85-36d8-ab89-9f4b32fa23fd | -20.75799 | -48.52702 | 2025-06-18 04:19:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
