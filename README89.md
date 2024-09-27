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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc8895d-562c-3355-866d-8160e931c035 | -9.935 | -47.78228 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbccba45-84a2-3914-b7d9-0b74e62e0b47 | -9.93321 | -47.78228 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96f2f895-6d54-343b-83d6-31e789c5bc14 | -9.92974 | -47.78172 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ca8a53-71bf-3163-8294-2ac703e7a3cc | -9.39412 | -48.32898 | 2024-09-27 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 070cbeb0-9ec9-32e5-b60d-9b0b62f49e78 | -9.39073 | -48.32844 | 2024-09-27 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8724bb99-f3ca-34f7-b9b2-ee5e1dfdf726 | -10.71496 | -48.75529 | 2024-09-27 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f963ba92-36af-35f2-baa4-dd8569999a38 | -10.71158 | -48.75474 | 2024-09-27 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34aeb821-4e97-3e41-a537-c84757f188ce | -10.71103 | -48.7584 | 2024-09-27 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67398f33-20e8-33f1-8675-63aeb03100b3 | -10.70832 | -48.569 | 2024-09-27 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e99a47fe-d1c4-35ee-a516-7858990c86e1 | -10.70492 | -48.56847 | 2024-09-27 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85176c4c-8c85-341e-9f24-8c6625b31762 | -10.70482 | -48.75364 | 2024-09-27 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b82742d1-0e1b-324e-8852-29ea6c175531 | -11.69926 | -47.83719 | 2024-09-27 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a0f80a6-89cd-3d4c-8bcb-4527c1f71e2d | -11.68455 | -47.83911 | 2024-09-27 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a13404ea-4e04-3684-90bc-3f128777b3ef | -12.01499 | -49.13763 | 2024-09-27 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf4fc8a7-f8ff-398d-b497-54f81cacf41d | -13.47153 | -48.57779 | 2024-09-27 04:40:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2daa9fe2-c087-355e-822b-4f0954d3bd06 | -13.46749 | -48.58108 | 2024-09-27 04:40:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6728e166-32dd-36ec-985a-fc76e222c6f7 | -13.46402 | -48.58052 | 2024-09-27 04:40:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a7fe499-5e90-3a6c-98a0-8b6526e0afd3 | -13.15666 | -48.52804 | 2024-09-27 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 648c72a3-b219-365e-bf5a-d4f9cc59fb6e | -12.49548 | -48.61602 | 2024-09-27 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 022b8351-31d6-3d1c-a602-c1d609fba2de | -12.49261 | -48.61166 | 2024-09-27 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fcbb60a-7502-36c7-be28-16fdc356fb05 | -12.66831 | -48.06155 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c425447f-0034-373f-9672-8643808fc313 | -12.66478 | -48.06101 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7104959f-5369-36d4-8067-2061747485d1 | -12.62025 | -48.2916 | 2024-09-27 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62320593-feeb-3835-a061-f2e1a428d2ba | -12.47644 | -47.96378 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dee8f11c-ce3d-3b2f-b23a-017e4b8f75c3 | -12.4723 | -47.96732 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 133d48b5-e362-3e9a-b1c0-34dd20e11c0f | -12.46876 | -47.96678 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdd23fbd-f57b-3281-aa77-69be28bf89ba | -12.46816 | -47.97086 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaf4d32f-c5a2-3756-a768-32b9d8fd0871 | -12.46462 | -47.97033 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1ade5a8-5ce5-3f1c-9493-71810aab1f2b | -12.46168 | -47.96572 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e108555-086f-3657-84c1-1513d9e65754 | -12.46109 | -47.9698 | 2024-09-27 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 046fa4cf-bca3-374f-9d03-93fa3d4b3b3d | -6.00802 | -49.3317 | 2024-09-27 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e171d738-a333-3a7a-8ad1-e0e04585c770 | -6.00747 | -49.33515 | 2024-09-27 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdbd660e-494c-3ad6-ba7c-88e9bf9a8518 | -6.00472 | -49.33119 | 2024-09-27 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 463f7e03-6685-3f36-8483-80a84c4cb638 | -6.00418 | -49.33463 | 2024-09-27 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c77bec64-5848-3190-b045-c7eb0b97aeaa | -5.99393 | -49.24473 | 2024-09-27 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e472754-554a-393a-b946-37f9f14b908f | -5.99117 | -49.24077 | 2024-09-27 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c0ed570-5acf-34d5-a18c-a73ef8f2d651 | -7.59057 | -49.19705 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6158d14-2abe-3132-949b-a019611f46df | -7.58726 | -49.19656 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf5a84fb-09f4-31f2-858a-ce624b604dde | -7.58342 | -49.19949 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e5c91ee-6f67-3154-b1c3-4d304f8f940d | -7.57957 | -49.20244 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edbaba70-c087-3f67-b594-de909f2612b8 | -7.57735 | -49.19498 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c5adb3b-ce9e-3df2-9eff-86a3cb36ca03 | -7.57573 | -49.20538 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 217387b5-0f78-3f93-a8e2-472062c3a41f | -7.57404 | -49.19445 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 604b41aa-f4fe-3669-8459-a0a76c61ffd4 | -7.57074 | -49.19393 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0772293f-2fb6-336c-a697-36fab93aae3c | -7.5702 | -49.1974 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35f10b90-10b5-39f5-983f-1a5b9116877c | -7.56966 | -49.20087 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e3395b9-b486-3da7-92b3-c5d0a96e3450 | -7.56797 | -49.18995 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14af78bf-5b0b-3291-ae04-3787a080a6bb | -7.56743 | -49.19341 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50afac07-9d43-3def-88f9-612509ea07ed | -7.56689 | -49.19688 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0c28bb76-7306-3151-9647-211c4d286e01 | -7.56359 | -49.19637 | 2024-09-27 04:40:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d0a34ee-9746-3b35-a02d-d16d92b43c35 | -7.89515 | -50.01126 | 2024-09-27 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3ff3596-9efc-354f-8448-71e7d52c85f1 | -8.66746 | -49.42426 | 2024-09-27 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f9b334e-b0f4-3173-92b3-17120d289061 | -10.74968 | -49.85922 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa77967c-dea0-3fa8-8cfc-4443882092b5 | -10.74637 | -49.8587 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f23f3533-fcea-336a-8d73-827da1837452 | -10.72656 | -49.87712 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3341df47-3111-3a97-b3b5-e05d4cc317be | -10.72265 | -49.21688 | 2024-09-27 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2add7104-cb9a-39fa-8095-271249dd1fa8 | -10.71931 | -49.21637 | 2024-09-27 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5261097-f1bd-3dfa-8762-fcd096eebe37 | -10.64087 | -49.90311 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d711ecd-4cdf-3ea5-89d8-dfd91385aa0c | -10.64032 | -49.90661 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caf6b081-32bf-384f-9bc7-4c582a3069ea | -10.63756 | -49.90258 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7e6078a0-732a-3ff5-90db-fba12850f146 | -10.63702 | -49.90609 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| abced960-bfda-3206-89a9-44c158c3c86f | -10.63647 | -49.90959 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d9f3dc7-a253-3a2c-ac53-84b93688b02c | -10.63371 | -49.90556 | 2024-09-27 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 63607049-3627-3c92-b808-c5bb65d1694d | -10.48026 | -50.25622 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc6f3acc-c59e-3a41-8ed8-942a7a7ab8bd | -9.97732 | -50.16479 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48d538a9-480a-3bd2-8017-ce20e615fd56 | -9.97347 | -50.16775 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 391db5cf-ec3e-33fe-93e9-3b7b7e3e717f | -9.90022 | -50.13417 | 2024-09-27 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dae27f79-ab19-37c1-a2e8-be8365dc3782 | -9.60695 | -50.14098 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a448420-2957-3e45-b7fc-a4dd26c733a1 | -9.60144 | -50.13298 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e37eddbb-45eb-3566-8c72-e7390cc86929 | -9.60089 | -50.13646 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c11144f-093e-3f74-9dfb-170ce365bff7 | -9.60035 | -50.13992 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c325bc5-7a07-394d-a56f-9e481ce60519 | -9.5998 | -50.1434 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa700dd0-1f25-3df7-af7a-c7579f6af7a4 | -9.59923 | -50.12551 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41a67261-8476-34d3-9d6f-e6d456636409 | -9.59814 | -50.13245 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81c6c412-d41a-3d93-8fb0-cf707cd3150a | -9.59759 | -50.13593 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e33a1524-3d14-36dd-9ccb-13615f7d06db | -9.59705 | -50.1394 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d1e195-e807-33f8-8b06-0a80f232d039 | -9.5965 | -50.14288 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ee96e04-824a-3302-beba-0dcc2bb33b8c | -9.59593 | -50.12498 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30f7f7ab-e481-3b0c-835c-d48c2f4d6f06 | -9.59484 | -50.13193 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56414c34-be61-3884-a4ef-3f0740d0f9ea | -9.59429 | -50.1354 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14441216-3e7b-3ea2-b2ea-8c4304b77491 | -9.59375 | -50.13887 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc7ea470-fe85-3cf0-a82b-5ccf7f71ccf4 | -9.59263 | -50.12446 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b829c5-19fe-30f4-89e1-3ccddc6e3ff3 | -9.59208 | -50.12793 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9f4b4ea-67e6-314f-932e-db22d5e62528 | -9.59154 | -50.1314 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa571dd3-531d-394b-9ff4-68a4d435321e | -9.59099 | -50.13488 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 843915a3-1dcf-3f28-86d8-a033d38e9754 | -9.59045 | -50.13835 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8642e6db-d977-3322-bb7a-47d490be7d4d | -9.58878 | -50.12741 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d0b14c5-e188-37ca-8d21-4dd48f805171 | -9.58824 | -50.13088 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d7a53a-74f8-36cd-ac44-b5af40593ebd | -9.58769 | -50.13435 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4f0f0f1-ed7f-3e6b-933e-6e5dcba22d2f | -9.58715 | -50.13783 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db058ee8-7dc8-3b36-a27f-460427434711 | -9.58494 | -50.13036 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92b6811c-6d3d-3ade-baac-69a6d31e7ab5 | -9.58439 | -50.13383 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4231630a-008e-3355-a0b2-5f589447a112 | -9.56201 | -50.18657 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 179be3d2-4360-3b5e-a257-86a7b2671da0 | -9.56146 | -50.19004 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a0c1402-378f-3c7d-b80f-45f026145b27 | -9.56091 | -50.19352 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7da8b8f4-7489-32f9-8a88-41191ee2bd96 | -9.55871 | -50.18604 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2483e9f8-4fa9-3f96-9a5a-eef219f7bb62 | -9.55598 | -50.20342 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f8ae5e7-44cc-30fd-bcc2-5b68f63611e0 | -9.55543 | -50.20689 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 191618a7-5576-30bd-9251-113ecb214ae8 | -9.55489 | -50.21037 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec36aa04-4b62-3642-8338-07b60ce9156d | -9.55159 | -50.20984 | 2024-09-27 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README90.md)
