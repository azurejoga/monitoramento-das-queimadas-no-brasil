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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6aa2aaa-5179-3ae0-9f54-e72ece5d033c | -15.00607 | -50.04716 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccbf5228-4659-36d9-896c-912665caa834 | -12.91661 | -57.00635 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31d192c1-d637-380b-b43c-4955fe8e61dc | -12.97803 | -54.78719 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83e6cd3f-b46c-3da3-b792-31c36c649be7 | -16.30522 | -45.70405 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed8f18d9-6d11-3e22-9e14-a1cddcc2a9e3 | -13.30338 | -51.78661 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5458955-55c9-35ed-814e-0dcf64f68bd2 | -11.21039 | -55.08547 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5835a147-b5a8-30aa-8ede-eb5f24c058c7 | -14.28633 | -45.2254 | 2025-09-04 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec7edc4b-3f19-3453-9b60-3db9b2324d47 | -15.16414 | -52.39231 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a6e8f5c-51c5-30d3-912a-60e4d4175723 | -15.30124 | -52.74134 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bdc9919-fa64-395e-b492-c524e07ba0fa | -14.55379 | -48.05255 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f96b533e-757c-3b85-88ab-ef888c982aed | -12.96812 | -54.7635 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c05f37-3874-3936-975b-0b7479e7c842 | -10.88954 | -55.74093 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5faf4d8c-fb07-3713-9d1c-d8fc86e47176 | -15.54963 | -48.37963 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6ef04d2-e9dd-3ff9-9952-12c4f3b05d5b | -13.44245 | -46.9386 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88e1b9a6-efd6-30ed-915b-9a684cf0be92 | -13.57126 | -48.1242 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2fe6403-e056-3c9f-a115-9d81fd5559e4 | -12.48436 | -48.07646 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f47a38d0-257b-3fa3-affd-54dcd0bf83b5 | -12.24566 | -50.14328 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22bcfd79-7ad0-3369-b676-ed4d5ebbc46b | -11.86094 | -51.52446 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29b8553b-138e-306e-8d50-275e3643b916 | -13.95452 | -53.98346 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f30be762-3ea3-3443-926d-d24752fbe1fd | -14.59247 | -48.02339 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc22f38b-f9e4-3ce5-bfda-3900de7130ab | -15.18082 | -52.35107 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8887f34f-066c-3a1c-8631-16ab116683a8 | -11.58314 | -52.12217 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e112636-7dc2-37fc-a1e3-67f72292593c | -11.67329 | -57.34255 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 780032c5-b472-3866-a1cc-8efa2b38888f | -12.91248 | -56.99802 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee8835fb-2e0b-32cf-b2b9-aa0044dfe1e5 | -13.74593 | -46.94263 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a96aca03-05be-3eb4-9e51-d2fe60debe18 | -13.44204 | -46.92724 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 419ef23c-6dfd-3d6d-80e1-597c55d33971 | -10.4844 | -53.64593 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fba15e5a-1569-34fd-be27-503e6f25df2e | -14.58402 | -53.01562 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ef080f1-8025-3758-93fe-62f45b925a3b | -15.04816 | -50.05849 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bf3d774-8415-30ca-ace2-dfea66549758 | -13.74122 | -46.94217 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe544e19-90ca-3d43-b952-476fbc63c0ff | -14.54509 | -48.05059 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48f2dab9-d8b4-31dc-bc4f-414648f53f58 | -12.1809 | -53.89183 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6d5d4fe-91ac-334a-85e1-3f8d1171d201 | -15.16983 | -52.35334 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 811b0cab-916f-35d5-817c-f21921e2a946 | -14.56476 | -48.03726 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a84a38d8-9555-3574-8254-94cf6206eb8a | -11.61721 | -47.77601 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acae2ae4-ce13-3c13-b64b-8fca13016bce | -13.58419 | -48.12608 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 944abe6b-2db7-3a6a-8c40-fe06dad9812e | -13.10775 | -57.11391 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95aef5d8-bbdc-39ce-97cb-31c1093ed1cf | -17.15898 | -46.22179 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a58e99b-361f-3d1e-8a6a-3776ad054421 | -12.49346 | -48.07345 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb067d86-d0b5-38cf-9432-c2a9d0eef57b | -15.57378 | -50.31979 | 2025-09-04 04:55:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2597fda-8117-38a5-8791-376a4e9335e1 | -16.46492 | -49.51211 | 2025-09-04 04:55:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f8b5bab-a423-3192-81bb-def1e52b736e | -16.30585 | -52.96328 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f70dd7a1-ccff-3134-9362-ea990afec122 | -11.19905 | -55.02714 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c65898b-6c14-3276-b4fb-5931f8d39aa9 | -10.52924 | -57.78061 | 2025-09-04 04:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e54282ee-48c0-38bc-95e2-e139253457e2 | -12.97975 | -54.77646 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4322d59d-cce3-394e-a157-91478dd70a64 | -16.54235 | -55.09801 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 853de292-0e92-3df4-a2b6-ef9346a088d2 | -12.86831 | -48.01725 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8c27fd9-7f4e-3708-8a38-c972d799993d | -11.58831 | -47.76334 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49592f33-7708-3cbf-9a96-1e4d58f29ffb | -12.91733 | -57.00218 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 306952b8-af4d-36aa-874c-9962de309661 | -12.23687 | -50.15119 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e4668ef-fe46-3422-ad21-8e31b052aaf2 | -15.24482 | -53.79853 | 2025-09-04 04:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8865a08a-8bbc-3c99-a04b-15b59293c499 | -12.89081 | -56.9515 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f7ef2bf4-ca99-3f9c-9feb-f3dba1ee053e | -12.97146 | -54.76406 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358984b2-450d-39c1-a5cf-249d44d74110 | -10.98505 | -49.76406 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 495e1fa7-4705-3439-acda-16d4114f21a7 | -15.54963 | -48.41414 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d13a0cf-53da-3846-91d3-2630fc324ba9 | -11.59734 | -52.14333 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f55bb0d-616e-37e9-878a-04e3628a98b1 | -14.77945 | -48.16601 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12965f84-e7fc-3d8b-a8f3-2681d5246eac | -15.73321 | -53.64441 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc698963-63f0-38c9-9639-e6f6bce8c23f | -15.14286 | -52.33377 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c1c2d58-52a7-3a27-9a19-649a826c9200 | -11.8799 | -50.60645 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 755a7e92-fb31-34dd-a3f1-a26ad8e8dc81 | -15.01979 | -50.03399 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9980c608-f175-3523-9d20-cc012b213b2c | -13.56586 | -48.13168 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9f3e45c-f7cc-332c-ad6a-a2b619e80ca2 | -14.60032 | -54.59018 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c32e1c84-8407-36c4-9b83-f813e920aeea | -14.59318 | -48.02583 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b637129e-8948-3f0f-b845-9ef46ca64fd8 | -11.85043 | -51.4507 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9bf2250-7b28-3ea1-923a-8928959519f1 | -12.90292 | -56.94506 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f69a4b67-81e5-3151-97f9-9555e5688780 | -11.5344 | -54.48721 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aaa45b16-23ea-3605-9752-c4d5ab55688d | -11.62149 | -47.77668 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c52f8a0-cf34-3019-b1ff-981017877a51 | -15.59538 | -52.89494 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dacd42f8-793f-339b-9236-23d295442d4f | -11.59168 | -52.1576 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51c95607-e00e-36e5-bf6c-40a92767e32e | -10.4578 | -53.62003 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 004294ed-5b50-34d0-bb9b-3fe93da95a00 | -16.53465 | -55.08188 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5faee973-4083-3701-8178-bf7f8e3bf6dc | -13.56963 | -48.13631 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aef25a8c-335c-36f5-b29c-852b33ed02cc | -17.97216 | -47.12267 | 2025-09-04 04:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b12f7c57-fb6a-32a9-9b0f-5d910b751c03 | -14.58177 | -53.03039 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e9375c9-4ceb-3dae-8b2d-bac11dcabb8b | -16.85364 | -49.62789 | 2025-09-04 04:55:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56809e39-b5cb-3b2d-af14-55041550f3fd | -15.15839 | -52.3726 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cf193bf-b193-3d8a-905d-c7c8e63ceb85 | -12.99078 | -48.06862 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d2b5669-332d-3e38-b1e8-d78affa9b14e | -11.61891 | -52.18452 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5df7205e-2427-3e88-b0a2-158b76c7fe59 | -12.47046 | -48.08299 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 461b6983-9fed-31c7-b5ac-1f9c24339934 | -11.63937 | -52.2098 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e13d89c7-d165-33b1-808e-5ac47a266ed9 | -12.86613 | -48.02163 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbaddd27-eb06-3be2-8490-4699ff8c0660 | -13.44091 | -46.93581 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 561a46a3-ca83-3dcd-b374-6606c29101b8 | -17.17127 | -46.25213 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf7149ab-630b-3b10-95be-e739c1b0f5bd | -10.51176 | -50.43246 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf82b4bd-8a01-3b76-9d83-d2f9eba0ee84 | -10.8989 | -50.83054 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c498934b-eb36-3588-bbb7-49ee0ccdc12b | -14.90739 | -49.6283 | 2025-09-04 04:55:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c358b42-4e2a-379a-9824-50425f526014 | -13.45425 | -46.8349 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69272024-536a-3210-bfdb-b02a930a10cc | -14.75473 | -48.08276 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77e60960-3c0e-3c79-8e6d-111a0ebdfc5c | -11.85115 | -51.43909 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55778e5b-099b-326b-807f-660aebd9ea2e | -18.68839 | -48.18499 | 2025-09-04 04:57:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| efa07afd-bc3d-3b59-97bd-1b205feaf1bf | -23.42662 | -47.05595 | 2025-09-04 04:57:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6a09da0c-ceef-354a-ad13-1be0fbaaefdf | -20.28972 | -46.71249 | 2025-09-04 04:57:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8a64f570-98ef-3b97-9831-eeeae9656415 | -22.22644 | -55.97396 | 2025-09-04 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0333903e-588e-388f-8113-e993eb9b8335 | -20.10103 | -50.0095 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| df4d9eab-f6d7-3164-9ab6-5936afda51d0 | -22.05329 | -56.34225 | 2025-09-04 04:57:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d204ca2d-e93b-30ce-ae34-480ab0bef1f4 | -20.09217 | -50.01231 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| dac028f9-e1da-3d52-87f3-f822b405e9f6 | -23.29696 | -46.16349 | 2025-09-04 04:57:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c9a01a02-e731-3b2b-af74-e88893cb6517 | -19.25545 | -46.52901 | 2025-09-04 04:57:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4a3b2be-110f-34fb-a05f-b3493476f1d3 | -22.22369 | -55.96963 | 2025-09-04 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README78.md)
