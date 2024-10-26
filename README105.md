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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bc0fa5f-b0d8-3938-a56a-1109a1eb2132 | -3.4729 | -43.3377 | 2024-10-26 13:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 261.0 |
| 0487fa00-1249-3b13-a8a2-cbd47193bde6 | -4.1949 | -44.2476 | 2024-10-26 13:35:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3ac21c0b-0b9d-3d76-aa93-993db21205b4 | -5.7308 | -43.8032 | 2024-10-26 13:35:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 18ca512c-ce62-30c8-92f9-0bb0cab25ca3 | -5.7306 | -43.8264 | 2024-10-26 13:35:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1ec75e46-4c19-3495-9aa0-100bcb977930 | -12.6444 | -42.3498 | 2024-10-26 13:36:16 | GOES-16 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 5def61e0-5d95-37f7-9574-89f832a19a9a | -12.9504 | -42.5129 | 2024-10-26 13:36:18 | GOES-16 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 372aef9c-2238-3fc9-8e1e-9284d5a2ffbb | -13.7652 | -42.5063 | 2024-10-26 13:36:22 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 67.9 |
| ca1af6e6-a989-3628-8936-d1efd9df3c16 | -14.0477 | -43.7983 | 2024-10-26 13:36:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 49474483-18d1-3bdb-a980-bb3d4ed1d512 | -14.5321 | -43.0582 | 2024-10-26 13:36:26 | GOES-16 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 48c796dd-2d7f-38ee-95f5-d1020b2f1ae3 | -14.8574 | -43.3546 | 2024-10-26 13:36:28 | GOES-16 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 8b842706-ba7a-370d-b9a0-1a2f7a7a220e | -15.9525 | -43.5366 | 2024-10-26 13:36:34 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 37e432b3-5c5e-3cbf-9138-6a41458b3ade | 3.6185 | -51.2955 | 2024-10-26 13:44:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 657337a9-a2ee-3c27-9e69-a8715d489c7c | 1.7959 | -50.4677 | 2024-10-26 13:44:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 67.4 |
| da969cdd-2f4d-3892-8fca-66f1c15380e9 | -2.2114 | -53.6828 | 2024-10-26 13:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3fb15e7c-c297-3d90-81cc-3067da30001d | -3.0573 | -44.4377 | 2024-10-26 13:45:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8eb6b2f3-8c9b-3109-82fe-78703b5d9ce3 | -3.4917 | -43.3136 | 2024-10-26 13:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| df73ac62-8f67-3a05-915e-c0b76ccf0f53 | -3.4729 | -43.3377 | 2024-10-26 13:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 358.8 |
| 994bcdbe-1196-3ec8-af99-3fee97c55a44 | -3.473 | -43.3144 | 2024-10-26 13:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 461.1 |
| 92903305-6da7-317a-a633-f2336c61e183 | -5.7308 | -43.8032 | 2024-10-26 13:45:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| b5eb671a-0676-3870-9b4e-96fa4fbafde4 | -5.7306 | -43.8264 | 2024-10-26 13:45:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 90f817e9-7c8f-322f-9d02-7fe4ae20eabb | -12.9504 | -42.5129 | 2024-10-26 13:46:18 | GOES-16 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 92.1 |
| adf4fdca-6eab-3fac-8515-ccefdda0936b | -14.0477 | -43.7983 | 2024-10-26 13:46:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c7748d63-c5dc-30f6-996c-c1417d46a05d | 3.6001 | -51.2961 | 2024-10-26 13:54:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6f140aee-d58b-3a2a-a569-ac5cf287a704 | 3.6185 | -51.2955 | 2024-10-26 13:54:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 4bd69635-4e83-395b-ba52-ea4ed50189ce | 1.7959 | -50.4677 | 2024-10-26 13:54:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e43c2a2c-9496-3a02-acbc-22112c5d9b94 | -2.2114 | -53.6828 | 2024-10-26 13:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ad171d57-cfe9-3c0e-b326-234d8a409165 | -3.473 | -43.3144 | 2024-10-26 13:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 392.7 |
| 5403db36-ff70-361a-bf76-d60d70b94098 | -3.4917 | -43.3136 | 2024-10-26 13:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 238.7 |
| ffd4f569-177f-3e93-8967-d5dd127e6e8a | -3.4731 | -43.2912 | 2024-10-26 13:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8289f231-cc9d-309f-982c-777ef412a573 | -5.7308 | -43.8032 | 2024-10-26 13:55:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| af95b074-7202-3139-88dd-29b1c371816a | -12.7668 | -42.9788 | 2024-10-26 13:56:17 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 63.4 |
| f40bf026-8096-3547-8e8a-d009d02a226f | -13.6686 | -43.3677 | 2024-10-26 13:56:22 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 7bd6e388-125a-3481-9c30-f566a91bb462 | -14.0477 | -43.7983 | 2024-10-26 13:56:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 54a2eb41-0146-366f-8932-3f0e842710cf | -15.7137 | -43.6355 | 2024-10-26 13:56:33 | GOES-16 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 065592a1-fc48-31c2-8e8a-0b3416c65772 | -15.8936 | -43.5251 | 2024-10-26 13:56:34 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ad3139c4-5957-3c20-a17f-40b6a21ffe21 | 3.6185 | -51.2955 | 2024-10-26 14:04:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e0daef7c-843d-372a-bd98-7153e6cb77d0 | 1.7959 | -50.4677 | 2024-10-26 14:04:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c86d2e68-8966-3425-9dee-2dba58094238 | -2.2114 | -53.6828 | 2024-10-26 14:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e0075bb8-0402-3536-a8a0-5014b21c3a5f | -2.7336 | -57.4522 | 2024-10-26 14:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 6e87e29a-a92f-3a5a-9cb6-bb2a233c5ff2 | -2.7153 | -57.4526 | 2024-10-26 14:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 17fd8c35-fdfb-3dd5-b508-d9878651fc18 | -2.7152 | -57.472 | 2024-10-26 14:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 888905ae-164f-3efa-9762-4ce1f07f6da0 | -3.4731 | -43.2912 | 2024-10-26 14:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ac25307a-a647-3fc0-aa4e-8f3a94ec7211 | -3.4917 | -43.3136 | 2024-10-26 14:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 247.9 |
| 18f74a3e-7e4a-30fa-997e-824b38e7aa7d | -3.473 | -43.3144 | 2024-10-26 14:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 448.8 |
| 72f2bff0-2f0e-34d6-ad84-2bc4986a183f | -5.7308 | -43.8032 | 2024-10-26 14:05:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 86578de8-2e98-3f32-bf52-4c42c36a3f15 | -6.1182 | -42.5086 | 2024-10-26 14:05:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 95797de7-84d9-30e7-8a93-a43db05dd148 | -7.41 | -44.7198 | 2024-10-26 14:05:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 635a2d11-8657-3d33-94df-dfe2fe765ce6 | -7.4097 | -44.7427 | 2024-10-26 14:05:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e7509d0d-b172-3d32-bf95-13ec628da9fa | -12.7668 | -42.9788 | 2024-10-26 14:06:17 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 62.5 |
| a67e3ac0-f015-3ba0-b78c-f17e727159f4 | -13.1729 | -42.9788 | 2024-10-26 14:06:19 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 72.9 |
| ddf20d2c-d130-3cc0-94a5-efd61d2dd2e4 | -13.7523 | -43.0884 | 2024-10-26 14:06:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 102.1 |
| b419be45-17d5-395f-ae55-50132d749bfd | -13.7334 | -43.0679 | 2024-10-26 14:06:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 4449a177-5994-3838-8364-913b9f67d5d7 | -14.0719 | -42.7136 | 2024-10-26 14:06:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 5af76377-700d-3821-b22e-1b437eca815f | -14.0477 | -43.7983 | 2024-10-26 14:06:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c3e28463-e657-33e6-b184-a619eb631fe7 | -15.6092 | -40.7774 | 2024-10-26 14:06:32 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 100.7 |
| b8a9ee6c-7922-3c17-89c7-0d81269fb2ac | -15.8552 | -43.4851 | 2024-10-26 14:06:34 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c3cfc644-f5a1-32f4-bc59-d659b151d932 | -15.9333 | -43.5166 | 2024-10-26 14:06:34 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1b3a94a6-7f92-3ddc-8b98-abd9b751783a | 3.637 | -51.2948 | 2024-10-26 14:14:44 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 64738141-cc4b-315d-bbf9-e25a790c98d6 | 3.6185 | -51.2955 | 2024-10-26 14:14:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 69.0 |
| bc9e6117-ac9d-3cb3-bf25-15afa4117235 | 1.7959 | -50.4677 | 2024-10-26 14:14:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 345fa100-2e53-3e2d-80d6-b88e88f1adf0 | -1.1831 | -53.8985 | 2024-10-26 14:15:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0ef5579e-e377-3efc-b9a8-9ab1ffae2af1 | -2.2114 | -53.6828 | 2024-10-26 14:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6128f5fe-904b-3459-9576-e9cc67775707 | -2.7152 | -57.472 | 2024-10-26 14:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8245d5b4-4f36-33a9-8801-25d708c7542b | -2.8055 | -42.4769 | 2024-10-26 14:15:21 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| cd23208d-41ca-36d1-9356-5327d91efcb4 | -2.7336 | -57.4522 | 2024-10-26 14:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 140.1 |
| ec643c6c-9a35-3e84-a8fd-72e6c64bdf31 | -2.7153 | -57.4526 | 2024-10-26 14:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| cc766d0b-7dfb-3087-992e-6f37a1fbcd69 | -3.4917 | -43.3136 | 2024-10-26 14:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 310.8 |
| 1babfe43-bcfa-3990-974b-7394029df323 | -3.473 | -43.3144 | 2024-10-26 14:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 406.2 |
| bffdbac6-c5d0-35b5-8813-177f64753950 | -3.4729 | -43.3377 | 2024-10-26 14:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 363.6 |
| 41adb31d-e534-3e19-9eb4-aedd6c0cf8d1 | -3.4731 | -43.2912 | 2024-10-26 14:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 274ef869-bfac-3059-ac0d-ef398f5e7c1a | -6.1182 | -42.5086 | 2024-10-26 14:15:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| fb4a1a71-ef87-3367-acfc-4216e47adee2 | -7.4288 | -44.718 | 2024-10-26 14:15:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| bf8d2391-85b2-3a98-aff2-e317cda0c611 | -7.41 | -44.7198 | 2024-10-26 14:15:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 4ce0d79e-fa72-395e-a10b-ac7ae76a17b7 | -7.4097 | -44.7427 | 2024-10-26 14:15:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c5573ccf-2781-3a55-a090-5c46c6faa7c5 | -8.3387 | -42.8084 | 2024-10-26 14:15:52 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| a0ac6bf6-73af-330b-bc05-7fe70577c549 | -13.1529 | -43.0064 | 2024-10-26 14:16:19 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 46e336fe-241b-35cf-b94a-c9da0ec17c54 | -13.1734 | -42.9546 | 2024-10-26 14:16:19 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 467e7fb0-2760-3f3a-bb3c-3271b7b78458 | -13.6686 | -43.3677 | 2024-10-26 14:16:22 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 7bf4b362-8ee6-3594-a0b1-9d0aecaf3ae4 | -13.7523 | -43.0884 | 2024-10-26 14:16:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 40a023bc-17f5-3674-9307-a079ced25660 | -13.7334 | -43.0679 | 2024-10-26 14:16:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 264326c1-5c40-337b-b145-1d84889ffa18 | -13.8968 | -43.5881 | 2024-10-26 14:16:23 | GOES-16 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8419574e-3b74-359f-863f-71c27ea67ec7 | -14.0477 | -43.7983 | 2024-10-26 14:16:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7d2bfe7e-5e84-35f5-932c-ee25877849b8 | -14.0719 | -42.7136 | 2024-10-26 14:16:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 96.1 |
| ac469624-d4a4-39e4-9184-d8110a27b91d | -14.1855 | -43.7248 | 2024-10-26 14:16:25 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 14d7e81a-1594-34a2-9ff3-a103b3063ac3 | -14.7677 | -43.0109 | 2024-10-26 14:16:28 | GOES-16 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 6a2152df-b069-3fc5-831b-aef687be518a | -15.6092 | -40.7774 | 2024-10-26 14:16:32 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| d0699543-4923-31f3-b6e6-33c85327c998 | -15.8163 | -43.4693 | 2024-10-26 14:16:33 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 8e1a54dc-04d2-3de9-b3bc-40dc48883c19 | -15.8936 | -43.5251 | 2024-10-26 14:16:34 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3a5a1a91-a6db-36aa-8180-7c98c34e45b8 | 1.7959 | -50.4677 | 2024-10-26 14:24:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b79cb30a-c305-39f6-b583-e407911e734f | -2.2114 | -53.6828 | 2024-10-26 14:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| fd226c1c-a367-3f0b-a956-7c9a353968b2 | -2.7153 | -57.4526 | 2024-10-26 14:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c7b54c65-a860-3f6c-b4b2-e78f66005a5f | -2.7336 | -57.4522 | 2024-10-26 14:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 3fe6750f-7b7b-3b52-b855-93219d5b3c3f | -2.7152 | -57.472 | 2024-10-26 14:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 137d6f42-bbab-3e2f-b9f4-d140f8e83aec | -2.8055 | -42.4769 | 2024-10-26 14:25:21 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 58c2d7c7-a63e-369a-b26b-9aaa4eccd0ba | -3.0363 | -54.2683 | 2024-10-26 14:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 562ec1d0-8663-3c68-ac43-b4a76a5a15c6 | -3.473 | -43.3144 | 2024-10-26 14:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 394.3 |
| 8e859794-e6ec-389c-a85b-349ff197d854 | -3.4729 | -43.3377 | 2024-10-26 14:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 9dafd344-cd4b-3079-b092-803b13073d33 | -3.4917 | -43.3136 | 2024-10-26 14:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 208.8 |
| d09922af-0a3f-3100-bb1d-16553d60117e | -5.9921 | -45.9682 | 2024-10-26 14:25:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4cf6fc46-11d1-376b-9ea8-914ded2871a9 | -6.5592 | -41.7062 | 2024-10-26 14:25:42 | GOES-16 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |


[Clique aqui para ver as próximas entradas](README106.md)
