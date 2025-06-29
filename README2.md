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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 984af0f8-c318-3a77-8373-80c2580ad1cb | -11.2474 | -52.7545 | 2025-06-29 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 25909502-20ec-3918-be2a-68d0c58d77f6 | -11.0356 | -56.2644 | 2025-06-29 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 171.5 |
| d22e4b40-9813-3159-956c-8b3d3e5c25b2 | -10.5579 | -52.0289 | 2025-06-29 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 191.7 |
| 777c7794-1fe6-38de-aafb-0d50425504e1 | -11.0166 | -56.2859 | 2025-06-29 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 254.4 |
| f814f325-4482-3d3f-a78e-8a6e1e69271c | -11.2666 | -52.7318 | 2025-06-29 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5129e526-f8f2-3269-b95d-d652f1e07a28 | -10.5765 | -52.048 | 2025-06-29 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c6a531b0-ad9c-3e96-bec6-b859620ddc9a | -10.9811 | -45.1104 | 2025-06-29 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 258.0 |
| b5ea17d2-af13-39e1-911e-b2b54d8d1803 | -10.5576 | -52.0499 | 2025-06-29 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 218.6 |
| 91e716d8-6d95-34a5-85b1-4fa7a410302d | -10.962 | -45.113 | 2025-06-29 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| cd7f9c65-6d5f-3d29-ba40-b63fcc40d625 | -22.4056 | -46.8205 | 2025-06-29 00:30:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fcbcb362-f920-3ac9-bf42-39ab8fec6e44 | -10.5576 | -52.0499 | 2025-06-29 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 190.7 |
| 1cc9bca8-a9f3-300b-84b0-875a0a18fc67 | -6.634 | -47.274 | 2025-06-29 00:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 61b7451f-09f6-3761-9e74-bf8b53269d91 | -10.5765 | -52.048 | 2025-06-29 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 15f6da3f-4c39-37cc-b82a-cad2c2d07108 | -10.9808 | -45.1335 | 2025-06-29 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 005004c0-55f7-3f92-819d-c0bc4bc9bfad | -6.6153 | -47.2754 | 2025-06-29 00:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9643827e-8a86-38fa-a624-774cb2d7a865 | -10.9811 | -45.1104 | 2025-06-29 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 350.0 |
| 00ad85a3-e603-3502-bcda-cf51dace6af5 | -17.4038 | -42.6435 | 2025-06-29 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 181f1d91-8fb0-3c05-94a3-e3f0abb6f900 | -11.2666 | -52.7318 | 2025-06-29 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 750c796c-6a5f-3b1c-a361-ac1df590e36c | -11.2664 | -52.7527 | 2025-06-29 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| fc45b061-7fa6-3578-82c9-9704d3929cde | -10.5579 | -52.0289 | 2025-06-29 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 156.5 |
| f5397be0-071f-312e-94e3-38db15d627ae | -17.4045 | -42.6186 | 2025-06-29 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 09e96cb1-0623-3344-8583-029b4bf02b49 | -10.5387 | -52.0517 | 2025-06-29 00:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ca24355b-c2e2-3de9-babc-4f7d0ec3dd61 | -10.9815 | -45.0874 | 2025-06-29 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 7009ab64-b72c-39b2-81fa-3cf03416a309 | -11.0003 | -45.1078 | 2025-06-29 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| fc433994-5904-38c7-af0a-edef4a02efdc | -10.5767 | -52.0271 | 2025-06-29 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2e279096-39e2-36c9-9a1b-cb5a6d191de4 | -10.539 | -52.0307 | 2025-06-29 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9b63a7c9-fc14-3609-9be3-18bda319bf38 | -10.962 | -45.113 | 2025-06-29 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| be7e70b5-4788-38e3-bf96-3fa1f1421939 | -17.7628 | -52.436901 | 2025-06-29 00:38:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2966260-ff56-3450-8ec3-950f524acbb4 | -17.7644 | -52.444099 | 2025-06-29 00:38:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b8aee26-88d6-3734-84da-e6486e4974dc | -17.4045 | -42.6186 | 2025-06-29 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 126.6 |
| da3dab81-2cd9-34f1-86e8-f9a34825a341 | -10.5387 | -52.0517 | 2025-06-29 00:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0cb1dfdc-809f-302f-a005-6bfdbd70b1c5 | -11.0003 | -45.1078 | 2025-06-29 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b57e4f42-637f-3881-a986-3902ace93ffa | -10.9811 | -45.1104 | 2025-06-29 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 319.9 |
| af8452fa-4426-3455-aeb4-76211cce67d2 | -6.634 | -47.274 | 2025-06-29 00:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 608a9c56-f4d0-302d-aca4-92197c9f3aa5 | -11.2664 | -52.7527 | 2025-06-29 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| e8d5602a-3943-36a5-83f5-dc1184390899 | -10.539 | -52.0307 | 2025-06-29 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| bf52e70f-0dce-36c9-b597-339cf6bd459f | -10.5767 | -52.0271 | 2025-06-29 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5c8c35c9-9efa-3c3b-bd76-39af2afee85f | -11.0356 | -56.2644 | 2025-06-29 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 2438b5b1-5ce9-3547-8e61-30a635510704 | -11.2666 | -52.7318 | 2025-06-29 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 04502584-2429-3dfe-b568-29eabe238a54 | -11.0168 | -56.2659 | 2025-06-29 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 07153268-4706-363e-aae5-9b66e2b3b19f | -10.5576 | -52.0499 | 2025-06-29 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 184.9 |
| 3653596c-a0c8-39ec-b150-809faa74ebbc | -10.9815 | -45.0874 | 2025-06-29 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 432b904e-c371-3707-8c44-b177d8f4f0e1 | -11.0166 | -56.2859 | 2025-06-29 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 268ba2f8-6deb-3c95-8695-661a57cd74f5 | -6.6151 | -47.2974 | 2025-06-29 00:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d52f17eb-4d58-3745-ba36-5879f99b99fb | -6.6153 | -47.2754 | 2025-06-29 00:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f2ff59c2-dc4a-3b5c-b0b1-b434380c4b59 | -10.5579 | -52.0289 | 2025-06-29 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 1570c56e-8a6b-30ad-9bb0-b304fca40913 | -10.962 | -45.113 | 2025-06-29 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 828037b9-9761-3e2d-a212-d7acf86d5eb3 | -11.0354 | -56.2844 | 2025-06-29 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 275.7 |
| 3c0bdf9c-7859-3cb8-8870-f887f53bfc53 | -10.5765 | -52.048 | 2025-06-29 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 174fe354-511f-3e51-a290-9e24aca64bd5 | -13.9591 | -54.478001 | 2025-06-29 00:41:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6b4b73-1254-31bc-aa13-dddb26c1386b | -11.2593 | -52.754101 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e84759-9572-3e5e-bbd3-5f2171ea124f | -11.5075 | -52.757 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b125684-5fc2-3610-a877-8f2b99d134f1 | -11.5417 | -52.771702 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a38e876-6142-3da9-82df-d40136cc10dc | -11.5711 | -52.7649 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8baa6fd8-45d6-349b-a772-a563e809e670 | -10.836 | -53.756599 | 2025-06-29 00:41:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de36a5ac-209f-38ce-96f2-7b85a8351c54 | -12.4197 | -54.868801 | 2025-06-29 00:41:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8b7532-bd92-3c62-9711-5367dc5cde82 | -10.5275 | -53.621799 | 2025-06-29 00:41:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0618865-0920-3dce-ab2e-c7601ea04062 | -10.8556 | -53.752201 | 2025-06-29 00:41:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea53e9a7-e64f-316b-ace9-80ecfff9300a | -10.2997 | -57.131802 | 2025-06-29 00:41:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77eea5b4-b74c-3928-b88c-d89d21f90775 | -11.5352 | -52.743 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4c0c5e2-a6e2-3a7a-8f08-c65846059c6e | -8.3675 | -51.0844 | 2025-06-29 00:41:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba32a967-2aae-31ec-819e-184cf7b7560a | -13.9509 | -54.4874 | 2025-06-29 00:41:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 139d33fe-5747-3ff9-8d9f-92f3e3a6f734 | -11.5401 | -52.809799 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e957c4fc-ef85-3005-8b43-774e81f5b68b | -12.6246 | -54.206799 | 2025-06-29 00:41:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 169138c1-2b4e-3023-aeff-f309d6eb83b1 | -11.031 | -56.284199 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 311d5997-62dd-3914-bfcb-de18b5b617d0 | -15.7323 | -49.552502 | 2025-06-29 00:41:00 | METOP-B | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b419ad2f-0df8-39c2-ab55-aee6e03a01b2 | -10.1004 | -52.1954 | 2025-06-29 00:41:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 309040fd-b202-33f7-81e7-edc0e5443cf7 | -11.0081 | -56.225601 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eff2d01c-055d-302e-9965-eef12f9fe87c | -11.514 | -52.785599 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f521143-49e5-303d-83f1-fa3bd261cebd | -11.5515 | -52.814602 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 554f1cb9-3e19-30b7-999a-3d412a4f70fa | -11.0485 | -55.369499 | 2025-06-29 00:41:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d060ef08-e00c-3332-9bd1-220ae62ad718 | -10.922 | -44.1493 | 2025-06-29 00:41:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34d8cbf2-7fb5-3e74-aed9-a2c7686ff2b5 | -11.5205 | -52.7691 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c951af0c-3ccc-3bed-8763-516cf7c62ddc | -11.2642 | -52.730301 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f54747f-d121-3c08-afce-c423f4190bf9 | -11.5744 | -52.779202 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40925dba-c48d-369c-9fc9-6b7ef8a20585 | -17.381599 | -42.603199 | 2025-06-29 00:41:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 59114e63-fc58-3540-827a-075c6b96a0ba | -12.0596 | -48.465801 | 2025-06-29 00:41:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2ba33f4-6cf5-37ba-93ac-33983d276bfd | -17.391199 | -42.600399 | 2025-06-29 00:41:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0da2ce14-c0da-3c3a-bf1c-48efc251777f | -21.131901 | -48.584 | 2025-06-29 00:41:00 | METOP-B | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d850f0d-a26a-3930-908f-4d03e683c7aa | -10.5564 | -52.024899 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c59b0564-59c2-3692-b68b-489ca201d592 | -10.9843 | -45.1096 | 2025-06-29 00:41:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47200c19-7372-33e4-a29c-06b501bcd33f | -11.5581 | -52.7528 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 906a81e5-687c-30a9-927b-64f324fc9973 | -2.7483 | -54.586498 | 2025-06-29 00:41:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5050d646-b315-39fa-897d-97256e080b5c | -10.3095 | -57.1297 | 2025-06-29 00:41:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6e1986-9494-3b8e-bd4a-c5995d3c2caf | -10.0406 | -59.347401 | 2025-06-29 00:41:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71d427cd-03a9-34b3-a766-1795fa412e71 | -6.6204 | -47.297798 | 2025-06-29 00:41:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5293bf7-f72b-32c0-a393-79736ee18334 | -13.9607 | -54.485199 | 2025-06-29 00:41:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6eab2bbb-4f28-3e05-be74-48f226c90377 | -10.0986 | -52.187901 | 2025-06-29 00:41:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7ba66f7-8256-390b-a8b0-166aa5c6571b | -10.5466 | -52.027199 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb99da2-3d89-3043-9333-f380cc55a457 | -10.9699 | -45.1339 | 2025-06-29 00:41:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d254963a-baf0-365c-b635-2b7733d080e2 | -10.5697 | -52.0378 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66eb5110-c2b1-398a-9147-c3383a626be3 | -11.0375 | -56.2668 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d159441e-06e9-347e-9759-e08e1477244f | -11.5695 | -52.757702 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9f728e5-bd43-3633-b587-75d5072a55a6 | -11.0195 | -56.231098 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 244d1eca-76e6-3361-82e8-647c58c59dc9 | -11.5597 | -52.759998 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8823efc6-eb22-39b9-82f7-5712856a58bb | -11.0408 | -56.282001 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac0bf01-a834-31f0-adc6-7fe217ccbb1a | -11.5776 | -52.793499 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67846fef-715f-3369-93f2-8b934d4b9ec2 | -11.5679 | -52.7505 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11cbf911-e881-3e58-a7ad-660bb9bf8cbf | -11.0392 | -56.274399 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f144b9eb-db18-3eb6-a888-f76eaa7f24fe | -12.1183 | -54.571999 | 2025-06-29 00:41:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
