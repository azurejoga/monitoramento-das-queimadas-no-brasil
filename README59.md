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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4e5ffa8-e866-349f-8800-8b0799d3a5fb | -22.01651 | -49.707 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9c6aff5d-1451-3e96-b742-3edfd95b92bb | -22.40016 | -49.97736 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac275af2-015f-348f-8ee8-8cfc60bff508 | -21.60487 | -47.36983 | 2025-10-08 04:21:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a5a0b62-fec8-33b0-adcf-f9e4610612be | -22.01145 | -49.71484 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1cbf42a4-29d7-36af-88f9-8eed1957121a | -22.38836 | -50.01252 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec415b0d-5079-3841-9a04-5e3c2daeb9ae | -21.59485 | -47.36799 | 2025-10-08 04:21:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c833557-5d5e-39cf-a8d7-2dccdb41d51c | -21.41327 | -49.68317 | 2025-10-08 04:21:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a56ae122-cfa8-3a78-8249-3c6bf267347c | -22.18311 | -51.36972 | 2025-10-08 04:21:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d09962d7-dd5d-39ad-bed2-4341cb962a8a | -21.89969 | -44.89269 | 2025-10-08 04:21:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ddfa703-29c1-3e75-bf8d-c0467dcf1406 | -21.84857 | -45.38006 | 2025-10-08 04:21:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 632f0f8f-21ae-3b4d-9d4e-ebd929995360 | -21.60547 | -47.36609 | 2025-10-08 04:21:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b0297fd-021d-3110-899c-86c25cee27d0 | -21.95493 | -44.66067 | 2025-10-08 04:21:00 | NPP-375D | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 39c77929-cdef-32a2-92d0-6480adc74c8f | -22.383 | -49.97982 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 957503ad-b23e-327f-a1c5-1e98b2f1ecb7 | -21.25751 | -48.80697 | 2025-10-08 04:21:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 07a819c1-54db-3f2f-82f0-1dfa9f5b4950 | -22.38249 | -49.96168 | 2025-10-08 04:21:00 | NPP-375D | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56f8a32c-ec92-38a7-b586-7565970be963 | -22.39595 | -50.02141 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f755309a-c0af-35ca-91c5-c04d1ae36716 | -22.37588 | -49.97831 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42d5c7c8-203c-3945-9893-c5b047a8921d | -22.37945 | -49.97902 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3159edd3-f5a9-3a68-ad85-11f76fc72ec9 | -22.30089 | -49.92257 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 670dcc6b-b724-3b32-b74a-cf738cb18cce | -22.01575 | -49.7113 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| abf3e299-cbb9-3eac-80a8-7ba4a07f8ef9 | -22.30877 | -49.91972 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 04919afb-ff8a-3e97-ae19-45a7c75985e4 | -22.39402 | -50.02241 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a4597bc9-e23c-3ef8-92d1-3c95a2e2360e | -22.29846 | -49.92486 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7153db67-c4f3-3350-aeca-14db1c76b17e | -22.30445 | -49.92329 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d95e8282-f792-3378-a078-f8d8697b77fd | -22.39446 | -49.9776 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bc3f401e-2c5f-39ef-b959-dc24e5e33e7b | -22.3037 | -49.92746 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 05467708-720a-38e6-845f-51e7dec02c15 | -21.84794 | -45.38097 | 2025-10-08 04:21:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3fe40562-e524-33eb-8adc-30bb57b59b73 | -22.30202 | -49.92559 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ba83d26a-07b2-3cdc-ac8e-8dda9c5f7ffd | -22.015 | -49.55392 | 2025-10-08 04:21:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 320be660-ae2b-3034-826d-2e2024817f13 | -21.41402 | -49.67886 | 2025-10-08 04:21:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 14baeede-de90-3e0d-9747-8287d4e703bf | -21.61489 | -47.37167 | 2025-10-08 04:21:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81f1b731-ee23-3285-b9a5-d096a40f39a3 | -21.59819 | -47.3686 | 2025-10-08 04:21:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28febcfd-c9bc-35a9-a8fa-a5542bb393e8 | -22.39193 | -50.01324 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 83ca60b8-0553-3d1a-854b-4cce370b06b2 | -22.39388 | -50.01231 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1361c8ae-bdc6-3c08-a753-9d437b61adf4 | -21.95684 | -44.65963 | 2025-10-08 04:21:00 | NPP-375D | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 77d68124-acff-3feb-97dd-82a2e664e23f | -21.61703 | -45.2953 | 2025-10-08 04:21:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 31272425-3f17-3814-a3b2-fd293f8a628d | -22.01247 | -49.71597 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0571f711-8299-349c-9872-43fbf253e6b3 | -21.59425 | -47.37173 | 2025-10-08 04:21:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f440672-b407-3f7f-9bb6-31617458f1ed | -22.30129 | -49.92979 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 78941bf8-e935-3e4e-87b3-0e03bcbba857 | -22.31234 | -49.92039 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ac6f70b2-5e6d-3f40-bf6d-61eaf005697e | -22.11061 | -45.25592 | 2025-10-08 04:21:00 | NPP-375D | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 55edc648-6502-3b9d-b538-58b060cc70a0 | -21.53038 | -45.43402 | 2025-10-08 04:21:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fed57aab-3e68-3ce9-80f1-454071e3c98b | -22.01298 | -49.70626 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ddfcf1d-7111-3959-829a-3d91f1c75e46 | -22.01131 | -51.89719 | 2025-10-08 04:21:00 | NPP-375D | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f6cd158e-ce5a-33cb-b977-d712c9a8c53e | -22.01396 | -49.70737 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dc3605ea-b7d5-393c-bbf2-b53993a5a482 | -21.61823 | -47.37229 | 2025-10-08 04:21:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adab0a9a-e9f4-3e31-9f42-4512e0ff4057 | -22.2267 | -49.72763 | 2025-10-08 04:21:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e2de1f23-e37a-34a4-9398-247283466160 | -22.01234 | -51.89173 | 2025-10-08 04:21:00 | NPP-375D | PIQUEROBI | SÃO PAULO | Brasil | 3538303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 97da0216-7f80-3799-b905-ceee35dd37ab | -21.60153 | -47.36922 | 2025-10-08 04:21:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da7659de-658a-3291-9f7a-ea1317454394 | -22.3909 | -49.97686 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4fa0449-19c7-3365-98dc-83310b8fe490 | -21.84916 | -50.55873 | 2025-10-08 04:21:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ee61fa4-b25a-3a3f-8a9b-a940807afcda | -22.30015 | -49.92673 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e22fecf0-10c5-3827-94b2-99455f09f0fb | -21.84629 | -44.99323 | 2025-10-08 04:21:00 | NPP-375D | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4896d477-38b0-3f91-a331-d148e4dedc96 | -22.00894 | -49.71524 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c236353-4f6b-39ee-81e0-523a2770122f | -21.91148 | -44.99871 | 2025-10-08 04:21:00 | NPP-375D | CAXAMBU | MINAS GERAIS | Brasil | 3115508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 80c2a334-c1e3-33f3-8e0f-5c6d37836675 | -22.22784 | -49.72531 | 2025-10-08 04:21:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 992bbe95-2fd5-38ba-8a3c-d3966f8abb47 | -21.57907 | -48.33291 | 2025-10-08 04:21:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ff0bca5-9ce5-3a3d-87eb-081e429f59d7 | -21.5988 | -47.36486 | 2025-10-08 04:21:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7340968-3d0a-3ab3-bacb-1633db8551f9 | -22.38379 | -49.97534 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3d175a7e-090b-3c2c-a358-025b52d10ecd | -22.39031 | -50.01159 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dfddee09-fb73-3fba-b4e8-07bc0de87f47 | -21.72844 | -46.99606 | 2025-10-08 04:21:00 | NPP-375D | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20d36a43-e92a-3892-a87c-12a66d1b77f0 | -22.38403 | -50.0161 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb946891-aadc-3473-8f5a-c328b0bb06e2 | -21.35211 | -46.45313 | 2025-10-08 04:21:00 | NPP-375D | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca5344c3-6d3f-39cf-a624-b3d3cdf7a1c3 | -21.41683 | -49.68388 | 2025-10-08 04:21:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ded89b73-45c5-37c9-ba21-c377279b625d | -22.3595 | -50.02936 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56d31720-8a86-385b-ae7f-40c08491a4a7 | -22.11172 | -45.24839 | 2025-10-08 04:21:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 498221d5-a46a-382e-b2fb-7539d06e76e0 | -22.38606 | -49.96235 | 2025-10-08 04:21:00 | NPP-375D | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0fd4d9ae-a318-352a-aedb-07a6c92796ad | -22.39803 | -49.97832 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2303c01b-06ec-3c89-90cf-24a50f079b94 | -20.63226 | -54.74882 | 2025-10-08 04:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92394098-a392-39ad-af3c-318b8e95cc15 | -21.41759 | -49.67958 | 2025-10-08 04:21:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e43d320f-849c-3d96-92a8-f42e3d8c1265 | -22.01322 | -49.71167 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b00df9ed-64f0-3d58-a17f-2439fe2a428e | -22.10834 | -45.24762 | 2025-10-08 04:21:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 87eedd6f-344b-3ab0-b787-c629a97dcd1f | -22.38655 | -49.98063 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e68ebf54-441c-39a2-8f94-a5a37a9738b6 | -21.59759 | -47.37234 | 2025-10-08 04:21:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9b23f0c-28aa-3c94-8e00-bf233f5c6b5c | -22.38734 | -49.97611 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a4a9811-0e0d-309d-9a46-91c88e44494a | -22.36385 | -50.0257 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ff2f40c-9829-3790-9982-3d65a357d0eb | -21.72511 | -46.99545 | 2025-10-08 04:21:00 | NPP-375D | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 636e1727-84d2-3619-8e7e-973cf91ed49b | -22.30275 | -49.92141 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e4631f3-8baf-3a66-b9e7-bf607df38122 | -22.39477 | -50.01815 | 2025-10-08 04:21:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a9f9d796-9dec-38bd-ac14-54ca3907543c | -22.01221 | -49.71055 | 2025-10-08 04:21:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0c714ea7-9022-3a68-b781-c31465375db3 | -15.321 | -46.1622 | 2025-10-08 04:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 968ee1a2-0a38-32e1-9243-eec11b29b0fa | -5.1414 | -44.967 | 2025-10-08 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 72f96662-2c5b-32df-99d6-827f7222a031 | -3.09231 | -50.57101 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce104d26-fede-39ba-92d0-61c24abf161e | -3.08484 | -50.57367 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d30645-caa9-39bf-98f4-04461cba7e89 | -1.977 | -50.24369 | 2025-10-08 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fef14c2f-1ce0-3a10-bd2b-7a6188ede5d8 | -2.44003 | -48.431 | 2025-10-08 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ab6925e-2b2d-3a12-8f21-b17b40568dc8 | -1.87214 | -55.15889 | 2025-10-08 04:36:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 932a1b3c-b212-3ef0-b206-97433ec81f55 | -2.87261 | -48.70308 | 2025-10-08 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d736201-3f72-3417-b804-329cac3d062a | 0.92486 | -51.12673 | 2025-10-08 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fdb43e79-ab97-3d4a-8d8e-9feb801b1c74 | -2.29455 | -47.99591 | 2025-10-08 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bab6eb4-1e10-38e6-9a16-84dc021d8e55 | 0.92989 | -51.13471 | 2025-10-08 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 037fd261-ad12-3620-b15a-408a6276f712 | -3.14553 | -50.30315 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d81f06a1-68f0-3bd9-95d2-f20f8983192f | -3.11088 | -47.79417 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| adbd9fa3-60bf-309b-8bd6-5da55ae5110f | -4.0565 | -42.51046 | 2025-10-08 04:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1e60d12b-ff1a-3f46-aa02-c52f8eef9b7c | -3.14611 | -50.2995 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2647ed57-0d44-369a-808d-7f16482ccceb | -2.56181 | -48.9718 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6456b3dc-9aa9-3edb-9b52-0d980fa3316e | -3.01904 | -51.34715 | 2025-10-08 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed1b25e0-c776-3381-80e0-323f19cda9a1 | -2.52157 | -44.11876 | 2025-10-08 04:36:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72c4f1cc-f0d4-386b-bc7a-117f8a314117 | -3.49175 | -48.93483 | 2025-10-08 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1faa38e-2c88-3ec3-b715-723e3283229d | -3.09052 | -50.58224 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README60.md)
