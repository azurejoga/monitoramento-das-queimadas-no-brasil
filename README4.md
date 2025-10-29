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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 460cda98-5a67-3b83-a8c4-af2f8febb591 | -19.4208 | -48.0797 | 2025-10-29 02:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7ca43b8c-4527-348a-a50b-c8df25dd6b89 | -10.6506 | -48.009 | 2025-10-29 02:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ac0f78fe-8849-392b-a768-89793fe9a724 | -10.6509 | -47.9869 | 2025-10-29 02:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 9243d7ad-24a8-3dfc-bdfd-dc34a14b6622 | -6.2939 | -41.8744 | 2025-10-29 02:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 646c99fe-7c4e-354a-8447-1ebfa868f01d | -19.4214 | -48.0566 | 2025-10-29 02:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 337771b6-cf5d-32f0-a57a-3911936cf7b5 | -15.1 | -43.8573 | 2025-10-29 02:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2fd1db23-8ebb-3b8d-9a2c-b393fe568d36 | -13.6426 | -46.4976 | 2025-10-29 02:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 0cae3bfd-1879-3fbe-a2c3-e4d426262f94 | -4.1972 | -50.0819 | 2025-10-29 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 155d7861-0d77-3d0c-a524-bc6506254b56 | -6.2936 | -41.8984 | 2025-10-29 02:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 48445e4b-3ea1-3f22-b657-6602fdee2451 | -12.0032 | -46.7892 | 2025-10-29 02:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ef000794-1453-3da2-930d-0dc43066e545 | -19.4411 | -48.0753 | 2025-10-29 02:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| bd9699c8-1027-3475-8d52-66ed2a8ee460 | -7.8037 | -46.4458 | 2025-10-29 02:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d32d1efb-79cb-30c1-96dd-11f64727e7ec | -9.5106 | -46.9872 | 2025-10-29 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 36a307b7-968e-3a41-beee-baa900327641 | -15.1 | -43.8573 | 2025-10-29 02:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b129f221-12c6-30c6-b547-93125616310c | -12.0036 | -46.7667 | 2025-10-29 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ee56b8c2-994c-39ee-8b26-821c1035fbd0 | -10.6506 | -48.009 | 2025-10-29 02:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d8bdf211-1d18-3874-a17a-2f84fdb31f0c | -15.1202 | -43.8294 | 2025-10-29 02:30:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2f88871e-5fff-3b46-9878-a53047ede49b | -4.2156 | -50.1022 | 2025-10-29 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a2d01663-de62-336e-a773-c2e43f944bf0 | -7.8037 | -46.4458 | 2025-10-29 02:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 0d5e28db-4a33-363e-8cfa-69b960575023 | -19.4214 | -48.0566 | 2025-10-29 02:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 4de8230f-6c79-3d74-b72b-47fd2e3623ac | -19.4208 | -48.0797 | 2025-10-29 02:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8719897d-4200-3d27-ba91-e64706a87a1f | -9.5106 | -46.9872 | 2025-10-29 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 12185fb9-c39d-30ba-8374-25c1d38ae08c | -4.4804 | -43.447 | 2025-10-29 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| fa97d495-5b03-3575-9e40-90232d1c778f | -13.6426 | -46.4976 | 2025-10-29 02:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 950dec1e-ce8e-3d3d-86cc-4b3c2d3a3680 | -9.9619 | -47.1593 | 2025-10-29 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6299197b-e6b4-30e3-89c6-4fdb6aea3684 | -19.4417 | -48.0522 | 2025-10-29 02:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5a0bde51-c1dc-3b98-a227-9a8974b483d1 | -15.1006 | -43.8333 | 2025-10-29 02:30:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 277.3 |
| ffe49361-a059-3127-84a8-44ff9bf48902 | -9.4916 | -46.9893 | 2025-10-29 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 1a2753a3-e12c-3f52-91ba-5d36ca0e23b0 | -15.1011 | -43.8093 | 2025-10-29 02:30:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 5f337fe0-e136-39a6-bf44-59c48d501506 | -10.6509 | -47.9869 | 2025-10-29 02:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 86e54b8d-3472-3793-ab0e-6fa67c48ce6a | -9.5109 | -46.9649 | 2025-10-29 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 176bbeeb-f929-3feb-961e-74429ddd6744 | -2.4263 | -49.3161 | 2025-10-29 02:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 9f680041-7488-38e8-8889-229987bc8e8a | -9.4913 | -47.0115 | 2025-10-29 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| bf98d862-737f-3218-970c-ea428aaa881b | -4.2157 | -50.0812 | 2025-10-29 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 6b0b26a3-1aa2-3976-94f8-c00eb4c40b08 | -4.1972 | -50.0819 | 2025-10-29 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0e2d4684-2209-30cf-b283-2dc4bb2efe8b | -2.4264 | -49.2948 | 2025-10-29 02:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| c6ced0e5-676b-3dbb-aac5-6e74da2e1ad5 | -12.0032 | -46.7892 | 2025-10-29 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b864f233-0852-3417-99b7-303c48aa4e99 | -6.2939 | -41.8744 | 2025-10-29 02:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| c9621cb3-9fc6-369f-a8db-56f9c95df788 | -15.1202 | -43.8294 | 2025-10-29 02:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c87b72d4-0606-35c9-9fa0-91f2481dd8e8 | -15.1011 | -43.8093 | 2025-10-29 02:40:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e58ec75e-15bc-328a-92b2-0711f7f9d3e3 | -12.0036 | -46.7667 | 2025-10-29 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 81bdcb7f-d45b-3345-83bf-1c01c51849fd | -10.6509 | -47.9869 | 2025-10-29 02:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 43381294-2e16-3e3b-98b1-9d1136a17568 | -12.0032 | -46.7892 | 2025-10-29 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6dfff89b-66c8-3e19-b90d-3b4eaaa285e5 | -15.1006 | -43.8333 | 2025-10-29 02:40:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 260.0 |
| 34f5b7d9-45d1-343f-9743-e30ff11a687a | -10.6506 | -48.009 | 2025-10-29 02:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 76b128d3-4b3e-3d6d-a1c9-bbc4014a1b16 | -9.5106 | -46.9872 | 2025-10-29 02:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| bb502063-44c7-357d-af1a-8bf8aba0d3de | -13.6422 | -46.5205 | 2025-10-29 02:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8ee7423e-013c-31b1-b487-bad8bb7adc99 | -9.9619 | -47.1593 | 2025-10-29 02:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 4f57d2bd-5557-364c-ac67-070257a1f92d | -4.4804 | -43.447 | 2025-10-29 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 2ea2126e-db79-35fd-945f-7f6e66f7f02f | -4.2156 | -50.1022 | 2025-10-29 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7c076bc4-36c2-3177-8afd-53ddb3f475ec | -4.2157 | -50.0812 | 2025-10-29 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 040cf0fd-94bb-369d-9a84-fc2ee912e466 | -4.1972 | -50.0819 | 2025-10-29 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f8c976bf-40db-3f1d-ab26-827be71bbe13 | -9.4916 | -46.9893 | 2025-10-29 02:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| fd663a44-47bc-38d2-af80-ec7d0196ed6d | -13.6426 | -46.4976 | 2025-10-29 02:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 817fa5c2-55ee-3ba3-8e6c-700f2c664bb1 | -15.1 | -43.8573 | 2025-10-29 02:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 446108bf-e7ee-3c22-aebc-fda4acd3477f | -6.2939 | -41.8744 | 2025-10-29 02:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 3705ec4e-98ce-3774-a409-d5cf4bc43a6b | -7.8037 | -46.4458 | 2025-10-29 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7574585c-f6e4-39ea-bf12-006035f37e34 | -15.1006 | -43.8333 | 2025-10-29 02:50:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 220.1 |
| ddd09924-b859-3e6e-a74e-de23ca9b175a | -4.4804 | -43.447 | 2025-10-29 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 09d50643-3d7f-3b86-8ad9-06a26181641a | -10.6509 | -47.9869 | 2025-10-29 02:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| baf2d85d-516a-3045-a9a9-47725d37f2cc | -13.6422 | -46.5205 | 2025-10-29 02:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 34508b87-a6f7-3a34-a712-787ed4b53f07 | -15.0809 | -43.8372 | 2025-10-29 02:50:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 3e43c4f5-bded-3ee7-a5fe-df4fc08ac70d | -18.9204 | -45.0237 | 2025-10-29 02:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 89e758a5-9317-30a7-a1ee-d67c7b12d8c0 | -6.3127 | -41.8727 | 2025-10-29 02:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 3c202fdf-48e1-3215-9609-56c318db20c4 | -6.2939 | -41.8744 | 2025-10-29 02:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 1f13f031-c2b4-3ff9-b282-cc7015bf22fb | -7.8035 | -46.4681 | 2025-10-29 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3f176739-26d2-392d-892f-b79235632ff7 | -6.1001 | -42.4391 | 2025-10-29 02:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 5278fb41-da4e-3af5-85fc-83e80a24f357 | -12.0036 | -46.7667 | 2025-10-29 02:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 675bc1b7-0048-3cb6-a03b-604c97ffdbbc | -15.1202 | -43.8294 | 2025-10-29 02:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5da47bff-65b5-3620-a884-46d0807b49eb | -4.2157 | -50.0812 | 2025-10-29 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e0867ff9-77f7-3874-9827-ac3000791028 | -7.8037 | -46.4458 | 2025-10-29 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4c4eed76-30cf-311b-b85a-0c667e77cd14 | -12.0032 | -46.7892 | 2025-10-29 02:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| aaf46161-8c57-3d37-9205-b7264f05ea05 | -2.4263 | -49.3161 | 2025-10-29 02:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 29054115-f559-3e22-a75f-1d483bf02242 | -15.1 | -43.8573 | 2025-10-29 02:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9a24841a-fcbe-300b-9d6d-68ce2f72e6b3 | -18.9197 | -45.0478 | 2025-10-29 02:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| f2523ed9-1679-3d14-87ce-776d3d06e44f | -10.6506 | -48.009 | 2025-10-29 02:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2b19e5b0-f9b3-3f6f-b5de-40e5c921807b | -9.943 | -47.1614 | 2025-10-29 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 1cf8848b-db74-32d0-9264-a0efae658fef | -13.6426 | -46.4976 | 2025-10-29 02:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 0048a35b-7905-330f-9b93-38be71af8efb | -12.0032 | -46.7892 | 2025-10-29 03:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4dd314dd-8fb5-3ff8-b6d6-18de98856bfa | -12.0036 | -46.7667 | 2025-10-29 03:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 6b493510-6c1e-35cd-95ea-71e0dff0f8e0 | -4.2156 | -50.1022 | 2025-10-29 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| ac9363ed-b0a5-3c22-8aeb-059dbcd7ed38 | -18.94 | -45.0429 | 2025-10-29 03:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6ac9f578-0627-3693-8d97-96e9ccd4bb00 | -13.6426 | -46.4976 | 2025-10-29 03:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fa004dcb-2d9a-38ee-a56d-c4d348ebdf25 | -4.4804 | -43.447 | 2025-10-29 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 490af1f7-a282-3076-bf10-443a0c905537 | -18.9407 | -45.0188 | 2025-10-29 03:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 18be76e4-cf60-3d2e-b0ab-b03c80a5826b | -6.2939 | -41.8744 | 2025-10-29 03:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| bdc9eb31-e7a9-3ec5-b043-4ac898ea1dc3 | -15.0809 | -43.8372 | 2025-10-29 03:00:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 75.0 |
| afe6e1e8-bff9-3296-a6a1-9b98a378650f | -4.2157 | -50.0812 | 2025-10-29 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8ced91a6-8686-3e15-a96e-28965cb9eea4 | -15.1006 | -43.8333 | 2025-10-29 03:00:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 216.5 |
| cc5ed4c5-2723-3e59-be32-9545e7c6e3d7 | -10.6509 | -47.9869 | 2025-10-29 03:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 29fa8166-63cb-3e2d-acf7-6ae23807a388 | -10.6506 | -48.009 | 2025-10-29 03:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f3d540af-3bc5-3725-91f1-50184c17b9f4 | -7.8035 | -46.4681 | 2025-10-29 03:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| eceb46d7-6d9b-3ee7-af69-c2dd2de2176f | -18.9197 | -45.0478 | 2025-10-29 03:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| debb72de-1203-303f-b97d-acbd72d2a95e | -6.1001 | -42.4391 | 2025-10-29 03:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 65c0a302-aff9-3316-ac97-af58da4687e3 | -7.8037 | -46.4458 | 2025-10-29 03:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3cfd9f13-0342-3be7-846d-181a93f7f2d4 | -15.1202 | -43.8294 | 2025-10-29 03:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4a673186-f1bb-388f-9bed-d1337db011c3 | -7.03688 | -39.48211 | 2025-10-29 03:04:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 64357d44-982e-3fbf-9a70-5137392e583e | -5.90209 | -37.82891 | 2025-10-29 03:04:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 71bca10e-1eea-33d2-ba38-188df6a7b80a | -8.13528 | -37.22705 | 2025-10-29 03:04:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3e5b70d-a47d-342b-aeca-6e76664fd697 | -5.89622 | -37.82807 | 2025-10-29 03:04:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
