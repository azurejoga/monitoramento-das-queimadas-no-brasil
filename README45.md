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
| 688595b8-dd3b-3349-8d42-e751a4d7748e | -8.58313 | -46.31174 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| b6bc81c9-86a2-3aa3-8fbf-5c8a67f4b0e5 | -8.55043 | -46.27278 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cfc3888a-e0bf-336c-ae99-90b124c25fa7 | -8.54123 | -46.32564 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dc3d70d0-bad8-34d1-a4ab-c060367506fe | -7.24356 | -44.88894 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e5e2946-182c-3f94-89e7-71709b702589 | -9.55044 | -42.9585 | 2025-10-05 03:53:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 688520a0-2c92-3b87-a027-479e93f53596 | -5.34571 | -42.97079 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a643804-a8a9-3602-a392-4087cb64795c | -6.46119 | -44.57713 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4a3a5946-86fc-3af4-9724-895ed672adba | -9.36791 | -43.02718 | 2025-10-05 03:53:00 | NOAA-20 | VÁRZEA BRANCA | PIAUÍ | Brasil | 2211357 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d64b6958-a571-3c7b-9af4-254389d14779 | -7.25165 | -34.93834 | 2025-10-05 03:53:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bfe5ec96-428b-38f0-a551-a2c97803366d | -5.4728 | -42.78739 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1af1befa-11b6-36a2-9302-5cd295b8a23b | -6.40326 | -43.06515 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d83df54-c906-3266-a690-6f6259a15de0 | -5.23473 | -42.9859 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43eec169-77e6-3bef-a4af-454fe6c8773e | -7.47521 | -43.03254 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| af501c92-4399-36fd-9697-5c64945afddf | -5.78366 | -42.92434 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 37cdbd73-bb8d-3be1-a6c8-b1acf46517d5 | -7.71187 | -42.55767 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 75d77c84-e0ca-3a07-9fd2-9c656fc19a77 | -5.25555 | -43.1619 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0401effa-db1c-37e1-a977-e2a4244bc419 | -6.1491 | -44.65819 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cb839fea-0228-3400-aa59-b8e81086db34 | -6.55102 | -45.80746 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5964843-fb50-351e-9098-227878d60a8c | -10.00733 | -48.26698 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6255cf4a-6036-3dbd-b7b4-659389a664ea | -7.03047 | -42.80523 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6c41d3fc-e4fd-3fe4-a227-182d7d7f7076 | -8.21728 | -49.14481 | 2025-10-05 03:53:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 691fe823-76c1-3f73-8dc4-10baf8ea3ea4 | -8.86032 | -46.84155 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1af093a4-d502-371c-a14a-8556fbdf7ab3 | -8.23181 | -46.80395 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a39ec7db-e865-3202-a193-90ccfba98236 | -9.29135 | -46.0131 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 597cbebb-8b69-3b1a-ae37-9464c783556a | -5.48553 | -43.4061 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 656e3d7e-5bcf-3fc4-aff0-0843e560aaf8 | -6.15796 | -44.65981 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5da5b3d8-3d50-39bb-9f64-d2a8bd82ddb1 | -6.35847 | -43.91544 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46ea52ed-e945-3b79-9fe1-6bb8556421b1 | -7.72079 | -42.38916 | 2025-10-05 03:53:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b4879c99-61a5-3951-92ac-b90991bebb2f | -7.79975 | -42.56525 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ca083b73-4023-3a6e-b18d-ddaca4bb0620 | -6.0814 | -44.04119 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d82c6731-2ce9-3936-ae1d-9112e2b36ae0 | -7.43177 | -46.52048 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d69dabbf-8628-3b27-9c0d-123feb048221 | -9.0594 | -47.01992 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1176a87d-82ff-3a53-a76a-7732d560d7be | -5.48608 | -42.80545 | 2025-10-05 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3b3d95d7-24e6-3425-8b20-3ed1f5af5d21 | -6.38592 | -43.38894 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34fc5886-5165-3ac4-a16b-c581e5f663b3 | -6.69838 | -41.95699 | 2025-10-05 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4781ac70-a697-3356-ad4b-324b7b77a58e | -10.64049 | -46.35118 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 5a29ef31-7170-3ad0-9338-9b8a97c5726b | -6.84129 | -45.48521 | 2025-10-05 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d3dead4-c272-39e2-97f1-2a798f277e60 | -6.34546 | -41.62287 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a8ffc0dc-7545-31a7-99e2-94f1b5de437d | -6.08313 | -43.48107 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 434d0852-467e-330f-8549-1bf0ad43ab1a | -7.66282 | -45.46763 | 2025-10-05 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c937111-a018-39a0-8645-ed97a737c376 | -7.645 | -45.48869 | 2025-10-05 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0f1cbd4-843c-3c60-a633-225f7d44ed2c | -6.35381 | -43.91527 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 69f662cd-8d3e-3ce9-abd4-2b50a480cdc4 | -10.18822 | -46.72544 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c436013-fe16-333a-b787-4046aa0147ff | -6.24796 | -45.37022 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8179af08-8ae5-3316-b432-a5ec6eb38386 | -6.39704 | -43.61643 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45b3413a-6d4f-3d60-ac12-8822f84488ed | -5.86856 | -43.55699 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0939a55-41ff-388d-8dff-b6fbf5460be7 | -8.86421 | -46.84798 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c163674-1707-3e97-8acc-c7e09984fdc9 | -7.25166 | -44.8949 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d03b5760-9fbe-3278-81b6-b672ed6d5286 | -8.91735 | -46.07062 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44152b75-c9e0-3aa7-b52b-81b8cbcac43e | -10.64952 | -46.32758 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 99a374f2-99a1-3aa6-83d1-da505a64d617 | -7.87025 | -45.22808 | 2025-10-05 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef924798-8a58-31fc-87dc-f450b2fcae0f | -8.59544 | -46.29783 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a9fb2211-6f5a-30ab-afed-ef6033eb0e67 | -5.54122 | -42.66843 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1822124d-98a1-357d-8606-2fb02a849cc8 | -7.79153 | -44.51672 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69b40edf-ad52-3b86-8151-834bd2677b11 | -6.59979 | -48.05765 | 2025-10-05 03:53:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4068305-8f85-382f-bfe8-931b674b4b64 | -6.40984 | -43.05041 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 745ca89c-7966-33a0-8890-b22ac4429372 | -5.82688 | -45.81377 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fafd6ef3-1d5d-367b-85ef-2ac87f6e4d97 | -6.28155 | -44.03607 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ef3b3cc-ae1f-33bf-a75b-0d882378227e | -7.52177 | -43.85906 | 2025-10-05 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb0ce1d3-afe2-320b-ac3c-97a219888860 | -5.84107 | -42.84883 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 29532e9e-142d-333b-b014-aac4b6ba2809 | -5.4344 | -44.34872 | 2025-10-05 03:53:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e2c89c7-d5ef-3ac6-a585-545fcef482f9 | -10.39173 | -45.39186 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14747e5d-5110-311c-9ddd-71c3cc7c4eec | -5.71094 | -42.71084 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 05998318-5aed-3305-b2b9-e6170201a241 | -7.75697 | -46.31136 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67386a0c-61c3-3c3a-bd64-b5a6232520dc | -7.72324 | -42.55946 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3d1518b3-2005-39dc-93e6-4c31fbfef592 | -6.30259 | -42.4436 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 05fe5fbf-c40a-39ba-be34-42472fa32b1a | -5.85518 | -45.85165 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76fc669d-888b-3368-80e4-c45cbaee906c | -5.94161 | -42.87315 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c13e511-23df-3363-aab2-9e02444828a0 | -8.55632 | -46.26942 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 75bb5378-6194-33d7-b006-25ae4709838e | -6.40724 | -43.06578 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7bb5a761-6040-3121-bd32-88598ed930e3 | -8.1664 | -43.34858 | 2025-10-05 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ddb156a0-9acf-3059-87f6-d284a4c28faa | -7.03516 | -42.80097 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a2486640-a923-3a11-abc0-9b66ad9020bb | -8.55519 | -46.27361 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5ecfa6bc-3e55-3ff6-b32c-998bd0987849 | -5.98117 | -42.65769 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3207eda-6df4-34ee-b8a9-deae557f2faa | -7.24429 | -44.88462 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e3267cf-2263-3eed-be58-6ac983859069 | -10.35402 | -48.17374 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 395165f7-bdfd-35bb-a1e0-7912cadb76f1 | -9.29215 | -46.00859 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc8d2627-f413-32be-a05c-a72465bba74e | -6.8807 | -38.53885 | 2025-10-05 03:53:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f55c77f2-2bd2-3e75-9ea4-fcba10520fd8 | -6.69351 | -42.84756 | 2025-10-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 72f42522-0ce4-3fb1-b6b5-61ad4f55d2dc | -5.92747 | -43.33487 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 135f57be-f634-3186-be4d-83da8a727ed3 | -7.2685 | -45.2965 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d668ad1-dfb6-30d0-a06c-b1ac45a5d8a6 | -6.67218 | -42.78352 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66049932-a364-39bc-b4ed-d89dd759f85e | -7.79152 | -48.04931 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77aee3e9-a43e-3a95-abbe-95469b55ef0f | -5.8873 | -42.90576 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 9fe1c3ad-b01a-3ba6-beeb-8f4fd4c867d7 | -8.57744 | -46.31608 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e75936b5-fb32-3a72-9b82-2ae2e18cc297 | -8.90025 | -46.67955 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 522fc66e-af9e-34c2-8bfb-e68f0e0f8bc8 | -7.25787 | -39.41434 | 2025-10-05 03:53:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e1470cd-1544-3c97-aab7-bd4923406ec7 | -6.763 | -42.2431 | 2025-10-05 03:53:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9dfc8154-af67-3c98-a464-d63556397177 | -8.53485 | -46.33425 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25d56acb-5d3f-389f-8480-5518f3262643 | -6.14467 | -44.65742 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8c15468f-e3cb-3ca7-a13c-655502aa759a | -9.05415 | -46.98749 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79416dcc-fcb2-31a9-86ae-47e44cf3629e | -9.90494 | -45.95816 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52d01d1b-984a-3849-a90c-03fc6ef2f4a2 | -6.16044 | -44.11201 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04c1623f-98af-3f1b-8ae0-1f2f6f3cd792 | -8.56065 | -44.6393 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b4ee51d-f71a-3e28-9cbf-327d19d04b3a | -6.16021 | -44.64665 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7302f20-ff00-327d-829f-7ba69d0a7a9d | -10.00885 | -48.28867 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90e09594-93c9-3419-9238-652c8ef36d85 | -6.2333 | -44.26966 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42ede452-3aad-32ad-b1db-73bd535d228c | -6.06248 | -41.24728 | 2025-10-05 03:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31a05691-1b70-3bd2-aeb5-72c141e8beef | -5.41002 | -41.31674 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 328c642f-3490-3722-ac2a-ff78303d8166 | -6.6072 | -44.32326 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README46.md)
