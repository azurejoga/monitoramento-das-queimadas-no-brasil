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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecf753f9-b8ec-3195-ba15-ae97d0929639 | -5.56215 | -46.2771 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b7e5af9b-ef93-3547-9146-66815e0f530f | -7.05171 | -42.00062 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3b00d3d-f5f5-396f-854f-8e16961b8633 | -3.26558 | -43.05447 | 2025-09-18 04:12:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 396bf454-a9d0-34d6-b56c-5cc4b545e182 | -4.10252 | -40.4874 | 2025-09-18 04:12:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f7f0359d-32ba-3048-808b-9234e6b46b46 | -6.61316 | -45.63112 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b78d081-9afc-3b21-8a55-adc3f22b9265 | -4.65137 | -47.56177 | 2025-09-18 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dcd81b5-9433-31b8-af53-5d613d1c0985 | -6.48123 | -45.99802 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 314b4dc5-47f9-36a2-ab03-8a39bd88cca8 | -6.53371 | -43.93315 | 2025-09-18 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4284b07d-f8fc-3d5d-a048-b0e138a62518 | -5.88062 | -45.74942 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b97994fd-2ffa-3269-9c7c-938d7fa81ef7 | -6.91985 | -44.81069 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2eedaefa-c250-31d0-8b64-45b24119c8f0 | -4.68964 | -41.9516 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ffdf8ec2-a380-3e4e-9628-a6170107d149 | -5.87387 | -45.88076 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 801b2290-0b0f-38ed-beec-094e8106a1ba | -5.80777 | -45.91306 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c00cfbc0-90d9-3a3d-badd-90baf0c6a038 | -7.00354 | -44.6012 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ace25ef1-047d-3894-b0dc-7f54066c6937 | -4.3443 | -40.73668 | 2025-09-18 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7337617c-1b54-3327-a1d7-dba7e9c9e69f | -5.79031 | -43.7578 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85de73b4-c0bd-3561-8943-6c4edc40c86c | -5.81364 | -45.91271 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b906e7b-d80b-3d7b-a075-ff1f630fac72 | -6.52633 | -44.1304 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12152527-4003-3053-b5c0-21b34771e95b | -6.33467 | -44.24137 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81d90964-3005-3bd8-ae94-8113d925ff3c | -5.87321 | -45.88479 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db98ebc0-a11e-3f29-977a-f005b0732ca1 | -2.92139 | -48.31282 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 41afedec-7f7d-39ec-9db3-3ba7e615f2fa | -2.92074 | -48.6706 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc2cb5e5-cea9-386c-a429-16ab5dc0ed3a | -6.41478 | -43.35455 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81343ff0-d91b-32b7-b9cd-8f766bcb7fba | -4.62181 | -47.02342 | 2025-09-18 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e99b6dd-6d88-3ec9-9615-a69ebeb10108 | -6.26248 | -43.4579 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09d35000-a8a7-3880-8b55-1957a9bad8b4 | -3.2689 | -43.055 | 2025-09-18 04:12:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bca9125-1489-35d4-b63f-345c55dbb204 | -5.8931 | -43.34584 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df556b1b-2493-310e-b511-19e213415172 | -5.82416 | -43.8851 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a86d62e-56c7-30cb-a336-44f714aba6f2 | -6.95205 | -44.56688 | 2025-09-18 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c2a51c5-8a38-3ec2-86b4-09ab97540105 | -5.55711 | -46.28497 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f23847f-2e3d-3a7b-9300-d889861ad711 | -7.22734 | -40.17794 | 2025-09-18 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38701a84-0c76-3361-952c-86d80cf7eaba | -5.07925 | -41.1696 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ddf91845-0d0b-3cda-9f1f-838602a325e8 | -5.36899 | -43.00813 | 2025-09-18 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 36d004be-8b26-3589-a9dc-bff8333cfb08 | -0.90713 | -47.54574 | 2025-09-18 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ef6a40a-3444-315a-bba6-2a21c2cbc1ba | -7.00634 | -44.60529 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f50c5dc4-fded-3121-bb72-7a5d048d7276 | -7.06123 | -44.35027 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 080064e4-cc75-37d3-a0d2-75141d90ba43 | -5.79979 | -45.71279 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3fd8166-7e5a-39f6-a7e4-b1ddbc2e5ca2 | -4.6226 | -47.01852 | 2025-09-18 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44f8eb06-ff5a-35d2-b061-896dc4e87ba2 | -5.22271 | -45.18137 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 85cfed55-6ca4-3240-8fcd-3828bbda61df | -6.8941 | -44.77634 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad42590f-2b07-310e-8d09-aaed6ef06ff8 | -3.10785 | -46.77184 | 2025-09-18 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b9bf029-0455-32e0-b3b7-d82a3a70a4e3 | -6.67438 | -45.30832 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d142bf6-a290-3622-94af-6c41b14aa21e | -6.4873 | -45.71672 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05fd83d4-129a-30ec-9ea4-8243f0ecace1 | -5.7693 | -46.15363 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62ebd260-91ef-3d65-94fb-37ca3b22765c | -5.74985 | -45.43745 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53dc1359-5010-3778-b660-004786292e44 | -3.79828 | -47.57983 | 2025-09-18 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9687f02-4fcf-332c-b631-d4cca208a17c | -6.21368 | -45.12379 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13705040-ac35-3028-bba7-8063f4953497 | -5.76597 | -46.15588 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd195618-8741-31d3-8c6b-a5da919d0c70 | -6.50704 | -39.5045 | 2025-09-18 04:12:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fd0cfd68-315d-3225-b101-92b6c2f9f1d8 | -7.05451 | -42.00468 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4f8b627-1ffa-38a0-aae3-6adc88a61121 | -6.9557 | -42.44122 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb432b75-6a0a-36c1-84b1-907e3221c8a0 | -5.08658 | -41.16705 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27ed3ab0-df4b-3b1c-8087-3c3c9963c580 | -6.30231 | -42.38556 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de166827-8d5b-3aeb-a727-10575e07fdac | -6.18369 | -41.2286 | 2025-09-18 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86371ccb-8f58-3c4b-bd8b-568ed846a65a | -5.49088 | -45.40573 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2254f911-177a-3be0-9e21-11c1e633008a | -6.63729 | -44.66936 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d663e1a7-ba9b-3720-92ff-02b9357290ca | -4.91613 | -47.85719 | 2025-09-18 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51eed901-add0-3791-8f90-2b044105b089 | -6.39489 | -43.33013 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60b4ea94-5076-351e-9fa3-feee89976d1c | -2.37785 | -47.72093 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58f6de48-aa0f-37c5-8ecf-0331c05e8b65 | -3.843 | -40.3795 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd3eda18-880f-33cb-bf36-1bcf0b2149dd | -6.64067 | -44.66991 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 80a8c6fc-456e-3cbb-a5e9-60cce478f113 | -5.33077 | -41.86861 | 2025-09-18 04:12:00 | NOAA-20 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ac3972f8-b817-310e-b4cd-6c1ee5bc14e2 | -6.98497 | -44.44741 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6807a0d5-ee8c-3bb1-8e1e-0745f876120b | -6.21164 | -44.28821 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 834cd6c7-3431-3c0b-b928-fa585ee27224 | -5.5403 | -42.17678 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34f94484-2740-3abf-ad21-fcefa57c545d | -6.40321 | -43.36337 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0f74947-b527-35fc-b4e5-276e2eb89ee6 | -6.92324 | -44.81124 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8095a401-547c-3c82-ade8-1a7c9e177726 | -5.08995 | -41.14529 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bfc367fd-8b07-3ead-a31b-29f7323955bb | -3.79886 | -47.57632 | 2025-09-18 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3f57120-d447-3fc6-a204-f0b6644d29c7 | -4.33091 | -48.38733 | 2025-09-18 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f6caada-2561-38e4-824a-fc6c98de5704 | -5.87058 | -45.90101 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f66e7a1e-1bbc-38fc-adcd-c080b93c432f | -4.80852 | -42.72866 | 2025-09-18 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bcd8718c-0195-3d9e-b51b-dec0e6fa2a1e | -5.87678 | -45.88536 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4354c75-a861-3d62-8bc6-684cc2c9bfa5 | -6.6119 | -45.63897 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53c40ec1-441c-383e-98ac-7955aa3e1a9e | -3.18975 | -54.98174 | 2025-09-18 04:12:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f828ce0-0d89-36f0-b394-96c958f9207c | -6.29954 | -42.38155 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7440767-1270-3ccf-85b3-649a41cf3bee | -4.09908 | -40.48687 | 2025-09-18 04:12:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c34fef4f-adcb-3b80-93aa-0f035caec55e | -7.06735 | -44.35492 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c72d0079-f8fe-308e-a9ea-30fd76d0a00e | -6.1653 | -44.49041 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dfb9755-5838-31be-8c12-4b0e826e6519 | -6.87218 | -43.96231 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c7335ec-e526-375e-81b4-d594ae387b94 | -5.87125 | -45.8969 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580b50ee-7705-3fce-b6ff-e82d03ab74da | -3.25781 | -48.45723 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f9afd72-e0aa-32d3-9b1c-e7aad6d900c6 | -6.38994 | -43.33999 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc186225-c1d9-386c-bade-fc01e49c6e4b | -5.63422 | -43.88428 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 784d5f77-97b0-3c95-99c8-60f28303ea02 | -2.37848 | -47.71711 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61097bb9-b880-35ca-8c1e-6b81cd0f69b0 | -5.59671 | -45.35781 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f86d987-9116-3ad0-a784-6764d9dfd6c5 | -2.25784 | -47.84406 | 2025-09-18 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20b41217-f97a-3dfe-bd51-e03994e00d3e | -6.01108 | -44.33334 | 2025-09-18 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b68f2e9-e957-3fdb-b627-d177e5fecac5 | -5.5365 | -42.20116 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 925d85a1-3efc-36b8-9b0e-6ff8277616c5 | -6.42249 | -43.34869 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12b87928-ec78-3e74-b41f-e692a3808d80 | -6.39103 | -43.33307 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a4fedb7-e686-3d7c-8dc6-6f624a9fdf9c | -6.95674 | -44.77562 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7256d0cc-0f64-372b-8d47-c1be140151db | -1.75788 | -48.05125 | 2025-09-18 04:12:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33022561-7bef-3daa-9d26-e8d2e22fa105 | -6.4148 | -45.85155 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7d9b86c-7914-36e3-827f-d05eaeace444 | -7.07233 | -44.3667 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0660fc15-4900-3db6-ad16-1e6a8fa91174 | -4.59941 | -43.77122 | 2025-09-18 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bfeaa88-2223-3847-9e1c-a80536ebeb09 | -3.84417 | -40.37202 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3a5945f-f26b-3f51-868b-8134e26221b1 | -7.05116 | -42.00417 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2de7a9d0-12eb-3ceb-ad12-6fa6d900dcba | -5.98299 | -45.85602 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 996ae725-895b-3cb1-b39d-423874d44529 | -5.82012 | -45.91795 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README13.md)
