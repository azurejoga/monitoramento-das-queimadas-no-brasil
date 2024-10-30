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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cdc80f2-8d20-36fd-95df-5618130edea9 | -3.02482 | -51.78566 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f302ac33-228f-338b-8f3a-93d8e6cc5cbe | -2.93004 | -51.58528 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 654c8911-1b58-37c3-b223-35788ffa3448 | -2.8986 | -51.47939 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c2ad0c8-e250-300e-a3da-9e10c1501f49 | -2.89775 | -51.48462 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a5ae294-2cc4-3f50-bc76-81eea1ac7005 | -2.88483 | -51.65716 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 394dd126-6905-34ad-b2dc-e96db42f18b9 | -2.88354 | -51.65461 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 11f51098-59d2-35bc-a85d-57ca9345b338 | -2.87698 | -51.31143 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4c66d4b-3e35-3370-86a2-402810fa151b | -2.84142 | -51.80162 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27d43c12-a115-377a-891b-a1c9d9fee7c8 | -2.84052 | -51.80714 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 687e19a4-63ba-3d72-8bf4-5f8216b099ac | -2.8356 | -51.80637 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e15040e-c010-33fa-b09b-8f6c0a5cc993 | -2.80652 | -51.9538 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eabe7ba-7e36-3a11-931c-70cf3cdeaa16 | -2.802 | -51.95017 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b557fad9-cae1-3d2e-a6e8-9cb930f75bac | -2.73555 | -51.72622 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f88f412-d00e-3c1d-b53a-d23e6d8b84a6 | -2.64774 | -51.75605 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02887e79-cb52-3200-9b67-d92245022f0b | -2.64564 | -51.75168 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ae972d05-5c90-3bf4-8151-0f712f7f3bd6 | -2.6446 | -51.74421 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f41f6ff-92fe-3212-a116-6ab1bb322f7d | -2.63969 | -51.74342 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7986a0d-c7fe-3aae-a4e6-578f2925699a | -3.39788 | -50.8083 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9378352-5dfe-3e21-a611-1253a2181ae6 | -3.2548 | -50.64256 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ded6f0a4-f379-3536-b278-153deca126ca | -3.25029 | -50.6418 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8116a72-5da1-3824-9690-10591f4486cd | -3.23626 | -50.72868 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02a5d0ce-1acc-3544-a06f-7cfe305c931b | -3.23172 | -50.72793 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ab91c1a-bc24-3816-a8fd-ab269c979e85 | -3.17515 | -50.59258 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d3c0d712-4b7e-37e3-a574-80b8f1ebb6cd | -3.1744 | -50.59709 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9a84a321-7e30-37ab-8e6b-d68b9dee5496 | -3.17221 | -50.59858 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3c19e73b-ae87-344b-a9cb-beda4daa4e4b | -3.16843 | -50.59333 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e23dca8c-7655-3926-a76c-23ef26f1af2f | -3.1677 | -50.59786 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 792488f7-b923-386a-8d42-945cfaa3b785 | -3.1632 | -50.59715 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 091a57f5-a807-3138-baec-3324ba68bf3a | -3.16165 | -50.59044 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 80f419e8-b0a4-389c-b990-ee0ca4e1cb18 | -3.16089 | -50.59496 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d73232c-a945-388e-8a72-5722fdea356b | -3.16083 | -50.62276 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4cf4825b-352c-3bbb-aa8a-96a01db2c8f5 | -3.15957 | -50.61977 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8fecf773-c494-3e95-9853-25499278f223 | -3.15884 | -50.62432 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb1a45bd-708f-3938-8620-d6c886fa5b7a | -3.15811 | -50.62889 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 973c9d99-300c-315f-9dd5-83eefecbe384 | -3.15419 | -50.59569 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9876bd58-208b-3727-bd89-7a143e1fd0f0 | -3.39332 | -50.80759 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bd6dc0b-5342-3753-9e3d-0f9c1edb7cd3 | -3.25102 | -50.63731 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b1b7510-8a8a-3a36-bd45-17f13a2e034e | -3.24957 | -50.64629 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0994e52-3c62-3845-992e-53e7921b2483 | -3.24651 | -50.63656 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e31b64ea-4d0e-30c2-a5dd-6cd585fe1de8 | -3.23551 | -50.73327 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 634817b6-9053-3753-bd14-9bbbf3e88cd9 | -3.1789 | -50.5978 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 991b421e-4560-3def-9951-171246a4b51c | -3.17743 | -50.59477 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8476be4d-2dd5-3364-8361-2d6b003e7126 | -3.17671 | -50.5993 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a50e0b40-f85f-3cd1-b638-e5232a241369 | -3.17364 | -50.6016 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bc5622a-b616-3e68-ad02-6e43e773b6c3 | -3.17293 | -50.59405 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ec8c2b36-fae7-3e4a-a901-77ff5b7745e2 | -3.17065 | -50.59186 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8111c1fb-1bb3-348c-8d1e-9b52d484ad45 | -3.16989 | -50.59638 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 83038dd1-d90f-3e91-bd30-5f3870ecb5f5 | -3.16914 | -50.60089 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 159ebab7-ef6a-3ad8-883f-1d18d35e6ccd | -3.16615 | -50.59115 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56016b2b-e9ad-3b44-9ffe-60ed7930d83c | -3.16539 | -50.59568 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d41ee0cc-ead9-3b29-bef7-4fdc5fdc0dd2 | -3.16392 | -50.59261 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff735d09-ebc0-3ceb-a0c2-46267b370f5e | -3.16007 | -50.62732 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a6463960-02a7-3563-ad23-eb35386419ca | -3.15942 | -50.59188 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e336c060-769a-3379-9a93-ef84ead26def | -3.15869 | -50.59642 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ef2ac0b-ca19-352e-93e9-0befe3f5b34f | -3.15556 | -50.6266 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 12d72659-225b-3f71-bc37-968cbc3a6ce6 | -3.15492 | -50.59116 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eaae4d6-a1fc-3e7b-98ca-ee5345b24a86 | -3.15042 | -50.59045 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eea53d0-eaf3-3b18-bdbb-702242bf8dfb | -3.59762 | -52.01891 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd982ff8-0d0a-3152-ac0d-3b7bc904ec24 | -3.8934 | -51.91552 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 56fe5ef2-27fa-37ce-a024-5e69c39ce833 | -3.89249 | -51.92105 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8552d710-df60-3017-987f-f3349be64a17 | -3.88854 | -51.91466 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 75d7fed5-9852-31f5-bf59-290d43dbd3f4 | -3.88761 | -51.92029 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 07da10db-0114-3c2e-8686-fda136fac340 | -3.86044 | -51.69959 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 811a69c6-617a-367b-ad44-3b6921813e89 | -3.86037 | -51.6977 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81fcf556-1f4e-3522-b1ba-b11315887c2a | -3.79248 | -51.96354 | 2024-10-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e2fb328-e0ac-3fd2-bd29-282a2e8d919b | -4.6695 | -50.9833 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c47444ac-45a7-320c-83ac-e951eac8e3c5 | -4.66576 | -50.97797 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f3c209f-6807-31a2-8e3a-09e8a6dfb5c4 | -4.47798 | -50.99856 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce2a256c-f58e-3f77-ac88-0ade7bdda5e1 | -4.05021 | -51.0793 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24df6034-aecb-34ba-abef-d6fe05b636de | -3.9423 | -50.99102 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0e3dff6-a8be-308d-a377-4251345c8629 | -3.93773 | -50.9903 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b2808ad-6e26-31ca-b26d-8dd20c978d31 | -3.93255 | -51.25438 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e33d05a-c825-383a-9b53-4a65a560cd1c | -3.92788 | -51.25369 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aac21303-8eb3-3dfe-8585-9fd3f8b1a4bc | -3.88415 | -51.02995 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bef7ffe6-cf5f-3f4c-930a-1c0455079fa4 | -3.85464 | -51.37822 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 807b1141-d6ef-3c4c-b505-c2962afd5553 | -3.85281 | -51.13195 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d8ca540-05f2-3b33-8cc4-b22700d05061 | -3.8499 | -51.12461 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dabf7bb-96dc-303c-9d43-b3f1ebc062f2 | -3.84916 | -51.12921 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 824e15e2-52ac-379a-8252-256d82ffb105 | -3.84893 | -51.12679 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49701e80-bca8-3529-8dcc-e538c97e6f66 | -3.82862 | -51.05177 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b02c5dd-983a-3285-9d46-90beed9b378b | -3.76017 | -51.0657 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9244f5e-63da-3ccb-a932-d9f9570b3925 | -3.72285 | -51.34463 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 111ef4b4-9f5d-39e1-9231-453fba6ff87c | -3.72203 | -51.34948 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f826a4ba-0b63-3913-95d2-5d57cacda6fd | -3.71734 | -51.34869 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e7b6b6f-b23a-3e2a-bcf1-2cbcb710e245 | -3.71653 | -51.35346 | 2024-10-30 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5307716a-c7b8-385c-9625-2fa86ce1e1da | -0.70378 | -51.98779 | 2024-10-30 04:19:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e24db131-7505-3808-b980-5cdd6ea62d75 | -0.70328 | -51.99086 | 2024-10-30 04:19:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc3e106f-5382-3307-b25e-9e9513722757 | -0.70278 | -51.99393 | 2024-10-30 04:19:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8c9a84a-d75f-33a6-a502-2dc5ba3bf3c6 | -0.70229 | -51.99699 | 2024-10-30 04:19:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c57398c3-b17a-3bc1-8cfd-b89c192a334a | -0.39762 | -51.72886 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eeec2e15-f352-38b9-bbed-65bdad63b90c | -0.39609 | -51.7267 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6324b25-bf10-3e45-b766-05e455419d1a | -0.3956 | -51.72969 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 422bfdb8-a23f-3850-83e3-6cde3e01b15e | -0.16972 | -51.67447 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3804195e-3a62-32c4-b868-8d03855ff60b | -0.16926 | -51.67744 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe8fa3e8-6983-381f-b65e-9a5fe7f94741 | -0.16652 | -51.56178 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f420ec-b42a-3321-86b2-aa72c211485b | -0.16463 | -51.67367 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52b63a2f-c9d6-3a33-96e7-0bdc80a48a4c | -0.16416 | -51.67664 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b965328-8039-3c68-ac37-ac64dd0e50fb | -0.161 | -51.56395 | 2024-10-30 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55f0f4b5-4056-30a5-8243-c9b1f9921656 | -1.76201 | -52.30819 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e04955fc-6ec6-3698-9547-b4b5d072f70d | -1.74553 | -52.34412 | 2024-10-30 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README46.md)
