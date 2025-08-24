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
| 7e218c6a-6b80-3dd8-8b59-403f66e1fb10 | -20.3396 | -51.6839 | 2025-08-24 00:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a8f3c620-b2ef-3478-8074-220f52b681ff | -8.9107 | -62.41 | 2025-08-24 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| df57969a-3573-3fc6-8bfc-22fc371dc808 | -14.7981 | -59.6343 | 2025-08-24 00:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a6780b4f-197a-36da-a762-3c8c7856c189 | -11.5055 | -51.8705 | 2025-08-24 00:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 062ca956-eadc-39a7-a0fb-6c8b95102d98 | -11.5426 | -51.9297 | 2025-08-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ced06c93-7bf0-3bb6-89ca-6f14fb4d07ba | -18.7778 | -45.0818 | 2025-08-24 00:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 619fab23-c9a6-38b9-8cdc-3357adeef329 | -22.0851 | -53.8204 | 2025-08-24 00:30:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| cb39f5f0-f526-3897-94fc-e6df39fb07fc | -11.5429 | -51.9086 | 2025-08-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 797863f5-1fc4-3e12-a29e-784d08ab440b | -3.5994 | -47.5359 | 2025-08-24 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d2df4f23-dc9b-3230-ac19-599419dcd0ef | -4.9605 | -55.8226 | 2025-08-24 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 84b61bb4-86cc-3a98-8490-388cd4c895f6 | -5.4182 | -60.1593 | 2025-08-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 8af7ec05-2f88-3593-bd4c-a24afe993e18 | -9.0416 | -65.7163 | 2025-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 1592b911-26a2-3e98-ab45-be7e8b026faf | -4.5567 | -43.2329 | 2025-08-24 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 7c8ec7bb-ac50-39d6-97cc-3866fbac5102 | -9.0045 | -65.7174 | 2025-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 631129a0-3cd3-3a88-a68a-4d88e46cfcdc | -14.8086 | -55.9883 | 2025-08-24 00:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4087954b-2307-35f5-b6df-4bf964f8f6a4 | -10.6009 | -50.1843 | 2025-08-24 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3721a35c-374f-3ad5-9bd8-56852c00812f | -22.0655 | -53.7802 | 2025-08-24 00:30:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 209.2 |
| 7a84820e-25f1-3d3d-9a09-4a9554134b24 | -18.7575 | -45.0866 | 2025-08-24 00:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 00f7ec06-2c2f-3523-8e04-ffb82b05c77d | -5.4548 | -60.1773 | 2025-08-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| eabfb374-3b44-31f8-acef-969a1d6deeaf | -3.5995 | -47.5142 | 2025-08-24 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 6562423c-19c6-354a-a2a4-876ae5a0c238 | -11.5245 | -51.8685 | 2025-08-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 43a93140-4be4-3ba5-8b26-7ebabe22ec6c | -16.797 | -51.3419 | 2025-08-24 00:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 4770e687-c7c8-307b-9f19-096059def323 | -5.4364 | -60.1779 | 2025-08-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 61998cf3-1baf-3e48-857a-cba3143d3649 | -17.6176 | -44.298 | 2025-08-24 00:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 94898b11-a8c9-38f9-898c-2d67f449ae3f | -20.3701 | -46.7433 | 2025-08-24 00:30:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| acb0e671-dec2-34d3-b147-5f7411bfbb2f | -5.4547 | -60.1964 | 2025-08-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6ac6db5b-da8b-3c47-8342-dfa5285e71d7 | -11.5236 | -51.9317 | 2025-08-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| fe03fb16-2dee-3811-be28-69cb40e4cbcc | -16.7965 | -51.3637 | 2025-08-24 00:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 78e61e93-86eb-3d0e-9ea0-0c4b96bdb8ab | -17.4045 | -42.6186 | 2025-08-24 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 09d218a7-f892-3961-9074-148c807c3dad | -9.0231 | -65.7169 | 2025-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 174.8 |
| c5c98ab2-26ff-340b-b0c1-54350566c339 | -9.0246 | -65.3807 | 2025-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 23a044c7-b11e-3085-aabd-4df0d9afc021 | -18.7569 | -45.1107 | 2025-08-24 00:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e8e49ddf-d928-36f0-bfd1-2b8c82a9257f | -5.4365 | -60.1588 | 2025-08-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d33401b5-f404-3dbf-a34c-e110279a352a | -20.3396 | -51.6839 | 2025-08-24 00:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3b531b96-6f40-34e3-ac8d-aeba16953038 | -14.7981 | -59.6343 | 2025-08-24 00:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c4f1b39a-eefa-3703-864c-c906e2a06d55 | -10.6131 | -44.3051 | 2025-08-24 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 32bfa54e-cf30-3275-974f-840d99d2cff7 | -3.5083 | -47.212 | 2025-08-24 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 7f14201f-6dc5-3007-a076-7c47921f9cb8 | -5.4181 | -60.1784 | 2025-08-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 248.6 |
| e35de050-c362-3a4f-8c87-ad9d85a5d478 | -11.5055 | -51.8705 | 2025-08-24 00:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8a07fbe7-f485-381c-84dd-792646b368bf | -22.0856 | -53.7984 | 2025-08-24 00:30:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 235.1 |
| 763e338b-d3a0-322d-ae61-0ce5b5d70681 | -14.8282 | -55.9657 | 2025-08-24 00:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b86dbf99-e23e-3042-b6be-d1a5947f6bce | -8.9106 | -62.4289 | 2025-08-24 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9a525c53-a28b-3bf3-9698-db5d28018103 | -10.6128 | -44.3284 | 2025-08-24 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| eb593587-b1ab-3626-ada0-9027e1f481d9 | -7.5534 | -63.8556 | 2025-08-24 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 6ff51fb7-fa16-3a7d-b8d7-54b7be0e4b55 | -9.0046 | -65.6988 | 2025-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 4e9d5e17-5559-3cd0-a077-79d30d6eb0cd | -5.4026 | -44.9952 | 2025-08-24 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 9464a6f5-b5da-34f6-8ac8-4f66928726fc | -20.3594 | -51.7023 | 2025-08-24 00:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 5f2871a4-9b2b-394d-9deb-5904cd3608dc | -4.9606 | -55.8028 | 2025-08-24 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 217c2b6f-3875-3224-b006-c3c09154f2f1 | -17.3844 | -42.6235 | 2025-08-24 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 62d649fc-de0e-301b-b859-f655197cbc35 | -20.339 | -51.7062 | 2025-08-24 00:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c6474788-90cb-310d-bbd0-ece00050a6e6 | -9.1998 | -60.793 | 2025-08-24 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5517406d-f370-343f-9196-44d7a3dec900 | -8.5946 | -62.5936 | 2025-08-24 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 35f06fd1-9921-3d78-a033-7bac1cc2ecca | -11.5239 | -51.9106 | 2025-08-24 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| bc022ffa-3706-3002-bdc2-f5ee2c251654 | -8.6131 | -62.5929 | 2025-08-24 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 3dc39ca3-bcb5-3823-837d-5682fff52083 | -14.8176 | -59.6128 | 2025-08-24 00:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 89fac75b-7e81-3ed4-8ed8-aa62a471a21a | -9.0232 | -65.6982 | 2025-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 6379dacf-ab02-3b44-9b72-c0df8dc89f39 | -4.9421 | -55.8233 | 2025-08-24 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 16afcaca-1d47-3e66-8d43-de8e6e28f9ad | -5.4213 | -44.9939 | 2025-08-24 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f8a33f52-5488-34dd-9e0b-e95618f7f000 | -14.7984 | -59.6145 | 2025-08-24 00:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| bc088e72-3129-39ae-a4fc-1cd671fc4cd1 | -22.0862 | -53.7763 | 2025-08-24 00:30:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 282.5 |
| a56b6f6f-2600-3347-8929-d3040f874ea2 | -8.9107 | -62.41 | 2025-08-24 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e6aebda1-5bbc-3230-8783-682f650074ef | -8.6314 | -62.63 | 2025-08-24 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0060979d-e6b3-302b-9b87-723d0b875c27 | -14.8089 | -55.9678 | 2025-08-24 00:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 7c56cdc7-8e8a-3645-9e2d-3040576b201d | -18.7771 | -45.1059 | 2025-08-24 00:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| cb975a49-88e2-354d-80a3-363f86a59433 | -12.0055 | -61.0201 | 2025-08-24 00:30:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b49ade0b-e8aa-345a-bb1e-c55d20a03b3c | -17.6183 | -44.2738 | 2025-08-24 00:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 9b5ef77a-9dd0-3c57-b48e-791d6558f6ea | -22.065 | -53.8023 | 2025-08-24 00:30:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 174.3 |
| cc014656-1e8c-3d52-91b8-55645175bb2a | -20.3599 | -51.68 | 2025-08-24 00:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 9ab67f84-6809-3181-8c22-7533692a103a | -8.9105 | -62.4479 | 2025-08-24 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 11ab131b-d092-3218-a5c3-85dd2c5781a9 | -9.0061 | -65.3813 | 2025-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a11754a7-0527-369f-97d3-b9c50587f8fa | -3.6005 | -47.534199 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4260b7e-ed9f-35a1-9890-a4c4e21df9a9 | -8.7665 | -49.963299 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66f2078-5e0f-3a6c-9302-531e1be72aff | -6.4665 | -43.472599 | 2025-08-24 00:34:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec6140ab-590b-3597-97a1-20d446e6272a | -15.1157 | -48.663399 | 2025-08-24 00:34:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 55d479f3-6a6c-3d9a-9b21-548a2685cbe4 | -5.5775 | -43.2477 | 2025-08-24 00:34:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5a63931-7924-344c-a377-17d9c82ec841 | -6.1803 | -45.429501 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46d64532-14b9-3058-afee-b84374556752 | -12.9952 | -45.231201 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f05b13fe-6ab0-3248-aeb8-419922ec832c | -11.5464 | -51.891102 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59b2a26b-534b-3d4e-aac0-9a7895bafb77 | -11.3145 | -47.8568 | 2025-08-24 00:34:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 568dd3dc-3ee1-33b2-98bf-43ab78bb3162 | -20.373301 | -46.729301 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 943a1c23-2f20-33e8-b391-26d8785c374f | -3.4438 | -44.134201 | 2025-08-24 00:34:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba0f8b2b-fecc-3f5b-9c76-e7548a41cc90 | -6.0919 | -44.6931 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ec03a79-332e-38e0-956f-ac1a40403746 | -22.0749 | -53.768799 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a9c84a2-c65e-3ee6-996f-403587da62d6 | -6.1246 | -44.391201 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 105be1a7-7ef7-346e-9753-6a9385698c17 | -8.5163 | -48.8708 | 2025-08-24 00:34:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 77fbc8d5-78ee-30c7-bf7a-036541016f9d | -3.5173 | -47.216301 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723c36c5-dc92-3140-83fb-c560230ca32d | -3.7845 | -47.571899 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b2b60a8-18e3-32ed-9ad8-fa37dd39e97f | -8.7704 | -49.981201 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7df2cde-96ea-3a43-aa3f-a5db64a70c59 | -18.7071 | -39.999401 | 2025-08-24 00:34:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 96248016-d251-3b03-9914-bf5ab9b26f52 | -3.733 | -48.928001 | 2025-08-24 00:34:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b176fb58-e494-3aa0-bcd1-74d91b6f1999 | -6.6027 | -48.043701 | 2025-08-24 00:34:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| dd739947-517b-300e-8988-0f9c9d5cbdfb | -13.549 | -51.534698 | 2025-08-24 00:34:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55ed3b7d-ad8d-39ef-81f3-06e89aed1857 | -12.7198 | -48.134102 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d1ca892-2d8b-3d7a-9f47-cee027409eda | -15.1138 | -48.654099 | 2025-08-24 00:34:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90466652-7963-3dad-aca2-20242bff7c25 | -4.4866 | -47.6665 | 2025-08-24 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6682b210-d3ad-3267-b8ab-f0e942738a55 | -3.6978 | -49.544399 | 2025-08-24 00:34:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70cba427-e64a-36a3-bad6-d750fb237fd6 | -7.4251 | -45.412601 | 2025-08-24 00:34:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d896771-a612-3442-889b-e81dfa3b649a | -10.7978 | -46.409199 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da49b9fe-56d0-3197-9a72-ae96e4e085ed | -11.3243 | -47.854599 | 2025-08-24 00:34:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 991ec98a-ce87-3cd0-b5f3-8ad779472fac | -22.084499 | -53.7672 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README4.md)
