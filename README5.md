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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27668425-67d5-3d53-b620-7b531650dd3f | -11.2941 | -54.033699 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 398c2809-6c28-3f60-96c6-db2640097a9e | -6.6698 | -52.8284 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06af47f9-f9e9-3ed5-a8be-989774fff89f | -11.164 | -51.306 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 649492aa-0cb5-360c-8146-5e76a39aeeab | -10.7601 | -50.686298 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7da9ccf8-9885-3bf7-b62c-51d8ca6b6f17 | -19.0914 | -46.2169 | 2026-08-30 00:32:00 | METOP-B | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22742577-d9e9-3d08-89f7-f24de2feb03b | -11.0361 | -57.218399 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a33392f0-e4f6-3d33-ac25-12b83b24c82c | -16.352699 | -50.9786 | 2026-08-30 00:32:00 | METOP-B | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25e5a957-325b-39db-b9e7-646e5bf603a0 | -8.2526 | -62.727699 | 2026-08-30 00:32:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 505895a2-9a08-3e33-851b-206d688a3d37 | -6.7828 | -55.6339 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a818366-4f25-363c-ae1b-5a050b463a33 | -11.0344 | -57.210201 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 530085c5-9574-3140-b5ec-f98200d2e4b0 | -9.6111 | -55.116798 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 859806c9-7a38-3c07-b400-4d49a4e5d534 | -5.8793 | -52.084999 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a90c7887-fba1-3fe3-97e1-d2c8a0d8b389 | -14.755 | -48.7323 | 2026-08-30 00:32:00 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea72b642-3869-3266-b0ae-17aec248ba47 | -9.7583 | -48.1558 | 2026-08-30 00:32:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 203df9c7-3bee-31ce-b147-ca1b3b46194f | -3.7565 | -59.312599 | 2026-08-30 00:32:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a9a198f-f8a1-32f4-b8fa-99a1613b5100 | -7.2352 | -60.602001 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4d11c1-ed1b-32ff-993c-d08c6bf18809 | -2.914 | -54.110699 | 2026-08-30 00:32:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83138e7d-ae13-36ff-9a79-4a29c46af983 | -5.889 | -57.7626 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af9e252b-6853-380e-86e8-f2886533ced9 | -9.181 | -59.614201 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6bec9be-1e02-3a09-9f14-0775c33f93f8 | -14.4245 | -52.562401 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e17d342-0304-3801-81d3-141c8beb4e13 | -21.527 | -48.615799 | 2026-08-30 00:32:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4abb8b18-2111-3dbf-93cc-5ece539cdc42 | -23.2045 | -46.9725 | 2026-08-30 00:32:00 | METOP-B | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c01f2fd7-2d02-3158-9250-75e3337d56a6 | -11.0441 | -57.208099 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a40acba-d51a-3819-a569-2b764cbe70a5 | -11.0379 | -57.226601 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a08e5587-f22f-3f88-a494-c1efe6b3d1e2 | -9.2197 | -59.748798 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8561f7a-e45b-3a95-bf97-bf48e39af376 | -23.1511 | -48.655602 | 2026-08-30 00:32:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b55061be-90ae-3701-a344-5976538101f1 | -8.5962 | -54.814301 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a15c713-1b93-3bc1-ae39-9f8d6096a013 | -10.7559 | -50.668701 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebacb3d2-a014-3795-8f9b-3609b2ac1668 | -6.6716 | -52.836201 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d588d74-85ba-3da7-aa5b-c285a9b18d07 | -4.9632 | -55.830601 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3996188e-8276-347a-a258-b9af273bb513 | -10.4777 | -64.4487 | 2026-08-30 00:32:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d842824-45e4-3575-b47a-d35b30319298 | -10.7441 | -50.662102 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9cbc1f31-ec78-3346-96ca-c4818ad70616 | -9.0427 | -65.331802 | 2026-08-30 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de1cf632-56cb-3ffa-8e92-6c54fe87d936 | -9.8441 | -60.245499 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5981c1-94fd-3cf9-81f2-a34974143325 | -13.8647 | -54.115002 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a162545-68ab-371e-b3a5-2ccf1cebfe82 | -8.6014 | -54.791401 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e07f65c1-ac5c-39c4-9ab9-d3f4ec5eaf8e | -11.1902 | -55.0928 | 2026-08-30 00:32:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f98c700f-00f1-3a2a-8a07-45e620016bb9 | -6.789 | -55.661499 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd91f9f-6587-3c95-9f77-12adf26d9f0b | -6.6156 | -55.440102 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5324309-bbb9-38cd-8542-fe1e5f75814b | -7.2376 | -60.6133 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 627a9209-3896-3453-8154-c01e0cc55ea8 | -11.7223 | -54.522499 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f571b1ae-3ff7-3ebd-a388-e0b9c679a401 | -7.3329 | -55.1493 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a956d52b-3d8b-333c-9b50-4a3c499c1c2c | 2.1946 | -50.705898 | 2026-08-30 00:32:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 78099ea0-dc77-364b-a750-8d73536e9df4 | -4.9251 | -55.752899 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5fba2c0-3a17-378a-9d67-81467a6b0edb | -7.5557 | -61.2938 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 668c88f5-e244-34aa-abb3-3e17f84b1d64 | -7.3011 | -60.576302 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1444bda4-7aea-313c-b687-b5219554ff50 | -6.2591 | -55.411701 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fe5cecc-efeb-3bb8-abee-844a7ccef7ce | -9.8905 | -60.2724 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fca2b323-3769-3f03-8fe8-9fef7441a8b4 | -11.8268 | -51.050999 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f933d589-53a6-3b92-b8a6-375693e99608 | -5.9719 | -57.672798 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a659b5-c1c7-3a82-9c51-a89c60220a17 | -6.8632 | -59.445 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 789090d1-94dd-3ef0-940e-9f1beb8cdce2 | -7.5022 | -55.306599 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ce2086-cc8d-3f2a-9c7e-796ec2d2a9af | -9.0574 | -65.355202 | 2026-08-30 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58457e95-cfc0-321a-bf31-bc075e42a015 | -9.1548 | -59.490299 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 768ed40c-d35d-3917-96e3-7ec2e66caf76 | -7.1294 | -56.5406 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 386a34dd-c97c-3157-81a1-165dee78e469 | -3.7701 | -59.327499 | 2026-08-30 00:32:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb03fbcf-58f0-3780-a42c-f2407a367a0d | -16.3412 | -50.9734 | 2026-08-30 00:32:00 | METOP-B | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f4fe87f-58d7-3cb7-a3e0-01b985b22837 | -14.1584 | -52.798599 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d71281b-a9d8-3ed2-93e0-c5637518a08f | -9.1766 | -59.593399 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51800888-a8bd-367f-b92a-9b3f1587fb33 | -6.773 | -55.636101 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e78048d-2f1d-3c47-88cf-64f92dda9a14 | -7.5655 | -61.291698 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd77b9d3-409b-3f93-8719-39cfd9b9188e | -10.7269 | -50.851501 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c61e2be2-8850-3a2c-8374-b9545928a61b | -6.9531 | -55.704601 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65b72b61-1d6a-3de8-ad61-88787289392d | -5.9604 | -57.667301 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f6a2c45-38c2-3ec4-9b4b-eaf4ff4b11b6 | -13.8663 | -54.122101 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3dd2684-f3fa-37f3-ae7a-10ca54563359 | -10.7954 | -45.304199 | 2026-08-30 00:32:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae1bf1ef-b564-3371-875b-d27605dd0a00 | -6.4258 | -55.511398 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b31e1a5d-acd6-338e-9a63-f3c2be486d6d | -11.8249 | -51.042702 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e102d036-3b4a-3dfc-9c78-7d122fc63b09 | -8.6148 | -54.7593 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4c7f813-8c50-303f-b340-b61a5da8dd24 | -10.7484 | -54.0341 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed11bdf-0ef0-3803-b2fa-068878a1b29f | -6.7534 | -55.640499 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 328041c2-501c-3435-bc09-c37fb688bdda | -18.8162 | -47.434399 | 2026-08-30 00:32:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a43568f9-cf6a-389a-9390-97dff116ee57 | -8.9597 | -62.366798 | 2026-08-30 00:32:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cbf050d1-d823-3b9f-a19f-a9706fb1cd37 | -7.2974 | -49.529701 | 2026-08-30 00:32:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beb85b0f-afba-3c04-b637-4c3aa63de03f | -8.2493 | -62.711498 | 2026-08-30 00:32:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3455d55a-af42-3e8c-b50a-67ffb092ccad | -9.6699 | -55.1035 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7565d90b-62d8-364f-8d4b-4c6a61ce9d9c | -14.7526 | -48.722198 | 2026-08-30 00:32:00 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f91c96b0-0eeb-3e3e-be66-1820f02f4c94 | -7.5037 | -55.313499 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccf2063e-e1ee-3856-8ed2-2f522dd05d70 | -9.1668 | -59.498501 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23569620-4515-39a7-88f0-7068692075f0 | -3.64 | -60.5453 | 2026-08-30 00:32:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e425e47-9f7d-3f1a-aca0-6f5f8106f071 | -5.489 | -43.995899 | 2026-08-30 00:32:00 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4c4144e-ef37-3cf6-be01-f98ef3cb47ac | -18.6544 | -46.8274 | 2026-08-30 00:32:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9e547a3e-430b-364b-86af-06059e5b746b | -6.6997 | -60.108601 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbf77684-cfb4-3506-840e-ae0676db858d | -6.5382 | -55.0966 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6119b5b6-9961-3158-89d6-d011440c3386 | -11.6321 | -54.5798 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb5190f1-3b66-3023-8cb0-9a4a8d5abbda | -15.6518 | -56.381001 | 2026-08-30 00:32:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed8da11-99ef-30f7-9c63-69c87754cdbc | -6.7844 | -55.6408 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7981805-291c-372e-8855-2cc4362ebfc3 | -4.9534 | -55.832802 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73e8f67a-1cac-3e8f-b820-7557c3e1ea15 | -9.8466 | -60.257099 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a37aeecc-f1d5-36a1-b3dd-12e980f6a6b9 | -11.76 | -54.506699 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66c06132-bd4d-3823-ad33-5854bcd09d58 | -1.3737 | -49.291801 | 2026-08-30 00:32:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8c846b-1d4e-38b6-b2d3-2f126b055cb5 | -9.0477 | -65.357101 | 2026-08-30 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 466ed8cc-fac9-3ec3-a8c1-76d97717e6d4 | -9.1679 | -58.303299 | 2026-08-30 00:32:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f79e423-6890-38c6-bcf7-79534f8dae7b | -3.2376 | -61.2281 | 2026-08-30 00:32:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2d61e9-b99b-3942-9c9b-2b0ba7cf09ab | -10.75 | -54.0411 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 210227de-8450-355c-a60e-a2743cead499 | -9.6802 | -55.0574 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2426415-4c52-36f9-810d-3dde44708a00 | -6.8416 | -59.439701 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c86a7976-5f93-36b0-989b-819d3c970222 | -9.2432 | -60.395302 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7847a6a-b6f9-3553-ba6b-cfc4897e2237 | -7.2938 | -60.5896 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86fc34f1-0ffc-3d7c-add2-825e1f9bf4ab | -11.2926 | -54.026699 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
