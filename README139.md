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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe3d557b-e60a-30a5-8231-826c2de7e046 | -10.39562 | -61.20053 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 11faeb5f-9282-3a89-ab2b-d5c2cfb825b8 | -14.87869 | -52.62018 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cefde456-57c7-3d85-ac53-08e9e8af5ff3 | -9.42458 | -50.43665 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| b37c4a3c-8087-3945-88e7-65603af9c498 | -10.76072 | -50.63188 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ebd1d568-37a3-382f-be13-df7a40cecf25 | -9.92478 | -60.44096 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| e0bb21fa-d50e-3b0f-917f-69fec8d33363 | -14.71902 | -58.72538 | 2026-08-28 17:45:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 300beb67-f5c2-34f1-b4ca-bbd39f7c8ba2 | -9.11952 | -61.59686 | 2026-08-28 17:45:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5e6725f1-bd22-303d-bc22-566e88256571 | -10.34027 | -50.38483 | 2026-08-28 17:45:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bfd25a7d-44a3-31a6-9b91-6837b38a882b | -10.27817 | -68.8596 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 05f7308d-9312-3d4d-bc02-1f58ea0dadeb | -9.0863 | -50.59772 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ef0f06fc-9ffb-3ff7-bde2-83a4fd87cbe8 | -10.83779 | -50.51082 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| df02e443-44d1-3ee9-87e1-83d93d82dabb | -9.87902 | -60.26697 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6633700e-8868-33f4-a6cd-ee7859507e5e | -8.78268 | -50.06295 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 51df1c64-ebbc-3095-a795-7e8c9215913e | -14.46941 | -58.51394 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b23d4751-7fd1-3dd4-84b9-ac132e470a1a | -12.2815 | -59.33156 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e5ab291-22fc-3fa6-a435-8486bf0a46d2 | -9.17901 | -59.61028 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7219294f-fe27-3efe-8782-158a9bfddcbd | -11.03267 | -57.24926 | 2026-08-28 17:45:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1d8f45-0f4d-3a19-976a-143f80b9382c | -14.18931 | -52.84516 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 11e9fcfa-2f94-3c0b-b6b5-07b94e3e8c06 | -14.39962 | -53.05498 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68ef9cb9-0312-32be-ab69-aade9abb66ff | -10.76882 | -50.62919 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 736bc478-cca6-3a7a-9ea5-91d70af3c873 | -10.08904 | -68.75466 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa8e458b-f14d-344a-a5cb-c106053952ee | -9.22721 | -59.77308 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4cb22af3-fa09-31c3-b91c-98e736317143 | -9.68591 | -65.10018 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| feeec435-6d0c-3cd9-8f2d-956b128a2581 | -14.16354 | -52.82096 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 507813d4-2609-3f0c-aa59-4e3218d55ff5 | -8.53517 | -55.26222 | 2026-08-28 17:45:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 237.3 |
| adf31ccb-2ca8-3c2e-823d-9dfc6a771423 | -10.0867 | -68.29326 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a60ca2a1-6aca-39db-b492-357c05ccadc4 | -10.40906 | -61.19841 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 637de50f-70d4-3022-a356-48518fde10c3 | -9.22655 | -59.76896 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 56336e13-cd5b-34a6-b9ec-b97788078622 | -11.21575 | -55.07724 | 2026-08-28 17:45:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 560c0bd1-b7dd-307b-8410-2eac8aa9050a | -9.17361 | -59.57679 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c7e93e4f-da67-317e-9bc9-646c1bd864bd | -14.41591 | -52.58219 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3352af13-764b-3b44-8a46-20b2bb439464 | -9.17812 | -59.55871 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2fb6770f-6e85-3513-a6f6-5a8af1b546d1 | -8.77168 | -50.07722 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6fbdfde9-2971-3880-a896-866b26534a1d | -9.10382 | -60.31888 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 658f0d3d-9cbd-3dcd-8bcb-9652cd8a21e5 | -14.18184 | -52.83366 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 11e9bac1-5705-367f-92fd-0e95384ad559 | -11.27492 | -54.03526 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| e14a0f6d-4e16-3e2d-9e0b-6937980e5dcd | -11.26744 | -54.02666 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| af381cf5-442a-3236-a07e-560623c497a5 | -9.86261 | -65.04614 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8f45f2b6-f692-3c02-87c5-58dfd89829be | -14.50023 | -52.16041 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c316c1b5-4fc1-34e4-b42f-0d6befd1bcdd | -9.1754 | -59.61086 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3fb6cd33-c217-3520-b132-4ca3d11630c3 | -9.85563 | -65.04718 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c655c014-4580-3a97-98a3-dbb4804daccc | -12.38663 | -48.19668 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b3b9badb-b508-3d3f-bcc8-b5d4eab187da | -9.86204 | -65.04224 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 73e05fe7-2cc8-3fc4-988d-e524defd165f | -14.47298 | -58.51332 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 967b6e98-af11-359d-960f-56f1ffe5d33b | -10.83353 | -50.50889 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 15e96802-c863-3f06-9e94-222325313910 | -10.3159 | -68.45572 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ad45a009-3f0e-301f-b2eb-7adc9b96346f | -11.03579 | -57.21919 | 2026-08-28 17:45:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d36a5e82-5f47-37bc-9dcf-9dd8c61a4a28 | -10.25844 | -64.49843 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58b94f18-25dd-3dd1-96c4-ace76e92cf65 | -10.84303 | -50.50461 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0130a150-191f-3f16-a4a8-8b31fa89e4cc | -10.47336 | -64.4858 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2977b4d7-3a88-34c7-ab8d-08c25f681a8c | -13.10923 | -50.04838 | 2026-08-28 17:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| dc669cfe-9ebd-39c2-82c9-f4751198e18c | -9.20078 | -61.09213 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a57a0797-fabb-31d9-bb11-d97a1f28507a | -9.02304 | -57.54124 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 731c5ffd-f14b-341f-88b6-90412a01cfa3 | -14.65813 | -56.99716 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3e16e04f-c8a2-3519-a73c-5563b6645739 | -11.19675 | -51.25863 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0a062073-2584-328a-bec5-5dd7e77f56c8 | -10.76269 | -50.64175 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5950caf-adba-33d0-82ba-20cc8f9d1998 | -10.30959 | -69.13283 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dc023b98-c8b0-3db1-9d20-b9a3b7423ba7 | -14.46702 | -58.5134 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| cc14b838-10a8-30ad-917d-9317dc77b42f | -14.93027 | -52.61335 | 2026-08-28 17:45:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89d653aa-6ce2-38bc-85c1-d3e74b1be0da | -9.05969 | -58.99187 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 594a3987-12c3-3e84-891b-6c5db73f253d | -10.05015 | -68.82862 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 5544c090-958a-349b-b25f-664d1dbd3dfe | -8.80522 | -50.49458 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b3931014-1490-31bd-832a-69c4fcb5b5ac | -8.58871 | -54.77897 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 70368089-9df4-3f6a-b7e5-4269f9ab45d9 | -13.41093 | -51.76826 | 2026-08-28 17:45:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 16bfd188-3135-3a56-829a-2e777193881a | -11.26639 | -54.02087 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 0d80eb3f-caea-3f2e-868c-6cb8f1ec1651 | -14.51963 | -56.50605 | 2026-08-28 17:45:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5e9bd6b9-e855-3bbd-86ba-46533ca2746e | -11.90957 | -49.99777 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9c2b5099-c310-3046-b616-c0af8d8d4188 | -10.44599 | -59.60873 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 50c1e7d9-bd6c-3728-a108-53033d289302 | -10.31022 | -68.45358 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c31b1fa8-adb6-3b7b-91e4-54ba7343a91b | -14.86404 | -52.62646 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0ee1de6b-5ee5-31f1-a536-6a7c559e3ea1 | -14.23726 | -51.76609 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a812dd53-0d5c-37a4-b325-75e661cc7ad1 | -10.51675 | -59.61792 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f4347dc9-f9b7-33e5-8a01-6153e31a86a0 | -14.59834 | -53.14529 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6c1cc5fb-c1a8-33fc-9b06-e71d6d40ca04 | -14.40521 | -53.05703 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68c226fa-f0cc-3338-9054-5b45032bc7da | -8.21317 | -54.95998 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 161c3517-fa6b-3612-97c6-0501bde3e915 | -10.33924 | -50.37959 | 2026-08-28 17:45:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| be36d0b2-8d8e-34e2-a00a-b17a62283e11 | -15.60284 | -56.38732 | 2026-08-28 17:45:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83ac24cf-bb2e-3cef-ac80-fc1ff19fd33d | -14.91407 | -52.61163 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cc74a094-6a59-39ad-8ea7-09b02a879a72 | -14.18244 | -52.8368 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 373054fc-6545-3670-8f92-61d503045008 | -9.96903 | -53.93864 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 4bbabeef-c83a-39f8-8bd1-e030ab0e8a2b | -9.7614 | -64.97328 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| ce923776-be36-3cd1-9777-15e7ff5ebcff | -8.67425 | -49.53772 | 2026-08-28 17:45:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e4b6dffc-21ee-3355-bbcc-8f527322a53f | -14.19946 | -52.84301 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb5406df-db80-3937-9602-92e9fd7fb9cb | -14.17674 | -52.83463 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f16ab5ec-a1fd-31df-b958-483aeeade5fc | -14.33313 | -53.22011 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f6a8ee6-f3e2-3163-909c-d37c16ec7457 | -10.99944 | -49.64137 | 2026-08-28 17:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 87c3f23d-2506-34f5-bc28-34bffd722b66 | -9.97412 | -53.93766 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| af102b9c-b4c8-34fa-b4f5-e5839e237be9 | -11.19439 | -55.0913 | 2026-08-28 17:45:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e7f64463-4a2b-35a8-8387-3f18dbbdc0ae | -9.96847 | -53.93553 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5f7ee43e-f09e-3495-9796-ef80312f5886 | -9.93858 | -60.43871 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 20ea2f5c-d929-3ea7-b2c7-424724d444bc | -10.07258 | -69.12522 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7261db78-e812-33dd-9bf3-287922665dd2 | -9.96552 | -53.93317 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b82c6f50-715c-3755-88ef-fba4dcf86789 | -14.44332 | -53.38651 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c853f89e-0f43-3705-ae70-460c5dd30341 | -9.13588 | -60.924 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cbb95cd1-696e-3c2e-9b86-b7726601f0f4 | -11.27137 | -54.02004 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| b69513fa-fbbb-36df-8a4d-213034688337 | -14.60782 | -53.14548 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1fee3949-5ce7-3cf5-8fc4-37031729b64a | -9.85507 | -65.04327 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 96bd6af9-f19f-3d92-aea5-991e76132714 | -8.23634 | -54.9659 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 240ce463-ecbb-3023-a912-8f81c21a4909 | -14.45311 | -53.3847 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a53f954c-839c-30ef-bae8-97171fb4e3f6 | -10.07126 | -69.12691 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README140.md)
