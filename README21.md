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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5521ffa-7f18-35c7-99d9-2db950304fe9 | -5.93173 | -43.33321 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 568e0c78-059a-327a-b7de-0f629b796079 | -6.61394 | -43.72244 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f240342-a7e6-31ea-a8e3-419308504e8b | -6.44623 | -44.15572 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d065fb52-3d4d-3055-908d-d5547d869aef | -6.40414 | -43.05867 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a557756c-b61d-38dd-9829-b402b40b5089 | -6.22122 | -42.92366 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e452bd8c-f925-3478-b3d4-d72a7c772f47 | -5.94514 | -42.87921 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d42d8975-68fa-3749-8dc8-69b7a551abb1 | -6.02454 | -44.02068 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f50ce5ae-775a-33c9-a42d-4c1eecd46278 | -5.79137 | -42.96777 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62d96235-0ad0-34d7-9772-cf83927bde99 | -6.70145 | -42.15466 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a498491-ad57-3463-9fa2-44433769f178 | -5.88915 | -42.9141 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| d4b68e31-ea23-398f-8d47-f31d9d26b765 | -6.60768 | -43.72132 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9bc0d7e-d09e-3cb3-a4a0-476759336e4d | -6.60905 | -44.32032 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94fd26a3-db33-3de8-9ca6-c95d5110ce8b | -6.14436 | -44.66744 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8801218a-2c26-375b-abe3-ba28d4452e41 | -6.4047 | -43.04699 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e63bb1a8-667e-3927-85fa-4c15f317ddb6 | -4.44178 | -43.2354 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 821cd2fa-5bee-3aa3-875b-7ca9419357e6 | -5.89876 | -38.48798 | 2025-10-05 03:32:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a732bf38-4bbf-3512-a97f-ec3e5f08029c | -6.40935 | -43.06416 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 54806b02-4ae3-30fe-8ccc-af0abf2facbe | -5.77761 | -42.97469 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3a16fa61-61bb-3bc1-a589-6895081b2203 | -4.44352 | -43.24379 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cdbb11a6-29c4-3a25-8e39-8c517f383890 | -6.25268 | -45.37862 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 235a71e2-879d-3d24-8915-d4c7347bb1e4 | -5.78366 | -42.97578 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e2a58c2c-89e9-3e74-bc3f-b57a50f28275 | -3.84533 | -41.5757 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e26655f4-2cb6-3fd8-b974-fc848f767e3f | -5.89516 | -42.91516 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 446946c8-bc20-31b6-862c-15be7446cab5 | -5.83685 | -44.4543 | 2025-10-05 03:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e0d090f9-d41c-3db4-90a9-c6f3f27003e7 | -5.77738 | -42.94199 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 7d4acbd7-7256-38fb-a99e-17411a7803f0 | -6.40674 | -43.07041 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c3e78f33-c71a-31a5-97aa-ca1b7149ac41 | -6.3434 | -44.0262 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 261d9278-7731-3ac2-9ce5-deb2099736e4 | -5.76513 | -42.9698 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 866c0f6b-eb21-3875-ab23-1b77d85b0f98 | -6.88228 | -38.53803 | 2025-10-05 03:32:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a8979b7-7268-3178-9b8e-98baa24814e8 | -6.61482 | -43.7177 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59f85b34-6ff9-3073-8135-c34d581bdda7 | -5.87127 | -42.54067 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 72777008-d89f-305d-abf0-ea014dc1b712 | -5.8754 | -42.54008 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1965ee97-fc4a-3aa9-af39-1d6105524a0f | -5.77571 | -42.95105 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 46913601-7b5d-3ab6-bfd2-1d5d7a728bee | -5.46441 | -42.78903 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 933b07a6-bb86-3371-9ff9-0a449262c0d0 | -7.51916 | -37.99189 | 2025-10-05 03:32:00 | NPP-375D | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 89ac27dd-566c-3d50-8c7a-077db01f405b | -3.84735 | -41.56383 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3dc100bb-1aee-3af4-b368-33fd9e8acd3b | -3.44239 | -43.34518 | 2025-10-05 03:32:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8290f12-9b6d-37dd-a0be-b8bd3a10e245 | -5.91799 | -42.89222 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 337f98c6-a9ed-3154-8bd3-fba7e243ae44 | -6.70276 | -42.17952 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e0041b0-8325-305e-8a46-96bf85e4b785 | -5.91122 | -42.89532 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ac57ade3-8ed8-34f2-8116-34f99651de31 | -6.15642 | -44.67672 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1f9dee7b-cf6e-3f2b-8263-3651e91dbfd3 | -5.24633 | -42.63912 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c587179a-a174-3a36-a5e7-2b37e435c56b | -6.67047 | -42.38939 | 2025-10-05 03:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8c4a3c83-5797-3128-8b0b-ac8336d2caef | -6.91997 | -37.44594 | 2025-10-05 03:32:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f888e4ad-2214-3db2-8818-ec500671ae70 | -4.89013 | -37.50003 | 2025-10-05 03:32:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c053b58-3be4-37ff-9e6d-e4078f888803 | -6.62419 | -42.41495 | 2025-10-05 03:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ae45ed2a-bc50-33be-8823-d21e97786054 | -7.01139 | -40.32137 | 2025-10-05 03:32:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7226a980-d9cd-3013-ae4e-775ac544b2fb | -5.92469 | -43.33683 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 462e09b0-1d02-34eb-8d7e-4e1aad709b8f | -6.11951 | -42.85957 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 828b846b-2b53-394b-98f2-80074a612a05 | -6.15418 | -44.6517 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9bf92c3-8601-3eee-b3d9-3fd13be0df5c | -5.89584 | -38.47794 | 2025-10-05 03:32:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 667a1968-8dd8-3382-a6aa-c8124335b564 | -5.94309 | -43.51614 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e91b099-131d-3538-a154-7f605878185b | -6.55671 | -44.16954 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 874d5348-eaea-3e5e-ba4d-30e40357a28d | -6.59602 | -44.31829 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d62d1b7d-2c13-329f-adfe-441c8c588d1b | -5.97565 | -44.35586 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c6c60ce-d7d4-32b0-ae59-d039751d0fe0 | -5.47044 | -42.79003 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8759f95b-fb2f-3b4a-9ff3-9749c3ee5db0 | -6.14686 | -44.67315 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c1f30314-440b-34bb-b8ff-69f542a24271 | -6.55897 | -44.15733 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4458306-2389-3d42-b0f7-ac0b10f9d66e | -6.40837 | -43.06124 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f58df413-57a7-3523-85aa-08be11b88c63 | -6.92058 | -37.44229 | 2025-10-05 03:32:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31d5d9bf-3aac-3b54-99a4-6d6f4b41caaa | -5.86956 | -42.53882 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3d38c2c-526c-3f96-8eac-f9f772140f6b | -6.43871 | -44.16036 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad8fbfd3-734d-3bd5-a3b2-f4a66465b2ac | -5.97745 | -44.35519 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672af81e-4e42-32f1-bfd5-f404e77afa4f | -7.0525 | -42.77715 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d1a9b98-850c-3010-96f6-dd84888e876c | -6.1506 | -44.61398 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9fb828a4-254b-3b57-b624-3e5ca82466de | -6.70978 | -42.17309 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 639e027a-3cc8-3f15-8ad9-a0d261d27809 | -5.77843 | -42.92985 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| a827764d-ee8b-32fb-9bce-713bf1b9eb84 | -5.77238 | -42.96917 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59cafc23-52ab-3977-b23a-f5472cb1c587 | -6.45945 | -44.58065 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cb256e31-1702-3505-ae6a-021357923e19 | -6.06328 | -41.23997 | 2025-10-05 03:32:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a13f9df8-1a40-36e7-92b9-d25bbbc3a4d6 | -6.24554 | -45.3785 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a218e4c-7abc-3cb2-8fe2-da4e25ff8105 | -5.92645 | -43.3273 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e7f45043-5c69-39f2-a3cc-c5ec677e1e67 | -5.77761 | -42.93451 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 5bf2e07a-273f-3223-b849-8b6c95ed82b3 | -2.91592 | -40.46683 | 2025-10-05 03:32:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52ce49b2-38bd-3266-99c3-5cf50821e15a | -5.26887 | -39.26216 | 2025-10-05 03:32:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b8041c2-ba8e-3b6a-89cd-a9e9ef245a8a | -3.87402 | -40.91173 | 2025-10-05 03:32:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80da84a3-074a-3f39-8e37-ff898456ac13 | -6.70074 | -42.15855 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c97e4a8-b394-33c6-8dbb-43254fd4d5a3 | -5.22105 | -43.70765 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6411230c-4ab7-34db-a854-4e98b0b75dab | -5.84393 | -42.88383 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0752a058-7b5c-3aa5-b6f6-5c7d5b498a3a | -5.54925 | -42.6688 | 2025-10-05 03:32:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 14d9142c-0d53-3d19-87bd-cea4c206e617 | -5.49374 | -42.79856 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 59c6ba44-7935-3d22-a03b-99c9d73c7d2d | -2.91232 | -40.46575 | 2025-10-05 03:32:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa68e72c-61b0-3a09-97b8-de62b1a7ea3e | -5.85258 | -42.8015 | 2025-10-05 03:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3aa7f8da-9738-318a-ad99-a33cf814f0d3 | -6.707 | -42.15625 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 491fb913-1fce-35f1-91bc-b4f5a70babf7 | -6.15103 | -44.64985 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 26098995-c810-3a66-a7ba-c1b63d936fe8 | -3.67146 | -41.76064 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c591ab9c-412c-30a2-aa72-56709bdba30c | -6.67193 | -42.3814 | 2025-10-05 03:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 695113e9-4199-348f-93b7-1b59461cba28 | -6.11778 | -42.86894 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 953a54f2-9693-3b40-a408-c9f2eb1a6a23 | -5.47563 | -42.79574 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 44157abf-8cb1-31e4-becc-82f0f14d4485 | -5.25536 | -42.97473 | 2025-10-05 03:32:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc8ea26e-47de-34d0-a0f6-45eee80e4dbe | -5.872 | -42.53653 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8097e281-d595-39fe-b867-9c68086dc9c3 | -6.14961 | -44.63924 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e14b7525-4d0c-3565-907a-302070b1433d | -6.16189 | -44.6472 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bb13299-9809-3838-b080-d89cae943d1e | -6.34952 | -43.91561 | 2025-10-05 03:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06f97ff7-d7bc-3839-b3de-683b71542547 | -7.03574 | -42.76961 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa981226-b3eb-30a9-a1e6-946c76d607f3 | -5.79743 | -42.96876 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d23b0768-0a65-38e1-8ac9-1ae29df54446 | -5.77196 | -42.96648 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7023202-d197-3c2d-8a4c-a935eeceee76 | -5.92093 | -43.32932 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4199e139-7d61-3ea4-9c09-8746ad4b05ac | -6.70069 | -41.95045 | 2025-10-05 03:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a9a6f22e-25b3-3aed-8048-d7806e3540bd | -7.52339 | -37.99253 | 2025-10-05 03:32:00 | NPP-375D | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |


[Clique aqui para ver as próximas entradas](README22.md)
