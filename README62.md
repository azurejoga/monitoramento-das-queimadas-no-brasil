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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfe2e2b7-7057-3b4b-81cc-4f2ed8f4452b | -5.74557 | -57.60503 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f231880-3724-35f3-b8fc-024fa51cf3ce | -6.43595 | -44.54282 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46c44042-b1f2-348c-b547-722323e12640 | -7.62327 | -45.23635 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ed3679b-cb26-3689-9a73-7ec146d07dd6 | -5.64631 | -51.8393 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f461d117-535a-3e17-aecf-192f87bae263 | -7.62648 | -46.27675 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b92ef63-22cf-3276-98e4-71ba0a31cb2b | -5.65819 | -45.14351 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f73d7c8-79f4-371a-907b-38ddeb35d37c | -7.62529 | -46.28144 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 650f59ce-7a9e-3125-a1ac-fe197a575139 | -7.19075 | -45.16443 | 2025-08-24 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 076597ce-d625-3418-8a28-0f37a896cb57 | -9.1536 | -59.464 | 2025-08-24 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 5fd52803-9a90-377e-8b1a-b3da8908adff | -4.9605 | -55.8226 | 2025-08-24 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c102d5bb-7a91-3afa-8a01-bce2aed94d1b | -20.3599 | -51.68 | 2025-08-24 05:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a9a74a26-d45f-3528-a6ff-42cebbc314f6 | -9.1721 | -59.4823 | 2025-08-24 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| eef59059-2018-3464-ba85-6d38d459522c | -16.797 | -51.3419 | 2025-08-24 05:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 441772ed-abe7-34ab-adbe-19cbc526e22a | -9.0232 | -65.6982 | 2025-08-24 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| e7050a1e-f853-360b-9cac-cae240633f37 | -11.5437 | -51.8454 | 2025-08-24 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1b6e551f-5f69-34f9-9933-a079d462a0a9 | -20.3396 | -51.6839 | 2025-08-24 05:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b440d0ab-e125-3dcb-b142-0f7d76c751a5 | -9.1722 | -59.4629 | 2025-08-24 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9d523732-d004-3a57-ab08-cefb17839f88 | -17.6176 | -44.298 | 2025-08-24 05:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| cc8da171-7ff2-3aaa-8ece-f27cd5af4781 | -20.3594 | -51.7023 | 2025-08-24 05:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 94341925-8c84-3a60-b201-809a93298196 | -17.5975 | -44.3027 | 2025-08-24 05:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| f98563fc-912d-3369-84a5-5f2d08c1b0a1 | -9.0046 | -65.6988 | 2025-08-24 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 10d5ed3a-14d1-3286-9c43-5c91e3885b32 | -9.1535 | -59.4834 | 2025-08-24 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| f5b08f13-977f-32e7-a2a9-9a608e83314a | -9.0231 | -65.7169 | 2025-08-24 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0f76259a-b36d-3abb-82b1-ef64bf68e65c | -17.83537 | -50.8119 | 2025-08-24 05:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b998329-8e50-36c5-b666-aea8d6a538fa | -14.81383 | -47.93863 | 2025-08-24 05:01:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 435433e8-cec0-3b62-b3fc-a83f6441dcd3 | -9.00913 | -65.69389 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 086661b8-0d19-3525-9269-873ef4d8f63e | -14.98335 | -50.18472 | 2025-08-24 05:01:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a9f3f61-b794-33b9-a422-e2b090ed5456 | -13.43976 | -47.03493 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9936a913-3967-3105-b8e8-081e9013129d | -17.83624 | -50.8138 | 2025-08-24 05:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fb1faf04-d90e-3ae0-b6ee-1cb7e96c043b | -14.27998 | -48.03213 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f09f95be-2dac-3156-b716-63f278a07afc | -11.52446 | -50.47531 | 2025-08-24 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a582fd87-aa96-310b-bd62-c66f371148fe | -10.98625 | -59.16329 | 2025-08-24 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5f1cd38-2d97-30db-941b-5ba2510e933b | -9.82086 | -64.26694 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6abab75-f934-33b1-9d49-68897bdd8384 | -13.46868 | -46.88494 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ef88ca7-a6ff-378f-8b57-8a37e7b609f5 | -11.54731 | -51.90271 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc194941-dd5a-36ce-931a-68267b23495c | -13.18546 | -51.92271 | 2025-08-24 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 515677db-c814-3d8e-9b97-f55e98f9a751 | -10.10647 | -57.76643 | 2025-08-24 05:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 530cbbfb-7115-36af-aa4a-fb5628e48c07 | -9.01868 | -65.71914 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e798b19-c890-3abe-a54a-e99b79bfd022 | -13.50273 | -47.03294 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f604694e-8697-3a7a-8b53-875b065e41b0 | -13.38937 | -47.52364 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7dbe579d-9269-3c2a-a803-630515660c85 | -9.64754 | -59.65137 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d07f632d-d3e4-3b83-89ab-02d2da022926 | -10.29627 | -60.53875 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e339ed-1a7d-3096-a1a3-df05a016ec6c | -9.81623 | -64.26883 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b116334-4813-3aca-962c-d5490d15e640 | -11.54603 | -51.9113 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0a8507d-1c75-3002-ae78-068d5467b496 | -11.52804 | -51.85585 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f0d79438-7c49-3cc9-98e3-3be553500872 | -13.05023 | -46.32284 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 639de60a-0cba-3362-9d07-8e29cbcece69 | -9.0099 | -63.63458 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cb24068-5d7d-30cf-8b3a-db7bc8b77402 | -14.34257 | -58.59519 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e499a228-377f-3aab-ac37-0629abfa9c3b | -9.51636 | -60.52066 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ca71af7-48bf-3585-90b2-f64d569a11e5 | -12.73735 | -48.1077 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13ee1ea0-b3a2-391a-8fb7-a2341471c28a | -9.02291 | -65.71998 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a364e3c-75b1-343f-a5cc-1af405262dc6 | -15.31399 | -56.1625 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e02c9ff2-3b96-3318-9da0-9aea9bc7a821 | -9.9582 | -60.1927 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecad6d3e-da2a-3748-b5a3-efb1981d51ba | -9.94372 | -60.17874 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4330272-f093-32ff-9641-206744bd772b | -12.58895 | -60.36067 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e3494c9-f0ff-39a5-8380-ee597abac103 | -11.51945 | -51.86335 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f509fce6-2ff1-3616-a008-87ad663a53d5 | -13.04547 | -45.21324 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c8d8806-90ba-3c20-9c49-956c53468fbf | -11.54301 | -51.90648 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd06e011-717f-3508-97bf-e77f1a0f22e2 | -14.78053 | -55.98253 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d8f5a99-fb81-3a85-8674-6a9db65cdcab | -15.29516 | -56.15199 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ed7c32-67ae-3138-800a-a3321fffe15f | -13.18584 | -59.1755 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfc43100-fbb6-3917-b5c6-776f6ea42c35 | -17.60407 | -44.30013 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9966f299-16d0-36b9-a4de-f9cf4c56fe9e | -9.51951 | -60.52532 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3b7a662-cc7c-3dd3-81a4-31e8721e3eb3 | -13.61843 | -48.16702 | 2025-08-24 05:01:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c789e1b1-9fc5-3ab1-b6ca-dda808948b82 | -9.02374 | -65.71548 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c27b8b18-2cd8-3157-af24-d172aa9e9f7f | -13.04306 | -45.23354 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6471cf82-6dae-3bcf-bcbd-f48dba5f3f8f | -10.41569 | -64.42157 | 2025-08-24 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 275b19a7-bcaa-3011-a2ac-0ee451c54ae6 | -9.00933 | -65.70317 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4848cb71-228a-37fb-ab14-b19fd010f1f4 | -13.05292 | -46.32036 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccf72025-9c5d-3f9a-a01b-a9e921309e71 | -15.64751 | -52.71491 | 2025-08-24 05:01:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a19a674-e7a3-3e05-b1a9-daa5e402a543 | -13.04354 | -45.22949 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26376169-8325-3121-8ff1-d2ea7705c52b | -12.59147 | -60.35744 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7349e25-91f0-306d-ae17-d6e809d48351 | -11.6232 | -55.6936 | 2025-08-24 05:01:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7461c3d7-2926-3477-8bb1-60ffc34b8b93 | -16.79046 | -51.35418 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f32b2ea5-bd58-3c7b-bd50-e80e8a7dd8cc | -15.32454 | -56.16059 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8361dc6-52d1-35da-bb0e-838e22e81c65 | -15.29736 | -56.15971 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 22c2c4b3-dd2e-37a1-b819-abbbeac2164c | -11.69112 | -60.18778 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e50c9a62-5f3c-3c54-9407-30b7f9ad389f | -13.49797 | -47.02925 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87f486e6-5d46-314b-ab8f-715751a23544 | -13.4452 | -47.0332 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1ba4d5c-9e0c-3ed8-bb3f-761ce65a99d6 | -11.90366 | -47.12067 | 2025-08-24 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5751f5f-c655-3047-a58c-26950c9a11bb | -15.1304 | -48.63719 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c64465d8-8148-32c2-adfd-7e7a5e8f5547 | -13.46284 | -47.01736 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d6a0123-f887-3a13-8543-bc6066638d2f | -16.79552 | -51.34724 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77185a4e-5d67-3cb1-8f4e-bb3e0b087bb4 | -9.01618 | -65.69987 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3f02ff92-2843-3d82-a115-ae236590fbb4 | -11.53537 | -51.85689 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 66cd0e21-1473-3f2a-b921-1a7271e58a53 | -15.04803 | -48.52034 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ded2516a-ac3b-3497-88c3-78c93adce40e | -9.33129 | -63.19893 | 2025-08-24 05:01:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70d4622b-3a1e-33df-943d-8a26b7350c15 | -15.33536 | -56.23534 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a9218af-c954-35b9-9789-2ac266c28311 | -11.52525 | -51.92562 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1c0387e-49ee-3e5a-bce5-1e42a79ade5a | -10.1029 | -57.76583 | 2025-08-24 05:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d41fc8-8328-36c7-bcae-51d8c08d74a2 | -11.69512 | -60.18841 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e93369f-d9cb-31bf-a7ee-cbe218d15aa8 | -10.41914 | -64.43307 | 2025-08-24 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa7c0e46-a26e-3654-b895-14017dcec24d | -16.48738 | -46.75395 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5b3faab-9043-3c11-ba3f-0924358f9bb0 | -16.79618 | -51.34664 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f2623ad1-43d8-3e73-9aaf-b7c300329968 | -11.53777 | -51.86607 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8cccd34e-399a-3702-b34b-bf466e2b4bf7 | -14.78109 | -55.97896 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23a7eb69-275f-37fe-8e50-fd2afcdf43fd | -9.33075 | -63.20194 | 2025-08-24 05:01:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90987d82-e1e9-3087-ae0a-90581c65a1db | -12.73236 | -48.11845 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd82b3df-753c-308c-832e-7755d98050d1 | -9.51282 | -60.51595 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21b9e755-6cce-3412-9804-6650f6b334f5 | -13.04258 | -45.23756 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README63.md)
