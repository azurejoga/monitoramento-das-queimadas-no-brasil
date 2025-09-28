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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3be392a6-d336-3f0e-b8ca-829f022f5ea0 | -10.75632 | -45.38709 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08764b5a-20b9-378f-ad68-c6cf47dd89d5 | -6.3978 | -43.52888 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c97fef72-aced-3cf1-bb7f-0042d4271819 | -9.06922 | -45.5404 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a94aa80-f6e0-3381-94ed-68d630aecc14 | -11.9839 | -47.89283 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e451118-397c-344f-8332-b9ecbc2e1c48 | -5.82896 | -45.59377 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a65afc3-567d-37d7-a800-bbe9b3dff95b | -10.59074 | -46.27723 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4045c406-378e-3981-9f35-d3db52b36aa6 | -11.36297 | -44.95161 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e99f1a8a-6af9-3384-b52c-dbcb1a9398d6 | -6.0711 | -43.77293 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fad60415-6b60-35ae-be24-c7c6447bf079 | -12.90211 | -45.16285 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da389b08-8b4f-3274-97c2-43daab311039 | -8.94591 | -48.66473 | 2025-09-28 04:25:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b682f04-ba87-3b2a-af67-47f1f9634bb5 | -7.77757 | -47.02137 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef0567bf-7f9e-32d8-9220-ab1a24036241 | -7.24674 | -44.75491 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de53e2c8-1ef2-3296-8046-879901a43eb3 | -7.15222 | -45.51111 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e049146c-f448-3e46-8ef3-3924c8197b6d | -5.64244 | -46.3893 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cef7c76-1d95-35dc-9b64-9eaadabd049c | -12.00836 | -47.97272 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8fedcd75-e616-3a2f-9f8d-b2bebdd66626 | -7.8067 | -47.0081 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6d7c1fba-6702-3ff6-973c-47eda51923ff | -12.89569 | -45.15782 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e43887d0-3dc6-3162-b064-517d620313ed | -5.90252 | -43.29169 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1dbe0de-891b-3b60-8e3a-2baa70fdbbb4 | -6.6527 | -43.87728 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c99e14fc-f0ad-39e9-b1eb-bb19f5869fa1 | -12.90737 | -45.15149 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59483634-8333-37a2-b78e-c6444bd20889 | -12.00786 | -47.95451 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 692b8fc7-f5de-3694-8afd-8d78067fa412 | -10.91828 | -44.29692 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e83dc5e-cee3-3f00-abb5-2136848679a0 | -12.01575 | -47.9051 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c29c222-d52a-3d6a-9af1-0274eaf89fcf | -9.54634 | -47.77388 | 2025-09-28 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f79b9844-9436-3abb-9b3d-af2887eb837b | -10.53706 | -43.62457 | 2025-09-28 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 49f8a102-10d6-3906-b498-2408fbfd22fb | -7.2315 | -44.76369 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ee840ce-b03f-3e20-bb3a-a6ec4c53d637 | -8.29056 | -45.4378 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 689d6a5b-5ef9-36db-80f2-bfb82e8a12cb | -5.95109 | -42.89732 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ebdfada3-4978-35e9-93c1-319931d4cb02 | -6.0576 | -44.86459 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32e194db-3bf9-31d9-8a07-69b0673f49ca | -6.15667 | -43.87542 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a58d9c7c-a172-3ddb-8f75-950979b84866 | -7.37536 | -47.02858 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 124e21bb-93f3-3fca-a3a9-2d63d950b237 | -8.81896 | -46.013 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 798afcef-f90c-30e2-8013-7d9bb583b430 | -11.37112 | -44.96865 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06058837-f50a-39a4-8b88-5f19684323f6 | -12.24565 | -47.18082 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71e92951-7b8e-3c1e-954d-27969fd35c77 | -5.73642 | -46.18108 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f89946e3-b266-3b0d-ab5f-e23e63057a64 | -6.92388 | -44.6459 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 215746b1-10d0-36fd-90a7-269c41bae4a0 | -12.02231 | -47.92796 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c214674-73f2-3e22-8bb9-dc60a1c3fa03 | -6.69683 | -42.73494 | 2025-09-28 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d54922d6-bca8-3c15-bdbe-0a4eda43ae18 | -6.70261 | -44.60513 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbc5cf92-c731-3987-b590-b1b16e14938b | -6.53974 | -43.82619 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d9b706b-3230-3fe1-8694-772c449ca8de | -7.38923 | -46.70631 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f9b4100-2a5e-3b4c-be36-4d8b815dc481 | -7.23432 | -44.76788 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f578af98-9dde-3415-93ed-b78a43cd9f01 | -12.93721 | -45.11942 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 818ec087-b214-33d8-baab-606e0edd1921 | -8.82548 | -46.21157 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 919520b6-c3da-304e-bfa1-e92fa11a420c | -5.84228 | -45.8759 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f27fd0dc-640c-3bc4-93f0-ade47f7f1ccb | -9.11332 | -46.67153 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75c95cdc-08af-3b28-ba5d-9384934eb500 | -6.31712 | -43.4655 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4454a0b5-5e63-3d1d-9b46-2bac28179f6d | -12.84703 | -46.89255 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cc780a0-49a7-36a9-9d1d-f58b820a00eb | -12.90619 | -45.15942 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fac6f319-b120-353a-9334-9db82b79ae19 | -5.48157 | -45.38305 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84af3e08-56d0-3e8a-8997-d3ac3f190712 | -7.82308 | -48.80073 | 2025-09-28 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c73571-5887-3a8f-a98b-266de22da144 | -11.35269 | -45.04528 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea33605b-7764-3cf6-b551-b28e6f885d45 | -11.38211 | -44.96652 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efdb6176-2272-367f-a6e6-64694973d019 | -7.79344 | -47.00599 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cdb83cba-b1f7-3c1e-8a4b-dbf1d8b86590 | -8.17713 | -46.38349 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da9441ee-0dab-3a0e-8169-673f05cb9544 | -6.26958 | -42.4954 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 175eb2e9-eb8d-36d6-9e65-3b7826bf5112 | -7.77701 | -47.02486 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e93920d9-9386-3d5f-b6fa-b9b11a366fe4 | -8.65562 | -43.99001 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c037818c-10cf-3a86-83ec-2d062384a36d | -9.28545 | -45.70156 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42a59bbf-5d57-3bab-b8ce-f23d4bfaa197 | -8.17337 | -43.34903 | 2025-09-28 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b276c61-9143-3eca-8f8c-6e3cd1dfe35b | -10.12923 | -45.32225 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93a009e4-269a-3211-ac51-24c4d4582474 | -7.28226 | -45.81126 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ff6cffd2-8fde-3fdb-92ee-a0862fc9c280 | -12.90035 | -45.17474 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7fca49e-048d-391d-9f28-296e30ab939f | -12.54164 | -48.29348 | 2025-09-28 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d884114f-88ab-3ef8-ad9e-e4c291b7f588 | -10.02685 | -52.12232 | 2025-09-28 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5368046a-f83f-3163-a96f-d1cc6e3bafc7 | -10.10526 | -45.33745 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 322cff0e-7f01-3f16-a1e9-ce350434436b | -7.33927 | -45.49015 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6418e484-c56a-3f0e-a582-5cdb937d9e29 | -6.48562 | -44.24033 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 093ba0ec-cc47-382b-85cc-6d850da64ef9 | -9.28991 | -45.69495 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91259b1d-4576-39cf-ba53-6aa2fad608c4 | -10.8194 | -45.38512 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53aa86ed-433a-3777-8b1d-2af1e4fa7c0f | -8.29001 | -45.44137 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4026ab26-691a-3b1d-9e27-0051693e6374 | -6.57573 | -43.73913 | 2025-09-28 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4389b99-ac4d-34ef-9b31-7c151aba2932 | -8.71744 | -47.97974 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa93733a-603c-3e81-b41f-942430bad2e9 | -12.00324 | -47.03724 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 931bf52c-c4d2-35a2-a794-e0c98bacfb2b | -9.21882 | -46.77747 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79ee4fbe-4dd0-3e90-8d74-04fa6dbd8e38 | -9.03756 | -49.09224 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea758372-b009-3a2c-8378-de2044bb7eea | -11.4286 | -44.91733 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3da9fd65-9822-3014-aeb3-424fe3f6abde | -6.42982 | -42.91713 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| bd5376d8-caed-389c-9c7d-0582c962f78b | -9.0091 | -47.83965 | 2025-09-28 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88536518-c260-3cf5-a5d3-8cf0183c8f73 | -5.93168 | -44.24454 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b602b9a-ba67-3dbd-8e46-6c60277e5c89 | -10.94777 | -47.78476 | 2025-09-28 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9901a5fc-7e92-3ac7-aee4-7bf23a8592a0 | -8.71843 | -50.05346 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b86a250-73d0-373d-af8c-63c8fe38f8a9 | -12.97913 | -46.85141 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25788d26-8621-3439-8b4e-f3b46c8a70d4 | -5.73588 | -46.18453 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74b17472-8a17-3a10-a802-5dc9f2bf3c0f | -5.88393 | -43.1981 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ac66d1ef-30a0-3e78-bd53-a38ccfb271e7 | -10.29466 | -45.42705 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b93c52f3-185b-3a42-bec3-caadbbef54a7 | -7.0058 | -45.62495 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b08e493-0e38-319e-80e5-c298fe25509c | -7.23809 | -47.6803 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e18e1bc9-6137-321a-8b7b-d7e322cd7877 | -7.95773 | -46.26714 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87784dd8-e357-3b95-afb7-f51306d50efd | -9.21827 | -46.78095 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2500eeb-6d3b-39b1-ba18-e61d2653a992 | -12.00553 | -47.99039 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c090a0fa-c45a-3da9-a8a6-39f58d02226e | -5.82391 | -44.44572 | 2025-09-28 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8ad9724a-b223-30bb-a6db-95fbc527adce | -11.98499 | -48.01239 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 187f2e00-02a3-3514-9e4c-8d5f6baadc8e | -6.74855 | -44.71964 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56253ce3-c9f2-323c-9f5f-32da7c01f31e | -12.28138 | -44.04727 | 2025-09-28 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 507fd7c1-48eb-3f3a-94d8-ca20b8cc78ae | -12.10224 | -44.20067 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 237e68ac-c1ad-3652-b9cb-62ae4eb46fc9 | -9.29424 | -43.21818 | 2025-09-28 04:25:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 205da292-a4a6-3f16-88c3-859d4e357a47 | -10.31364 | -48.19812 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bf905a7-7882-3c5f-a536-c1d5e0310b10 | -7.2529 | -42.98519 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e870cf1c-deff-3aa4-a8fd-b568c7e53b82 | -6.69866 | -44.60823 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README68.md)
