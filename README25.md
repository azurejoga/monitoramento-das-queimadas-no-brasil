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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8854fc4-a62a-3b11-a8f7-543b73973990 | -3.34056 | -50.20441 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f2545e8-0b83-3efb-8507-60e6e7657fd9 | -4.5458 | -45.67752 | 2025-11-09 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2be3ab49-c68a-33c9-b7f7-1cc2c59c2561 | -6.62139 | -55.01736 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3ff47da-5795-3cbc-befe-c309035626fb | -4.14407 | -46.26088 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9e11ba9-72e9-3cf6-a433-ae64f9fa180f | -3.32041 | -49.13454 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da156e38-ac5b-386e-af5d-076ce60aa99d | -3.31382 | -50.12332 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77527ec1-2aa7-3060-970b-6978c60cbd19 | -3.40433 | -50.26988 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c04e774-9bb1-39d6-a86a-b9c20255189d | -3.09679 | -50.32514 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee2f4a2-0347-34e8-8dc7-b28916cb2316 | -3.73444 | -50.03963 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecdb02e1-e9ee-3b85-b7ab-da8e7d1248ee | -5.20008 | -47.83685 | 2025-11-09 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc6b044c-240d-3a69-bb44-7f612f268eea | -3.81743 | -51.06341 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41fc578d-88bc-3a46-912d-c8fd4960ff15 | -4.11831 | -49.80466 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d73f624-4b2f-3d52-9652-8a4cdcfe551c | -2.60948 | -49.22465 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 239b3cea-91b6-3afa-83a1-a3d2cae7f054 | -2.48108 | -54.19764 | 2025-11-09 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cf95fd2-f6fb-36b1-8c76-549b72157b29 | -4.40174 | -49.66727 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f0f94d2-6115-3a0c-8607-654c81678546 | -3.66414 | -51.75471 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ff63b67-4bb1-3245-bbec-55c0bbea4f5f | -4.11561 | -47.29232 | 2025-11-09 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 491e86dc-df8b-3628-87ae-25bc9b929acf | -7.17356 | -41.73589 | 2025-11-09 04:38:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6c1a8295-b8f9-37f9-aada-ca37ffacf152 | -4.30054 | -45.71605 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d54ade15-4212-34c7-9e79-68e72e0a082b | -3.09181 | -49.22609 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8f57eab-7cfc-3ae7-bd86-20ab0aa3c95c | -3.97869 | -51.03815 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4fd637e-5328-3eb8-93f1-29d6f46aa855 | -5.89224 | -43.96513 | 2025-11-09 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d5a83e1-fe54-37ee-8b30-4858ab79b03f | -5.20945 | -48.68501 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4c798e0-b82b-3b1c-9726-9f930ae8f168 | -4.54391 | -44.60739 | 2025-11-09 04:38:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64981008-a492-3f5c-9780-319be3922f48 | -3.33811 | -44.37935 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 4d99d116-a240-316d-865e-c6457068dba8 | -4.24121 | -44.66792 | 2025-11-09 04:38:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 749058d3-97a0-3a2b-90ef-176e314adcf6 | -4.05313 | -46.42772 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7b3e372c-6872-3f56-9e86-26e7bc72dec9 | -6.88759 | -49.24729 | 2025-11-09 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09bd57ee-ab16-36b5-a28b-a41861ebc562 | -1.7207 | -54.68256 | 2025-11-09 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79ef1e8a-0d16-350b-82b4-e7ae812b7182 | -3.15162 | -50.59642 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f8182d2-179d-32fe-8d1b-7a31fa4efd60 | -6.993 | -46.81153 | 2025-11-09 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e6e61d3-0861-3b7c-857d-d16457e7bf20 | -3.0934 | -50.3246 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e70049c1-38ce-3105-99c2-b75f9db9bd84 | -6.0018 | -44.03302 | 2025-11-09 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa22789f-2190-3027-b56c-2a7e0e2aad99 | -4.9026 | -48.62631 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7314b64-2d1f-39e2-9f31-5b65b56e44f9 | -3.10575 | -50.20436 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2152792-85b6-34b2-bc2e-f734251d3e51 | -2.98773 | -52.82192 | 2025-11-09 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55ef9f1c-d394-32f4-8909-e3e93b864cba | -3.03144 | -50.27126 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93c5eabd-1b92-39a3-bd12-fd9ac38f98e1 | -3.67985 | -51.32117 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 533e4101-59db-35d2-95cb-1045a53c85f7 | -3.33487 | -53.24888 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec531ef3-da6d-3dd7-95e2-cd98d92980bc | -7.56381 | -45.88042 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 618e2e7f-a628-3356-90f8-2fa36a628b61 | -3.38337 | -50.15241 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e669971a-ef80-3e40-9c53-fc10073b2a4e | -3.13339 | -49.24364 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5accfa1-7a8b-3a26-9da9-21e8c66723f2 | -3.43685 | -49.75082 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3332f45f-7056-32a7-a296-06f731d4816a | -4.90667 | -44.6443 | 2025-11-09 04:38:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6dc2192-35e4-370e-9b1e-f9e56c4b334d | -3.76658 | -45.87276 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e82da20-9df0-3bb6-9122-acf740a251c3 | -7.55429 | -45.8576 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 924b7c33-193d-38a6-bf35-9c788f5e3e62 | -2.2932 | -47.87072 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b491878f-999c-3774-b853-33b7fbfc56d6 | -2.43278 | -48.04042 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8d283f0-bdd0-317f-ba66-815dd3d30ca5 | -6.99393 | -42.78566 | 2025-11-09 04:38:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a98e6a04-5254-3c55-9670-c54e5729195e | -3.58312 | -51.24672 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 484841c2-cbf5-3881-8fc8-a739ab7e1f6e | -3.5947 | -41.65918 | 2025-11-09 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2a492f70-e661-3933-bd5d-74af1389a2d1 | -3.86929 | -52.13509 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f27b7b1-697b-3b62-8f3b-1f5283efc871 | -4.33497 | -39.36567 | 2025-11-09 04:38:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59a4395e-0d00-31ce-964a-68ce22aafb92 | -3.10134 | -50.31843 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c9263497-be1f-340a-ba97-069e3ef15e33 | -2.60176 | -49.25182 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1496bff2-bd80-394b-b2ac-111b631f8eb3 | -1.6993 | -54.6763 | 2025-11-09 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 196e5116-836d-30ea-a748-126cc6a0edf0 | -3.09457 | -50.31734 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 469a4744-db9b-3eb3-abdc-13e654fd1de2 | -3.58467 | -41.66267 | 2025-11-09 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 679c52d6-f39c-3ce0-9e44-73fff32a7ef2 | -3.47467 | -48.97578 | 2025-11-09 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6400e0e8-6221-35b7-b991-7536dfa9b11a | -7.55802 | -45.85817 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75d66bf9-85eb-3ba1-8299-5539f31ba4fa | -6.34541 | -46.76759 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97058378-3424-3522-8bb8-bf00ddae1b1b | -3.57191 | -52.25836 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5548148e-35e1-3f0a-9a62-2731328eaec8 | -4.63581 | -46.40117 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 34e4ceee-a444-32d0-b4dc-35b2ed6b77c7 | -5.7145 | -42.18145 | 2025-11-09 04:38:00 | NOAA-20 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1f81e32b-d699-3c7b-b80e-ea36beb3b92e | -3.09795 | -50.31788 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4e6dba0c-23bf-32d0-80f1-c8ffb2d65acd | -5.21694 | -45.14555 | 2025-11-09 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 190c182d-a4a0-37a5-aa58-2daf6af05e4d | -3.29576 | -50.19393 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b96cfa83-7151-3a31-a88f-3c5bcf88ee82 | -3.65099 | -50.28238 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b84a9d4-6c66-344f-9fe4-c8bd63441dac | -3.03924 | -50.30957 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9857bb6b-936d-3f00-be09-f8bb73c2e64f | -6.87595 | -47.2454 | 2025-11-09 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54c36cf1-5a4b-3e57-a778-019524899263 | -3.31986 | -49.13799 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c023f2e-fb5f-3e08-ab61-0e514de078d4 | -4.20944 | -49.76569 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a82cd853-9807-3305-aa33-a6f0d4c505c3 | -4.33271 | -49.7595 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d2bea90-2ab9-3471-9583-a1b2b6ed1434 | -2.44265 | -49.22647 | 2025-11-09 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a10c030b-b9d2-30ac-88b0-a9c3ad37d4f1 | -7.23192 | -46.78504 | 2025-11-09 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc993b8-c792-3eaf-b0e0-8d072fa1b063 | -3.32341 | -44.37225 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab50704d-7b75-3ada-b059-2266a570b0c7 | -4.6323 | -46.4006 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2429a30f-43f9-3b0c-a178-3702349234c0 | -3.45034 | -45.6475 | 2025-11-09 04:38:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 270ee74a-967f-3155-8c8e-735934bc5965 | -3.14664 | -50.27367 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1f17f14-4940-3835-936c-b248a7c29a67 | -4.39842 | -49.77373 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d15e0599-7b6a-32a1-bbf7-fdd4e3c02cf5 | -3.83755 | -51.1287 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2386bba9-62ef-3f78-b246-fdfe66d2232b | -6.02104 | -43.77275 | 2025-11-09 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2813d638-83f4-351b-a5c9-93d3c31709cf | -3.80892 | -45.99305 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 529fa9ee-0e79-3737-b2a8-59fe2b023086 | -3.88401 | -49.82481 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6839878d-307c-3c0e-978f-83229d3e7e08 | -3.40231 | -50.4552 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e61d876-754b-39fe-b1c9-abb27e03089d | -3.41218 | -51.56465 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2b29d68-1b5d-36c4-9216-e9ea56ba0abe | -5.2853 | -44.95071 | 2025-11-09 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 268f75e2-7527-3e66-9a41-b4e956d8fe32 | -2.547 | -45.15361 | 2025-11-09 04:38:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e96012db-a87a-3df5-95a9-e68291510aea | -3.69228 | -51.12229 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 891968e3-56a1-373a-80ad-e0b5990cf7d8 | -4.30086 | -48.58463 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 647c17e8-4a4e-31c7-b52d-9e97a5365a06 | -3.52596 | -52.07737 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f930f0cc-11d7-3cfc-bfa1-a5f402054d51 | -3.13515 | -49.1021 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6919524c-a950-32ec-9a2b-292078c19fd8 | -4.37857 | -48.696 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3560c53b-ab5a-3adc-bc6a-6fe0a396631c | -3.48687 | -46.10976 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df7e18a7-ceb9-3ac9-9d71-19323fb78ac4 | -3.95276 | -49.02651 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3060355c-099b-3f33-b763-99fa6dc6c37e | -5.57435 | -47.12341 | 2025-11-09 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28ad530f-2ada-3978-a270-b07c9b6dc40f | -1.72142 | -54.67824 | 2025-11-09 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25d1cb5e-b8fc-3bee-b086-ac3601107a64 | -3.34953 | -50.2132 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd3cb7ce-4189-39d8-ab97-05eb1db9508b | -2.79745 | -48.93931 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d14195d-0ace-35e6-ac54-3ba649693346 | -5.01618 | -45.53422 | 2025-11-09 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README26.md)
