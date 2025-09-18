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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfb973a4-8880-3dda-a6f0-7dbd7fdccdc7 | -8.669 | -46.4291 | 2025-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 995425e3-f45d-3f7f-90f9-37193139a9e2 | -9.1895 | -46.9994 | 2025-09-18 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 40f7a35b-2de7-3754-b3bf-1112cfd9d99b | -10.6551 | -46.4501 | 2025-09-18 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 9e3dce40-585d-307b-8c59-c0c2e3deef92 | -8.9347 | -46.2894 | 2025-09-18 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9bb7f81c-dd44-3a72-a85d-a2f6f28e85a2 | -6.9212 | -44.764 | 2025-09-18 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 54b2d8a5-1bfb-3b9f-a20b-865b2657e4b8 | -8.9638 | -45.519 | 2025-09-18 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7118f3e4-59d2-36be-b199-a89580895a86 | -8.0092 | -44.9589 | 2025-09-18 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4ef2affe-6d53-3fd7-b56b-49fb777da073 | -8.9722 | -46.3079 | 2025-09-18 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ffb57e6a-98c1-3941-88bb-ddcb7d49077f | -8.3523 | -44.6487 | 2025-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| dcad6745-9548-3a9c-82a9-547f66701ea0 | -8.6268 | -45.3054 | 2025-09-18 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 24aa872b-e171-3866-b4c5-663fed1deb27 | -15.8233 | -59.4016 | 2025-09-18 13:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| dd4e747d-7edf-301a-a991-bf60aa629a60 | -8.7868 | -46.0578 | 2025-09-18 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a5b51949-f42c-3a5b-bc7c-233dd7beae93 | -8.6885 | -46.3823 | 2025-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8affe4bd-e406-3db1-a20a-7eeb32f3a94c | -8.0196 | -45.662 | 2025-09-18 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cc9a3b65-4104-3463-893e-af4b70f2c533 | -7.5412 | -44.7532 | 2025-09-18 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 71685679-1669-3a81-a16f-d2fb611d2602 | -7.9471 | -43.8828 | 2025-09-18 13:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 85b4bd9f-a030-3f3e-a2af-774d040b801c | -6.0599 | -44.6747 | 2025-09-18 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 08c84588-a728-3935-8a94-0906b7b3bf36 | -7.5159 | -45.3251 | 2025-09-18 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 6d48a790-d8f9-36e2-ac8b-75cbb0ef5d39 | -15.8236 | -59.3816 | 2025-09-18 13:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 44229aa4-844c-3151-83bb-9f642ee1bd1f | -10.6741 | -46.4477 | 2025-09-18 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 09af6b8a-8382-3ec0-b0fa-5763219bd28f | -8.0199 | -45.6394 | 2025-09-18 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 05f69a1b-a792-3e06-bf98-8138f5ec02ce | -19.5872 | -57.7557 | 2025-09-18 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| 15bf4089-3b6e-3d13-88a6-eca93d0882a0 | -7.6574 | -44.4667 | 2025-09-18 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f4467b18-caa5-34ca-b5f7-1f460e918286 | -8.669 | -46.4291 | 2025-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5362ac26-2631-31b8-a29b-e1b53ef510bf | -15.804 | -59.4035 | 2025-09-18 13:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| dfbf6e50-acdf-3a2f-83ba-90a4c15b4d64 | -8.7262 | -46.3784 | 2025-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| edab341a-9b26-39ff-98fd-f124d2cf43c1 | -19.5869 | -57.7765 | 2025-09-18 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.7 |
| a7a67960-42ad-3b2e-a781-df60c7111d6e | -8.3334 | -44.6507 | 2025-09-18 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6fbc4c55-9fff-365a-9748-bd3436f1afb8 | -8.3523 | -44.6487 | 2025-09-18 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 67ed42bc-0966-391d-9fec-7bac326135d7 | -7.5162 | -45.3024 | 2025-09-18 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| a2ec6388-1976-3e95-911c-fa11f43cf92c | -8.899 | -46.136 | 2025-09-18 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b5de46bc-678c-3927-a471-7e64d59748a3 | -8.9638 | -45.519 | 2025-09-18 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6c13bab5-ac59-3bdc-a50a-dfd051974ff8 | -8.0092 | -44.9589 | 2025-09-18 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 53c60fdc-7a2c-3f26-9cb5-0064c59a3f5a | -8.0281 | -44.957 | 2025-09-18 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 288.2 |
| 13acd4e2-51d9-3b75-8d3c-1b0932ade8f1 | -7.5601 | -44.7514 | 2025-09-18 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8a452b70-88e5-31f5-82e8-ef1d3e148276 | -6.0069 | -44.3354 | 2025-09-18 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c963ee9d-7a39-3837-bf8a-c0fdf4549636 | -10.6551 | -46.4501 | 2025-09-18 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b45e2206-123a-3ef0-ba22-367406f38442 | -9.2084 | -46.9974 | 2025-09-18 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 188.2 |
| f8fc0a79-e981-3630-ad73-703b38014e97 | -7.5818 | -44.4971 | 2025-09-18 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c3328d13-fd3c-39e6-aa69-90e3f635e521 | -8.7076 | -46.3579 | 2025-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d08af923-9f94-360f-af90-c2eb4bb713e1 | -7.6386 | -44.4686 | 2025-09-18 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 9d58cd09-3850-376e-b1c2-7170a98901c5 | -8.4645 | -44.7286 | 2025-09-18 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 1a6c9e31-9527-3f6b-bf37-33f79254b5a3 | -8.7073 | -46.3804 | 2025-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| f48889e0-7c25-3a10-b348-434e63c79b78 | -6.9978 | -44.62 | 2025-09-18 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| cd61b276-f09b-3eb5-9622-ea4357cc8d40 | -7.535 | -45.3006 | 2025-09-18 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 50be8597-b49a-3821-a558-7412257cf70b | -8.7076 | -46.3579 | 2025-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4a3ef513-5d33-3632-9f2b-334464479fa8 | -8.0281 | -44.957 | 2025-09-18 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 6507f039-0cdc-33d3-bf50-20c273d77e7a | -10.0371 | -47.1952 | 2025-09-18 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2e1a02c1-301f-3322-858e-6174269bb7fc | -8.7868 | -46.0578 | 2025-09-18 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d3527ed0-3301-3cdb-95a8-8951425292ca | -6.0599 | -44.6747 | 2025-09-18 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 14a14fd7-079b-3a9a-a6d5-17dcf39f4bc4 | -8.6027 | -45.7162 | 2025-09-18 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ff46deff-49ce-3611-a0d1-eee971b08298 | -6.9024 | -44.7656 | 2025-09-18 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 89489de1-4fc2-3e87-9fe1-a66faee896c8 | -5.6365 | -43.8796 | 2025-09-18 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5ca5d492-86a1-3bdd-a599-884f1c3edebb | -15.804 | -59.4035 | 2025-09-18 13:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 91f22e7a-6d89-34eb-be2b-97d435e9c84b | -19.5869 | -57.7765 | 2025-09-18 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| e983fdce-ce4b-3640-9122-5e8ead16f8d2 | -10.6551 | -46.4501 | 2025-09-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| bb200e61-555f-3acd-b194-078b5aa06611 | -8.6687 | -46.4515 | 2025-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 77db65ac-3ec1-3677-b6a4-8e4a4b692c3a | -9.0202 | -45.5355 | 2025-09-18 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| fc46271d-d89a-3077-aa7e-6e438f8e9b0a | -8.9719 | -46.3304 | 2025-09-18 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 45f0a8ef-0dfd-3587-b726-4d383a7091f9 | -7.5162 | -45.3024 | 2025-09-18 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 822d6d37-3a0b-3ee9-9f0c-fa6d813d6901 | -19.5872 | -57.7557 | 2025-09-18 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.9 |
| dcffb756-06ae-3a3e-94be-411daa0a808f | -6.0069 | -44.3354 | 2025-09-18 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 53dcf4b7-3fa3-3d56-bffd-1ae5e002d3aa | -8.9638 | -45.519 | 2025-09-18 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| f298a31e-d49b-3e0b-a441-3b642ab1f126 | -7.5412 | -44.7532 | 2025-09-18 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 933576cf-b31d-3428-9557-c005274e644d | -7.6574 | -44.4667 | 2025-09-18 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 6dd33b2d-5e18-3b3b-aa9b-e4917105cb98 | -8.9344 | -46.3119 | 2025-09-18 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 399f86c9-2c53-3875-9adb-604802a1405c | -8.6268 | -45.3054 | 2025-09-18 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7aa0297e-b59e-32d5-8f42-9caf6042009f | -23.974 | -48.9009 | 2025-09-18 13:30:00 | GOES-19 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 9cdb9355-6d36-3dcd-9537-48a446c7249a | -6.9978 | -44.62 | 2025-09-18 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 188b7791-a952-30cd-a5c2-baa5b24b40aa | -9.1239 | -44.862 | 2025-09-18 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 30623254-0d07-3aca-ae6f-d5530b4a2b11 | -8.0196 | -45.662 | 2025-09-18 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0bb14dcd-b43a-348a-b4b0-9455272f8290 | -8.4831 | -44.7495 | 2025-09-18 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 03a601b0-08a4-31bb-a05e-357896c68531 | -6.9212 | -44.764 | 2025-09-18 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| f5eb447a-e3e1-36ae-a7bf-ea3dfda7d7af | -8.899 | -46.136 | 2025-09-18 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 989465f4-d746-3f0a-b135-8622d1cdcab3 | -9.1895 | -46.9994 | 2025-09-18 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 4272aaaa-d56f-313a-9aad-22a469bd451f | -8.4645 | -44.7286 | 2025-09-18 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 732a629a-4728-3d91-bce9-347b47329dd3 | -8.7866 | -46.0804 | 2025-09-18 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8419415f-0dff-3939-8804-10f53e33b989 | -8.0092 | -44.9589 | 2025-09-18 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1306a37d-88f9-3221-b1f6-21aacffd02c3 | -7.8509 | -45.6105 | 2025-09-18 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 87ece86f-4ef2-3d11-bef4-cdd5c5ee10e6 | -7.5601 | -44.7514 | 2025-09-18 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 0c736769-2d32-36db-888c-56089e52b82e | -9.2084 | -46.9974 | 2025-09-18 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 80d0dc94-79d1-337b-975f-239cec2f00f8 | -7.5818 | -44.4971 | 2025-09-18 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 83fe3dfe-ac34-30ec-a89a-71ca23828e1f | -6.0071 | -44.3124 | 2025-09-18 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 71621ec1-9ca3-3923-8b9a-99bb5085b6d3 | -15.8233 | -59.4016 | 2025-09-18 13:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| d9ad7535-78df-3e7f-a742-1a775e2687df | -8.7073 | -46.3804 | 2025-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.6 |
| b3b0c854-2334-3068-9091-2a22f606ff25 | -7.8698 | -45.6087 | 2025-09-18 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 94105911-709b-3f5c-8411-09df381c196e | -7.6386 | -44.4686 | 2025-09-18 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 8a982fcd-96c1-3181-b6d2-0778535679f5 | -10.6741 | -46.4477 | 2025-09-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 32d9702e-1064-3c7f-a37e-438048bb5623 | -8.0199 | -45.6394 | 2025-09-18 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 523c549d-1375-35dc-8cb6-9958aaa3a40c | -8.669 | -46.4291 | 2025-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8b913f0d-9085-35ef-bc4f-26ad04d5dafc | -15.8236 | -59.3816 | 2025-09-18 13:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 2358141f-94bd-3871-9f70-03a5e6cc8e22 | -8.3523 | -44.6487 | 2025-09-18 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 3451d220-efc6-3bfe-b751-bbdfdb3a72f6 | -7.535 | -45.3006 | 2025-09-18 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0a9e94ea-2727-34ee-925d-3a8605a26607 | -8.7262 | -46.3784 | 2025-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 05192ece-b74c-31ca-83fd-d7cd9feca255 | -11.4849 | -43.6166 | 2025-09-18 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| c7905800-0200-35fe-91da-ea6908d0838f | -8.0092 | -44.9589 | 2025-09-18 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ed052a0b-6121-3f96-8e2b-ae7026fe83b2 | -18.5781 | -45.0334 | 2025-09-18 13:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c874e829-bc42-387f-83cc-2a62f1fcf50c | -6.0599 | -44.6747 | 2025-09-18 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 13671d88-ca24-3ed1-a86f-0c6dfadc6dff | -11.5041 | -43.6136 | 2025-09-18 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 13ea22e8-f70e-304a-9192-3df9e046da1d | -8.3523 | -44.6487 | 2025-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |


[Clique aqui para ver as próximas entradas](README36.md)
