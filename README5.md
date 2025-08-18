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
| 627f86bf-6789-382f-a174-1b1fb074ea28 | -8.0476 | -47.683998 | 2025-08-18 00:58:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99882cb5-71c6-30f2-a273-b5899c231fe6 | -11.8551 | -51.5886 | 2025-08-18 00:58:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3673d3ff-74cd-3156-815b-d77e51812dd9 | -13.4716 | -47.070801 | 2025-08-18 00:58:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e167dd9a-3e28-3232-8ad9-1f4acd51b35a | -12.543 | -48.500801 | 2025-08-18 00:58:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73af150a-d7ed-3e7f-9a6d-9574f8adaa60 | -3.9952 | -42.565601 | 2025-08-18 00:58:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ce0aaa0-05d0-31b1-8e6d-f46dfff9cd9d | -11.3164 | -55.206799 | 2025-08-18 00:58:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be0d6084-b51c-36fd-8d88-fa8f69ad7215 | -6.428 | -44.771099 | 2025-08-18 00:58:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed6cd0a-9828-37aa-b990-2e6ea45c6306 | -14.9841 | -54.780399 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd2172cb-b277-3c02-a45b-15499b1b3d2b | -14.9822 | -54.771198 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78561aa3-44ca-339d-8e18-3f070968f1fc | -6.5726 | -44.4827 | 2025-08-18 00:58:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb26f9a5-d641-3160-b4e1-74a019791bf7 | -17.400999 | -42.6115 | 2025-08-18 00:58:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 726165ff-0aa6-3b70-8f0e-21a9c47c6990 | -13.4693 | -47.061501 | 2025-08-18 00:58:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 06210c8f-1e96-35bb-bfde-3d8ae9bb203e | -16.7957 | -50.089901 | 2025-08-18 00:58:00 | METOP-C | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7e75a80-cf3f-338b-a351-b1cb6c1c9640 | -13.2575 | -50.770699 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 415239b2-47e4-3d67-b9ca-5929b8a98747 | -16.239901 | -50.140202 | 2025-08-18 00:58:00 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41ae0d30-6181-3f75-a4a0-0a8f61042d6a | -15.0056 | -54.7855 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b10eaf50-17a2-370e-9add-cc83d2a2a39b | -3.5978 | -47.5303 | 2025-08-18 00:58:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d419f591-a2dc-38f8-a798-e7f47b4867dc | -17.1784 | -46.216999 | 2025-08-18 00:58:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 356ac66c-815a-3c8a-9066-283a1103c720 | -18.7845 | -49.074299 | 2025-08-18 00:58:00 | METOP-C | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3be113-5b56-32c7-8ce0-eb998e0f048b | -13.2363 | -50.768299 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f32ce8fd-8258-3c66-a629-e0e086e992a3 | -8.0451 | -47.673901 | 2025-08-18 00:58:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccf7e41d-cb51-3a67-8f2f-34788e449c42 | -6.5779 | -44.462898 | 2025-08-18 00:58:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca42df6c-4222-35ee-94cb-ddecd95110e7 | -18.5487 | -43.983101 | 2025-08-18 00:58:00 | METOP-C | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e4ebf64-6747-3982-9efd-5f30008288db | -12.9817 | -56.855099 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51067b42-055d-382a-a921-0c8d911a1d0c | -8.8018 | -52.083401 | 2025-08-18 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5557e6f7-6257-3df6-b3e3-98e8edb58238 | -13.2347 | -50.7612 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9c33186-a699-3c2a-a72a-601dd7cba976 | -17.391399 | -42.6143 | 2025-08-18 00:58:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f2ca8905-34ad-38cc-8602-47db743244ef | -8.8002 | -52.0765 | 2025-08-18 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a601f2-e871-30ea-a587-ec876ec5bc1b | -6.4419 | -44.785301 | 2025-08-18 00:58:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82e129cc-4055-31bf-9dfc-d19b311269b5 | -6.1657 | -47.283199 | 2025-08-18 00:58:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca402b7-4da9-3411-aae6-29e764dd1fc7 | -12.9891 | -56.841599 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80db461a-cd88-3825-b1e4-c58e0bc72d7b | -13.2607 | -50.784801 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2fa2b146-525d-39f0-85c5-0eae0b41c3db | -16.7973 | -50.097 | 2025-08-18 00:58:00 | METOP-C | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a3f86cda-d68d-3734-a6cb-0e6e0419b5e8 | -13.2559 | -50.763699 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76cd05e0-b4ca-3c3e-9340-34f584572a40 | -12.9794 | -56.843601 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a722ad6-2590-3493-a8ce-d9f31a4ed5c4 | -17.1709 | -46.228901 | 2025-08-18 00:58:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 16fb3a14-d16e-3fbe-a7b2-13707e5efd69 | -15.0075 | -54.794701 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88f28ca4-26ff-3df9-8103-accabb7fd534 | -8.1183 | -50.022701 | 2025-08-18 00:58:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26cd7b77-f052-3603-adcc-28492160fe64 | -19.1541 | -47.0177 | 2025-08-18 00:58:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 804826f7-6bc1-3d26-ab4e-1b482e951466 | -6.5629 | -44.4851 | 2025-08-18 00:58:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b3c86b8-ff2e-33c9-95f6-7e6714bffadc | -13.2281 | -50.777599 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91d08f14-78a0-3f73-92e1-d2edd850b61f | -15.5049 | -48.519699 | 2025-08-18 00:58:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 989e8c1a-b65e-3a26-b4f8-dbdf59b3b8b6 | -13.1317 | -57.1408 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c18fad2c-da4d-3f94-8e6f-031d85bb69ba | -16.2383 | -50.133099 | 2025-08-18 00:58:00 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fd87824e-3ede-31b3-a3c7-b112e763ba88 | -26.006901 | -52.064899 | 2025-08-18 00:58:00 | METOP-C | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b8a842c-7f93-378e-a52c-eee37261af1b | -7.5625 | -45.443802 | 2025-08-18 00:58:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c396d538-3304-3764-98f2-50a709f900f6 | -13.5944 | -46.98 | 2025-08-18 00:58:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d7c57497-dd1a-327a-95c6-b0f587b17e30 | -3.9983 | -42.537201 | 2025-08-18 00:58:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3c616c07-e46e-3a0c-804c-400ca1464861 | -12.9914 | -56.8531 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb6aeb5-a830-32a1-9788-706bd9092e25 | -17.096201 | -49.8671 | 2025-08-18 00:58:00 | METOP-C | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8246330e-4677-38a4-9a5f-3b42d0401c4d | -7.9162 | -51.372398 | 2025-08-18 00:58:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d6449b-439e-3d32-9e39-45098108100c | -13.2265 | -50.770599 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83491ef8-2a2a-3c00-8e3b-4a4c25e36be9 | -15.5067 | -48.527401 | 2025-08-18 00:58:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c707c6ff-f641-3eea-af68-efff9e6814a6 | -22.850599 | -55.101898 | 2025-08-18 00:58:00 | METOP-C | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b4e6382-3ad3-3294-aa3b-a06c8dc4736e | -12.9989 | -56.8395 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3ac970-3ebf-342f-a670-15a6278120ae | -14.9958 | -54.787601 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5c3e65ed-597a-34b4-af73-21e08168120e | -17.1663 | -46.210098 | 2025-08-18 00:58:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0f60ac3d-e8b7-3211-9ea1-799caab01572 | -13.2331 | -50.7542 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3137af8b-5102-32a3-ad21-9b9f437151cc | -15.0095 | -54.804001 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8484d77d-cce0-3679-bfcc-d756bd4425f3 | -14.9939 | -54.778301 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3080b6-dee6-37b8-90f5-a19caba3dde1 | -13.5954 | -47.753899 | 2025-08-18 00:58:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1db90f5e-ecce-3da2-a6bd-f75abc256f98 | -14.9724 | -54.773399 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec661895-107c-3a31-ae3b-f5109e14eac4 | -14.9705 | -54.764198 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa6a146f-694d-3b20-bbe8-964d15701ba3 | -6.4377 | -44.7687 | 2025-08-18 00:58:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cee633fd-f4b7-3b39-8364-4525577347aa | -13.0208 | -56.847 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 677bef82-010a-35b0-bc4c-3c2a111af09e | -11.8453 | -51.5909 | 2025-08-18 00:58:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a59789f1-5d3c-30f8-9520-e18c88c687cf | -13.2249 | -50.7635 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9b05fd-cba5-38f1-bcba-83e7aea6237e | -13.5933 | -47.7453 | 2025-08-18 00:58:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 357b8194-c276-36ef-be3c-7b65bc6b4455 | -13.2413 | -50.7449 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37b4b90b-af30-3107-bd1a-714fe43e3a3c | -13.2313 | -50.791599 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b96c4e36-995b-38b9-9e40-f9ba6c24ea3f | -17.094601 | -49.859901 | 2025-08-18 00:58:00 | METOP-C | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5e11191-9d7b-34dc-8288-2b9296e776d4 | -12.6416 | -46.893002 | 2025-08-18 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15b43925-edea-30c1-9914-63a1cef79603 | -9.8719 | -44.693802 | 2025-08-18 00:58:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95336fb7-69be-38e9-8a21-fae156d34d47 | -10.2796 | -48.373699 | 2025-08-18 00:58:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21be9eac-4536-3351-9bdb-4f6ea2fa4c9f | -17.1686 | -46.219501 | 2025-08-18 00:58:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9240db15-eb2f-37a6-ba83-c3577914112b | -8.1165 | -50.015099 | 2025-08-18 00:58:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab2b0617-7190-3224-910c-3320fa3ba8f3 | -17.3955 | -42.6297 | 2025-08-18 00:58:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 15e08f54-0a6d-3935-a42e-6df056e5904d | -13.1464 | -57.1628 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7aef0632-fa27-3337-b5d1-3159aed7dab3 | -13.011 | -56.848999 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c717a079-c026-3337-8201-f89746916261 | -6.5586 | -44.467701 | 2025-08-18 00:58:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d088b2c2-a698-3c48-9384-2855b826623c | -6.1522 | -49.872398 | 2025-08-18 00:58:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 735cd286-7f91-34cd-a1d4-b7e0fa323b6d | -16.2367 | -50.1259 | 2025-08-18 00:58:00 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9f4d03-d1b1-302b-8165-cdd34cadcdbd | -13.0087 | -56.837502 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4e43cb7-7fc2-36d9-80ec-9ed1b5813f32 | -14.9803 | -54.762001 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12e30dd2-2bfa-31db-bf76-531eef5f05fb | -19.1464 | -47.0285 | 2025-08-18 00:58:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb607b90-04e9-3118-97a4-8323cfabb2fb | -13.0012 | -56.851002 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7307b179-5f36-3467-8c14-fe528f952aad | -13.9891 | -48.102299 | 2025-08-18 00:58:00 | METOP-C | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 653867c7-6957-3376-a714-c8f67c158063 | -12.6319 | -46.895401 | 2025-08-18 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec341475-6825-397c-a065-e1bff44dde9e | -11.356 | -55.3913 | 2025-08-18 00:58:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08caf3e2-e662-31e2-bc24-1c005e01bc4d | -9.8816 | -44.691299 | 2025-08-18 00:58:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7eef947c-2971-3761-a5dc-15e1223a0370 | -13.2297 | -50.784599 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1b5e04f-426e-302e-ad7c-08761491baf4 | -22.146799 | -50.023701 | 2025-08-18 00:58:00 | METOP-C | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e44afd6f-2c61-3919-b0f0-bd3d6960a427 | -3.9887 | -42.5396 | 2025-08-18 00:58:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b658f82-eee3-3ec8-8e20-382bb9cd221f | -13.2525 | -50.793999 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31286745-9dba-3362-bfb1-8207aeae64a4 | -13.2509 | -50.786999 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41623fb9-049e-3ea7-a185-81b034f7efbb | -23.3158 | -46.883999 | 2025-08-18 00:58:00 | METOP-C | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fa5472a-d49a-360b-a8c8-4cf854bbae8b | -17.4051 | -42.6269 | 2025-08-18 00:58:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9a852a4-276e-36cc-b45f-19808fcdb281 | -14.9997 | -54.806099 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e88ec634-b8fe-3742-9baa-619bbf2aa641 | -13.1342 | -57.152802 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75469ee8-a606-3603-9fc4-65bdf0894297 | -19.1873 | -46.5504 | 2025-08-18 00:58:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
