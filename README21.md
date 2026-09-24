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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a47a35d-57cd-390a-a407-de0a5a37c87f | -12.4024 | -46.9579 | 2026-09-24 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f32b64d8-5b26-3d79-80b6-142887fe665a | -12.4216 | -46.9551 | 2026-09-24 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 65cacae3-9638-33a3-9586-0d6aa0606c63 | -3.457 | -60.5692 | 2026-09-24 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2b4af84b-5a75-342e-b583-c3dcd83dd068 | -3.6764 | -60.5649 | 2026-09-24 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5d227c48-3ca8-370f-867b-a17f78158f7f | -11.9396 | -50.7415 | 2026-09-24 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 0fdeb0ce-256e-3e75-a36a-60abf643f451 | -8.6476 | -67.0292 | 2026-09-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 429e2f5f-885c-346b-9ce8-9fdc6530e619 | -8.1309 | -54.8263 | 2026-09-24 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 6ccc96f4-00d0-341f-818a-e5e38374ff93 | -11.9392 | -50.7629 | 2026-09-24 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| f665c3e6-ebbf-3d4c-bf30-19ab0a99dde0 | -12.0418 | -50.2796 | 2026-09-24 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e011639f-013e-3b72-8fc0-fdd4f51a4b5b | -9.8491 | -48.4927 | 2026-09-24 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 77d89896-4c7c-3598-9909-534942049dd0 | -8.2802 | -54.7764 | 2026-09-24 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 2ffdcdad-95ea-3296-b67f-a5801398d01c | -9.043 | -48.1384 | 2026-09-24 00:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c5f89979-a7c1-3304-8e2a-16b853bece82 | -12.0414 | -50.3011 | 2026-09-24 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| d7fb12f0-1376-3f71-a410-d6e04557dd84 | -3.6763 | -60.5839 | 2026-09-24 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 029ef11b-c964-3ca9-ae74-e62e0146735f | -6.4303 | -59.9532 | 2026-09-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| daf4acac-abb3-38d3-85ea-94b8935b6d8c | -6.6146 | -59.9272 | 2026-09-24 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 00be82d7-a86d-3821-bcb8-c571328ea93d | -6.4486 | -59.9717 | 2026-09-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 10e6e128-933a-36b2-8e7f-7eda581aa3d2 | -10.2824 | -49.9821 | 2026-09-24 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 72221038-03a1-334d-b408-a57b2ea41c27 | -3.1637 | -54.6054 | 2026-09-24 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 554c630d-245a-3413-ada9-23c892fda6dc | -6.6331 | -59.9265 | 2026-09-24 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7910646a-433c-3ad2-bad2-bfd03cca3d7e | -10.111 | -46.0209 | 2026-09-24 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f943d832-528b-3a1d-a1c8-88998f6d6900 | -6.633 | -59.9457 | 2026-09-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1333614b-0b26-31a9-96a9-9dbffb339867 | -3.6947 | -60.5645 | 2026-09-24 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9c05a1da-e69b-3fe6-9b7d-ca2c7e75bfe7 | -3.457 | -60.5692 | 2026-09-24 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 535966b1-ce76-38d3-849d-85eab4a02a68 | -3.4392 | -50.0896 | 2026-09-24 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 67f27c13-87f5-3610-bc3f-e0aa7215551a | -6.6331 | -59.9265 | 2026-09-24 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e09c6ece-55de-3ba1-8ebe-34e993f0155a | -9.4953 | -64.0316 | 2026-09-24 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| d8e7bc8a-4937-3bf9-94bb-5a365a887a97 | -6.6146 | -59.9272 | 2026-09-24 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 10a7efd1-cfe4-31d1-b006-99de38ca5f64 | -7.7679 | -72.9879 | 2026-09-24 01:00:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2a4fd5ca-9a15-361e-a280-b7875a8e1afb | -6.0741 | -47.2703 | 2026-09-24 01:00:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 152faf5e-1298-3281-87f4-28d8e3a3cdc5 | -8.2616 | -54.7776 | 2026-09-24 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| af5aa9d2-7e2c-3b92-a943-efe8a5f63512 | -6.4303 | -59.9532 | 2026-09-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| ffe53d66-5d29-3fa1-9f40-1ec7e41acf0d | -11.9583 | -50.7607 | 2026-09-24 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| af0146ad-e656-3201-ac32-8bb49dbf2931 | -9.0158 | -60.5138 | 2026-09-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 3b1fe604-ce7d-3a61-a1d7-1ca86f5a2b1c | -9.8677 | -48.5126 | 2026-09-24 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 6d4ea144-2c66-3ef2-ba4a-7708e08e8527 | -9.695 | -64.9081 | 2026-09-24 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| e69b6b78-49b1-3c58-9dae-882c46a99a11 | -9.6949 | -64.9269 | 2026-09-24 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 8e83ebfd-8098-33a9-9311-9e9029c10ca6 | -5.7756 | -45.0826 | 2026-09-24 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| ce627856-c4a8-3366-9541-cd47af109d47 | -10.2637 | -49.9626 | 2026-09-24 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 41f39425-801e-3451-b67c-4e682499d667 | -12.4216 | -46.9551 | 2026-09-24 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 43d7ed9c-1e10-3ac1-8f05-1009aef22311 | -12.4024 | -46.9579 | 2026-09-24 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 03562d2e-aebe-3d86-a712-219f7a90c417 | -11.9586 | -50.7393 | 2026-09-24 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| fa34b4e5-62c8-3360-8864-04027a2e757f | -3.6947 | -60.5645 | 2026-09-24 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e064682a-379b-3a0c-b818-b679336345d7 | -3.4577 | -50.089 | 2026-09-24 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 42da35ec-3507-3461-91ac-faf08427c086 | -15.5686 | -42.3547 | 2026-09-24 01:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8acc46f8-e662-377f-91cd-38c0d6bb08c0 | -6.4302 | -59.9724 | 2026-09-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 205c1b3b-27e5-3b18-9f50-1faa6da4de03 | -5.7754 | -45.1053 | 2026-09-24 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6ebab85e-27d6-30c5-a573-1cb401fe3d3a | -3.6764 | -60.5649 | 2026-09-24 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0a8f9df9-1912-316b-937a-1227ead642f2 | -10.2824 | -49.9821 | 2026-09-24 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 786f56e6-1ce9-37fb-bc94-5a3a29702c15 | -9.8491 | -48.4927 | 2026-09-24 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 239bf4e2-aa0e-3670-a170-27014e4e7877 | -11.9392 | -50.7629 | 2026-09-24 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 90732365-fb41-36de-bdc4-6a8cee7e4b75 | -6.5962 | -59.9279 | 2026-09-24 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 207b118b-f7b7-30ee-beef-e61779214f2b | -6.6148 | -59.908 | 2026-09-24 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| d34cf18b-1a6c-356e-8965-86ca1c8a8254 | -9.868 | -48.4907 | 2026-09-24 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3ba5daff-fdb1-3a9e-ba52-8af38f9e0bbc | -6.6775 | -58.5748 | 2026-09-24 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| a74d4d6f-fa82-3754-b7a4-03e076a82335 | -3.6946 | -60.5835 | 2026-09-24 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 86328571-dec6-3799-ac79-62412dca76bd | -10.111 | -46.0209 | 2026-09-24 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 0d388d47-3586-35ed-8cdd-c579a96102eb | -3.6763 | -60.5839 | 2026-09-24 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 83ac60e6-b6f4-394f-9d92-45b144176c99 | -14.5916 | -45.624 | 2026-09-24 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7759ab2c-acc7-3ee2-bebe-6257fcdebfe8 | -3.9169 | -59.6641 | 2026-09-24 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| d78fd12c-f4da-3b51-acc5-7295c9023087 | -9.043 | -48.1384 | 2026-09-24 01:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| d479fd02-08d4-35fb-97fb-ec7bb46e2c51 | -6.0739 | -47.2922 | 2026-09-24 01:00:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 27aab9d5-dd16-3143-9977-9c630ff19607 | -3.6947 | -60.5455 | 2026-09-24 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1b0661b8-e06c-3bb0-9637-468788e8e2a0 | -3.4578 | -50.0679 | 2026-09-24 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 404c06bb-918d-329c-87ac-abff0334c7cf | -10.1107 | -46.0435 | 2026-09-24 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| aa607557-05a8-3c27-b435-a46c009df955 | -3.1637 | -54.6054 | 2026-09-24 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| fd801ce9-4466-3d4a-9432-e9f69bb96aeb | -6.4486 | -59.9717 | 2026-09-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 65d3aa62-85c6-3ffa-a47f-f4b5ce686646 | -9.8488 | -48.5146 | 2026-09-24 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| a1103b4b-ac29-32f9-aaa6-bb999d23b8d1 | -10.0917 | -46.0458 | 2026-09-24 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 96d28e89-ef3a-3aaa-b8ff-4d9c3a43c6a4 | -9.0157 | -60.533 | 2026-09-24 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 56e9f1f5-2e1f-3859-b4f4-fbb9967ac91e | -10.2827 | -49.9606 | 2026-09-24 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 70d76c46-52db-3fca-847e-eb0cfad07c79 | -6.633 | -59.9457 | 2026-09-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3d81d985-f77e-3bca-9a28-5d4147a47632 | -4.1181 | -51.0695 | 2026-09-24 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 0ed7c1a1-70ca-3c6f-bf30-bbec6a28b209 | -6.789 | -48.6779 | 2026-09-24 01:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 03ebfc1a-a41c-3d40-84b3-4f56681085a0 | -10.0921 | -46.0232 | 2026-09-24 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 5b4bbf16-4525-333b-9076-49b6571b7411 | -3.4387 | -60.5695 | 2026-09-24 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ed16e029-7dab-3913-bcbe-0da450b459d2 | -6.0928 | -57.6262 | 2026-09-24 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 9865ff9c-c6f3-38a6-a20f-e1f46f06246a | -6.3501 | -57.7717 | 2026-09-24 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| ecc25958-7b2f-3e10-a92a-83e5914615cb | -6.4487 | -59.9526 | 2026-09-24 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| fb375f52-9f02-36d0-9368-1d3876efe201 | -6.6145 | -59.9464 | 2026-09-24 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 93cab925-2481-32c2-a2c4-2578d78212cc | -10.9115 | -53.9429 | 2026-09-24 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 57bf9130-90ea-3765-9b8b-6fbe4e5bf5f5 | -10.1114 | -45.9982 | 2026-09-24 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 186b5d0f-45e1-361c-9754-251aa71ce401 | -4.118 | -51.0903 | 2026-09-24 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a2f5f6e5-0aac-3724-ac8c-774322f12840 | -10.0924 | -46.0005 | 2026-09-24 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 2f6d7dc8-4176-3503-b1b2-43b7e6b98aec | -6.0552 | -47.2935 | 2026-09-24 01:00:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| fb0f3408-e22a-3757-84f4-002f61cf0720 | -6.0554 | -47.2715 | 2026-09-24 01:00:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9a16047c-05dd-30d4-897b-be2ed7435d20 | -4.2951 | -49.1234 | 2026-09-24 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c1ef90b1-b016-3088-9c2d-106f44468b8d | -10.2824 | -49.9821 | 2026-09-24 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e887b336-f8a2-3adb-b6b6-d33920a071b7 | -3.6764 | -60.5649 | 2026-09-24 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f2060ded-01bf-3890-a916-13ac15ed3d50 | -8.2616 | -54.7776 | 2026-09-24 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b1a76c37-d399-3bc2-b4a9-a9f17b973d0b | -6.633 | -59.9457 | 2026-09-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 2952e693-ef42-32c3-b7c2-d570ad8c536a | -9.0158 | -60.5138 | 2026-09-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 83ddfeb9-a933-300a-8c8b-022345e33b5c | -7.7679 | -72.9879 | 2026-09-24 01:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c419ba83-4b4a-353e-922c-711242134efc | -6.6331 | -59.9265 | 2026-09-24 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e010e415-ef7a-3ad7-96c3-50a93d7846c1 | -3.457 | -60.5692 | 2026-09-24 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| ea4f5aa5-77b9-3323-b1c3-d3e58128a3a3 | -10.1114 | -45.9982 | 2026-09-24 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9f537d5a-f52b-3344-bf05-3f7d5073fe04 | -6.6146 | -59.9272 | 2026-09-24 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 735bcc9b-6836-30f9-8f0f-7669beb0b2bf | -11.9586 | -50.7393 | 2026-09-24 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1a03e507-c382-3fb4-b867-14977067d170 | -6.5962 | -59.9279 | 2026-09-24 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 7b7ae418-de06-3d5f-be33-6db5e629a54c | -4.118 | -51.0903 | 2026-09-24 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |


[Clique aqui para ver as próximas entradas](README22.md)
