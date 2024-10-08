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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fc5f0be-8106-3a66-a339-abf71c02bc09 | -11.0991 | -54.0285 | 2024-10-08 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| d21a1c67-b4da-34b3-bf44-114bf57f72be | -11.0994 | -54.008 | 2024-10-08 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 2a815197-517f-37f4-9a26-35d1c66ba0b4 | -11.118 | -54.0268 | 2024-10-08 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 0f0332c7-b8a1-3a70-8254-60167c9cd8a9 | -11.1183 | -54.0062 | 2024-10-08 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 00edba00-0ee5-3f14-a189-77cdf1523436 | -11.1185 | -53.9857 | 2024-10-08 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e257a1fc-1295-3ef8-b7ee-1165dcea4356 | -11.1372 | -54.0045 | 2024-10-08 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6d8edf09-ec8c-30f2-b268-b38368d40e9f | -11.5233 | -65.137 | 2024-10-08 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 4abcf310-ef9d-3618-8613-6a4626d38d53 | -12.1585 | -47.7745 | 2024-10-08 00:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2d674b16-f234-3a51-9adc-71fbe6bd4927 | -12.1589 | -47.7522 | 2024-10-08 00:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 52933f0b-d2a3-3775-84fc-82fbe61b4fdd | -12.3616 | -47.0986 | 2024-10-08 00:46:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5ec96c34-bfca-339e-8e28-6b2bf4f28c8a | -15.6877 | -59.4145 | 2024-10-08 00:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 10454af7-d790-358e-9626-aa8039e0e029 | -16.5897 | -46.4979 | 2024-10-08 00:46:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 127.6 |
| c4fd8e9f-500a-36d1-9e4c-02b38d9c567c | -16.5902 | -46.4746 | 2024-10-08 00:46:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 133.8 |
| e72334bf-e766-3359-9a5a-5ccdb69caa6d | -16.4353 | -57.3393 | 2024-10-08 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.3 |
| e3505a0e-b869-3d13-bc26-d9e6b515ad9a | -16.5075 | -57.7183 | 2024-10-08 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 22b9f5d7-aabb-3f2d-af4a-1d60e106f869 | -16.6531 | -57.1305 | 2024-10-08 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.2 |
| 98dd842e-532c-3920-af1b-a3640c34468a | -16.9924 | -56.7003 | 2024-10-08 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 4aa49a98-01dc-3900-8df4-3a30889d8c14 | -16.9927 | -56.6797 | 2024-10-08 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 94582a4f-af3d-3cc5-9bcb-2f0b41baaf10 | -17.0123 | -56.6773 | 2024-10-08 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 565fd781-f995-3a23-966f-07f820766630 | -17.3353 | -55.0156 | 2024-10-08 00:46:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 980437f6-4f18-3ac2-b2b8-f1a01b88b0d0 | -17.1584 | -56.1429 | 2024-10-08 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.4 |
| 8ee784d9-2cc2-3886-a292-ade99432c55e | -17.1588 | -56.1222 | 2024-10-08 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 77a4037b-a769-3dd4-862a-b1a05b4cbc43 | -18.6192 | -57.2603 | 2024-10-08 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.2 |
| 60eefff7-6a31-3c34-aa48-9afba8ff9701 | -19.0045 | -50.2277 | 2024-10-08 00:46:52 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 256d4141-34f2-354f-8add-e60fae1f163d | -19.2723 | -46.1305 | 2024-10-08 00:46:53 | GOES-16 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c7ed802c-833f-345e-b0c4-2edfb4f2b0ce | -20.3724 | -43.9716 | 2024-10-08 00:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.3 |
| 6634e816-fd35-3dfd-961f-75b8c7bfe82b | -20.3732 | -43.9468 | 2024-10-08 00:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 230.1 |
| 359dabd3-fcd3-384a-9081-3d025b3f86c1 | -20.374 | -43.922 | 2024-10-08 00:46:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| e8334623-360f-3f31-9e8e-6d46777f527d | -20.3938 | -43.9412 | 2024-10-08 00:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 308.0 |
| 4dd95a42-a25c-3dae-b815-347ac729bdf3 | -20.3946 | -43.9163 | 2024-10-08 00:46:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 142.8 |
| d79014ee-fb85-3675-8953-e5238ca41c9a | -20.4144 | -43.9356 | 2024-10-08 00:46:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.8 |
| c67feef8-65e5-3b18-923f-273a8731497c | -20.4152 | -43.9107 | 2024-10-08 00:46:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 3f47d149-fe27-3b56-be59-cd8642295ba0 | -20.4251 | -47.6688 | 2024-10-08 00:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 31f09ac6-e97c-372d-be1c-b56df787cd4d | -20.4258 | -47.6453 | 2024-10-08 00:46:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 169.3 |
| b35dc40b-c14b-331a-be97-c907e22d6b9e | -20.4264 | -47.6218 | 2024-10-08 00:46:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9f80f6df-d727-32ad-900e-39544da9e2a0 | -20.4152 | -48.7589 | 2024-10-08 00:46:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d7919d8c-126e-391b-a92b-b2a9b1e059e5 | -20.4463 | -47.6405 | 2024-10-08 00:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 663b30a3-0d6c-3e4e-a18c-1edef70a86fc | -21.0712 | -47.2331 | 2024-10-08 00:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b76fdab8-dcc4-3446-8158-70c6a5eb013c | -23.9049 | -54.2392 | 2024-10-08 00:47:18 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 116.4 |
| 9fd3e925-090b-3814-9c9f-04975c856408 | -2.78 | -48.5806 | 2024-10-08 00:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9e23264b-47cf-3dc1-a594-ff94529c50dd | -2.7985 | -48.5801 | 2024-10-08 00:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| ae9cfcae-2a2e-3b8e-aeef-7ae29fe97e92 | -3.2862 | -47.133 | 2024-10-08 00:55:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a5ec7538-9f6e-3b00-9c54-0ebd1fa52f62 | -5.5716 | -44.8927 | 2024-10-08 00:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| cd2938de-f0c4-323b-8246-4cfc8802f2de | -5.5718 | -44.87 | 2024-10-08 00:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 3161dec0-68c9-33f3-8988-98a37b335c5a | -5.8216 | -44.1196 | 2024-10-08 00:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d1b8d4dc-2515-3880-b765-825dd5ad3243 | -6.4213 | -38.8347 | 2024-10-08 00:55:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 71.5 |
| e89d6869-a8a8-3feb-a3d0-f4e574711a6b | -9.3901 | -66.5444 | 2024-10-08 00:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5b220b64-fe5a-31fb-b137-4613558ff084 | -9.4086 | -66.5624 | 2024-10-08 00:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f5eb84bc-d8f3-3c3c-a651-bd1a3febc1a9 | -9.4087 | -66.5438 | 2024-10-08 00:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3b252340-5428-36c5-aa3f-c149171eeaef | -9.445 | -66.7289 | 2024-10-08 00:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 37bbccb7-03e1-3e50-bb9a-1fb248da1576 | -9.4635 | -66.7283 | 2024-10-08 00:56:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b35c04f3-e336-36a9-86f4-f9fb34df9c29 | -10.0653 | -45.2761 | 2024-10-08 00:56:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| fd00d552-12c6-3420-8b9d-c5bd35f598e2 | -10.0843 | -45.2737 | 2024-10-08 00:56:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| d4e35bfd-2946-3f5f-b2fd-f7b28dd76f5e | -10.1261 | -55.2093 | 2024-10-08 00:56:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8c77d588-05bc-32bd-8e17-a965148cecd1 | -10.1263 | -55.1891 | 2024-10-08 00:56:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 9a5fcd9e-5121-3ac7-ba73-9bd3ca6bac88 | -10.1451 | -55.1876 | 2024-10-08 00:56:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| d27f38a7-7c41-306a-bf2d-1488d95e8ea5 | -10.6256 | -55.9154 | 2024-10-08 00:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 776d43b0-0ef2-3fdc-b16a-09ac3a55d2a1 | -10.8754 | -63.9169 | 2024-10-08 00:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 65cae81f-cc24-3d09-9681-7c35a166e140 | -10.8755 | -63.8979 | 2024-10-08 00:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1a9a9e8a-a11a-3920-ac19-bea319ecb310 | -11.2479 | -51.3071 | 2024-10-08 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f6ae70fd-a3bd-3ad3-ba56-347886af81e5 | -11.2482 | -51.2859 | 2024-10-08 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 371f1cfc-b0ad-306c-9bca-15c2a0aad07a | -11.3043 | -51.3434 | 2024-10-08 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5f7c9efd-fdca-3008-8509-2f32cbaca0fc | -11.5233 | -65.137 | 2024-10-08 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.5 |
| ef24cdcb-d3a3-382d-979b-7e460ac930c5 | -12.3616 | -47.0986 | 2024-10-08 00:56:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a073ccea-a33f-3a2d-a46a-a3914bdfe9db | -12.8242 | -62.4573 | 2024-10-08 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| dc565521-84a8-3045-8cc5-85baf93192a4 | -16.5897 | -46.4979 | 2024-10-08 00:56:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 157.2 |
| dae1da19-f2ed-3f66-9da0-297b9293ffd7 | -16.5902 | -46.4746 | 2024-10-08 00:56:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 6478762c-b834-3be5-9101-580e14247956 | -16.6101 | -46.4707 | 2024-10-08 00:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2f6487db-6308-3748-8d04-9791800f3ea7 | -16.4353 | -57.3393 | 2024-10-08 00:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 61495704-33bb-3b58-bdab-84d80cb026ba | -16.9924 | -56.7003 | 2024-10-08 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.4 |
| 9e26dccb-d30a-34ba-a5bb-dfc788f5c72a | -16.9927 | -56.6797 | 2024-10-08 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| 82680944-dcef-307f-9ddf-47c8172ce906 | -17.0123 | -56.6773 | 2024-10-08 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| fc595fbf-2f24-3bb2-953b-8a184e4b377b | -17.1274 | -56.828 | 2024-10-08 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| cff455ff-181c-3c1f-84a2-14e97a1b8a42 | -17.1588 | -56.1222 | 2024-10-08 00:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 73f79555-a5f0-337f-80d2-f1331167e412 | -17.3353 | -55.0156 | 2024-10-08 00:56:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 41.2 |
| cfa644ea-c92f-3287-98cf-97420203a7db | -18.6192 | -57.2603 | 2024-10-08 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.4 |
| a15d5740-e40a-3289-8cc0-6b49bd8c6e7a | -18.6195 | -57.2396 | 2024-10-08 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 5a53bb03-d29c-3574-948d-8c2508f2724b | -19.0039 | -50.2502 | 2024-10-08 00:56:52 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 4d656ab6-bdaf-3208-b07a-4a9c6b071bc7 | -19.0045 | -50.2277 | 2024-10-08 00:56:52 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 121.1 |
| f5564d1d-4e5b-3f7e-989d-a1adba940c25 | -20.3724 | -43.9716 | 2024-10-08 00:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 5503690d-cc58-33fb-bb90-e00863360766 | -20.3732 | -43.9468 | 2024-10-08 00:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 212.3 |
| 45c4721d-8286-3a9e-afd4-f9891098c7f4 | -20.374 | -43.922 | 2024-10-08 00:56:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.3 |
| e400feef-178b-3ea4-bbda-5e6536d7c390 | -20.3938 | -43.9412 | 2024-10-08 00:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 232.4 |
| cc96ac83-7012-3d29-8705-e934fbd27d1f | -20.3946 | -43.9163 | 2024-10-08 00:56:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.4 |
| e6c409c1-8b3b-3be3-af0e-058bf16a7aab | -20.4251 | -47.6688 | 2024-10-08 00:56:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 954f9019-e5da-3952-a94a-b6090c9cce71 | -20.4258 | -47.6453 | 2024-10-08 00:56:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 1dc104a6-86af-3e5c-a6ca-26cfb7cfbac4 | -21.0712 | -47.2331 | 2024-10-08 00:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d72dac64-a9fe-35c8-92b5-732c08fdb5e4 | -23.451599 | -47.270802 | 2024-10-08 00:57:15 | METOP-C | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16335247-cfcd-367c-87c9-56d2020ef862 | -22.910101 | -47.386501 | 2024-10-08 00:57:24 | METOP-C | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e17524a-f13c-35e8-a6a3-6f1eb76d24eb | -22.8078 | -46.749699 | 2024-10-08 00:57:24 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7da89f6-73cc-3c02-982c-dfa88c0306b9 | -22.809601 | -46.757301 | 2024-10-08 00:57:24 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fdc1f1f0-bb62-3f5c-a495-3908aacdf6bf | -22.7981 | -46.752201 | 2024-10-08 00:57:24 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93fbf2f5-51e8-3461-85f0-128f0704541c | -22.7999 | -46.7598 | 2024-10-08 00:57:24 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 826bc30f-0235-3724-b1ba-54348db1b061 | -24.244101 | -54.244801 | 2024-10-08 00:57:25 | METOP-C | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e7ef486-a5c2-38a7-bb9a-e5df1c13bc41 | -24.2465 | -54.258099 | 2024-10-08 00:57:25 | METOP-C | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea0c9678-0329-37bf-807d-40700a170895 | -22.579599 | -46.655102 | 2024-10-08 00:57:27 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e022a962-96da-39c2-896d-4a83d925a7da | -22.5814 | -46.6628 | 2024-10-08 00:57:27 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb889ea7-57d2-3926-b982-b2dd82493f1e | -22.575199 | -46.680698 | 2024-10-08 00:57:27 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95a48e8d-ce1e-3d0d-a6e3-bddf545c0e30 | -22.577 | -46.6884 | 2024-10-08 00:57:27 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f847106-dbee-38f7-8b8d-00ab943caad9 | -22.414 | -46.608799 | 2024-10-08 00:57:29 | METOP-C | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README14.md)
