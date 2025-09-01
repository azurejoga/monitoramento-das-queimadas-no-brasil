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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49faa0f0-86bd-3f43-9023-1b9b32022d8e | -9.13802 | -65.83936 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1486f1f-635f-346e-b81d-3ff347d54ce3 | -9.17406 | -67.71819 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 829918c6-5d37-327c-b4f4-b5d29f942f63 | -9.86714 | -65.03308 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8290f2fd-2584-3aab-a8b2-2b7e97e0e855 | -8.83877 | -64.14666 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d73e9d33-dc31-3d2e-a850-c5fd36ce9acc | -10.08237 | -68.99799 | 2025-09-01 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 351e7d8a-f062-3856-90c2-09b28bce4fd1 | -9.69107 | -65.00782 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7ac0639-8b0c-3eca-b59f-f733c468be4c | -9.11923 | -61.21435 | 2025-09-01 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c75658-ee06-32d2-9558-dfba12aed6d3 | -9.00714 | -65.69137 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d64d20cd-11c2-319d-b27b-d5d7190dbe45 | -9.83187 | -65.05198 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42a6a301-5c5d-36d5-b7bb-82a4cc1eb0de | -9.17861 | -65.77789 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdf17de9-b38f-3013-a54c-e037ab47a004 | -9.83479 | -65.05647 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbb5a18c-e0a3-343f-92c5-7413fc9bd62b | -10.92468 | -69.21031 | 2025-09-01 05:53:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72595397-5834-304c-8fe3-4183cc5f3a7c | -9.1362 | -65.85043 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b68079-b0b4-339a-81fb-b0b14c017bb2 | -9.4857 | -65.59567 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3502dd87-5a96-32fc-ba88-7da12ebfdd09 | -7.91013 | -71.58842 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 330cac1a-0dda-31aa-9857-9ca4c6bcd8f8 | -9.17129 | -67.71416 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb32d7a3-bf24-3e13-8096-710b5e907419 | -7.0757 | -44.3606 | 2025-09-01 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0fb420b5-0871-3165-aa8a-d4550bb3e052 | -10.5937 | -44.331 | 2025-09-01 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| c215d3c3-7dd6-33a7-b6ed-c01493b37fb9 | -15.7289 | -48.9892 | 2025-09-01 06:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 46a5799e-e6a4-3e25-bcd7-827a6a23825b | -7.0946 | -44.3589 | 2025-09-01 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 596b7951-2823-36bb-807e-c974f0ceb7c5 | -10.6128 | -44.3284 | 2025-09-01 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 8c9ec619-cdcd-3b45-a01a-2e7bc53c1357 | -11.0373 | -45.1717 | 2025-09-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 54078221-26b1-3cb8-843f-690b64c6e42e | -7.076 | -44.3376 | 2025-09-01 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1ccf250b-cbad-37ea-80ba-cea340c74ccc | -11.0565 | -45.1691 | 2025-09-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5c0f73dd-cb9e-35a5-b254-9a03c915a2e2 | -18.6503 | -52.6007 | 2025-09-01 06:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 941e7747-20e2-3afc-9098-f3e5ff2693d1 | -18.6704 | -52.5973 | 2025-09-01 06:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a9730839-6ef2-3e2b-bb05-7bbaafcf66f6 | -12.8625 | -48.0545 | 2025-09-01 06:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| fb4deab4-3bcf-3a86-bd07-b13c0bb4154f | -7.0948 | -44.3358 | 2025-09-01 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9f7d8841-db84-3485-bf97-488dd4a35628 | -11.0568 | -45.146 | 2025-09-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 335.5 |
| 91f73b67-e715-3ca9-bbd3-0441b0cd8bc8 | -11.0377 | -45.1487 | 2025-09-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.6 |
| 22c59f44-f24a-3fd5-9ab6-6e1b9aa5b66a | -11.0381 | -45.1256 | 2025-09-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e46cecc3-573a-3125-b7b8-935f64cbb44d | -11.0572 | -45.123 | 2025-09-01 06:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1503278f-21d4-3c3d-bb3c-04247873048f | -11.0648 | -47.0042 | 2025-09-01 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 9cda52b4-d338-3cfc-ac56-0eb99c2aed0c | -11.0457 | -47.0066 | 2025-09-01 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 271.0 |
| c6febb87-6734-3997-b920-2c9e945873ae | -15.7289 | -48.9892 | 2025-09-01 06:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 0eb17e57-5d8c-341a-86d3-10c417de4b1d | -19.966 | -50.4197 | 2025-09-01 06:10:00 | GOES-19 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| 7721c5f9-8f2f-3b4d-8260-61359d18706a | -10.6128 | -44.3284 | 2025-09-01 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 4383d16e-b72d-3467-bd19-8bcd89c7b55e | -7.0946 | -44.3589 | 2025-09-01 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a73ed14b-c047-3bde-b075-4e4f9ff188a6 | -15.5862 | -48.3435 | 2025-09-01 06:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 43bd8e49-1cbb-3ddd-8445-03001a1e4387 | -11.0565 | -45.1691 | 2025-09-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f048211e-2c5e-33e1-965f-2948daad8aa4 | -11.0461 | -46.9842 | 2025-09-01 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| e995dd7f-39d0-3eda-b4b6-dce10fea9f2a | -11.0381 | -45.1256 | 2025-09-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e927b6e1-bdcb-3a9e-91de-65fd0487e076 | -11.0377 | -45.1487 | 2025-09-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 5f3e17a9-aa04-3cf5-ad34-4dff5404a0f6 | -7.076 | -44.3376 | 2025-09-01 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fd1cf0a5-608e-3719-af25-1fb851ab16f2 | -11.026 | -47.0538 | 2025-09-01 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 6b7f8493-78d8-32c7-9080-8aaa9a958d81 | -11.0568 | -45.146 | 2025-09-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 300.6 |
| c9cc68e2-8f92-376c-8f21-5f187093ba65 | -7.0757 | -44.3606 | 2025-09-01 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a1c2248c-acb1-3532-9b53-a23a36dd60be | -15.7112 | -48.9032 | 2025-09-01 06:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 760dab79-0d02-380b-8127-e67b92227f21 | -11.0572 | -45.123 | 2025-09-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8e7142d3-50d7-30ab-93e2-0ed86f112c4d | -7.0948 | -44.3358 | 2025-09-01 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 35bd7fa5-bd8e-36f9-8288-05d827c87cad | -11.045 | -47.0514 | 2025-09-01 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 2828950b-c519-3561-94dd-995996ddb3fa | -10.6131 | -44.3051 | 2025-09-01 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c9b36114-c0b0-3ea0-b2a4-2b0ced116e00 | -11.0373 | -45.1717 | 2025-09-01 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d58a50a1-d6cc-38d6-a720-b1e74c39f0a0 | -15.5867 | -48.321 | 2025-09-01 06:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 58abe506-4de2-34e1-83ae-427f2f199274 | -11.0454 | -47.029 | 2025-09-01 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 645ecaa6-10d9-390d-a2d8-c6e0dccd62f9 | -10.5937 | -44.331 | 2025-09-01 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f392e69c-9947-337c-8622-1564d1a640e7 | -7.10897 | -63.03389 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76b19bba-1170-3fc6-85b3-c1d9f495e62a | -7.59042 | -61.62539 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16701864-139e-374f-a4bd-97eae5a8f613 | -10.08649 | -68.47298 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91a9e774-9c1d-38cd-9365-8daa1927dadf | -7.7019 | -61.48217 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdbd5f32-8dbc-38ac-949b-e6b21916d933 | -7.7026 | -61.47676 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebc95cb8-b645-39f7-b4f7-3429bed395a4 | -8.50871 | -67.13197 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f63d0c37-9d4b-3a0d-945d-bf337621736d | -9.13987 | -65.84235 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d171df05-ea7a-350e-9bde-11cdb0455971 | -7.09624 | -63.0405 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4330ee6-7d10-33bd-aaf0-3ea33a2356a4 | -9.88362 | -65.01713 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80404c81-2e74-33da-bbba-2f6f8cae2ad4 | -8.72836 | -62.41787 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 926a2427-dc64-3076-994d-0f453731abde | -9.27654 | -67.64694 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a82e06c-6053-3c30-a6c2-e427cc463f85 | -9.95419 | -66.87013 | 2025-09-01 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10e589dc-7519-317c-beb2-8c44266aed62 | -7.70059 | -61.48473 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e79f5203-4eec-3d35-8bbe-32717d9bc8e6 | -9.12504 | -65.84017 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a030df-e062-3b93-81db-ed3c74913ccc | -9.06317 | -65.42966 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb76a960-60d9-3c91-ba49-68c76a3c765a | -8.73138 | -62.40142 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d435ca9-9aa0-3fc0-a800-70f8e8de6b95 | -9.66375 | -68.97681 | 2025-09-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c353be6-2956-3a4f-acd3-1328beacdd53 | -10.49978 | -68.10687 | 2025-09-01 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cca4e81-aeae-34a4-b259-3ee250843a54 | -10.57064 | -69.96694 | 2025-09-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d87ee70a-0997-3ec5-a4c0-4ffbf99d495d | -9.83711 | -65.05078 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 010a0351-a9e2-3268-91b0-2933b8f17dd7 | -9.17145 | -67.5643 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4af7ae9f-1fc6-36f7-856c-d67fc3953165 | -8.69182 | -62.41574 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df1f3ccd-a6c3-3807-82e5-10e56231eddb | -8.70371 | -62.41431 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6db01184-3e46-3364-abae-36cfd7e7388b | -8.75914 | -61.42632 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6d82e4b-b514-34ab-85cf-b01edaa53466 | -8.59758 | -72.82556 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92f26515-2d88-3988-a4c4-0e85e95d9afc | -9.13418 | -65.84728 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9280eb24-dce3-313b-83b0-cde5da671c87 | -10.08338 | -68.99759 | 2025-09-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97898dc0-331c-3de9-ac49-2b98eb610cb3 | -7.8202 | -72.91369 | 2025-09-01 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742dfd2b-4709-3a6f-b27f-3b0c76292802 | -9.86525 | -65.03468 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7abc6264-018f-358c-9786-fa9029a23329 | -9.12343 | -65.54694 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03a94871-2162-31ff-b2e0-09f6a84f9ad2 | -8.66418 | -62.92722 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea2644ed-2657-3e25-8f4b-79f7908263c4 | -9.06358 | -65.42665 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b45c2dc-5429-3848-94c1-ef8ce3416357 | -9.17585 | -67.56491 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4a5ca23-c19b-38c3-94be-2eb8e36178b2 | -8.46192 | -71.18079 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c8d7ba3-6fc4-3d94-a315-f6a79606b9b4 | -9.13313 | -65.55124 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cbd63f3-672b-3c74-b601-de628f2516e9 | -7.93295 | -72.99578 | 2025-09-01 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da9e0882-b96e-392b-8cc0-e2c233d68caa | -8.93932 | -71.27718 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0182e90-fda2-368c-a484-b3fe17d68390 | -7.0951 | -63.13548 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de7f3e85-2fe2-325c-a103-a9643c07ac67 | -12.44523 | -63.92369 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22c1c47a-8795-3187-af33-2f15baea8c54 | -7.27744 | -60.65645 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d08c313-18ec-376a-ad61-4bc6b66da6a9 | -9.87979 | -65.01312 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab3bdec8-360a-3cd5-abd3-1f3f0200d031 | -9.88553 | -65.01054 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bbf69ff-12ee-3bac-a66b-26c0d090bfe9 | -8.72819 | -62.4255 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e18b6404-44d7-3ee0-8ba0-1a33edf2d2d1 | -9.88419 | -65.02047 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README93.md)
