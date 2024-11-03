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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a68a4ce-bdde-318b-9352-2f31670b9244 | -1.22757 | -52.02528 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45289dd5-6cb5-3dc7-aa35-4e76e0889957 | -1.22376 | -52.02469 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5933cc0d-3dcf-355e-8dea-9b4d0a337bc3 | -1.21151 | -52.22992 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41b765de-25ee-3ee2-82ab-aa3add7bb4bb | -1.20599 | -52.1403 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14d0955e-f5e5-3680-b95a-ef232f80dfeb | -1.20529 | -52.14489 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d388def-d065-3e28-aead-1767e281328c | -1.17397 | -52.10006 | 2024-11-03 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 843403e5-a9e0-326a-91c1-16ea47759379 | -1.14172 | -52.77608 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e16a7c0a-f860-3572-82dd-2abcb94d593a | -0.91423 | -53.12961 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8edf761-5539-323e-892b-b9f52ca4c006 | -2.04669 | -51.91932 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfa7b502-0f99-3662-a452-87b63fc58a86 | -1.43738 | -51.93665 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 717babbf-674a-35c9-934a-676a8598d99a | -1.4359 | -51.93433 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f05f2188-fc12-3a75-8acc-cc45e3b050a1 | -1.36079 | -51.96145 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d256c144-2918-3fff-a117-0f396b15b493 | -1.35768 | -51.95615 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1d6e0fe-4c65-361b-8ef1-bb08828651ef | -1.35695 | -51.96085 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4feb0e50-9098-3e88-bdf8-4e8ac25ef770 | -1.35156 | -51.86771 | 2024-11-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4708b21-017b-3b7b-85b8-c3b31901cc6b | -1.19811 | -51.92252 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 59a2b1be-5731-36e0-9233-c1d20dca2a1d | -1.19736 | -51.92726 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8efc455e-32ab-3a99-8839-8ec225e72106 | -1.19426 | -51.92194 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 59e22d18-4e68-3d3e-975a-7f84c1209857 | -1.19352 | -51.92668 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5b740d1a-bce5-31de-8860-84cbd9c480c6 | -1.06492 | -51.90945 | 2024-11-03 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d05aef3-d72a-375f-8c1b-ef718f5a3323 | -1.06419 | -51.91415 | 2024-11-03 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ceb92a73-6bea-31f5-adc6-d11d0de08721 | -1.05829 | -51.72301 | 2024-11-03 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3714f4fd-a973-3cf0-a9c5-da170ad11724 | -1.0568 | -51.73269 | 2024-11-03 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed8f5fd9-77ee-35ff-9752-fc6375f19fa6 | -1.05441 | -51.72241 | 2024-11-03 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 175cc202-42c5-32e1-8fe8-27e485f4489a | -1.05366 | -51.72728 | 2024-11-03 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fde35ed-2431-3efe-8e1a-d4068d13665b | -3.6368 | -52.31216 | 2024-11-03 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b6a2c50-879f-3e13-8f39-d3b35cf2f94c | -3.63316 | -52.31343 | 2024-11-03 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d567a455-cce5-3ccf-ac8b-f306fd14460b | -3.63292 | -52.31159 | 2024-11-03 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec1cdbce-0227-3fc0-a7d3-2aa450be6908 | -3.40152 | -52.47414 | 2024-11-03 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b53f691e-c248-354e-a1d6-29b844e9f289 | -3.34825 | -52.70375 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89afe2a6-b478-356d-b332-434260349922 | -3.31529 | -52.99827 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89ff8e4b-07f9-31fb-85d8-6c4c41ac40ec | -3.31431 | -52.99505 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 775ac6cd-6106-3783-a407-74a8249bdc71 | -3.24566 | -52.36329 | 2024-11-03 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8449643-27f8-31f2-80f3-e5ebd21cc3fa | -3.22459 | -53.64838 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c398a05-b30c-324c-9864-a2b4826c000b | -2.74107 | -52.56205 | 2024-11-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6089cd17-b75e-31cd-a3e6-9b897e38b377 | -2.7084 | -52.85384 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55e0eb7d-7fe1-3bdb-b648-f3e027b056cd | -2.69411 | -53.2886 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dd5bca8-c4e8-33e5-b05f-9d199d6a5818 | -2.69405 | -52.39272 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4f23fef-2aba-3995-b76b-153eda4412a7 | -2.68727 | -53.30879 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a54266c-b9a8-3a70-97a2-96b23fd42869 | -2.68365 | -53.30824 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 553ebf94-26bc-39de-b7ed-29efb3c564e1 | -2.68301 | -53.31238 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a445e200-eb51-3f9b-94d3-36c96817acb0 | -2.68003 | -53.30768 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e574829-87d4-3464-9b00-593bb2b5da0f | -2.66918 | -53.30602 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aefa8ed-388c-369d-a8d9-f951eb3fed87 | -2.66854 | -53.31017 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28c143e9-d4dc-34b9-9f47-4c93a2dd05e5 | -2.66793 | -52.83627 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b675733-5a8a-3322-a9f4-5446aa336e90 | -2.66725 | -52.84064 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2d86ea7-71a7-30cc-be13-1a8ceab6b700 | -2.66684 | -53.29715 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57f16a47-598e-3b55-819a-3ce79e383046 | -2.6662 | -53.3013 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e87849ee-cf85-3cff-a3bb-a32e48637554 | -2.66556 | -53.30545 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6dc4a25-73e5-3321-9804-981e910991c4 | -2.66422 | -52.8357 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d54e0141-b1b4-3df5-9bf8-48d35f14bf5f | -2.66051 | -52.83512 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f2aedf4-7ea2-3dc2-9cc9-6798e2c794b8 | -2.63092 | -52.42814 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8baa10d7-5078-33a5-a3f9-8893b5a2e5e7 | -2.63021 | -52.4327 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f481ebf2-9643-32f4-a240-4235ddd8bf23 | -2.62712 | -52.42756 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e62c50fe-7b51-3310-a5dc-ceee17b06ab6 | -2.62641 | -52.43211 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4865a7e6-bce0-3c35-88c9-14ce5bbcb66c | -2.58102 | -53.17871 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2a2974b-ff23-3304-84fb-2b2b9d1ecb42 | -2.57803 | -53.17395 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e257752-4381-3e27-8e17-5f9cd506d2a1 | -2.57738 | -53.17815 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e3d82d-0517-3be1-9cdc-6101d62fd918 | -2.57673 | -53.18235 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8473e28-232e-37d4-914c-6c20389c638f | -2.57439 | -53.17338 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afedd942-08d6-313d-ad6e-44980ac5266e | -2.57374 | -53.17758 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f889f9e4-3253-38b1-ba3a-e0f9650b3ec1 | -2.5731 | -53.18178 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe2272c9-60e8-35bd-a17a-586af644de33 | -2.5701 | -53.17702 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 808ba5e0-3f0a-3e1a-9d83-91f41b996a99 | -2.56647 | -53.17645 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8688a0f9-210d-30fe-8cb2-873660757979 | -2.50309 | -52.98146 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b677f852-3322-3327-8632-2435407e514b | -2.50243 | -52.98576 | 2024-11-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b33558c-6d44-3f8f-83e3-f9f4a43bfa93 | -2.41859 | -53.33789 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 73e0ff5a-4b9e-3797-abbe-b64e7d423525 | -2.41796 | -53.34202 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8a821cbb-3b5d-3e05-95e0-7072685c74ee | -2.41498 | -53.33738 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9e4fc6b5-3609-3eb5-a761-0c26e8a82975 | -2.41434 | -53.34152 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 634a4175-15f8-3bae-8add-790a4bfac7da | -2.41371 | -53.34566 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 28907353-6615-382d-9092-85667e255c66 | -2.41137 | -53.33685 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d06c812a-78ca-356b-b660-f7bde82092de | -2.41074 | -53.34099 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e7aaec5e-dab9-3d2c-87dc-aaf3caa70ce5 | -2.41011 | -53.34513 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| aa9235e9-7b5c-39a9-869b-3c0144a1e9b6 | -2.40948 | -53.34927 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f9ad597-d38b-3bdd-a4d3-ad2a35a3685d | -2.40714 | -53.34044 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1fdac7ee-ea55-3773-9953-f7eccc85177c | -2.4065 | -53.3446 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d08dbf8f-b46c-3e36-8f5a-35ad95db8c02 | -2.40606 | -53.34182 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b058d2b7-0f37-3cdd-8d00-5b6067f0a097 | -2.40588 | -53.34872 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| facba83e-aaa3-367f-a059-cb17ddcb03e8 | -2.40541 | -53.34597 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f27b573b-fb7e-3e8d-8dc2-3d99f5d85e1d | -2.40476 | -53.35005 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 626fbe42-0403-36ba-a3ee-9bd5dd0cc3e2 | -2.4029 | -53.34402 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36d8b736-fab0-32d5-a609-f73e9d445173 | -2.40228 | -53.34814 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 212864cd-d70b-392f-b336-3be48b754a4d | -2.40181 | -53.34538 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c5201e1-8938-3376-9520-e5249f406200 | -2.40165 | -53.35223 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b6160b12-6b99-3cb2-992a-b55d4dc517ec | -2.40117 | -53.34947 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63e9a559-06fd-31e6-81aa-bf55d9be9e70 | -2.40052 | -53.35356 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c097a9f6-05e1-30a1-be78-b011d30007c7 | -2.39931 | -53.34341 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ac92af9-de11-3bb6-ba8d-326ff5cd4bbd | -2.39868 | -53.34753 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0fcfaba-ecc7-3c8f-aeb7-712048a7f9e4 | -2.39822 | -53.34476 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31513427-2a09-3790-a9b0-f1b537b4f650 | -2.39806 | -53.35166 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b6fbadf-2721-3438-b6fa-530931660aef | -2.39758 | -53.34888 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0c41adc-7f70-365d-95d0-0f0db5ede052 | -2.39743 | -53.35578 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbbdd934-1610-36ee-b432-f153666546eb | -2.39693 | -53.35299 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10760c7c-9398-3649-af77-0189a6aca1aa | -2.39398 | -53.34832 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f35d5155-b676-3281-ae1a-92253ea762f9 | -3.10765 | -53.21666 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d03d487b-daff-3d56-8ee9-d77eb33565d9 | -3.10259 | -53.29833 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16bf690d-bd49-3b62-8553-f51772518683 | -3.10211 | -52.69888 | 2024-11-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00d638d4-86ca-3d80-bc31-b2913553d544 | -3.09903 | -52.69387 | 2024-11-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1d13b61-f255-3fa0-9350-b6e695a35afa | -3.09835 | -52.69831 | 2024-11-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
