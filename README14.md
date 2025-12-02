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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c856bab8-6a57-3b3f-95af-2a912f562892 | -3.85833 | -47.05608 | 2025-12-02 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 794097cf-d315-30d1-abf7-3faabf937a8f | -3.859 | -47.05164 | 2025-12-02 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99883457-bef6-397d-a5a2-90e5e89f7867 | -5.47555 | -45.41429 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86b15272-cf10-3680-ac97-e46b56ac43e7 | -9.32322 | -43.08405 | 2025-12-02 04:57:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e401e07b-604f-3287-87f0-0503e6954867 | -3.09998 | -51.54335 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cccf3c10-a3f7-37d7-aaaa-c5c9de6ea012 | -5.59585 | -45.17464 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ebf4525-1827-3ca1-81cf-5d52ae5c2166 | -3.11604 | -54.17282 | 2025-12-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76ba3918-bc2d-3e88-a0ff-f0b39f57dbb0 | -3.46011 | -52.23217 | 2025-12-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d92eb5ac-df7f-3f02-8d33-6d1e6758b9da | -8.05439 | -43.09809 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 27c22b50-c57f-3f5e-a29e-8becbdbb9f2a | -3.53189 | -51.63131 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d78290a-4727-3fb1-bbeb-5b2b6ad5fe95 | -4.04284 | -49.50896 | 2025-12-02 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09fc5cde-35e4-3226-8253-056d5c27ab1c | -4.61809 | -49.5419 | 2025-12-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9769cddf-e5c3-3d7e-bca7-7c8a24df7c6d | -3.42705 | -52.92644 | 2025-12-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5388fb3a-ddb5-3f51-ae36-0c6d1a1787bc | -8.16875 | -43.22495 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| d0ea8cc7-8b64-3787-9b81-41b2f9b4eb19 | -3.15014 | -51.49045 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 306b3975-8424-37a4-920d-ef70a1e5b28f | -3.38602 | -50.00312 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cf307f3-458d-3f23-a361-992c363c3f5a | -8.17631 | -43.21658 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 02a13c39-690d-3109-a47e-01d81909d642 | -8.05374 | -43.10307 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 670c683b-8d5f-30db-bdc7-05557076600b | -4.39708 | -48.92315 | 2025-12-02 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed793a24-5285-3773-813b-ee7ff78eced5 | -3.88306 | -50.30313 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92e4cfe4-f769-39ec-bd18-760481396684 | -5.48625 | -45.41279 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f13cf71a-be8a-3b01-874f-da510e0a4d8a | -8.16951 | -43.22049 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 49a985a7-60da-3e68-b90a-51a77a8c27c2 | -3.67787 | -47.62074 | 2025-12-02 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29dd3228-7986-385a-bc25-03d7984e8f31 | -8.16317 | -43.21945 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5573c1aa-3f3b-356f-90ac-96b80d92b4fd | -8.16335 | -43.21967 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 483047b9-24cb-3702-be09-64e2cf209179 | -7.29669 | -45.11211 | 2025-12-02 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 317adff5-0301-3dc6-b7db-1e421a930c03 | -8.04691 | -43.10706 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| ef7685ec-e8c3-35f2-8208-d5791f2b17e3 | -3.07451 | -51.52493 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8537a19-9e7c-3922-aef6-23d8dfab5823 | -3.85523 | -51.07767 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df952870-eb11-3b89-9b21-df5fcdc0fc58 | -8.1755 | -43.22111 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 7b17a538-04a0-3787-b716-13855143d6c8 | -3.85019 | -47.82431 | 2025-12-02 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64e0adf5-434d-3b6e-97de-b0eccb5b70c5 | -3.74441 | -50.97358 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bead06eb-996d-31cf-a80a-15dd07fb4b55 | -2.38265 | -56.05756 | 2025-12-02 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b107934-8753-3079-b8b8-0f789eeaa6d6 | -5.94096 | -45.39667 | 2025-12-02 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fde39ff5-d8f5-3e3b-92b1-81ce1a0e306a | -7.30206 | -45.11299 | 2025-12-02 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1001a4b2-698e-3147-84f0-ef8eac8cf289 | -4.22239 | -44.31532 | 2025-12-02 04:57:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aabd95ca-7f70-3cb2-9d49-8fd5f30db9fe | -3.10879 | -54.17467 | 2025-12-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4305fa56-1b17-32d8-911c-f14aeafc4c92 | -3.96324 | -46.98443 | 2025-12-02 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6893ff8f-be3a-3e8a-86b2-c835b5f49516 | -4.22289 | -44.31187 | 2025-12-02 04:57:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 129301e1-b517-38be-8d43-8e345cea4707 | -4.38997 | -45.48999 | 2025-12-02 04:57:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3287a41-ab4a-3953-bbc8-6112e08b4f1f | -3.46106 | -50.00019 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d8420f0-8af2-3168-a353-c9c51ef8f873 | -3.85522 | -47.0464 | 2025-12-02 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f393779e-2424-3cc6-a312-4f30af201db7 | -8.17568 | -43.22128 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 22e100a8-e174-3ec3-b4c6-4d7eecb327c1 | -7.90926 | -43.78645 | 2025-12-02 04:57:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9cbbb7a-e274-3b0d-889e-875a688abaf6 | -3.85588 | -47.042 | 2025-12-02 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7423f6ab-607d-3d9e-a863-37c0c5532b46 | -8.16933 | -43.22029 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 85c45421-268a-3bed-94f0-accda36e8a7d | -8.04756 | -43.10211 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| b6b64c18-98e8-3a2b-b621-83384ab48897 | -3.34234 | -50.01849 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9defb3f-caea-3dd9-9d4f-a2266987bd11 | -3.34169 | -50.02279 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50a14407-fb6a-35e3-ba41-3776e33010f5 | -5.16652 | -44.80173 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6d5e7c5-71aa-3905-b384-3acbb4180949 | -8.05835 | -43.10677 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 2e369d8e-6847-396a-b84d-0229cd91da59 | -4.86727 | -48.11159 | 2025-12-02 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88dcbac7-f53c-3c42-9c2e-3f4437e195e6 | -5.17097 | -44.79785 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6836561-75fe-30a3-817c-e1da9d4a0df0 | -8.1689 | -43.22513 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| bfc4d7f7-0904-3363-b916-43ac56eff9e0 | -3.48692 | -49.69376 | 2025-12-02 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ecd3834-a8df-3091-8969-66f6c1107e0b | -5.17052 | -44.80109 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4db50a4d-0793-3020-bab7-467ae067737a | -3.70615 | -50.65446 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 093ca685-fda3-3400-ae5e-3bc8ed512c9c | -8.0531 | -43.10796 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| e3d7df61-2957-3309-a906-4261fd0e26e9 | -12.04366 | -54.24328 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f223175-417b-3121-a675-415f352fbcb0 | -12.04311 | -54.2469 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 580c4abc-8518-303a-a9df-5377111a66cc | -12.51938 | -56.91415 | 2025-12-02 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b26aacd9-21f3-37fd-819e-0ddb8f73d7e2 | -15.9643 | -56.606 | 2025-12-02 04:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7a62eb5-bbd2-3379-bf80-36308835a6b5 | -14.4425 | -56.24996 | 2025-12-02 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2223ed78-2589-32ec-a143-666e7f187d3d | -15.97141 | -56.62555 | 2025-12-02 04:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f201fa3a-36e1-3b5f-bf06-124286f89cca | -12.04553 | -55.35744 | 2025-12-02 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7a1c0ed-9f88-30f7-b097-70013e577dac | -12.04701 | -54.2438 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| edea104d-1d29-3bcc-876b-3725b81b89fb | -12.51997 | -56.9105 | 2025-12-02 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a33ae4cc-cbde-3854-a345-97c10efe2fb3 | -12.41081 | -54.88837 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a88f1dac-4759-3d82-b5c4-1b28e6841320 | -12.40694 | -54.89138 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33c9f46d-b33f-3cc5-9afa-a480c7a63a10 | -15.1158 | -52.9458 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7037532-bac4-3397-89c5-8c2551cb0b5e | -12.04884 | -55.35798 | 2025-12-02 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52021690-99fd-3859-bcc1-6edef9fb1911 | -12.41026 | -54.89191 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffac5dc0-c63c-30a2-9fcd-57f2f101d24d | -11.13572 | -53.93947 | 2025-12-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d005cef-4638-365f-b5c9-478baf4241d1 | -14.1912 | -57.41523 | 2025-12-02 04:59:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fec4241-1efa-3ab7-b501-bb4d48beca72 | -11.66953 | -54.58116 | 2025-12-02 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bd0d14c-b50e-3d64-8886-8ed1fb4391cf | -12.45814 | -54.46741 | 2025-12-02 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0073d4d6-0a92-35f5-a634-590308d43842 | -15.96761 | -56.60655 | 2025-12-02 04:59:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fb17348-937e-3f05-abbf-43606b609308 | -15.06426 | -54.51943 | 2025-12-02 04:59:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84792bfd-0313-3aa4-82e3-0e0d74e71df5 | -10.89209 | -54.13435 | 2025-12-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38153315-7d6d-39cd-9f31-888520a2f5f6 | -12.04498 | -55.36096 | 2025-12-02 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fae392f1-ea34-360c-8379-cc10ca3b0dd1 | -15.12665 | -52.94747 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 633b0be4-d645-3fb0-ae1a-4084ae603e0d | -13.04073 | -53.71352 | 2025-12-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90ceeb78-fdce-3935-ad46-afa52c8109de | -13.88105 | -56.20778 | 2025-12-02 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42b9148e-063c-3653-8bc4-eec3bd9f27a4 | -11.6734 | -54.57812 | 2025-12-02 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d8d2b1a-028a-3820-a7f7-99fc4c749276 | -11.11983 | -54.64301 | 2025-12-02 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fe379b7-9f52-34e9-8e23-afcc340d879a | -11.43473 | -54.87012 | 2025-12-02 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ecd140c-0932-3da9-b97d-a2d3b4ea7064 | -11.44135 | -54.87118 | 2025-12-02 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d7cc07e-1bd5-30d8-b5ce-eb2a51d049e1 | -15.12365 | -52.9426 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de2349a7-204a-3249-9d21-0c60b6ed70aa | -15.12003 | -52.94205 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b817d302-a358-3a44-92ce-fa711e481ab5 | -12.45869 | -54.46381 | 2025-12-02 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 564b226c-08bd-38ea-b1f4-7633e534d3c1 | -12.52056 | -56.90686 | 2025-12-02 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6bf518f-4755-3086-81e6-7b292288d22a | -15.12241 | -52.95125 | 2025-12-02 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cfb646a1-ee12-3f66-a4a7-a6e535195cc2 | -12.41413 | -54.8889 | 2025-12-02 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48d1e49c-cfca-3492-a190-8bb334531e8d | -11.43749 | -54.87417 | 2025-12-02 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1126fb2d-bb05-3caf-8612-c9a7f259fb0d | -12.04829 | -55.36149 | 2025-12-02 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64495283-ed24-3e43-85d9-2419cc0d8520 | -13.20414 | -53.14733 | 2025-12-02 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eed668ce-c9fa-3fd7-a622-6a84c648aaa2 | -15.13245 | -56.68294 | 2025-12-02 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04601f28-0602-3d0b-941f-7a612be3aa52 | -11.67232 | -54.58524 | 2025-12-02 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99396d5a-6248-35ad-8021-f0472c0472f2 | -15.31917 | -53.01303 | 2025-12-02 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fa9645a-3f7f-306b-aedc-5e72f2cf2aef | -11.08205 | -54.77774 | 2025-12-02 04:59:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
