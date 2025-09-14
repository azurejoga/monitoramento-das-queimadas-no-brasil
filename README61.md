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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfa4ec1f-a27b-3e4d-baab-d94840d3876c | -11.45926 | -50.75262 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff9a7424-0055-3724-98cf-4a68e14e2c3a | -9.02023 | -47.04944 | 2025-09-14 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7334ec94-1b89-3d64-ad23-39fa9356c7e4 | -14.81802 | -48.77036 | 2025-09-14 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79763a41-fa93-3fe2-bc92-93279c2977ed | -12.56774 | -45.65735 | 2025-09-14 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd3d817a-26e6-30dd-8b14-770738799fa9 | -13.58693 | -51.67511 | 2025-09-14 05:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40fa84a5-2102-397b-b80b-e941ff314af8 | -14.3205 | -46.10012 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ec29d90-af24-384c-94a9-87893354da08 | -12.74853 | -48.01921 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be92ab00-5942-3005-80d5-81989fa76c0b | -13.93773 | -44.8455 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 3ea2b744-831d-3cde-b4eb-8d0a70f2c802 | -8.93119 | -46.15948 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa4a74da-1840-36ff-a873-b9c1371183df | -14.4354 | -43.20318 | 2025-09-14 05:08:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10c9feb1-3291-3e0e-b31c-70d5b9a3b0f8 | -11.44452 | -50.46771 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9314831-c095-3d56-b869-e7820123fcd0 | -12.68304 | -54.69975 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a13eb37b-9943-3519-9473-b44dfc4952b0 | -13.00132 | -47.97984 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efac1c54-047e-327d-af1b-a1c486f8ff42 | -13.93108 | -44.84491 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c9240908-f3ee-3eca-873c-8ee7c3f8beb9 | -12.67486 | -54.68211 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 7fd488c8-9374-36e6-bed5-2b63b011e113 | -10.40642 | -48.60738 | 2025-09-14 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d812a934-8d6d-3140-880c-502d9d4ec7c0 | -12.14266 | -47.59392 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd2aaa46-7af8-364f-a567-6f9aefc6a002 | -14.27892 | -46.13795 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c2e894d-e869-372f-acd7-af1c0e13c5c6 | -11.23982 | -47.62802 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfa6db1d-6657-342a-90fa-9e3ecdcbe932 | -13.95035 | -44.85299 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 6824f6a5-2e82-387c-8582-5402f78eccf6 | -12.78309 | -48.03047 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51403e38-98dd-3a4d-bb06-1fc3972d6817 | -10.92014 | -45.59148 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8bc5b2e-f7c6-355c-acb7-8c43c535b392 | -12.09545 | -51.382 | 2025-09-14 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2290ad9-0971-30a4-89e0-684e3f0076dd | -12.92896 | -54.73919 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c71faf9f-1644-3b66-ad4c-65ff42a871e7 | -12.92484 | -54.74265 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 07f4ea84-1d06-3797-b313-17be2f1c24ae | -12.70589 | -54.71537 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1f01fbb7-e7e3-37ed-9a14-ef42de82a8ec | -12.03682 | -46.53555 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e219b69-ee77-348c-8438-6e04f520b9e0 | -11.24558 | -47.62561 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a47faa2-0ab7-3dfb-b72e-cdb6f1810801 | -12.78148 | -48.04385 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7975af43-9c0c-3981-9335-6e8e13328187 | -12.78429 | -48.02049 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66e2cb32-44cc-36cf-bd37-3d3db3799a16 | -11.77934 | -46.62568 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f8cfef0-2221-3a79-ad9f-0537c7261355 | -11.7823 | -46.65021 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2088a092-68f8-3d7b-95d4-288449076e60 | -11.88582 | -50.53924 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78125ef8-18e8-3a04-9de6-9de3c2c0f6fb | -11.47878 | -50.77258 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2949000-d055-3ecb-8e65-c89f06cd35c6 | -13.02174 | -47.99162 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78fd8010-cb39-3693-ae80-44f534439b7e | -7.39404 | -49.97975 | 2025-09-14 05:08:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4beab226-c642-366b-9b03-5b39cef7e37b | -10.89414 | -48.17703 | 2025-09-14 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90001f21-a173-3992-a8b3-3c726513dabf | -12.78546 | -47.98506 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5a07d51-b7b1-320f-8a2a-6b4de235c4b4 | -11.39781 | -50.4543 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb7a05db-5937-340c-8994-ab89773a1e4a | -12.66604 | -54.69307 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33049623-f7dc-3814-a64a-be61e27cba07 | -14.27942 | -46.13328 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0529e9c8-ff3a-3194-b4f3-4454274bc271 | -11.44008 | -50.46708 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b12e6b65-6b10-3387-9c6e-07cdf9ed012d | -12.12875 | -44.84519 | 2025-09-14 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63ba0251-1aa4-3d2e-9582-8f355e8e93ff | -11.8226 | -50.5033 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b90b5076-b8a4-328f-b31f-f6cdd03c7b28 | -11.43445 | -50.47523 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 760d429f-f86a-336d-94cc-a8fd5256624c | -12.66956 | -54.69359 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6fd3c74-b6a7-3743-aa60-991ed1861bb8 | -11.43505 | -50.47085 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a269dbc5-5f50-3beb-98b7-74d0f386c8ef | -11.1413 | -47.65648 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b973bcfb-6542-3cdb-804c-f57d08af3f4c | -11.23786 | -47.62682 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d7083cf-51cb-3a78-8960-95a564a4e15e | -12.92072 | -54.74611 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a4a4a5cd-39c7-3a55-b2be-c88bdb7dea9d | -12.81402 | -47.9546 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8eb0562-42bc-35f3-a773-abb1c5e7b89a | -11.35996 | -47.33241 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76797b30-d66c-36e6-87e1-96eb351e15fe | -11.4065 | -55.358 | 2025-09-14 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d5b1b9b-5c1e-3bb4-aecb-2aa6ade3f571 | -11.38163 | -47.34135 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63c1aec4-9aed-305e-aede-669dc707db94 | -12.93222 | -54.74258 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b9b1fc7-83ce-3a98-8182-be512e559def | -12.78304 | -48.00419 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36658aa0-3dd9-3dc7-89ee-6aab7541f71c | -12.96811 | -48.04877 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c2dd9aa-f879-398c-974b-e8da794efebd | -14.18331 | -46.15953 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fe4cb47-a2c2-353b-ad42-c228f3ec6410 | -13.89544 | -48.30603 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ba10d26-1a9c-337a-85fa-cca134d16224 | -12.66548 | -54.67252 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f139ea2e-8727-370a-bb22-642f4b6f735e | -12.80777 | -47.9612 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b8048e8-fc5c-3044-ae04-91aa086e9f64 | -12.98401 | -47.98779 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e33f6c59-700f-3f3c-9916-75d6f7a9afbb | -12.76665 | -48.0047 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7457697b-6dc2-3e30-bd16-03522c0510f1 | -11.13806 | -45.32723 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a4fe703-5b4b-339b-99f8-81cd8fcc6154 | -14.49974 | -53.88395 | 2025-09-14 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4d10a57-83be-34cd-90ba-780d3f35634b | -12.09123 | -51.38143 | 2025-09-14 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf815bb1-e220-3ec6-b98b-fd48e001b478 | -12.69474 | -54.71779 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a2e2b171-c9b6-3878-a36f-9ac23b1067f1 | -11.21276 | -47.67049 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ce6184b-d11c-3975-b26a-698aef49b823 | -12.7506 | -48.00267 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d04544b0-c862-385d-a1d7-bb684070e59d | -11.81507 | -50.50342 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6ec0336-1b43-38d9-874a-5f17068a06cb | -13.93352 | -44.82214 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cba6fe6-f092-31b2-8250-843b8cb2cafc | -12.08938 | -44.73032 | 2025-09-14 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58b7e1d3-2241-381f-8e94-1fe6e91696cb | -7.87881 | -49.50141 | 2025-09-14 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b153433e-7786-393f-8b97-91c14c028f86 | -12.77321 | -48.0223 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 288930fb-df28-365b-832e-4f21a4b1aef1 | -12.76908 | -48.01141 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18849edf-364c-34d6-b5c0-f47f6f17ba8e | -12.69539 | -54.68934 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 7784d1a0-2f1f-3731-a7d9-45e0aed812b1 | -12.68656 | -54.70029 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 00bf2eb0-794a-38a0-b446-1b9d059f688f | -12.90957 | -54.74845 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be9a2c52-c58c-3136-a4f4-dc4505f1bf7f | -14.20578 | -46.18131 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa1266c9-4d96-3911-99b3-f621f293acdd | -8.63113 | -54.65392 | 2025-09-14 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d80474d8-1119-3e4b-9cd1-bad9a325d101 | -12.81996 | -47.95061 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e7178d7-0483-3221-923f-1bdd7e7c75c0 | -12.93076 | -47.95387 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cca55969-712e-3ca3-9c8e-1cbef615ab8f | -10.75668 | -44.77358 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61a9503c-aaf8-383a-83dd-9f6fd840d50d | -12.65551 | -54.66687 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda3c16a-5977-378d-b82b-48ad262d83e9 | -11.45777 | -50.79293 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30133ddb-4292-3c1b-857a-2b9844471ba4 | -12.08474 | -47.56594 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26a1bbdc-7562-36ec-b245-344e70cb7adc | -10.70154 | -48.67691 | 2025-09-14 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08b94c0b-feb1-35ff-bab2-584d5098e03a | -14.43447 | -43.2114 | 2025-09-14 05:08:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f690ff4d-cc97-3131-b0d3-c419f36bda34 | -11.13179 | -45.32682 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9684d756-50e7-3447-b387-818ffac75c75 | -10.9638 | -49.56696 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5119fcf-23bc-3a25-a8a4-251e645f6947 | -13.93892 | -44.83442 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| c535b67e-57d6-3394-a4e7-cec0c2e1a0ae | -12.68775 | -54.69228 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e82c7284-87de-38b4-8e11-e9fc339e8ed1 | -12.67019 | -54.66505 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48dc2a3c-7cac-3e30-8847-10c05d6a10d8 | -11.38098 | -47.34246 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85bbd6ae-70f1-3404-b2b7-6d859a0fc444 | -14.48135 | -47.32698 | 2025-09-14 05:08:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 240eb4e4-6f30-32b3-9996-ead259d78983 | -11.84665 | -50.49313 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f8d116c6-4c2e-30fc-a6a7-cecf71d07f4c | -12.92836 | -54.74318 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d2c9dda4-27a2-3246-9675-398d256b3776 | -12.936 | -54.74025 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1a2ceb61-cb27-3be5-a6a1-90fc362d7670 | -8.18411 | -46.7735 | 2025-09-14 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb2d0cd3-78e6-3001-b06d-ddf994c70367 | -14.28504 | -46.13894 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README62.md)
