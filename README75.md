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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 600ae58c-5b71-311c-9a7d-3d6aded9f2ef | -16.9203 | -42.1171 | 2026-09-30 18:10:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.5 |
| 9a0067a7-4e4d-343d-a9c1-f73bb607b6ad | -10.9653 | -47.2845 | 2026-09-30 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 609428a1-cbd1-32d1-a5d6-d52961655faa | -15.7863 | -44.6939 | 2026-09-30 18:10:00 | GOES-19 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 30f4a14c-9dda-3af9-a64e-7341b457145b | -9.7877 | -44.8058 | 2026-09-30 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 0ca229bb-fb86-3cdd-9623-1962a5c7316f | -7.9723 | -71.3443 | 2026-09-30 18:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 54b4368b-225f-3780-9e74-cea36fff6170 | -10.9463 | -47.2869 | 2026-09-30 18:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1358caf0-e508-3dae-a85a-3732dd8990f4 | -11.699 | -43.4416 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 310.2 |
| 1d2b1b2f-4b32-3c67-a13c-daae2cb33ecf | -5.4142 | -45.8734 | 2026-09-30 18:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 7adffd41-817d-3157-ac3f-cb886927090b | -12.514 | -43.0703 | 2026-09-30 18:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 149.4 |
| 9fc7d5cf-1949-3783-ac0f-a61c6263c91b | -11.7182 | -43.4386 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 245.7 |
| ef179a56-ccaf-3add-8502-174698585f09 | -11.3555 | -43.3526 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| f7ba09a6-21f0-3e83-b016-a29070abe0c4 | -11.4499 | -43.4329 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 246.2 |
| e7b7f600-67fd-3250-a227-5cbd8d437ba3 | -9.8613 | -44.9577 | 2026-09-30 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| da5f9b55-7773-3677-8d74-b10648ef8be4 | -9.8064 | -44.8265 | 2026-09-30 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f264715d-6d70-3a4c-b51a-3b14f9b3287b | -11.4682 | -43.4774 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 248.1 |
| 0854dfba-3b13-3b8e-a03b-1c76f4df89c2 | -11.4311 | -43.4121 | 2026-09-30 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 219.5 |
| fec5f58e-7985-305f-9ff6-28d3a6f654fb | -13.3835 | -44.0132 | 2026-09-30 18:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| c302baa6-f96e-3258-a3c9-a7eaa1c7c3ad | -7.9907 | -71.3441 | 2026-09-30 18:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 06a7946a-dc36-3500-b2f9-e7924345bdd9 | -12.4539 | -44.1702 | 2026-09-30 18:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 3178e4eb-1317-3528-b2cc-9e1be3313208 | -12.4355 | -44.1262 | 2026-09-30 18:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ac2915e4-ca7a-3403-82a6-69454ae06ddc | -6.3243 | -44.448 | 2026-09-30 18:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7eaeb7b8-e1e2-35d4-9b2f-c4faafdbecbc | -11.39 | -43.47 | 2026-09-30 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a278d92-24cc-3ba6-8886-502c8b898b88 | -15.25 | -41.71 | 2026-09-30 18:15:00 | MSG-03 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8744f424-7ed5-3cbb-b68a-5b841b0249ae | -3.11 | -50.25 | 2026-09-30 18:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a02703-7dfc-34e5-8c03-84394dce7243 | -7.29 | -39.15 | 2026-09-30 18:15:00 | MSG-03 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 28559b5f-4e93-3b44-9bee-6508206eefd3 | -8.14 | -43.49 | 2026-09-30 18:15:00 | MSG-03 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c9035ca-cb52-394e-b074-c967b700058f | -13.78 | -43.24 | 2026-09-30 18:15:00 | MSG-03 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cea48273-8af7-3c96-9915-0db87995e4a8 | -15.74 | -43.67 | 2026-09-30 18:15:00 | MSG-03 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d9e71d60-d3bc-3d44-917c-6c4d2bad3df3 | -5.73 | -45.18 | 2026-09-30 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e316f69-64df-338b-b0d3-f3f0403f2482 | -15.26 | -41.75 | 2026-09-30 18:15:00 | MSG-03 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8dc9a25-568b-3017-9b9c-ada5258e4c42 | -7.29 | -39.11 | 2026-09-30 18:15:00 | MSG-03 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 30121769-4a42-3aba-bb1d-980e91a6a097 | -13.56 | -53.2 | 2026-09-30 18:15:00 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 769ddfb2-61b7-3440-83a8-0bde31857c7c | -9.9 | -50.16 | 2026-09-30 18:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1b424fd-d5d8-3206-9f3b-89dad64fcd9f | -4.26 | -50.7 | 2026-09-30 18:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d967f52d-0315-3317-a5b3-99cc4ca7900a | -13.78 | -43.19 | 2026-09-30 18:15:00 | MSG-03 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d320153b-258b-386f-b231-a86b39473cf0 | -3.11 | -50.31 | 2026-09-30 18:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1075fc3-555e-318d-9cdc-492e637e93a1 | -5.76 | -45.19 | 2026-09-30 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1ef9ab0-4c49-3bc3-a489-5a5fe3f5ceec | -5.73 | -45.14 | 2026-09-30 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69e5e875-c86f-3eb9-9bc6-9e139edee053 | -4.26 | -50.81 | 2026-09-30 18:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0819c85-da1a-3637-858b-ca19845f3007 | -8.21 | -45.48 | 2026-09-30 18:15:00 | MSG-03 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47da858e-6059-3992-9b1d-a62098445e9f | -4.29 | -50.76 | 2026-09-30 18:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7364127-96b0-3c1f-b6f7-eb2842ae4624 | -15.22 | -41.7 | 2026-09-30 18:15:00 | MSG-03 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61c984d1-d522-39ae-8b48-dadc8c2d5eb0 | -5.76 | -45.14 | 2026-09-30 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf7dd07c-3d60-3721-b887-f8623a8638b2 | -4.26 | -50.75 | 2026-09-30 18:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87fb5ec3-9b46-3372-960e-e91068e2c324 | -10.5197 | -45.3784 | 2026-09-30 18:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 2709c50d-189a-34dd-8576-b4c24394a01f | -10.907 | -43.8433 | 2026-09-30 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5d570213-94fb-3f02-bde7-d880f6867b2a | -10.2843 | -44.6274 | 2026-09-30 18:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 07d37ee9-c66f-323a-a814-bbc0a78873a8 | -11.699 | -43.4416 | 2026-09-30 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 2cf30d66-b480-341e-b76c-1862f434a02d | -11.7182 | -43.4386 | 2026-09-30 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| abad92de-3514-32f5-a1c1-4ac7b0d0a388 | -11.6789 | -43.4921 | 2026-09-30 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 909400a3-0b12-3e81-b9ab-4feb1947d98c | -11.1954 | -44.85 | 2026-09-30 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 21f78629-8b58-3fce-a7c4-5f9e055542a9 | -12.5135 | -43.0943 | 2026-09-30 18:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 203.1 |
| f19adfe8-1cce-37d1-a4c5-c566f15679fe | -9.7687 | -44.8082 | 2026-09-30 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 13dfe962-a4c1-332a-8fd3-3129dd22aeac | -15.2234 | -46.157 | 2026-09-30 18:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 4cd3107e-433a-35c0-85e4-22fd4f076b7f | -15.1348 | -44.0412 | 2026-09-30 18:20:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| cdb6c91d-e186-3cc7-abcd-4c0adc6cb332 | -5.7563 | -45.152 | 2026-09-30 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 578.7 |
| 35427de4-3608-3e78-a87f-2c166e53677a | 1.8953 | -55.5841 | 2026-09-30 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 58b19245-f223-350f-b19d-28602e9b524e | -5.4142 | -45.8734 | 2026-09-30 18:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3de0b6eb-97a8-3d4a-a641-236a5e61009e | 1.8219 | -55.6444 | 2026-09-30 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| eda4769c-61e8-3b0a-88d5-26b66e1e21d1 | -12.4539 | -44.1702 | 2026-09-30 18:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| e4423b85-2c0d-3a2c-a154-9895a0520322 | -13.384 | -43.9895 | 2026-09-30 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c257b07e-62d9-3fa1-a4fe-6e540c11d997 | -15.9476 | -39.9576 | 2026-09-30 18:20:00 | GOES-19 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 141.0 |
| f6bec77d-4882-3976-946e-10325721d807 | 1.8587 | -55.5648 | 2026-09-30 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6800d431-9621-30ca-b52e-75b923f32f90 | -13.3835 | -44.0132 | 2026-09-30 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 603c186d-0317-3c31-987a-cfe530f9959d | 1.8403 | -55.6442 | 2026-09-30 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e73e7a99-970b-3d49-90e5-3cf2ab4c6593 | -12.514 | -43.0703 | 2026-09-30 18:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 95fc8a79-e12a-32a9-874e-df9cc61dae47 | -15.1456 | -43.5847 | 2026-09-30 18:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 114.9 |
| e2548d2a-18d5-3fb2-b917-2cc23e77b562 | -5.7561 | -45.1747 | 2026-09-30 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 341.6 |
| d90a35fb-dec5-3a20-8293-e002572569ad | -7.9907 | -71.3441 | 2026-09-30 18:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 3626b2f3-0e59-365e-a1fc-161dbefe890f | 1.822 | -55.6247 | 2026-09-30 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a560c6b9-8d88-3bab-9f39-ae2b65af065d | -11.678 | -43.5396 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 136f15e1-2ea6-357c-a07d-9a0f9c1074fb | -13.384 | -43.9895 | 2026-09-30 18:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 4942b48d-fdd6-3372-9930-687d9487c8cc | -13.3835 | -44.0132 | 2026-09-30 18:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| abd96ce3-f662-3af4-88ea-25d71dccc87f | -15.1348 | -44.0412 | 2026-09-30 18:30:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 181.9 |
| cfdc88d2-217b-37e9-8cb8-3b62597f62da | -11.6588 | -43.5425 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 320.8 |
| 96d1fd8a-bd92-3021-a584-8ecc0b2e2fb3 | -10.5197 | -45.3784 | 2026-09-30 18:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b0a94831-3c40-3952-afa7-d80bd6c7cda1 | -12.5135 | -43.0943 | 2026-09-30 18:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 307.3 |
| 7bd2c902-1f50-3c44-af11-4ac4df88a215 | -5.7376 | -45.1533 | 2026-09-30 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7a241aca-cbc3-392e-ada0-d0c366ac2b6d | 1.9793 | -50.84 | 2026-09-30 18:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 72ddc8c1-c709-3c5f-b2ee-f36433754074 | -11.6592 | -43.5188 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 354f57fa-b813-3dbd-a4fe-e715d611e50f | -13.0017 | -44.7357 | 2026-09-30 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 6c87d8d1-4e5c-35f1-8068-6036ba4ce1a4 | 1.8403 | -55.6442 | 2026-09-30 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| fe360432-461c-3b8f-9973-d0193fca7c94 | -7.2721 | -72.7177 | 2026-09-30 18:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 0c2328e0-a141-3657-ae20-28ccb02fc9ac | -11.6596 | -43.4951 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 2b23c421-b002-3fef-8b49-174ca68fdb71 | -11.1954 | -44.85 | 2026-09-30 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4d7ce6fc-a32d-3ff6-adac-3e67a2e9f59c | -4.1227 | -46.878 | 2026-09-30 18:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1799cbb5-7113-3870-9647-29e22a194b76 | -11.6986 | -43.4654 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| e8832e60-6b21-319a-8439-da6ee3ac5b51 | -11.7182 | -43.4386 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 180e3440-05ff-3481-be1a-ff467cc8359d | -11.19 | -45.1736 | 2026-09-30 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d80cffb6-cd95-3dd1-ac46-0f7517aa514e | -11.6212 | -43.5011 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| ea9a0c07-7c85-3d86-9767-665a70d34fa7 | -9.8064 | -44.8265 | 2026-09-30 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b8cc9fff-01bb-341f-95a8-151ac904ce03 | -11.6784 | -43.5158 | 2026-09-30 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.1 |
| 72c6957d-c058-3853-96b6-c8447ae76aaa | -11.2095 | -45.1478 | 2026-09-30 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 276c0a09-a28b-3995-8a47-b0c785d93802 | -6.1894 | -44.8472 | 2026-09-30 18:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a9b57e19-6c89-33e6-ad76-afb681f06136 | 1.8587 | -55.5648 | 2026-09-30 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cee2d446-ff47-354c-9903-37ee5992e386 | -10.7115 | -45.2845 | 2026-09-30 18:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| b2d92cd2-121a-3ef7-ac22-14eae1aa1232 | -12.514 | -43.0703 | 2026-09-30 18:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 97d07815-adc3-35f7-bdc4-ba137e2c9c87 | -12.4346 | -44.1733 | 2026-09-30 18:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| ce4b363f-c736-3b4d-9851-7bbe78a2bb6b | -10.7112 | -45.3075 | 2026-09-30 18:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 283.2 |
| a26355d1-2e2e-3d62-92f6-7449cd0b1afa | -12.5329 | -43.091 | 2026-09-30 18:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 117.8 |


[Clique aqui para ver as próximas entradas](README76.md)
