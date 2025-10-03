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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cc946ba-6a71-3b56-a381-d4acc5268cdf | -5.7956 | -45.75583 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00acbcff-5c60-3133-9c60-91cd80d51c1f | -7.7175 | -46.6256 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8c83cf4-b898-3d58-b94e-0ed2afffa97e | -11.85308 | -44.95844 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c129c2e1-93ff-3285-8b7b-76e0aeeaa9bf | -7.52665 | -47.28949 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d99ab309-4e5c-3ada-a8b6-f96e4b2a8965 | -10.90291 | -46.71778 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb9b2c66-d08e-3ddf-8848-560a878ae6a7 | -9.95169 | -48.77842 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fac873c-00b9-3f1a-8e1e-e271ce226d3d | -7.75974 | -46.28171 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 58fe5c7a-69ba-3315-886c-0e912286ce83 | -8.82822 | -46.77705 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d691f772-5901-376b-957e-9140801246f2 | -10.84031 | -46.59513 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97af7e69-b519-32d2-974c-b4aae7672c6b | -11.84083 | -45.0452 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3046642-396a-31f0-a175-560162261f30 | -6.68361 | -42.8354 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 369a889d-c5e9-3928-a844-765595117645 | -11.5564 | -46.99931 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d9c865c-9db2-3464-b820-08003114ba0c | -11.62306 | -47.98981 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0947e2ca-4c30-32ac-a73d-cf5334f3a7d3 | -11.49407 | -45.00897 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc32bdae-e7af-3070-990a-fb79eea039d4 | -10.25273 | -44.94363 | 2025-10-03 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9500586-2f9f-3c61-900e-ddd3a447a2f6 | -5.92521 | -44.26448 | 2025-10-03 04:32:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 086387cc-feef-332e-8045-cbfeb3e34fd0 | -8.59316 | -44.78408 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aea1bf3f-d3b8-3d5b-b8d2-7ab52b2612b7 | -7.44872 | -46.98192 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c96d8af-3f5e-33a0-bd83-ee3a92c7547d | -6.23576 | -44.23689 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91e5616b-53cf-3c08-8a75-be41842c7cd4 | -6.55803 | -43.88812 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41295e50-3743-30b4-9f4e-4defab5647f3 | -11.32117 | -49.01044 | 2025-10-03 04:32:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 640bbc57-164e-3f3b-8759-c4b0b8a9f025 | -11.29509 | -47.8326 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff4c7793-2c4e-37b5-8d73-11f8c58b2a3e | -8.25482 | -50.57385 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b62d13c3-8e7b-3619-b7ed-fcd64cd55ea5 | -11.59857 | -47.66614 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f3207d0-64cc-3025-89cd-8c80110bc7d5 | -11.09172 | -47.80433 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4b1b79b-164b-31ac-9bfd-ce6f4c483db8 | -9.90804 | -43.7203 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 5068fad5-5034-33ea-b92e-ae98d00149ef | -8.98938 | -48.78461 | 2025-10-03 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3a7c43c-ebe5-3630-9079-0095c789b5de | -8.75221 | -47.33352 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e8db41c-2b55-3684-bd23-67b901a07f92 | -7.49991 | -48.85731 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 875ac8e7-8873-3f65-9c71-894719730a55 | -5.78194 | -45.7538 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa89d771-fc07-347e-8e29-7cfd3fcd455a | -9.9425 | -43.76196 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 41c12c40-3eee-30d0-8561-4d5c062f09b7 | -7.24787 | -49.40541 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47ab3fe4-d066-3f98-bc2b-717b526071f8 | -6.68154 | -43.70973 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d40cb26-8c5b-35d5-bf21-5a39738e1b95 | -9.95471 | -43.70609 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fd7eee4-c610-3841-9c12-c0b5126ee5b8 | -10.63928 | -49.06917 | 2025-10-03 04:32:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7287a8e-5516-3390-b721-4173bb773831 | -10.00637 | -50.23838 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 159a7cab-1492-3ffe-bc41-63097f419214 | -7.74946 | -46.2577 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 308436d1-69e3-3d8e-934e-e6171b9878a0 | -7.76083 | -42.59328 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c3f6725f-d9f0-3099-9038-c5675f018bff | -7.5193 | -38.00834 | 2025-10-03 04:32:00 | NOAA-20 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62b1e30a-3e47-38d6-bacf-e859b0714334 | -7.48555 | -43.0383 | 2025-10-03 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5f587ba-91cb-35e1-879b-3a57695dc419 | -10.83827 | -46.59123 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48d1bbaa-bb04-3c6a-887a-0e45e1fc3973 | -11.08837 | -47.80383 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 978748f5-1ed3-3f4b-897d-1b7ef02b6738 | -11.11216 | -47.73795 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6996f516-6a29-3e50-bbdd-d11e561388e6 | -11.90291 | -46.26904 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ca5176c-95e6-3a72-89c9-64582beddf7f | -11.90879 | -46.27817 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28f29d8c-975d-336b-a7c8-70f90055b7ae | -10.90522 | -46.70259 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc19b1d8-6eff-31f3-9078-57d247371aff | -6.1164 | -43.12225 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4af8fc3-3fde-3aa7-8b12-7c5860f3fcce | -5.90573 | -43.90311 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d151bc96-1a06-3cc8-b32f-c7bc74aa834f | -6.13839 | -46.54789 | 2025-10-03 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d9580ae-f257-30e1-9125-13f9bd91b56e | -5.46055 | -51.40343 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376caa33-7040-3c16-b36a-baf368e82236 | -7.80129 | -42.51781 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2dbdbf18-3b07-373e-a596-40fd40b8a529 | -10.34488 | -48.17854 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 457dd3b1-b6aa-3d20-9337-1bf060fc3f18 | -11.7801 | -46.83521 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aacc11e6-78bb-3629-9594-4808c7689890 | -10.87772 | -46.72157 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21c72507-5d5a-34dc-92d2-4e2c39a5c14c | -7.76497 | -42.59388 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3ee34095-ef54-347a-a7fb-0fd9a37720a0 | -7.44811 | -46.46236 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 891a616f-b884-3b6d-9b92-b846b1124b27 | -9.95944 | -48.77247 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ff8fa0c-38c4-3fac-8eb8-475088f76674 | -12.29467 | -45.37487 | 2025-10-03 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1865b6b9-0958-311c-8e9b-3c3e9d284b8d | -10.88631 | -46.71129 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ea2433e-7ebf-3657-b2a4-a871468f1f0d | -5.44578 | -44.82676 | 2025-10-03 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6d4d861-b8fd-37e3-8955-dcb9b1563e40 | -10.91559 | -47.02602 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e01f9d5-c725-3a0f-92fa-dbfe396a7a83 | -8.18035 | -47.01234 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23bd37d3-54f3-361b-b156-574c2f6176cc | -10.98829 | -46.68371 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 433b45f6-4e4e-3f9f-81f1-0390ec4b69dc | -9.0821 | -48.02467 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cae1c08e-d830-3517-8181-6606c4719252 | -8.0227 | -55.41536 | 2025-10-03 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cbaab24-94fd-3e44-80d2-ddcede62fd56 | -10.00337 | -50.25682 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3fa804c5-215f-3d5c-b986-526ab34c353e | -8.60981 | -54.97495 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28b6eb79-5347-364d-996e-63655eda67c8 | -11.23376 | -48.20481 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b58e2c8-db61-39cb-bfca-b3fdf0e31fa5 | -7.75054 | -44.79533 | 2025-10-03 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d059743-1955-3a33-b744-1bed7ada4ce8 | -8.53458 | -47.27019 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8d42c2b-8cbf-38c6-b5e6-4a3b2b251da9 | -11.18736 | -47.73909 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8e8fec2-227b-3c72-85fe-2e2da9d587af | -10.89662 | -46.71291 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c08615ef-7e5e-363f-aa34-f277c1795c88 | -7.54474 | -47.19539 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9dc1bd9-d8e0-36b5-b0c9-db3e28c86ac3 | -6.38092 | -44.76256 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39821dad-9846-3404-9f4e-252a00e88c89 | -11.09187 | -47.87011 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 57d3b99c-e980-384d-aaed-c1373ebac091 | -7.1556 | -44.99524 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 851e37f9-b8f5-32f8-a423-f213c91e21f0 | -7.47909 | -46.46338 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4df36ec5-8f61-3915-aaa4-cd05d2210972 | -11.05186 | -47.80175 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c78aa722-52c6-3e96-9bf2-4b3377652bab | -9.34374 | -45.72396 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 437f0d7e-e074-3984-8ae5-cd928ee6c104 | -7.7483 | -46.24235 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b22a695-1757-3083-ab9d-d1db81d5edab | -5.64949 | -49.12962 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d967c47-a1cd-3362-9077-406d1e78acbb | -5.63037 | -43.91452 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| cf99f9cd-eba4-3c76-a2c8-0e4e60782968 | -7.7523 | -46.26192 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f10f1cb1-2eb7-3e95-a737-b6f72e44740d | -7.75734 | -42.55804 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b3946080-c939-30dd-9dd2-794e6f0d6f92 | -4.66675 | -45.7879 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ec1b165-4556-31df-aac6-09f131a44f2e | -7.87912 | -47.33718 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f7422cb-d1d6-3bf5-a623-180616de499b | -7.77018 | -42.58699 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 5f460fb1-9045-3960-a741-e576b2cf7bf2 | -7.31243 | -47.29155 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b04427b-cf03-32d4-b697-36f2d3335f32 | -11.84553 | -44.9573 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f96431e9-c031-31a6-8758-a6369c4a4523 | -9.41316 | -47.53403 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7329a5e7-a357-3ee9-a1e3-ce676ce9f620 | -9.06747 | -46.65607 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6534b0af-5acc-3c9e-a440-fccc52aa36c6 | -10.00457 | -50.24945 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d36d4251-31e7-3f2e-8102-61589e348337 | -6.05758 | -44.628 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a25f7487-7f76-3d7e-a12c-79436be7454a | -8.62614 | -54.98739 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d3ef450-d921-38a4-b52f-89b9ed5a67f0 | -7.01132 | -44.4953 | 2025-10-03 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb091f57-3baa-3f4a-ac40-5a15d1eb905c | -8.30597 | -44.85703 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c37d9a8-e940-33f3-9e92-cf300de8ddd9 | -9.16965 | -46.53909 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddfa4231-86bb-30cd-b1a7-3b3b8d0d3620 | -7.56891 | -42.39525 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e420bdf8-02f3-3f9e-bd63-25d2a1293520 | -5.7808 | -45.76122 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 001992b5-7805-319e-bbc3-f1f287fabb4e | -8.6143 | -54.97574 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README98.md)
