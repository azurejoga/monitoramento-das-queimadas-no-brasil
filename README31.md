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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb394f6-5290-38a3-8dcb-8389a419b92b | -3.61983 | -53.51345 | 2024-10-09 01:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0699aecd-02df-31bf-8d91-0d32c51648b2 | -3.5855 | -53.26731 | 2024-10-09 01:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cf0499da-a915-3ed6-8c1f-0a17faaa89bc | -3.48727 | -50.81346 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e50c2663-e3e9-33c1-8fcb-f9b0ef496897 | -3.40876 | -50.33941 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f1e1552a-09af-332a-9f6c-1c50f3136b8e | -3.40711 | -50.32804 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| dac51e40-54bc-337e-9d76-5de684c94224 | -3.33804 | -50.12965 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 985d3f7a-c03e-33e5-bfda-3245cd6dc039 | -3.33636 | -50.11778 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| fc2dc219-1d4c-3aae-ba49-5b9b3488ce15 | -3.2633 | -51.24686 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1ea7af43-d5d6-32e8-907f-ba0496990f02 | -3.26185 | -51.23671 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 5a52eb06-b059-3b22-9550-853851977867 | -3.20582 | -50.91555 | 2024-10-09 01:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| be02709d-4fc5-331b-9e63-28ea33d5c2f8 | -3.108 | -50.38405 | 2024-10-09 01:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 589e9b64-ea89-3784-a9fe-2a21a2666754 | -2.9887 | -49.53686 | 2024-10-09 01:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 06267acd-3438-3bd1-a8bc-65a6d1c102a4 | -2.98684 | -49.52363 | 2024-10-09 01:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fbb031ee-3834-3f50-b44e-5622cb4bb1a5 | -2.95538 | -49.20338 | 2024-10-09 01:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 1e81d9cd-4cc2-3e8a-8d22-6f8aa990316a | -2.95374 | -49.21012 | 2024-10-09 01:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| d5b8f213-9d70-3bb0-b50b-dbce483d81a2 | -2.95178 | -49.19615 | 2024-10-09 01:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 8615a679-8857-3760-85d9-d27d75fb31bc | -2.94443 | -49.20497 | 2024-10-09 01:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 320f45b0-d46b-3241-9bdb-ebc0dff65408 | -5.58847 | -43.27139 | 2024-10-09 01:15:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 138c9323-3fe0-31b6-b6fc-5906680f7c26 | -5.2368 | -43.82964 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| c234361e-4481-34d1-801a-2463e3c0b03a | -5.22801 | -43.82394 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 462ed11f-eafe-38ad-b5e7-a7d63d8419b0 | -7.25591 | -59.64851 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7bc4e0de-8e24-3849-a7d7-e139a3b4d095 | -7.2532 | -59.62683 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8e1eae03-e4db-3970-8f3a-c91e338b30fd | -7.24407 | -59.63345 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d5743e33-68c7-328e-8383-b90457fd38c7 | -7.23987 | -59.62857 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 232d01c8-1c24-323e-a336-13d922614de3 | -7.19673 | -59.79511 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 87683da7-7dd7-379c-8d29-c6942a0c9ca7 | -7.1939 | -59.77267 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 3d8471e3-64e2-3711-8e3f-52b01fe8a5c0 | -7.16874 | -59.36427 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5c30b00c-f163-3fe6-be71-7484f9187eee | -7.0327 | -59.43034 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c5f8d5a9-a12e-3d43-976f-84c212340255 | -7.03012 | -59.40967 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0d625550-a9b5-3c65-b340-12c87d58c410 | -7.0192 | -59.41668 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e7a74cd4-6300-3a33-8491-0a34fad2e0a0 | -7.01708 | -59.41142 | 2024-10-09 01:15:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b9469dae-97c6-36b5-851f-adafaab84b14 | -6.90119 | -52.19045 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3d5f445a-832d-333e-8eb4-79aeb046c396 | -6.86882 | -55.31457 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 33dd625f-c9bb-336c-aaef-e32fccb0a360 | -6.78857 | -51.65856 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a5c2b5d-71f6-3fb7-a065-af5082123ae1 | -6.77444 | -60.0648 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 227.6 |
| 5cebaf92-e7ae-3987-a195-829c5b3a6b4c | -6.77149 | -60.04155 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 223.1 |
| 41dcdd5e-adcd-3644-a494-b7b24286cae3 | -6.76073 | -60.06654 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 53449945-37b5-347b-b966-4b0646a14d80 | -6.75783 | -60.04347 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 3a7ac130-f3b9-332f-bb65-31e58b359937 | -6.53368 | -58.4266 | 2024-10-09 01:15:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1603d1d2-1ca2-3b4b-8af8-51433fd0b076 | -6.52751 | -58.42187 | 2024-10-09 01:15:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 71e9c9b8-168f-38f7-b59c-a23b789a5517 | -6.52536 | -58.4049 | 2024-10-09 01:15:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 954a54f5-f428-392c-9a77-08a29b4e64b9 | -6.52174 | -58.42814 | 2024-10-09 01:15:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 339a36ea-36e8-364f-9acc-e86c4978832b | -6.51946 | -58.41114 | 2024-10-09 01:15:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 81ab4158-a2fd-35eb-a4d7-ca00dd79187c | -6.491 | -49.91866 | 2024-10-09 01:15:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| b9b924b5-1732-3ef1-9a1b-d4d93b791e30 | -6.4894 | -49.90776 | 2024-10-09 01:15:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a09660cd-acaf-3171-ab88-5ca665037aba | -6.41912 | -51.71826 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a85de2b1-f61b-36c9-86f1-d3dec02d0ddc | -6.41012 | -51.71958 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d527fd19-df75-37aa-8c0c-e20fec2764de | -6.40883 | -51.71045 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 2fc988a2-07cd-33aa-82e3-c1d2a80ac2c7 | -6.09614 | -52.82908 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f86b796-6d66-32d1-b085-f38b49cff3b2 | -6.00419 | -44.64633 | 2024-10-09 01:15:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| caff882a-93ea-34fe-b707-d2556bff9f4f | -6.00288 | -44.64096 | 2024-10-09 01:15:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 0305454e-dff6-3b1e-a67e-2220062797de | -5.99976 | -44.61787 | 2024-10-09 01:15:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 59d00201-dfd9-336a-b34d-1813d8c65371 | -5.85427 | -49.83711 | 2024-10-09 01:15:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3852fab7-579c-312c-8096-4b232bb44afd | -5.8526 | -49.82563 | 2024-10-09 01:15:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 62a232d4-0804-3c62-a77c-13e40bc367fe | -5.85049 | -48.1703 | 2024-10-09 01:15:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 5bf0d332-1374-3c17-9238-f3677283c82e | -5.84821 | -48.15532 | 2024-10-09 01:15:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 590d8e18-691d-3c23-ac19-b7f5db259ecc | -5.8443 | -49.83865 | 2024-10-09 01:15:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c95639f4-e006-3df1-af5b-470c25bdcbcc | -5.81659 | -44.13373 | 2024-10-09 01:15:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 11c473e9-d989-3f75-a117-8d130d5f4865 | -5.79307 | -53.36464 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3b98c38e-1c32-3878-8cf7-c20ef2d830fe | -5.76297 | -51.45021 | 2024-10-09 01:15:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 17e69f03-cfc3-32b6-8b82-86ef4cd607bd | -5.71228 | -49.2775 | 2024-10-09 01:15:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| e0c62d70-ed12-3bd9-8de1-f53ef1202d2d | -5.69103 | -53.76241 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cffe2ae6-e162-3f2d-b20e-80b7e39e53e2 | -5.68979 | -53.75348 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5b042a22-c82b-3bfc-b4aa-bd3c4ee957b0 | -5.59528 | -53.73682 | 2024-10-09 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 320944b1-ff5b-3d20-893a-9b55c8c74aa9 | -5.58386 | -44.88809 | 2024-10-09 01:15:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| dcbfa90d-2762-3c55-af79-f5de9e11f533 | -5.58361 | -44.88156 | 2024-10-09 01:15:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| cc65377b-0b00-31a4-accb-b4b151ef6404 | -5.57963 | -44.86073 | 2024-10-09 01:15:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| b9665d2d-6b97-37a5-94fb-2ba0aa2decef | -5.44749 | -49.57419 | 2024-10-09 01:15:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| e99041b0-425f-3616-98c2-00d3d2348e95 | -5.44574 | -49.56218 | 2024-10-09 01:15:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 07eb23bb-1a6b-3290-870b-7aa869f9c776 | -5.26443 | -46.15554 | 2024-10-09 01:15:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 1e663484-b945-3e86-891f-5aa1dd96d720 | -5.09726 | -60.22886 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 99880d61-bb9a-3368-afde-84fed0a005ea | -5.08914 | -60.2352 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a732dc57-a617-3859-b2ea-96ad43c8677f | -5.08619 | -60.21302 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 919178ad-009b-3a05-8d75-a7b261a4b738 | -4.95271 | -49.75806 | 2024-10-09 01:15:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ef99680-ecbb-3e17-bc33-5eab890034d1 | -4.94253 | -49.75949 | 2024-10-09 01:15:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fd6b8465-6e6f-3f07-a5df-464478393dee | -4.90585 | -49.93309 | 2024-10-09 01:15:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a062dbdd-cb0a-3509-ad8e-aa6f135b7def | -4.80479 | -49.94316 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 27d9b782-7085-3de6-9a8e-15dd053facf3 | -4.80437 | -49.93731 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e09fb43a-b0ba-39ce-896a-2cfd73581a83 | -4.72349 | -50.87514 | 2024-10-09 01:15:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3e571399-a7da-32bd-b60b-489795cc8b88 | -4.68547 | -45.88303 | 2024-10-09 01:15:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f180d34e-0db0-3b62-91ba-f7dfa3b829c0 | -4.64856 | -44.36746 | 2024-10-09 01:15:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| d5d20fde-4dea-3cad-90fc-13f1f237a1b7 | -4.63847 | -44.3758 | 2024-10-09 01:15:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 4421b2cd-c031-31d8-9fb0-80917ab4291b | -4.37753 | -48.70771 | 2024-10-09 01:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d8bc4a51-0630-3791-afce-b27e5233127b | -4.28432 | -48.62386 | 2024-10-09 01:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 97d015cb-36fa-3943-b0da-ca958eda3c25 | -4.22481 | -44.2682 | 2024-10-09 01:15:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| c40a4801-ba26-3418-9978-26b991838085 | -4.18118 | -49.39596 | 2024-10-09 01:15:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0f27e07a-7bb6-32d5-8bb8-0a1dbc16a6dd | -4.15636 | -51.04668 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dbd7ab29-6698-3223-8b7e-2d12a72f7176 | -4.10458 | -48.26864 | 2024-10-09 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e657716f-9475-3dc2-b812-20b9e583729f | -4.10226 | -48.2532 | 2024-10-09 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9dd17515-37d4-3439-9eea-3b896923911c | -4.09647 | -48.2765 | 2024-10-09 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b3bb0cfd-1452-3010-a12f-0bbcb87c62b6 | -4.09423 | -48.26094 | 2024-10-09 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 6283b1b2-f7f5-3895-9e19-bcb212379cf2 | -4.09306 | -48.27063 | 2024-10-09 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e8d45a73-327e-39f8-b0a3-f09892aa7df2 | -4.05535 | -51.1198 | 2024-10-09 01:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b7e23d6e-b7fd-3f96-babd-00b4d4d70634 | -1.11 | -53.6173 | 2024-10-09 01:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 1ead9447-42df-3574-94cc-c4e30c6e3441 | -1.1284 | -53.6171 | 2024-10-09 01:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3a31f8e5-04f1-3225-882c-a1636d9b6229 | -2.3535 | -48.9986 | 2024-10-09 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 82178df1-2868-33ce-ac04-3e6f09edd40b | -3.8007 | -41.6229 | 2024-10-09 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 898143fa-97ab-34ed-9870-9851bca6551b | -3.8008 | -41.5989 | 2024-10-09 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 32912245-6582-35a9-a4ec-ef83858096f8 | -3.8194 | -41.6219 | 2024-10-09 01:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| c60a84c0-eb96-389e-8a1f-a63306c88b31 | -3.8196 | -41.5979 | 2024-10-09 01:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |


[Clique aqui para ver as próximas entradas](README32.md)
