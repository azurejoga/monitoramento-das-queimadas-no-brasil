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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b2d7bef-79cd-3359-89e9-b4603de45382 | -12.4843 | -58.4795 | 2026-05-06 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f6a1f8fa-668e-3e33-81cb-fcef446f0634 | -12.5222 | -58.4765 | 2026-05-06 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| df3187ce-9cad-3740-9da9-151ef9df4494 | -12.5031 | -58.4979 | 2026-05-06 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 3028cfe7-c07a-3bfd-83b0-0da6afb1a317 | -12.5033 | -58.4781 | 2026-05-06 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| cfef1433-236a-3902-b7e1-095592a61587 | -12.5035 | -58.4582 | 2026-05-06 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d7e61289-0415-364d-8ca3-138fc8f22a5d | -22.60706 | -49.56434 | 2026-05-06 00:30:00 | TERRA_M-M | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c2d07422-d105-3b17-a955-f57da1ce79c0 | -22.80528 | -49.34569 | 2026-05-06 00:30:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 83ba42c6-170f-3cb4-86b1-24d8d411657f | -23.08401 | -48.61883 | 2026-05-06 00:30:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 98e0018d-afb3-3a70-9dd7-ac427b281beb | -21.71175 | -48.42287 | 2026-05-06 00:30:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 04b1644a-3453-3216-8068-9fb7a0b8ffe8 | -22.74423 | -48.21143 | 2026-05-06 00:30:00 | TERRA_M-M | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49a5f2ee-a343-37f8-b273-d5e4ed390b6f | -21.79534 | -50.77752 | 2026-05-06 00:30:00 | TERRA_M-M | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a7323542-c8f0-3f12-8d1e-78f0d3be09dd | -21.7022 | -48.42478 | 2026-05-06 00:30:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 830d80d4-9741-3a03-9af6-697237d4ca2f | -23.70434 | -51.68124 | 2026-05-06 00:30:00 | TERRA_M-M | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 1dab607f-b7a7-33c4-b615-9caf96ccfbe7 | -21.28225 | -48.97751 | 2026-05-06 00:30:00 | TERRA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 185f5dbe-32a4-3ae7-bf92-65acd54cf076 | -23.07469 | -48.62053 | 2026-05-06 00:30:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8fa0d9a9-ce28-3943-a760-1ba60199826b | -19.94524 | -54.38292 | 2026-05-06 00:33:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 0f6f9a68-6573-313d-a446-6fe30f8cd31b | -16.49004 | -52.72327 | 2026-05-06 00:33:00 | TERRA_M-M | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 420b9b4f-44c0-33d2-bf98-5ba164d6cf8c | -13.72825 | -51.88269 | 2026-05-06 00:33:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 28651141-d174-3f55-9442-f38956969d7d | -19.94966 | -54.38713 | 2026-05-06 00:33:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2c7411cf-4872-378f-b103-d63123d69c25 | -16.11036 | -49.23466 | 2026-05-06 00:33:00 | TERRA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a325452e-7d0e-3157-a4db-763f5567e781 | -18.77795 | -51.943 | 2026-05-06 00:33:00 | TERRA_M-M | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| db16e14b-6dcb-3a00-b56f-82ffe7781b72 | -18.43978 | -54.71297 | 2026-05-06 00:33:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 46.5 |
| e8e7feb5-8881-3eb8-8481-c61cedd6134b | -16.42237 | -54.92149 | 2026-05-06 00:33:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 99c71fc6-93a2-3a21-ba32-b15742d1e2cf | -21.1866 | -49.20727 | 2026-05-06 00:33:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 15ff56a1-7073-3669-8677-d36ce6c7f684 | -20.21086 | -50.65599 | 2026-05-06 00:33:00 | TERRA_M-M | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| e6133611-2297-3839-bacb-501a4a870911 | -15.63265 | -47.91157 | 2026-05-06 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e610f51e-c86b-327b-bc22-2eb9f2238e4a | -18.78549 | -51.93238 | 2026-05-06 00:33:00 | TERRA_M-M | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f74ea567-f1e8-381a-a406-e8e7b311e304 | -18.07922 | -46.37123 | 2026-05-06 00:33:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 6effc86f-e377-3c0d-a088-a5dd6ad754e0 | -13.43967 | -43.85097 | 2026-05-06 00:33:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 445cc72d-da44-3ab7-8574-4641456127c9 | -18.50616 | -55.51695 | 2026-05-06 00:33:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 6f46d3fb-ec4c-3f13-ae62-84308b12a266 | -16.43046 | -54.90937 | 2026-05-06 00:33:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0b458d15-ee79-396e-938d-92929fc50bc9 | -16.15409 | -58.49424 | 2026-05-06 00:33:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 7e07be1d-b79c-3210-9125-9d08f84c20f2 | -16.42097 | -54.91064 | 2026-05-06 00:33:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| af5ba83f-6381-3b56-b87f-d521d8e788ee | -20.20948 | -50.64644 | 2026-05-06 00:33:00 | TERRA_M-M | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| 159c2aaf-7709-3616-b8ae-3480eb8f507c | -18.78676 | -51.94163 | 2026-05-06 00:33:00 | TERRA_M-M | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2221e079-e352-3b83-874f-7040b5c129d9 | -21.97866 | -57.59351 | 2026-05-06 00:33:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 3af493fd-c809-30c8-b3f0-b9bcc33144d8 | -14.06831 | -47.80219 | 2026-05-06 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6a35f8c1-23ea-338f-9d92-d91a4709f67a | -16.43184 | -54.92011 | 2026-05-06 00:33:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c868115a-8229-346f-a03a-df3e495feeab | -18.43017 | -54.71427 | 2026-05-06 00:33:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6113e115-358a-37f6-a686-3a4343fe2449 | -18.43844 | -54.70198 | 2026-05-06 00:33:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1897812c-1413-31f5-8090-4d4c74fb2127 | -18.49604 | -55.5183 | 2026-05-06 00:33:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| eacb3e88-3e36-3c8b-a281-76aa9093a139 | -17.80176 | -46.70663 | 2026-05-06 00:33:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3e430cda-c148-352e-812d-cfffd5c677dd | -14.06591 | -47.7873 | 2026-05-06 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3385f6b2-1324-3764-8976-ab57ea78130e | -20.22588 | -50.76072 | 2026-05-06 00:33:00 | TERRA_M-M | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 4fe8d868-4813-3ed5-b61b-73041e105bb6 | -14.13648 | -45.36395 | 2026-05-06 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a5b96322-5972-3813-9962-652c0a13fadb | -16.42739 | -57.27401 | 2026-05-06 00:33:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| b89c9dc0-f48f-33a7-be94-967ceac0e7bc | -17.80453 | -46.72345 | 2026-05-06 00:33:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| ab751371-be8d-3f4b-9428-4e39f180990a | -15.63025 | -47.89683 | 2026-05-06 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 74278c77-6794-35b9-a2c8-cc66d9a67c8d | -18.48393 | -51.68604 | 2026-05-06 00:33:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 814795e2-c492-3aeb-a5da-d74ac4b48d11 | -21.19587 | -49.20564 | 2026-05-06 00:33:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| af29effb-9533-3482-8772-3b02c2ac0be6 | -16.75902 | -51.87271 | 2026-05-06 00:33:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a07d7862-74b2-315e-813b-6224abefd153 | -20.22452 | -50.75123 | 2026-05-06 00:33:00 | TERRA_M-M | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a183b280-c54b-3080-a24f-68e19e1a3e0f | -12.27432 | -43.51147 | 2026-05-06 00:33:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 97951f65-70e9-3b86-8404-274b6b78b4f3 | -19.94832 | -54.37599 | 2026-05-06 00:33:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 45e96ac9-3799-3f65-aaaf-b9f5d7824ff3 | -12.34073 | -50.00698 | 2026-05-06 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3909ea27-7f14-30a9-b6a8-d811d681f9f6 | -11.4341 | -55.11042 | 2026-05-06 00:35:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 506fd7b5-6a8f-3706-b0df-b594f147f9cb | -11.44319 | -55.10913 | 2026-05-06 00:35:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cc607df7-f0ee-3e8d-82c7-97ff696a0366 | -13.69676 | -55.69358 | 2026-05-06 00:35:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 72348997-7e47-307e-836b-ec34204ad6a1 | -11.29837 | -54.03051 | 2026-05-06 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3acd7d1f-5944-391f-9433-8a6fdfef4d0b | -11.43284 | -55.10086 | 2026-05-06 00:35:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bc5804ab-2707-3ab9-b4c3-1c29952cf023 | -12.34384 | -50.02412 | 2026-05-06 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3c7575c4-8982-33b6-814d-a8d023f99785 | -12.49794 | -58.46962 | 2026-05-06 00:35:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b293eec4-6559-30b3-9cc0-f7cf19e31a98 | -12.48829 | -58.4869 | 2026-05-06 00:35:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 8b14fec2-683b-3525-a2b6-d50afddf69b1 | -11.44193 | -55.09959 | 2026-05-06 00:35:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0a8fb0a4-6a77-316b-94d7-4aedf3113ea6 | -12.50173 | -58.5015 | 2026-05-06 00:35:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6c23b152-4e69-350a-9f98-6def72e7ad80 | -11.12465 | -45.14566 | 2026-05-06 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| d5877ea9-be18-3767-9c10-6f774c4140a7 | -12.34204 | -50.01247 | 2026-05-06 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e0e61d98-858a-39ff-ae8b-c0300df98d1d | -12.33263 | -44.59708 | 2026-05-06 00:35:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| cc90ec38-66a8-3b81-8830-85183a57c226 | -6.21978 | -55.64872 | 2026-05-06 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eae464b2-e3b0-31f4-975b-b1781a5c5e4b | -13.9894 | -56.64759 | 2026-05-06 00:35:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dfb34cdc-c560-38a4-be2e-e0a7876591cf | -11.13883 | -45.13817 | 2026-05-06 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 32bfc562-4f68-327d-87cf-254a82db502c | -12.50948 | -58.46826 | 2026-05-06 00:35:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 9f3e652c-8f3c-3ece-a433-c7e07d076af0 | -12.49981 | -58.48536 | 2026-05-06 00:35:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 0c59d4c4-b6cc-3655-8e90-e31068e5eb1e | -12.51136 | -58.48396 | 2026-05-06 00:35:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 71627ee1-cf7f-3e7c-a26a-7bb0d44b01fe | -13.6954 | -55.68277 | 2026-05-06 00:35:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d3b00199-5dc7-31d0-abeb-7570f41cb5be | -9.24805 | -60.34235 | 2026-05-06 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8698f6d7-e258-3643-a41e-c9d9efaae2de | -12.46038 | -54.4519 | 2026-05-06 00:35:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 90e3a1f4-0b82-3c7c-96f1-83347e193f18 | -12.3538 | -50.02258 | 2026-05-06 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ca5e22cf-6a31-3a50-844c-63419135f5f0 | -12.26826 | -43.51786 | 2026-05-06 00:35:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 0f95dadd-ca0f-3ffc-a26d-9c29facb3868 | -13.98819 | -56.65406 | 2026-05-06 00:35:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 37b499ac-8841-3c25-bf8b-1160932b0329 | -12.34245 | -50.01865 | 2026-05-06 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 5c486bfc-b3ba-3a9c-b90e-588674e48f4b | -10.9332 | -49.43781 | 2026-05-06 00:35:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e08b0f21-3c31-35bb-86e7-da17f39581f4 | -12.34417 | -50.03032 | 2026-05-06 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 87fb501e-5522-3831-9bd8-29a010c26aed | -11.63823 | -54.16606 | 2026-05-06 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 2ce0cdc5-406e-3608-95dc-5d29ce4b3608 | -12.5033 | -58.4781 | 2026-05-06 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 36d4a200-df43-3a5e-b991-46a925e318bd | -12.4843 | -58.4795 | 2026-05-06 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 6d80872b-4d76-38d9-ba6b-54e1a1afa247 | -12.5031 | -58.4979 | 2026-05-06 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| d3a528c6-43a1-355d-bef4-287e20b92b64 | -12.5035 | -58.4582 | 2026-05-06 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| f39ee205-9768-35e0-9c1a-0b0f87e1b9fc | -12.5222 | -58.4765 | 2026-05-06 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 1e7dad23-e1f9-30a9-a178-593f4bacd46b | -12.5031 | -58.4979 | 2026-05-06 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 7b509b14-9433-3a57-937a-72ec4ba35d28 | -12.5035 | -58.4582 | 2026-05-06 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 140c9416-dfd4-30e3-96a3-c4f9a9b24e54 | -20.2237 | -50.6371 | 2026-05-06 00:50:00 | GOES-19 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| ac3b1d6a-21d7-34a0-8336-10e782be86b4 | -12.5033 | -58.4781 | 2026-05-06 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| f89d629d-c17d-3460-9339-5aac48465fec | -18.443701 | -54.709702 | 2026-05-06 00:56:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dd6aef74-d1b6-3ef0-adcf-bb9ac0373952 | -18.4879 | -51.679001 | 2026-05-06 00:56:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca3abb0b-24c0-330d-9b7f-465ddfcb3590 | -13.4392 | -43.8354 | 2026-05-06 00:56:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0244da4-d962-3625-86f1-a818bd5cc1d1 | -12.5011 | -58.4855 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 890f51a5-c2d9-3779-89dc-84e25d9aed05 | -20.208 | -50.642399 | 2026-05-06 00:56:00 | METOP-C | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd97ad83-7199-32df-b1c4-c09f46421b81 | -18.433901 | -54.7117 | 2026-05-06 00:56:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| abf85276-f461-36e0-a0f0-0d292925c4c7 | -16.423901 | -54.9077 | 2026-05-06 00:56:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
