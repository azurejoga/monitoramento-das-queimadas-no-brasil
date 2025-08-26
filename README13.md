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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56938fc4-e1f0-3543-b2ce-7525b757c5f0 | -15.0244 | -48.1689 | 2025-08-26 01:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 305fe5cb-4393-347c-a265-11ef04a3d05b | -6.9128 | -59.3578 | 2025-08-26 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 68c11d4e-9861-3ac7-899d-1ccdd14cc6de | -6.766 | -62.8659 | 2025-08-26 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 98474c13-144f-3638-ab28-d11b11d40fd1 | -8.8548 | -62.4503 | 2025-08-26 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 235.7 |
| dadaab90-8ddb-3eca-b1bf-811622151ad4 | -11.1583 | -44.7859 | 2025-08-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 3724f52f-d9f3-3d3b-a398-e59283b658d8 | -13.1644 | -45.2897 | 2025-08-26 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 46b9ef78-b557-34cd-acfb-95628e02e3df | -4.9605 | -55.8226 | 2025-08-26 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 32ce487b-f2b5-3d94-89b4-7964f5467514 | -14.6567 | -49.0729 | 2025-08-26 01:00:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 5cff34ec-e1ba-33df-9324-f1b59d2af09f | -9.1677 | -40.6026 | 2025-08-26 01:00:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 09b806c8-c90d-331e-9163-e30242639edf | -11.2937 | -55.1129 | 2025-08-26 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| c0ea16ea-d3e1-355c-aab7-3f82069d0db8 | -8.3396 | -50.5652 | 2025-08-26 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9c0a5f03-fdb5-3266-bedd-3d6d6edcb9f5 | -11.1587 | -44.7627 | 2025-08-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 408.3 |
| 0c16b7fd-0415-3078-82c2-dd9b54a4e6d2 | -7.3854 | -64.3475 | 2025-08-26 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 175.8 |
| d802eb95-8328-34be-bf23-9153f770003b | -14.6372 | -49.0759 | 2025-08-26 01:00:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9bb5fbb0-046f-378b-8410-68d41a2200fc | -7.367 | -64.348 | 2025-08-26 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 455db5ab-f833-3ffb-aff5-c481f33f6f88 | -6.2459 | -60.0174 | 2025-08-26 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 46ac0421-b67f-32d4-8f26-df16b3abd9d8 | -23.0478 | -50.364 | 2025-08-26 01:00:00 | GOES-19 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.8 |
| 7688c19e-a471-334b-8287-e717204a07be | -9.9339 | -46.47 | 2025-08-26 01:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7880e67f-712c-320f-ab1e-716b91d24767 | -9.023 | -65.7355 | 2025-08-26 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 3bc9e7cf-4ffe-31dc-a384-e1306944521c | -6.2458 | -60.0365 | 2025-08-26 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 4b84f5a1-b076-3c23-98a0-87775d6c7c4f | -6.7144 | -58.5732 | 2025-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e1207ad7-a500-3dbf-857c-926f9aa6a373 | -6.9127 | -59.3771 | 2025-08-26 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 79464169-50b2-3ed0-8855-d7f3773447f9 | -8.9873 | -65.4379 | 2025-08-26 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a64bd77c-038d-300f-b989-4ee6c5119a0e | -9.0415 | -65.7349 | 2025-08-26 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| b216c073-9717-3bfa-aab2-d1bab82ebe18 | -11.6277 | -46.3899 | 2025-08-26 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4db7974a-5dc8-3353-9cb4-9cbc76986e1b | -6.7819 | -59.6711 | 2025-08-26 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| bd64f0e2-d3b8-3b50-87cf-50b2bf24c452 | -10.4241 | -64.3903 | 2025-08-26 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| abe84840-5080-3a6c-a5e1-3b272b4ca5fa | -8.8363 | -62.451 | 2025-08-26 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 1226c9ee-1198-3eff-8197-f142a95e528e | -6.2275 | -60.018 | 2025-08-26 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 877517cd-79c5-349c-90c4-71634ca078ee | -9.236 | -60.9256 | 2025-08-26 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 268a8cc9-17a3-3cd5-b65a-1422ee38141c | -7.3669 | -64.3667 | 2025-08-26 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c6191fbb-ec1a-3199-b389-6b2f4b65f06e | -11.3126 | -55.1112 | 2025-08-26 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| b1afebaf-408a-3ed0-add3-adeb1ac61ffd | -7.4224 | -60.6236 | 2025-08-26 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 6b27dfc3-cf29-354d-9898-25aaa0de5efa | -13.4618 | -51.1541 | 2025-08-26 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2053988d-218f-36f8-a853-e1ba9a4c55cf | -11.1779 | -44.76 | 2025-08-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6972f50a-517c-3e8a-8f8e-e6907d69e766 | -9.1909 | -59.4619 | 2025-08-26 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5097b435-cb2b-3542-9bf4-b9a5f442e456 | -13.4425 | -51.1566 | 2025-08-26 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| d794b20a-c382-3eff-8517-85152c8bb29e | -11.14 | -44.7422 | 2025-08-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 177f3e90-a230-36e4-be46-1d3bac6aeda4 | -8.8734 | -62.4495 | 2025-08-26 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0ce8fa42-484d-3079-bfd6-178eaadb2259 | -9.191 | -59.4425 | 2025-08-26 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f24a4506-087c-3387-ae64-2934826920c5 | -11.1587 | -44.7627 | 2025-08-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 404.5 |
| ba5789fe-79fe-3530-8e0e-a4ec1ea00e4c | -6.7144 | -58.5732 | 2025-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1eda1bbb-91a4-3b71-a038-924d0aa36d51 | -11.5587 | -52.138 | 2025-08-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 386.0 |
| c4d19cf9-f9e8-31a3-99f0-c849952d48fa | -11.1779 | -44.76 | 2025-08-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| db2c9b61-862d-35bd-88cf-a2aa2333be97 | -6.2276 | -59.9989 | 2025-08-26 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7c39bb1d-651b-3506-bdae-e688fbd02b2b | -7.3854 | -64.3475 | 2025-08-26 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 145.9 |
| e924e51e-3387-3f43-89c5-852c1611fa5a | -11.1583 | -44.7859 | 2025-08-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 8410ed2b-862f-3be4-a5a8-3b193ae5c8f9 | -11.559 | -52.117 | 2025-08-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 259.0 |
| f314d01b-29ca-3eb5-a903-9c6e3657fd36 | -8.8548 | -62.4503 | 2025-08-26 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 201.1 |
| f488eae0-80aa-3cbe-a913-296720222e86 | -9.0415 | -65.7349 | 2025-08-26 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| bbaa38d8-55fa-3aba-932b-596c42c82a83 | -5.5281 | -60.2133 | 2025-08-26 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ae3d551b-cfc5-345f-a4af-d502c54995f4 | -10.7597 | -47.0648 | 2025-08-26 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e126bcfc-aea0-365d-96e6-b372286d5bf6 | -6.2458 | -60.0365 | 2025-08-26 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b7fcf6e2-b592-37d8-9fd4-77e775520723 | -13.1644 | -45.2897 | 2025-08-26 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 76fe535f-89d2-35f4-9b4a-5a1a27d40997 | -13.4425 | -51.1566 | 2025-08-26 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 4175a3ff-a27c-32fa-b8aa-0917de8c491f | -11.5397 | -52.14 | 2025-08-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 484.4 |
| 36903b4d-7677-375f-8d0d-5ef402fcf91b | -6.7145 | -58.5539 | 2025-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| abccf3c5-3b68-3d05-9b3a-302969b554be | -9.1677 | -40.6026 | 2025-08-26 01:10:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 68.5 |
| c29af118-b2a3-39b0-896e-30cf8cefc03f | -7.4224 | -60.6236 | 2025-08-26 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 75796ae0-47ab-38b7-ba82-7bc1e6e903c9 | -11.14 | -44.7422 | 2025-08-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3bef4764-7522-3258-889a-9576c91b09f8 | -8.3209 | -50.5667 | 2025-08-26 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 3c235635-933f-39b8-82f5-948b0c3c9b02 | -8.9874 | -65.4192 | 2025-08-26 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 944e01b8-bf01-39bc-9a64-c12ec9da9b1f | -6.7634 | -59.6911 | 2025-08-26 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 22c75bd0-73a6-3f0c-aec3-cc85027d2997 | -8.3394 | -50.5863 | 2025-08-26 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5bb52367-61db-38d2-90f1-9a370df572f5 | -9.1722 | -59.4629 | 2025-08-26 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| b18ad285-40f2-3934-bb35-1710e936e6e8 | -6.7635 | -59.6718 | 2025-08-26 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| bcedbaa4-dc23-33ef-9fd8-a88c36f726e0 | -6.246 | -59.9982 | 2025-08-26 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 331ed7d3-26c7-3fc9-81ea-643180374a59 | -11.1591 | -44.7395 | 2025-08-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 759ff07f-15cf-35f0-9502-6d8d97a951b8 | -11.1396 | -44.7654 | 2025-08-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| e11e67e0-ab6c-3c9c-a3ff-bdfe625171db | -7.367 | -64.348 | 2025-08-26 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 3f06c5c9-0430-3122-be7f-c56ead6827dd | -8.9873 | -65.4379 | 2025-08-26 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e0b79f35-f37d-3576-a3ba-2a16abe781ed | -11.54 | -52.119 | 2025-08-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 277.3 |
| 84a6c5df-c506-3e5f-876f-b11bdf9fcc0d | -11.3126 | -55.1112 | 2025-08-26 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 21d52b76-6eb5-321f-8a49-4d929ae671ba | -14.6372 | -49.0759 | 2025-08-26 01:10:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0e580b43-9702-3cbe-a799-eb9d55e78c31 | -6.9128 | -59.3578 | 2025-08-26 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4311b9d0-b331-318e-9c5e-ff0ce855712e | -9.1909 | -59.4619 | 2025-08-26 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 292eb30b-a844-3bb1-b187-f123c9879a83 | -6.7819 | -59.6711 | 2025-08-26 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| bbdd87a1-aabd-37ca-b89b-e4db97184b71 | -9.023 | -65.7355 | 2025-08-26 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1c9ab110-a024-3aca-8008-4e8ba0312faa | -6.6961 | -58.5546 | 2025-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a3ec4853-cdef-3421-a8ca-eb0cbdbc2f4e | -7.3669 | -64.3667 | 2025-08-26 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 97b3b6ca-4004-3a21-b42e-8065ff7b3bdc | -6.2275 | -60.018 | 2025-08-26 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1f250cc8-6d5a-3dc0-a980-5ba70f7c2b88 | -7.3854 | -64.3662 | 2025-08-26 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f3c01409-01e8-38f5-92d4-3241ec03c280 | -6.2459 | -60.0174 | 2025-08-26 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 16ebb7c9-6277-33c7-8e3f-359545456a0f | -14.6376 | -49.0537 | 2025-08-26 01:10:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b488b6a7-7a9e-3658-99e7-20a6aad79a86 | -6.9127 | -59.3771 | 2025-08-26 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2e3984ce-a63b-3bb7-856e-c50637d5ac43 | -6.766 | -62.8659 | 2025-08-26 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 33222528-8a85-331c-9a31-c184f4b105d7 | -13.4429 | -51.1351 | 2025-08-26 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f1c50750-f5c7-3564-b6a4-b4825d2876d1 | -9.0231 | -65.7169 | 2025-08-26 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 86b98aa0-8b16-3f23-b6a3-3537bf4fadfc | -8.8363 | -62.451 | 2025-08-26 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 51da4c05-14ea-32c0-b30a-9bfbca6dad30 | -11.5394 | -52.161 | 2025-08-26 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 8dfb4824-aed0-39b0-8446-5fa8c5497b07 | -6.7476 | -62.8664 | 2025-08-26 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6d29be5e-b0d2-3b85-b81a-edf2e656a92a | -7.3541 | -59.6669 | 2025-08-26 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| bc39e0b3-bff5-314d-bcf3-ee8ecd0726b0 | -8.8364 | -62.4321 | 2025-08-26 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8548990d-6ba2-3b98-ac97-1771a0a8766b | -4.9606 | -55.8028 | 2025-08-26 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8443a08a-fb4a-36fd-aad6-a12cabe5ad60 | -4.9605 | -55.8226 | 2025-08-26 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 2ce76159-cc4a-3137-8d2a-671efbe98632 | -6.6959 | -58.574 | 2025-08-26 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 81fcab0c-29a7-3c49-a663-d90c2ae3a468 | -8.3396 | -50.5652 | 2025-08-26 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 52406c39-512d-3aa3-be17-38cfa2627dfc | -9.1724 | -59.4436 | 2025-08-26 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 27b5660c-637a-318e-b36d-656c78f76f29 | -11.2937 | -55.1129 | 2025-08-26 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 02ece0fa-ce45-32bb-8f63-0526571c075a | -8.855 | -62.4313 | 2025-08-26 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 94.1 |


[Clique aqui para ver as próximas entradas](README14.md)
