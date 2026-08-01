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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d82a613-4fa0-377b-9e2f-80a870aa5337 | -18.38354 | -47.2085 | 2026-08-01 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4107735-0306-31b4-b999-4413aaea0f37 | -28.76864 | -50.09301 | 2026-08-01 04:25:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c95f0f2b-477a-3456-8f70-71abf352e11c | -20.38255 | -58.02539 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| adaf4116-f3a7-33b0-ad71-d7b4e31fc725 | -20.55981 | -57.318 | 2026-08-01 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a0209b8-816b-3107-be5c-8834f43d601e | -28.29954 | -49.87426 | 2026-08-01 04:25:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a702e247-fe7e-309e-a672-1980e360915f | -21.70693 | -56.52344 | 2026-08-01 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61d2cc7b-33a0-3ecc-8fa7-df13c0962fb6 | -28.29623 | -49.8736 | 2026-08-01 04:25:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| da5726c2-019a-3bc0-9fea-d7709af83569 | -23.19879 | -49.15712 | 2026-08-01 04:25:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df429251-3d64-3314-bf54-fef83136555d | -21.29301 | -56.14242 | 2026-08-01 04:25:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e5e1c88-9e30-310d-b3a1-6e4a265cc9b9 | -20.37617 | -58.01252 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 933937e9-797e-3a26-ae4e-77e6d7a72286 | -23.19939 | -49.15337 | 2026-08-01 04:25:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 878c8106-4806-3600-91e3-f20b64b01aaa | -20.38449 | -58.02593 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d95d032c-0686-32c3-a75a-fdb50b9d023e | -20.38178 | -58.02901 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cda87a9b-056b-3d6e-94b0-135b0e47d60e | -20.38332 | -58.02176 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 098b61e5-8e6c-3aef-a905-a1a620e41a59 | -21.98429 | -57.60163 | 2026-08-01 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd09411f-f558-39ff-8129-47570d7992bd | -28.43749 | -49.57354 | 2026-08-01 04:25:00 | NOAA-21 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9cbcfd41-e6b9-3bd1-87a1-c53eee7ee1aa | -28.29575 | -49.98626 | 2026-08-01 04:25:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5efd35be-6e50-3ebc-ae84-726d6fef4ef1 | -20.38152 | -58.0138 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 276bc0f2-fe16-36b4-a4c3-d04ae2162a97 | -26.82175 | -51.81648 | 2026-08-01 04:25:00 | NOAA-21 | PONTE SERRADA | SANTA CATARINA | Brasil | 4213401 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 17415d4d-1bee-35f7-bda6-1801b0090e5c | -20.3837 | -58.02954 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8ffb1cc4-e7fa-3ccd-8c16-36b5054235e9 | -21.04598 | -55.82935 | 2026-08-01 04:25:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61758801-5701-3a7e-9234-857b8433528d | -23.02788 | -52.65702 | 2026-08-01 04:25:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 2d118867-b83b-3900-b3a0-f9aa67c2c4dd | -20.60551 | -57.3047 | 2026-08-01 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d29025f3-f8f9-3ebb-b5d0-ae6aede83faa | -20.60483 | -57.30793 | 2026-08-01 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90f4cb75-a974-3745-a763-c1501ba71a0f | -20.37951 | -58.0132 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fd75bb95-aac7-3b09-b15c-6f71a8816599 | -23.78962 | -49.29203 | 2026-08-01 04:25:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 774b7ad0-524e-34ec-8859-e4d82fbc1977 | -28.59004 | -50.30115 | 2026-08-01 04:25:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b61ae10-7eaf-35b0-80b2-702c027037ad | -21.04137 | -55.82827 | 2026-08-01 04:25:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdcf58a9-f73e-3c6d-b10a-70ecc2590559 | -21.66751 | -56.32924 | 2026-08-01 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6ed94dad-0927-356a-8c51-9bbc6bf851df | -28.29907 | -49.98692 | 2026-08-01 04:25:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b13e76f6-2b76-34fb-be1d-29c483fb3e1c | -20.38528 | -58.02231 | 2026-08-01 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c9904545-a5f5-3597-917e-87e8135b9766 | -21.66863 | -56.3238 | 2026-08-01 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f5d84200-daaa-33a0-88fa-ede7b6cb4546 | -20.56189 | -57.30824 | 2026-08-01 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa5140da-f236-3f96-af36-c7a46a5f003f | -20.6062 | -57.30143 | 2026-08-01 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66217af4-18e8-3f03-bf9b-7dcca57b8476 | -29.00068 | -50.75537 | 2026-08-01 04:25:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a533898a-8caf-3d91-bd5c-129adfed4753 | -20.56121 | -57.31145 | 2026-08-01 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd808487-f03f-3ba6-a568-615375618435 | -29.98109 | -51.20484 | 2026-08-01 04:27:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 1a7e2cf5-316f-3d92-8423-bd0afa049772 | -14.073 | -46.2669 | 2026-08-01 04:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 17c9dc25-00a4-3229-b4ca-cad40f2c1bb6 | -14.0929 | -46.2407 | 2026-08-01 04:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 9b0d84bb-a0bf-3f28-a084-ce28276d7da9 | -14.0925 | -46.2637 | 2026-08-01 04:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| dfeaad6f-42e4-36b3-94b6-d9ed28bcdc2f | -4.2578 | -38.0284 | 2026-08-01 04:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 78.6 |
| a7ca6110-d400-3b2e-acfc-1c434a925342 | -11.2591 | -54.8517 | 2026-08-01 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 892ae6c2-f8ba-3d93-a679-615c79fb2e8d | -14.0725 | -46.2899 | 2026-08-01 04:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 3da4aeb2-494f-30de-874d-a6fa17da4004 | -11.2399 | -54.8737 | 2026-08-01 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| c20420b7-4c6d-31bd-a21b-42392abd3be4 | -11.2402 | -54.8534 | 2026-08-01 04:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a802ab87-d7af-3d19-8407-ab8cdb4e12d3 | -11.2402 | -54.8534 | 2026-08-01 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5995499b-d9bf-3910-8653-1a0f2b12d38a | -11.2591 | -54.8517 | 2026-08-01 04:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| dd63437d-5b2a-3b27-a665-3b66107ff2c9 | -4.2578 | -38.0284 | 2026-08-01 04:40:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 63.2 |
| fd0b4848-18fd-3fda-8044-b34121928333 | -14.073 | -46.2669 | 2026-08-01 04:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a1dd1291-91bf-3744-87ab-cc51da767d17 | -14.0725 | -46.2899 | 2026-08-01 04:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4279ac31-da36-336c-87c3-87818bcba29c | -14.0925 | -46.2637 | 2026-08-01 04:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| d980aca8-25d3-3d52-977d-7f0f524c457c | -11.2402 | -54.8534 | 2026-08-01 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3521a3cc-5abf-39b6-b724-cb27f56677a3 | -14.073 | -46.2669 | 2026-08-01 04:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2e45617f-2c9b-3034-9919-0fa2d26b1c81 | -11.2591 | -54.8517 | 2026-08-01 04:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| cfed8a3d-c212-3b0d-8da2-cb657158bef6 | 1.10533 | -60.51376 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c292593-f242-3eea-8479-9f2999da243a | -0.99104 | -48.08451 | 2026-08-01 04:53:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a0651fc-6400-3730-8385-0b3e3a0e0276 | 0.79059 | -51.96743 | 2026-08-01 04:53:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f02914bb-36fa-392b-8f63-13d75a11c86f | 1.09459 | -60.52484 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df27387-aa9e-372e-929d-86c19a05ba5a | 1.0993 | -60.52176 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 114962e3-117a-3012-896d-1ec1e9effadc | 1.09857 | -60.51026 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f7181e0-5283-31c6-994b-96cad962d13f | -0.0904 | -51.28048 | 2026-08-01 04:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a86ec13a-1310-3766-aea4-0edd5e13a908 | 1.09996 | -60.51929 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba4ac21a-406b-32fb-a7bc-1f6f17a61384 | 1.09788 | -60.50574 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e65a26d9-cd05-3521-b173-ea3b9da19e99 | 1.10003 | -60.52629 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e01df6ba-8c13-380d-bc4b-7d44639a25ae | 1.09324 | -60.52275 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c3f0dba-6df3-3ec9-bfa1-fd06ef9c7c14 | 1.09927 | -60.51477 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb977137-f3ca-3570-b663-d75bd72b0bc8 | 1.10065 | -60.52382 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0cdc19b-8131-3b6b-9de4-a632139cd1a7 | 1.09858 | -60.51725 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c7fd2fd-6103-3cc2-bbed-f3db020586ae | 1.09785 | -60.51273 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19ed00bb-b775-3c64-a979-88fbb788c64d | 1.10135 | -60.52837 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f0c0c24-df2e-3a5a-8335-1d9603309d36 | 1.10602 | -60.51828 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7bdfa00-5097-3c4f-8def-660df8355f49 | -0.99162 | -48.08081 | 2026-08-01 04:53:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 428c8d55-1294-3d6e-8028-cf41924f0dde | 1.09713 | -60.50823 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cf7adad-81c9-3dde-ae14-56144e32aab3 | 1.09641 | -60.50373 | 2026-08-01 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ab15d29-ac5a-3613-807a-adcdddf83880 | -0.08702 | -51.27995 | 2026-08-01 04:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 780f18f1-990a-3b3e-a707-d840823b1b3c | -5.93366 | -46.35122 | 2026-08-01 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d178e6fe-2e8d-3d3f-8d70-19033149a4a7 | -3.4831 | -47.68542 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20f1647d-d801-3a98-ae17-74bb8e8f734d | -6.42815 | -43.71247 | 2026-08-01 04:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fee4c1eb-e016-34e5-8e90-f5d59a0f2dbe | -4.96249 | -45.14429 | 2026-08-01 04:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4dc0d92-34d0-3d3e-9449-c460606cfac5 | -6.26977 | -41.87993 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ff6b23b3-441d-302e-a2cb-cb29d7039ca0 | -5.04249 | -43.26537 | 2026-08-01 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f79677bb-d11d-324a-8eff-e58f1e008444 | -6.67427 | -42.56719 | 2026-08-01 04:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 296c6f03-c5bb-3683-8f80-ae709fd8c14b | -7.24808 | -42.13911 | 2026-08-01 04:55:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 477cfc55-4ffd-3161-a689-6629d5696bf6 | -6.72098 | -44.01708 | 2026-08-01 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8389103-a4d4-3f30-b69e-fc7cbd1f683a | -4.27242 | -48.19685 | 2026-08-01 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66bb77f8-a7d7-3919-a53b-dc856b7598a3 | -6.64706 | -43.91783 | 2026-08-01 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e5e05740-e608-3e18-90a4-0dc6d2a7e900 | -7.19593 | -42.96144 | 2026-08-01 04:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0bd7f940-4c63-37e9-9644-66136b84f7b2 | -6.66859 | -42.56969 | 2026-08-01 04:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9caa1d01-c5a6-3dc2-9e68-3fa1ae08ff9a | -8.34493 | -45.98754 | 2026-08-01 04:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d47e6dd5-0b2f-316e-8048-d9f2b2b2705a | -0.85524 | -52.71384 | 2026-08-01 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 631bd2c7-6755-35f8-bc9b-7a1b6dfc3ad7 | -7.49548 | -46.12004 | 2026-08-01 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa2b366-e0ba-3aad-8e3c-b6babdc07704 | -3.1171 | -47.90806 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f775439-cebb-3978-89d7-3cc64d7598a1 | -3.84931 | -44.08937 | 2026-08-01 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 019076bd-bf79-3245-a0da-c56f969e24c1 | -5.81828 | -44.75846 | 2026-08-01 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 788917e7-e719-338b-a097-df16bfa98c8d | -6.56231 | -55.1592 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d53c1336-e629-3e2f-99cb-b8b59c8da223 | -7.60624 | -42.58572 | 2026-08-01 04:55:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dba8251f-2c4c-356a-9ec0-95f8ad71273f | -4.65187 | -42.4337 | 2026-08-01 04:55:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d0454b08-3c50-3b9f-85f4-6f1f7eb12dec | -6.4274 | -43.7177 | 2026-08-01 04:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 43087e77-f180-364a-850c-4d608dc0c090 | -3.0322 | -48.40751 | 2026-08-01 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1046dfeb-5862-3f24-a3cc-cc4976dfb92c | -6.27076 | -41.87284 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |


[Clique aqui para ver as próximas entradas](README16.md)
