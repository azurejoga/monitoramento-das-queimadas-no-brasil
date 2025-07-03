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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08af65f0-caca-323e-bd19-40489a8ec7bf | -17.65491 | -46.83187 | 2025-07-03 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0a78f29-028f-3f09-8312-bcfde199e185 | -18.20766 | -51.35558 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bba18ce0-5b1e-3b56-b3aa-8842cff7c68a | -21.61109 | -57.57243 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7101219-6023-3d57-a05a-62fe74051a6e | -18.21885 | -51.35005 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a178147-f4ba-30a6-ba13-a74823864c0e | -21.68899 | -49.50063 | 2025-07-03 04:38:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ed7958a4-58ae-3a28-ba45-db12baeda6eb | -20.72229 | -56.6577 | 2025-07-03 04:38:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 391ecbc9-96f8-399a-bd10-1bbbfff78b85 | -19.37567 | -47.68741 | 2025-07-03 04:38:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c368fda7-c58a-353b-be20-223e323f4cb4 | -18.49418 | -51.65577 | 2025-07-03 04:38:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4740e43-7669-314e-83dd-258520af9f65 | -21.61606 | -57.56933 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0884fee-146b-32e9-85e3-c03685d9240e | -20.25888 | -44.4984 | 2025-07-03 04:38:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e16b6073-a5ed-38b8-ab46-04f554c83ddd | -21.61655 | -57.56382 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 763127dd-42c7-3dfc-962f-431847013017 | -21.95622 | -57.58523 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0997d35-7b32-3d4f-92f6-051c5204612e | -16.29389 | -49.94577 | 2025-07-03 04:38:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1806fc1e-f0b6-3196-be51-709150d1a91a | -20.76243 | -46.76903 | 2025-07-03 04:38:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 279d5b6f-3b5b-3c05-865b-6014628dca24 | -21.88627 | -56.11129 | 2025-07-03 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3d135ef-4854-357e-aa66-03badfe6f16d | -18.65657 | -55.74673 | 2025-07-03 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 9e73dc82-3ce7-37ca-85e3-bda2f6cfe3fe | -21.68772 | -49.50329 | 2025-07-03 04:38:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b6b99bbb-f571-3ce2-8e18-6f167633fcd9 | -21.61573 | -57.56795 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1dd7fae-2141-3385-ac5e-3d866f3152d6 | -18.0587 | -44.49419 | 2025-07-03 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51db2812-9f0b-3474-901e-8e0023e7cdc8 | -21.88846 | -56.11514 | 2025-07-03 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0567c3e-4145-3757-aeda-b1fb673e93e9 | -20.54403 | -48.75208 | 2025-07-03 04:38:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0c8309e5-ccd7-3389-8961-018f94d3b105 | -18.20825 | -51.35192 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f9afc51-ca01-311f-b24b-843e24f6c79a | -18.42982 | -54.55667 | 2025-07-03 04:38:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a58884ff-106d-3600-82ee-af14535aa1f0 | -20.723 | -56.65403 | 2025-07-03 04:38:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| aa14a09d-3879-329f-a0ad-0ab78076ca21 | -19.44008 | -48.55202 | 2025-07-03 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee28f3a3-6253-39ea-87ab-fc3911a6d05e | -21.61686 | -57.56517 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ab75a3a-7412-35c2-95c3-22ae3814fa23 | -17.90812 | -54.13898 | 2025-07-03 04:38:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 104ca789-24d9-3941-9ebe-89ff1b68c24e | -16.29333 | -49.94937 | 2025-07-03 04:38:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c49a2028-777f-3bd6-9323-989060cff297 | -18.20884 | -51.34826 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d356f163-9290-3937-93e1-948f419e2f30 | -17.65617 | -46.83421 | 2025-07-03 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62a3a53f-eb02-3cd0-8e53-5a4798d62906 | -18.65261 | -55.74592 | 2025-07-03 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5f33e430-ae83-3ecc-89ae-708c9e6f70c6 | -18.2161 | -51.34579 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b475ef25-862d-3f2a-9859-9107a26bca47 | -20.72776 | -56.65109 | 2025-07-03 04:38:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccd8586d-8099-3521-abc3-2a7d47eeb32d | -18.42899 | -54.56133 | 2025-07-03 04:38:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d2eb1f1-69e6-34ad-878e-d8504d4879b0 | -18.29096 | -44.68302 | 2025-07-03 04:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13e094eb-7cdf-308e-9e7a-4d4a4fb22182 | -21.68555 | -49.50005 | 2025-07-03 04:38:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bf2b2e27-6650-3a6f-9fdd-4f1f72cecedf | -16.57972 | -43.64548 | 2025-07-03 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ca923a5-4f13-3c4d-9a83-346871eee758 | -21.6124 | -57.56266 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6fa0bfb-73ac-339d-be4d-8e0b614bc047 | -17.85996 | -44.56971 | 2025-07-03 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee89897e-6ae8-3b73-8760-cf18ad93b4af | -21.61765 | -57.56105 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b3d4792-19d9-3d7b-a763-569758ebb72e | -19.36152 | -44.30441 | 2025-07-03 04:38:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f2f5da1-4b34-311e-9e24-c5b52baa2f24 | -17.65309 | -46.8291 | 2025-07-03 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f002400-fec7-3a7c-94e4-8038fec9ec1d | -18.65756 | -55.74138 | 2025-07-03 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 1925caab-a48d-3a17-b1c4-1a4ecf4d6d45 | -18.21218 | -51.34886 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fac98b70-7e86-3f30-8d05-365e58d1a302 | -21.70368 | -57.67992 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47da672b-f23b-33fe-aa0c-2dd95e0e697c | -19.46945 | -44.29797 | 2025-07-03 04:38:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78383c7a-547c-3c7a-9a4e-a5406952dae6 | -22.52806 | -47.38419 | 2025-07-03 04:38:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2781910-246f-3453-b2fd-fdea8fbcd641 | -20.0531 | -44.28188 | 2025-07-03 04:38:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6704170a-d838-3f29-94be-baa10112da14 | -18.37221 | -49.26981 | 2025-07-03 04:38:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90e240af-6c23-3b6f-b323-c0ceb1f26278 | -17.66397 | -42.26999 | 2025-07-03 04:38:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 893c537a-a05d-3e38-9ed0-0aa91ca20d73 | -18.21944 | -51.34639 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63da1987-10e3-35b7-be19-0dccda90066a | -18.21551 | -51.34945 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51508c1d-35e1-3c81-88e9-e2a58e02eeca | -18.61414 | -44.26462 | 2025-07-03 04:38:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db154242-b9d1-388d-b3dd-e7bed430337f | -20.31046 | -45.58383 | 2025-07-03 04:38:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43d4f821-e6bf-3d41-b9b0-36ea4615d319 | -20.99501 | -51.79237 | 2025-07-03 04:38:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| efab8ad1-e71d-33e8-b273-f02b191da139 | -20.54053 | -48.75151 | 2025-07-03 04:38:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3d113283-3d98-3c7d-8c17-409dc4a8b8eb | -21.61073 | -57.57105 | 2025-07-03 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b2e6da0-3b7d-34c0-9a59-002d85f87293 | -22.53187 | -47.38477 | 2025-07-03 04:38:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16189439-da68-36cb-9f4e-f595a39c68b7 | -19.37206 | -47.68682 | 2025-07-03 04:38:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19fb92da-d479-389a-bd07-6142f8d1eaf3 | -18.21826 | -51.35371 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80f709b2-0b3f-3308-b6ef-bfd76026685c | -20.72706 | -56.65475 | 2025-07-03 04:38:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d1166dc2-d3f8-34d0-a43c-96e07e57eb84 | -19.43659 | -48.55149 | 2025-07-03 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a9a8e46-0ec6-3936-ab18-6e215a74e560 | -16.07611 | -51.56498 | 2025-07-03 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a022a78e-4524-3e2d-93f8-a8a10c87f5cc | -18.21433 | -51.35677 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31bc2486-ef6b-3741-84a1-9080f858af28 | -17.77902 | -42.80975 | 2025-07-03 04:38:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d8af41e-6152-38cc-80a1-a5bd59e52e88 | -16.07273 | -51.5644 | 2025-07-03 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99cea3cd-c07b-33b3-a1c5-de3edaecbcbc | -21.68829 | -49.49932 | 2025-07-03 04:38:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| faa5e456-4264-3f97-8f2c-952752152130 | -16.09045 | -46.75625 | 2025-07-03 04:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e581d44b-f7e2-3878-b5c9-e8ce73a78fa3 | -19.37506 | -47.69184 | 2025-07-03 04:38:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd01a6f7-93e7-3202-9c72-8862ee0a40ee | -17.65121 | -46.83131 | 2025-07-03 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04f31728-f4dd-358c-ae08-71e420691870 | -19.35709 | -44.30396 | 2025-07-03 04:38:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1b3a309-0e8f-3646-899e-32c82bdb8f13 | -16.29722 | -49.94633 | 2025-07-03 04:38:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 686c17cb-ee9a-3183-8eef-d73b00893f77 | -18.40857 | -55.59152 | 2025-07-03 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2fa87017-88f9-3964-a217-8b5ffed963b4 | -18.40639 | -55.59207 | 2025-07-03 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cbaec81d-9651-3229-9bcf-cc28cdcecf30 | -18.21159 | -51.35252 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3179607a-e2d4-38b1-ad45-3f6747e98283 | -17.65679 | -46.82967 | 2025-07-03 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a000234-301d-3fd7-8645-94fdddb7171f | -18.21492 | -51.35312 | 2025-07-03 04:38:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12eb02a1-1fa5-308b-880f-6fa0935e1308 | -6.2945 | -43.6659 | 2025-07-03 04:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 3ae3f010-0b37-3085-9f07-da61bd3e9e10 | -5.9938 | -43.7366 | 2025-07-03 04:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f85d7086-ba50-34ad-adec-b1990878add1 | -7.2219 | -43.0682 | 2025-07-03 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 82eb0791-c42e-3a23-8d31-05338d6ae5bf | -6.9793 | -42.8798 | 2025-07-03 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 54b456ae-f8e9-387b-bdd2-63a17648a4f1 | -6.9416 | -42.8834 | 2025-07-03 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 62dcfd8e-c669-3665-9ef4-90634e6febad | -11.6588 | -44.5974 | 2025-07-03 04:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7fa0126f-3e58-38d2-a5eb-2a07e16c14fa | -6.9602 | -42.9052 | 2025-07-03 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.3 |
| e9683f98-4959-319b-9eda-7958c9654c34 | -6.9605 | -42.8816 | 2025-07-03 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 327.4 |
| 2a1eca0e-15f7-3f43-b063-0969a800397d | -27.32382 | -48.5872 | 2025-07-03 04:40:00 | NPP-375D | GOVERNADOR CELSO RAMOS | SANTA CATARINA | Brasil | 4206009 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6497fe15-6cad-365f-a878-c627cac1362b | -11.6588 | -44.5974 | 2025-07-03 04:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 266b4f5b-aaaf-3958-b8cb-a61cd5122383 | -7.2219 | -43.0682 | 2025-07-03 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| af522309-339d-3c7c-997b-a84e55880743 | -6.9602 | -42.9052 | 2025-07-03 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 8b88460a-eaa8-368d-bd12-ef90a7169bce | -6.9416 | -42.8834 | 2025-07-03 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 6c52bb47-8411-3491-a360-8da91ce9ec51 | -6.9793 | -42.8798 | 2025-07-03 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 87929d72-f9ba-3e07-b7ec-84c2a72c49c3 | -5.9938 | -43.7366 | 2025-07-03 04:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| eb10f2dd-b645-3afb-a205-3d10125ff2fb | -6.9605 | -42.8816 | 2025-07-03 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 282.9 |
| 91d4aabf-46a7-399c-9b46-ba3f7606ae8f | -6.9607 | -42.858 | 2025-07-03 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 16445ad9-93d1-39fb-8425-ab8734d3c43f | -7.22575 | -43.05533 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d124047a-cd51-3602-a8bc-b3a40e832425 | -3.51415 | -47.22024 | 2025-07-03 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03a00abd-00ac-3d57-b3a5-453ce69bc39a | -5.72149 | -49.10861 | 2025-07-03 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc79ef47-c112-3cca-adc9-7425ea070451 | -6.20859 | -43.36369 | 2025-07-03 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61e60190-4c7a-313d-917d-00306139c563 | -4.32265 | -48.08059 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22c789ba-76a6-3da7-9476-22108b798a5c | -2.91526 | -48.2395 | 2025-07-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README19.md)
