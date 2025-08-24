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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4991a523-8fa5-3670-8021-3fb7db0b92fe | -5.80568 | -59.21298 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aa4bfea-2aa4-3721-a9f3-cd8a3d732964 | -14.81972 | -55.9796 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c15d9e01-d5ed-339e-b186-1d7e6d431522 | -3.59914 | -47.52929 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b7cda9b0-a8d4-35a7-9ea8-2adf4dbb0886 | -10.14673 | -67.22658 | 2025-08-24 05:23:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc57e7d-7ba3-3db1-8730-3ae2abeb6729 | -6.63209 | -58.53994 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71d2b09d-471e-3c2b-880d-c423778196d0 | -7.50956 | -63.83651 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 122c0c78-b069-366a-a24a-e1a854b452c5 | -4.48049 | -47.67172 | 2025-08-24 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bb5248b-e93a-302c-b1d7-7dda14952489 | -2.92273 | -53.70008 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 71723cdd-34c6-37b4-a9e1-974ac9f284e5 | -6.31173 | -59.88309 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 963b2f53-8455-324a-b60c-f4ee0d0aca0f | -7.56716 | -61.37927 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2346730-c462-3733-b2a9-5c4a796c1360 | -14.34703 | -58.59455 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1728058-8fef-3413-872d-2db2c4d0e225 | -14.82415 | -55.97408 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa59fee1-5961-3e52-afc4-0ef489ceff10 | -5.73398 | -59.88534 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 344ac513-2d78-3caf-989d-3ce2618e1a60 | -4.95671 | -55.81379 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d86deae9-71b9-3eae-9203-ce10c7b79047 | -6.43334 | -53.38696 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 867b8494-6d08-31fc-87e1-c4a40b4b0093 | -12.72734 | -48.14307 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9533eae9-ac79-35a4-9911-320b60a096a3 | -3.43979 | -49.04589 | 2025-08-24 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| daed3426-978c-3cf5-8c14-b1897226ea8e | -7.43537 | -60.6227 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4438f07-229a-3d8b-9087-7c77ef57d6e8 | -7.50666 | -63.83183 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98309c80-9561-3eaf-87d3-72467f751453 | -15.07173 | -48.52745 | 2025-08-24 05:23:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49f8efce-a1df-3db2-bd67-ac8039696e64 | -7.10068 | -62.96936 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ee5634-f00a-3adf-8283-32f932d2efa4 | -10.94876 | -63.01043 | 2025-08-24 05:23:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48ce168d-8d60-3bf4-8c0d-8459b3c2e348 | -13.01049 | -56.88414 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3065cdca-d740-3eef-8240-fad7cb2b075f | -6.56216 | -60.06118 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42b490c8-4c85-3241-a6ab-42e581ca3fd4 | -14.29904 | -60.38407 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cf7e34d-755c-3582-8a7a-023d7eafa97d | -6.9312 | -62.89203 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0172a60-cd1d-348b-9cea-f27dfecdffb2 | -5.75269 | -57.57521 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 11ad221d-0738-3144-bdb2-f7e7ff643ca0 | -8.84551 | -49.90878 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e55b446a-f98c-368c-b6f3-b0b82022eaed | -11.70151 | -60.18453 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ded1dfef-a610-3982-9aa4-e8a8dc7ffe1a | -7.80514 | -61.3569 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caedbfd7-c7d6-34d5-9a43-617fbe1a97f5 | -6.37816 | -62.90657 | 2025-08-24 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92633d56-da24-3748-87b3-61463ae7690e | -5.81097 | -59.21364 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| add443ca-8843-3719-b269-e7afbca27f70 | -6.93943 | -59.64243 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcef2f40-151a-3267-85bd-56fad627ea8b | -14.30018 | -60.37649 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6c4d791-2463-3786-a755-7326b13bdc93 | -3.05615 | -49.50441 | 2025-08-24 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7624d3c3-f09b-3ef3-8054-35bc6601cb5d | -22.13958 | -43.65284 | 2025-08-24 05:23:00 | AQUA_M-M | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 9d605d05-90f6-349f-9c43-063e08161a76 | -7.43428 | -60.62963 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c13e43d9-d8e7-39a5-92a2-e75cd68cc34a | -7.55691 | -63.86123 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 267ded33-96ef-3033-9fdd-ecb53932ee1a | -6.57138 | -59.87384 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 212e21d2-598a-37a6-9353-3987b56bafca | -5.09891 | -56.9766 | 2025-08-24 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bce144bd-87e8-3840-9864-5c4dd6804426 | -5.76548 | -59.87957 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72ba2449-f9ca-3b44-b86b-9d97c83993c9 | -7.55757 | -63.85712 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08e338af-1c72-3af1-8950-fdcf9a0cf2da | -7.44801 | -59.93108 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f92e4ee-4422-3495-8d11-7de45c05268d | -7.43482 | -60.62617 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37dd4673-159b-37b8-952f-e196cf1a3040 | -9.67904 | -48.34939 | 2025-08-24 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4dd821c-c958-3a65-b3bd-44cb21fa158a | -3.12986 | -58.04068 | 2025-08-24 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bca0df89-3651-32f3-ac88-2eae8af61dca | -13.18457 | -51.92522 | 2025-08-24 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c005e94f-08c4-3cea-90ac-141c2cf669e6 | -5.87989 | -57.76191 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbc8aa68-b599-39e9-895e-a9cf2688257a | -5.45097 | -60.19595 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 334c558b-ecb2-3527-80e4-b2cb724f2751 | -11.70773 | -60.18928 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dea0fc7d-3803-3a9e-bb4a-72dcfd45fe61 | -7.07524 | -60.05978 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a91e6d8b-9303-306d-a8d7-e9e621b41016 | -6.91528 | -52.85371 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff6f1fbd-628d-3e41-a81a-65de9176d395 | -6.57765 | -59.87417 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7086cd03-4757-36ba-b5df-cf241c0cbfac | -5.74903 | -57.59951 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f39a88e8-7967-38a0-8528-6bc74ed6c630 | -7.54328 | -63.85473 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69e487ad-a3e1-36ac-92a1-0d75aac1edb1 | -5.7473 | -57.58684 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f698abb1-cb7f-34e7-a427-41b3c354543a | -6.5627 | -60.0577 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e65f2e4-0456-3226-bd82-8c4be6646e2c | -10.41366 | -64.42169 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.9 |
| d855535c-9f10-3b61-98f8-63edade44ec1 | -3.89904 | -54.68986 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f57d8ce-0bf9-3f9f-aef3-da182c642ed2 | -5.42873 | -60.16412 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e047ddbf-7b97-3e23-87a5-f716ff545a9c | -13.0226 | -56.82566 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3e7259f-9473-336a-b757-987910f33542 | -4.30599 | -48.10341 | 2025-08-24 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c15b01bb-f18b-3245-a059-e30a96a2dfed | -7.78684 | -61.5792 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8db0115-69f1-3e60-99f1-8d2e18726c99 | -2.93078 | -53.70554 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc5ecc47-fe13-3273-97f6-2425c7e1736a | -4.70648 | -55.93393 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfdb107d-ade1-3314-bc06-4dcbf0b0ec83 | -6.92124 | -62.90987 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faf20625-208c-3d24-8372-d3976922d501 | -7.74729 | -47.35593 | 2025-08-24 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f81477c-fd11-3af4-85b1-de6b3976b34c | -5.6107 | -60.23841 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a18a3e9a-5a72-3dc2-8216-1954734e53f9 | -5.44929 | -60.18508 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f653944a-f352-38a0-8f9d-06241bcaf860 | -7.17144 | -60.65849 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60dd0c1c-dd1b-3c64-9d31-aeeda053e6f0 | -3.89846 | -54.69357 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 620f5d30-8024-360e-a4ea-0d3aeb6bd1dd | -5.80652 | -59.22025 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b4cc0b-c832-3ba3-ab25-dad452786c84 | -13.18213 | -51.92522 | 2025-08-24 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c09f6cb-bdc4-37ef-b0e0-c3786ee64f27 | -4.48449 | -47.6731 | 2025-08-24 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 254269fb-55fc-3a75-b605-ca0d292568c1 | -12.72045 | -48.14012 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c459d0f-6d25-3344-8a7d-c8cfc7c1a7c4 | -9.61961 | -48.32699 | 2025-08-24 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a1fad6e-c213-3755-b828-f7b77739e4b0 | -7.80869 | -62.33893 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e03f3c6-c6ec-33ab-9ba0-1aaca82d4a8c | -5.4348 | -60.16861 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff1d53f5-5165-3e38-8766-f46ee6daed21 | -5.75086 | -57.58739 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4240256-407c-3324-a508-9cde7286abb5 | -2.91653 | -48.30373 | 2025-08-24 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e5fa5af-9242-3e41-85a3-1ef16dc69442 | -23.10618 | -49.96574 | 2025-08-24 05:23:00 | AQUA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| dc279eea-fec4-379b-97c5-8a76515f4b67 | -6.58044 | -59.8782 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c41b2ae-4f8e-35f1-ac30-22e121163579 | -5.44544 | -60.18801 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6dee9d7a-63eb-3fe2-a2ae-af348674567e | -7.4409 | -60.63067 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c05f650b-a31a-37fa-92ea-12b4f9160b12 | -14.34178 | -58.5961 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2c70ebc-9448-3528-bcca-4d62519b83cc | -5.79897 | -59.21192 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de574bed-1472-3bac-b009-6b52fa79864d | -5.73979 | -63.15891 | 2025-08-24 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bc1e03a-61f4-3782-92a0-599313f09d66 | -6.57378 | -59.87716 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8098983-59ba-3e1f-9847-4938ab3acd99 | -15.12952 | -48.63675 | 2025-08-24 05:23:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5769d067-da51-3c54-aa92-b5cb3e7b3629 | -6.74861 | -62.86645 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19032a61-11ec-38b3-a901-00a858d5bf72 | -7.43813 | -60.62669 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bafccb97-c8df-3b83-b5a5-46ec717e9084 | -12.15848 | -60.76641 | 2025-08-24 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 954628bd-09ed-365e-af4d-14cc83ca8ca0 | -7.90609 | -61.51229 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be70cf50-fd2b-3b46-86eb-96320a1155e9 | -11.70434 | -60.18876 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 059494ef-0921-3603-b82a-eea6460557dc | -12.73031 | -48.11554 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f168767-60c0-363c-866d-675e2860fc97 | -12.58852 | -60.36089 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 724fb006-b0bb-3c60-bcd2-fc6c99139d6a | -7.02783 | -55.43838 | 2025-08-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6cba188-2430-33c4-bc1e-078043e46dca | -14.81971 | -55.97345 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d4cdfd5-9528-316e-afaa-988bed1063fa | -3.89805 | -54.68544 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bed54ef2-3a3e-3c9c-b5aa-8228a9e80a7f | -5.74852 | -57.57874 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README74.md)
