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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6daa8048-ce38-3bf8-a017-de554dcd5bb2 | -14.4685 | -51.9405 | 2026-08-15 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| ed101d17-bff9-354b-88e4-b09f2d9d0c0a | -6.6194 | -59.0609 | 2026-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 3ed2dee8-f314-3c9e-9b18-754140cb7e8e | -6.6193 | -59.0802 | 2026-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8589d3d8-db14-3528-aa96-d98cc1649d6a | -6.1222 | -44.0271 | 2026-08-15 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 0a0cc5ae-93e5-33e8-8297-02f6c944fa9d | -6.6013 | -59.0037 | 2026-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ee6554a5-089b-32d5-a882-8a4ddaa9593b | -14.4302 | -51.9243 | 2026-08-15 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7c77b2a7-7060-3a10-8a29-e5d9843c8680 | -11.4 | -46.3079 | 2026-08-15 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 6feab0b9-e28c-3db0-91eb-781b92670249 | -6.9685 | -59.2976 | 2026-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 7edb110e-30eb-31be-930e-a1024adb4e6a | -6.9334 | -43.6333 | 2026-08-15 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 6ba5e3a9-077f-3195-a10a-b3606e2dda4e | -11.3996 | -46.3305 | 2026-08-15 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 82c6e581-c9be-35bd-a9f6-b29976d08818 | -6.6195 | -59.0416 | 2026-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 03d217c5-de62-3b27-86ba-cec917918161 | -11.3996 | -46.3305 | 2026-08-15 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 5ca04a79-73bb-3d55-a0ec-ee934889fc5b | -9.1219 | -46.404 | 2026-08-15 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ad76d4bb-5912-3a95-91c4-5f08d1cc78f0 | -6.6197 | -59.003 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bb328a2c-fb12-3cf5-b794-2d7dbc3dcb0f | -6.9334 | -43.6333 | 2026-08-15 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| e5d62ca0-12fc-334e-81bd-53485704bce6 | -8.5171 | -46.5338 | 2026-08-15 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| eea2512c-0f17-3487-b4c3-546a919c14a6 | -14.4499 | -51.9004 | 2026-08-15 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f187468a-6841-3c1d-81df-275598eca4c6 | -8.9601 | -60.5165 | 2026-08-15 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5018576c-02f4-38f6-a179-0161e382d9bc | -14.4495 | -51.9217 | 2026-08-15 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c9c751e4-8f6a-35bd-9381-859140526419 | -6.6195 | -59.0416 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5de6db9e-9eaa-3bfb-a389-f5b1f80ebb9c | -3.9785 | -49.4563 | 2026-08-15 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 4af02ef4-edc7-3421-9144-fa689174bac8 | -1.5805 | -47.7462 | 2026-08-15 01:10:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d490acaa-15c5-3acd-9d9c-13d0598912da | -6.6193 | -59.0802 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 70177f62-7eb1-3209-9e46-a91c6117ff7c | -6.6013 | -59.0037 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 18c18879-25a7-385b-a4e3-a62b9fdddde5 | -6.6194 | -59.0609 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 4db3e81e-48c6-3dc0-8505-f01920d8d47a | -6.1222 | -44.0271 | 2026-08-15 01:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5b204fb0-16ce-3c89-9efb-979e254a34cf | -6.95 | -59.2984 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5b18406f-870b-3df2-98b5-286ff8ccd19d | -11.4 | -46.3079 | 2026-08-15 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 32eca097-497f-3d94-ad7d-316065733ddc | -6.9686 | -59.2783 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f20ad9ee-73f9-3b52-82f1-6691c5b2c918 | -6.9145 | -43.6351 | 2026-08-15 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 3933636b-b84a-3122-ae58-5c99be3c1dc0 | -6.9685 | -59.2976 | 2026-08-15 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 35afc069-a10c-3f01-ac61-38e78b4327a0 | -14.4302 | -51.9243 | 2026-08-15 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 9bccda6e-d0d5-3ac7-b7f6-cc149fc1a977 | -14.4492 | -51.9431 | 2026-08-15 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 99b72932-6410-30a7-a191-68da937e2f5e | -14.4499 | -51.9004 | 2026-08-15 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3fe5def1-e803-35f4-b0a2-6102589cf009 | -6.6197 | -59.003 | 2026-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3ab1fd9f-7f2b-31a8-8673-5a609822d87c | -6.6194 | -59.0609 | 2026-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 65b6ddd3-527a-3bd8-a05d-e84d90d2449f | -11.4191 | -46.3053 | 2026-08-15 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4e1e2851-1d75-37bf-9e9a-277212ad89d4 | -11.3996 | -46.3305 | 2026-08-15 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 259.0 |
| 65d10bcb-7ef8-3791-b51c-391508732e30 | -6.6195 | -59.0416 | 2026-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| bebef7ff-fc0b-3d7b-9706-0370a2102a3c | -14.4492 | -51.9431 | 2026-08-15 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| aa7188d4-5164-3a4e-9dba-8717c39d78ac | -6.9334 | -43.6333 | 2026-08-15 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 6f5641a3-8170-3851-964e-1875bded6350 | -11.4187 | -46.328 | 2026-08-15 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| ffebc475-e2c7-34b7-826f-7777f964ad6e | -1.5805 | -47.7462 | 2026-08-15 01:20:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 64bbb52d-9d07-351a-ae33-d12175eef190 | -6.6013 | -59.0037 | 2026-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| cca794ca-6277-352e-a392-acaf2ee6064c | -14.4302 | -51.9243 | 2026-08-15 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9aaac79f-d4dc-3bb1-8c45-5ba36e2c2966 | -6.6378 | -59.0602 | 2026-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1b35790d-2f30-3466-bd6a-488cb3f18ceb | -3.9785 | -49.4563 | 2026-08-15 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 15d6daed-3a9c-3a2a-8614-efe42973f9d8 | -16.8797 | -54.1536 | 2026-08-15 01:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 04941bc7-225f-34b1-85db-7b93c8a7a1f6 | -11.4 | -46.3079 | 2026-08-15 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 15f49cf1-5bca-3c80-b406-5f8311dfce05 | -14.4495 | -51.9217 | 2026-08-15 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 199fe6aa-67ed-3a55-9030-55afce352301 | -16.8994 | -54.1509 | 2026-08-15 01:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 88d300ef-7119-3526-8013-050f5e3711bf | -6.9145 | -43.6351 | 2026-08-15 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 23818b2f-2de5-3139-856c-12f6a593399c | -9.1219 | -46.404 | 2026-08-15 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ac7ffd7d-4d19-30d0-a69f-d2fa2dbd6f57 | -6.9685 | -59.2976 | 2026-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7a649f95-2538-3c81-8969-4ae0dc5c8f1e | -16.8801 | -54.1325 | 2026-08-15 01:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 133e5b48-502e-3ef1-a692-906c3adc1162 | -6.1222 | -44.0271 | 2026-08-15 01:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| dd45c13d-6e3d-3566-95b2-a68206f8e74f | -6.6194 | -59.0609 | 2026-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| a54e16be-ac4f-34d4-8af9-e14ea1b4960f | -11.4187 | -46.328 | 2026-08-15 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 258bddbf-9322-3abb-89fa-c783e93fa972 | -6.6013 | -59.0037 | 2026-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e94cd889-2108-3208-b38e-5917f57f96fc | -9.1219 | -46.404 | 2026-08-15 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a0ecdc7c-fa76-39bf-afa3-2d8ccf437ea7 | -6.6197 | -59.003 | 2026-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| cb57d0fa-d5a7-3b52-bb38-2e772eb98e59 | -6.6195 | -59.0416 | 2026-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b93d5e89-9015-353e-83c8-d347db35da07 | -6.1222 | -44.0271 | 2026-08-15 01:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 04847e3c-8156-3eba-a1a9-234c063d58a8 | -6.9685 | -59.2976 | 2026-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4d88d1b0-4eb1-318e-9280-9f2993b8e2a1 | -14.4499 | -51.9004 | 2026-08-15 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 03b0bb1e-fefa-3b4d-bf1f-2c67396a7ee2 | -11.4191 | -46.3053 | 2026-08-15 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 8d81577f-787c-39cb-bbac-6f20d374be86 | -14.4495 | -51.9217 | 2026-08-15 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 70774639-c4ca-321c-905d-f06d104e0d5a | -6.9334 | -43.6333 | 2026-08-15 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 46cbb5b7-92b3-3177-b983-0a927d20b975 | -14.4302 | -51.9243 | 2026-08-15 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| f7fcf607-df78-3c22-ac3d-ebaa556bb846 | -6.9145 | -43.6351 | 2026-08-15 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 13ce8efa-525b-36ec-a1ca-5f396a232ccd | -1.5805 | -47.7462 | 2026-08-15 01:30:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| dd372d7e-152a-3611-a43f-429fac230736 | -11.4 | -46.3079 | 2026-08-15 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| db7d108b-8dc3-3212-a0c4-e2fe9197f187 | -14.4306 | -51.9029 | 2026-08-15 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 37e54b6f-a95c-3fb4-ac5f-7e54df6638e1 | -6.6193 | -59.0802 | 2026-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 795acf67-7c60-3b64-88cc-8e56f041fd76 | -11.3996 | -46.3305 | 2026-08-15 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 295.3 |
| 83253699-17fd-3ea6-9d4c-debd600a7d34 | -11.3992 | -46.3532 | 2026-08-15 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 87f3f0ce-1fbf-39ec-9176-b45d4a27b098 | -11.4184 | -46.3506 | 2026-08-15 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9d1ab250-b3fd-3704-808f-f0371ee71ea7 | -11.4 | -46.3079 | 2026-08-15 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| bfdf51f1-e979-314f-9cd2-200c42c820cb | -14.4302 | -51.9243 | 2026-08-15 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 849466dc-40c3-34f7-84d2-e9ffae246106 | -1.5805 | -47.7462 | 2026-08-15 01:40:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7bd27270-e4a0-3508-944f-e74e94dbb4ac | -11.4191 | -46.3053 | 2026-08-15 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 071e746d-d9d5-321a-a528-63028568833c | -6.1222 | -44.0271 | 2026-08-15 01:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 23d7d662-8167-3f4f-8459-eb77868a6f5a | -6.9334 | -43.6333 | 2026-08-15 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 86524c37-76ea-3a5c-8c00-3b0c9d7b0dcd | -14.4495 | -51.9217 | 2026-08-15 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5589a7f3-793a-3b77-a648-eb03b4339370 | -14.4499 | -51.9004 | 2026-08-15 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| f73b2f8d-02e4-38a8-8453-aa5461671e1d | -9.1219 | -46.404 | 2026-08-15 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c96be866-fab4-3612-a517-f695ed67a502 | -6.95 | -59.2984 | 2026-08-15 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c88680d0-a1f2-3adc-946c-84440a0c509f | -11.3996 | -46.3305 | 2026-08-15 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 416.7 |
| 9ca6e18e-2f65-3eed-9a2e-c740625fbd3e | -6.9145 | -43.6351 | 2026-08-15 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b3cf86f8-847f-3473-875f-8cb755955ad5 | -6.6194 | -59.0609 | 2026-08-15 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 9a8dfaf6-f21d-389e-a1b6-84113605ac84 | -11.4187 | -46.328 | 2026-08-15 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 0aceb6eb-d804-3f72-b289-20a5d9d7a4fb | -6.6013 | -59.0037 | 2026-08-15 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0c9fea39-7683-35d4-b1c4-6aee41d0e90d | -6.6197 | -59.003 | 2026-08-15 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| beba743b-06f0-34ed-bf95-954428730814 | -14.4495 | -51.9217 | 2026-08-15 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| bfa9d8d4-79ba-332a-a466-7509252c293f | -14.4302 | -51.9243 | 2026-08-15 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1a32dd78-0dcc-3cfc-9181-043d5dc9e153 | -11.4 | -46.3079 | 2026-08-15 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 74492bad-4de4-39b5-bb20-893d7893e8d5 | -11.4187 | -46.328 | 2026-08-15 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 453.4 |
| 04d9dae1-0bd7-3e58-aa03-3c480169deb0 | -9.1219 | -46.404 | 2026-08-15 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 1eafd38c-8e4d-3983-900a-f2f7b540390d | -14.4499 | -51.9004 | 2026-08-15 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| c9e3709a-ba9b-3e48-bf11-f1aa54ce6b6b | -6.6194 | -59.0609 | 2026-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |


[Clique aqui para ver as próximas entradas](README5.md)
