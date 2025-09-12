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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a0e8c76-b060-325f-bcb2-4cafdec2ed9d | -9.07719 | -50.49026 | 2025-09-12 00:11:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 6844aedb-9a74-3eee-89c8-7974b972d712 | -11.41919 | -43.70448 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e87a6996-31d1-3b78-824b-942e8c97cf54 | -9.11248 | -47.11898 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 3e38a9ff-e609-37c0-b5f3-6dc7ef837907 | -8.89366 | -49.93852 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 441.8 |
| 78e57d85-39a9-3ab2-b680-5bbc15ce270f | -8.96039 | -46.0915 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| d4bef2b8-e5e0-3595-978b-d24f773cbe88 | -6.19057 | -42.74683 | 2025-09-12 00:11:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e17503fa-d3c8-3212-81b8-5616cef404cb | -9.01549 | -45.74251 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a3124575-531f-3df5-8ef2-e0c112a42b50 | -7.56229 | -44.39547 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3b58dbfa-ef4c-32e3-a8ed-e2f9ad742940 | -8.95895 | -46.08063 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 07900a5f-d54b-3406-9cb4-5f59a9ff7d8b | -5.40399 | -45.93618 | 2025-09-12 00:11:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 29f01e84-2f84-30c1-a662-48787981db14 | -7.41021 | -44.36407 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4c0d3f32-124b-3fe3-8964-94f44305578d | -6.44788 | -41.76257 | 2025-09-12 00:11:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 51922772-fda5-3671-ba2a-76c6cc48698d | -12.2495 | -46.75343 | 2025-09-12 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 32e5f720-99eb-30ac-a487-8cf6a836744e | -6.38999 | -43.51716 | 2025-09-12 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 96bb466e-8fdd-370e-a8ab-77dc52878134 | -9.00646 | -46.12528 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 03551fae-87f0-30e9-b8c3-71a3207ee1fe | -11.46949 | -43.60273 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a90c62d9-11ea-37cb-aa01-0adebad75550 | -6.30197 | -42.22568 | 2025-09-12 00:11:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 126.7 |
| efaea05a-7355-3729-8028-d2a271b3189e | -7.42235 | -50.66107 | 2025-09-12 00:11:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 8778cef1-6ff4-332f-bce3-df18aa9c68b3 | -6.553 | -43.96476 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e57a6229-b7f4-34fc-8540-28e71078d02c | -6.411 | -42.60473 | 2025-09-12 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f0ff918d-31af-3778-9bc2-f5ee61f9c4ed | -7.33131 | -49.63334 | 2025-09-12 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| da7f50e0-7c34-3b31-8474-7bca84cea659 | -11.69872 | -46.53477 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 2a5cfcde-e18b-3ef5-bd88-00c6a5f40f0a | -10.35632 | -50.53215 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e3cd4084-d4d5-38c7-8abd-ec7518917581 | -12.10861 | -44.86996 | 2025-09-12 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 23fc7510-2097-33e6-8361-a5b295a7ebcd | -5.66202 | -45.94379 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7bb4cb34-718c-36e0-aab1-d60b0e491aee | -6.25785 | -43.48839 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dab632fe-8e4d-3ca7-a95c-d57b62a7ab2f | -10.38195 | -50.50314 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| b8ed0343-c816-3cc2-878c-2215d4ca8776 | -9.49326 | -48.66961 | 2025-09-12 00:11:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 11ea4b82-8c2a-3cf5-a432-68ea104fb077 | -9.07448 | -47.11609 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 77c26a28-aa5e-3e24-aaee-7e5870e997fd | -11.09571 | -48.41357 | 2025-09-12 00:11:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9981aa6f-995c-332e-81b7-40cd1418ae48 | -8.08327 | -42.5651 | 2025-09-12 00:11:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 4f4884fd-387c-30c4-b427-2703bf68bc26 | -10.57878 | -47.22698 | 2025-09-12 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c3cf6549-29d7-3a5e-846f-941f893b6548 | -11.74396 | -43.3799 | 2025-09-12 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b14d5f79-0afc-3691-9f5b-789449ca968b | -6.46693 | -44.94618 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 25881418-66a1-33bc-8ed4-ad7986b12b69 | -10.33848 | -48.81575 | 2025-09-12 00:11:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 9511e770-4dee-3c17-aeea-0cb504a45685 | -5.12155 | -45.34793 | 2025-09-12 00:11:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a968c0a2-f0c3-39c1-b09c-ce282b48e46c | -11.14658 | -45.31865 | 2025-09-12 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 21c9fd49-3630-38a4-9f5e-004b4da26a15 | -11.98321 | -51.12265 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 7b35ac63-fd0c-3865-b4cf-60e60974cbe3 | -7.44824 | -44.4423 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 77a70004-fbf3-3886-abc9-d299cd65a9e8 | -6.30334 | -43.42804 | 2025-09-12 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1fc1f059-f41a-379c-8c6d-58d633af2592 | -8.59015 | -41.45397 | 2025-09-12 00:11:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| a9513e07-d1c8-32b2-9845-bc3daa8da5c7 | -11.24219 | -49.40699 | 2025-09-12 00:11:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 329cc9fb-91e1-3619-873c-cff03843e529 | -6.63241 | -49.78992 | 2025-09-12 00:11:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| cac53ef1-3698-3989-8091-442619bf6431 | -6.14995 | -43.37485 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 28d4ed86-3b3e-3f8c-9195-cdfe5a21dbb1 | -7.31883 | -44.1715 | 2025-09-12 00:11:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 53b29a91-53b6-394c-98e8-690d9b16c5ce | -11.68339 | -46.54313 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 44b778f7-493a-3063-8f90-056ec76efb03 | -11.68511 | -46.55653 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 941.9 |
| a14b944c-4806-3b3b-972a-f8c4dda4e8c9 | -8.17868 | -46.12016 | 2025-09-12 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| b45d20e1-138c-35f5-a0bd-db4772271453 | -6.14114 | -43.37609 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 340724b9-0a18-3fa9-ab26-4f8ce40f3ba3 | -8.48948 | -47.27 | 2025-09-12 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2cd7183b-fb82-35cd-8e4e-84ea366ee136 | -8.49117 | -47.28334 | 2025-09-12 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 730a5081-fc48-3622-aeea-7bf7fd6caf7a | -9.08209 | -46.96217 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 32941007-a857-34af-aadf-ee6d884d292c | -8.93778 | -46.07223 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4f47b083-cb87-3495-979d-1780732cb3eb | -5.72931 | -43.86008 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c801fe0e-badf-3bdb-805b-3946c90730d5 | -12.50593 | -47.43432 | 2025-09-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 05f7aa17-ffc6-3faf-95bc-90b4688963ae | -12.59096 | -45.67423 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e9d88948-a41e-3563-bdbd-549ec7fcfada | -12.5907 | -45.66794 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6e032988-9bc4-3c09-9580-51c606b6923a | -6.07481 | -43.56247 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2baefe80-6527-31a1-b4e2-0ee6344e6ae5 | -5.65264 | -45.94509 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| d59386c3-d0f4-3010-bcb7-95d28ef0b0d8 | -6.31615 | -43.43787 | 2025-09-12 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2997a8f3-99c7-3a5d-87ca-037c7a8f6e96 | -11.97265 | -46.65246 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| afe5e1cf-a662-3fb3-bb27-4bb62c207514 | -6.67963 | -44.14874 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 42da34f9-7a3e-34de-8e13-329e40efd82f | -6.10466 | -43.90834 | 2025-09-12 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19a9e79d-3bb2-3dad-9037-ba75c24a6ee0 | -6.27519 | -43.2251 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ae425a19-6d9f-3bce-9d3e-8d9af0cbc694 | -9.04463 | -47.05192 | 2025-09-12 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 269cb4ba-6274-392b-ab1a-7cf40db8bac2 | -6.47598 | -44.94503 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 2bc1f564-2d52-3cab-9608-7b16bf84d40b | -5.65099 | -43.89495 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54376aba-e350-3763-817d-9bef2b2865ff | -6.34266 | -43.04664 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a4e0f853-5903-3c44-9a96-9ad80f02c7b3 | -5.69678 | -49.19873 | 2025-09-12 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b7ff75d1-efd6-3402-aec7-ec62c42503c7 | -6.11841 | -42.95473 | 2025-09-12 00:11:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b840aecf-0f8a-3bf9-823d-47d30efc14ab | -6.82509 | -52.8223 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 2b049b9b-25cc-36cb-b0ca-525792143d4d | -6.17806 | -43.25384 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b5ada019-9dc2-3bd0-afa4-76e14e3276e3 | -6.81836 | -45.64373 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a5386f26-e401-3b49-aa31-3e464cbb77ef | -5.6522 | -43.90375 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d17c7d3-cad6-3b7d-9f7b-1e608c2c0b95 | -11.89341 | -41.27731 | 2025-09-12 00:11:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 2d91048a-d981-339d-a7a7-30853afc302f | -7.92959 | -44.86625 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e03c1e32-eea0-3292-88cf-3ef4fbd2baca | -8.87345 | -49.54253 | 2025-09-12 00:11:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 2e737fee-e4d7-3c2d-9e58-a8402d39a2b6 | -9.07215 | -50.49748 | 2025-09-12 00:11:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 2ba9f06d-d216-3d4a-a29e-2955388fc8f7 | -10.1288 | -47.91465 | 2025-09-12 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| faa192e3-149d-314b-8224-70fd1a7175a6 | -11.96797 | -51.15008 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7722f272-7dcc-3b58-b9ca-a9e5dc709f02 | -6.6009 | -44.31202 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5b4a89d2-9c7a-39cc-9a97-310b78a61b27 | -9.04639 | -47.06562 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4f6b095f-41f2-3a36-bbf5-3a89762e5a05 | -11.37393 | -43.50953 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6410c6aa-5cb5-3630-a10e-981c0b49ddfb | -6.26787 | -43.49594 | 2025-09-12 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f3a7c7b9-0843-3ac2-938e-a3bf29b91b40 | -12.02 | -43.79331 | 2025-09-12 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| eac66e01-6c44-33a0-82d2-0d51307d49f2 | -5.66905 | -44.30376 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eaab393f-38ec-3333-b373-67c69af36091 | -7.28828 | -44.48037 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1592e3a2-846a-39fd-9803-b15eb97f1d55 | -5.70254 | -49.2037 | 2025-09-12 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| b39a5481-a08a-3349-89eb-015824921da5 | -8.89621 | -49.96032 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 244369c9-c95c-3a72-9003-faace130053f | -8.21763 | -45.79145 | 2025-09-12 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0bb7fb4e-d62c-329e-83d2-0011e39e446e | -11.56819 | -43.24036 | 2025-09-12 00:11:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 494b58b4-96fb-3622-85fb-1855ea4d175f | -6.53067 | -44.60344 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e7f27b29-f050-3306-a676-f3fc481ea399 | -6.48668 | -43.87501 | 2025-09-12 00:11:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 8d69075b-b120-3a32-9833-e014b409f3e6 | -10.58039 | -47.22109 | 2025-09-12 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 6f60c3f8-f8dd-3cea-a0fd-c9843fa2545d | -7.31865 | -49.63501 | 2025-09-12 00:11:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 49df16e0-99db-308f-9e51-1b6c958ecf4b | -6.26445 | -43.40661 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c85c090c-5c4c-31e4-8e5e-3981b2b6fb44 | -7.33076 | -49.64002 | 2025-09-12 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| b7ec814d-c568-30b8-8af8-9e8105549f85 | -6.42491 | -44.50453 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a0ee78ab-38cc-395f-b0d1-edc709eb2c36 | -6.18347 | -43.48689 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92268bfc-492d-3e7e-b573-72139b98b2a7 | -6.29818 | -44.58338 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README7.md)
