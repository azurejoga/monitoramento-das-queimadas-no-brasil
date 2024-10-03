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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab2ca140-1432-3bc6-8a42-304151d2448e | -4.4657 | -42.8877 | 2024-10-03 00:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 1341bbba-3ee5-39ad-8182-462605527ca6 | -4.5375 | -43.304 | 2024-10-03 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 91ad4822-524e-3cae-92f1-8b051af0860d | -4.58 | -48.0132 | 2024-10-03 00:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 6d76a80c-cf3a-38a6-af59-5894f9f8aff0 | -4.9264 | -43.79 | 2024-10-03 00:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 7f21e17f-1aac-39cf-8831-befe08151653 | -4.9265 | -43.7669 | 2024-10-03 00:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| bc325053-dfcd-3b84-ba95-7f89fd6847db | -5.2253 | -43.8164 | 2024-10-03 00:35:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| a9226b82-3c90-3c2c-8094-b8ca90f554f6 | -5.2255 | -43.7932 | 2024-10-03 00:35:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 4806b423-9eb7-35aa-9ee7-0946a8d7dc4e | -5.2441 | -43.8151 | 2024-10-03 00:35:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 616.3 |
| 209fa40f-ab09-3e77-9912-2c47e91670a4 | -5.2443 | -43.792 | 2024-10-03 00:35:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 687.8 |
| 9e20b550-d734-3ec2-8c82-1f4a34aa1c2b | -5.2628 | -43.8138 | 2024-10-03 00:35:36 | GOES-16 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 341e24f7-d260-376e-b575-e02c409a3c8c | -5.263 | -43.7907 | 2024-10-03 00:35:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 998b3a15-a3f2-3d38-a68e-f7b49eae6544 | -5.8545 | -44.6217 | 2024-10-03 00:35:39 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 5932ceae-87b6-36f5-8aaf-3844648f5bec | -5.8547 | -44.5988 | 2024-10-03 00:35:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 72a02e24-931f-3722-8c14-519490576c0c | -6.6453 | -54.952 | 2024-10-03 00:35:44 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9da81934-1bef-3663-8604-ac3076eb95f1 | -6.8777 | -59.0504 | 2024-10-03 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4e9a8846-f0ae-33ea-aa98-bcd2b981c82e | -6.8778 | -59.031 | 2024-10-03 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8ce1c14e-3106-3ee1-b453-ff3c38c88a87 | -7.1871 | -59.7893 | 2024-10-03 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 9a3a5c1c-7a05-3ffc-b765-ab526f432224 | -7.2056 | -59.7886 | 2024-10-03 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4e4382d7-31f5-3048-b66e-87052b6b3550 | -8.4248 | -46.3865 | 2024-10-03 00:35:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f14599a2-8d27-38cc-83cc-3e80a7a50983 | -8.425 | -46.3641 | 2024-10-03 00:35:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ee366220-3b1b-382e-a6ec-d03e4ddd3376 | -8.8506 | -45.5086 | 2024-10-03 00:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| f61cd72d-4619-314a-9f52-3c1833c05dde | -8.8695 | -45.5066 | 2024-10-03 00:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 1b4b9569-5d98-3b28-a83e-6f09e607b255 | -8.6488 | -66.7139 | 2024-10-03 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 0c7942ff-4e6b-3041-98ae-0c1fb1f9d9db | -8.6489 | -66.6953 | 2024-10-03 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| de2e0b22-b0c7-3fa6-80d0-a45641cff986 | -8.649 | -66.6767 | 2024-10-03 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| fcfc5e42-bcae-31c1-b503-49f21ef12ebf | -8.6674 | -66.6948 | 2024-10-03 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 37fa238a-9bc8-3350-bb18-7b6b264f3308 | -8.6675 | -66.6762 | 2024-10-03 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 344da7fe-3e84-3ab5-afb3-4eb221bf9129 | -8.8926 | -62.3348 | 2024-10-03 00:35:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 347a5d84-7ae9-3807-b228-a194f956dc56 | -8.9976 | -67.4094 | 2024-10-03 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| da1e83eb-64ed-3484-a4df-af47a202a565 | -9.0149 | -67.7423 | 2024-10-03 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| f5ddd0cd-b5e0-3c59-9285-b593d58f0f89 | -9.0334 | -67.7419 | 2024-10-03 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1667fcf3-fd35-3bd3-90d6-2b271fa9e5d5 | -9.0515 | -67.871 | 2024-10-03 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 0c909805-991d-3be7-a9fa-286d10d46ff8 | -9.0516 | -67.8525 | 2024-10-03 00:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| ca3df1ee-bda5-3396-9fc9-80c279dc12b2 | -9.1566 | -61.6758 | 2024-10-03 00:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c7ac2327-4fcc-3558-8659-71ed9b502dd4 | -9.4574 | -40.3641 | 2024-10-03 00:35:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 7f61dbf2-5ab8-3607-8f00-8a2dbfed371d | -9.1752 | -61.6749 | 2024-10-03 00:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 514d158f-84e2-33b1-bf96-89ea21dba033 | -9.1754 | -61.6558 | 2024-10-03 00:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 08a96c4a-ecd7-3cd1-a17e-142d30788cff | -9.2739 | -67.8286 | 2024-10-03 00:35:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| fc2f04e4-c003-3c91-98e1-146f884ce3cf | -9.3839 | -61.0526 | 2024-10-03 00:36:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| c6c972de-9c2e-3952-8564-513bff5ade3e | -9.3681 | -67.3998 | 2024-10-03 00:36:00 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8c102313-b25a-3a20-a05e-c361b40cf0dd | -9.4025 | -61.0517 | 2024-10-03 00:36:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 57dee6f3-7d3b-3e87-b9be-04d13016ea6f | -9.3833 | -68.3256 | 2024-10-03 00:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 32.2 |
| c4063b03-85ac-363d-8d90-9caf699df235 | -9.4244 | -67.2313 | 2024-10-03 00:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 4b45d239-5e8b-3a1c-8702-19c5216e79d5 | -9.4367 | -64.5607 | 2024-10-03 00:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 942cb889-2062-3545-b5fa-3ff898fb9434 | -9.4368 | -64.5419 | 2024-10-03 00:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 147.0 |
| a999fbff-cd2e-3423-bdcd-061f3e6d59c6 | -9.468 | -62.3857 | 2024-10-03 00:36:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 596fbe31-dae1-37d1-b65b-541a74693618 | -9.4865 | -62.4039 | 2024-10-03 00:36:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8cccd812-0816-3f85-b3b4-6dcc3d565344 | -9.4866 | -62.3849 | 2024-10-03 00:36:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 9d8f0975-10bc-33fb-a256-0368e74352d2 | -9.4939 | -68.508 | 2024-10-03 00:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d1b208cb-0f8c-302e-b09e-22c26b851ab1 | -9.494 | -68.4895 | 2024-10-03 00:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a13bac59-63f2-3db8-bc00-b7cb4d2dd4af | -9.5125 | -68.4891 | 2024-10-03 00:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 773c638f-8000-3f14-82a1-0b996c24aa70 | -10.145 | -36.1406 | 2024-10-03 00:36:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.0 |
| 15856a2c-afd9-3c8c-88fe-892a210c98e4 | -9.7173 | -64.2302 | 2024-10-03 00:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3fd44394-0d44-39ae-b77e-30e200945201 | -9.9067 | -67.3294 | 2024-10-03 00:36:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 57392d4f-9b1b-3b71-893b-48b604ac9c9e | -10.129 | -56.7722 | 2024-10-03 00:36:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 66c87ab3-4444-323f-9ad2-f697ae23ff33 | -10.1292 | -56.7523 | 2024-10-03 00:36:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e2d40879-2b4d-31bd-8f2e-54bedafeafb7 | -10.1615 | -57.2861 | 2024-10-03 00:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e213af7f-e02b-305a-9776-f842d7af1cb9 | -10.1617 | -57.2663 | 2024-10-03 00:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3fa8d423-c5df-38c0-a69c-a355e9d0b4ac | -10.1802 | -57.2848 | 2024-10-03 00:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ee189302-9a2a-30b3-b3f2-2a33308c3dc1 | -10.1804 | -57.265 | 2024-10-03 00:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| c050984d-998a-3556-a47f-ae41f17b6a1b | -10.6505 | -53.6994 | 2024-10-03 00:36:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 33746d02-2289-35af-b5e3-b8fa1259beb7 | -10.9769 | -46.5443 | 2024-10-03 00:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| da7d2b0d-a30b-39ed-bcb9-599cf2e64f73 | -10.8942 | -63.8971 | 2024-10-03 00:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 3c54e0c3-5dab-35d9-85d6-fef32e6ed05d | -11.2567 | -46.9123 | 2024-10-03 00:36:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 37461bf1-66e8-3562-85f3-89e799742f9e | -11.2758 | -46.9098 | 2024-10-03 00:36:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 24c8501f-3f07-3291-8a00-7ef8104efa27 | -11.2379 | -60.5837 | 2024-10-03 00:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 187918b0-285a-3cd4-97ba-b619da6cfe02 | -11.2565 | -60.6019 | 2024-10-03 00:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 9f8bebf2-6cf1-329a-8b1c-9db1788ed1cc | -11.2566 | -60.5825 | 2024-10-03 00:36:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 31225746-e23c-33db-844e-db3a9be382f4 | -11.5982 | -65.1527 | 2024-10-03 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4e984152-d0dd-33d1-9d0b-ea161dc8b4cd | -11.617 | -65.1519 | 2024-10-03 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c519d18b-0fb1-3b9d-926b-78318b0c6f09 | -11.6742 | -65.0172 | 2024-10-03 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| dfcd3113-98bc-3049-a7b3-48e80b2f8f99 | -11.693 | -65.0163 | 2024-10-03 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8bf28637-d588-399b-8b94-9e96b201c7e8 | -11.9876 | -57.1877 | 2024-10-03 00:36:14 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d9fc4389-1b96-34bb-8f6e-c12708d5dc11 | -12.2668 | -45.958 | 2024-10-03 00:36:15 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| f6e13e1d-17d7-3f68-9cbd-6ad8a00f645e | -12.3851 | -62.9828 | 2024-10-03 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d66a355d-a1e9-3265-8123-284a1987f520 | -12.4038 | -63.0009 | 2024-10-03 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 99800012-c3cb-3775-8396-8760d6fccd5f | -12.404 | -62.9817 | 2024-10-03 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| f477a11b-b25e-3d44-b903-44d034ac13cc | -12.5332 | -53.1003 | 2024-10-03 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| cf53f754-5cc4-39ad-b2c9-ad5c31d5193c | -12.6484 | -63.1214 | 2024-10-03 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 121.8 |
| d203714d-4b74-3ed4-877d-372ec3d762f7 | -12.6486 | -63.1022 | 2024-10-03 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 42248ab4-55a8-3712-94f3-dc1b18ffcba1 | -12.786 | -62.4982 | 2024-10-03 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 25f7b389-c64d-36fb-a8d6-6f5f24d0e49e | -12.8047 | -62.5163 | 2024-10-03 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d0a36ff1-b2a2-30f1-8d53-c37f3a9b2454 | -12.8049 | -62.497 | 2024-10-03 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 9479ce38-4378-3ac6-9ca5-4e4fdd070297 | -12.824 | -62.4766 | 2024-10-03 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 665e8b85-263c-3927-b7ac-b6d74edfd08e | -12.9741 | -62.6409 | 2024-10-03 00:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 397f1a80-c9d2-3f79-a606-82317d1cf957 | -13.5195 | -51.1467 | 2024-10-03 00:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| a8bccfa9-c540-31f5-ae20-5adf1ce0c4c7 | -13.5369 | -51.2514 | 2024-10-03 00:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6c53bd97-928a-3044-9750-320e75257f77 | -13.5373 | -51.23 | 2024-10-03 00:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 202365bd-630e-386b-ac9a-3f09254c4956 | -13.5558 | -51.2704 | 2024-10-03 00:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 86de67ac-8b93-3e55-9bd8-5e81904a1b70 | -13.5562 | -51.2489 | 2024-10-03 00:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 3eb07e03-2fa6-342f-9ecc-16fa9d29e97a | -13.5565 | -51.2275 | 2024-10-03 00:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 7d4953f8-898d-377d-8383-840f6de48c91 | -14.522 | -45.2414 | 2024-10-03 00:36:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f681cb50-2b96-362b-a6e8-3c4e9752ba24 | -14.5225 | -45.218 | 2024-10-03 00:36:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 4efe232d-6f06-351d-86c2-6e78c79583c8 | -15.2332 | -47.5032 | 2024-10-03 00:36:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 697f870e-d734-3126-9170-ce9b189ae82c | -15.2528 | -47.4999 | 2024-10-03 00:36:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a4bf6a41-c48a-3870-8f36-3d507abc665d | -16.7594 | -57.8328 | 2024-10-03 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.5 |
| f1c9dbc0-347c-3286-94aa-29f8db09c927 | -16.7597 | -57.8124 | 2024-10-03 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.2 |
| 0c033b3e-729b-3ff7-9adc-d824150dd189 | -16.779 | -57.8306 | 2024-10-03 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 3a5fa365-0d4f-3e6b-ab67-701bf7772145 | -16.7793 | -57.8102 | 2024-10-03 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 20f0b11e-81e5-3ee4-88ef-aa73c271a21f | -16.7985 | -57.8284 | 2024-10-03 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |


[Clique aqui para ver as próximas entradas](README20.md)
