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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 266797a0-c494-3ef3-a35e-851eeccbcfe7 | -8.68762 | -49.23983 | 2026-07-28 04:32:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6327cdaf-f76e-318c-a1ae-1d71c87925fa | -12.04248 | -47.80289 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6f39c3d-824a-3a8d-b90e-525aff95d8be | -10.93675 | -43.05495 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f49f5bae-bebe-34e2-aefb-d39528b16bcf | -11.97486 | -45.54781 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a55d458-b5d6-3f97-ae04-cf48ec5fc0f2 | -7.24392 | -43.1417 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d2b9027d-ad1f-3d14-bf9a-de49eeafd439 | -12.33881 | -48.23082 | 2026-07-28 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f09c1cc-bae4-3e76-b94c-7f4db355425a | -6.87367 | -46.00042 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 783cef6a-de5f-3fb4-a047-5bf7fb55dec0 | -7.00576 | -45.42538 | 2026-07-28 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 877ae3d1-fd2f-3d0e-91ec-f7728cfa187d | -11.97541 | -45.54426 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caa38404-6628-3df9-b094-a8e146071871 | -12.33944 | -48.227 | 2026-07-28 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84881872-ea52-3336-8b32-1c097acbc513 | -7.72348 | -46.50329 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7704944c-590d-3542-8441-b98a3386f367 | -13.29707 | -45.11238 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98222e8f-b2aa-381c-b734-95264b21c4cc | -10.7388 | -49.62842 | 2026-07-28 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f971570-873d-3f9a-88a5-277ddd350d45 | -11.98485 | -45.54941 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e527348-34de-398b-874e-58894fee126c | -13.62045 | -43.71858 | 2026-07-28 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1250fef-911c-3559-a5d3-137ded536750 | -12.49699 | -43.77169 | 2026-07-28 04:32:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 046f1a40-a1ef-3819-a3b8-bab126dd18ef | -7.3682 | -48.14625 | 2026-07-28 04:32:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 892b810d-f0c1-3923-8a45-981d5b1899c1 | -12.46104 | -50.54902 | 2026-07-28 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e023933-073b-3846-bca8-c9b7d36e04fa | -11.45022 | -47.53465 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b571253d-52a9-3f14-8eff-054dde67c40c | -13.2982 | -45.10503 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d6f8bfd-b842-3f6c-b3d0-eadc3366b16c | -11.38065 | -48.82361 | 2026-07-28 04:32:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe568e2-5497-38c4-bfd2-b78705faa8ec | -11.98207 | -45.54533 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d31b7c7-807a-3232-8b4e-aeaaccf21a6d | -10.94091 | -43.05141 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| be8926ab-b9e7-375d-852d-557cf1d17717 | -9.66229 | -40.59901 | 2026-07-28 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 25bfa2f1-a781-386b-a35c-20c79d0666f7 | -12.45511 | -46.51207 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 692bd977-cf46-312c-9dc7-97ff9d2f566a | -9.65826 | -40.59843 | 2026-07-28 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bbf2ced9-e935-3cd1-8557-d2aad492f7d7 | -6.8731 | -46.00396 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4bd0673e-ea53-3286-8300-74629ccd9017 | -11.78134 | -47.08671 | 2026-07-28 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 150383ce-dfb7-3457-b11a-56a053ef2cc1 | -7.24964 | -43.12727 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f94ff746-42e8-35e6-aa27-a66e378dd1c8 | -6.86975 | -46.00343 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1bbeaa9-f9f9-3179-91f6-8a6e06654bf5 | -12.84697 | -44.38674 | 2026-07-28 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 64796fb3-aff1-378e-83f9-9a5f9e47a85e | -13.4526 | -44.04436 | 2026-07-28 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42cdf656-c855-3275-bf04-d3a08ddc111f | -12.45454 | -46.51561 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e5e8fb5-fc73-3a4d-9ab6-e9f5256f5a2b | -7.83284 | -47.09919 | 2026-07-28 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53247a6a-ac80-3540-a13c-0ff5bca59ae6 | -7.87513 | -46.90443 | 2026-07-28 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38b7426a-23dc-3e2e-94c6-9514d0d85708 | -10.7384 | -49.62609 | 2026-07-28 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6354e643-fd30-3313-901d-31c5bfd9f38a | -6.8664 | -46.00288 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 939c980a-863f-3184-80c0-3c87724ff3ba | -9.36337 | -44.73101 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5ef4f96-6a4f-3984-8b6d-aac6943f3d22 | -11.78192 | -47.08313 | 2026-07-28 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 452f21f8-d554-3606-bfc1-ef4fdda3c621 | -13.30101 | -45.10923 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 732f9a41-ec19-3abb-b460-1a5d89a3af90 | -9.61178 | -47.7649 | 2026-07-28 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27552ff7-d3d6-356c-85ea-0cdaea799c9f | -12.84983 | -44.39108 | 2026-07-28 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5cf3edb0-0956-3107-895f-6571ca09c8c3 | -9.33612 | -47.90594 | 2026-07-28 04:32:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36f4579e-e63f-3fed-9375-1c2c8c9068b5 | -12.84926 | -44.39487 | 2026-07-28 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25591528-aec4-3a79-b670-e094c726b0c3 | -9.10546 | -49.65558 | 2026-07-28 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 922d1a75-aee9-3e39-8eb7-be83aa3a75db | -10.94684 | -43.06067 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a7052522-b44d-3e1e-afc0-7e30637bb8cf | -12.22199 | -46.61551 | 2026-07-28 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a26327e-b45e-3a70-af78-a5a9b1c69e4c | -10.38281 | -49.57897 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 96bb2e64-84e1-3b1a-9482-4125efc6e508 | -7.00963 | -45.42244 | 2026-07-28 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 300d4ca6-a2c9-3ece-a44a-ab4954f83fa2 | -7.62375 | -38.79854 | 2026-07-28 04:32:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73b091f1-b95c-302d-92db-4e9c9b93eed8 | -7.46115 | -49.73223 | 2026-07-28 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 774298f4-4270-34cd-b67d-ba69260a70da | -9.36392 | -44.72747 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aebeff24-469f-3453-9b32-31824c211cb9 | -13.30325 | -45.1171 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e43bca5f-b253-3f7d-acef-f66106590cdb | -10.72789 | -44.03653 | 2026-07-28 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48c6871a-2a6b-3b53-b2a4-f5871e2bf114 | -11.50106 | -47.54284 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27c66248-1865-38da-910a-519317d4b901 | -7.92491 | -55.03971 | 2026-07-28 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3fe8774-e5cb-35ae-8ec4-21cc7d2389cb | -9.36586 | -44.72752 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 322fb2af-1d0a-3642-b06a-b2fde9d79908 | -11.9854 | -45.54587 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b83593a6-c01a-35cc-8785-1790ba9a8977 | -8.68387 | -49.2392 | 2026-07-28 04:32:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 002977ad-11b8-36f9-9eb1-136347ac99e0 | -11.89148 | -43.82674 | 2026-07-28 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7389ff2e-3e84-380b-9414-b1eac97d7d84 | -13.29596 | -45.09715 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 0683745b-3c6c-3dc5-bf1c-6a24260025da | -11.8909 | -43.83063 | 2026-07-28 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b42c26a-ddee-3d55-9024-181f80700fed | -7.40833 | -46.82959 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54f7fd09-e891-3fce-89c3-ba8896b0c27c | -10.26466 | -49.73044 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbf670b2-bbd7-32be-8620-88aa77398843 | -6.86918 | -46.00696 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b12a40a8-c649-305f-a78e-a423b388abe3 | -12.84755 | -44.38295 | 2026-07-28 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a650e193-4e4e-3494-8864-5a6b410090e5 | -6.83818 | -42.88609 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9c92b5ef-d856-31b2-b9f8-cbbb12b92630 | -13.30044 | -45.1129 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5511d07d-1e58-309f-8ebe-b0b4d396ce36 | -7.72289 | -46.5069 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42946d75-a81f-3aa3-b5e2-d42135b7cd98 | -10.37966 | -45.13083 | 2026-07-28 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 807f8c2d-2e26-3177-8837-b02c00850c1e | -6.83185 | -42.88129 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 75f70f2a-406f-3801-9750-6b2728c615d2 | -6.87702 | -46.00095 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a5f0a84-8035-3050-b004-32e6edd33042 | -13.30382 | -45.11343 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96314c2f-5d21-3f16-8661-96f7fc171842 | -12.45786 | -46.51616 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f33d360f-636b-35cf-b88c-838dface24ab | -10.75012 | -42.08981 | 2026-07-28 04:32:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 50048f80-fcea-307e-bd0c-e5c93fea3320 | -7.24049 | -43.14117 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6b598b3-c21d-3655-8672-6cd32a580656 | -7.89904 | -48.27966 | 2026-07-28 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5c0e2d8-53c1-333f-a663-8dcc4a3dd36a | -7.0052 | -45.42886 | 2026-07-28 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4dff120-a291-3b77-ac40-e52086be4f37 | -7.41173 | -46.83017 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bdb2690-fe1d-3b2e-939a-7d265cab4134 | -12.49408 | -43.76719 | 2026-07-28 04:32:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 53c73f36-b786-3f78-9c64-5f9c4035806c | -6.54807 | -42.50357 | 2026-07-28 04:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 04eb924a-3a56-3ebf-a92d-5a86eefb9984 | -16.63516 | -46.86625 | 2026-07-28 04:34:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b791913c-fb3d-3392-847b-e2965e442620 | -18.36278 | -50.67776 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4febeb01-4cea-3c10-8b68-975eb88626e3 | -15.77063 | -48.3928 | 2026-07-28 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da28edae-801b-3dc6-97f4-7dffabba4462 | -17.16418 | -46.83522 | 2026-07-28 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8421298-a0a0-3256-a8b9-55363cdd4d19 | -18.37497 | -50.67132 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 12720f9d-8d39-3b0d-b0b9-ef3441f9a45d | -15.76389 | -48.39159 | 2026-07-28 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7823ebb-2bad-3811-a557-eddb3263a0de | -14.41356 | -52.11789 | 2026-07-28 04:34:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 74affc99-424a-3942-a7ad-9ef174692529 | -15.76787 | -48.38853 | 2026-07-28 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5df03d1-0909-33c7-8dfd-944973db7623 | -18.36934 | -50.6615 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 52ba8344-5dc3-3652-98a4-3b2197725b22 | -13.35447 | -54.28865 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fdac981-dadb-3195-8c61-ef1a620d5fe0 | -17.40073 | -47.33142 | 2026-07-28 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6d8c77f-8877-3173-84ac-dad2ef0bb2e5 | -17.72536 | -48.6028 | 2026-07-28 04:34:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b26ad694-0056-3713-9c4d-727bd6cf368e | -15.81674 | -41.89864 | 2026-07-28 04:34:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f67d076c-51e8-376d-ba8e-539b70a7041f | -16.86639 | -49.58127 | 2026-07-28 04:34:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6389029f-0e5f-359f-ae1c-b565ddf5df49 | -18.36991 | -50.67911 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 08165ac3-102f-3676-b6b0-dc5bb14583b7 | -18.36817 | -50.65877 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b71ee37b-1f06-3562-bdd7-78a73c48d21d | -12.72987 | -52.05879 | 2026-07-28 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4f7e4745-3545-3cdb-bdfd-b0369e931d6c | -15.24322 | -48.58004 | 2026-07-28 04:34:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c2f22ce-c43b-3344-99b5-b8f404b6106d | -13.98008 | -53.94968 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README15.md)
