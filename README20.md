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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cd813f0-e088-3838-85c4-016fabe874eb | -7.75392 | -46.24681 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| c7a1a3c9-136c-3098-aeae-39b89aaea4e3 | -6.06669 | -44.61917 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09edded5-a1c9-3783-8b13-37e642e777f0 | -7.05737 | -43.30373 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5c8c944b-a0b3-34d2-af21-e9639e2523e1 | -6.65298 | -42.78924 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c91468c8-2677-32d0-9c01-280c37e462b3 | -3.45425 | -40.23213 | 2025-10-03 03:42:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| eb55d94f-c7c0-35b3-8c2f-6046cad66c12 | -5.45037 | -44.82556 | 2025-10-03 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a55ca98-4a66-3654-be4e-085f6cdad025 | -8.30589 | -44.86657 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04926cad-316b-36c7-8bc0-59fbf517b6ad | -6.70516 | -42.79784 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8433a0dc-4557-3274-8742-ffbd90f2262d | -7.74808 | -46.24567 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d75b0f4-fdcf-31b0-95b8-1e01c384fc37 | -7.25455 | -48.4795 | 2025-10-03 03:42:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 51c404d6-7327-3af5-be8f-52af6873ff5e | -5.31732 | -45.28467 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf1da632-8a06-36bd-8ee2-c4c856eaa6b3 | -7.78996 | -47.37789 | 2025-10-03 03:42:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc0d405b-1c77-3921-9e98-9f63a2ebb33f | -7.52629 | -47.29231 | 2025-10-03 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73ab75f6-1ade-3666-b6b9-f56518c36c96 | -2.25446 | -47.88165 | 2025-10-03 03:42:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d12de63-9345-342c-821a-2e2beaa89ac4 | -5.48288 | -44.10906 | 2025-10-03 03:42:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7d9b662-cf80-3c43-b413-41735caf4f9b | -6.23821 | -45.3512 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d57ef6f6-4009-3f10-904e-02a77242aead | -3.93766 | -47.56147 | 2025-10-03 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b0da2021-e7be-3bd8-81f5-df093cf79557 | -6.29441 | -43.90987 | 2025-10-03 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21c4be18-3543-3723-bd4c-c63f456794b7 | -5.40632 | -41.34954 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a18fb780-0d9c-3c46-bc11-b8a3361feb53 | -5.35258 | -45.05385 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57567b9e-c658-3779-acd0-b034ec5cb268 | -6.38246 | -44.76049 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e97a74ca-332f-3295-be96-1fc998b707c4 | -6.29731 | -43.90661 | 2025-10-03 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df967aab-d89f-3a81-b866-908ce55066f8 | -7.744 | -42.5912 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57f331e6-34f2-3211-91da-7385f9a049ed | -7.3139 | -42.87031 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c753dab-f1ec-3324-a193-e6fca5582aee | -6.30005 | -43.90789 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4026dea4-0ca4-32ba-b5bf-bae2f9ebff7b | -6.28221 | -44.0509 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d43a5b60-8bec-3aa6-b4b8-c7cedb1c9d69 | -4.66667 | -45.7961 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f900d7f0-631c-3c13-957d-e83b8fb0a2cb | -3.84529 | -41.58308 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4ce3dd82-2eef-3013-892b-ebbfab88cdbf | -3.09323 | -47.0236 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a4209bb6-f580-3885-8f84-2b99ee5c525f | -6.35951 | -44.5949 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1726df75-0751-37d2-89f3-dbc2990e00ee | -5.40046 | -41.33061 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca38b272-098c-375e-8adc-54b05d25e388 | -5.31801 | -45.28077 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbf0f255-ace7-3fd7-be47-a4eeccd51bad | -4.57138 | -46.50001 | 2025-10-03 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa16cbb1-40bb-3419-a439-118ac6d17266 | -5.44481 | -44.82464 | 2025-10-03 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7b81b60-a563-31c8-a737-e88ec461ad2a | -8.3053 | -44.86988 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41365dfe-0633-35e9-a79c-0edebc8c09f6 | -4.6561 | -45.82178 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7385a99-c2d4-35fc-b24e-2d79251ac5df | -6.12811 | -44.03215 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc5d93ec-eb18-3253-9bd7-16dd259a3a88 | -3.84607 | -41.57834 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f4b98ce3-5294-37aa-a5c4-5b6bc174344e | -4.65154 | -45.81247 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cff9678c-b095-392b-b5c1-bbfdca35b49f | -4.94057 | -38.00168 | 2025-10-03 03:42:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 2e516d2e-e51a-368d-8838-d25a966fd32c | -7.78736 | -42.55926 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| af20b1c9-5986-3d90-8dba-4f1fe3c67b43 | -5.39903 | -41.33918 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf2c2257-0f6a-3fe4-9270-d084c6e4a767 | -5.74225 | -44.26109 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eac1103f-e848-3314-9ed9-f6795d120ff8 | -8.05443 | -43.9784 | 2025-10-03 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2abf1b54-e03f-369c-bf32-19c5c5f0b527 | -6.286 | -44.05279 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 370d8331-dc67-31ec-bd59-6a6d791f5fd4 | -5.6283 | -43.92117 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d72efcd7-1ff3-3b23-8cb3-d189fd850223 | -7.52174 | -38.00747 | 2025-10-03 03:42:00 | NOAA-21 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca86abd4-cbe1-3832-befc-0b76e2ba3792 | -6.1896 | -44.63068 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe378b25-2dad-3640-b5eb-161bc0040015 | -7.75316 | -46.25088 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| e7f19bb3-7d65-3e97-8514-08aa12f403a6 | -6.67676 | -42.79278 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 91d3f429-ce00-3ae4-b1bd-83f8880ef496 | -4.66274 | -45.78315 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1e83dc5-c73e-3c6b-8a55-409c027fa241 | -6.79766 | -44.74966 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09e0662c-d2e0-3419-bdc2-d9628a9adcdd | -7.7635 | -42.61487 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 506fc89e-5942-3947-b5ac-882b91b8f331 | -6.41803 | -43.92563 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50394f2b-825c-33dd-a796-e5e71612f740 | -7.29598 | -44.18681 | 2025-10-03 03:42:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21a07f4e-7962-36de-aa89-f5df942d1b6f | -4.67408 | -45.78873 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e12de11f-3eaf-3ebd-a773-d2a66c5b02cc | -6.41558 | -43.92711 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd4f752e-ded2-3355-96e5-6f1454c7e0b7 | -4.6553 | -45.79065 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0f18b30e-2119-3555-b7a3-63c0d04438d3 | -6.23903 | -44.23308 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9017eba2-abf7-3a1e-890e-a779f2a969b6 | -6.20289 | -45.92145 | 2025-10-03 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9265121-8d85-3dd2-8ecf-5e98b7571bac | -8.30649 | -44.85705 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d86d5d7d-d71f-3f3c-bb2b-69238b17cab0 | -3.93659 | -47.56744 | 2025-10-03 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7499a973-24d6-39b3-b4f1-5f6a301c0603 | -7.79923 | -42.51789 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f45a1d35-812d-34a2-b576-fd67a0c95b0d | -7.74062 | -46.2533 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 453ea991-7ec0-30ce-ad4c-98a6a395792c | -7.57064 | -42.39503 | 2025-10-03 03:42:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 872eb0ff-c24b-3b8c-a92e-a8f78e41d015 | -6.71063 | -42.80108 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 20e9f21d-2d6b-38fa-b967-c457b7216ee6 | -6.67158 | -42.82302 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a81822d6-e5a4-3e11-9d40-e917f26d8403 | -9.15283 | -36.8141 | 2025-10-03 03:42:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7b36d5be-1b28-3458-8f35-84e160aac415 | -6.05415 | -44.61684 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c72ed24-e28b-383d-bb31-1e23b879edab | -6.73046 | -44.14473 | 2025-10-03 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d90a429-6737-340f-82a3-33c453b628e7 | -8.30709 | -44.85382 | 2025-10-03 03:42:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ba6494c-c8e1-3f0f-b356-c8bb67848eff | -4.65228 | -45.80815 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7ea24307-e0d7-3217-b755-e55223bea11e | -6.97269 | -44.39609 | 2025-10-03 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2df715ab-07e3-3db4-9b9b-a2c8a23d4dda | -7.57408 | -38.28354 | 2025-10-03 03:42:00 | NOAA-21 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 89e55c71-0d2d-36e9-a92e-ebe307f0b08c | -7.78339 | -42.5009 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 14d5e1ce-4593-32b8-a681-a5ecb10708d8 | -4.64322 | -45.78929 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaeed66c-f1dc-3de6-8ed2-063b9f8a6e04 | -6.27623 | -44.04736 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca2433a4-93c2-33f5-a790-cfae5847577b | -7.78653 | -42.56402 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a72fa2bc-79ad-33e5-bf28-f8e7bc81d2b1 | -4.76517 | -45.32702 | 2025-10-03 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a77f5715-0d47-31a9-bde2-6d8c70bfbf57 | -5.41202 | -41.34233 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9c661500-93f5-3f40-a41b-97957aaa396f | -4.57765 | -46.50102 | 2025-10-03 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e206fd7-02a6-3a21-b198-36b74304a6c2 | -6.65207 | -42.79449 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8b3d50bc-c7ed-3e54-b628-35a9a6f3d05b | -6.0299 | -44.62788 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66bd7c5d-b844-3b2c-aaba-2e46bc731519 | -6.0523 | -44.62753 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72654188-568b-3191-ad67-2d46c3a2268a | -5.64015 | -44.51466 | 2025-10-03 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 18a303ac-943d-3afa-88a5-5239067b370e | -7.76248 | -46.26588 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 301938b4-671b-3db9-9592-bc05b90d7bd9 | -3.094 | -47.0077 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a236c52a-cc16-35b2-ac7d-a96a6c464438 | -4.67338 | -45.79284 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 74649b9d-874e-3803-994d-4d5c24f920db | -7.79762 | -42.52718 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 30054fad-2bb7-37ba-8025-34c4d2c010d9 | -7.70844 | -46.20341 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 672de913-eb33-3109-956e-e19d587094ac | -6.27242 | -44.04577 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97461df9-be76-3a57-99a3-88608d6aa91a | -6.70816 | -42.80895 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bea52672-7d65-3791-bcd7-4793a61a70d2 | -6.34428 | -44.30869 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f682ea8a-5523-31b2-b764-1e4d2cf51205 | -7.1977 | -45.38153 | 2025-10-03 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f32f269-a0b3-3f8d-b37d-6ca0a69f5c26 | -7.29185 | -45.26629 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddce23e6-ce78-3761-9c67-f2862c07437e | -7.76984 | -42.60566 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| af8fea63-9654-3057-88ae-71d862c10766 | -6.29677 | -43.90963 | 2025-10-03 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10402f01-fff1-30b3-a064-97a622b8ffa3 | -4.44182 | -43.23867 | 2025-10-03 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db1df262-78e6-33c5-b2d1-4d717b923e63 | -6.59604 | -44.32301 | 2025-10-03 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1049ad2d-819d-3dbd-b6e2-27379871d50b | -6.0493 | -44.61261 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |


[Clique aqui para ver as próximas entradas](README21.md)
