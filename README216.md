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

## Dados Diários - Página 216

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38114646-0dc5-3d93-ba05-bcb09c62b3aa | -9.1158 | -51.5315 | 2024-10-03 14:05:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| f87f5414-fff7-3445-9171-f06c5a634689 | -9.2066 | -45.7188 | 2024-10-03 14:05:58 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 21569050-ae01-3305-9212-9fee6fb363e7 | -9.0516 | -67.8525 | 2024-10-03 14:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| f54e1975-3e19-3caf-85e1-d4b0f39ccc62 | -9.3832 | -68.3441 | 2024-10-03 14:06:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 569105c9-f9f0-3901-8b3f-2b0a31c1c327 | -9.3833 | -68.3256 | 2024-10-03 14:06:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 141.5 |
| c3db4e90-7f3c-343a-bb7b-269b1aa862f3 | -9.4018 | -68.3252 | 2024-10-03 14:06:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6f345faf-01b3-3f77-a53f-dbb35c2ff55f | -9.5772 | -46.2639 | 2024-10-03 14:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b5f49652-2d25-32d4-8eb3-41880df74de0 | -9.4368 | -64.5419 | 2024-10-03 14:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0768233d-e92a-3548-95c9-46f93dc06060 | -9.6012 | -50.1779 | 2024-10-03 14:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 90c677ea-5769-3d4d-a3d5-535e4561db60 | -10.5736 | -48.0839 | 2024-10-03 14:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 7b3980e5-7098-364c-92d3-ecff10487b53 | -10.6116 | -48.0795 | 2024-10-03 14:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| aecb1083-fea6-31b4-b42f-682ebf3cd21b | -10.5926 | -48.0817 | 2024-10-03 14:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e422dc88-168d-3e52-8e33-d353daec8f89 | -10.7168 | -46.1489 | 2024-10-03 14:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 91adc633-7a7d-3ab5-acff-614ad42c58a8 | -10.7122 | -47.6927 | 2024-10-03 14:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 69522c22-9fcb-3376-bd6e-f48ca7fd1f2b | -10.6319 | -53.6805 | 2024-10-03 14:06:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f48f6188-43d1-3fbc-be50-7aa82bd2ca12 | -10.7459 | -47.9757 | 2024-10-03 14:06:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 97a1a8a7-cbe8-390d-bd32-a3f360a8d1b2 | -10.8025 | -45.547 | 2024-10-03 14:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e729361c-f15f-3a08-a976-1e1395d1e893 | -10.6317 | -53.7011 | 2024-10-03 14:06:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ebe69b12-a527-3570-9448-da35d8d63ff1 | -10.6505 | -53.6994 | 2024-10-03 14:06:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 8a0f9995-01d1-39ed-a166-a7ba052f5b70 | -10.7502 | -47.6882 | 2024-10-03 14:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 54537c1f-1bfc-3eec-bef1-c77f5f65f184 | -10.7312 | -47.6904 | 2024-10-03 14:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 280.5 |
| 550d20d5-5408-3eb3-b2af-06fca2549bf2 | -11.2779 | -43.4118 | 2024-10-03 14:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2ad2ea2c-895d-382c-9fe7-86498f143f6d | -11.1575 | -45.9779 | 2024-10-03 14:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| edbede8e-f9cd-39f9-81bb-d914bd8d2570 | -11.2758 | -46.9098 | 2024-10-03 14:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| b59ced6b-1a75-3da8-9981-447cd2a0d259 | -11.551 | -63.7712 | 2024-10-03 14:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.4 |
| d17cbb4a-e723-3bf9-98a1-24cf1aa32b63 | -11.5698 | -63.7703 | 2024-10-03 14:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| b0aa310e-0355-302d-9e16-39f298b626af | -11.7967 | -57.3627 | 2024-10-03 14:06:13 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 3bf3cb1c-0260-371b-818a-d0d046b804d4 | -11.6241 | -64.0529 | 2024-10-03 14:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 50dae740-5064-34f9-8364-fe15ca676521 | -11.9737 | -47.3986 | 2024-10-03 14:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| bd53264a-07fb-304a-bebc-c3225f763e87 | -12.0128 | -47.3486 | 2024-10-03 14:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| f4162918-03c5-3d81-bb81-c9a7cbb8570f | -11.9936 | -47.3513 | 2024-10-03 14:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c6538d0b-4f9f-3a69-bf07-de5abb98ef4c | -12.3934 | -50.9658 | 2024-10-03 14:06:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 462e0e6f-131d-3eab-8fd7-088a56ec7d7c | -12.3292 | -54.0954 | 2024-10-03 14:06:16 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8234eaa0-aec0-3bd6-a67f-19cb19a1e2ff | -12.3937 | -50.9444 | 2024-10-03 14:06:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3d22cb3a-89f7-3fe4-b9ae-121da75aa6e2 | -12.5708 | -53.1379 | 2024-10-03 14:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ffc4bf3a-9e07-39f9-99fd-2c1ca7ac00ca | -12.762 | -50.5997 | 2024-10-03 14:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| fd6b843c-97bc-3729-adf1-15feabab0f5c | -13.0021 | -44.7123 | 2024-10-03 14:06:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| ff911010-fa5f-39da-9bd4-45da317e1475 | -12.9831 | -51.129 | 2024-10-03 14:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f336261a-cbf3-30a2-aa1d-3963f306bdd9 | -13.0017 | -44.7357 | 2024-10-03 14:06:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 9208f62f-9f0c-3bb9-8a51-ea5981c7eaec | -13.0406 | -51.1218 | 2024-10-03 14:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 14fd992a-b435-3368-8819-e1ca7b72fa4b | -13.1636 | -46.3231 | 2024-10-03 14:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 5d702f46-8cb5-372f-a69e-0a05940ed525 | -13.1783 | -48.6516 | 2024-10-03 14:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9b55837f-a179-3fef-9351-91e0562b734a | -13.1976 | -48.6489 | 2024-10-03 14:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 136.6 |
| abc48d5c-97b0-35f2-a041-e0c0fc136396 | -13.198 | -48.6267 | 2024-10-03 14:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 3fa08072-a28d-3fdc-9990-d60569ab64bd | -13.5195 | -51.1467 | 2024-10-03 14:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 81136b0e-703e-371c-bffd-552836b7845e | -13.5198 | -51.1252 | 2024-10-03 14:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 59b779c1-02ea-3f87-9b27-bdd12a063b54 | -13.615 | -51.1771 | 2024-10-03 14:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3b64df03-b040-3b67-b667-e2060e620f03 | -13.6146 | -51.1986 | 2024-10-03 14:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0df5226a-3fad-3384-ad25-44502691ab4d | -13.6339 | -51.1961 | 2024-10-03 14:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 512a7c0d-21cd-33a3-b7ac-4d40779ce59d | -13.6342 | -51.1746 | 2024-10-03 14:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| b3890cf0-2991-3667-a6bc-95f0d447e87c | -14.0392 | -45.0947 | 2024-10-03 14:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 276.6 |
| 2aa18c11-6362-3a38-b914-25f7125b8398 | -14.7935 | -48.05 | 2024-10-03 14:06:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0fd515c1-2e1e-363b-bb30-5597615b9b68 | -14.7017 | -48.7559 | 2024-10-03 14:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f79bf262-efea-363b-b448-3e61c8ebe370 | -14.8181 | -48.7598 | 2024-10-03 14:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 452c67ed-c97d-3ea9-9dad-6f57f85764f1 | -19.0133 | -43.2246 | 2024-10-03 14:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.8 |
| 5897202e-6eba-318c-9413-9b6729f16e9b | -19.0148 | -43.1749 | 2024-10-03 14:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.6 |
| dac32360-f7d6-32a3-a8d4-5acf8b3fbcff | -19.0141 | -43.1998 | 2024-10-03 14:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 315.3 |
| 69c4bb32-d52a-33f3-af08-0e4e9fa39eb6 | -19.0337 | -43.2193 | 2024-10-03 14:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 39b9af12-7027-3237-83d3-66220949e18c | -19.744 | -40.6685 | 2024-10-03 14:06:54 | GOES-16 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 174.4 |
| 44d1949c-3799-3b30-b32e-fa864778a120 | -6.1138 | -44.9213 | 2024-10-03 14:15:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 8d269324-52b1-3039-bdf8-a16be5f94c1a | -6.2565 | -41.8538 | 2024-10-03 14:15:41 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 1f01a848-5c9d-3754-8c7c-e049e35f0591 | -6.2968 | -43.4331 | 2024-10-03 14:15:42 | GOES-16 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| f1c6c34e-5da8-301b-9ddb-9779622180a6 | -6.3196 | -43.0335 | 2024-10-03 14:15:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 5a8cfcb5-b7a0-3091-afb3-ca2ac081534b | -6.3008 | -43.0351 | 2024-10-03 14:15:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c0b557e2-efb6-328b-84c0-df6482b0ed3b | -6.6169 | -45.1767 | 2024-10-03 14:15:43 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3dee16b5-aff7-3682-9910-b45a54c51df2 | -6.9791 | -42.9034 | 2024-10-03 14:15:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| b3d1d911-ff44-3b78-895c-4e1877cce32d | -6.9075 | -44.2836 | 2024-10-03 14:15:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 6528119d-b19e-3afb-8ba2-8e6eb13ce494 | -6.9479 | -47.6668 | 2024-10-03 14:15:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 84d57f39-4269-398b-bbba-0beec61288ab | -6.9979 | -42.9016 | 2024-10-03 14:15:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| e10ec1cc-7343-3cf9-b12d-1dccea7f499e | -6.8885 | -44.3083 | 2024-10-03 14:15:45 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| edf2af2c-070e-3c96-bbbf-8f904f4b2212 | -6.9666 | -47.6653 | 2024-10-03 14:15:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 853e548e-9ccf-3ab0-921b-0723f24edcd9 | -7.2001 | -43.3283 | 2024-10-03 14:15:47 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 4ef512ea-1345-3484-b28f-c0f29b2d00e4 | -7.6255 | -42.4362 | 2024-10-03 14:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 0b78bb4f-268d-312c-9218-bb67275eb8b1 | -7.6444 | -42.4342 | 2024-10-03 14:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| df8472fe-af2c-398b-920b-427a8a5d8d79 | -7.6441 | -42.458 | 2024-10-03 14:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| d7b9f50a-6e79-32e0-806d-b48ead1d2e34 | -7.7601 | -43.7626 | 2024-10-03 14:15:50 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| cdef5853-00fb-36b9-8d08-2d631e349c7f | -7.8149 | -45.4782 | 2024-10-03 14:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e55f9483-7cbf-31bb-bef8-7ba9eaad534f | -8.1762 | -43.6723 | 2024-10-03 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5005c807-637d-3487-8f93-00bf50ba6dd4 | -8.1937 | -46.8324 | 2024-10-03 14:15:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 01947a75-5d6d-31fb-8797-6418f1860151 | -8.1859 | -44.3901 | 2024-10-03 14:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4d5b7941-5f52-3f6e-820d-bb994759408b | -8.1573 | -43.6744 | 2024-10-03 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 42a292a3-b89a-3207-82f4-7a0669776ff8 | -8.157 | -43.6977 | 2024-10-03 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 316.0 |
| 28923620-4d18-3545-8702-a5f69e499e37 | -8.1567 | -43.7211 | 2024-10-03 14:15:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 275.2 |
| fae4fe10-6bf2-3ed9-a458-52a9dc935765 | -8.1759 | -43.6957 | 2024-10-03 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 4ba7d02c-c626-316c-aa14-8d5bf38714bf | -8.2239 | -44.363 | 2024-10-03 14:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 7a3d7d77-bbda-39aa-87d4-e64f353dd1db | -8.3194 | -42.8343 | 2024-10-03 14:15:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| db4f1fd0-eb2d-30b5-af4b-1477adff986d | -8.4259 | -46.2968 | 2024-10-03 14:15:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| ad9c9f8c-ec38-37be-bfab-cc6a504fa7e8 | -8.4646 | -62.6556 | 2024-10-03 14:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 4822b1f5-7ef4-344f-b896-1e7bb0929d40 | -8.6302 | -46.5224 | 2024-10-03 14:15:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 0f544c5b-1ce9-3084-ba23-8ccf4c260663 | -8.4829 | -62.6927 | 2024-10-03 14:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 23091ff4-34e4-3631-b77e-60bd2b8a1372 | -8.4831 | -62.6549 | 2024-10-03 14:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c5a0ac9c-8b8f-36f9-a7b2-e244b1027930 | -8.4645 | -62.6745 | 2024-10-03 14:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 4367bc40-04ee-3d5f-96c0-21ba77da9b07 | -8.7225 | -45.204 | 2024-10-03 14:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e8cf3b1c-215d-3605-aa8b-8df8a58576e4 | -8.6113 | -46.5243 | 2024-10-03 14:15:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 8c0ce904-5f31-3179-9dad-682cd51486c0 | -8.7795 | -45.175 | 2024-10-03 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 24db9403-523a-307f-b5e2-752a32a6117d | -8.8362 | -45.1688 | 2024-10-03 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 1431c5a7-0c45-3903-b394-3223972d3b72 | -8.817 | -45.1937 | 2024-10-03 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 99a2933b-6728-314b-9c7f-781abdd192ee | -8.649 | -66.6767 | 2024-10-03 14:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b0e7c684-bbb6-33d3-a8ce-5e25589c2e66 | -8.9674 | -45.2456 | 2024-10-03 14:15:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 18a5f202-d270-3edd-8f8a-b2a6d8d7072f | -8.8312 | -67.3951 | 2024-10-03 14:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |


[Clique aqui para ver as próximas entradas](README217.md)
