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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d98299-ec35-3fb8-aaef-938f2cbed0bf | -9.29075 | -45.4808 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61a55dd1-f2f2-3530-a65f-9a7311c1cfe7 | -10.08249 | -51.64326 | 2026-05-21 04:23:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d2880b6-d8c1-3f4c-b0db-29b3de90dd2b | -9.95378 | -52.45317 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f76703b-840b-3f1b-9e0e-c71e1a31070b | -10.48537 | -49.36541 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e1a6ead-891c-3be9-9f2c-d6adfc04e82a | -12.22957 | -44.25908 | 2026-05-21 04:23:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e3f4329-de13-35f9-bc96-28a856a5098d | -8.60358 | -45.9549 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee468b39-01f7-3048-8a40-e992b2354666 | -10.59136 | -46.65328 | 2026-05-21 04:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bb79082-d467-3735-8987-2d77e50aa7fb | -11.56013 | -56.94209 | 2026-05-21 04:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb1e88e4-f583-348d-8b57-059cc2393c0d | -10.32738 | -53.57848 | 2026-05-21 04:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dba372b8-a281-3eb8-a1e5-9aff953b0d2b | -8.54853 | -45.98188 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 278176f3-6030-3e14-b096-83648309ec1d | -8.73623 | -47.98238 | 2026-05-21 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1860e35e-23f1-3dd2-80d6-5f398cb08848 | -11.34323 | -48.00161 | 2026-05-21 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca849df-6e86-3ef7-8623-269a94104d03 | -10.19365 | -46.90331 | 2026-05-21 04:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28afa825-d8d2-3064-ac89-c8d8a12a962a | -10.11341 | -52.40622 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90f1cb06-9956-3106-a457-9720cb75998d | -8.72981 | -47.97711 | 2026-05-21 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86a8b0b4-03c1-3a87-bba0-0d2ae81a2881 | -10.48613 | -49.36087 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| dab8d7b0-4f80-38a1-95cc-0e0d2e5ce18f | -10.87192 | -44.64344 | 2026-05-21 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41467b0b-2e16-3a4e-b5c2-bdbcec03b75d | -11.32444 | -47.56084 | 2026-05-21 04:23:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 962652f2-8e5d-38cd-9989-f088137d5edc | -9.29971 | -45.48972 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6fcde720-3fa6-35c4-8b22-955f52ebc033 | -10.43821 | -47.95248 | 2026-05-21 04:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8ee1940-2715-3a96-a2fc-a5189c6f98f7 | -9.29696 | -45.4857 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bf5a834e-bf13-3610-b1f7-1ab8c217f117 | -11.65263 | -47.59248 | 2026-05-21 04:23:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4cc465f6-1ca8-3e76-97f6-423bcf3413d1 | -11.33606 | -47.42556 | 2026-05-21 04:23:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b50ec362-21f2-344e-8270-8d7a065ea725 | -10.49358 | -49.36221 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cdcda68d-b750-3f53-950d-ab8e0a37e4a4 | -10.10885 | -52.40547 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3dc2315-ca21-356d-81f0-39da50f76596 | -10.59883 | -53.47336 | 2026-05-21 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7989ba03-ad31-375d-a787-c04e609c2900 | -12.22785 | -44.24743 | 2026-05-21 04:23:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9a5f3f4-4c0f-3b89-a640-0d71ebafd30e | -9.30964 | -45.49132 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2f69f2dd-0d7d-3bc6-9f3d-5ee2a31e910f | -11.33484 | -51.41004 | 2026-05-21 04:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77b7674e-d121-3009-8c5c-159d12b92f48 | -11.46433 | -52.91788 | 2026-05-21 04:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27f05c2f-34e6-35c2-916b-8afe14f37be4 | -11.45529 | -55.11651 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cad5bcde-dad2-338e-b7e1-d110d0048a56 | -11.54614 | -54.53182 | 2026-05-21 04:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4457b0a9-5aa3-303f-8bad-31971540face | -10.42279 | -44.95694 | 2026-05-21 04:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d033a348-a747-3a6f-86d8-d7c56e726402 | -10.44649 | -47.94577 | 2026-05-21 04:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 553d858c-b821-3bbf-891f-907b713ae452 | -9.95836 | -52.454 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da389880-b382-38cc-b204-6597ac464647 | -11.43598 | -55.10228 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eef32701-69d9-31cf-bbde-09d208ca3472 | -11.07453 | -48.26664 | 2026-05-21 04:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0702a10-222e-33dd-9730-6b077306f086 | -11.45063 | -55.11208 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdbec908-b122-3269-b605-013a2b215aa4 | -11.56102 | -56.93758 | 2026-05-21 04:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10838449-6990-3782-a1fc-80addb778280 | -10.4973 | -49.36287 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cd4d65d-673c-3546-b8f1-4364dd87ef59 | -10.64841 | -42.29935 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d5fb7e9-9677-3222-93f9-60d5e0226398 | -10.64115 | -42.29825 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3623f903-12e8-31e0-a2b4-cc9c276a04c7 | -10.39511 | -49.44336 | 2026-05-21 04:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6f7ce20-498e-3e56-825a-1d4d1aae0c2f | -12.05765 | -45.29049 | 2026-05-21 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d8f25e-2e67-3d01-81ea-9b399bbe6372 | -10.65204 | -42.29989 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6068732e-7831-3e63-980e-bc82bb24a108 | -11.67623 | -54.58522 | 2026-05-21 04:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c77535d5-6b62-3170-8452-d0e9b0fbf83b | -11.4781 | -52.92053 | 2026-05-21 04:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2db456cf-dfc4-3533-b0d6-1122a3e90c36 | -12.22683 | -46.60502 | 2026-05-21 04:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9821621f-66f7-3cbc-861c-641fa389c9e7 | -11.55067 | -54.53583 | 2026-05-21 04:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41129689-ad39-3c9c-9fc1-e17dc01dd5f1 | -8.55406 | -45.99 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ca677cf7-4792-3252-83d3-8ad4e86508ab | -10.65181 | -42.30657 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d1b1db3-e033-3cf0-b8c3-4170aab2d34a | -11.7599 | -48.28601 | 2026-05-21 04:23:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8790db0-952e-3cdb-bbd3-593c285afc08 | -11.99645 | -47.76446 | 2026-05-21 04:23:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b495482e-125b-3e63-879d-cf2c071c8c85 | -11.43533 | -55.10566 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f018aa18-5539-3a27-8383-09b2e2863201 | -8.73336 | -47.97771 | 2026-05-21 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbc35b7c-2067-3262-a05a-97c6fada4e8b | -10.44169 | -47.95304 | 2026-05-21 04:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63e7b47f-f60a-3fea-bcd5-afdb7ca8f8da | -9.29475 | -45.47821 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c69a9dd1-9eb7-382f-8c30-290b83cf5b18 | -10.48986 | -49.36152 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 624360f8-b92e-315f-8993-1f82b8cfd592 | -13.2849 | -50.28151 | 2026-05-21 04:23:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dab526b-a747-3f0d-89dc-62c8963903e9 | -8.35858 | -48.1372 | 2026-05-21 04:23:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5af7df-09eb-345a-8314-8bbff997b195 | -8.73691 | -47.97831 | 2026-05-21 04:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f868ba72-0f83-3c0e-aa7c-e65e5d1a4631 | -11.97525 | -52.47074 | 2026-05-21 04:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a7debed-95c1-3924-b972-84f088f99e33 | -11.03275 | -49.47889 | 2026-05-21 04:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c8fb17-8871-3f6d-aafd-7277f280575b | -8.71177 | -47.86668 | 2026-05-21 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 210b4eec-102a-395e-a992-ae09d39a187f | -11.30404 | -54.7197 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adc6cabf-4794-326f-94aa-0a6390c9869d | -10.49433 | -49.35771 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fbb30ac9-00e6-3ba0-8554-47407ed7bc66 | -11.71498 | -47.81125 | 2026-05-21 04:23:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca32a953-fa07-3fe3-866b-b6ebaeb2371c | -11.56426 | -56.95253 | 2026-05-21 04:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad19dac3-60af-3918-9ae1-41fe7c7837a5 | -10.6488 | -42.30177 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc979183-9269-317b-b8b2-96d9d098cc25 | -11.32043 | -47.5639 | 2026-05-21 04:23:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8de61f0-b9d2-3083-b22c-51264e5f2ab2 | -8.61345 | -45.99988 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e84b3a4-ccce-3007-9cc6-430534f036d6 | -11.09481 | -46.56392 | 2026-05-21 04:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c5a64f4-3605-3f70-919f-c4baa793875c | -8.61288 | -46.00341 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a8b56c1-7178-3ac8-b9cf-c92bb6ed0f8f | -12.06429 | -45.29155 | 2026-05-21 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49f0f04d-1437-3c47-8a42-dd5255633260 | -9.95923 | -52.44926 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 053abd59-ef8e-3ea1-a966-74c1422b1f9f | -9.30688 | -45.4873 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d90d8b04-57ed-3e60-9d0d-23e08821a90d | -11.56695 | -56.9389 | 2026-05-21 04:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3c169c8-fed4-3c85-a153-941816eff7cc | -10.44997 | -47.94636 | 2026-05-21 04:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e93baf0e-054c-314e-9c41-f7b2b7f5fc57 | -11.96185 | -43.38997 | 2026-05-21 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f2be7a6-a069-335d-9f15-a6ebd181a9b0 | -13.02369 | -49.93177 | 2026-05-21 04:23:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bb48618-02a0-3db1-a1bf-04a39e47d3ae | -11.56606 | -56.9434 | 2026-05-21 04:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10f61896-6715-350d-ad09-930e0c00662e | -9.30302 | -45.49025 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 131c3cf6-28c6-38d5-a165-82aef8e13d75 | -11.61231 | -47.90374 | 2026-05-21 04:23:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5daa9a77-43a8-3688-945f-0a129c08c2f2 | -9.71448 | -50.41702 | 2026-05-21 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9748272f-2748-3da3-a70a-4a7bd5fbebe9 | -13.0274 | -49.93245 | 2026-05-21 04:23:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6832658-c403-316f-b6f5-d168047067be | -10.35509 | -47.81934 | 2026-05-21 04:23:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 991eee55-0b20-3136-add1-24ca3458736a | -8.61401 | -45.99635 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 21aa7a7c-b13b-34dc-8aa3-50c14cf8b42a | -11.14198 | -43.19428 | 2026-05-21 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 242290a2-3ecf-304a-905e-b072797d2f7a | -9.30357 | -45.48677 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 047beb2a-9362-3a44-b871-a2107ea1971e | -9.95355 | -52.45597 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e360e88-b4e1-3527-a053-697699d5b89c | -8.02294 | -50.67741 | 2026-05-21 04:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26ea8ae1-27ad-3b55-9e9c-e851e3e32abc | -11.43066 | -55.10129 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efdc5310-07c2-385a-8e89-e31c5ccb9509 | -11.95836 | -43.38937 | 2026-05-21 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5bc288f-27b0-31fb-809b-106fe9ad5210 | -8.55796 | -45.98703 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2598ad1b-1ff9-3a40-b213-17502282ce82 | -11.01458 | -49.04874 | 2026-05-21 04:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0da6ccbb-4acb-33bf-a631-68e097d7e898 | -9.2942 | -45.48169 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 62bbd842-7864-3da6-b8f2-556522d76c50 | -14.01076 | -47.509 | 2026-05-21 04:23:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aebc409-89ab-377d-a373-95032d5ae8ba | -10.64478 | -42.2988 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb3fd249-184b-3efd-a423-6ca6ccf9284c | -10.08706 | -52.18134 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 223c4a62-f15f-3b8b-8cca-9e6e543a1805 | -11.01775 | -42.86655 | 2026-05-21 04:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
