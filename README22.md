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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d1c8d5c-1225-38cc-bbab-dcb90f604e94 | -11.22277 | -54.82273 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89d4e004-17be-3f22-bc75-36ffab855102 | -6.62329 | -59.0573 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 471879cd-2ee2-3c49-9e63-7f0bdf70f355 | -6.83593 | -56.44402 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 87950d4f-3cf5-35c6-ade0-51b6744596d6 | -11.80757 | -51.78714 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bdb7882-a49c-3c18-a925-efe35a943568 | -8.54605 | -54.58975 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adfd368c-c865-3a26-9134-f450ff3ae5db | -6.60375 | -58.99929 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da881a8f-bc93-3c80-8158-37e92633bb3d | -11.08135 | -47.2535 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| da35752b-8f21-3f29-abb1-a027df79449b | -8.90349 | -60.55894 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d47e4b2a-23a9-3554-aa52-fbbc4bda6a1f | -6.8683 | -56.42537 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b986874-1064-364c-9ab2-6d0f04261dac | -6.83291 | -56.46217 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37a0ca0e-123a-3381-b071-c0c2f95d3fbd | -6.79553 | -58.78932 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bbcc860-77eb-3ff0-8080-65735dccd618 | -6.60917 | -59.00014 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b20d1c9-5eac-3d4c-95f7-a807a7b9bb45 | -6.71047 | -58.95661 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c862c48b-5581-3843-b699-c1c65de7f87d | -3.74413 | -59.33066 | 2026-08-16 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76fffb89-de66-3c4f-8719-1e66d7a466cf | -12.0318 | -46.44162 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fa36d05f-b1f2-3d7d-940e-3c0303a00afc | -8.54913 | -54.59536 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 500a6f82-8820-3211-a92e-3d6d1dd5673b | -6.4343 | -60.07669 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5678e375-02e0-3ae0-abb5-673c967a3eca | -11.07402 | -47.27842 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17d6eae5-bb96-3b33-bc1c-5fcb33a99186 | -9.0829 | -61.39944 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e29d4f3-0698-3389-9d3e-1d2e5e4dc06e | -6.60149 | -58.99228 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78e011c2-f1bd-3eb7-b6c2-fd10a03984ec | -11.09648 | -47.25168 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf353e42-cf5f-3ce8-b66e-3acfa86f6a5a | -8.43396 | -62.67403 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a56e569d-1941-3c26-835b-1d2d5e08c462 | -8.98155 | -60.5227 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 638a79b8-1ee9-3642-9e01-6b616e919e23 | -6.31119 | -43.62724 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fce53bc1-03f3-3eef-8afd-1df151d4bf74 | -11.62128 | -51.09501 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f54eb41-60d1-34e8-b693-13127ab9f034 | -6.7178 | -58.93092 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e80179a-99b4-3703-93ce-6c24bfb2a700 | -6.60565 | -59.00008 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb1767b2-c4bc-33b2-abbb-e5291c54ae38 | -8.60359 | -54.70444 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d421dcca-5fb7-336e-b771-cbb7b3414ce2 | -8.65629 | -54.72562 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b71366a-0b1f-3481-8c03-1d27dad3441f | -12.23644 | -43.14235 | 2026-08-16 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 16bbd2ae-de56-37d0-900d-78bce4b253b7 | -8.896 | -60.56282 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5c82b807-860d-362d-a5e3-7b94c8cf6228 | -9.084 | -61.40176 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 723bc6fc-d866-3e55-900e-ee31d4faa881 | -6.23682 | -47.7349 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bec130af-3cf3-3f68-bd89-dbfef191d7d4 | -8.96435 | -60.51965 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| af146680-d6f4-391e-9699-fb100c92cd7b | -8.6165 | -54.6755 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c0016a1-1fe1-3dc7-8ced-51d514628496 | -6.59608 | -58.99141 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae061496-ae9b-387e-a3f6-198981d34108 | -6.5565 | -43.111 | 2026-08-16 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d1da25e-656f-3304-8f6f-6568e5479324 | -10.80624 | -50.32756 | 2026-08-16 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7efb2cd4-ea06-3ca7-9555-67a47c27f078 | -6.93569 | -43.63834 | 2026-08-16 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aff5d939-354a-341f-84de-b703bdbbd359 | -7.36491 | -46.81278 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4d64da5-9c37-3f8f-b88f-0f016913c929 | -11.07765 | -47.27898 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e93e2b29-731b-3371-8d68-c8dbba181288 | -6.81625 | -56.45028 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f907008a-7484-3b43-82ed-ecc1a22f98f8 | -9.19702 | -59.66919 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81571c65-5c25-38ae-a455-8ab402f6425a | -10.81834 | -50.31514 | 2026-08-16 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 214afab6-a926-330c-b926-da38434b8ee0 | -6.61157 | -58.98619 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5af3342-d603-3069-9141-1dacebcf9da8 | -8.43285 | -62.67977 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 99f9fa58-fb87-34e7-a97b-85f3862786cc | -7.38906 | -59.99982 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f629541-07c4-34f6-9e41-0a922d433b04 | -11.45915 | -46.61487 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 012bf684-95a8-3973-b86e-ada2d12b3598 | -6.7865 | -55.84567 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57d1ce8c-7f58-3390-86ad-2e2b1b4d16d6 | -8.97008 | -60.52068 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5f7b6784-6548-3ec6-9092-496760d6110e | -11.20915 | -54.81071 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21dfd4f8-1652-3738-a53d-86669337421d | -6.63296 | -56.39703 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1eb9515-3761-31cf-b960-6b735f8afa9f | -6.30928 | -43.6104 | 2026-08-16 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4084374e-4fd6-364c-adc5-d8d4decb0dcc | -8.96209 | -60.53172 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 66681d30-af14-3915-83a1-4d934719f469 | -8.55785 | -50.41837 | 2026-08-16 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c83df2ae-80c7-3b55-a62c-99f6dca71505 | -8.10612 | -51.65581 | 2026-08-16 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b573c71-575c-3966-b2bb-a103c8952a73 | -10.41708 | -47.84106 | 2026-08-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db58c3cf-7e3b-39a3-b944-7051baa5099b | -8.90308 | -60.59232 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 107bab92-fda0-3d4f-ad7b-f702aec21496 | -6.8463 | -56.4449 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7a75e47-dab1-35db-955a-d59b665222da | -6.61419 | -58.9836 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b98d511-5b9c-3682-ac05-1bfa03b0c65b | -6.85934 | -58.97594 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b4b7cdb0-7454-389a-a612-209da533dade | -8.42889 | -62.6749 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 601f78bd-4f82-3615-b55f-8e2e07962fef | -8.65236 | -54.72498 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 466ca459-ee46-3098-ab1a-022521b3ed78 | -7.46447 | -44.87084 | 2026-08-16 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a89d2c47-6c14-3d7e-bb0f-5b01db3b747d | -6.97477 | -56.46457 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce20be27-8a28-3817-addc-efcbd7916d63 | -6.70295 | -58.95265 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b67b60d6-3921-34a9-8682-0b99852b6388 | -8.64234 | -54.71282 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42c21c06-7141-35e4-a34b-5d2fe0f4bb48 | -6.31605 | -43.6238 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c6ace7ba-09ff-3a22-ad1f-992794a76e39 | -6.97777 | -59.01098 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9f21e3b0-d83d-3ea0-a60a-c6e0497f89df | -6.36937 | -58.32318 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b314ea8b-15cc-3361-88ba-a50eb4349da1 | -11.46294 | -46.61544 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b0fa07ea-f29f-3c72-9dd8-c924fcb7dd0c | -11.88465 | -51.94347 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa675129-1937-3070-a886-555da8f51d00 | -11.91151 | -49.33823 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 521a4e13-23e6-38e0-8c81-a46653bbe358 | -11.5074 | -54.6357 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91a564a5-b4e7-3933-9622-a940097a2453 | -8.90039 | -60.57518 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f5bc902f-2145-33eb-a268-5138f7d449a8 | -6.30693 | -43.62662 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 09c9eacc-a861-3cc5-851c-3bc2daaebcd2 | -7.34966 | -59.59705 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0f15dc9-caeb-37f7-b012-5445424dd1ac | -11.90419 | -45.97426 | 2026-08-16 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a43332c-35ef-3763-8ef0-71ca87ec807d | -8.79418 | -47.9274 | 2026-08-16 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9497c9e-6f8b-362d-9148-d1e866db86da | -7.40507 | -41.93193 | 2026-08-16 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ada2219f-1607-37b1-a21f-4499d49b332c | -6.62975 | -59.08387 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9833d006-ab60-322f-a2f4-11b5f1c5d294 | -3.50483 | -58.94962 | 2026-08-16 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ff701a0-10ad-33df-b708-f66026f257e6 | -6.85166 | -58.95695 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ca0df94-62ce-39ed-a905-7fe45bcb8f46 | -6.60435 | -58.99581 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7388de52-7029-3c3b-bf2d-4e530074e48e | -7.4162 | -60.01202 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd7c0f71-b3d6-3596-bd74-4719e008371e | -11.22658 | -54.82339 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b819e2e5-3a1c-37b1-99cb-5b67caea466c | -6.72376 | -58.92841 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8bbef9a-4720-362a-ae56-9d4b06ecc20d | -7.59543 | -60.89178 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b39a4d6c-7d3a-3e92-8db5-7af782c215c3 | -9.1028 | -46.38597 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fa1358a-a68b-3d4f-a4ec-e3bce8d7a854 | -8.98304 | -60.51471 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0c18aea4-9735-334e-8d87-610f2898789a | -6.93197 | -43.63367 | 2026-08-16 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4ad3860-37c9-3872-9e7c-3dd00a51c0f7 | -11.83853 | -51.85108 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1848c4e3-d21f-3883-b345-cf7e30db1042 | -6.61276 | -58.9793 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54400bf0-d4c0-377e-8e4b-c354635702a8 | -10.0781 | -60.49603 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96867ea3-0c4d-3b01-aac0-a8afdf152200 | -6.95493 | -59.29826 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51932cca-db2d-3f13-9a9d-43e398e9ad6b | -6.72429 | -58.94147 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ac06aae-81ef-3c97-9a72-a40824658d90 | -8.96509 | -60.51569 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e8b2af26-46c9-3e34-b62a-ea20ce9ef081 | -6.64919 | -56.4381 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 015aa546-df07-3a5e-add9-c6959903a745 | -6.21982 | -47.7323 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 57045153-b094-3d5d-b1b2-74c62bb3cb94 | -8.64186 | -54.69219 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
