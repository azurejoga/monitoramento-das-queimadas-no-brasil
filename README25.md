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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88e2aa54-a78a-3de6-954d-6f02e7f0ef26 | -10.36655 | -47.16704 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd9ca0e1-47ed-3717-afc1-cbf87b96bc65 | -8.70647 | -44.41801 | 2025-10-28 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e948575c-41f6-3ded-93cc-08f910cddb40 | -7.80197 | -43.83156 | 2025-10-28 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f26a9b64-f230-321a-9ef2-506dd27d8a74 | -8.63949 | -44.77479 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97e7f2d0-f2d5-32dc-9e07-41d11bb7b26d | -8.25148 | -46.89431 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bb4047be-047b-3d49-9e2c-9eea431a7cc3 | -7.36933 | -42.44223 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 437751b1-636f-3d9b-8d74-caa89184ba01 | -6.12726 | -42.44646 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c57975a-4ce5-3aaa-96bb-b9477208b19f | -7.97236 | -46.7422 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 878e2bb0-5380-320e-b2ed-347616c3b268 | -6.7027 | -42.04802 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7233c772-da1f-35af-ba40-8b58a3139522 | -8.03257 | -45.14229 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47314a18-cdcd-3665-a166-321ca3f37422 | -10.54908 | -45.05233 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00f73934-0078-3a78-a212-df850aec355c | -6.11286 | -43.70781 | 2025-10-28 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a20ad922-89b2-3d13-a76a-d6084b66b16a | -10.95365 | -48.05871 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fe24b76-5564-3f62-a63d-daaa2e852fa7 | -9.19233 | -44.57308 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74d32a9f-0df4-3df6-992d-768ed6bf44e7 | -12.63105 | -45.08094 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4067cd8c-8438-38e5-984a-75366df3122b | -9.56764 | -46.97606 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 016f963f-f5b5-3d47-bfc5-795d95f5319d | -12.08501 | -45.66345 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c635c83-ae96-37d7-b465-bc9cf3eeea8a | -5.6297 | -46.30606 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d056029b-e29e-3d25-9495-9b36d1ff567e | -5.61803 | -45.98289 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ce95c66-97e9-3394-81f9-a78d92895242 | -10.30036 | -47.22231 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14b21aa2-e2bb-3ed6-a2ee-7d72cb72a2c8 | -9.98052 | -47.15879 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1e6f4fc-e4ef-338a-9190-c4b85e4bb00d | -8.56164 | -47.73576 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b22caa8a-8af4-3865-b5d2-4d5cbf702f0b | -7.47538 | -47.161 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f23e8772-ac7e-3449-a78a-57cd3dc6a0be | -4.85435 | -50.68353 | 2025-10-28 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99396d48-05ac-3529-8908-1a14878b6e8f | -9.56111 | -46.97066 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f908301a-0591-3bcc-871e-f7d648add89f | -9.46667 | -46.88296 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36c1f1fc-27a7-3fd9-a2cd-0e333a085b35 | -6.46702 | -43.1894 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6aa9040-24d7-3bca-ab28-141c7f6af076 | -7.8428 | -46.40689 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 91212f25-3fd3-37f1-a49f-eef478ed20ed | -6.73911 | -48.17115 | 2025-10-28 04:14:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c421655-809a-3811-8a25-0e13184fad7f | -10.52268 | -47.73337 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdb0214f-db07-3809-85cf-fb5f673a154e | -10.92639 | -50.27227 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5cdfd24-5237-3846-bedc-79992e6366bb | -11.91265 | -43.8284 | 2025-10-28 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19bd8d47-bfa2-3293-83a4-3eb6f19fbc9d | -8.56727 | -47.02789 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e477e53-362f-388c-a01f-e1cc001de48e | -7.07985 | -44.94881 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f283bf87-c04b-3f94-817e-48204ac271ac | -6.44944 | -43.81859 | 2025-10-28 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aac7daa0-a6b6-3bb8-a726-d11e69a9623a | -9.47469 | -46.90158 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fdfcc57a-6b91-3e93-8b54-2cdb8389bd9f | -8.16086 | -47.01115 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9154073b-875f-36da-8c9c-1d37c8b89491 | -8.6327 | -44.79579 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c624542-3ab4-3ad6-9134-b3a0b971d213 | -10.57778 | -44.53076 | 2025-10-28 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0141a800-7afe-3f63-af94-3968ad950413 | -9.58393 | -49.67368 | 2025-10-28 04:14:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51f11867-46b0-3cd0-abf5-f5725a8a002d | -5.43826 | -47.3954 | 2025-10-28 04:14:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 799b1b44-9d52-3ddc-bd4e-f1c72f3cd340 | -6.58653 | -44.62722 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75be4aae-09c5-35dc-a380-568f182547f2 | -7.82149 | -46.42476 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f222ed7e-516d-33c8-837b-cd08cdb2b00b | -9.97475 | -47.171 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f83a42b-537c-376d-b626-3d8d119be9e0 | -8.0464 | -41.11349 | 2025-10-28 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 50d11f60-6f35-3a87-998b-9f11ee2c46f6 | -7.81518 | -46.44077 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b6e511a-1274-3e28-8f5c-9d79f4ac8af7 | -10.32228 | -48.7867 | 2025-10-28 04:14:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 795f7488-a123-37e8-a1c9-8838f773f5fe | -6.44768 | -42.35487 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 87760662-eabb-33f1-9637-f6ded6b29fe5 | -9.88396 | -44.88887 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9f24af5-91f4-3be5-8c81-ac40755878b2 | -12.08065 | -45.6478 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d00e0f52-feeb-3f23-bb84-72831fdacf90 | -7.00486 | -46.99393 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23223891-ef0d-3f81-bcc7-6856884a9e44 | -11.33204 | -43.18309 | 2025-10-28 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 669cd3cf-1458-3873-aff2-2e20e4d69912 | -5.63589 | -47.61284 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ad88f30-5d2a-3dac-bcd8-e16d89d667b7 | -8.1542 | -47.00562 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c2e296-9e47-3d48-bacc-608c01bfcda4 | -5.67244 | -47.82475 | 2025-10-28 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cc9154f-245c-3c65-836b-ba80cfaf6f87 | -5.23922 | -49.49864 | 2025-10-28 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5668f891-e4d5-33d6-9b62-093e8cfd0447 | -6.488 | -42.22573 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6a5a7a3b-f0c3-36ab-a29c-25c1bfa32442 | -7.85553 | -46.39643 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe3ab15f-0757-3853-9218-0aaa9fd94cc3 | -9.078 | -45.15717 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ab33c07-4d44-3075-80a8-814e2ca6cdd2 | -10.91774 | -50.27074 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b1e8613-291f-3bd9-8a28-3c44d5a49af6 | -12.48182 | -44.21559 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2d6ef53-c742-38fd-85b9-611f5b965ad3 | -8.19583 | -46.93604 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e28c9cb6-5123-3703-8a2c-3d45baa08f97 | -7.82575 | -46.4212 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d62c5d01-15a1-32b7-906f-44082c6517f6 | -11.3707 | -45.27819 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daac5dbd-d8db-3ecd-994a-85657648c5ae | -8.71668 | -50.00456 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fa1b135-c638-326b-8bb5-ca0bf7fac0cf | -8.15122 | -47.00072 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92f2095e-578f-3041-b679-c33363ec3991 | -7.07364 | -44.94409 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27ec59b9-7ab3-331d-995c-7637d836a377 | -10.93298 | -50.26044 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 822e1cf6-b83f-31cc-ba5a-103e81f35344 | -9.61169 | -47.80592 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0299ae6-d0b5-3498-9cfd-d8c120cf43d6 | -7.95981 | -45.46344 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2b357f3-020f-3b3c-a37b-d17cb6202526 | -11.85182 | -47.92043 | 2025-10-28 04:14:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 574c5bad-015e-3464-831d-60e3d846052b | -7.32331 | -47.21235 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68c5ad35-ee72-33ed-a4d8-9cfff9a29bc9 | -12.61937 | -44.24902 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d57f2612-9737-30d7-82c8-6b64518fc461 | -12.32104 | -47.4542 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ef7e6df-6b85-3093-9196-ef5b8a799828 | -10.02405 | -47.16625 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d58a1f87-f1d8-38e7-9abc-2c2a2d21782e | -9.22185 | -48.60253 | 2025-10-28 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6e680fb5-abe5-3f8f-9ca7-2d096af96509 | -10.40756 | -45.29824 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04aa4a56-9a61-38f0-bd8b-040105edbced | -6.11904 | -42.45581 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a836b48-084f-32ac-8285-090cef8241ed | -8.32525 | -46.16194 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a47229f-799f-36db-905a-c2dc363b2a35 | -8.49753 | -48.28391 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a2401de0-112e-3bc6-a95e-5ad655c73277 | -7.94955 | -45.50492 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7ac7b5d1-ae90-322b-834d-d056e94a4b00 | -7.19571 | -46.73883 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f6af62f-80ba-388f-91a5-d8da653a7508 | -6.57746 | -41.40774 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2260ef3d-0500-3a9c-aa0c-f02ce5ad0560 | -6.48469 | -42.22522 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d8681577-6666-3c9d-9605-fd3f723c1c6e | -6.66244 | -41.51682 | 2025-10-28 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c8815a5-1a7a-33d6-9fc4-84e0bbb8eb21 | -9.22326 | -46.3569 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8dae0c77-5f26-3dcd-a1ef-92cbb88d72d4 | -9.95215 | -47.10563 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a1973cc-8ee8-397d-b313-ae557854900c | -10.778 | -43.86484 | 2025-10-28 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8e260a5-9c22-3e93-8b1d-3bd6090d55fe | -5.91926 | -45.39494 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ef062d1-f358-341f-a73d-374fde844fad | -9.22261 | -46.36085 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d68f3a0a-2d34-3ced-af3b-0adf5cb249ab | -7.43482 | -41.86264 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66c36c45-4459-33a4-8249-0ababa139339 | -6.43869 | -42.03914 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ec62783f-3aa7-3bd0-928d-42bb0596f3c5 | -8.65873 | -43.9231 | 2025-10-28 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a5dc675-a151-3c81-ad17-662ac129bfd5 | -7.61334 | -46.47932 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee422e2e-0f6b-36aa-81d8-1f580d550f88 | -7.9592 | -45.46719 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01cb0249-7882-3e28-b645-9c3e10e8729d | -6.42744 | -42.3303 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cdbb1a70-26a7-3a94-81cd-7d70d80ca574 | -6.48415 | -42.2287 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2e903e28-6a26-36bd-a4b8-d255c094b568 | -6.23434 | -42.56641 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1c8bbb2c-6ae7-3f4a-a4b7-bc105aa34591 | -6.97813 | -39.11766 | 2025-10-28 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 973324e1-80ed-3e3e-9a1b-ea8b663b9d6b | -6.43483 | -42.04208 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)
