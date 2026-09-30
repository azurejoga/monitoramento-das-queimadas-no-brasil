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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e4c9740-014e-3ad9-9930-3983b84e5701 | -5.73189 | -45.17252 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aabe1d7e-b19c-39f7-9f80-92c00fdf18eb | -6.85954 | -40.93921 | 2026-09-30 03:55:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbbde427-5a7c-3687-a5ae-912fbbc720a1 | -7.02396 | -44.62086 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edad491c-082a-3412-a910-57f5efbc0c11 | -4.80908 | -45.64711 | 2026-09-30 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 632499b6-e981-36c0-b3ab-4c9310006a49 | -10.96062 | -43.88892 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bb88766-d114-3199-aab9-30a9f0540530 | -9.80912 | -48.21539 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac51b871-bb19-36de-aa31-6829c83506f1 | -12.00078 | -44.92521 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d335756e-a458-3d62-a30f-3db4f1b856ea | -11.62303 | -43.5338 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01adae8b-a390-3d0e-9630-e75d39b7dfe7 | -5.02632 | -43.57172 | 2026-09-30 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf299fb7-6895-3dca-81e5-5a57f14af186 | -9.81917 | -48.21115 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54b32bd2-721e-3b70-ba36-aec7c7a37edc | -9.76151 | -44.82013 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7db4fd11-427d-3fa0-982d-74f4264b224b | -11.17631 | -44.82835 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6009fc2d-3d68-3754-a43c-44394f4fe9e9 | -9.52507 | -46.35001 | 2026-09-30 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8bf6832-8578-3091-9df8-f1d6df8ab954 | -11.26725 | -43.52415 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60f2f2eb-3c5f-3cfc-979a-0bb3224f4186 | -10.71259 | -47.83282 | 2026-09-30 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2eb876ac-9c92-3860-97fa-72dd82004489 | -9.65694 | -40.58654 | 2026-09-30 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a57b267e-7bae-376c-9675-947f988b3183 | -5.34193 | -46.1936 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 421c0fb6-ca88-3b05-aea4-11071c5ab3be | -4.45438 | -47.92307 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4089b1af-edc5-3c46-b13c-a005e1ffce85 | -9.75734 | -46.24113 | 2026-09-30 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e82c013-2038-3d15-ad40-f5b694d1519a | -7.85256 | -45.82119 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e786b1b-881b-3cd6-948b-472862efe591 | -9.07328 | -49.8716 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 716e6f21-6ceb-3497-8ce0-c1db3f4cdf6e | -7.81437 | -45.8212 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 3b563377-8e3c-3e8d-aedf-81ded981e138 | -6.28597 | -43.63973 | 2026-09-30 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b70bf91-7739-3d8e-811c-0912236c6e59 | -4.46142 | -47.92076 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1d4fbda8-6dac-3d9a-9691-c0c1350bbedf | -10.90374 | -43.85379 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c25419f4-6203-3881-92c3-51c21f5f2dec | -6.29571 | -43.65596 | 2026-09-30 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ba02ebe4-f249-311a-8916-9723b47e4770 | -10.51638 | -45.37673 | 2026-09-30 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c501989a-5da2-338d-b8db-9b19644b7947 | -9.04326 | -47.32792 | 2026-09-30 03:55:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e509581-2a1d-34a7-9a63-edbde8c33e44 | -4.34968 | -48.97067 | 2026-09-30 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e18029d0-f6ed-3455-b9fb-df742979e334 | -9.12078 | -40.64095 | 2026-09-30 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f41947ae-c7b0-3250-94e9-eb1afe792f3e | -6.07197 | -44.8725 | 2026-09-30 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af677335-1aca-34c4-9887-4110ae2e6685 | -10.71864 | -44.42794 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a555715c-c761-390e-a5e3-df4d071f73b5 | -9.44612 | -47.69982 | 2026-09-30 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f2ecd29-c171-3c32-906d-b5f269c4b477 | -9.81492 | -48.21301 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3a6c66f-705a-39fd-8f9f-ee288a5c02f0 | -5.73318 | -45.05572 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 744faeca-f665-343e-83bd-3823166a2f1b | -10.71393 | -50.84122 | 2026-09-30 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 618b36fc-28c3-3faf-bab7-f9e735fa80f9 | -7.81634 | -45.9196 | 2026-09-30 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 832c5029-4688-369e-bb21-6dc880d9edce | -9.77458 | -44.8184 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8ae5484-b76d-3fc8-8bad-4d161dcdae81 | -11.41482 | -43.42131 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6905fb5c-d609-3717-9f96-e67d39349fde | -6.29631 | -43.65237 | 2026-09-30 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2387e3d1-28fa-3f49-ac87-8f79329e666f | -7.53183 | -44.54603 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b01247-5345-3eb2-8485-acc03766f575 | -6.39897 | -44.83922 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eebd93fa-3008-316c-914a-40b506e5b3d5 | -11.67235 | -44.51279 | 2026-09-30 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61f21f5f-c156-3a58-9c6b-3caecdf913bf | -4.36111 | -47.77557 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84586735-6dd2-33eb-994b-37213f299c1a | -11.16815 | -44.7749 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d86bd0c7-f0fe-38a6-a8fe-1df7eb41de66 | -10.7076 | -47.83203 | 2026-09-30 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74c9b6e2-963f-3cc5-8011-b9b8e95844a9 | -9.80816 | -48.21288 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa665204-43c0-34ec-93ad-dc2a96f2edb3 | -7.48951 | -45.79073 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bc6c4c0-2488-35b1-8cba-896eaf2e528a | -9.77045 | -44.81772 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 696d8391-d8f9-330a-b53d-c790b110a93d | -8.27993 | -50.26703 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 425e2f9f-8c4f-3a19-86d8-c286e3589620 | -10.90921 | -43.85147 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cca526b-fbc2-3c81-a897-4e352913c2ab | -5.82023 | -46.21284 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75dfd274-548a-3eed-9451-424729372089 | -11.6362 | -43.53498 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69b75476-8d48-3242-bd0c-04029010404a | -8.21434 | -45.4687 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fbcaa15-ad6f-3b7b-87ca-232f754bded8 | -11.16412 | -44.7742 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6befd10d-b186-31a8-bf6f-fc45940998db | -10.13641 | -45.13302 | 2026-09-30 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cc69b49-9789-3d2c-8bec-6ceadf451ce7 | -10.73447 | -50.50288 | 2026-09-30 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1897b120-566d-31ba-be5f-6cae45b03852 | -3.37469 | -50.95721 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e411f003-b7fe-37a7-8b6a-330768014991 | -8.21509 | -45.46431 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de43d243-f9a1-3912-98a2-3ae69ae5c838 | -7.3853 | -47.01717 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af1664cb-55e7-33e4-be6e-a5270f674bf5 | -9.78967 | -48.22634 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd250943-76f0-3e42-8926-4db1617f1e14 | -10.77498 | -47.72328 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c97baf6-e6b9-3286-9668-d98a617b794c | -11.43919 | -43.43468 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec5d7264-f8d0-3b9e-a10c-9e7f8cdac6c7 | -10.71544 | -44.42287 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eeda5c98-02fa-3739-9379-553c61019141 | -7.47489 | -45.79351 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ee3d05a-6802-3000-b485-8fe1c5a746c8 | -5.97711 | -46.61015 | 2026-09-30 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de4e5f21-3831-3d38-b8da-d4e21bfec6ef | -11.17008 | -44.81209 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1f3d303e-93cf-3fba-a944-0944a4f62faa | -5.09826 | -46.03962 | 2026-09-30 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b816490c-7cfe-3454-b6cf-bf85fb775566 | -6.16873 | -44.6189 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48f13e43-bd0e-32b5-89c7-66ade678c47a | -8.55903 | -47.78656 | 2026-09-30 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a265891e-8fe1-348a-b24c-5413d192f1e6 | -5.66819 | -43.55753 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dac659d-ceb8-3772-9110-06cb2821fcc0 | -10.29098 | -44.61967 | 2026-09-30 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ee4a875-85b3-3884-8611-54ca23b7f9ff | -4.94903 | -49.4177 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22b27a52-1ee4-32c4-a97c-574cd2427720 | -3.37421 | -50.95289 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 424b41f8-ce3b-3caf-861e-ec9793b97ae6 | -7.50287 | -45.82294 | 2026-09-30 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f37eb904-135d-3c9a-a467-2385540af0a0 | -6.70939 | -45.63595 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f9d6aad-fdbe-326a-9633-d1eb2da8c03c | -7.51563 | -44.53946 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a62410d-9cbf-3bce-b5d6-2b92017573e0 | -8.05137 | -45.46625 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff94509f-f6e6-33d6-9d95-72c0e157a24e | -5.5581 | -45.33633 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3420d8a-9f0a-3797-9f68-b3caf08f0ddf | -8.36771 | -45.39109 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e24f3aee-b1af-38a1-8fe9-0c147723c156 | -6.75034 | -44.84795 | 2026-09-30 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ac2b09a-91ec-390a-9101-ee1c03eba8cf | -11.4167 | -43.41879 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 98139073-5b54-364e-bebb-99ec7bc1d6b6 | -11.66842 | -44.51211 | 2026-09-30 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2f424a2-d78a-37f3-819a-96414a818239 | -4.44554 | -46.2844 | 2026-09-30 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72847078-d2cb-34b6-b7d0-f4e91214f7f7 | -9.93109 | -50.15637 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3257aec2-3351-3127-9190-c1ffbc3f177f | -11.41966 | -43.42389 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b87b951e-a7a2-3f6c-a568-a6f6bf844ef0 | -7.53248 | -44.54564 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a18dc37-2774-3aa3-a570-0d3c8c0e56d2 | -9.82178 | -48.20496 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7cd9f27-1ccb-3ef5-8143-658cc1a5ad5d | -10.77364 | -47.72169 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d1075715-3d1b-32f8-b7e4-d8399b8073b3 | -3.38148 | -50.9585 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 069574cb-e9c7-366e-ab8a-aef403457081 | -9.81339 | -48.21359 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3ad5cea-b3e7-356c-b9a0-422d2b1fed07 | -7.20565 | -40.11892 | 2026-09-30 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 92ff7c98-345a-3b9c-8c67-50965c0396b4 | -3.3753 | -50.94657 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 45804c8e-e148-379b-9ac2-38c1710b82ec | -3.37638 | -50.94024 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5b8dcced-3719-3cce-b3d2-f4446a11731e | -12.33647 | -39.75645 | 2026-09-30 03:55:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6988f7b1-bcc0-3ca8-aa93-f09696c7331b | -9.14863 | -46.76782 | 2026-09-30 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 273479bc-08f7-34f7-88c6-f106e801e4ad | -7.64123 | -45.51158 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c38a4f7-5f3f-3a87-ad19-5e70174c4a46 | -11.41823 | -43.46793 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e611b921-a24e-305f-b9e4-a8792e54633a | -8.25044 | -45.44356 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bafa66e0-4981-388f-8f04-9eae15eacb53 | -6.39826 | -44.83934 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README16.md)
