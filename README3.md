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
| 9e417c3c-0984-352d-846a-ebc8bc8142c5 | -10.6178 | -44.63263 | 2026-01-16 03:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd33468b-e435-323b-9208-b9f99ff95bd1 | -9.29924 | -40.8432 | 2026-01-16 03:25:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ddc90334-38dc-3947-bc52-98ec355081ed | -13.42912 | -43.86327 | 2026-01-16 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0038fcd8-38bf-357c-a5f9-f4e6a0c6b181 | -9.42725 | -35.54898 | 2026-01-16 03:25:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dc26ff3b-06de-3cb2-a307-3f06cfc25aa7 | -9.43189 | -35.54488 | 2026-01-16 03:25:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 372370c5-05f9-34f7-aaca-9e33d5b6ed74 | -11.24734 | -37.25909 | 2026-01-16 03:25:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c1e2fe37-2f2f-3426-8edb-ff67952885ba | -9.29992 | -40.8396 | 2026-01-16 03:25:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d66f51b-c836-3f64-a841-85e3f5eea74b | -13.32255 | -40.45789 | 2026-01-16 03:25:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b33abb08-0f15-3a6f-86fb-e75ec4cd58a5 | -17.61606 | -46.66272 | 2026-01-16 03:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 356f282f-f87b-3bae-b017-12b3306894c4 | -14.77551 | -45.94524 | 2026-01-16 03:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee707550-3294-3636-a142-b0da340ce692 | -18.39733 | -43.32236 | 2026-01-16 03:27:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74f1ec08-5793-347e-9e4c-5b4f065cac8b | -19.95119 | -41.21412 | 2026-01-16 03:27:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b357092-36e6-32dd-be35-6cef318afa9e | -16.13709 | -40.40322 | 2026-01-16 03:27:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ca5153d3-0bcc-333f-8583-7188796660de | -14.76484 | -45.92965 | 2026-01-16 03:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a7389c6-6da8-3c3a-8850-204eb1a290f8 | -16.6566 | -43.35379 | 2026-01-16 03:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa1a8cd0-fe47-343d-993b-0f01d64f9ed8 | -17.60944 | -46.66103 | 2026-01-16 03:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a090a440-87bf-31d0-9992-e048d009b3e0 | -16.13138 | -40.40765 | 2026-01-16 03:27:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 76e2a2b3-0bba-3782-8920-551136e0fa63 | -22.57183 | -42.02767 | 2026-01-16 03:27:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 38304c63-318d-3629-922c-dcb7e1d1a8b8 | -14.77017 | -45.93746 | 2026-01-16 03:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9e510a6-075c-3976-b4f0-9d934491b5df | -20.21478 | -40.25645 | 2026-01-16 03:27:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4d0c71c8-0a7c-3930-a6f2-5c44b5768ce3 | -18.39193 | -43.32119 | 2026-01-16 03:27:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baea0468-9970-3397-baa9-3c2c7962f9f7 | -18.8124 | -51.5914 | 2026-01-16 03:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 85d9dd2a-e403-30a0-b2ea-7f709abb1ddd | -18.8119 | -51.6134 | 2026-01-16 03:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| fbc43232-c92b-3ef6-bad6-7b98137ea0cb | -18.832 | -51.6099 | 2026-01-16 03:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| da089009-10b1-3b71-bccc-6b74b03a987e | -18.8124 | -51.5914 | 2026-01-16 03:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a9f751f7-10fc-3693-b375-aaf2a446e910 | -18.8119 | -51.6134 | 2026-01-16 03:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 78b5f326-82a3-3d8d-a3f6-18157e571d0e | -18.832 | -51.6099 | 2026-01-16 03:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| bbedbd38-1fea-3df1-8c0c-4e4b44af9077 | 2.7634 | -60.315 | 2026-01-16 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 9debf9b6-aa74-36f4-b6d4-726ac83fc555 | -18.8119 | -51.6134 | 2026-01-16 03:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 9ac29b4a-4b8d-3837-9661-9aa30ac48806 | -18.8124 | -51.5914 | 2026-01-16 03:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e75c856c-fa12-34d4-9d0e-d7f0d74be91a | -18.832 | -51.6099 | 2026-01-16 03:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 979d9003-abe8-339e-a4b4-5cb692d32dc9 | -18.8119 | -51.6134 | 2026-01-16 04:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1bf216b8-ee9a-3d0e-8f50-d1b4033b30a2 | -18.832 | -51.6099 | 2026-01-16 04:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 58f263d2-1da7-34ce-97a9-5a9399f01ccb | 2.7634 | -60.315 | 2026-01-16 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| ebce0c43-ba9c-3c3b-a146-a2a6c91ae9d5 | -18.8124 | -51.5914 | 2026-01-16 04:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| afe89090-a9bc-3b33-a9fb-d25cb09f4f08 | -18.8119 | -51.6134 | 2026-01-16 04:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 89041ffc-d342-36c5-bc7f-e8ffb58fd3a2 | -18.832 | -51.6099 | 2026-01-16 04:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a1eed757-f0f5-323d-9eee-a30607d0f931 | -18.8124 | -51.5914 | 2026-01-16 04:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 947ab790-656f-316b-b3bb-a67efb251f25 | 2.7634 | -60.315 | 2026-01-16 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 435642d2-b08f-34aa-97de-ef35c5fa4eb2 | -4.9407 | -43.42899 | 2026-01-16 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7603d382-437c-3549-b392-a66ae5a14700 | -5.03111 | -40.62769 | 2026-01-16 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a619af5-2a83-3d0b-a7ee-cc61aa78dcb9 | -7.02845 | -43.7403 | 2026-01-16 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e3fd512-b874-3279-a240-a5605b560036 | -6.05996 | -44.63005 | 2026-01-16 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a32ec81-9f24-3fad-a08b-877bea2cf50b | -0.08931 | -51.27698 | 2026-01-16 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386090bd-05fe-3cc0-b457-ff0750d6b07e | -0.08874 | -51.28046 | 2026-01-16 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 234ff9fc-fc46-3bb9-afab-de309e70df5f | -5.30841 | -45.17164 | 2026-01-16 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd7c38cb-f66b-387c-81d6-8dea688b1115 | -4.68636 | -40.70114 | 2026-01-16 04:14:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cebd3659-3647-3620-857d-4053a0662b65 | -4.32025 | -45.35374 | 2026-01-16 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf13077a-fa37-3fca-8101-a846293e4fa6 | -7.22976 | -43.06394 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 117614db-ad54-3788-8e7f-e0546e6f8fa1 | -6.23844 | -44.15282 | 2026-01-16 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c31c0a7-2f42-3d49-b80c-892d013c2fcb | -4.2176 | -48.47254 | 2026-01-16 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02607be1-5792-3a49-810b-2abc1b65982b | -4.68079 | -38.04385 | 2026-01-16 04:14:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6aa937e3-01a7-39d9-9194-388a0bf3f500 | -3.47543 | -43.33215 | 2026-01-16 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feb0e4e2-2558-349a-b4c3-a3dc14b6c1f3 | -5.83349 | -42.59584 | 2026-01-16 04:14:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1835f92-6d9c-38fb-b106-bd87f5a1c668 | -4.68004 | -38.04898 | 2026-01-16 04:14:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dd5b1dfd-c028-38ff-bb3d-588f5cebb607 | -2.74817 | -45.5831 | 2026-01-16 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f1d3c8b-6623-3f30-bb04-3b49ee11e674 | -5.85969 | -43.23232 | 2026-01-16 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0234a488-150d-37f3-b012-6439bd18461e | -5.55848 | -40.61895 | 2026-01-16 04:14:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9bdac3e3-dfbd-3d7e-bb05-ce8e581dcb81 | -7.23414 | -43.05753 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 2baf5990-6288-36f2-9ed4-cb6f110256db | -6.88741 | -42.83953 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a296d82f-3480-34f6-96b0-a32f45820ec6 | -5.6988 | -43.15 | 2026-01-16 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5e702d43-ae6f-3b36-b3a5-188d675f1d21 | -7.2303 | -43.06047 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a5714b80-5761-351d-a394-783f58a75268 | -6.23699 | -40.30464 | 2026-01-16 04:14:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 79deb7d3-e24a-3a48-8c75-73b1134bcb55 | -4.93077 | -43.42743 | 2026-01-16 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b932bd40-dd5d-318b-9dad-4f4dd0a8e54e | -6.4862 | -38.31164 | 2026-01-16 04:14:00 | NOAA-21 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d52e3bb7-6526-3077-b172-88d93cd3a700 | -0.08731 | -51.28038 | 2026-01-16 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a42a780-9669-3f0d-ab20-1d3b048a4a4d | -6.70747 | -46.52838 | 2026-01-16 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 693dc6fa-adef-34e0-be0c-d13fecdffba2 | -6.24079 | -41.24597 | 2026-01-16 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa36afb0-48a1-38e4-9ae6-2995d7f6837e | -7.22808 | -43.05303 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d817672c-b541-3b89-8117-09fde7c4da09 | -7.54565 | -45.5273 | 2026-01-16 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a480b3b-a98f-3482-a3aa-17b972ab76a5 | -6.06634 | -40.40292 | 2026-01-16 04:14:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f482ea5a-d6fc-3135-b3d7-22ce33022474 | -2.54035 | -43.26308 | 2026-01-16 04:14:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d9612d6-52b9-3f5c-8f98-7e6bc61d46f8 | -7.23691 | -43.06151 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4de44a45-0caa-384d-bacc-ff1576ba4de5 | -4.97227 | -44.96957 | 2026-01-16 04:14:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 695c2faf-3d6c-30a2-b6c8-1a938ca02764 | -5.56849 | -43.97773 | 2026-01-16 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe848e07-6f83-3274-92ff-57eef1e88d9f | -6.4822 | -38.31104 | 2026-01-16 04:14:00 | NOAA-21 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bb2fad3-462a-3fea-ade1-f621a655856d | -4.59872 | -45.99291 | 2026-01-16 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93e5ac68-6140-35ba-b7c4-3c8e85812cd8 | -5.13676 | -37.60632 | 2026-01-16 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 41576372-d07f-397e-932a-d5008bef75fd | -5.13731 | -37.60263 | 2026-01-16 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 24476b2e-6fd0-3e2a-bac4-2f9c3c3df5b1 | -4.73769 | -41.32606 | 2026-01-16 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2bd04ff-347e-3d33-806d-0fcaee4e2522 | -6.0639 | -44.62697 | 2026-01-16 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1dfa6c9-b2ff-39c8-96e6-bf7fd13e95f2 | -7.33483 | -44.42889 | 2026-01-16 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ea07707-9bd6-37d6-9698-a1f7792a8965 | -7.2336 | -43.06099 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2a833ca7-53fd-3563-bf50-2e6ce24316eb | -6.88687 | -42.843 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 426318c1-51a1-3006-bca2-6d05ca99fa85 | -4.33648 | -48.59545 | 2026-01-16 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 660c2559-4c79-3b1a-b070-f908eb5e4b92 | -6.02298 | -44.54698 | 2026-01-16 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fb4cd5f-f152-3fd1-a7a0-8b1bbf8605dd | -5.7021 | -43.15051 | 2026-01-16 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 069f9c58-6837-32c1-bf56-1180302622c7 | -7.22699 | -43.05996 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c16de84b-f4c0-3854-b510-129ef4a34c31 | -4.64987 | -41.30146 | 2026-01-16 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8033c2ed-7468-3a07-a0ee-b5cc040e20a4 | -6.55348 | -43.21157 | 2026-01-16 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 538d4849-0009-3a4b-8358-3c9cd1825ac4 | -6.06054 | -44.62645 | 2026-01-16 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c76a9946-1a55-3fd1-a2ab-cbd0e094da68 | -6.64493 | -43.43088 | 2026-01-16 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ec4918d-af17-35b1-8f9a-7560813c1faf | -4.65043 | -41.29786 | 2026-01-16 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a5a5c86-0896-3a65-b993-fc215f91cdbf | -7.45491 | -43.49656 | 2026-01-16 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ada349a8-6114-320a-87da-9ca716827db2 | -6.01962 | -44.54645 | 2026-01-16 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8431c860-fecb-3e46-b644-f81829363f1d | -2.76722 | -45.39693 | 2026-01-16 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1681c0e-a1ab-379c-9ffc-2df3cf5b2637 | -5.38541 | -43.19541 | 2026-01-16 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45e759db-616a-3d97-878c-92b3b968c119 | -3.9781 | -43.42547 | 2026-01-16 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b1ff197-35ea-3998-84ee-1d0ffc4171ba | -7.22423 | -43.05597 | 2026-01-16 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| df4b4bd6-1835-3559-bc0b-e4e86de380d9 | -5.47679 | -45.43238 | 2026-01-16 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README4.md)
