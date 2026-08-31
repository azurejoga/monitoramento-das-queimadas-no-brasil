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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dab49a62-02d4-3ca6-b5a1-a4b32b5dbb39 | -9.2081 | -65.7857 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 2bb5111e-2fea-3caa-b55f-83325ce1d3a2 | -9.9646 | -66.8252 | 2026-08-31 18:30:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9b2e083b-7fed-32d1-a513-65a2ac303e1c | -6.1183 | -53.5472 | 2026-08-31 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| ca5778cc-4ad4-374a-92a4-1dac1fa753db | -9.12 | -61.6011 | 2026-08-31 18:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 95ac191b-74d4-3dae-a865-55addcaf498d | -11.1809 | -55.0821 | 2026-08-31 18:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5466c867-21e0-3a13-8b7c-5518a9865ce2 | -9.1719 | -59.5017 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8318e333-de06-3ef1-a665-41c4fc661bbb | -12.3814 | -48.1655 | 2026-08-31 18:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7ee98708-37f5-31ff-ac6b-f0ac7822303b | -15.8649 | -56.4841 | 2026-08-31 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e2ee80cf-e193-3360-bc85-8f1ee81084f0 | -6.1109 | -57.684 | 2026-08-31 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| b0498a5f-1f00-3a43-ac36-5df5189a28eb | -8.3413 | -71.0291 | 2026-08-31 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6513b00d-58db-34cd-b426-a8f5d7749065 | -11.0933 | -51.5345 | 2026-08-31 18:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 224b756a-279c-3d5d-9076-aab0bd0831dc | -3.4002 | -61.3276 | 2026-08-31 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a68c47c1-c660-3952-b57c-f26baa714268 | -10.844 | -45.3356 | 2026-08-31 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 735feb68-c203-3f8b-81dc-83484032b112 | -10.0125 | -68.8476 | 2026-08-31 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b15ab411-fac3-32e6-b4b3-376526e755cc | -8.3785 | -70.8639 | 2026-08-31 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 61af371e-482c-3c60-a5c1-59608e6d2d08 | -9.0152 | -60.6099 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 69036277-115f-380c-bc29-4d32a361fdf4 | -3.1083 | -61.2191 | 2026-08-31 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| caaf41ae-f414-32d1-bdec-76a6030548dc | -15.6333 | -56.4081 | 2026-08-31 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| addae380-000b-38c4-b403-97ab6ee6324a | -9.9708 | -53.9419 | 2026-08-31 18:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c6640ae3-9825-3476-8208-24ae20b5caa9 | -6.137 | -53.5259 | 2026-08-31 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 73873a60-513c-3a89-855c-6f24270dc4df | -15.6139 | -56.4103 | 2026-08-31 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| cdad307a-245e-373d-9a2d-bef9087d74eb | -7.9239 | -44.2327 | 2026-08-31 18:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e529840a-30d7-3d37-9244-98e6592682c4 | -15.4036 | -52.7076 | 2026-08-31 18:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fdce6a5b-895b-30ae-9c24-e0a0739b9715 | -9.1906 | -51.546 | 2026-08-31 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| cf95ac74-f871-313e-b4bb-8d0a1e8208b3 | -9.4153 | -45.6726 | 2026-08-31 18:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 8ca98924-b324-3c57-b136-eacf03748f7f | -8.8521 | -66.7641 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 51e9e633-c154-3962-b6fa-6163d9d6f544 | -9.0612 | -65.4916 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e6d9019e-e6db-3e98-9a21-09af7b90937d | -11.1995 | -55.1008 | 2026-08-31 18:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a8655eb0-f9b0-3bbe-85ee-301c51262669 | -6.6542 | -59.426 | 2026-08-31 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 52225133-9a84-3826-88ab-022ec2e0395b | -15.4231 | -52.7049 | 2026-08-31 18:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e9a851ae-b1ef-335a-b00b-bb3322bf2a66 | -14.5868 | -54.1153 | 2026-08-31 18:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6bbbde44-a920-3aad-bfc4-ea3de85e8d1e | -11.2317 | -53.9958 | 2026-08-31 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 11281403-b088-3621-abf3-433b8ac5e5ee | -10.8046 | -50.5046 | 2026-08-31 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| bbc83a05-3010-37e0-88a1-4916bce4fee1 | -14.2369 | -51.9498 | 2026-08-31 18:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b81bd4e1-2d33-3f9a-8682-00c65e506e39 | -9.2089 | -51.5863 | 2026-08-31 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| db5c1d30-bcdc-3dfc-9fd4-3f82c190217e | -11.2314 | -54.0164 | 2026-08-31 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ad67fb28-6d16-39b1-8887-3f254e1910e9 | -13.4519 | -57.039 | 2026-08-31 18:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| cda2dddc-7e3f-31bd-93b8-cbc771f3e080 | -9.6048 | -68.6164 | 2026-08-31 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f2947fe4-b306-3fd9-b136-88f186298c45 | -14.2792 | -52.8758 | 2026-08-31 18:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a135091f-ee45-390a-95c1-69b6e5c08ee5 | -11.0744 | -51.5365 | 2026-08-31 18:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 6ef64952-0c92-333c-bd4d-5ca099ca1c37 | -9.6939 | -65.1145 | 2026-08-31 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 136.9 |
| dce46545-6888-321c-851d-426cbfdc1177 | -11.6967 | -54.6081 | 2026-08-31 18:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a310c528-31f3-38cc-8c82-955e97ba6a45 | -7.6253 | -55.2787 | 2026-08-31 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 1352a90b-49d7-3b69-934c-397522df9ee8 | -12.0925 | -44.996 | 2026-08-31 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| cb1109bb-63a5-380a-8bb9-678fb56bc47c | -6.3844 | -55.2251 | 2026-08-31 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 84914fff-cedb-3590-a15d-424524a06de3 | -13.4137 | -57.0426 | 2026-08-31 18:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e1ab668f-b81e-3b57-9510-e9a0f2fd3f8e | -9.173 | -59.3659 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eeb9c291-5897-3983-a1b6-2788979ab575 | -14.5871 | -54.0944 | 2026-08-31 18:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3f9fbf60-a403-3467-88b0-800483f185a5 | -7.1435 | -72.864 | 2026-08-31 18:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| e9508973-5ce5-3551-8bb2-0b837c836ecb | -9.9896 | -53.9404 | 2026-08-31 18:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 2983b15a-d193-3c67-b1bd-2c030065ccfb | -6.9521 | -58.9506 | 2026-08-31 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6df8d25e-1e42-31ee-af34-ea9f4a59f6ba | -7.917 | -61.3481 | 2026-08-31 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 5bf9e6f7-1b91-32c7-a864-52c851cdd4ba | -6.8568 | -59.4757 | 2026-08-31 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 08f5f02d-e789-33c3-91ed-75ad17bc9c7d | -7.6066 | -55.2998 | 2026-08-31 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 50dee582-8d87-3fab-9b82-602493e3bb2e | -3.1449 | -61.1808 | 2026-08-31 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 86f3d3b6-9f1a-33bb-831e-04496376cd74 | -11.3236 | -45.1778 | 2026-08-31 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2634232d-f0b3-3707-a349-0ccd0f3562dd | -11.381 | -45.1697 | 2026-08-31 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| cc743def-3c1c-3d99-85a3-a63dad0146a9 | -9.2092 | -51.5654 | 2026-08-31 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b8755006-8723-3391-b419-8810a9077bbb | -9.971 | -53.9214 | 2026-08-31 18:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 7de289cd-ce9f-352f-92c8-f16fa0341400 | -3.4979 | -59.0409 | 2026-08-31 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| f201d4fc-48ec-3fc2-8393-8f5f32b2fffc | -8.9295 | -62.3712 | 2026-08-31 18:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 180ee3ea-c2c5-3cda-be73-3e525dec5dd6 | -10.7462 | -47.9536 | 2026-08-31 18:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8679426a-c71d-30bf-8766-fb4df86af6af | -8.6674 | -62.8179 | 2026-08-31 18:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 80f598be-67b6-39f0-a624-d7eb5f2696af | -9.1718 | -59.5211 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e2c343e8-45eb-3d48-a399-398c209dfc2b | -9.4721 | -57.0156 | 2026-08-31 18:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 15aec634-e8c2-34b9-8627-3985f29ae633 | -6.8416 | -41.7272 | 2026-08-31 18:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| d33bbd0e-20d6-32d7-84e6-cb0b01170f0e | -9.2256 | -59.7894 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d167fad3-968c-3851-a8f6-6970a3c713f2 | -6.1368 | -53.5463 | 2026-08-31 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d0feeeba-c59a-30ec-b414-1ea14b3eeaf3 | -14.4831 | -52.2151 | 2026-08-31 18:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4ff69afb-d550-38b6-ab4b-b2e53caf933c | -8.5363 | -67.1617 | 2026-08-31 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| b29ba0c9-5d58-34a8-bf3f-3d90b0f10251 | -9.1529 | -59.5609 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 815d8cf5-53ba-31f9-9ff2-b4e79d5405ed | -15.653 | -56.3854 | 2026-08-31 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8660ffe3-5cdc-3a4d-8a2a-6ac9586ad480 | -4.1515 | -60.7068 | 2026-08-31 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| a6c8fc2b-d83a-38e8-b086-d68e1389253c | -10.7856 | -50.5066 | 2026-08-31 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 153.0 |
| f5c666a0-28d1-396b-bb14-6e0429b618b2 | -4.1698 | -60.7064 | 2026-08-31 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| aa36c763-db07-3e53-b243-52e27f1a76f8 | -10.3388 | -49.9977 | 2026-08-31 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 260.2 |
| ddcb968c-f46b-3fc4-82d1-8c1c1b6bc3e7 | -9.6676 | -47.9429 | 2026-08-31 18:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 336.9 |
| 7dc7506f-90e7-3c43-80fe-f94925f1299f | -15.2475 | -53.8876 | 2026-08-31 18:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8a59b42d-0d1f-3bf8-90e0-24562fbb99a0 | -6.7699 | -55.6644 | 2026-08-31 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6abb07ac-7b69-3d46-89ed-a08fb003d940 | -2.6741 | -59.3628 | 2026-08-31 18:30:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| daba4056-81f0-3ffb-adc1-eaffe34c521e | -5.9636 | -57.6704 | 2026-08-31 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 9b1b33bf-bc6f-3a3c-a1f9-8201de9773c7 | -14.5028 | -52.1913 | 2026-08-31 18:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b5377e2e-0090-3e46-bb3c-e8f55d4855c2 | -12.9032 | -45.8382 | 2026-08-31 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 7638de03-dc46-3c7e-83ee-11b70439e8c6 | -15.2669 | -53.8851 | 2026-08-31 18:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 168.2 |
| bd40d574-2846-3c31-b066-1bc076268554 | -8.9874 | -65.4192 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fdfcd802-0a54-3cae-afd5-83e047565e91 | -15.0244 | -48.1689 | 2026-08-31 18:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 865fd5fd-0cea-3774-8951-2d1248254759 | -11.6649 | -47.5957 | 2026-08-31 18:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 12819e0d-e38e-3bff-9ad9-f9b1d366dae1 | -8.4896 | -70.6243 | 2026-08-31 18:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 460a474d-a6b0-3613-b627-f57b193784c6 | -5.8537 | -57.5576 | 2026-08-31 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 40f3bd9a-b3c5-364d-9c77-45af2bd5ec28 | -8.8026 | -71.0783 | 2026-08-31 18:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0ce60d68-b2b3-3548-92f3-0a384ad78b02 | -10.2731 | -68.7675 | 2026-08-31 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 4075b69c-2d40-338a-b647-4b052fd58b6d | -9.2086 | -59.5773 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f49ae217-0674-34a4-8673-290a06573393 | -9.9898 | -53.9199 | 2026-08-31 18:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 7b1f64c5-6ec9-3301-a754-753f0fce4257 | -11.1807 | -55.1024 | 2026-08-31 18:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0f48033c-1aae-38cf-97f7-727c14c4752b | -12.0925 | -47.1587 | 2026-08-31 18:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 46d14971-b1d6-358f-9b9c-9c82ed8cb7f2 | -14.2599 | -52.8782 | 2026-08-31 18:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 50402a59-5380-3935-b9a6-288f8152eae0 | -8.574 | -66.9569 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a8881f1e-c12c-381b-a9d0-46476fe2f867 | -3.6076 | -59.0769 | 2026-08-31 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 32ec5a8a-9a64-368e-990c-ac65ad212891 | -10.572 | -57.4752 | 2026-08-31 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ec34a62f-5bbe-330b-9987-fb1c978dcb50 | -8.9428 | -63.2797 | 2026-08-31 18:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |


[Clique aqui para ver as próximas entradas](README186.md)
