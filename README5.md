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
| d06890ef-3f32-322c-8c93-d664e043d0f5 | -15.41405 | -56.29561 | 2026-01-23 04:36:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bde5d332-fde8-37f2-beac-b0df29032a91 | -20.38202 | -57.88832 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 217797ec-bf51-3928-a880-2999f5de973b | -20.90619 | -56.38617 | 2026-01-23 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78500b75-4439-3b69-b6e3-d829bcfcd9bd | -23.60076 | -48.33649 | 2026-01-23 04:38:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc7b4390-56d2-3178-87e3-213669fa762f | -21.5356 | -57.53916 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9222f991-ceda-3e2e-9a49-3e06044ca6c1 | -20.36284 | -57.86778 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ab7ee071-86f4-390d-b1d9-fee1c059ddda | -19.17658 | -57.54211 | 2026-01-23 04:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a9d84880-48eb-3ecc-99d4-7b89d52a720e | -21.19695 | -56.92993 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 563162fd-d304-3a4f-bf96-e69ae305cb1f | -20.49623 | -55.19282 | 2026-01-23 04:38:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a73a38a8-7288-3011-ae77-555425a52100 | -15.59196 | -59.29739 | 2026-01-23 04:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc3d42cb-de83-34e9-b4b7-e7c9c0e69c09 | -21.78125 | -56.28811 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3e34251d-986a-3839-84eb-82eada8bd564 | -21.53523 | -57.53645 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd123a48-5144-39a8-a043-78c68f66641f | -20.34554 | -57.86389 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| e6f38c76-79a8-3fdf-a886-4c54b3aea45d | -21.78301 | -56.28493 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| df12b2b9-e7e8-3aa9-b35a-c22e54ee9414 | -19.45763 | -53.98439 | 2026-01-23 04:38:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 345cf89d-64ca-36d8-8b6e-9ff9621226b3 | -19.66806 | -56.87182 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5df3097a-8e13-3233-aa7e-85fb87abb4f1 | -19.68047 | -56.91974 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 510eeb74-94d7-3c40-8010-3433aaeaacd3 | -22.01907 | -56.3399 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9da5ebe6-4478-37e6-ba3a-c7330873fb02 | -20.34209 | -57.85851 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| e4c45588-f428-3efa-878b-62377f85b860 | -19.32613 | -54.03054 | 2026-01-23 04:38:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a5aa932-5225-32db-942e-d4b17d7801e1 | -24.00397 | -52.56368 | 2026-01-23 04:38:00 | NOAA-20 | ARARUNA | PARANÁ | Brasil | 4101705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a20a580e-2e22-3c82-881e-4f3446fa9435 | -20.3829 | -57.88391 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a143bb26-e6f0-3add-8c95-42517fc884d1 | -22.6142 | -49.57247 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2944c2a5-c381-39c1-b10c-c900355a94c5 | -20.37063 | -57.87415 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 54f25793-0e26-3b92-9502-8ec963c74c79 | -20.37858 | -57.88294 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 912a8bf5-4ed7-3cc8-9a4a-07614a64a602 | -22.61074 | -49.57191 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c5efd0f-84b9-34c0-9ad6-6f3409c509fd | -20.37843 | -57.88053 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 910f70ed-ad59-3cf9-924e-67b2024f2ad9 | -20.33603 | -57.86636 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4c4d7ae0-c033-3695-ba67-577464fbb275 | -22.3679 | -48.34915 | 2026-01-23 04:38:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be09b5df-98d3-3a46-a5a5-e49f8b6c8227 | -22.60786 | -49.5673 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 129847ad-1f65-3d63-afa6-9fb83499c3dc | -20.36631 | -57.87318 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 105c6ebf-640e-3a16-9a3f-bbb6fbf9fb59 | -19.67634 | -56.91885 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0fd10acf-022a-3846-a9c0-a846c9c3cfbc | -20.32738 | -57.86441 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 43752ee5-b128-313a-a4c1-a81ba2dbd2c6 | -20.34641 | -57.85947 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 62780c9b-194e-32e9-9b9d-f36e09c990c4 | -19.67292 | -56.86877 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 495a9729-4cf1-3884-b48f-2adc079a6e92 | -19.67823 | -56.93164 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3ccdf4eb-4d0e-33ce-b886-2a0fad2fc98a | -19.17573 | -57.54644 | 2026-01-23 04:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4610185d-89c4-33d4-a60f-950c116c2787 | -19.68211 | -56.96336 | 2026-01-23 04:38:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 44d42dc7-0b9b-3d20-93e0-ef1167823c41 | -21.53634 | -57.53539 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9c66d261-8d57-336b-a3ff-e5fbffa30618 | -19.6688 | -56.86789 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 98dc588e-909f-39a8-9510-59a2f08c503d | -18.41695 | -54.56363 | 2026-01-23 04:38:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c6d109b-5cad-36b3-8d1f-8d2e319bf802 | -23.43918 | -51.42801 | 2026-01-23 04:38:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 27de0ffc-d8e9-3cff-899b-ec67456468f8 | -19.66393 | -56.87093 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 9f940cb0-528d-31f5-8b9f-773626063b6e | -22.60383 | -49.57077 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2006d284-b81c-3371-accf-b38951640ce2 | -19.68453 | -56.87538 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ff551b35-0f17-3ec6-bf1a-273b0d2cfda5 | -20.84377 | -51.73957 | 2026-01-23 04:38:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e915d6c3-fd48-30a9-9c7e-e6bbc9a63c86 | -18.16012 | -51.1238 | 2026-01-23 04:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85dd90d6-ef8a-3d24-bdbf-03e01aed0902 | -22.59873 | -54.98602 | 2026-01-23 04:38:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3ca9baac-adf9-3805-a7d2-96bfa0e860d1 | -16.26423 | -58.31913 | 2026-01-23 04:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1c409b39-8e02-3b7e-81a9-1cc0826fca32 | -19.68379 | -56.87932 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6d8f4419-3088-3a54-b1ef-7ccae6de174b | -23.05435 | -49.06079 | 2026-01-23 04:38:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 540e1eb5-1566-3a79-9e90-19b8d1a0f5a4 | -19.68041 | -56.87449 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4893bd31-5598-35f2-a37d-8fd6820c4a0b | -16.44749 | -58.16966 | 2026-01-23 04:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d1b720bf-3f05-3505-b908-079bb63f4473 | -21.77834 | -56.28218 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96f8e94b-9826-3276-8aa9-63d8d2641860 | -19.45336 | -53.98794 | 2026-01-23 04:38:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b211b2e-a031-333a-9517-f15f5d43a94b | -22.02389 | -56.33553 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e13989c-5467-36ca-a114-024caded147d | -19.1722 | -57.54141 | 2026-01-23 04:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3d98d120-5214-3283-a332-e68b44bc4622 | -15.5978 | -59.29526 | 2026-01-23 04:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e8f2299-4904-30e6-9956-c5630ea3c45f | -19.68311 | -56.92857 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| daea17ca-6c54-3a97-a162-16600a85578e | -19.29603 | -53.17499 | 2026-01-23 04:38:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 249d1082-a42f-3166-aaa6-7eecf3663e59 | -21.26177 | -50.87505 | 2026-01-23 04:38:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77f77e39-d004-31b9-b041-bd9f0c04158c | -21.53596 | -57.53262 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c38df30b-1254-352c-9eff-953db6f9717f | -21.78204 | -56.29002 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a00f2d4-5bc7-339c-9cf0-aeea315ddca0 | -22.61362 | -49.57649 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12ccf307-4376-31a9-bd7d-8b11a9c69409 | -19.17135 | -57.54576 | 2026-01-23 04:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7b9b5217-5293-33d4-8837-5ddc5a298543 | -19.77677 | -50.73515 | 2026-01-23 04:38:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 073ddd6e-1591-39a9-9eb0-868169dd2009 | -20.33171 | -57.86538 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d09aba46-4769-32db-9e86-c0bed27b3fa4 | -22.60325 | -49.57479 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48171c08-feb2-306a-8bd0-ea6ef2953d31 | -22.6067 | -49.57536 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d81730f-9490-3c44-9aff-c23e8c7c82d5 | -21.78218 | -56.28304 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| efaaa795-8ed4-3f81-bce7-e021fc0cc60a | -20.91013 | -56.38693 | 2026-01-23 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c32d2bac-f9c6-3b2e-8d4c-5f9f4053f4f2 | -20.3819 | -57.88593 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 09cb14e0-fc6b-390b-abe4-60c6e19d8cc1 | -21.77917 | -56.28407 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6c6737b9-dd8c-30ad-92f6-0a56e15afaab | -24.56659 | -51.97004 | 2026-01-23 04:38:00 | NOAA-20 | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e5fe97b3-41e3-379d-a561-70c3fe11f569 | -21.77741 | -56.28722 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 742d3757-e514-3382-b01e-a3aebd8f8462 | -19.84851 | -50.70982 | 2026-01-23 04:38:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c1af03d0-0c18-3322-ab02-ac4ee43d99a8 | -20.35852 | -57.86681 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ef9a251b-ae35-3aa7-85ab-9086e2ef8f0b | -21.53106 | -57.53562 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec9a1cf7-d2e8-34d7-905e-1995213e298e | -20.37514 | -57.87756 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dc9cecba-083d-3cdb-b970-8551e7535d52 | -20.34122 | -57.86292 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 50f5f4f9-4a2b-3c2f-b03e-f19baa3a45dd | -22.02292 | -56.34067 | 2026-01-23 04:38:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3c55f48-215d-3a5b-bb76-351991bf2c87 | -21.43212 | -48.78249 | 2026-01-23 04:38:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fda5069b-2b24-3170-aba7-6d9eedef4350 | -20.90569 | -49.14055 | 2026-01-23 04:38:00 | NOAA-20 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3a0656b3-00cd-32fb-b519-72b9724fc7bc | -19.68716 | -56.88416 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 92f9dc19-ad8a-323f-9809-67bacd34e5ce | -22.61016 | -49.57593 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec2f3122-0fdd-3ce8-a0df-7364ba5f60c2 | -21.53451 | -57.54019 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6758837-b55a-3052-b380-4554dbd146cc | -19.68791 | -56.88021 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3b6d9a47-fccf-33b4-bc6b-76af28056a56 | -20.90915 | -49.14111 | 2026-01-23 04:38:00 | NOAA-20 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 87b19ab4-50fa-3fc1-bd0f-d5e74823fb0f | -22.61132 | -49.56786 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88c8809f-e1c9-3686-93b0-c06be68702f6 | -22.60728 | -49.57135 | 2026-01-23 04:38:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cd405637-5639-3c1f-8c69-0d6aca78bd1a | -21.19622 | -56.93382 | 2026-01-23 04:38:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a37cfdeb-9487-3504-931c-3398d809860a | -19.67703 | -56.86966 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 44cf9d14-9291-37e5-9bfc-a0e1344abe1c | -22.73246 | -49.35115 | 2026-01-23 04:38:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9effa272-63bb-369f-a572-00ee03feff44 | -16.4438 | -58.16332 | 2026-01-23 04:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8ec918b6-ab4e-3a86-b183-b7c515aff78b | -22.03704 | -49.50315 | 2026-01-23 04:38:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dd820ae0-2989-31fc-a9ff-f4f3958b484b | -15.59715 | -59.29849 | 2026-01-23 04:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2add1a98-ae73-3799-bbfa-6d3e3678ed78 | -19.68115 | -56.87055 | 2026-01-23 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6ce0909a-4cd6-3bc3-b7e8-9fea36a19708 | -21.29218 | -55.92921 | 2026-01-23 04:38:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f4cd067-9a4d-37f8-9251-8a56a4b54530 | -21.19377 | -50.6569 | 2026-01-23 04:38:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e1c80462-3f1d-3faa-b173-c2500f90771d | -20.3741 | -57.87955 | 2026-01-23 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README6.md)
