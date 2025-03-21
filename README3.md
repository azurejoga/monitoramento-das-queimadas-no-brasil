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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce8ffffc-5c46-36c6-8808-946688bb868e | -12.45769 | -43.57277 | 2025-03-21 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2a62291-cd79-3de3-9eca-bfb8cd858b0f | -11.2391 | -39.4104 | 2025-03-21 04:06:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bcafa527-7b36-33f1-bd06-5da8f01e4cf2 | -8.87156 | -36.43433 | 2025-03-21 04:06:00 | NOAA-20 | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0847b918-0830-3a21-9e85-3f7be9d90b83 | -9.8941 | -38.21022 | 2025-03-21 04:06:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 858d60f4-7ada-3985-a7cc-2f3d5a5ea9b2 | -12.86145 | -38.36717 | 2025-03-21 04:06:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16d4d619-11bc-3337-886a-b53642b8f00c | -10.16838 | -37.124 | 2025-03-21 04:06:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f7225d12-4fb2-35a9-820b-99e8fc3b27b5 | -12.8181 | -38.41434 | 2025-03-21 04:06:00 | NOAA-20 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f190e3de-4232-3f6e-a221-c4c8741fef04 | -10.24352 | -40.50817 | 2025-03-21 04:06:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d321df8-fcac-369d-9e9d-96c57f169e2d | -16.62567 | -43.16138 | 2025-03-21 04:08:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39832b64-6676-33d4-aca9-eb28b93dc5b2 | -20.12033 | -46.77911 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6447bae4-5f0d-3d78-a297-c637dcab3012 | -20.21449 | -46.67818 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26ef9962-3bcd-3ca0-820a-268fcf374c11 | -12.77756 | -45.4063 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11a59c4e-a7e8-3eb9-bbea-1461cc8753e9 | -20.11757 | -46.77454 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d64c275-f87e-394c-998b-0b4ec0492bd8 | -20.20839 | -46.67257 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d7a3432-c0ff-3725-8ec4-7f104b7c5c6f | -20.2218 | -46.61422 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65c51070-489a-3362-a4de-de364c218386 | -15.7371 | -41.14722 | 2025-03-21 04:08:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ca3808d6-42ba-3367-bd52-048d03365647 | -20.21721 | -46.66212 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b316b682-281c-36a2-8871-6f667937d11c | -20.11824 | -46.77055 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbc7e429-bf55-33a2-9824-a4259bc266bc | -15.80204 | -42.02922 | 2025-03-21 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| acf063a1-a86d-3021-97ff-9a7e307ab8be | -12.78172 | -45.40296 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd58acf1-318b-38d0-9689-bf04787f28e9 | -17.39803 | -42.12151 | 2025-03-21 04:08:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f025d985-ecec-3d34-b278-05f503960fb7 | -17.90694 | -44.41198 | 2025-03-21 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58e91232-2f2e-3cf8-a968-d4a452c10c1a | -20.12511 | -46.77174 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d52fdeba-9745-3a09-be36-ebf99f746f0f | -12.7887 | -45.40419 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bd3e7b8-4fcd-37c2-ad2f-04f6bf679126 | -20.11479 | -46.77002 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34241ca5-862e-39c2-99d6-91d4f30dcdb4 | -20.3488 | -40.36147 | 2025-03-21 04:08:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 23f7ba32-4c25-39d3-8e17-35807da1dca4 | -20.1272 | -46.78033 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d57b8a2b-682a-372b-8ccd-b9b260a0e6af | -18.30832 | -44.62253 | 2025-03-21 04:08:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18310c35-3b61-3b2f-8cb5-6f1a58a642c1 | -20.1293 | -46.78888 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89b5f7db-1c49-3687-aca8-e8816a694dcf | -19.43682 | -44.33864 | 2025-03-21 04:08:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5daf0f1-1539-3a9f-932e-5175378e0a6f | -16.42899 | -42.63152 | 2025-03-21 04:08:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 298b0b4a-c178-37be-89ee-cccc54b4166a | -18.12046 | -39.68282 | 2025-03-21 04:08:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5aacc71f-9035-30ef-9350-46312b29f881 | -20.11689 | -46.77853 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e44f6f2e-844a-32f1-a8e1-deab17bebbed | -14.11924 | -41.67718 | 2025-03-21 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f29f99d2-19d2-346d-ab69-bea0296cb84d | -17.48849 | -39.45211 | 2025-03-21 04:08:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c6f6c8b-d1f9-3ce4-b7bb-1b92cab8b826 | -12.78105 | -45.40691 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c72797b-6866-31db-9c37-1d14d221a329 | -20.12854 | -46.77238 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5bbd479-357e-3c96-9990-b9d1a3c648c4 | -15.80148 | -42.03292 | 2025-03-21 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 6b089c89-c299-31bc-9bd9-455d5de97e23 | -12.77823 | -45.40235 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed750199-a8fc-3da2-95c5-a7c9eb985b21 | -20.12653 | -46.78432 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c43eaa95-04c6-3f18-ad41-20fea5f6655a | -12.78521 | -45.40357 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6156d53f-c769-3d61-b965-3f6676f430c1 | -15.80338 | -42.02922 | 2025-03-21 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5311e52b-17f8-3cb1-bd66-fc649af3240a | -20.12101 | -46.7751 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a58f108-8d5a-369d-8b52-f57c7dc9db04 | -20.21517 | -46.67413 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40d8b3a2-9cfb-3204-a27c-4a5a521fa428 | -12.77407 | -45.4057 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e92627cb-22a6-36e6-a268-43f3961e19a3 | -19.83195 | -40.10821 | 2025-03-21 04:08:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4d087bb8-af36-394a-8c89-3745ff67dbfc | -20.11546 | -46.76606 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7098f1d1-ba37-31e7-94e3-7fb2db896809 | -15.79866 | -42.02868 | 2025-03-21 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fd6d9077-b598-39c9-a506-f1b96954d118 | -20.11613 | -46.7621 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39bda81c-6c77-3f57-aed5-b237eed29153 | -20.22861 | -46.61556 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4f932ed-780a-3448-a55c-9599d934c0e7 | -19.83128 | -40.11323 | 2025-03-21 04:08:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 432ff556-61cc-3d73-a18c-f9e7745e714d | -20.12996 | -46.78492 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3096e06a-6dc1-3b6e-8049-61bf49f97f3e | -12.7734 | -45.40967 | 2025-03-21 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d87fc579-acfc-310f-969b-ddcd949c0449 | -19.84959 | -43.84455 | 2025-03-21 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2efa6035-1a13-3ce5-ab18-1fdeb0cacf24 | -20.22927 | -46.61166 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5a2d67d-8f1e-3f4c-8478-5dcb8a16bda3 | -20.2206 | -46.66292 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73b965d1-f058-309a-9a0d-87aaeaef1e8e | -15.80283 | -42.03293 | 2025-03-21 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 14293cd0-d7ca-3fc9-a377-459f3da190fe | -20.21585 | -46.67011 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 793fd2b3-81ce-3d5f-a5e0-5c5abfa922a4 | -15.7981 | -42.03239 | 2025-03-21 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| a9020b98-6ade-3d70-b3cf-9f30d9396894 | -20.20907 | -46.66858 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9bb4bded-2957-3c1f-9dfa-14378a0b371c | -20.20771 | -46.67656 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fc60d14-041a-3b3f-8149-bb39a882f54a | -20.22993 | -46.60772 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8e51beb-8c21-3382-91b6-314152bc3e04 | -19.89817 | -48.35832 | 2025-03-21 04:08:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 854e7a1e-7132-312a-ab44-6a97f9641012 | -20.22795 | -46.61946 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8b0262d-1236-32c8-a2ec-a791ff1e74e8 | -15.94505 | -42.62123 | 2025-03-21 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aaa2de88-fd7c-375f-a106-0bf33786ca87 | -19.71813 | -40.35257 | 2025-03-21 04:08:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2806aa5a-c6a4-335b-8294-5f18fa068cbd | -20.12444 | -46.77572 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19a53742-804a-38b2-8d24-78931b1703db | -20.1334 | -46.78551 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d02e3b15-f808-34a7-acbf-cf8e0b3b8c76 | -20.21111 | -46.67734 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c4e3ac7-aa0a-3044-af9e-c84d35d96c0d | -14.13596 | -41.69074 | 2025-03-21 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f9d95884-d8dd-3cef-bddf-71824215ef77 | -15.83145 | -43.2927 | 2025-03-21 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 832aee22-582f-30dd-abba-682182722e99 | -20.21991 | -46.66696 | 2025-03-21 04:08:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d18c2b5-36a5-3314-890f-7ebc84705813 | -14.12079 | -41.67667 | 2025-03-21 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef3a8b39-33ef-36f5-a564-5d36d528178d | -19.71776 | -40.355 | 2025-03-21 04:08:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 91e5ddba-4457-3d7d-bfa8-5a22ea2064d7 | -17.46399 | -39.24331 | 2025-03-21 04:08:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3d0b4a1d-28a4-3a95-b5d9-cbb5739b6cf7 | -25.19204 | -49.32849 | 2025-03-21 04:10:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c942eb50-2f49-33f7-ac30-ae7a857f0931 | -23.34033 | -46.77183 | 2025-03-21 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a2720ce1-f002-3984-8acb-f0e8a04dc774 | -20.14172 | -50.73069 | 2025-03-21 04:10:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1bf17bcb-b735-37eb-a68f-3266dbf8f8fe | -20.92278 | -56.54733 | 2025-03-21 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b0ffc01-4c4f-37c6-819a-c138f63924e7 | -19.42919 | -54.78884 | 2025-03-21 04:10:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f25b7530-3c4b-34b7-883f-b2763acdc0ee | -23.52095 | -46.97339 | 2025-03-21 04:10:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 03c4856a-cde8-3aff-a3fc-d6f20f7e0286 | -20.92022 | -56.54543 | 2025-03-21 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a245d3fd-1f47-3283-888c-ba0345c0b4b1 | -23.97416 | -53.38338 | 2025-03-21 04:10:00 | NOAA-20 | ALTO PIQUIRI | PARANÁ | Brasil | 4100707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c388018-0e44-3735-8edb-55ca25a5e50c | -20.14093 | -50.73476 | 2025-03-21 04:10:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2c604727-93c8-39eb-a319-1e163975b589 | -20.48673 | -48.58632 | 2025-03-21 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66b5e73c-79b4-33a7-9bf3-ec311fe5c512 | -20.44557 | -52.30961 | 2025-03-21 04:10:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e888a38-ee35-3eb6-acda-a7681904a705 | -19.42461 | -54.78341 | 2025-03-21 04:10:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aaa622d-39ef-3050-9d87-7821528c3e83 | -19.42377 | -54.78728 | 2025-03-21 04:10:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13d28dda-469c-30f0-b2d5-cd5e89b000c6 | -22.11703 | -56.70841 | 2025-03-21 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1182d977-2fde-33c8-81dc-e8f596c8f02b | -22.11807 | -56.70396 | 2025-03-21 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bebe2070-24d1-32fe-a902-4ed42608c5ac | -20.92381 | -56.54294 | 2025-03-21 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e4a9f15-bcd1-3f57-b09e-c12b43784bfa | -19.43545 | -54.78653 | 2025-03-21 04:10:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 437ef0dd-f417-3e12-8312-ef063e317307 | -23.52584 | -47.19281 | 2025-03-21 04:10:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 20ca1e3c-966d-3769-8499-4fe47eed31f6 | -24.24346 | -50.74031 | 2025-03-21 04:10:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e385b39a-5f7c-3c00-a3e0-430b6a98a9ff | -23.33697 | -46.77119 | 2025-03-21 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cbc9afe2-13a2-3e30-b769-a0419c53bbca | -24.24239 | -50.74154 | 2025-03-21 04:10:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d08cec53-df5a-3c2c-9ea1-9d6353c81b4f | -22.87162 | -47.17533 | 2025-03-21 04:10:00 | NOAA-20 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ead55dd2-30bb-3a3d-95a7-446bcdb6e697 | -21.26239 | -49.0405 | 2025-03-21 04:10:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d996306d-ac91-3bf8-9c84-4b524ed418bc | -23.52246 | -47.19214 | 2025-03-21 04:10:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| feeef160-58cb-300d-9fac-250c76e96c9a | -23.59299 | -47.43944 | 2025-03-21 04:10:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
