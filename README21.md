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
| 1294a5e6-4e9e-31cf-94cf-9bf4e04eb75d | -11.79605 | -46.38941 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b70cb37d-12f4-3968-b148-56b43fe3a4d7 | -8.57549 | -54.56763 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b69224f7-bc62-3932-b788-f3b3ddf353ed | -12.85544 | -44.38989 | 2026-09-12 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fcae7824-7e05-3195-ab0b-3fd06645d268 | -8.99761 | -50.86193 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e1ee8b1-dee1-3170-af1b-3a9379e33577 | -7.41764 | -46.14974 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fa953c3-f54e-3518-85c4-07e2ab1e3d41 | -9.4662 | -50.31298 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62199863-3538-3cc3-97ef-8b75d836ebcd | -11.80374 | -46.38645 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01016900-c7fb-30c7-bd5e-77ba95f8a158 | -7.62078 | -46.67994 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4420ea60-a2a5-30ba-831c-0e659fa1683d | -6.52177 | -47.6117 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e9e29e5-350e-311a-b1f0-c8f0251aef3e | -9.31984 | -45.64144 | 2026-09-12 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e71e76d2-f79e-3f87-98bd-f42169f17cc4 | -4.87388 | -56.00802 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ead22f1-085f-3db9-bde6-4a2cacebbae2 | -6.61761 | -51.14524 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 723b717e-46de-38a6-8345-0911fb844e6a | -5.83116 | -53.79387 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2bc74ca-1999-3cbd-8943-8472527ec58d | -11.37573 | -46.83546 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ae842fa-66ad-3438-aa64-16b413b97edd | -9.36924 | -48.41297 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfbb67fb-ca04-3451-9039-225ef184e5b8 | -6.11336 | -52.24213 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9854dc65-1dab-31dc-bf9e-5772c37c6207 | -12.41572 | -40.92131 | 2026-09-12 04:34:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6cfd88b4-c77b-342b-be0f-4459c37ecf82 | -6.79756 | -58.7937 | 2026-09-12 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e136250-7a84-3782-9b51-2729bd5112db | -12.6478 | -51.42469 | 2026-09-12 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4dd2c39-ea90-3da6-a937-fe858bd1cec4 | -11.24205 | -54.1293 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a7b1bb1-e068-3adf-9a82-cb667158e0e5 | -6.18679 | -57.71862 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d986d724-11f5-34e0-9205-eaed6bcb5e75 | -10.53844 | -51.36602 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e163a6f-c22d-312f-b5c0-8925d2e8d175 | -8.82655 | -46.02407 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfb7030a-f565-3be1-8d04-e83cd6241830 | -10.55104 | -51.37628 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec741650-c87d-3916-a674-c9a3bece7d63 | -6.31382 | -55.14833 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5c697b0-0386-3c2b-9203-c6be92805a62 | -9.18435 | -59.4502 | 2026-09-12 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c782b33b-d607-3662-a649-91a1c986f5e5 | -9.3687 | -48.41645 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8911acfd-4e99-39be-9182-2dc8cdf0d133 | -11.27092 | -47.67153 | 2026-09-12 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bd8fcbe-1265-3d83-8874-029af20ce25a | -11.23744 | -54.13213 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae7c8cfc-269e-38f5-8ae7-29b856ce94b3 | -10.29303 | -49.9986 | 2026-09-12 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 433ba8cb-917e-3a03-b866-de4d629dc2f8 | -6.86155 | -47.43648 | 2026-09-12 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1393c58c-77d1-3e59-88d3-cb7a4f76eb3b | -7.3078 | -45.99339 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a197ff-d609-3108-8185-f918d2a3604a | -12.37957 | -47.38586 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 037f59d5-2090-3853-9fc9-5b6eac7ca17a | -12.85496 | -44.39346 | 2026-09-12 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 09d53780-41d4-3dec-8999-ba38a82381a9 | -9.72844 | -54.81421 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1521b101-d228-3935-a7b8-44f4d2c4ebb0 | -8.53604 | -54.71811 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b7b507cd-87dd-37ad-a2c5-e1a848bbc318 | -10.54759 | -51.37555 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 620d25c1-5b2d-3842-95f2-15e8ab7b5f58 | -8.57908 | -54.57238 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7f3f411-17a9-3939-91f3-da358e153d67 | -11.43376 | -51.43682 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2cbbceb-31eb-3b2e-9d0c-e299d000e8ae | -9.69798 | -43.40038 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| be8ae542-35f5-33d6-acb5-362afd1275d9 | -4.85938 | -56.00199 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8d39143-7c9b-3bd9-8d84-b8eec86832a1 | -6.24261 | -51.69286 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd2e3113-8926-34b3-bdd8-785193067968 | -5.85151 | -52.11313 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec203030-d18a-3458-8413-6a4ca0120dc0 | -7.09665 | -55.41758 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fd89ace-25fc-3018-adfa-0396d049c5f4 | -10.14611 | -36.20014 | 2026-09-12 04:34:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e75a26b7-92fd-3e34-b05d-51702241be96 | -11.23713 | -54.11045 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eaafe57-eb53-32b2-872c-b12b7587bb06 | -11.66859 | -50.67883 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8a1963-8759-337f-8002-dc06a33660ed | -6.86075 | -55.25878 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 983f4097-cba8-3433-9d30-e4942ce78e05 | -8.57409 | -54.57572 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fb785c3-32c3-34d4-b66f-b85dd48708db | -6.95696 | -44.5417 | 2026-09-12 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d072cf73-e2a5-35bb-b355-6d6033d82f4f | -12.26996 | -48.58073 | 2026-09-12 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7237f0ea-b11d-38c6-b18c-b355d1248cb1 | -5.86366 | -51.64072 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db862574-588d-30f3-abc2-1256800ce1e2 | -11.3503 | -45.78905 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61bb3539-1764-3d23-8e82-b31bb19b569e | -11.20997 | -45.40883 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb534da0-a49d-31b8-99b4-2a38cdd79731 | -11.08072 | -50.83992 | 2026-09-12 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9cc01f5f-77c6-312b-8cd6-080d9a666805 | -9.23561 | -51.73501 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8f9f0d-bdd6-3954-b983-ab2928f9010b | -10.14334 | -36.20421 | 2026-09-12 04:34:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6fd0dfb7-59ed-35bd-80d7-7ac3302573e0 | -6.11718 | -52.24283 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50df6d82-b884-3700-abb8-a3364e5e42a0 | -6.61829 | -51.14106 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37e5e8b5-3448-3fb0-b0ec-3dbdac7e59ef | -7.15149 | -42.10059 | 2026-09-12 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 74c34eaf-a25c-387f-9f48-8c14567040e1 | -6.03945 | -52.22155 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01431513-e8e7-38b3-9d33-55caab566420 | -9.71135 | -43.39478 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 928f7c69-cdcc-336c-92df-ab90bc9787c2 | -7.15032 | -42.10884 | 2026-09-12 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd826e78-5201-39bc-b1ae-c286c5d94de0 | -8.82597 | -46.02797 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f59363-ceb5-3582-9a44-8e63aa6c9b31 | -10.53947 | -51.33798 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16fda2e7-834b-3385-96da-4792b9432ea5 | -10.48911 | -51.36197 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd4bb632-04e8-3219-afcc-8d89c241d1bd | -6.11173 | -55.63843 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6655e20b-4a96-3797-9ac5-bec8b7d466aa | -12.12451 | -48.97424 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 663f1175-4793-3644-abb3-fc5bab11791f | -5.82424 | -53.80941 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d24f8306-f2cc-3d0e-9f94-fafad0361a6a | -13.43534 | -43.81324 | 2026-09-12 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17952402-dede-346a-96f1-b844aee91e79 | -7.11403 | -55.1271 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7122152-05a3-3953-ba80-ff505a51d481 | -6.88288 | -55.65014 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fdfc4442-6dde-379f-8240-b613744a5de5 | -11.23652 | -54.11394 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8beac7-3fd5-3b32-94c7-2125f9bea31a | -11.35332 | -45.79393 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a76e562-9f55-3601-8724-a3db4cdd93d3 | -9.71369 | -54.34877 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c161cea-7ded-3c0d-9d79-d2c3fdc6d480 | -11.03958 | -49.69112 | 2026-09-12 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01392d58-63b9-3d3e-9432-63d938127bc7 | -10.48564 | -51.36137 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a933636-4fa2-3fc8-bb26-38ff908e64c9 | -10.8222 | -50.58942 | 2026-09-12 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4290abe-935d-3e7d-88b7-d615e881c470 | -9.70886 | -54.35197 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31aee123-ff24-3b9f-ad1b-9d70c96fb1ed | -9.52691 | -40.33365 | 2026-09-12 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 672ad74b-c33c-3cd7-b4b4-47afda741617 | -4.87294 | -56.01355 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 59afb5d4-8cac-34b0-a634-9e6fe9d7fdef | -6.11106 | -57.63327 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dffe2a2-7ac8-3fde-80ee-2ac1a761072a | -11.23955 | -54.14353 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea21dcd-19fc-39ee-a48d-28f5729ae743 | -12.13108 | -48.95368 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a592d51-a7a7-3967-88bc-9d1cf83d0ce9 | -10.92443 | -48.49084 | 2026-09-12 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e44bf261-5891-37cb-a6d5-33e66407d269 | -6.50943 | -47.60197 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a7ca811e-9787-30aa-a8a8-fdb02775b1b8 | -6.88464 | -55.63991 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12b22204-2137-3a71-b82a-e5894ef5e93e | -5.79242 | -53.81633 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b26da4ac-280d-3890-8807-6b9df7808244 | -12.12007 | -48.95911 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 458e822a-7219-39f1-8aa8-c812505ad034 | -10.04868 | -46.26868 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad55c706-c478-306c-8935-c45237ce7cbc | -6.96065 | -44.54225 | 2026-09-12 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8493f87b-a65c-3987-8b12-095793620936 | -9.15935 | -49.98454 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeed263d-25ec-3a64-a213-77810a28fb85 | -11.2056 | -49.00265 | 2026-09-12 04:34:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2986cf4f-da23-364e-9a5c-60c5f588bb29 | -6.33943 | -55.30878 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c811547-4b7e-3f99-aca5-3474a54e2ec7 | -8.44184 | -47.52803 | 2026-09-12 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5a97fce-1dbd-35d9-9269-692f2678176d | -6.61875 | -58.85196 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ade0d371-f39b-3fb0-85ad-7afd6e44eff3 | -7.18679 | -45.91837 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05706ae6-daf1-35d8-81e7-cb29134eae4f | -10.54704 | -51.33527 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede15c58-a8f6-34ef-aef8-5155f6fcf2c7 | -6.61796 | -58.85635 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed11b254-9386-393b-b1cc-f0c642bceada | -11.3763 | -46.83158 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README22.md)
