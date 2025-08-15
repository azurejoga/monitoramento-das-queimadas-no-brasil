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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38bd03ea-72e8-36ca-8728-5e7e7dfabcc7 | -7.38395 | -44.88327 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3600639e-545b-31a2-ada8-afbeb9ca60f2 | -6.91313 | -59.15441 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 448d6912-2e19-325f-bc77-bc8f218967ca | -4.06903 | -47.98405 | 2025-08-15 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62523a1e-b0c4-329c-ba71-9147baad7b50 | -8.31704 | -45.01052 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1fe6c54-0077-3e5d-835e-5764444f1990 | -6.69705 | -58.82285 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| becf7101-cd61-3398-9348-eb17eb9a0c99 | -4.60293 | -43.32183 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1027afe5-46e0-32b2-afd0-b822fdffdfe1 | -6.95954 | -42.87261 | 2025-08-15 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 42b2a6cb-6818-392f-9a73-a06d9668b300 | -6.88877 | -59.16077 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e8bd361-364f-3a7c-9ae7-c802da5e63b8 | -7.3124 | -44.69302 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d52d26a8-bccc-306f-95ed-b094f8c44985 | -7.85201 | -48.23893 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3510df22-6719-3064-b732-8696eb074f37 | -7.02304 | -44.28555 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205cb202-3356-3160-98cb-42ac0814b748 | -8.743 | -44.0394 | 2025-08-15 04:27:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78e3e1f2-14bd-3f3a-b300-baf01f730c05 | -3.44518 | -48.97144 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e4b5b01-4479-36b5-8069-0853827c3689 | -7.64132 | -44.93755 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 031d329c-8794-3584-b9c1-97253c4f29e1 | -7.61473 | -45.19916 | 2025-08-15 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b14dbb9-6acd-3e3e-ae56-122f308fb266 | -6.94683 | -60.01321 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b9783e07-ef01-3c8f-b567-93bff47a6865 | -7.39357 | -44.86608 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d181098-4b43-3b93-8019-41a7348a3801 | -10.23814 | -48.26723 | 2025-08-15 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75e039f0-3b05-3e45-956a-fa4da649c413 | -6.09036 | -59.93349 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8d18471d-92f0-33ca-9b53-011cac763b61 | -11.23456 | -41.50396 | 2025-08-15 04:27:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8204e8a7-9312-3dec-8216-784c64f0aca6 | -6.37562 | -43.38882 | 2025-08-15 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02b5d42d-0509-30a5-9da5-1582a3166180 | -7.94463 | -46.84851 | 2025-08-15 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2259951-e4db-3654-b209-18e34d655989 | -5.86331 | -44.74329 | 2025-08-15 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43741eee-8651-3d56-b7b3-6b3f460382d0 | -10.18271 | -49.50475 | 2025-08-15 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f412d888-6c5a-3d47-a0c5-56c9da8b0ddc | -7.0849 | -59.21301 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9582eee5-5c6f-3fb0-87ee-ffaf505453f0 | -6.69828 | -58.85316 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b8374b76-3f39-306e-800c-7f97ca569636 | -5.53988 | -42.66326 | 2025-08-15 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f456577f-f7cc-3fcd-a5e5-037a57e35afe | -7.09245 | -59.22161 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca93f04a-cb1b-309f-8d91-c5eb01c5d70f | -7.08686 | -59.2144 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4767326a-7d63-3614-825e-7d0c4c43f324 | -6.94819 | -60.00618 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 347cfb7d-be3a-3823-acd0-2a5a35334dd9 | -9.72557 | -48.02525 | 2025-08-15 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8ef6109-3fd3-3a8a-ba00-6c0d873f8eeb | -3.11145 | -47.50172 | 2025-08-15 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f973d6e-a428-3917-978b-f4403bd7f23a | -8.29666 | -45.00739 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fe2c2e4-71e8-3fc6-b091-31ce632a7296 | -7.08944 | -59.22616 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cad3e556-fbce-3811-962a-75d2f78fc1d6 | -6.94252 | -59.99768 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65c5c8cb-7777-3791-8a5c-3f30d5b9ab87 | -5.26793 | -43.58848 | 2025-08-15 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| adf42f1c-a79d-39aa-ba56-d25c3895128e | -3.00677 | -46.69442 | 2025-08-15 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6e92954-4b88-36c3-82da-9adc5c4d7018 | -6.08766 | -59.94755 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 01dd01ec-002b-3db9-a7a3-1eeee221e78d | -6.93442 | -44.5649 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f47326c8-dd2f-3ec8-99bf-fb66559fac76 | -9.18955 | -45.32582 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c322efe2-0a1e-30db-9fbf-10beb0478d77 | -2.58668 | -51.9245 | 2025-08-15 04:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d639ecfd-6cd7-3f39-b7b4-77b1fc7ce429 | -7.079 | -59.21899 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7fa2fa0-8c08-3518-8302-0f1a2e16f9d6 | -7.05573 | -59.21979 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82e17390-b9d1-3b6b-8c48-249062961f3a | -7.32083 | -60.62197 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3df2432d-c084-37c2-be9d-940439c09210 | -6.70264 | -58.82968 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 165dbd5a-08bc-320f-abf1-6d8c8add1b5d | -6.95089 | -44.54861 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f54754f4-42b0-375d-ab54-32639c164bbe | -6.91332 | -59.14091 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42cc12f2-553c-33f7-8e0f-9354d999d686 | -9.02605 | -40.52219 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b347e31f-10cd-319e-a528-8b50392498c6 | -8.30968 | -45.01315 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 790afe89-07c8-382f-9ffa-93b249b3f263 | -7.59117 | -45.19544 | 2025-08-15 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48bad993-bfb7-3d0a-abf7-444e388b5752 | -5.68679 | -43.6537 | 2025-08-15 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acaed755-42f4-39f8-9bdc-43818c6e2df7 | -5.22068 | -43.19106 | 2025-08-15 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb4bf649-518d-34ec-9005-0e64e68cabd5 | -3.64619 | -48.32729 | 2025-08-15 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d68dc9a-39b2-36c6-9ee5-569b98e39dd3 | -8.51116 | -43.323 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25bf9def-f235-37f3-9189-1d389b9d4af2 | -6.96688 | -42.87371 | 2025-08-15 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| cb5dbeef-4eff-35aa-962d-66b414ee4b41 | -2.91463 | -48.30112 | 2025-08-15 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c476577-3ba3-3154-81d8-67bfe5f0b595 | -6.92639 | -59.52905 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f69be9c5-e1cd-3723-93cb-d640bcc9d144 | -7.33532 | -60.62498 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bc228e2-4d50-3231-b889-8ca3bf39087b | -2.9104 | -48.30462 | 2025-08-15 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c295b425-7a8e-3f60-9a38-8a8f8226e5ee | -9.0348 | -40.52348 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f58803f2-f089-363b-9d43-80b20117f7f4 | -6.90881 | -45.21048 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6881d463-2006-306c-81ff-aa325ede18b0 | -8.31987 | -45.01471 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 839157d7-38b0-3da7-8fca-ead1a3911a54 | -7.85724 | -48.2284 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d688ac3d-e481-34dd-8b31-873c67e59ce0 | -5.6862 | -43.65757 | 2025-08-15 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38217a38-67f1-3911-b15a-f0e5a828879a | -8.02079 | -40.42072 | 2025-08-15 04:27:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c0374d5-d6d2-348f-939d-ad97ba3b6ced | -6.65297 | -58.82055 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d04338a-acd3-3854-ab8e-01f43b966dbe | -6.53398 | -56.19696 | 2025-08-15 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aac33c1e-9e2c-3027-bae5-29d07fb911dd | -7.63793 | -44.93701 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f42d716-bccc-3a2a-b836-d136f6943707 | -4.39011 | -41.91621 | 2025-08-15 04:27:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42f9eaa9-c9f5-3327-bcbd-0d745bf7ad4d | -8.51418 | -43.32782 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c43bfd08-bdb3-39ed-aba4-83a4a338ed45 | -6.51496 | -56.20548 | 2025-08-15 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0179a0ad-2cdd-35f8-9372-79c9e550ff83 | -2.84886 | -48.78433 | 2025-08-15 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b44742a8-c920-399f-89da-ca3f6e8b2c67 | -7.07902 | -44.48851 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62ce6167-bf4b-3959-806d-75d5b2bb3c2f | -5.76308 | -46.6688 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b5e4bed7-3fa0-3a16-9f3e-6026df898d8a | -7.31929 | -60.62996 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17e103f7-c28e-3676-8284-399c8969654f | -6.70366 | -58.82415 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 09ada9ba-64f6-375c-87fa-226a8937dd94 | -4.18278 | -42.4291 | 2025-08-15 04:27:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9101928d-edd0-3d95-9c07-afa6ffc23ed8 | -5.2673 | -44.44654 | 2025-08-15 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2b0b7f7-1b55-32b1-8a48-d6e3b3ba03a6 | -6.1034 | -59.94247 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 628dd824-ef56-3a98-adbf-0fefa0c9a5da | -6.69601 | -58.82844 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ba96690d-bd10-34b3-9972-f10d9bfd4640 | -4.22573 | -47.22029 | 2025-08-15 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff75d8f5-1055-3368-a851-fc7bfc2f3383 | -6.6629 | -58.82213 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8ca9110e-50c6-3e14-bf5b-b23230fe49fa | -6.94501 | -60.13681 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8d4429e-d4c9-38bd-a494-93f5d29d297a | -9.21213 | -45.33679 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fa6ea22-9b5d-39ea-9c1c-25e2f72f57de | -6.90658 | -59.13971 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 580b29e7-e0d3-3d63-8ad2-52eba4e281b3 | -4.39145 | -41.90725 | 2025-08-15 04:27:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 27576bc9-159b-31bb-ab68-c595c2dfdb4f | -4.98266 | -41.71368 | 2025-08-15 04:27:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 668e07ab-c9bb-3840-a78e-aa9dca2eba6a | -4.18641 | -42.42966 | 2025-08-15 04:27:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0b38a2d8-fec0-305f-9d4f-9c1dc3d1500f | -7.08225 | -59.2383 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12368ad8-ce12-3312-bece-9da38e5c98d4 | -7.38734 | -44.88377 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a7414bf-5448-3096-8365-92330ae9c47a | -5.59755 | -45.38076 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4775f70e-8d2d-3862-af69-c3630f9c16c6 | -9.83606 | -47.80891 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30a00ad3-fc3d-317a-8a3d-6a7ee67fd9e1 | -6.90014 | -59.6363 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d2c7036-611a-3c02-bc59-b803046a84c6 | -6.90936 | -45.20692 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 30fd713a-e5f4-3dec-86ac-1bdd62d29d5d | -5.33057 | -44.98774 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94b85750-8e9f-3948-9588-44be77d78ffa | -7.38678 | -44.86509 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a02c8c54-bdb9-324b-993e-ed9ed6974b01 | -6.65961 | -58.82171 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bf7fb4f6-e132-39ab-be9c-22cb3d1891b5 | -6.88315 | -59.15344 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67a9e68c-7789-3eac-9eee-c9faa0e65b04 | -6.94557 | -59.99816 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e355caa1-f46d-37e8-a52d-42ee403bbf21 | -7.89585 | -42.1205 | 2025-08-15 04:27:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
