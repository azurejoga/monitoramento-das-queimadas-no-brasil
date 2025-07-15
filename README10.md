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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e635d102-b309-3ec5-8cfd-2dd1464becb2 | -5.78264 | -45.09359 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fa10ae0f-e132-3d6a-b0b5-98eaf438a2c0 | -4.21946 | -41.7701 | 2025-07-15 04:08:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 117f438c-144e-3052-a42d-657d491ed48e | -2.91384 | -48.24306 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 63e4546b-0a57-321c-9192-f1bb39fc6a1c | -6.24589 | -43.34408 | 2025-07-15 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f863bfa3-e7f1-3322-9651-3f4b0a7695eb | -5.43077 | -43.17794 | 2025-07-15 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28bc232c-dde6-3d30-ad3e-a65c62cbd7fa | -4.61753 | -43.32188 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 270327ae-a95a-3cae-b21b-8a8475c6e38c | -6.14024 | -44.0853 | 2025-07-15 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7090d1ef-1654-3528-8e7b-7441b5f11d32 | -4.61406 | -43.32132 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b3ad55c-714e-3675-88cc-4af1e5ed9ac7 | -5.42734 | -43.17739 | 2025-07-15 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c981a333-5d09-37b1-823d-ca83d4169b68 | -5.57709 | -46.5274 | 2025-07-15 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7d1ad9c-2441-3719-83d7-75eb1b61d70f | -2.91946 | -48.23867 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5b6f9fd9-c8f7-32de-9adf-c6e97f047d8c | -4.4593 | -40.85426 | 2025-07-15 04:08:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ccfc4ab2-3e1e-3942-9d0b-a149af551cc6 | -5.33506 | -43.75216 | 2025-07-15 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fafcdd5d-51d2-34e3-9c73-3a4fadac8325 | -5.79111 | -45.1158 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b1df445-4cdb-3fd6-8b51-ec1aec0251e6 | -5.53273 | -43.89149 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6017d1d2-41f4-3b62-a2a4-b5886f4eba9c | -3.42934 | -43.34935 | 2025-07-15 04:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de35ab0d-889c-3b60-832c-5fb26c730cb8 | -4.0112 | -49.46856 | 2025-07-15 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21f2f17a-4756-3c17-937e-ceef9626c583 | -4.7771 | -45.34081 | 2025-07-15 04:08:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0674347b-fa96-3673-b89d-b786e6177522 | -5.48623 | -42.15006 | 2025-07-15 04:08:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9cce5637-96f4-3f3e-9e68-4f37962fbdc5 | -5.23462 | -40.87268 | 2025-07-15 04:08:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a1819e5c-16d8-3eca-a479-ec45ee58e78e | -3.36259 | -49.16699 | 2025-07-15 04:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 460e0246-4241-393d-9d7e-3e717af9914d | -5.69613 | -44.2437 | 2025-07-15 04:08:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd7a9e18-31b2-3fe3-b2a1-18479cea705c | -6.29005 | -43.41988 | 2025-07-15 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b51fa29d-c3b8-39f7-a140-016527da877f | -2.92783 | -48.24124 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88177859-7837-3617-9ae3-86ea52e54b15 | -5.33092 | -43.7555 | 2025-07-15 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae623cb-48ef-3da1-845c-a318a18ff48f | -6.28903 | -43.41895 | 2025-07-15 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4165f365-5d6a-3520-8bce-bccddca3b5c1 | -5.58118 | -46.5281 | 2025-07-15 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 578fff2f-8f9d-3dfb-aa68-b2b8e2a2606e | -5.69905 | -44.24836 | 2025-07-15 04:08:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65bcceab-b912-384d-8d05-356627eae9f8 | -2.9239 | -48.23527 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aad62c2d-ccd6-3278-8994-1986850845e7 | -5.77312 | -39.59365 | 2025-07-15 04:08:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd9c6835-a125-34d8-bc3d-ff88b90ace9c | -6.52979 | -42.37676 | 2025-07-15 04:08:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7ae377c4-ac5f-3738-9b6b-d3dcc8067afb | -2.91823 | -48.23968 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 06f65607-9d44-3a45-8093-c137c23af7ee | -4.7786 | -45.34342 | 2025-07-15 04:08:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23d6ea28-c9a8-30e9-9a96-c62b18b6483c | -5.53626 | -43.89205 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 342f695e-c8d3-30a1-9276-582e6b54b287 | -5.53753 | -43.88411 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fc326b8b-2754-314c-9c9d-d06dc1cdd2d6 | -5.79395 | -45.11856 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8188723a-509f-384e-9f95-d649f322e18f | -3.92599 | -43.15297 | 2025-07-15 04:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de9efb97-a720-38b3-bd86-54725080bb29 | -3.38025 | -47.46838 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d334bb1-a882-34cf-94bc-81bf4c47905d | -3.7622 | -47.11807 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 64dc4902-ec95-3a02-9ccd-7c2161bc0cdd | -6.1367 | -44.08478 | 2025-07-15 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6516e7b3-e07e-3836-a2d9-930bd8b1f315 | -4.0356 | -48.05855 | 2025-07-15 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb30681d-b014-31a6-9c7c-04286424d272 | -6.36243 | -42.64051 | 2025-07-15 04:08:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a3ce2290-277b-3758-a407-943545fa80ae | -5.36859 | -43.92187 | 2025-07-15 04:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1c2468d-86f4-3f25-ac97-db77016aad7b | -5.36505 | -43.92132 | 2025-07-15 04:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c147b6a-1695-3d52-8bd6-86717c559401 | -11.4588 | -45.0895 | 2025-07-15 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 1dbaff7d-2572-303c-8b2c-f0c09257ee18 | -11.4393 | -45.1154 | 2025-07-15 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 549b6994-5b7a-39cf-9371-8e0ba057192b | -11.4397 | -45.0923 | 2025-07-15 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 0433b319-80cf-36ff-bd3f-70c2146a44c3 | -11.4584 | -45.1126 | 2025-07-15 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8a10596b-df2f-351d-9e8d-da3ce4884f9e | -11.478 | -45.0868 | 2025-07-15 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4991af18-3288-3a81-9833-2322722efc08 | -10.5586 | -49.1337 | 2025-07-15 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 486794a3-89dd-3293-94e0-405a32c64472 | -5.3741 | -43.9216 | 2025-07-15 04:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| e2b03dd1-8435-363b-ae25-8bbb13cca29b | -12.06928 | -47.98617 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e5770d-3140-335e-9171-067eb22766c2 | -10.88617 | -54.04763 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c1b0392-6df2-3086-b7e5-adbe6a79de15 | -6.71764 | -44.32852 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc77e92c-4435-3bbe-8a83-6e8dda13e975 | -11.43976 | -45.129 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ca4c6a74-96b1-3865-bfd4-a5dedb48be3e | -10.88524 | -54.05223 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08f4bbc9-6b36-3ebf-bf59-7a5d778fee39 | -8.65084 | -47.74969 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f4f48f2-f361-3b33-bcd1-70d4cde6a387 | -9.61733 | -49.02185 | 2025-07-15 04:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71c7d44f-7529-30f5-825d-70cac16cd5ea | -11.35978 | -48.73063 | 2025-07-15 04:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea09ac20-4c2c-3d08-aed3-ae3f1aa43f4c | -8.22989 | -44.92073 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70c02d61-565d-3ef8-991a-c6e657d684a2 | -13.65844 | -45.73502 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5de2776b-c127-3d1d-ade7-33d37479a0f0 | -8.25822 | -46.36563 | 2025-07-15 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bab50ff-13fd-398c-8585-ccb17e3f076b | -6.54686 | -44.68373 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bb21299-76e1-30fe-aae3-6a13409358a1 | -8.5882 | -47.43801 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef5a140-197c-3209-801c-22b68948cad0 | -7.09604 | -45.4515 | 2025-07-15 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47058223-8d67-30cd-81ff-935cd2103cae | -10.64938 | -44.48574 | 2025-07-15 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 026f98f2-1d0a-3eb5-ada1-c8e3967d6b99 | -11.4575 | -45.08759 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 359c36d3-e8ba-346a-a52b-a68ddbf15595 | -11.72985 | -47.05804 | 2025-07-15 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4591d397-3b2a-3d70-b1e7-c6a1c536caff | -9.79372 | -47.74267 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25aff3b1-6772-3c40-b535-35eace298296 | -10.87779 | -54.06454 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb116754-61e0-3d8a-a5f7-360be221af99 | -11.45685 | -45.09148 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 567a6afe-c4d9-3fcd-9ee9-8c7cc42334d7 | -6.38095 | -43.71592 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3362a81a-8235-3fdd-96a5-b6c8ac3f726c | -11.9008 | -46.7578 | 2025-07-15 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7ebd9d4-3309-3f2c-bb26-5673fe93d30a | -6.38504 | -43.71266 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e221f72f-a3b2-345b-a3ae-f6412ed89254 | -7.53849 | -43.92532 | 2025-07-15 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aca8c718-21c3-35b8-b666-2f54b61421af | -6.71409 | -44.32793 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf37867b-5906-3064-8e70-bcccac2bb155 | -11.45205 | -45.0987 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 449ab446-9887-38ce-bd85-47edb6f2fcf4 | -8.64662 | -47.74896 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c677ef36-7a2b-3b11-8ca3-3c51cdaa2042 | -7.19959 | -43.10479 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 73f63586-9084-39ee-ad89-b7071c17bd7a | -7.00598 | -43.86915 | 2025-07-15 04:10:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e989e81e-8592-3f0c-b411-8d7386c18a64 | -7.15837 | -42.99459 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08237966-23a1-3c4a-a6c2-53edad6a9953 | -9.79625 | -47.73862 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffa7c0a7-f23b-3150-b680-c7135eceb475 | -9.98162 | -48.08461 | 2025-07-15 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 020e4256-428b-358b-af6a-aaaf4cb6346d | -11.36054 | -48.72647 | 2025-07-15 04:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0d6acf8-b414-3c75-babb-38b7f1d501b8 | -6.71034 | -47.79987 | 2025-07-15 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 429b7b06-bbfb-34c1-928e-8525e75635d0 | -10.87257 | -54.05856 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ec9e6a-ae1d-3f31-8cec-018372392721 | -7.09872 | -44.38484 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eddbbf1-1dba-333e-a997-744a28459926 | -7.75887 | -40.63014 | 2025-07-15 04:10:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c264fc01-45df-3f5e-80a0-60c36ae29f23 | -6.99145 | -47.08814 | 2025-07-15 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4a4cee1-ddf2-3080-87a4-604245c27b66 | -10.28043 | -47.61728 | 2025-07-15 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 925932f6-44fe-3f95-9f13-dc5fe53399e3 | -10.64467 | -45.21901 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc42cf88-9adf-3c52-93f0-eaa439784327 | -7.30075 | -45.36205 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e0a3ff9-dd73-30f5-9a49-a947c3db0118 | -11.45139 | -45.10263 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d13f27e2-7a14-3712-8ae2-7263f58dcc7b | -9.43611 | -40.31691 | 2025-07-15 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf1e7bce-a24c-315b-8f7d-e33a639efc32 | -8.59711 | -47.43577 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ac55c9a-1829-31ec-8965-a2ba933c09c3 | -6.87743 | -50.27051 | 2025-07-15 04:10:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 735b1d5e-1998-3af1-871f-803e540ee394 | -7.88844 | -44.49851 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61dfd283-b4db-317e-add6-27c138918bff | -7.20557 | -45.33018 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0a421ff-4a61-325a-b866-a0614fce340d | -13.76386 | -42.6169 | 2025-07-15 04:10:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8fef00a6-c05d-3509-b462-efd8de0f5306 | -13.6521 | -45.7298 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README11.md)
