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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a8883c-7b47-3323-9e93-fa2d844c4d4c | -9.25232 | -48.86918 | 2025-05-30 05:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a62c3fb2-a870-3694-873e-f013bd10e02d | -8.90459 | -44.78126 | 2025-05-30 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71d5943c-42c4-315c-984d-dd10e93ac815 | -9.3946 | -48.41602 | 2025-05-30 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d081d78-3752-3d04-afac-5b6dc83a8de9 | -7.58546 | -45.86272 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6732e93-5b90-3a4e-95b6-04b26bea778b | -7.08667 | -46.04742 | 2025-05-30 05:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4c99268-7d02-373c-ba65-c543f52cd27f | -9.60518 | -49.02295 | 2025-05-30 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7990a5b-5756-3157-a1a6-12d40b1e647c | -5.18538 | -48.08028 | 2025-05-30 05:12:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4b37c89-aa49-3d04-95f8-d8b1a0f7ccd3 | -7.9599 | -46.17247 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 041d184a-c1ab-398b-b4f8-0e0042c33957 | -7.99871 | -45.68015 | 2025-05-30 05:12:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75494b7a-af36-3533-99a9-02f33a8ec648 | -8.51392 | -50.01855 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60b316ba-b1cf-3fce-803d-da063bfc1cd6 | -7.58581 | -45.95615 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 876d82bc-a006-3170-83e8-eb20bfed5771 | -6.21436 | -57.77458 | 2025-05-30 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a118a4c1-e4e2-309d-bfa9-854c2bb106f6 | -8.90448 | -44.78077 | 2025-05-30 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e196270-a545-31e0-93af-073de2c6c3eb | -7.95581 | -46.17528 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f698a5e-1c60-3832-9f00-6b2a4c1b6d08 | -9.25275 | -48.86589 | 2025-05-30 05:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a44cd3b9-43f5-3bbe-90d5-fd7a178dd574 | -7.70101 | -49.39182 | 2025-05-30 05:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55516a3a-4573-34dd-b38c-4d3dbd48e2de | -8.90523 | -44.77459 | 2025-05-30 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57cd3971-c645-3e6a-9d93-7ead4b2c1d6e | -7.58718 | -45.94601 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbb346ad-1fbe-3641-a1ae-f1a85c73fd13 | -6.34435 | -43.37761 | 2025-05-30 05:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16a79b61-d10c-359b-858e-430e11e8f084 | -8.00444 | -45.6869 | 2025-05-30 05:12:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a13a1fa-6a17-33c1-939f-d010c00a8a67 | -7.962 | -46.17697 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dd68e5b-756d-3ba2-a138-48f506110d5d | -9.25318 | -48.86259 | 2025-05-30 05:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa20f5fa-32c9-3868-8bc8-ee5e60742463 | -7.58893 | -45.94623 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e0bfe1-dad5-3df3-900b-2e813c4fca1d | -7.89571 | -55.41629 | 2025-05-30 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2abff80-e229-3e1d-bff2-239e8fa78e56 | -6.63259 | -55.01027 | 2025-05-30 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fafc898-4efd-34df-8c7e-9c037a700936 | -7.58763 | -45.9564 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd8a6f4e-d708-3666-b7c1-7a8d9a30e12c | -9.79721 | -47.7483 | 2025-05-30 05:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24539e5e-cec5-3b48-bc66-fa54aa7caec3 | -8.90538 | -44.77511 | 2025-05-30 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f18c1c82-b3ed-3334-bbd4-646f510146a2 | -7.96275 | -46.17096 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a8fd587-b871-3672-ad36-c8a7ab5a5095 | -9.60838 | -49.02294 | 2025-05-30 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e83404a2-e4e0-3155-af18-9c8ca30b3537 | -8.51494 | -50.01946 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b92e85d-8490-3ecf-9527-bef6297e57cf | -9.84558 | -48.14654 | 2025-05-30 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0661439b-6416-37f4-8a57-42faec14cad2 | -9.39508 | -48.41227 | 2025-05-30 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66f3ffad-a546-3a4b-a8a7-d33cba48901e | -8.51986 | -50.0202 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdd6f461-2405-3824-9b7c-900bcab6870c | -9.85127 | -48.14727 | 2025-05-30 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3efcd84-93f6-32fc-9024-67b4735855da | -9.36701 | -57.55198 | 2025-05-30 05:12:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73c72320-f062-3dfa-a68b-c9866d49d994 | -7.90329 | -55.41351 | 2025-05-30 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4728e67f-86d0-3f39-8b27-c461139f6ed1 | -8.51468 | -50.0131 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bcfeae8-8b45-357e-aaa6-039e1426507c | -10.26813 | -46.48078 | 2025-05-30 05:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03416884-a69c-33d0-8e84-355a87fc81ba | -7.5865 | -45.9511 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 581031ff-2329-3908-9d66-70e8b473ed15 | -7.61438 | -45.74485 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 678cd120-d767-3e9b-a197-49ec156e76c4 | -9.39365 | -48.42344 | 2025-05-30 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5772ae5b-29ed-318c-9cb8-ac0bc796e3f3 | -7.9062 | -55.41792 | 2025-05-30 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84997a89-8c87-3ad6-89e3-1a9000710b5f | -6.23903 | -43.37611 | 2025-05-30 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc5d1a8e-4d39-3b00-98f0-863293aed88a | -8.19744 | -49.80595 | 2025-05-30 05:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53344494-1432-39fe-886b-be31cae5e1b7 | -8.51884 | -50.01926 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8800e8d2-1d28-34d8-a7c3-283743094255 | -7.61479 | -45.74466 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 581751f8-d8a0-3b3a-a2fe-4ba75e5c8e69 | -9.36367 | -57.55146 | 2025-05-30 05:12:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09747fef-4dc0-3e6a-9cf8-cb4c5af5da15 | -7.66675 | -49.37741 | 2025-05-30 05:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cbdc7db-727c-31d4-af7f-bef74c8447e0 | -9.85073 | -48.15129 | 2025-05-30 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3749dcae-5b7c-3a73-8401-89a1317762d7 | -6.33614 | -43.38386 | 2025-05-30 05:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c455a94d-502a-3566-b066-eb5239361e29 | -10.45421 | -47.95103 | 2025-05-30 05:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d227b784-00b6-3c12-82f0-c376946fbb58 | -9.11011 | -49.62926 | 2025-05-30 05:12:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1543ccbd-fd88-3088-9032-7fec7373552c | -8.51567 | -50.014 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb120a5e-bc72-3705-88b1-6c1b0d2df1d8 | -6.34273 | -43.37899 | 2025-05-30 05:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d84463fc-2001-3420-9000-1fc893a2f7e8 | -6.34338 | -43.38515 | 2025-05-30 05:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ee4ad3e-987a-3f24-b349-dbf49b7e4666 | -7.57842 | -45.86678 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ba188d0-57e9-3c33-bbe4-490cb5e183df | -9.40063 | -48.41306 | 2025-05-30 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf3224b8-47c2-34a1-8423-4468f5c8b4ac | -9.36034 | -57.55093 | 2025-05-30 05:12:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74feda54-7e7e-317d-b28d-06851046c047 | -5.18003 | -48.07951 | 2025-05-30 05:12:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52e76a92-731b-35e2-838a-87df2250a8cd | -7.62648 | -45.75223 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 709aed84-d268-3743-ad3f-27cae4187066 | -6.6361 | -55.01081 | 2025-05-30 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d72ea785-7538-3163-b7f9-77484481e53c | -7.89979 | -55.41296 | 2025-05-30 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cb0710e-218f-3cf5-b262-7829c297aaa3 | -7.58029 | -45.86174 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb7cd856-bd76-359e-b091-3758608d9c56 | -8.79432 | -47.94106 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1f1747f-54cf-3022-8a0d-2b497a101d57 | -9.85245 | -48.14968 | 2025-05-30 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b7ed81b-d9fb-3a1a-a2c2-9f6a5fde9dc5 | -7.61545 | -45.73946 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a56c4aa6-7e59-36ee-8082-1c8c969eef6b | -9.79671 | -47.75232 | 2025-05-30 05:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e797881f-8be9-31a5-8bb0-5b12509229ff | -9.25725 | -48.87331 | 2025-05-30 05:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c5038fb-a326-386b-90b2-b849e4bb5b1d | -9.25769 | -48.86996 | 2025-05-30 05:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2494f046-3452-3257-8b62-ae9905444603 | -9.7917 | -47.74937 | 2025-05-30 05:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5f8cd8e-1b83-3bfb-a282-c53bd063dda3 | -7.95653 | -46.16949 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 459c0878-4917-3443-a20b-3dbd98c3d183 | -7.89921 | -55.41684 | 2025-05-30 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 091f04c7-d273-3e82-b0a6-90711245bfb2 | -7.95373 | -46.17075 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e66891b-39d8-3d88-82ed-4dc5d99b6dc5 | -7.62692 | -45.7521 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 243ef48d-1d89-358e-b494-cf319018a68b | -7.59214 | -45.95711 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4af4c457-cdda-37c7-9d28-b7ca1b3d68f6 | -9.60796 | -49.02621 | 2025-05-30 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4871f46-66b1-3383-a430-366da588e723 | -7.70608 | -49.39255 | 2025-05-30 05:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a36866e-c965-32a8-9c5e-e4d7d2c483dc | -9.7975 | -47.75031 | 2025-05-30 05:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8eccf8c-16be-351b-8516-5fbae0582320 | -10.46052 | -47.94783 | 2025-05-30 05:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 056d869d-b446-3d02-9e78-c7923caeda6b | -10.46 | -47.95198 | 2025-05-30 05:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13ec7acc-ba1d-3a57-8df5-4d9fd1afdafb | -8.79609 | -47.93948 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c02c310d-9bc2-3a8a-825d-dced2c564fab | -6.3417 | -43.38657 | 2025-05-30 05:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cca06f8-c3a0-34de-9eea-f12591354f11 | -9.84726 | -48.14493 | 2025-05-30 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec16af36-7e48-36f6-85f1-004525903d64 | -8.79559 | -47.94337 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee774ae8-f0ce-3b31-9ba0-bf5811c5257c | -8.19666 | -49.81158 | 2025-05-30 05:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae64a633-4ae5-3c65-ab6a-9b55910410a4 | -9.6101 | -49.02684 | 2025-05-30 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9df46c39-c1c0-38bd-9e50-7275de2b5e14 | -7.58828 | -45.95133 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92426977-e6d4-3709-870c-f63a50a8ab62 | -10.29914 | -57.14034 | 2025-05-30 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5d53fba-87b8-30c7-a587-86a82cf14d7b | -11.69209 | -46.21564 | 2025-05-30 05:14:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a517d28-e1f4-3d78-ab4e-5f29b9d0f898 | -12.01575 | -49.52323 | 2025-05-30 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73914802-efba-31d8-9446-cb8c0b21f055 | -11.79464 | -44.28614 | 2025-05-30 05:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 14c9f392-c012-3fc0-ae84-898d8fc76a8d | -13.63128 | -47.43407 | 2025-05-30 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2275f0e7-b14e-3854-a7e9-516440ddfc6e | -10.68028 | -57.60686 | 2025-05-30 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c114ea65-54d7-3a6f-9fca-1698f77936e9 | -14.84701 | -48.09406 | 2025-05-30 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc8dde40-6c19-3442-b8de-fd7a0b46bb9c | -12.06578 | -48.47322 | 2025-05-30 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94af6822-61e3-3d6d-9380-123693be775c | -11.65711 | -55.36331 | 2025-05-30 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0ce2f70-70c1-3aa2-b1b0-985e26a85b9d | -10.29577 | -57.13982 | 2025-05-30 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e61e8856-c854-3991-b3eb-9f63b157da44 | -10.19786 | -59.43863 | 2025-05-30 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f13d4dd1-6640-3152-b6b7-80c8fed02b5e | -13.63401 | -47.42742 | 2025-05-30 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README12.md)
