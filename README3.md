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
| 26bbe7e7-96ef-325d-8ea7-60deead84839 | -3.0005 | -48.9592 | 2026-08-23 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 5f549d5f-383c-3aa2-8128-c6e0a6fe0712 | -12.2613 | -43.1845 | 2026-08-23 00:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 39469653-40cc-3120-9afd-ab0cc0c6bdb1 | -7.5669 | -61.1906 | 2026-08-23 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6d56b91c-c54e-3b63-b8fa-3f56bd201fdd | -3.0005 | -48.9592 | 2026-08-23 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| 539b8c4d-7398-32e9-8168-b66f91520026 | -6.8188 | -59.6696 | 2026-08-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 0413f50c-9e85-319e-8c71-1995154eb7d6 | -6.9699 | -59.0658 | 2026-08-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 59f0a424-0dc3-36e7-b6f3-1001d9f23e78 | -6.8062 | -58.6469 | 2026-08-23 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 1a2def9e-be5e-3ad8-b98e-905060cef83c | -5.7615 | -57.5807 | 2026-08-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 88a8636c-1caa-3e0c-b160-4401c97a9fe8 | -6.1285 | -57.8393 | 2026-08-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| e1f49bde-a529-3bd4-b27c-5a2cf85c8a4b | -12.2613 | -43.1845 | 2026-08-23 00:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 73.8 |
| dcb1d740-35ea-3718-b336-3ec4cfb56e26 | -6.1925 | -53.5231 | 2026-08-23 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 7d706440-3ba3-3e50-b0e3-36a4e1f2ae03 | -6.8571 | -59.4179 | 2026-08-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 88ddcbdb-990e-3e5a-b6b3-389c24a72066 | -12.7409 | -48.4258 | 2026-08-23 00:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ac76e025-c65c-3eb0-bbb2-fe19fe703d45 | -20.2758 | -48.6518 | 2026-08-23 00:50:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 86.9 |
| fc3ab093-a494-3a64-bf05-ffee61976713 | -9.1909 | -59.4619 | 2026-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b6a7b903-754f-36e2-8736-f6fa852dc821 | -6.9698 | -59.0852 | 2026-08-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| b10f9eef-ac34-3012-bc76-e2efd7a9a7de | -5.78 | -57.5605 | 2026-08-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| a0c6e6f1-8b95-3c1c-a0ab-befee28f89ba | -5.7799 | -57.58 | 2026-08-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| afb23174-cae2-3a5c-84b2-3a0ab3cbeaa2 | -12.242 | -43.1877 | 2026-08-23 00:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 73.0 |
| e954cda8-cc7e-3acc-89f6-353cc7176536 | -6.8061 | -58.6663 | 2026-08-23 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| adb9ba95-de65-3896-b9c0-4fdb3104f20d | -21.454 | -46.1371 | 2026-08-23 00:50:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 6b978b2d-a8d5-3fb9-bbd2-9cce63606c09 | -6.1286 | -57.8198 | 2026-08-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6f86af3a-e9b5-3359-8a31-427d9989ef4d | -6.8027 | -62.9024 | 2026-08-23 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 04a0b64f-eacc-35b8-9888-cf15ccd187e6 | -6.8008 | -59.5934 | 2026-08-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 2ce78222-454e-3eb2-80e4-7b386f7e3cd2 | -6.9513 | -59.0859 | 2026-08-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 46363721-11ee-3bc3-9a3f-c0220ef265c0 | -12.7377 | -46.4567 | 2026-08-23 00:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 08215eb1-19cd-3c02-ba32-a5184abaf168 | -12.7413 | -48.4036 | 2026-08-23 00:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 7bc6efba-4905-3581-83c8-a03ba27a3a45 | -9.1722 | -59.4629 | 2026-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3d500af0-1b3f-3844-8b26-cf4d50c67fad | -6.5487 | -58.522 | 2026-08-23 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| cbd62e99-b628-3cda-9562-25d873cab3c2 | -21.4748 | -46.1316 | 2026-08-23 00:50:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| 7f047a3d-3124-3a0e-8623-3899f1f0d1ad | -9.191 | -59.4425 | 2026-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b239adcf-154e-3b3a-8d4e-83823176ef56 | -6.9514 | -59.0666 | 2026-08-23 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| fb291318-ed10-3fc3-812e-1b51f657e8ac | -2.982 | -48.9598 | 2026-08-23 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| db769a22-bd23-3113-91f1-45f64b07695b | -3.0004 | -48.9805 | 2026-08-23 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8843f040-ecc4-3112-85e3-59d074326c8b | -7.6664 | -63.3449 | 2026-08-23 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e1b21ef5-0e0c-3112-87cb-b68a3867f7a7 | -3.0005 | -48.9592 | 2026-08-23 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 216.0 |
| 8f80b3e0-efa9-3c95-b8eb-27c4473b04ab | -21.454 | -46.1371 | 2026-08-23 01:00:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.2 |
| 0c09ccf6-884a-3488-bf73-90b0adde3f7f | -10.8172 | -50.9711 | 2026-08-23 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 8c58ad72-58e3-3dde-9ba9-3f63bef31281 | -5.78 | -57.5605 | 2026-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e5940d5f-4b21-3791-8242-98231829dd8d | -9.1909 | -59.4619 | 2026-08-23 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 82e0cdb1-d74f-3aba-8c21-9cdefc8468a0 | -6.9699 | -59.0658 | 2026-08-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 2c960ead-31c3-3db0-bf12-2c0b85ebba35 | -6.8188 | -59.6696 | 2026-08-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 19450270-1438-3aff-b21d-89920f308122 | -10.8361 | -50.9691 | 2026-08-23 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 11fcc2a0-bbb0-3e04-8986-9c1cb04a6573 | -5.7799 | -57.58 | 2026-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c3720307-c6dd-33a3-9bd4-6a26524dc884 | -5.7615 | -57.5807 | 2026-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e6da6f33-3585-3ba2-8fd4-1cb43c063d3d | -6.1286 | -57.8198 | 2026-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 62565209-3277-33f3-b7ec-a693a2ed4e8e | -6.8062 | -58.6469 | 2026-08-23 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| d0c19078-1e80-31b0-8e2d-955dc319b578 | -6.8008 | -59.5934 | 2026-08-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 73190491-8f7b-3c4b-97b8-a3f5a1b0e505 | -7.5669 | -61.1906 | 2026-08-23 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e5450173-2c3c-33be-b899-23e01c75c9d4 | -6.1285 | -57.8393 | 2026-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| af520d15-318a-35d6-bf91-199b3126255c | -6.9513 | -59.0859 | 2026-08-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 48fd5974-bac4-34e8-9d6b-6b46c7d67aba | -6.8061 | -58.6663 | 2026-08-23 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ab952979-07e3-365d-82a1-2f24c1b7e511 | -6.9514 | -59.0666 | 2026-08-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| fff54a46-ae73-3cb7-96ad-84e08e43e080 | -12.2613 | -43.1845 | 2026-08-23 01:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 102.9 |
| a45ea20e-48c2-3894-bce8-bc80eab8d640 | -13.1886 | -51.4447 | 2026-08-23 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 06fef843-2995-30f2-ac87-0328c451d1fb | -6.8373 | -59.6689 | 2026-08-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e3076628-27c6-3f8f-a82a-5761fcc78207 | -6.8247 | -58.6461 | 2026-08-23 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2f140e6c-f0a9-39cf-8458-d735d054eb68 | -6.1925 | -53.5231 | 2026-08-23 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 86135bf5-9c84-3ed4-8cc0-365fea24ef89 | -2.982 | -48.9598 | 2026-08-23 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| f3d6ccf7-542c-3e14-ae56-2e57a9be9413 | -6.9698 | -59.0852 | 2026-08-23 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f737ec51-9302-3470-9753-a31a00785fbb | -9.191 | -59.4425 | 2026-08-23 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c4b3c6ed-2839-3748-9e55-f5854d8fb5dc | -6.5487 | -58.522 | 2026-08-23 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 68c986bc-c179-3171-b654-06d68f1e59bf | -9.15773 | -59.55626 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 82b99414-607c-3d35-a700-5aa113e8a6e4 | -8.92331 | -60.71803 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 75c70f53-d09d-34b6-bcc4-44aac408746a | -8.53988 | -54.84606 | 2026-08-23 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6893521f-a8e0-3c74-a20a-fe5e52dcc883 | -9.06452 | -60.43291 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ce7a9818-68a4-3034-a926-b6b191dd4b55 | -9.19208 | -59.46229 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 73897c72-d758-3d94-8a40-9e13e6dbc249 | -8.52984 | -55.34512 | 2026-08-23 01:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 06892370-afa8-36b3-91aa-d42819279fa7 | -9.1162 | -61.60292 | 2026-08-23 01:07:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 62aafa6c-96e0-3800-8e55-504eddefaf7a | -9.10267 | -60.90408 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| bb77b6b0-4e66-309c-b2c4-a8a8b27e7b1a | -9.2173 | -60.90792 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c372431d-ba99-35c0-bf69-d003efa3972d | -9.17735 | -59.44676 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 49d81ca6-6711-3701-88bd-85def807e116 | -9.59465 | -60.50493 | 2026-08-23 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6c3ba56e-7d99-34b3-bb65-13e7d68ddfab | -9.16806 | -59.46614 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 2018061c-19b0-33fc-a36e-d2de71af61be | -8.53873 | -54.85139 | 2026-08-23 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| c0dcead7-9d2e-305d-95e4-9d81e5530c64 | -9.15878 | -59.48535 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| bb3ad90e-6d9a-3c6b-9111-1d83794c9a87 | -9.51921 | -67.1655 | 2026-08-23 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| eddbaeb8-24ba-37dd-a132-af66625bc789 | -9.10474 | -60.91762 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ee6f3f3b-f918-392e-93a2-f6b161190b9c | -8.89741 | -60.54636 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 016ff9f6-e617-3b90-ab92-91a5d6a91281 | -9.10418 | -61.59232 | 2026-08-23 01:07:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 30ed6219-bb36-3b93-ba6a-e0c709ac2d82 | -8.94886 | -60.57709 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 12c559c4-9507-3c58-b750-66f8bea03164 | -9.1523 | -59.56262 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 49ce28e1-fa66-3ba9-aa96-f2415bd2ec86 | -9.8568 | -60.11451 | 2026-08-23 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| d1ca79b2-8197-3e53-ae33-dec948ec9d94 | -8.9481 | -60.58282 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 42670994-403d-364e-9c07-0d050e69751b | -9.85911 | -60.12968 | 2026-08-23 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0e3743d6-28a3-3ff1-bcfb-aac1a3382358 | -9.09402 | -60.9193 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 088f8a5e-a9b7-35a1-9394-402a5dfb3ae8 | -9.53448 | -63.57097 | 2026-08-23 01:07:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19a2623c-61d8-328f-9281-bba3712673f0 | -9.23156 | -60.39422 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5da6272b-0289-3655-bf3f-697a5ed5a5d9 | -9.65591 | -63.84307 | 2026-08-23 01:07:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 64af56fb-7765-3938-9f2c-2947b88d1e25 | -9.21527 | -60.89449 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 51b32022-4210-3e75-a7bf-e883573e118e | -9.2293 | -60.37941 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cd3321db-5905-3fc7-a793-a59feda6edee | -9.0961 | -60.93283 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7c354458-bf1d-37ae-8b79-5d1fff3efbb2 | -9.06676 | -60.44765 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8527905d-a421-355e-8f69-ac271213ea7e | -9.22032 | -60.78157 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bc049073-3f29-3f3c-8ddc-8084f099d03b | -9.18007 | -59.46424 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8f94d4d0-d370-3e2c-b3c4-a14f812c4dfa | -8.95109 | -60.59147 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b9cf411c-85f1-3a97-acb8-dab92172a7ea | -9.11439 | -61.59083 | 2026-08-23 01:07:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| efdb2945-6249-372f-8ba0-3ef8a79278ba | -9.41865 | -60.41234 | 2026-08-23 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cff2f62c-8a3e-31ae-b5c3-10566f03ba5b | -9.18939 | -59.4449 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 432e50d4-04a7-326d-b511-4546cd83724f | -9.04455 | -60.45139 | 2026-08-23 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |


[Clique aqui para ver as próximas entradas](README4.md)
