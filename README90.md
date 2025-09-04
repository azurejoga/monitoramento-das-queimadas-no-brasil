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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3165995-9e65-3294-84e9-7340dc63ea4c | -12.94025 | -48.06868 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edbbd0d4-1f88-3068-a380-5db341350fa6 | -14.56736 | -48.05684 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf332e78-5362-371c-9673-a50e00116c1a | -15.02024 | -48.10498 | 2025-09-04 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9da7c6f7-db5a-3961-9d72-a1f292c3ec55 | -11.88574 | -51.53984 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9e9f095-da1d-3954-8419-98ce163fbb52 | -13.57088 | -48.13459 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aac947fb-9627-347d-81c5-723fcb4d7da0 | -15.0476 | -50.06188 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cc0a409-ef84-33a7-910f-4e1cad00be29 | -12.91578 | -57.00097 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b4ef0e6-af47-32b8-a031-dabf281059b3 | -12.90222 | -56.94218 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 534f9195-a158-3401-98cc-169c7e3e234b | -14.59552 | -48.01827 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eee5b556-7fc0-36f1-988f-eedbb50323ea | -12.90957 | -56.94329 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92c645ea-6829-3330-8386-4d939eddd739 | -15.6105 | -52.8917 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4edb3a55-a0d2-347b-b384-be33b2c926e1 | -13.10099 | -57.11468 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 0e27c06b-abf4-3f13-a673-26666bd1625a | -12.91516 | -57.00534 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ec3a372-8092-3b23-9bf6-e5324399b6af | -11.54017 | -54.48824 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ad3b56-9ae3-3b0e-b4a4-20de4860cd8d | -14.59623 | -48.01131 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6731dbc7-f577-36d1-bef3-c68c1a2b104e | -13.5795 | -48.12249 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f406ab3-fbf8-3f57-9117-3a1834cf5622 | -13.08846 | -57.12315 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82af1f35-d703-38d4-a268-abb259c04d77 | -10.78921 | -52.76269 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8a7d06a-01d7-3e7d-8190-9d783baec8bb | -14.88384 | -59.50207 | 2025-09-04 05:18:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 308742db-710e-3521-9527-a83ef6a65861 | -12.90279 | -48.0488 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1103623-dfd9-3acc-964f-2e13f4de6b4f | -15.19139 | -48.01936 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbf19387-ff4b-3973-ae38-8f36d688e18a | -14.53823 | -48.07774 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93debd0a-0c45-3cd8-a677-bdb2a12bad3f | -13.1089 | -57.11146 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 24ac6f80-3129-3b5b-a09f-d03e318faa47 | -12.48469 | -48.07832 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba013eef-a577-35a2-92d0-c2666a8b649f | -15.41681 | -55.93762 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e6b7bdc-502c-35ae-a42b-6ad4bef319d4 | -11.54069 | -54.48432 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 656cbd06-a8e3-305b-a02c-5409761a318e | -11.87897 | -51.55179 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7510d0b-0118-32ca-8094-4b9757371818 | -14.53159 | -48.07695 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e3ff73e-f365-3815-a4bc-286976420137 | -13.10525 | -57.11089 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 62c2def0-2296-3095-84b4-04b29ae8a217 | -12.60698 | -56.99589 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a8756c94-6de9-3fe3-a8a0-8940e9e26c7b | -14.56614 | -54.53762 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c22fb3d5-bffd-3860-a648-4cb5f8c25eec | -14.9101 | -49.62823 | 2025-09-04 05:18:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78f0d6e6-17db-3c35-9180-d67c6c75e052 | -12.93379 | -48.06736 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3899a83a-fd77-3707-a3a6-7c06e4c7993b | -11.65633 | -54.51931 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5f7c03f-ebed-33d1-8f9e-ed6a07040d2b | -14.75152 | -48.08617 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56bc0b8e-82df-3ba8-8711-3541d9e8e315 | -11.61624 | -47.78183 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d830fe5-c5b0-362b-92e4-654682fbb3a3 | -12.97618 | -54.78684 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f05623e4-7cb3-33b3-896a-b16b10c6ccd8 | -13.29662 | -46.84544 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d851ece5-5b7e-3c5d-962c-1bd2c3b505d9 | -15.17524 | -52.35878 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff5727b7-f95d-3c80-9f19-e32fcac5c02c | -12.63444 | -56.98666 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fc2347a-31a1-3149-8222-46fc93fd9173 | -11.86625 | -51.52822 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9acf1768-c7de-3e78-aa30-7cf64ec99fcb | -15.55406 | -48.41544 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ae96a44-9077-3e1f-8d89-0eb15c11e12c | -15.54695 | -48.40366 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9388f79-106a-3ae0-a19b-41106d52b0d0 | -10.40957 | -60.80441 | 2025-09-04 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d7302e1-da20-3a83-baef-414933261653 | -12.96005 | -48.06648 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c8fe865-4e37-393d-826e-f07e214a8729 | -13.5785 | -48.12499 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06e8891e-d8a8-355d-81cb-6d703def0f54 | -11.83724 | -51.42373 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83eab94e-8919-3b57-bc3d-f8500bfcc727 | -15.00712 | -50.04844 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4ead7fe-66fd-37d6-82ce-0195728c0254 | -14.55558 | -48.04123 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6194cba6-98c4-368a-b72f-65ac7185d044 | -12.62651 | -56.98992 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c2e62af-4f26-33e5-89e7-71ad2c9b4ac4 | -12.63558 | -57.00463 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11d66437-4af9-3669-ba87-b21ae1d16406 | -12.87296 | -48.01884 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3199bd41-6b35-314c-8680-762ab0cc8e44 | -12.9987 | -48.07586 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 362a64f5-98e3-390c-8308-df8b77c70c7c | -12.46445 | -48.08297 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa6e3f1e-51ba-3e07-b373-031d7504598d | -14.81222 | -48.21439 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efb568e6-c1cd-311c-8c89-dd1de40d9df4 | -11.86226 | -51.4346 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4aa19f1-4fd5-3816-820c-9c267cca182b | -13.74276 | -46.94207 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dfae374-22ad-3a31-bdbf-f71e139409dc | -15.18521 | -48.01323 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4db3dde9-a49b-3943-af72-6290593db78f | -14.39831 | -51.67181 | 2025-09-04 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fbbe1a9-770a-3a18-aa51-c64a1c3f04fe | -11.78081 | -47.33223 | 2025-09-04 05:18:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df8bce09-d50f-3cf1-8c67-18ff7b95276a | -14.57268 | -54.55579 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eede476-4baa-3320-8fb2-ad092e850a7c | -15.18464 | -48.01907 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45f78b2e-612b-3495-9b2b-f9d61cd108b5 | -14.53882 | -48.07215 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c12cdc9-486b-3462-aab5-9e286971497b | -14.78662 | -48.13799 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13612ab2-334d-3c56-85ac-1f0c9d5d8380 | -11.88097 | -51.53619 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9481b564-a198-33b9-91cc-44129eab2f4b | -14.99303 | -50.06781 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7da9d472-ca64-32e5-ad0b-5957099f28fa | -12.47102 | -48.08303 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23bf8522-89d5-3987-abd9-0f2f49015260 | -12.45797 | -48.08117 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ebbf958-cfe0-3061-921c-9446043f6b1e | -15.04589 | -50.07716 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 655e813c-c19d-3dfb-b2c5-512a73117093 | -12.47812 | -48.07829 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77b99950-5167-3018-8474-f6512dd806cf | -13.74733 | -46.94955 | 2025-09-04 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94b57bc9-a2d3-3bae-a0cb-383bd583f1d6 | -13.95401 | -53.98417 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6abe292e-56e7-3f83-b221-db820da2ea44 | -14.56204 | -48.04375 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5821950f-1ee3-3c2d-8036-869b6e36ed07 | -15.04431 | -50.0375 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c2c2015-1532-36aa-99d4-5be2cbeae6e8 | -10.61514 | -55.40675 | 2025-09-04 05:18:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fc8ff28-9990-3a05-9dc3-2826953b4fab | -12.6381 | -56.98721 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b662a68-5386-38d2-9811-8b3706babe31 | -12.97564 | -54.79077 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2481ec06-130d-3a09-9518-94f9bec9b0fc | -11.19502 | -55.01126 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79ba9f99-d21e-32d9-930f-e6f344edaaaf | -13.43474 | -46.93367 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac881af2-5898-36d1-9dae-62f59d6999de | -12.63495 | -57.00898 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9d4f03d-690a-352a-8652-99de18c65b7c | -11.57789 | -52.11001 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30f74dbf-e8e4-3df9-9961-91782190afd1 | -16.55573 | -55.10587 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4bfb27bf-9be0-35ac-82d3-03f66b7b4eef | -15.5938 | -52.8937 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82a96dad-0ecb-36fc-bf92-f05795402b8d | -11.20559 | -55.02386 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab9bc81a-690c-3b48-9b9b-50e0e45fe1ab | -12.96063 | -48.06393 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2591bacd-5f4b-31b5-9ece-96856977201b | -11.63503 | -52.2082 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dc20486-d3bd-3008-9a5e-5bb7dd95bb28 | -14.81906 | -48.33129 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91816152-c05a-310b-955b-9731c698f750 | -14.20609 | -48.08993 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f48b34e-3e93-3d07-bbe8-eb5e5e9d4ec4 | -11.73119 | -47.75603 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61d24a3f-ec5e-36e1-8116-361294d8e89e | -12.61001 | -57.0008 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a8d73b7-e9d0-322e-8b79-13463183091e | -11.88018 | -51.54233 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5329fda4-f107-38f2-a1d3-3807323dc14d | -13.57139 | -48.12962 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3fcf670b-2e8b-37ee-8766-5abe3d3e540d | -11.19803 | -55.0191 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db0942ca-5c54-328e-a888-f2f31d475fa3 | -15.1468 | -52.33622 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f45a506c-5b4e-318f-88a8-90153df37eb8 | -11.63856 | -52.19929 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07bbe1aa-eeb6-33c0-9219-85945faf65d5 | -11.65001 | -54.53448 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61ea90e3-6f48-3f95-a51e-8aba2bfc36f2 | -17.0392 | -47.13968 | 2025-09-04 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 873e97b3-99ab-3aa8-8781-91b8b9cd65b8 | -12.61064 | -56.99643 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5720fabb-f051-3871-9dc0-a9a3712aa03c | -15.04134 | -50.06421 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f83ddc33-a96d-3459-963a-550087cf11c6 | -14.52186 | -53.14259 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README91.md)
