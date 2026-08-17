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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2dc533c-1e66-3514-9a5e-33005dead769 | -6.82777 | -56.45558 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69431415-e45f-307b-a3eb-e9eb535d92ab | -13.54532 | -51.8275 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 832e4c0d-ccf3-38e1-b540-402756c4ff08 | -14.50595 | -53.02072 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ca912b0-d009-39b9-8c31-cd8b68658706 | -11.31476 | -45.86689 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02b345c0-ce27-35d8-a03f-bf1ef7afcd66 | -14.38369 | -53.1502 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0153046-6a20-33b8-88d6-8f3ae89efd4a | -7.55462 | -61.18024 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef457b9e-bb3d-3696-a6cd-397c94622d4d | -11.88531 | -50.2221 | 2026-08-17 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee9d1a7b-aa0f-3ad6-b03c-ea02863e95f5 | -13.81412 | -53.84875 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8855976e-1792-3181-9582-4fa2d4a8a7f9 | -11.90842 | -47.34766 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64940f5f-1821-3f41-94b3-27f821520761 | -10.77279 | -53.07904 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cabfaeed-6838-3eb5-a9c6-05566ef192db | -14.40219 | -51.97037 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9bafaa8-439a-34c7-a78f-b174c3aa45a6 | -7.38114 | -59.9914 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4deaf79-f1fb-3b99-8332-a1b44f2a28ee | -14.7315 | -47.96333 | 2026-08-17 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b77f919-24ed-31e6-9b29-da106ba80599 | -12.04255 | -46.48735 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22ea905c-5509-3485-aeb3-5941f8011ffe | -6.64666 | -58.97403 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64ebc5c5-9aeb-37a3-a184-80bdefb4000e | -6.86182 | -56.42809 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42e6bae6-35cf-3df9-93c2-95781cdcb51a | -13.42864 | -57.0628 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5876ed26-b59e-34f3-be58-71d979c4c323 | -12.76274 | -48.43255 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78dd236b-3853-3d03-88fd-c56ff7ff3708 | -8.89891 | -60.56438 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6719bd4-aaf7-3fe6-b940-960f6fc62b06 | -8.52589 | -54.91529 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 23ab8fa7-7bdb-3a7f-8230-f585b837c99c | -11.48856 | -46.57657 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55a34a41-dbba-3b48-8ddd-ac5924637c25 | -6.93901 | -60.08988 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7da3c262-151b-39d3-95f5-134096bab967 | -11.71562 | -54.59473 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5247ebcd-e264-3de0-a35a-3cea572177c4 | -11.59282 | -46.72242 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55ceb765-300d-30d3-89d3-250f6936a6e8 | -8.95212 | -60.56752 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c582f63-5cbd-3ef8-a2e7-94ba1bd982ea | -10.37637 | -48.30694 | 2026-08-17 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb0b8393-a7cd-3ec0-997d-2213670a1dc2 | -6.97806 | -59.04321 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 494b0159-5fce-3e08-b4fb-62237b90b9f9 | -7.40149 | -55.48513 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95a7595d-948c-3324-bc4b-a6d63ac2bf77 | -8.90254 | -60.60403 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 74ed29f0-0de9-3912-9055-ac1efd81a1bb | -9.1229 | -45.17598 | 2026-08-17 04:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a341aebc-c6c9-310f-953d-db9eae5f7313 | -11.36694 | -55.44193 | 2026-08-17 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0904b347-e38f-3cd5-b21a-9eed7ec6a3ee | -11.4754 | -46.57814 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 341995cb-009a-3ace-b879-aa0cf96d0d13 | -10.9215 | -62.76938 | 2026-08-17 04:57:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5013d70c-ee99-3ca1-8a3f-9afdea2ce5aa | -7.77619 | -48.27459 | 2026-08-17 04:57:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74ffb62c-bf66-34da-a04e-ac2d2afe3b66 | -11.45271 | -46.58633 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b058568-ec31-3141-ac25-717068cbc3f0 | -8.90354 | -60.59766 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90729a7e-2c85-3a58-a8dd-179069660650 | -8.90127 | -60.58102 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95c2ae78-5f49-304d-abd6-1579d825996e | -11.30023 | -54.87352 | 2026-08-17 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59164289-a19f-3fab-bcb3-c868cfcb7f2e | -6.70644 | -58.94593 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd7ae4ad-7431-3dc5-a735-7d8c63cbf65d | -12.65901 | -48.48589 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8bcbf46-2801-3b9f-92e2-4df781792c3e | -6.81896 | -56.45793 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec10ad5c-3517-36ca-ac7c-c7ebffe14380 | -11.71392 | -54.6262 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6836d1bb-8273-3d7c-a08b-4f848288d808 | -14.32738 | -53.09694 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bd99a92-6900-3f0c-a82e-ead2615c5880 | -8.0266 | -55.14827 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 071a5e2a-c8b0-355e-ac80-dd115b977f10 | -12.74446 | -48.42346 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 674f1044-3202-3e9f-b259-83e3a1c24d44 | -12.03773 | -46.49054 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 937f4ddd-674e-30f7-b264-7c98bac402ad | -8.96192 | -60.51416 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d19b93c8-47b7-38b2-a28e-b1f363e3182a | -9.1747 | -59.67887 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf914cf2-3be9-3787-8276-694065d9a5df | -12.24431 | -47.00961 | 2026-08-17 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd4352a1-17ce-3053-83aa-76ced8cd46d2 | -13.53221 | -46.27354 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 765638ea-548b-3cf2-b0be-83bf78fa2abd | -11.32006 | -46.24814 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 864f1270-bd29-36b0-96ad-c5f1688ddd97 | -11.32799 | -47.01089 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed13ec44-b96b-31a5-8a46-1c33f71eccf3 | -6.63349 | -59.07779 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e62e75a-d002-3d90-862c-e43d7ba61db5 | -14.53406 | -53.26621 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06758404-c3fd-3a8c-94fc-0c019cc8aa5c | -11.47327 | -46.59335 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb6e63bc-5d43-3ceb-9e7b-b0a14f4d3004 | -8.9487 | -60.52787 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d77968f-cfac-3063-bba1-006625993015 | -7.38314 | -55.50136 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b7004e1-aca4-3276-b7ff-24d420197b32 | -8.90184 | -60.57795 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c62d6ee3-6bc7-3367-a899-91758f7cef0f | -6.71215 | -58.94171 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fa270adb-2860-3e53-a184-d1402047add0 | -8.90423 | -60.59464 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 053c72a1-af49-3dcb-9c14-e600c1f57e91 | -8.9002 | -60.55804 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40cbf89f-392a-34d6-8aac-29455cef9574 | -12.655 | -48.51425 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 809a831d-c8de-34d2-a231-9448c4742b20 | -11.4105 | -46.40156 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff261997-30d8-355e-a6bd-732cec47761a | -12.55355 | -47.84671 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78349e94-9c0f-3080-8d61-87aa6f33110e | -10.11504 | -48.81381 | 2026-08-17 04:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7aa1300-4940-3404-bf8f-fa4b261b045c | -11.70805 | -54.59738 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fb4e37f-13d8-3002-9208-ffc9cee6ed7d | -11.83619 | -51.77528 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 46870f37-2172-3a89-b6cc-7646cba90211 | -7.37708 | -55.49068 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e80e083-1bb7-37d0-aeb3-5ea80755df08 | -12.04201 | -46.49124 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5111f84-77d6-3535-9e52-c10a5cce6f13 | -14.29794 | -47.1846 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c37411d3-d7f3-3cdf-b285-fe5994e5927a | -7.39333 | -60.01258 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 807f2e7c-5598-36b9-9fe6-c342c47fe162 | -6.86737 | -58.94483 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3a65c6a-788c-339a-bf5e-c400801ac47b | -13.45921 | -49.20963 | 2026-08-17 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cecf9904-026b-3920-90e4-59a17ceeb7fb | -10.06295 | -62.4531 | 2026-08-17 04:57:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a9ade13-4246-36e7-a985-7b4bb483d67e | -13.51883 | -46.2375 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1025f58-8bc0-34d0-be36-7530493cc98e | -7.61288 | -60.95272 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b89a7970-3ccf-377a-84eb-283d156aaa2d | -8.96596 | -60.5213 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b2d5fbd-76fa-3a97-b921-e1ec32352c3a | -9.12687 | -46.01873 | 2026-08-17 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00bf2a59-ad16-3a89-b968-7537e35dff5e | -12.70961 | -48.51288 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d82b14d-3c78-3a4e-8b11-ffcf8394789c | -11.0874 | -47.30039 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49c4eab5-bbbd-3636-acf2-10c6f06312cc | -10.46652 | -46.30141 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 254a463e-b702-36de-99cb-405839f4ac0c | -8.96481 | -60.52757 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f6e4939-6052-3965-a05b-bdf9ccd9df1b | -14.49725 | -45.6861 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 674e78e5-801d-38a7-be5d-64d03507b6f8 | -14.88886 | -46.63723 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be3ff440-ba30-3d66-aa12-39a19a9153a1 | -13.49896 | -46.25076 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b844e7b-f426-3678-8620-d4cc2fee8a94 | -7.40496 | -60.01732 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa9ca299-eb55-3f69-86f8-44cb644f889c | -11.51167 | -54.62467 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58190261-5af6-319a-aee6-fbd97ddc40ac | -6.63253 | -59.08327 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 652486bc-0d82-3b4b-b8e0-0792de82fead | -11.81548 | -44.81024 | 2026-08-17 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f64044dd-c68d-3935-82a6-eb9f191b217c | -7.3808 | -55.51542 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a08f2d9e-b8e5-3560-b6ac-82bfb6eca616 | -8.67091 | -54.76127 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 374add3a-1df3-36b3-a8e2-4b7455fe59ad | -14.87448 | -46.64394 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eee050a7-912d-325e-905c-d1cdd5e819d4 | -13.74992 | -53.42891 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81b69dbe-32a1-39d3-96df-13d44d8c3c87 | -15.16945 | -48.65034 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc19b316-df6a-3c15-9714-623af6b01497 | -8.97283 | -60.51294 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06036278-bf99-3974-92aa-1a356a5e28b3 | -13.51167 | -46.22285 | 2026-08-17 04:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 393a37a8-b29c-3f17-801d-6fba587fbc46 | -7.55529 | -61.17654 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c76558ae-f615-3816-ad21-144ed533e23d | -8.97915 | -60.5076 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56434f94-7a81-36ca-84e2-be6a2cbea2a6 | -11.46645 | -46.58049 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8fef4268-ce29-36c9-b6c4-e7040dd74e52 | -7.61831 | -60.9538 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README40.md)
