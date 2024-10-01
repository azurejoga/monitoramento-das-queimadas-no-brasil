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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eeba5482-3296-3517-bfbb-d0383e65eba4 | -11.6641 | -65.195602 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99427ee1-74bc-38a1-82be-d6ffea664879 | -16.6459 | -55.1908 | 2024-10-01 01:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| cb441375-eaec-3c0c-bfca-5a5757c676e7 | -16.6263 | -55.1934 | 2024-10-01 01:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 519724c2-b3ed-310c-a1ac-1e7bc4ac58b8 | -16.8983 | -57.6949 | 2024-10-01 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 3552d5a9-1f2e-30af-9f0f-ff0578ee95ce | -18.5423 | -43.4683 | 2024-10-01 01:46:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| c71ad049-569f-388a-992d-81493f337581 | -18.6011 | -53.0412 | 2024-10-01 01:46:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 25e368e9-b898-3407-970c-41a765818ff8 | -18.6977 | -57.3123 | 2024-10-01 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 914bbba0-ad5d-3ea8-a8fb-6a19c95b001c | -18.6973 | -57.333 | 2024-10-01 01:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 8c8272a4-c5e6-3809-be5c-365d21708408 | -9.1935 | -58.198502 | 2024-10-01 01:46:52 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d49772eb-c9f3-3ff3-b8b2-0f8e89241899 | -9.1958 | -58.208302 | 2024-10-01 01:46:52 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05587b8c-0655-3a1a-8bca-8d153b007fd7 | -19.1329 | -57.4628 | 2024-10-01 01:46:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| e1a64794-2e7f-35bc-bfdc-28ecf3d7ddef | -20.6393 | -48.7549 | 2024-10-01 01:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| ee264a65-df6c-332e-9298-0a8b11b20897 | -20.6188 | -48.7595 | 2024-10-01 01:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| ece29126-207c-33ad-93d4-9f4b3d8caa81 | -9.9696 | -64.769203 | 2024-10-01 01:47:04 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef78f23-483d-3a3a-b061-9786d12ff48f | -10.7038 | -69.414398 | 2024-10-01 01:47:08 | METOP-C | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 151647a6-23e9-3e58-a34e-c795dc15e76d | -22.3922 | -49.2961 | 2024-10-01 01:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| 1e27313c-d3e0-31c9-b979-d0488ea55706 | -22.3916 | -49.3194 | 2024-10-01 01:47:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 9471e413-1eca-38f7-9475-f16a37934996 | -22.3713 | -49.3011 | 2024-10-01 01:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.8 |
| 169668e2-d43e-388f-9e7b-d124dfd83e95 | -22.3707 | -49.3244 | 2024-10-01 01:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 229.8 |
| edbb8b6d-90b2-3bcf-a018-cd20b8ba8e7b | -23.0793 | -45.3951 | 2024-10-01 01:47:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| cbdfca88-d7b9-34ed-99a3-7725507ebde1 | -10.2723 | -68.755203 | 2024-10-01 01:47:13 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 55583d3e-2ad6-3174-a492-54643c41d5df | -8.4759 | -62.7038 | 2024-10-01 01:47:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6dab5dee-1bba-3dea-a9eb-73b2180b1df5 | -8.4661 | -62.7061 | 2024-10-01 01:47:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 524c8844-0917-35b2-b028-89fc22b74fa8 | -8.4677 | -62.713001 | 2024-10-01 01:47:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c98045f0-f0c4-3ef8-9af8-8bbe520d6d3a | -8.4693 | -62.719898 | 2024-10-01 01:47:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb4548cd-09de-3a87-adc2-9dfeb20e16a5 | -9.2722 | -67.597603 | 2024-10-01 01:47:26 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd812e70-5287-3ef4-b82a-993c68043e45 | -3.0277 | -61.664501 | 2024-10-01 01:48:45 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0c44c9-c821-36a3-af9b-d891e8349227 | -3.0295 | -61.672199 | 2024-10-01 01:48:45 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49ba288b-dcd5-3281-b8e8-d17cb80db116 | -3.0282 | -51.3345 | 2024-10-01 01:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| eed94aa7-bbb3-352d-9a01-dcf3accc17eb | -5.9788 | -45.3621 | 2024-10-01 01:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1e9b8bb9-6708-3697-80e3-3e932f4bde3e | -5.9786 | -45.3847 | 2024-10-01 01:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 87e4cdfa-e063-3e5c-a57b-175fb6ff4394 | -6.545 | -43.0373 | 2024-10-01 01:55:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d68d0b03-619f-35b6-a897-3a167a591393 | -8.4643 | -62.7124 | 2024-10-01 01:55:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bf5f77b8-5980-33f3-9329-00f6f2fe90ae | -10.5743 | -48.0399 | 2024-10-01 01:56:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8bc7fa91-7165-31d7-b335-2a8262ad0d8b | -10.9429 | -50.0833 | 2024-10-01 01:56:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4b6dabbb-a0cb-3ce4-b1cd-4b39fef0d48c | -10.924 | -50.0854 | 2024-10-01 01:56:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f7e99e29-08a9-328e-9d01-1114f7a44d2b | -11.6744 | -64.9793 | 2024-10-01 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ad7e4513-787f-30c1-9b7e-3d8238cd265d | -11.6743 | -64.9983 | 2024-10-01 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 26a8e414-5292-38ce-b0a7-04ed7facfac5 | -11.6556 | -64.9802 | 2024-10-01 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 87764dd0-27e8-3363-9ab3-99160d7bef70 | -11.6555 | -64.9991 | 2024-10-01 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 3f75bcc6-d61c-37ec-912b-7a8532887bfc | -12.6039 | -53.4879 | 2024-10-01 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 39ca0edd-a747-3750-b6bc-edbd2a3c00ff | -12.7636 | -62.9036 | 2024-10-01 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9fe2012a-c01e-351e-9a21-1905404ef209 | -13.5957 | -51.1796 | 2024-10-01 01:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d03a9b5d-9aef-32cf-875f-c06332216f98 | -13.5954 | -51.2011 | 2024-10-01 01:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| c1dfdeb0-2318-3af0-9c0f-9e5e57cd5af9 | -13.5765 | -51.1821 | 2024-10-01 01:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 269ddcce-80be-3d30-b971-d77e4b97dc08 | -13.5761 | -51.2036 | 2024-10-01 01:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f8be95f2-9609-3f51-bae5-4a16bdd66594 | -14.7406 | -48.7498 | 2024-10-01 01:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| a9d558b5-653d-3c13-bb6c-c608ca6cd17c | -14.7402 | -48.7721 | 2024-10-01 01:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 78b00d12-1768-3120-8bdd-3c584f2943b1 | -14.7596 | -48.769 | 2024-10-01 01:56:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1a883bb3-9821-3c1c-b46d-d508fdbb41cd | -16.6263 | -55.1934 | 2024-10-01 01:56:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 1481c3e9-2997-34f4-83d8-ec1967d2291d | -16.5134 | -57.3305 | 2024-10-01 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 7f24eb88-200b-345a-9b68-3c0112461921 | -16.5131 | -57.3509 | 2024-10-01 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 059ae508-73aa-3adb-98df-35f352ccdd67 | -16.4939 | -57.3327 | 2024-10-01 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| c59f584f-ea2f-3381-a1c3-e1e502ef01c0 | -16.4935 | -57.3531 | 2024-10-01 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 0c6168a2-3e20-3ed3-9ba5-7732e94f26be | -16.4743 | -57.3349 | 2024-10-01 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 458df749-f574-3d12-8680-120e85d00896 | -16.474 | -57.3553 | 2024-10-01 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 90bcc726-17ec-3465-8138-3c1ef1b863ba | -16.7471 | -57.3651 | 2024-10-01 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 440faf12-d04d-3d00-a8e6-bf841e5137f5 | -16.7461 | -57.4265 | 2024-10-01 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 441c0714-98c1-3be9-8e95-5c78c8dcbedd | -16.7385 | -55.491 | 2024-10-01 01:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 31c16c28-d2a3-344f-9b61-560f198096a9 | -16.7382 | -55.5118 | 2024-10-01 01:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 37601541-ab74-3054-a98e-a79e0c1470af | -16.7189 | -55.4935 | 2024-10-01 01:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 138.6 |
| 6ee0a21d-27c3-3ed1-9577-a321df7ef9e1 | -16.7186 | -55.5144 | 2024-10-01 01:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 120.4 |
| 11a05c40-3fe8-390f-9fdf-0e7d7ba6c0e6 | -16.8784 | -57.7175 | 2024-10-01 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| d9964a6b-50ee-38d2-9c4c-8f9418ea0466 | -16.8983 | -57.6949 | 2024-10-01 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 962e0936-d95f-3c11-8666-8bc8ab2cc900 | -16.898 | -57.7153 | 2024-10-01 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| c623992a-cf1e-317b-81df-8e72257c2607 | -16.8787 | -57.6971 | 2024-10-01 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| c31e3d7d-a435-31f1-94a8-493b51bdaeda | -18.5423 | -43.4683 | 2024-10-01 01:56:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| 70d738b0-bfbe-399b-b193-a95e67a1da7d | -18.6011 | -53.0412 | 2024-10-01 01:56:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 7d9b9155-a723-367d-a815-d3de3a3a6d9b | -18.9085 | -49.2356 | 2024-10-01 01:56:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| d6fcfbab-b583-3e38-8a11-fd36b93014a1 | -18.7176 | -57.3097 | 2024-10-01 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| eb822501-5b0f-3b9a-aeef-2c4e31afb492 | -18.7172 | -57.3305 | 2024-10-01 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| d5c68b2c-5ab6-3d3b-b6b9-76b7ac4d2a2f | -18.6977 | -57.3123 | 2024-10-01 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.2 |
| c86720eb-ec0d-3c86-bd3c-36244618c06c | -18.6973 | -57.333 | 2024-10-01 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 242.8 |
| fc5dee43-4b8e-3b4f-ad4e-d711422301a3 | -18.697 | -57.3538 | 2024-10-01 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 72601a07-a5bb-32d4-b52f-89c9c6e10973 | -19.1329 | -57.4628 | 2024-10-01 01:56:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| ccd68979-3460-3576-a470-de0a49266f24 | -20.6393 | -48.7549 | 2024-10-01 01:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.9 |
| d5cbdc85-bfe9-390f-9012-fff610b4df9e | -20.6188 | -48.7595 | 2024-10-01 01:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| 556f563b-a35e-3acf-a591-07fe108d9a89 | -20.8123 | -53.1364 | 2024-10-01 01:57:01 | GOES-16 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f2b37bd1-6cb3-3a3d-8a26-fd287067d576 | -22.3713 | -49.3011 | 2024-10-01 01:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 167.3 |
| ec74c3d7-a1d8-3c4d-a6e9-ef66049cd4d2 | -22.3707 | -49.3244 | 2024-10-01 01:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 283.7 |
| 5043811f-cb49-3b3a-af78-b1b858a80984 | -22.37 | -49.3477 | 2024-10-01 01:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| afe45147-149f-3d88-aa3f-5fbe3c60b626 | -13.55 | -51.19 | 2024-10-01 02:04:08 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd838810-2920-32b3-a9fd-eb9bfe055caa | -12.96 | -51.37 | 2024-10-01 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6139a133-59b6-391f-9112-cbd03be33115 | -12.95 | -51.31 | 2024-10-01 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf2597d4-7d1f-39ca-bd18-8818ed5522e1 | -12.95 | -51.25 | 2024-10-01 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8cc2ba2-7b89-31d7-8f01-dd3b204ca3bb | -12.95 | -51.19 | 2024-10-01 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e35fe8c8-3989-347a-ab82-3359d2292d8f | -12.99 | -51.38 | 2024-10-01 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b462ac7e-0173-339c-8e83-5dedafbde4d5 | -12.98 | -51.32 | 2024-10-01 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a1b7de1-ae62-3ba1-8d54-cb4e9797d6b9 | -12.98 | -51.26 | 2024-10-01 02:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cb11224-4b65-334e-92bd-0823d01f9775 | -2.91 | -50.73 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af7b87cd-f4a1-3dae-8f22-e24e892fd407 | -2.82 | -50.78 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f00d52dc-5448-3a40-9a30-69c02bf51719 | -2.82 | -50.72 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce2c46b-f558-3249-ae3d-ed13812d1aa6 | -2.85 | -50.78 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa01ae30-e310-3a6d-8a0a-0d6dbe8e76b2 | -2.85 | -50.72 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d16fb07d-ff8d-3d7f-917f-495afeb87585 | -2.85 | -50.67 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f9af2c-6970-329e-8d5d-0346b2f5e317 | -2.88 | -50.78 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec428c9-0f2f-3c88-bc31-84278b97ea51 | -2.88 | -50.73 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5e71278-aa95-31f6-9dba-71135ee1664b | -2.88 | -50.67 | 2024-10-01 02:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee4eba6-f52c-3da1-90b0-67a55ccaf933 | -2.38 | -50.36 | 2024-10-01 02:05:14 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2116c2f9-cbf8-3218-8faf-389fa6889877 | -2.38 | -50.31 | 2024-10-01 02:05:14 | MSG-03 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README30.md)
