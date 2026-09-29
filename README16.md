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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d8fe8da-fba9-320d-9719-a729513e1f47 | -5.73741 | -45.17533 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ba313c5-ff5f-3787-a7dc-3edae2666364 | -5.4883 | -45.30696 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cef5eaf2-a42c-3b06-b377-5aa5e85b10d8 | -7.01305 | -45.30324 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d36bbcea-8e4e-34af-a83f-d21d30e5ea37 | -8.24881 | -45.44296 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3fa089c7-982b-36bc-aa51-6cd12556a867 | -7.99154 | -43.25692 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 282f6ead-68d9-34e1-ad08-d3290dd15cde | -7.50528 | -44.55755 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22cfe5f1-936f-3955-9471-9a4481ba51b0 | -6.68648 | -46.98828 | 2026-09-29 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bff78d7-a18f-3906-a92b-386742de555c | -7.63939 | -45.51653 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 423d8a67-87be-38eb-9b7b-fd95d3f58923 | -6.12773 | -43.73375 | 2026-09-29 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 352a19db-3814-3a2d-80c8-d09b9809864c | -7.24458 | -45.26084 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7472c719-4e34-3be6-9cb0-363f32127f76 | -4.31832 | -48.63242 | 2026-09-29 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1712cf-e501-3464-8263-11ab91282379 | -7.32911 | -42.07992 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 430f6d88-5a32-3a67-9758-0f80dff4d7ba | -7.32856 | -42.08352 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe4f463c-afdf-30fe-a05d-f089039fb56e | -7.67223 | -49.07712 | 2026-09-29 04:14:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc6385dd-228b-3514-a9b1-b1bfe2ceb92d | -5.72973 | -43.27859 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c4172f1-9770-390c-b18c-6261a9c00caa | -6.653 | -41.79307 | 2026-09-29 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb607abf-cbf9-3b09-ae5e-7eb6e9fcbc4a | -7.83956 | -45.82177 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c0a84aa-a29d-385d-aae1-c9ea9ed30607 | -3.11926 | -40.99003 | 2026-09-29 04:14:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e843853-020b-36f6-829e-5ac0b1b3b4d4 | -4.12818 | -51.06104 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70f0dafe-aa7e-39e6-8416-a6e16dc9dc7e | -4.13285 | -51.06205 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a49eea5-8660-3742-b901-1b9405105367 | -5.73527 | -45.03396 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f55b912c-a6ac-38d7-91c0-d8ae4e0517be | -6.15195 | -52.91426 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f5a4c93-bb3a-3627-be3f-10955f02013b | -5.33201 | -46.19806 | 2026-09-29 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be252e10-4e78-374e-b5ee-4f345b3b6053 | -5.73056 | -45.17425 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ccd8300-842c-3d2b-8d3d-17149ede52af | -5.72919 | -43.28204 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da64e641-7a2a-37cf-b492-cd5c93629dc0 | -8.24203 | -45.44187 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64e66564-785c-320e-a1f8-3da23c16aa85 | -7.24648 | -43.36966 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0a233bd4-475c-3a24-8f43-7ae4ad7b4172 | -7.26905 | -43.37672 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9e32c0e-99a4-3f00-8a41-6d59622ade07 | -8.64315 | -45.34523 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b458f2b3-956d-3f70-b4e3-f9579e08acfa | -4.45802 | -47.91876 | 2026-09-29 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6cb05153-9801-353a-b6f6-18cb6569ddc2 | -8.24524 | -45.4651 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d284b680-7c6d-3e7f-8ad9-153f09c8d536 | -6.24221 | -41.58916 | 2026-09-29 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38341423-07ed-35a6-9c33-b518845bb086 | -7.95623 | -49.57962 | 2026-09-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19837015-767c-32c5-8c19-fc450d4eaea9 | -8.03409 | -43.33469 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd50c86f-d55a-3a29-8113-e8dc4e652599 | -8.24704 | -45.45395 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99b0ec1c-2ca0-3e3a-a104-2839c199135d | -8.36786 | -45.48786 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acc5d94d-514b-35d4-b02d-4fcf173f15d2 | -3.04899 | -46.92781 | 2026-09-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab36ca6f-c5f5-3306-9c1e-53562ea8ca1c | -5.73963 | -43.28013 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daa4fcc8-7709-3f16-a553-b5bc99b529b1 | -8.24922 | -45.462 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3c004ab-c465-3c45-9219-ccbaf7df62ab | -8.23387 | -45.47087 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aec0dd4b-bf47-3e12-8b08-edf9c1d3f194 | -4.72081 | -44.34612 | 2026-09-29 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd893909-6fd4-38b7-a32d-c39250bce1ee | -7.00965 | -45.30269 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5290033a-e439-3b94-a73b-267d6105019b | -4.0023 | -38.98273 | 2026-09-29 04:14:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 440e38ec-8bc0-3dab-ab0e-8a6ed04be999 | -7.39879 | -40.22522 | 2026-09-29 04:14:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 9487580d-95db-3901-ab14-abab89e60da6 | -6.19011 | -46.39079 | 2026-09-29 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d38c49fa-a954-3a58-80a8-aa637e30c7c1 | -5.73579 | -43.28307 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6827178-f817-32af-847d-5546130897c1 | -7.6985 | -44.92733 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4d6f19d-f301-3288-81c2-559a3f4f42ca | -8.2516 | -45.44723 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1c41e39-5c52-3896-84ec-0aa7311692ab | -7.27768 | -46.79425 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b456cf21-2cc4-30a0-b313-50457c825756 | -7.90181 | -45.45954 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba588db0-0ab0-36a3-b39e-7504859eb0a2 | -6.16783 | -52.92059 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78a2ea0-34d2-31e5-86ee-77315b161400 | -5.36654 | -46.2235 | 2026-09-29 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 431ad65f-c41b-3fb6-b2b8-25bb85ff2901 | -8.36446 | -45.48736 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df0be8f0-793a-3705-bafc-23d999ae76ef | -9.05116 | -45.00182 | 2026-09-29 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b19e65-ab59-30fe-816e-caa3ff4bb740 | -5.42697 | -43.44946 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10941378-5dc0-3142-9b26-53aee7fe301d | -5.48486 | -45.12893 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feee4b46-abd4-3873-af4a-dd1612ce6ce2 | -7.52303 | -45.08453 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b90aa1ff-2d5e-3faa-b148-9881b42a07aa | -4.36158 | -47.77032 | 2026-09-29 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 12c088b6-59ac-3d9b-985d-1e3d26032d18 | -8.21813 | -45.4606 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08d58fa8-b9cd-33ce-a750-716d6a5c23bd | -3.41984 | -43.16407 | 2026-09-29 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fac64e1f-f33c-3d9d-83d5-3b081b98f881 | -6.73946 | -44.83739 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b117d8c4-1b9b-3fb1-b286-7b5c649f6094 | -4.66491 | -49.23235 | 2026-09-29 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d18cd879-62b6-341f-aacf-9471efd80dea | -7.67738 | -44.88728 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22adb8a3-a001-3850-808b-e62cdc6977b9 | -6.38202 | -46.50513 | 2026-09-29 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7cd424c-6310-30d5-9fc1-b4967a565ca8 | -5.43027 | -43.44997 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1692a605-20ec-3b95-b603-55ae9fb11b97 | -8.97972 | -44.14265 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7efee00-ba05-3fda-b25a-be286431a872 | -2.29173 | -48.5774 | 2026-09-29 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49130468-088a-3076-8575-e3e8998dc43e | -7.46514 | -46.68567 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa2faa25-afab-3398-ba66-1fecdda71ad2 | -7.53406 | -45.88745 | 2026-09-29 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc9321c5-2465-38f5-82dc-2f8fd3f85707 | -6.91373 | -45.59446 | 2026-09-29 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef6815e8-e703-3158-b68a-01c70ea8cf97 | -7.99484 | -43.25743 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 619f276c-cd0b-3748-b8f7-0c5347eb794f | -5.12391 | -47.76285 | 2026-09-29 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bceb8525-22cc-37a7-bc27-175653c3510f | -7.47694 | -45.8082 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f5f9f28-626f-39cd-8ba1-744e67479a65 | -4.361 | -47.77378 | 2026-09-29 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 00893ce9-5804-3660-8fe2-ecce67cfe7cc | -7.39356 | -46.4193 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7e044f5-db68-36ad-8558-9437389949d0 | -7.69607 | -48.86069 | 2026-09-29 04:14:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3de1b37-2c52-372e-8024-13e82a84229b | -9.77154 | -36.98265 | 2026-09-29 04:14:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a3fc0b6d-447a-396f-9a0d-71182aa41d4c | -7.43301 | -46.87888 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 220141de-7be2-334a-b08a-22951cb6d2d7 | -7.50806 | -44.56157 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0370bf8c-f79b-3bb9-96e7-d2ba6942975a | -4.82275 | -45.63983 | 2026-09-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c747f2b6-e41c-3d84-8352-dc073fd2433b | -5.73457 | -45.06039 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a14ada1f-fdca-31e0-b25c-5c9aea35b740 | -7.07509 | -41.74098 | 2026-09-29 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1598e1d-044c-380e-94ba-bdbf06d953f6 | -4.66562 | -49.22808 | 2026-09-29 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 468264de-80dd-3667-aabc-9c969e3125a3 | -7.07059 | -41.74779 | 2026-09-29 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f772ede4-e153-301e-9b73-e68f7ff783e7 | -7.49918 | -44.55297 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79d92d34-b3d4-3b38-9c59-0433b183c5ef | -7.47978 | -45.81264 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fb8b64a-07b4-370e-ac30-4a821c96eb75 | -7.95692 | -49.57568 | 2026-09-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7afae18b-4922-3854-beb7-214e3fc202d7 | -8.98193 | -44.15012 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e446be59-3dfe-35fe-bebe-a5c0028fa3b9 | -7.61962 | -47.83081 | 2026-09-29 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aef1bf8-ff01-3031-9c06-a2f2e5e01464 | -7.37912 | -42.13544 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ef452596-9aa9-346d-bf6d-190fbc61359a | -7.47349 | -45.80764 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 088a1768-2531-3010-8422-31d903be4cb2 | -7.83328 | -45.81686 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28117a74-4649-39a4-a1d5-bf0387e52473 | -8.54617 | -47.84773 | 2026-09-29 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7036ab32-4bd0-3de1-98f1-3925e2498f3a | -5.74024 | -45.17964 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6f805fa9-02d6-3f2f-ae0e-998161ac2a1a | -6.7019 | -45.68922 | 2026-09-29 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a92f0b6b-6ea4-3a99-ae47-ad12dbd75043 | -5.74414 | -45.17674 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12d2c35b-aa2f-3cf8-b986-d5dd40db19e5 | -7.24739 | -45.26506 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70ac7e30-1205-3a00-ae97-355c574720ff | -6.32149 | -52.62358 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 38e095a9-4f1c-3658-923c-53eceb6e664e | -6.24559 | -41.58968 | 2026-09-29 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45cbee7c-6334-3c03-95c0-dc3c18cf08aa | -8.73049 | -44.92097 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
