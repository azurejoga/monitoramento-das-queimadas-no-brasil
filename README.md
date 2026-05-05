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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aa208ca-ee61-30dc-81c9-bbac9b09c34c | -14.0457 | -47.6318 | 2026-05-05 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 7a113ac0-8e68-3d9b-ae07-b29f83449b7b | -21.8696 | -48.0712 | 2026-05-05 00:30:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1787ffdd-b194-3603-a834-1f3d892b41b3 | -21.8488 | -48.0763 | 2026-05-05 00:40:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 048bd09c-e205-3e8b-90a5-22bc428f33d9 | -14.3248 | -57.7276 | 2026-05-05 00:43:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aaaed2f5-f374-3d1f-9fa5-a47db78fb05b | -20.0923 | -57.203098 | 2026-05-05 00:43:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0d60eef5-2b7d-3ad9-89d2-852e6144ad91 | -14.019 | -47.620499 | 2026-05-05 00:43:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90f0b8fb-fed2-37c2-a21c-5c536f81852a | -12.3376 | -50.003399 | 2026-05-05 00:43:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e065668a-b175-3cf5-991c-a94de9ea85aa | -16.597601 | -58.2313 | 2026-05-05 00:43:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 836d155d-ebf0-365b-99a4-a97bc61f1e61 | -21.851601 | -48.044601 | 2026-05-05 00:43:00 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 78f58164-7cd1-3692-8ff6-4a392605c4d3 | -12.0226 | -55.533401 | 2026-05-05 00:43:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94ffa501-aac5-3a88-9423-3e5fc814ee57 | -21.6973 | -48.412899 | 2026-05-05 00:43:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f24f5886-a169-3903-a8b0-d83160a1fba9 | -12.0242 | -55.540699 | 2026-05-05 00:43:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43050094-e093-31c1-9b97-845013750881 | -14.0286 | -47.617802 | 2026-05-05 00:43:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 395cd9f0-836c-31eb-a552-b5c0bfea9c27 | -12.334 | -49.989399 | 2026-05-05 00:43:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a500a6b-4558-3678-ab70-1716523403f0 | -12.5154 | -58.478298 | 2026-05-05 00:43:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed74554f-a1b5-34b8-a656-ad382cb3c183 | -12.2903 | -57.545601 | 2026-05-05 00:43:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99beade7-4781-3aca-904d-74aa50a7b7ed | -12.5138 | -58.471001 | 2026-05-05 00:43:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35485d86-e692-3140-b92a-d6898202a0e4 | -13.6921 | -55.665001 | 2026-05-05 00:43:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db9e2c2e-8605-3bc1-9011-9457b5ea5714 | -16.1591 | -58.485401 | 2026-05-05 00:43:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1cd08fd-e64d-3352-a973-98ee3cb9acf4 | -13.6938 | -55.672199 | 2026-05-05 00:43:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b12b5bac-d78a-369f-b5aa-07b60c3267c0 | -14.0012 | -56.628502 | 2026-05-05 00:43:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87a10db2-bf8b-3571-a28f-74df0c4184cd | -21.8585 | -48.071098 | 2026-05-05 00:43:00 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b1ba290f-1f4f-3ec1-8919-24b973b3cc94 | -16.596001 | -58.2234 | 2026-05-05 00:43:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec7e707f-23c8-388e-9e16-734a4820bc48 | -23.5599 | -51.7337 | 2026-05-05 00:43:00 | METOP-B | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26c1444c-5a36-3a19-98dc-38198241185b | -12.2918 | -57.552601 | 2026-05-05 00:43:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8de5a1-b1da-39ff-a09a-f032245e0a97 | -21.855 | -48.0578 | 2026-05-05 00:43:00 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 861c7685-31fc-3b46-97c2-d6e0e933decb | -21.958799 | -57.580502 | 2026-05-05 00:43:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b50b5ddf-4419-31b4-9173-46b2fcaf2a80 | -20.2253 | -50.7393 | 2026-05-05 00:43:00 | METOP-B | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2eea205-364c-302c-aa37-8ad3afe953c3 | -21.841999 | -48.047501 | 2026-05-05 00:43:00 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 875a7e21-b5c2-35ec-8c2b-afa0897e830e | -12.5056 | -58.480499 | 2026-05-05 00:43:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00380c8c-9cce-3ca2-81c1-ec52453da9fe | -20.227699 | -50.7491 | 2026-05-05 00:43:00 | METOP-B | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9fc5495c-9837-3c9d-8c11-8bb30e299b3f | -12.504 | -58.473202 | 2026-05-05 00:43:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b426a8a1-3423-38cb-a099-36fb54b9ec61 | -13.9996 | -56.621498 | 2026-05-05 00:43:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9543130-5cf9-344c-9d3e-0904d0c1c70d | -21.8454 | -48.060699 | 2026-05-05 00:43:00 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7ef400-0895-3b9d-9b51-335c7e626d75 | -14.0336 | -47.636799 | 2026-05-05 00:43:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9200c9c7-c66f-3e81-bc2a-701a37db0a3e | -16.157499 | -58.477501 | 2026-05-05 00:43:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e167739-cdb3-3bc6-92b7-2326b07892fd | -23.558001 | -51.725399 | 2026-05-05 00:43:00 | METOP-B | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0c78715-6770-32a1-a78c-498cd6203396 | -21.8495 | -48.0527 | 2026-05-05 00:50:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ceb26283-9da5-32e0-aead-e660b4517b03 | -21.8696 | -48.0712 | 2026-05-05 00:50:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b09bf9bd-94f4-3787-9866-dca7e38ec115 | -21.8488 | -48.0763 | 2026-05-05 00:50:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0a474b6f-508b-3bca-80a4-aa7fa610c6e4 | -21.8696 | -48.0712 | 2026-05-05 01:00:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 10560ecd-109f-3b15-a1c4-33d488d59042 | -12.0271 | -55.536999 | 2026-05-05 01:15:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52ee5108-7836-3e6b-98f4-0d2e72399bf1 | -18.432199 | -54.711601 | 2026-05-05 01:15:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a77fa180-de4a-3dc8-9b67-a411c9e909de | -16.5963 | -58.2323 | 2026-05-05 01:15:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8be5bd4c-dc7c-3f3b-aff4-7a2b65eef6f8 | -12.3357 | -50.002602 | 2026-05-05 01:15:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 093cb3b3-91e7-3aa6-8d7c-14a3484add25 | -12.3391 | -50.016102 | 2026-05-05 01:15:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8be27556-5d4f-3e05-848e-2eeff33dac6f | -12.5145 | -58.487801 | 2026-05-05 01:15:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95bb9687-60e6-3ae9-a063-8746bd7e8da5 | -18.440399 | -54.702 | 2026-05-05 01:15:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c8283fc3-9666-3925-b9de-030cb4621190 | -23.556299 | -51.7258 | 2026-05-05 01:15:00 | METOP-C | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7fccdc9a-0e7d-371c-b5ac-22fab0886a02 | -21.8519 | -48.060398 | 2026-05-05 01:15:00 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 94341384-854d-36d8-bcbe-ffab99144ebb | -16.160101 | -58.4972 | 2026-05-05 01:15:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c9acf68-abe1-3aeb-90ae-e805a1803050 | -12.5031 | -58.482601 | 2026-05-05 01:15:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 265d1a15-a6f8-39f3-ab95-2ec40452ad2e | -12.5129 | -58.4804 | 2026-05-05 01:15:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d958a253-6e39-30d1-afc9-f5ac7caadedc | -12.5047 | -58.490002 | 2026-05-05 01:15:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 726d989c-caff-31ca-a543-c3598ad030e1 | -21.535 | -47.1353 | 2026-05-05 01:15:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7857c218-8998-382b-93b5-d79496a22a34 | -18.441999 | -54.709202 | 2026-05-05 01:15:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7ad54dbf-9a8c-3483-b852-9eec682f433e | -23.558201 | -51.733898 | 2026-05-05 01:15:00 | METOP-C | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86245259-9377-3c00-88a6-8a58578a6a79 | -23.568001 | -51.731201 | 2026-05-05 01:15:00 | METOP-C | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a371b1a-7643-394b-b70b-0eda88fdd6f9 | -12.3454 | -50.0 | 2026-05-05 01:15:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 650b1305-2ed2-3271-9bad-cd9c7c261e59 | -12.0288 | -55.544201 | 2026-05-05 01:15:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6b3f439-0753-3c3c-9731-bd52cb1be137 | -23.569901 | -51.7393 | 2026-05-05 01:15:00 | METOP-C | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a257ac30-b6d7-3c95-aac6-6c6fca68f9cf | -12.3488 | -50.0135 | 2026-05-05 01:15:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32b57a56-75e6-377e-a49b-639c2715f0c8 | -13.6982 | -55.669998 | 2026-05-05 01:15:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd02bede-9b2d-397f-bbd8-4c6f8e414383 | -16.598 | -58.240299 | 2026-05-05 01:15:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74e9764a-f1e5-3487-a10c-758dc8c5747c | -16.1584 | -58.489101 | 2026-05-05 01:15:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1fd24d0b-f983-3ccd-8b1f-5279db7f0d49 | -23.566099 | -51.723099 | 2026-05-05 01:15:00 | METOP-C | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb82d66b-3baf-347f-802b-42a96730d653 | -16.1486 | -58.491199 | 2026-05-05 01:15:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67e32923-3676-3f30-a990-7ae01a4a8c76 | -14.3234 | -57.734402 | 2026-05-05 01:15:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ccecb19-9c1f-3084-aea6-f345371ec987 | -21.5446 | -47.132401 | 2026-05-05 01:15:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fea5db6b-bcc2-3716-be87-27d826285128 | -21.8488 | -48.0763 | 2026-05-05 01:30:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 68a4f890-c703-38f0-8c79-a3d84ddcd0fa | -21.8696 | -48.0712 | 2026-05-05 01:30:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e8cbb224-841e-3e2f-8bf3-e89277b9b3d3 | -21.8488 | -48.0763 | 2026-05-05 01:40:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 67.9 |
| dccac750-7925-3d35-ac96-4999557e0732 | -21.8696 | -48.0712 | 2026-05-05 01:40:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 32d8b6a1-670c-3561-b62a-7464dbef0b23 | -13.92644 | -47.28759 | 2026-05-05 03:32:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64f9821c-cb8a-38f1-8ee4-23e1c1d5f740 | -11.13067 | -45.14021 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3fe47080-4617-35f2-8a06-9954e555b1bb | -11.78851 | -43.61332 | 2026-05-05 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 890180d7-66b1-366e-8368-f311582f7da0 | -11.1325 | -45.14239 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7b90d65a-5e6c-3531-a86d-cac27bc67508 | -11.78692 | -43.62133 | 2026-05-05 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| effe0068-9ff2-324b-966a-c8e36fb2a40d | -11.94882 | -43.3782 | 2026-05-05 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a12d034-bed2-3f4c-97cf-6f239be66ef5 | -11.79343 | -43.61842 | 2026-05-05 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57075ae0-0206-3a8e-97a4-040743deb306 | -11.13704 | -45.14132 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddc34891-2bd0-31b0-b0c3-09213e86e8cd | -11.91719 | -40.67126 | 2026-05-05 03:32:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0129aa5-92ed-38ee-a819-1d2d3b8e6369 | -10.20936 | -44.76305 | 2026-05-05 03:32:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28f0d924-e15c-350b-a5a6-33b99b6bf723 | -14.0743 | -47.62669 | 2026-05-05 03:32:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a97e1ec4-8d96-34fe-ad13-bedcbfb59c4d | -13.92616 | -47.28695 | 2026-05-05 03:32:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5845bf32-3618-3e15-a785-8231ff6a257d | -14.05241 | -47.66698 | 2026-05-05 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b62414cc-8eeb-32a6-af33-4f84e9478f7c | -9.5625 | -44.56735 | 2026-05-05 03:32:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2bfec6d-3210-32e8-a3f7-ab536d7cd414 | -13.43434 | -43.84713 | 2026-05-05 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 49179ac6-ea02-3005-ab7f-22438d6240f8 | -12.27268 | -43.50264 | 2026-05-05 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8091c561-a855-3232-81b5-bfcc774cb74d | -14.07499 | -47.62976 | 2026-05-05 03:32:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fbd5611-77ae-3b37-a29d-120fe5428dae | -9.56784 | -44.57346 | 2026-05-05 03:32:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 062745c9-d5d4-3a2b-a9a7-b517387ba8e3 | -11.13352 | -45.13738 | 2026-05-05 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5c6828dc-b500-344e-acd5-fc174dd026f1 | -11.782 | -43.6162 | 2026-05-05 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 362d8e1e-f02b-3a6c-b71b-baf75b389b95 | -11.96861 | -43.97967 | 2026-05-05 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1cf4ade-5b38-3586-8639-997c4ae4e4e3 | -12.27678 | -43.51157 | 2026-05-05 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fefb487d-f411-3dc2-bde8-a4796d3707b2 | -12.26707 | -43.50147 | 2026-05-05 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc3c959d-823b-3b30-9fb4-616fe2294035 | -14.0515 | -47.6637 | 2026-05-05 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 81c69267-7efd-33e9-a58a-3f675e7b659f | -13.43686 | -43.84851 | 2026-05-05 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 63389ced-379b-38e4-9e47-fef94a6fe755 | -12.27754 | -43.50767 | 2026-05-05 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3df45e33-008c-356e-a58d-f89a604dbf1a | -12.27192 | -43.50654 | 2026-05-05 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README2.md)
