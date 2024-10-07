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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb11a811-e94a-31bc-bd05-bb00c6aa6b50 | -12.9782 | -47.629299 | 2024-10-07 00:27:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74e6283c-ac10-3e76-bb47-a6f0c11af3e5 | -13.6079 | -50.831402 | 2024-10-07 00:27:13 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49384a44-723a-355f-afdb-c653609abfec | -13.6102 | -50.843201 | 2024-10-07 00:27:13 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d63c7df-2f90-3032-8791-631ef6a2fbaa | -13.6409 | -51.254002 | 2024-10-07 00:27:14 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19bdd543-f5ef-34d5-8ce0-06602c6ff13c | -12.5187 | -46.971298 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e94b0a5-b2ef-36c3-8d90-4d5b2a473377 | -12.5203 | -46.978699 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44fa4208-a2c4-3d88-a249-7379c078976f | -12.5251 | -47.000702 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5f39e28-339b-303c-96d8-7aef81b2477f | -12.5057 | -46.958801 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f695317c-2aaa-3f3d-9ba3-9cae41360510 | -12.5073 | -46.966202 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e197f7b-89f1-39d8-a3ba-c45aa37176de | -12.5089 | -46.973499 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 074ddd65-d596-3b17-93e9-6de5623e00ad | -12.5105 | -46.9809 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4ffe2a-92a6-3481-9ba9-302070ad6798 | -12.5121 | -46.988201 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35dbdd69-5d1b-3026-9ead-904d90cf72f1 | -12.5153 | -47.002899 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6ca2045-df3a-3bc9-9496-d4ccbfe54a6f | -13.2669 | -50.602402 | 2024-10-07 00:27:18 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c74991b4-8d57-381b-91a7-5494a7bb3f63 | -13.2691 | -50.613701 | 2024-10-07 00:27:18 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc7e605e-ffed-3e61-90be-eb2168b55842 | -13.2714 | -50.625 | 2024-10-07 00:27:18 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7171459-439f-3f9f-a053-f9baba82a938 | -12.4959 | -46.960999 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48a47734-d6be-3bf2-b5ed-cc33fd2c3a3a | -12.4975 | -46.968399 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4c79482-cfc7-3f13-a577-b250ec3f6de1 | -12.4991 | -46.9757 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6a38cfc-4241-3e16-9700-ad3b2dc585a5 | -12.5007 | -46.983101 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 917f0b3b-d7dd-3bc2-b698-1f06c3fd1b79 | -12.5023 | -46.990398 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98ce258f-0514-3a8c-b587-e7cbf58c483b | -12.5039 | -46.997799 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d937109-af25-3e32-8bdb-9d74b586111f | -12.5055 | -47.0051 | 2024-10-07 00:27:18 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f52e3833-9ff7-343d-9747-c0c0fbdb514b | -10.2725 | -45.420101 | 2024-10-07 00:27:18 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b7773f95-ed5d-3c68-84a7-c5f096e455fa | -10.2741 | -45.427101 | 2024-10-07 00:27:18 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 26b8a86c-0628-32f6-85c6-035a43e628f7 | -12.465 | -46.960201 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4270d17-73b3-33f2-a721-08dbb270c7e7 | -12.4861 | -46.9632 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 544f62c3-a74e-38c8-a594-e81c42acfdc8 | -12.4877 | -46.970501 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72e12ab3-4de7-318f-81f6-66f136263bed | -12.4893 | -46.977901 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83ef4db0-6ed6-3b04-92ed-1d1954daf6c9 | -12.4909 | -46.985199 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec9b3c4-5c57-3754-8921-88912e8a0291 | -12.4925 | -46.992599 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 147e76b9-0949-387a-8022-abdacd63824b | -12.4941 | -46.999901 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e03057ab-de0a-3e27-8967-10e3f3b73175 | -12.4957 | -47.007301 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b5bf863-4024-3b7f-8c95-32b59a37b0b1 | -12.4973 | -47.014599 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bde7b0e3-4a6f-3909-859d-59ed07bdd8a7 | -12.4763 | -46.965401 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| daa843ef-739f-3cb9-afcc-46e2ada94a12 | -12.4779 | -46.972698 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 299fc868-c133-3555-9950-650db69e7544 | -12.4795 | -46.980099 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7da5e405-1c4f-3283-a084-cafea81c702c | -12.4665 | -46.967602 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e4711e5-a577-3879-991a-47163cde5d21 | -12.4552 | -46.962299 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd7b476b-6d6b-38bd-a355-3aa11e831472 | -12.4567 | -46.9697 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e90b3382-8d79-38d8-8603-e6fcddc8cbe4 | -12.4517 | -46.9939 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f24b595c-f495-3403-b7ab-c9384792786b | -12.4419 | -46.996101 | 2024-10-07 00:27:19 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d0dc266-63a9-3963-9541-a23c7d292059 | -13.3233 | -51.292599 | 2024-10-07 00:27:20 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00b15118-8a4f-3567-94bb-d217295fac5f | -13.3258 | -51.305099 | 2024-10-07 00:27:20 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e78d7c6-66a7-3c28-810c-9eab2a605bf6 | -13.3161 | -51.307098 | 2024-10-07 00:27:20 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 042d5483-eb76-3b8b-b2e3-ca843fdfc7a9 | -13.2036 | -51.1506 | 2024-10-07 00:27:21 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1003e665-1a5d-3bb9-bb18-0397e9991e4b | -11.7409 | -44.483002 | 2024-10-07 00:27:22 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0788621-9642-3b95-99e1-d92933faebf5 | -11.7425 | -44.490101 | 2024-10-07 00:27:22 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bfbfb1ad-644e-3996-94e8-0e29859246b7 | -11.7441 | -44.497299 | 2024-10-07 00:27:22 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2793f6-501b-3b3b-a30c-84dbcfad92d3 | -12.8225 | -50.521301 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0535697-e467-3ef4-806f-c4347a5d579b | -12.8247 | -50.5322 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49844890-bf68-35b4-8936-02bf03a7a98d | -12.8314 | -50.565201 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f96ce181-08bf-3e1a-b9da-b9cb4617fb30 | -12.8084 | -50.5014 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1960d460-b7f4-3080-86bd-d4fe814a01d3 | -12.8106 | -50.512299 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0ec5839-4ccc-3378-80e3-d6eb4e97522d | -12.8128 | -50.5233 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26c7d291-2627-3be0-bf90-b4eca3157882 | -12.815 | -50.534199 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff3f42b-61d4-339a-8d0a-66379b8a9517 | -12.8217 | -50.5672 | 2024-10-07 00:27:25 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae00c556-81d2-312c-a234-597d7b4f745b | -12.7768 | -50.496601 | 2024-10-07 00:27:26 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef0d49c-62a0-3b3c-9cd5-d131ec3d9b31 | -12.779 | -50.5075 | 2024-10-07 00:27:26 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f4a6153-a84a-3acb-b4ce-8b3cd6956665 | -11.8999 | -48.296001 | 2024-10-07 00:27:33 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30c0ffea-87c3-3cf2-82ab-b653e0206047 | -12.1897 | -50.517601 | 2024-10-07 00:27:36 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fcb8032-4456-38f9-a035-bc98d3159cf8 | -12.1919 | -50.528301 | 2024-10-07 00:27:36 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d20a3136-5500-36d8-a388-c5ce309b94b8 | -11.6295 | -48.422401 | 2024-10-07 00:27:38 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2dd508c-3e0b-3597-b4ab-33c2dea4871b | -11.6312 | -48.4305 | 2024-10-07 00:27:38 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7014a1b-7ecc-3fbe-bc00-3d809b39b2c1 | -11.633 | -48.438702 | 2024-10-07 00:27:38 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 439fdb8d-f9ee-3eb2-a751-59fca774b511 | -11.7502 | -49.970001 | 2024-10-07 00:27:41 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f422845-cd86-3256-91b8-c88c8f437872 | -11.7523 | -49.979801 | 2024-10-07 00:27:41 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0164e8e-ad54-3f00-95ec-f816449c48e7 | -10.2823 | -45.4179 | 2024-10-07 00:27:49 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 063bc68f-0448-309b-a20e-8103a175354c | -10.2839 | -45.424801 | 2024-10-07 00:27:49 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2610d98-08ac-39f3-8c88-b5f992048f57 | -9.9498 | -44.091 | 2024-10-07 00:27:49 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a344196-f6b1-3823-b60b-1d771e84ce3a | -9.9515 | -44.0984 | 2024-10-07 00:27:49 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 21656675-9114-3b8a-a170-294be21a29f1 | -9.9532 | -44.105801 | 2024-10-07 00:27:49 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f06b373-d9b7-3a9b-ac0b-5c1d59974ec9 | -9.94 | -44.0933 | 2024-10-07 00:27:49 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fadd53ef-be01-3707-b986-9b006976856c | -9.9417 | -44.1007 | 2024-10-07 00:27:49 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7df177b-91ed-3012-988e-3c63223f9918 | -9.9434 | -44.108101 | 2024-10-07 00:27:49 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1144b0b7-6724-395f-ad20-c7d977b923b6 | -11.2593 | -51.351799 | 2024-10-07 00:27:54 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efaefc50-2afe-3d35-82c0-cb5f3324a8a3 | -11.2617 | -51.363499 | 2024-10-07 00:27:54 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf7500c0-18f9-312f-8fab-74dc1d3303e8 | -11.2641 | -51.375198 | 2024-10-07 00:27:54 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dafbce05-a7f5-39a4-bcfc-f29b53577ad2 | -11.2495 | -51.353802 | 2024-10-07 00:27:54 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55da525c-8a91-3a4e-87d7-9fd61944dc76 | -11.2519 | -51.365501 | 2024-10-07 00:27:54 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ecbb409-3255-304c-8552-2323a1a7a22c | -8.6271 | -40.530499 | 2024-10-07 00:27:57 | METOP-B | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5a02cf3e-4433-3625-a126-11e15621f2be | -8.6299 | -40.542198 | 2024-10-07 00:27:57 | METOP-B | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 07c36436-072d-3778-85bc-f5577245ceb7 | -9.2383 | -43.511002 | 2024-10-07 00:27:59 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 29fc0d29-8d33-37af-97e7-1c4fedb21ba5 | -9.2401 | -43.518799 | 2024-10-07 00:27:59 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8205038d-8aa3-31b2-9a87-c71df5ec146e | -9.1825 | -45.704601 | 2024-10-07 00:28:08 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f8bc68f5-66d0-32e9-99c9-7e293ba8159a | -9.096 | -45.869598 | 2024-10-07 00:28:10 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df68a406-ec99-36af-ba2a-8267c67adbb4 | -7.8283 | -42.2006 | 2024-10-07 00:28:16 | METOP-B | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 54beeb7b-2e1e-3144-b3bf-77cf15781096 | -7.8305 | -42.209999 | 2024-10-07 00:28:16 | METOP-B | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5b5e3278-4697-3bc6-a269-bd1999e83a1f | -7.8327 | -42.219398 | 2024-10-07 00:28:16 | METOP-B | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61c7ba0a-f1e5-3c48-a7b4-1b287897dd38 | -7.6364 | -42.481201 | 2024-10-07 00:28:21 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c3467203-b8a3-3403-831a-7a2ad5e36f15 | -7.6385 | -42.490398 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 727d5ff4-7957-303d-9775-447288b68658 | -7.7744 | -43.071201 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9592172-ac5f-3ee5-a704-c21075f528a3 | -7.6116 | -42.419201 | 2024-10-07 00:28:21 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 328348da-b53b-3e4b-801e-0138b2f650f8 | -7.6137 | -42.428398 | 2024-10-07 00:28:21 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1cda621b-fe9d-36d7-953a-12169b4df1e3 | -7.6288 | -42.492699 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d0a7e464-1aec-30de-93e8-3f49c78c899c | -7.631 | -42.501801 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99b15e59-7e0a-332e-b520-206c6e4cf427 | -7.7646 | -43.073502 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c7bae6c0-2c04-3339-8c89-89212d964cbb | -7.7685 | -43.0905 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 043101b2-70d9-376d-8567-cdaeb17163bc | -7.7705 | -43.0989 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8beef435-1846-3c43-8201-c70ca8ba201c | -7.619 | -42.494999 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README10.md)
