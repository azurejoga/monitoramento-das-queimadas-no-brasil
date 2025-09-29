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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45bbdcc-0c77-3ae8-92ae-b91b0987303a | -25.0604 | -49.35817 | 2025-09-29 03:49:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2e3b4e47-29cf-3984-96b5-a1336aab4d33 | -14.5429 | -48.41076 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edbb900e-8615-3c78-9223-c11aee9f2b54 | -13.4049 | -48.15611 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d95497f6-c763-313c-807b-4752bfda87a1 | -21.13609 | -45.10811 | 2025-09-29 03:49:00 | NPP-375D | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3ad97f25-e539-38e8-8761-6b45303964dc | -20.56556 | -41.93987 | 2025-09-29 03:49:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f713fbc9-eae8-3dd3-833e-59581fefeeb0 | -19.67735 | -43.77012 | 2025-09-29 03:49:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6d2e10d-eb81-39f9-8f76-a03dc2d2ca86 | -15.16106 | -46.41351 | 2025-09-29 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ea88f3a-a29e-3efc-9dac-9cc201a63f0d | -12.85061 | -46.97168 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3d38344-2870-3b5a-853f-bbda1b52b157 | -13.78231 | -47.86527 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cb91119-34fe-355f-90dc-ea46b252e9c9 | -13.35914 | -47.30048 | 2025-09-29 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a09c051b-c978-34f0-8165-dc2cf30c8ea3 | -15.15639 | -46.40967 | 2025-09-29 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21f1372-0e0c-374f-89f5-56bca56ed002 | -13.35901 | -47.30476 | 2025-09-29 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 966b1732-c528-342e-a887-8485546481a8 | -13.7771 | -47.86089 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90e7af97-52b8-3276-bb73-6b139c964e3e | -12.79622 | -47.75386 | 2025-09-29 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c52b6c05-47fc-3337-b9a0-0ee712c3b8b8 | -12.76321 | -46.86723 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3bd763b3-4376-3a32-8a30-c46b831562d8 | -12.84989 | -46.97531 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 519c6e67-4231-3241-878a-6ba4fdaf4ef7 | -13.79304 | -47.87259 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50d2db07-294e-31a5-a9e4-b796929db2dc | -23.75108 | -51.78291 | 2025-09-29 03:49:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 61e00553-feff-333c-883b-9059f35ee851 | -13.49297 | -47.40923 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1878cc29-7bb6-37ea-affe-9f5a0458071c | -12.869 | -46.96777 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36d18949-d90a-338d-84af-638665136672 | -13.38411 | -48.15998 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e2208da6-e93b-34fb-bb37-2877d004ab51 | -12.98364 | -46.26352 | 2025-09-29 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8951c089-9de9-375d-bf59-1b0e9097e3bf | -12.79797 | -47.74514 | 2025-09-29 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1496af54-c785-3996-90c7-deca0b0fba38 | -23.42205 | -49.46258 | 2025-09-29 03:49:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 81348bd5-4f5e-3a76-a829-e3ce70d62c57 | -14.58886 | -45.01505 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1cbe7cea-1610-36ae-891b-7b25a0134643 | -15.58629 | -41.80872 | 2025-09-29 03:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 739d90db-4dbc-3c6d-9a92-cf01f39f664e | -13.39108 | -48.15652 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3191671f-fbe0-35e6-8d0e-de4263c41863 | -21.42181 | -43.77097 | 2025-09-29 03:49:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a4e7ddf7-5836-3a4b-b217-c773f428b51b | -20.54413 | -45.10279 | 2025-09-29 03:49:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 15bee977-ea05-3958-8294-0e0d3e57eb8d | -14.53536 | -48.44246 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ad60168-f220-300d-8488-4e1a4c0d7928 | -15.03431 | -46.97719 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97065717-4372-310b-848e-df044ab8af56 | -13.79829 | -47.90646 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed310800-9ccf-31ea-93f0-a887c25a95b3 | -13.7923 | -47.87617 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37b88a1a-decd-30d4-9c4a-8270d7d642ba | -13.63313 | -47.33843 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bde44640-fd5d-36fa-92ca-22266ee87b61 | -15.04721 | -46.97051 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a00e6200-2b30-3c2d-9d07-c11ee64227db | -15.39164 | -39.37098 | 2025-09-29 03:49:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bc629334-30e9-3994-bbe1-0ac9e31f5ab6 | -21.33406 | -44.48983 | 2025-09-29 03:49:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aba64d5c-099e-3024-948e-817a7b141bb4 | -13.38593 | -48.15099 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 588a0dc3-24bd-3009-b471-46c9c110bde6 | -23.22328 | -49.40276 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c596dfef-2268-3d4a-8d2b-70a0c2248754 | -13.55583 | -47.27374 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b99aa76-30cb-33d9-83ce-92438e0ebb62 | -20.44095 | -43.22915 | 2025-09-29 03:49:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11dcc49b-c1a4-3983-8421-0d9fdbd6bb9b | -13.0114 | -49.45751 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca8f8159-635f-33a3-8237-86fb1e1d7239 | -14.5709 | -48.27811 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 726204af-7ad1-34ce-9c8c-9e01481e7a5b | -13.80102 | -47.95285 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48483cf2-a566-340f-90cc-2883f29a2b11 | -14.53101 | -48.43739 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b77223d-a08c-3b87-88b3-7ea057d8f3b1 | -15.16559 | -46.41802 | 2025-09-29 03:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2c4c577-78c2-3151-915e-8bfce2166e33 | -12.80304 | -47.75067 | 2025-09-29 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b72ca20e-ffe1-3ec7-876d-ae830a2b47e5 | -14.56505 | -48.27641 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbf7ad57-7bfb-3192-8ddd-994d8217307c | -22.02817 | -46.49046 | 2025-09-29 03:49:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f8b4f289-2c87-3dd3-97a1-6f8ee75c8af4 | -14.54397 | -48.43532 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e9ff85c-b37a-3013-a4db-c9219bde40ff | -13.78448 | -47.86787 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11159ec4-9369-3775-aaf2-897df9301d99 | -19.82385 | -44.6375 | 2025-09-29 03:49:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc03a1fb-5ccb-3c23-8fe6-31a79613c424 | -14.54292 | -48.4403 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bcb3a506-71cb-3a42-9ebd-079a3562efe3 | -13.39176 | -48.15886 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7b55ae93-3619-33ff-a7a3-69453b9969fa | -12.86491 | -46.96727 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c3ab05c1-02fb-3776-91a0-4d67139adf98 | -12.84917 | -46.97895 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 708d12f0-bba7-3071-a46c-0d333310dce9 | -14.56966 | -48.24389 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a06e59ce-83b5-37dd-8708-fb8a52641ccf | -12.75817 | -46.86315 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f057b1d9-cf12-3f91-9c04-f5dd6c690027 | -13.49368 | -47.40573 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bb01445-a148-3546-b20a-60eebf7b1d86 | -13.23331 | -50.95606 | 2025-09-29 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe65c9aa-09a9-3c51-98f6-5a96c87e020b | -12.98296 | -46.26701 | 2025-09-29 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a4f80c4-393e-39dc-bd4a-1bf3a0b9ebbf | -15.04106 | -46.97288 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8795b937-9553-3e0e-842c-5daf5fc15938 | -14.43892 | -44.87632 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92e813d0-ecc4-38e5-a5b3-370389174242 | -13.38568 | -48.15791 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e9557f2a-a7f6-3ae2-a64f-33401f1df389 | -14.56471 | -48.24872 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60ff1a85-e9b8-39f4-9ffb-5667aceb86a1 | -13.57266 | -47.30846 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6baa5311-a71a-3efb-b2d1-360297b1d452 | -15.0632 | -45.05884 | 2025-09-29 03:49:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c9f90a3-56e5-3e9a-8f48-96e57633ab5e | -23.22874 | -49.40368 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7b90758a-bea3-367d-99f0-eeaf82894e17 | -13.00216 | -49.43624 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0b27ff8-1d47-3af6-b7b8-d551a18bb34b | -15.05875 | -42.34186 | 2025-09-29 03:49:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 833b1d5d-91cc-36ea-ad7b-e4d2cdf8568f | -13.83552 | -47.4927 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e635e225-0c2d-3478-8251-eb74e6f0a165 | -13.64584 | -48.06358 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36559110-e2b3-3ec4-b5ea-16a42940e5c2 | -21.55636 | -41.25255 | 2025-09-29 03:49:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3edc7c5b-25e9-3152-a229-6fb494ce4fc1 | -13.78173 | -47.86806 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1e023b89-4619-36fd-90a4-19826c2f5932 | -12.75963 | -46.85578 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57988129-f616-3368-8869-6f1436ae133d | -14.52592 | -48.39695 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 112adea6-59c4-3591-bbbf-9b98feaeffac | -13.2726 | -48.45709 | 2025-09-29 03:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99faf386-c9d6-343a-951d-79968b25ec87 | -14.53736 | -48.43261 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e8d4ac7c-1bee-3f54-9106-aec6466a0ae6 | -23.75226 | -51.77808 | 2025-09-29 03:49:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b1a1c0cc-25ea-3968-982e-e7fe3f8c4d46 | -12.88257 | -46.98856 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d1c03ac-fade-3a70-89e1-c316dc1891d7 | -13.57527 | -47.30187 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e255e9cc-4bba-3652-a964-afff56d0f54f | -13.79605 | -47.94711 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3849403-f2db-3817-a441-a4491d53ef25 | -14.08855 | -44.0938 | 2025-09-29 03:49:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdc6a9f9-17d1-3687-92a1-a82075c5ac39 | -13.58324 | -47.29185 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed48c0fc-71a2-3c9c-be7c-58019d318fea | -23.21985 | -49.41789 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| aa1ed9c8-9264-3d67-bb26-9bbad3a870da | -13.61451 | -47.31296 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 445dcaeb-6f55-3621-802c-c8f9f3461e3a | -12.90156 | -47.10733 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d7cb38fc-c9f4-32a4-87f7-a13da9c82031 | -13.58963 | -47.2896 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04128649-d30b-33ab-80c6-04e64de5984e | -14.54889 | -48.41201 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72e0d829-a151-33b6-bdab-9e7e421fadf8 | -13.82677 | -47.4768 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8fb7df5-c03a-33f0-90d4-76e500aec600 | -14.52669 | -48.39874 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0ef6ff0-7be6-3a27-8b6e-3db3403187f4 | -15.05473 | -42.3411 | 2025-09-29 03:49:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 08af57ec-ddde-3164-8fc0-10171ce88882 | -14.52786 | -48.42267 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50ddd571-2d6b-3634-81ec-d08995500346 | -13.55818 | -47.26966 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe77c92e-2a3a-3877-96b9-76cc78e6686c | -14.58003 | -48.23478 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acc77f84-a54c-3fa8-b1e6-85047dd26644 | -13.62158 | -47.3368 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9905bf3-d9ac-3e1f-a526-529f0d3308b2 | -15.03507 | -46.97337 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 831dc927-e1d2-3e3e-b6be-44574f9d7519 | -13.18598 | -47.45132 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b74810ff-002a-3cec-a740-cb1d29b1fbca | -13.02592 | -49.44214 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 55b7fb17-52a1-319a-9c03-3849db43f558 | -14.57723 | -48.23708 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README23.md)
